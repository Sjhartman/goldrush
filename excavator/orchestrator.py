"""
excavator/orchestrator.py

Reads an IRB audit JSON produced by data-claim.py and generates
Databricks SQL extraction scripts by coordinating the specialist modules.

Script numbering (goldrush):
  1 -- cohort definition
  2 -- patient demographics
  3 -- address history (only if addresses approved)
  4 -- clinical outcomes + pathology notes
  5 -- Tempus genomic data (only if Tempus elements approved)
  6 -- attrition report (deterministic Python, no API call)

Usage:
    venv/bin/python excavator/orchestrator.py <path_to_audit_json>
    venv/bin/python excavator/orchestrator.py <audit_json> --materialize
    venv/bin/python excavator/orchestrator.py <audit_json> --tempus-codes XT,XF,RS,XO
    venv/bin/python excavator/orchestrator.py --amend <audit_json> "add zip code to demographics"
"""

import json
import os
import re
import sys
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from pathlib import Path

import anthropic

# Add parent dir to path so relative imports resolve when run as a script
_here = Path(__file__).parent
if str(_here.parent) not in sys.path:
    sys.path.insert(0, str(_here.parent))

from excavator import cohort, demographics, addresses, clinical_pathology, tempus_databricks, tempus_catalog, attrition, cohort_temporal_diagnoses
from excavator.shared.embedding import (
    embed_cohort, normalize_cohort_sql, normalize_extraction_sql,
    _collapse_comment_blanks, strip_fences, strip_cohort_prefix,
)
from excavator.shared.databricks import run_quality_checks
from excavator.shared.schema_validation import (
    load_actual_schema, load_tempus_schema, build_tempus_schema_context,
    validate_sql, fix_sql_errors, build_fix_log, validate_tempus_sql,
)
from excavator.validators import irb_auditor, contract_checker, clarification_checker

GOLDRUSH_DIR    = Path(__file__).parent.parent
SCHEMAS_DIR     = GOLDRUSH_DIR / "schemas"

# Keys for the per-table Tempus SQL outputs (Script 5a-5f)
TEMPUS_TABLE_KEYS = ["orders", "specimens", "biomarkers", "cnv", "fusions", "rna_findings"]
INDEX_FILE      = SCHEMAS_DIR / "index.md"
INDEX_BRIEF     = SCHEMAS_DIR / "index_brief.md"
CLEAN_SCHEMAS   = SCHEMAS_DIR / "clean_schemas"

MODEL                     = os.environ.get("ANTHROPIC_MODEL", "claude-sonnet-4-6")
TEMPUS_DEFAULT_TEST_CODES = ["XT", "XF", "RS", "XO"]

# Tables that trigger the addresses specialist
_ADDRESS_TABLES = {"PAT_ADDR_CHNG_HX", "PATIENT_ADDRESS", "ZC_STATE", "ZC_COUNTY"}

# Tables that trigger the clinical_pathology specialist (always included)
_PATHOLOGY_TABLES = {"HNO_INFO", "HNO_NOTE_TEXT", "ZC_NOTE_TYPE", "ZC_NOTE_TYPE_IP"}


# ---------------------------------------------------------------------------
# Load and normalize audit JSON
# ---------------------------------------------------------------------------

def load_audit(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def extract_fields(audit: dict) -> dict:
    result = audit["result"]
    val    = result["validation"]
    return {
        "irb_summary":        result.get("irb_summary", {}),
        "request_summary":    result.get("request_summary", {}),
        "approved":           val.get("approved_elements", []),
        "denied":             val.get("denied_elements", []),
        "ambiguous":          val.get("ambiguous_elements", []),
        "icd_code_analysis":  result.get("icd_code_analysis", {}),
        "exclusion_diagnoses": result.get("icd_code_analysis", {}).get("exclusion_diagnoses", []),
        "consistency_checks": result.get("consistency_checks", {}),
        "reviewer_notes":     result.get("reviewer_notes", ""),
        "rdc_authorization":  result.get("irb_summary", {}).get("rdc_authorization", {}),
    }


# ---------------------------------------------------------------------------
# Classification (two-tier: brief index then full schemas)
# ---------------------------------------------------------------------------

CLASSIFICATION_SCHEMA = {
    "type": "object",
    "properties": {
        "clarity_elements": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "element":   {"type": "string"},
                    "rationale": {"type": "string"},
                },
                "required": ["element", "rationale"],
            },
        },
        "gap_elements": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "element":     {"type": "string"},
                    "gap_reason":  {"type": "string"},
                    "future_note": {"type": "string"},
                },
                "required": ["element", "gap_reason"],
            },
        },
        "tempus_elements": {
            "type": "array",
            "description": "Elements from curated.tempus SQL tables: CNV, MSI, TMB, HRD, RNA fusions, clinically reported variant classifications.",
            "items": {
                "type": "object",
                "properties": {
                    "element":          {"type": "string"},
                    "rationale":        {"type": "string"},
                    "suggested_tables": {"type": "array", "items": {"type": "string"}},
                },
                "required": ["element", "rationale"],
            },
        },
        "tempus_catalog_elements": {
            "type": "array",
            "description": "Elements from Tempus catalog TSV files on NFS: raw DNA mutations (somatic/germline), allelic fraction/VAF, RNA expression/TPM. These are NOT in Databricks SQL.",
            "items": {
                "type": "object",
                "properties": {
                    "element":   {"type": "string"},
                    "rationale": {"type": "string"},
                },
                "required": ["element", "rationale"],
            },
        },
        "tables_needed": {
            "type": "array",
            "items": {"type": "string"},
        },
    },
    "required": ["clarity_elements", "gap_elements", "tempus_elements", "tempus_catalog_elements", "tables_needed"],
}


def classify_and_identify(client: anthropic.Anthropic, fields: dict) -> dict:
    """
    Two-tier classification:
    - Pass 1 (cheap): index_brief.md if available, else index.md
    - Pass 2: full clean_schemas/ for candidate tables

    Returns dict with clarity_elements, gap_elements, tempus_elements, tables_needed.
    """
    approved_text = "\n".join(f"- {e['element']}" for e in fields["approved"])
    request_context = json.dumps({
        "irb_summary":        fields["irb_summary"],
        "request_summary":    fields["request_summary"],
        "icd_code_analysis":  fields["icd_code_analysis"],
        "consistency_checks": fields["consistency_checks"],
    }, indent=2)

    tempus_schema     = load_tempus_schema()
    tempus_schema_ctx = build_tempus_schema_context(tempus_schema)

    # Choose index file: prefer brief for token efficiency
    index_file = INDEX_BRIEF if INDEX_BRIEF.exists() else INDEX_FILE
    index_text = index_file.read_text(encoding="utf-8") if index_file.exists() else ""

    prompt = f"""You are a data engineer classifying IRB-approved data elements.

Classify each element into exactly ONE of:
1. CLARITY: answerable from curated.epic_clarity.* (EHR data)
2. TEMPUS_SQL: answerable from curated.tempus.* Databricks SQL tables
      -- CNV / copy number variants
      -- MSI (microsatellite instability), TMB (tumor mutational burden), HRD
      -- RNA fusions / gene fusions
      -- Clinically reported variant classifications (somatic/inherited reported tables)
3. TEMPUS_CATALOG: in Tempus catalog TSV files on the NFS cluster (NOT in Databricks SQL)
      -- Raw somatic DNA mutations / SNVs / indels (accsn_variant_somatic.tsv)
      -- Raw germline DNA mutations (accsn_variant_germline_filtered.tsv)
      -- Allelic fraction / VAF / variant allele frequency (embedded in somatic variants)
      -- RNA expression / TPM / transcriptomics (CPM_tables on NFS)
4. GAP: answerable by neither

Then list the Clarity tables needed for CLARITY elements. Be conservative -- only
include tables directly required. Stick to standard clinical tables:
  - Diagnoses/cohort: PAT_ENC_DX, PROBLEM_LIST, HSP_DISCH_DIAG, EDG_CURRENT_ICD10
  - Demographics: PATIENT, PATIENT_RACE, ETHNIC_BACKGROUND, IDENTITY_ID
  - Addresses: PAT_ADDR_CHNG_HX, PATIENT_ADDRESS
  - Mortality: EXTERNAL_DEATH_REPORTS
  - Staging: V_CANCER_STAGING (supplementary only -- poorly filled in this environment)
  - Research enrollment: ENROLL_INFO, CLARITY_RSH
  - Treatment plans: TPL_INFO
  - Clinical notes: HNO_INFO, HNO_NOTE_TEXT
Add ZC_ lookup tables only for columns that will be decoded in the SQL.

Known unavailable tables and substitutions:
  - HSP_ACCOUNT -> PAT_ENC_HSP
  - ZC_LINE_OF_TREATMENT -> use line_of_treatment_c directly
  - ZC_RESEARCH_STATUS -> omit or use record_status_c directly
  - ZC_DISCH_CODE -> ZC_DISCH_DISP
  - AP_DIAG_CODES, LAB_CASE_ADDEND -> do not exist

REQUEST CONTEXT:
{request_context}

APPROVED ELEMENTS:
{approved_text}

CLARITY SCHEMA INDEX:
{index_text}

TEMPUS SCHEMA (priority tables):
{tempus_schema_ctx}

Return structured JSON matching the required schema."""

    response = client.messages.create(
        model=MODEL,
        max_tokens=4096,
        tools=[{
            "name": "StructuredOutput",
            "description": "Return structured classification result",
            "input_schema": CLASSIFICATION_SCHEMA,
        }],
        tool_choice={"type": "tool", "name": "StructuredOutput"},
        messages=[{"role": "user", "content": prompt}],
    )

    for block in response.content:
        if block.type == "tool_use" and block.name == "StructuredOutput":
            result = block.input
            result.setdefault("clarity_elements", [])
            result.setdefault("gap_elements", [])
            result.setdefault("tempus_elements", [])
            result.setdefault("tempus_catalog_elements", [])
            result.setdefault("tables_needed", [])
            return result

    raise RuntimeError("Classification call did not return structured output")


# ---------------------------------------------------------------------------
# Schema loading
# ---------------------------------------------------------------------------

def load_schemas(table_names: list) -> tuple:
    """Load clean schema markdown for identified tables. Returns (schemas, missing)."""
    schemas = {}
    for t in table_names:
        path = CLEAN_SCHEMAS / f"{t.upper()}.md"
        if not path.exists():
            continue
        content = path.read_text(encoding="utf-8")
        if t.upper().startswith("ZC_"):
            content = "\n".join(content.splitlines()[:30])
        schemas[t.upper()] = content

    # Always try to load pathology note schemas
    for t in _PATHOLOGY_TABLES:
        if t not in schemas:
            path = CLEAN_SCHEMAS / f"{t}.md"
            if path.exists():
                schemas[t] = path.read_text(encoding="utf-8")

    missing = [t for t in table_names if t.upper() not in schemas]
    return schemas, missing


# ---------------------------------------------------------------------------
# Gap report
# ---------------------------------------------------------------------------

def build_gap_report(fields: dict, gap_elements: list, missing_schemas: list,
                     tables_used: list, tempus_elements: list = None) -> str:
    irb       = fields["irb_summary"]
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

    lines = [
        f"# Gap Report -- {irb.get('pi_name', 'Unknown PI')} "
        f"(IRB #{irb.get('protocol_number', 'N/A')})",
        f"_Generated: {timestamp}_\n",
        "This report lists approved elements that cannot be answered from Epic Clarity, "
        "elements available in Tempus, and ambiguous elements requiring manual review.\n",
    ]

    tempus_els = tempus_elements or []
    lines += [
        "## Elements in Tempus (Not Clarity)", "",
        "These elements are available in `curated.tempus.*` and are extracted in Script 5.", "",
        "| Approved Element | Rationale | Suggested Tempus Tables |",
        "| --- | --- | --- |",
    ]
    for el in tempus_els:
        tables_str = ", ".join(el.get("suggested_tables", [])).replace("|", "/")
        lines.append(
            f"| {el['element']} | {el.get('rationale', '').replace('|','/')} | {tables_str} |"
        )
    if not tempus_els:
        lines.append("_None -- no approved elements require Tempus data._")

    lines += [
        "", "## Elements Not Available in Clarity or Tempus", "",
        "| Approved Element | Why Not Available | Future Integration |",
        "| --- | --- | --- |",
    ]
    for el in gap_elements:
        future = el.get("future_note", "").replace("|", "/")
        lines.append(
            f"| {el['element']} | {el['gap_reason'].replace('|','/')} | {future} |"
        )
    if not gap_elements:
        lines.append("_None -- all approved elements are answerable from Clarity or Tempus._")

    lines += [
        "", "## Ambiguous Elements -- Manual Review Required", "",
        "These elements were **not clearly approved** in the IRB protocol. "
        "Access is **denied** pending clarification.\n",
    ]
    if fields["ambiguous"]:
        lines += ["| Element | Reason for Ambiguity |", "| --- | --- |"]
        for el in fields["ambiguous"]:
            reason = el.get("rationale", el.get("reason", "")).replace("|", "/")
            lines.append(f"| {el['element']} | {reason} |")
    else:
        lines.append("_None._")

    lines += ["", "## Denied Elements", ""]
    if fields["denied"]:
        lines += ["| Element | Reason |", "| --- | --- |"]
        for el in fields["denied"]:
            reason = el.get("rationale", el.get("reason", "")).replace("|", "/")
            lines.append(f"| {el['element']} | {reason} |")
    else:
        lines.append("_None._")

    lines += [
        "", "## Clarity Tables Used", "",
        ", ".join(f"`{t}`" for t in sorted(tables_used)) or "_None_",
    ]

    if missing_schemas:
        lines += [
            "", "## Schema Warnings", "",
            "These tables were identified as relevant but had no clean schema file:\n",
        ]
        for t in missing_schemas:
            lines.append(f"- `{t}`")

    if fields.get("reviewer_notes"):
        lines += ["", "## Reviewer Notes from IRB Validator", "", fields["reviewer_notes"]]

    return "\n".join(lines) + "\n"


# ---------------------------------------------------------------------------
# Amendment mode
# ---------------------------------------------------------------------------

_AMEND_TOOL = {
    "name": "submit_amendment",
    "description": "Submit the amended SQL scripts.",
    "input_schema": {
        "type": "object",
        "properties": {
            "cohort_sql":              {"type": "string"},
            "demographics_sql":        {"type": "string"},
            "addresses_sql":           {"type": "string"},
            "clinical_pathology_sql":  {"type": "string"},
            "tempus_sql":              {"type": "string"},
            "summary":                 {"type": "string"},
        },
        "required": [
            "cohort_sql", "demographics_sql", "addresses_sql",
            "clinical_pathology_sql", "tempus_sql", "summary",
        ],
    },
}


def _run_id(audit_path: Path) -> str:
    """Extract the run timestamp from the audit filename (last __ segment)."""
    parts = audit_path.stem.split("__")
    return parts[-1] if len(parts) >= 2 else audit_path.stem


def _find_sql_files(audit_path: Path, out_dir: Path = None) -> dict:
    rid = _run_id(audit_path)
    d   = out_dir if out_dir is not None else audit_path.parent
    paths = {
        "cohort":             d / f"cohort_{rid}.sql",
        "demographics":       d / f"demographics_{rid}.sql",
        "addresses":          d / f"addresses_{rid}.sql",
        "clinical_pathology": d / f"clinical_pathology_{rid}.sql",
        "tempus_catalog":     d / f"tempus_catalog_{rid}.py",
        "attrition":          d / f"attrition_{rid}.sql",
        "temporal_diagnoses": d / f"temporal_diagnoses_{rid}.sql",
        "conversation":       d / f"conversation_{rid}.md",
    }
    for key in TEMPUS_TABLE_KEYS:
        paths[f"tempus_{key}"] = d / f"tempus_{key}_{rid}.sql"
    return paths


def amend_command(audit_path: Path, request: str,
                  tempus_codes: list = None, out_dir: Path = None) -> None:
    if out_dir is None:
        if audit_path.parent.name == "claim_out":
            out_dir = audit_path.parent.parent / "excavator_out"
        else:
            out_dir = audit_path.parent
    paths = _find_sql_files(audit_path, out_dir=out_dir)

    if not paths["cohort"].exists():
        print(f"Cannot amend -- cohort script missing: {paths['cohort'].name}")
        print("Run orchestrator.py without --amend to generate it first.")
        sys.exit(1)

    cohort_sql   = paths["cohort"].read_text(encoding="utf-8")
    demo_sql     = paths["demographics"].read_text(encoding="utf-8") if paths["demographics"].exists() else ""
    addr_sql     = paths["addresses"].read_text(encoding="utf-8") if paths["addresses"].exists() else ""
    clinical_sql = paths["clinical_pathology"].read_text(encoding="utf-8") if paths["clinical_pathology"].exists() else ""
    tempus_parts = [
        paths[f"tempus_{k}"].read_text(encoding="utf-8")
        for k in TEMPUS_TABLE_KEYS
        if paths[f"tempus_{k}"].exists()
    ]
    tempus_sql_e = "\n\n-- ---\n\n".join(tempus_parts)

    all_sql    = cohort_sql + demo_sql + addr_sql + clinical_sql + tempus_sql_e
    ref_tables = {m.upper() for m in re.findall(r'curated\.epic_clarity\.(\w+)', all_sql, re.IGNORECASE)}
    schemas, _ = load_schemas(list(ref_tables))

    index_text = INDEX_FILE.read_text(encoding="utf-8") if INDEX_FILE.exists() else ""

    audit  = load_audit(audit_path)
    fields = extract_fields(audit)
    irb    = fields["irb_summary"]

    codes       = tempus_codes or TEMPUS_DEFAULT_TEST_CODES
    like_parts  = [f"o.test_code LIKE '%{c}%'" for c in codes]
    like_block  = "\n               OR ".join(like_parts)

    t_schema    = load_tempus_schema()
    t_schema_ctx = build_tempus_schema_context(t_schema)

    schema_block = "\n\n---\n\n".join(f"TABLE: {k}\n{v}" for k, v in schemas.items())

    print(f"Amending SQL for: {irb.get('pi_name')} (IRB #{irb.get('protocol_number')})")
    print(f"Request: {request[:120]}{'...' if len(request) > 120 else ''}")

    client = anthropic.Anthropic()

    from excavator.shared.prompts import BASE_SYSTEM_PROMPT

    prompt = f"""You are amending self-contained Databricks SQL scripts for a governed clinical
data request.

AMENDMENT REQUEST:
{request}

CURRENT SQL -- SCRIPT 1 (cohort):
{cohort_sql}

CURRENT SQL -- SCRIPT 2 (demographics, self-contained):
{demo_sql}

CURRENT SQL -- SCRIPT 3 (addresses, self-contained{' -- not present' if not addr_sql else ''}):
{addr_sql if addr_sql else '(not generated for this request)'}

CURRENT SQL -- SCRIPT 4 (clinical outcomes + pathology notes, self-contained):
{clinical_sql}

CURRENT SQL -- SCRIPT 5 (Tempus extraction, self-contained{' -- not present' if not tempus_sql_e else ''}):
{tempus_sql_e if tempus_sql_e else '(not generated for this request)'}

AVAILABLE SCHEMAS:
{index_text}

{schema_block}

TEMPUS SCHEMA:
{t_schema_ctx}

RULES:
- Return COMPLETE updated SQL for each modified script; empty string for unchanged scripts.
- All Databricks rules apply: ASCII only, no trailing semicolon, no block comments,
  no DATETIME (use TIMESTAMP), DATE_REAL via DATE_ADD(DATE '1840-12-31', CAST(col AS INT)).
- If cohort logic changes, update the embedded cohort block in all extraction scripts too.
- tempus_patients CTE template if needed:
    tempus_patients AS (
        SELECT DISTINCT p.emrid
        FROM curated.tempus.`order` o
        INNER JOIN curated.tempus.patient p ON p.tempusId = o.tempusId
        WHERE p.emrid IS NOT NULL
          AND ({like_block})
    )

Call submit_amendment with the full updated scripts and a concise summary."""

    print("\nSending amendment request to Claude...")
    with client.messages.stream(
        model=MODEL,
        max_tokens=32768,
        system=BASE_SYSTEM_PROMPT,
        tools=[_AMEND_TOOL],
        tool_choice={"type": "tool", "name": "submit_amendment"},
        messages=[{"role": "user", "content": prompt}],
    ) as stream:
        response = stream.get_final_message()

    result = None
    for block in response.content:
        if block.type == "tool_use" and block.name == "submit_amendment":
            result = block.input
            break

    if not result:
        print("ERROR: Amendment call returned no structured output.")
        sys.exit(1)

    summary      = result.get("summary", "")
    new_cohort   = strip_fences(result.get("cohort_sql",             "") or "")
    new_demo     = strip_fences(result.get("demographics_sql",       "") or "")
    new_addr     = strip_fences(result.get("addresses_sql",          "") or "")
    new_clinical = strip_fences(result.get("clinical_pathology_sql", "") or "")

    modified = []
    for name, sql_var in [("cohort", new_cohort), ("demographics", new_demo),
                          ("addresses", new_addr), ("clinical_pathology", new_clinical)]:
        if sql_var.strip():
            modified.append(name)

    if not modified:
        print("\nNo scripts were modified.")
        print(f"Summary: {summary}")
        print("NOTE: Tempus sub-scripts are not amended. Regenerate with --tempus to update them.")
        return

    # Quality checks
    print("\nRunning quality checks...")
    for name, sql_var in [("cohort", new_cohort), ("demographics", new_demo),
                          ("addresses", new_addr), ("clinical_pathology", new_clinical)]:
        if sql_var.strip():
            run_quality_checks(sql_var, name)

    # Write updated files
    ts = datetime.now().strftime("%Y-%m-%d %H:%M")
    print("\nOutputs updated:")
    for name, path, sql_var in [
        ("cohort",             paths["cohort"],             new_cohort),
        ("demographics",       paths["demographics"],       new_demo),
        ("addresses",          paths["addresses"],          new_addr),
        ("clinical_pathology", paths["clinical_pathology"], new_clinical),
    ]:
        if sql_var.strip():
            path.write_text(sql_var, encoding="utf-8")
            print(f"  {name}: {path.name} ({path.stat().st_size // 1024} KB)")

    if tempus_sql_e:
        print("  NOTE: Tempus sub-scripts not amended. Regenerate with --tempus to update them.")

    print(f"\nSummary: {summary}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def _parse_tempus_codes(raw: str = None) -> list:
    if not raw:
        return None
    return [c.strip() for c in raw.split(",") if c.strip()]


def main():
    import argparse as _ap
    parser = _ap.ArgumentParser(
        description="Generate Databricks SQL from an IRB audit JSON",
        formatter_class=_ap.RawDescriptionHelpFormatter,
        epilog=(
            "Examples:\n"
            "  venv/bin/python excavator/orchestrator.py audit.json\n"
            "  venv/bin/python excavator/orchestrator.py audit.json --tempus-codes XT,XF\n"
            "  venv/bin/python excavator/orchestrator.py --amend audit.json \"add zip code\"\n"
        ),
    )
    parser.add_argument("audit_json", nargs="?",
                        help="Path to IRB audit JSON")
    parser.add_argument("--amend", metavar="AUDIT_JSON",
                        help="Amend existing SQL files for this audit JSON")
    parser.add_argument("request", nargs="?",
                        help="Amendment request text (required with --amend)")
    parser.add_argument("--tempus-codes", default=None, metavar="CODES",
                        help=f"Comma-separated Tempus test_code substrings. "
                             f"Default: {','.join(TEMPUS_DEFAULT_TEST_CODES)}")
    parser.add_argument("--materialize", action="store_true",
                        help="Generate view-referencing mode for Databricks notebook use")
    parser.add_argument("--no-validators", action="store_true",
                        help="Skip IRB auditor and contract checker (faster, less thorough)")
    script_group = parser.add_argument_group(
        "script selection",
        "Flags to generate specific scripts only. If none are given, all applicable scripts "
        "are generated (default). Mix freely: e.g. --cohort --demographics."
    )
    script_group.add_argument("--cohort",            action="store_true", help="Script 1: cohort eligibility")
    script_group.add_argument("--demographics",      action="store_true", help="Script 2: patient demographics")
    script_group.add_argument("--addresses",         action="store_true", help="Script 3: address history")
    script_group.add_argument("--clinical-pathology",action="store_true", help="Script 4: staging, mortality, notes",
                              dest="clinical_pathology")
    script_group.add_argument("--tempus",            action="store_true", help="Script 5: Tempus genomic data")
    script_group.add_argument("--attrition",            action="store_true", help="Script 6: CONSORT attrition counts")
    script_group.add_argument("--temporal-diagnoses",  action="store_true", help="Supplement: all diagnoses per patient with date",
                              dest="temporal_diagnoses")
    parser.add_argument("--output-dir", default=None, metavar="PATH",
                        help="Directory to write SQL and reports into. Defaults to excavator_out/ "
                             "next to the audit JSON when the audit is in claim_out/, otherwise "
                             "writes next to the audit JSON.")
    args = parser.parse_args()

    tempus_codes = _parse_tempus_codes(args.tempus_codes)

    _any_script_flag = any([args.cohort, args.demographics, args.addresses,
                            args.clinical_pathology, args.tempus, args.attrition,
                            args.temporal_diagnoses])
    run_cohort              = args.cohort            or not _any_script_flag
    run_demo                = args.demographics      or not _any_script_flag
    run_addr                = args.addresses         or not _any_script_flag
    run_clinical            = args.clinical_pathology or not _any_script_flag
    run_tempus              = args.tempus            or not _any_script_flag
    run_attrition           = args.attrition         or not _any_script_flag
    run_temporal_diagnoses  = args.temporal_diagnoses  # opt-in only, never part of default run

    if args.amend:
        audit_path = Path(args.amend).resolve()
        if not audit_path.exists():
            print(f"File not found: {audit_path}")
            sys.exit(1)
        request = args.request or args.audit_json or ""
        if not request:
            print("--amend requires a request string as the next positional argument")
            sys.exit(1)
        out_dir_amend = Path(args.output_dir) if args.output_dir else None
        amend_command(audit_path, request, tempus_codes=tempus_codes, out_dir=out_dir_amend)
        return

    if not args.audit_json:
        parser.print_help()
        sys.exit(1)

    audit_path = Path(args.audit_json).resolve()
    if not audit_path.exists():
        print(f"File not found: {audit_path}")
        sys.exit(1)

    print(f"Loading audit: {audit_path.name}")
    audit_data = load_audit(audit_path)
    fields     = extract_fields(audit_data)

    rid_early     = _run_id(audit_path)
    report_path   = audit_path.parent / f"report__{rid_early}.md"
    report_text   = report_path.read_text(encoding="utf-8") if report_path.exists() else None
    if report_text:
        print(f"  Claim report loaded: {report_path.name}")
    else:
        print(f"  NOTE: claim report not found at {report_path.name} -- clarification check will be skipped")
    irb        = fields["irb_summary"]
    print(f"  IRB #{irb.get('protocol_number')} -- PI: {irb.get('pi_name')}")
    print(f"  Approved: {len(fields['approved'])}  "
          f"Denied: {len(fields['denied'])}  "
          f"Ambiguous (->denied): {len(fields['ambiguous'])}")

    client = anthropic.Anthropic()

    # Stage 1: classify elements + identify tables
    print("\nClassifying elements and identifying tables...")
    classification          = classify_and_identify(client, fields)
    clarity_elements        = classification["clarity_elements"]
    gap_elements            = classification["gap_elements"]
    tempus_elements         = classification["tempus_elements"]
    tempus_catalog_elements = classification["tempus_catalog_elements"]
    table_names             = classification["tables_needed"]
    print(f"  Clarity-answerable: {len(clarity_elements)}  "
          f"Tempus SQL: {len(tempus_elements)}  "
          f"Tempus catalog: {len(tempus_catalog_elements)}  "
          f"Gap (external): {len(gap_elements)}")
    print(f"  Tables identified: {table_names}")

    schemas, missing = load_schemas(table_names)
    if missing:
        print(f"  WARNING -- no schema for: {missing}")

    # Determine which specialists to call
    table_names_upper   = [t.upper() for t in table_names]
    generate_addresses       = any(t in _ADDRESS_TABLES for t in table_names_upper)
    generate_tempus_sql     = bool(tempus_elements)
    generate_tempus_catalog = bool(tempus_catalog_elements)

    tempus_schema_ctx = None
    if generate_tempus_sql:
        t_schema          = load_tempus_schema()
        tempus_schema_ctx = build_tempus_schema_context(t_schema)

    active_codes = tempus_codes or TEMPUS_DEFAULT_TEST_CODES
    print(f"\nGenerating cohort SQL (Script 1) -- Tempus filter: {', '.join(active_codes)}...")
    cohort_sql = cohort.generate(client, fields, clarity_elements, schemas,
                                 tempus_codes=tempus_codes)

    # Scripts 2, 3, 4, 5 are independent -- run in parallel after cohort
    demo_sql = addr_sql = clinical_sql = None
    tempus_sqls: dict = {}

    need_demo            = run_demo
    need_addr            = run_addr and generate_addresses
    need_clinical        = run_clinical
    need_tempus          = run_tempus and generate_tempus_sql
    need_tempus_catalog  = run_tempus and generate_tempus_catalog

    active_parts = []
    if need_demo:           active_parts.append("demographics (2)")
    if need_clinical:       active_parts.append("clinical_pathology (4)")
    if need_addr:           active_parts.append("addresses (3)")
    if need_tempus:         active_parts.append(f"Tempus SQL ({len(tempus_elements)} elements, parallel per-table)")
    if need_tempus_catalog: active_parts.append(f"Tempus catalog ({len(tempus_catalog_elements)} elements)")

    tempus_catalog_py = None
    if active_parts:
        print(f"Generating {', '.join(active_parts)} in parallel...")
        with ThreadPoolExecutor(max_workers=4) as executor:
            f_demo     = executor.submit(demographics.generate, client, fields, clarity_elements, schemas) if need_demo     else None
            f_addr     = executor.submit(addresses.generate,    client, fields, clarity_elements, schemas) if need_addr     else None
            f_clinical = executor.submit(clinical_pathology.generate, client, fields, clarity_elements, schemas) if need_clinical else None
            f_tempus   = executor.submit(tempus_databricks.generate, client, fields, tempus_elements, tempus_schema_ctx) if need_tempus else None

            demo_sql     = f_demo.result()     if f_demo     else None
            addr_sql     = f_addr.result()     if f_addr     else None
            clinical_sql = f_clinical.result() if f_clinical else None
            tempus_sqls  = f_tempus.result()   if f_tempus   else {}

    if need_tempus_catalog:
        tempus_catalog_py = tempus_catalog.generate(fields, tempus_catalog_elements)

    # Normalize cohort SQL
    cohort_sql = normalize_cohort_sql(cohort_sql)

    # Generate temporal diagnoses SQL (deterministic, opt-in only)
    # Runs here so it is available for QC and schema validation below
    temporal_diagnoses_sql = None
    if run_temporal_diagnoses:
        temporal_diagnoses_sql = _collapse_comment_blanks(
            cohort_temporal_diagnoses.generate(cohort_sql, fields)
        )

    # Embed cohort into each extraction script and normalize.
    # strip_cohort_prefix removes any eligible_cohort re-derivation the specialist
    # generated before we prepend the canonical cohort block from Script 1.
    if demo_sql:
        demo_sql = _collapse_comment_blanks(embed_cohort(cohort_sql, strip_cohort_prefix(strip_fences(demo_sql))))
        demo_sql = re.sub(r'\bDATETIME\b', 'TIMESTAMP', demo_sql)
    if clinical_sql:
        clinical_sql = _collapse_comment_blanks(embed_cohort(cohort_sql, strip_cohort_prefix(strip_fences(clinical_sql))))
        clinical_sql = re.sub(r'\bDATETIME\b', 'TIMESTAMP', clinical_sql)
    if addr_sql:
        addr_sql = _collapse_comment_blanks(embed_cohort(cohort_sql, strip_cohort_prefix(strip_fences(addr_sql))))
        addr_sql = re.sub(r'\bDATETIME\b', 'TIMESTAMP', addr_sql)
    if tempus_sqls:
        for key, sql in list(tempus_sqls.items()):
            embedded = _collapse_comment_blanks(embed_cohort(cohort_sql, strip_cohort_prefix(strip_fences(sql))))
            tempus_sqls[key] = re.sub(r'\bDATETIME\b', 'TIMESTAMP', embedded)

    # Quality checks
    print("\nRunning quality checks...")
    qc_scripts = [("cohort", cohort_sql)]
    if demo_sql:                 qc_scripts.append(("demographics",          demo_sql))
    if clinical_sql:             qc_scripts.append(("clinical_pathology",    clinical_sql))
    if addr_sql:                 qc_scripts.append(("addresses",             addr_sql))
    for key, sql in tempus_sqls.items():
        qc_scripts.append((f"tempus_{key}", sql))
    if temporal_diagnoses_sql:   qc_scripts.append(("temporal_diagnoses",    temporal_diagnoses_sql))
    any_errors = any(run_quality_checks(sql, lbl) for lbl, sql in qc_scripts)
    if not any_errors:
        print("  All quality checks passed")

    # Schema validation with auto-fix (Clarity)
    actual_schema = load_actual_schema()
    fix_results   = {}

    if actual_schema:
        print("\nValidating SQL against data lake schema...")
        to_validate = [("cohort", cohort_sql)]
        if demo_sql:               to_validate.append(("demographics",         demo_sql))
        if clinical_sql:           to_validate.append(("clinical_pathology",   clinical_sql))
        if addr_sql:               to_validate.append(("addresses",            addr_sql))
        if temporal_diagnoses_sql: to_validate.append(("temporal_diagnoses",   temporal_diagnoses_sql))
        sql_vars = dict(to_validate)

        for lbl, sql in list(sql_vars.items()):
            errors = validate_sql(sql, actual_schema, lbl)
            fix_results[lbl] = {"had_errors": bool(errors), "fixes": []}

            if errors:
                print(f"  {len(errors)} error(s) in {lbl} -- auto-fixing...")
                for _, msg in errors:
                    print(f"    {msg}")
                fixed, fixes = fix_sql_errors(client, sql, errors, actual_schema)
                fix_results[lbl]["fixes"] = list(fixes)
                remaining = validate_sql(fixed, actual_schema, lbl)
                if remaining:
                    print(f"  {len(remaining)} error(s) remain -- second fix pass...")
                    fixed2, fixes2 = fix_sql_errors(client, fixed, remaining, actual_schema)
                    fix_results[lbl]["fixes"].extend(fixes2)
                    remaining2 = validate_sql(fixed2, actual_schema, lbl)
                    if remaining2:
                        print(f"  WARNING: {len(remaining2)} error(s) still unresolved")
                    else:
                        print(f"  {lbl}: {len(fix_results[lbl]['fixes'])} fix(es) applied, re-validated OK")
                    fixed = fixed2
                else:
                    print(f"  {lbl}: {len(fixes)} fix(es) applied, re-validated OK")
                sql_vars[lbl] = fixed
            else:
                print(f"  {lbl}: OK")

        cohort_sql   = sql_vars["cohort"]
        if demo_sql:               demo_sql               = sql_vars.get("demographics",        demo_sql)
        if clinical_sql:           clinical_sql           = sql_vars.get("clinical_pathology",  clinical_sql)
        if addr_sql:               addr_sql               = sql_vars.get("addresses",           addr_sql)
        if temporal_diagnoses_sql: temporal_diagnoses_sql = sql_vars.get("temporal_diagnoses",  temporal_diagnoses_sql)

        # Re-embed the fixed cohort block into Tempus sub-scripts so column-name
        # fixes (e.g. CONTACT_DATE_REAL -> PAT_ENC_DATE_REAL) propagate through.
        if tempus_sqls and fix_results.get("cohort", {}).get("fixes"):
            for key, sql in list(tempus_sqls.items()):
                bare = strip_cohort_prefix(sql)
                tempus_sqls[key] = _collapse_comment_blanks(
                    embed_cohort(cohort_sql, bare)
                )
    else:
        print(f"\n  NOTE: epic_clarity_columns.tsv not found -- skipping schema validation.")
        fix_results = {}

    # Tempus schema validation (report-only)
    if tempus_sqls:
        t_schema_full = load_tempus_schema()
        all_tempus_ok = True
        for key, sql in tempus_sqls.items():
            t_errors = validate_tempus_sql(sql, t_schema_full, f"tempus_{key}")
            if t_errors:
                all_tempus_ok = False
                print(f"\n  tempus_{key}: {len(t_errors)} schema warning(s):")
                for _, msg in t_errors:
                    print(f"    [WARN] {msg}")
        if all_tempus_ok:
            print("  tempus: OK")

    # Validators (IRB auditor + contract checker) -- run on whichever scripts were generated
    if not args.no_validators:
        scripts_for_audit = {"cohort": cohort_sql}
        if demo_sql:               scripts_for_audit["demographics"]        = demo_sql
        if clinical_sql:           scripts_for_audit["clinical_pathology"]  = clinical_sql
        if addr_sql:               scripts_for_audit["addresses"]           = addr_sql
        for key, sql in tempus_sqls.items():
            scripts_for_audit[f"tempus_{key}"] = sql
        if temporal_diagnoses_sql: scripts_for_audit["temporal_diagnoses"]  = temporal_diagnoses_sql

        print("\nRunning validators...")
        with ThreadPoolExecutor(max_workers=3) as ex:
            f_irb      = ex.submit(irb_auditor.audit, client, fields, scripts_for_audit)
            f_contract = ex.submit(contract_checker.check_all, client, scripts_for_audit)
            f_clarity  = (
                ex.submit(clarification_checker.check, client, report_text, scripts_for_audit)
                if report_text else None
            )
            audit_result        = f_irb.result()
            contract_results    = f_contract.result()
            clarification_result = f_clarity.result() if f_clarity else None

        irb_auditor.print_audit_result(audit_result)
        contract_checker.print_contract_results(contract_results)
        if clarification_result is not None:
            clarification_checker.print_results(clarification_result)
        else:
            print("\nClarification Check: SKIPPED (no claim report found)")

    # Generate attrition SQL (deterministic)
    attrition_sql = None
    if run_attrition:
        attrition_sql = _collapse_comment_blanks(attrition.generate(cohort_sql, fields))

    # Gap report
    gap_md = None
    if not _any_script_flag:
        gap_md = build_gap_report(fields, gap_elements, missing, list(schemas.keys()),
                                  tempus_elements=tempus_elements)

    # Resolve output directory
    if args.output_dir:
        out_dir = Path(args.output_dir)
    elif audit_path.parent.name == "claim_out":
        out_dir = audit_path.parent.parent / "excavator_out"
    else:
        out_dir = audit_path.parent
    out_dir.mkdir(parents=True, exist_ok=True)

    rid   = _run_id(audit_path)
    paths = _find_sql_files(audit_path, out_dir=out_dir)

    def kb(p): return p.stat().st_size // 1024

    print(f"\nOutputs written:")

    cohort_path = paths["cohort"]
    cohort_path.write_text(cohort_sql, encoding="utf-8")
    print(f"  Script 1 -- cohort:             {cohort_path.name} ({kb(cohort_path)} KB)")

    if demo_sql:
        demo_path = paths["demographics"]
        demo_path.write_text(demo_sql, encoding="utf-8")
        print(f"  Script 2 -- demographics:       {demo_path.name} ({kb(demo_path)} KB)")

    if addr_sql:
        addr_path = paths["addresses"]
        addr_path.write_text(addr_sql, encoding="utf-8")
        print(f"  Script 3 -- addresses:          {addr_path.name} ({kb(addr_path)} KB)")

    if clinical_sql:
        clinical_path = paths["clinical_pathology"]
        clinical_path.write_text(clinical_sql, encoding="utf-8")
        print(f"  Script 4 -- clinical_pathology: {clinical_path.name} ({kb(clinical_path)} KB)")

    for key, sql in tempus_sqls.items():
        p = paths[f"tempus_{key}"]
        p.write_text(sql, encoding="utf-8")
        print(f"  Script 5 -- Tempus {key}:  {p.name} ({kb(p)} KB)")

    if tempus_catalog_py:
        cat_path = paths["tempus_catalog"]
        cat_path.write_text(tempus_catalog_py, encoding="utf-8")
        print(f"  Catalog   -- Tempus (cluster Python): {cat_path.name} ({kb(cat_path)} KB)")

    if attrition_sql:
        attrn_path = paths["attrition"]
        attrn_path.write_text(attrition_sql, encoding="utf-8")
        print(f"  Script 6 -- attrition:          {attrn_path.name} ({kb(attrn_path)} KB)")

    if temporal_diagnoses_sql:
        td_path = paths["temporal_diagnoses"]
        td_path.write_text(temporal_diagnoses_sql, encoding="utf-8")
        print(f"  Supplement -- temporal_diagnoses: {td_path.name} ({kb(td_path)} KB)")

    if gap_md:
        gap_path = out_dir / f"gap_report_{rid}.md"
        gap_path.write_text(gap_md, encoding="utf-8")
        print(f"  Gap report:                     {gap_path.name}")

    if any(r.get("had_errors") for r in fix_results.values()):
        ts           = datetime.now().strftime("%Y-%m-%d %H:%M")
        fix_log      = build_fix_log(irb, fix_results, ts)
        fix_log_path = out_dir / f"schema_fixes_{rid}.md"
        fix_log_path.write_text(fix_log, encoding="utf-8")
        print(f"  Fix log:                        {fix_log_path.name}")


if __name__ == "__main__":
    main()
