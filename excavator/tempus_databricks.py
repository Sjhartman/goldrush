"""
Specialist: Tempus genomic data extraction (Scripts 5a-5f).

Generates one focused SQL file per output table:
  5a: tempus_orders       -- one row per order (order metadata + patient diagnosis)
  5b: tempus_specimens    -- one row per specimen
  5c: tempus_biomarkers   -- one row per biomarker result (MSI/TMB/HRD/IHC)
  5d: tempus_cnv          -- one row per CNV call
  5e: tempus_fusions      -- one row per fusion call
  5f: tempus_rna_findings -- one row per RNA expression finding (conditional)

Each script is self-contained: the orchestrator embeds the cohort CTE block before writing.
"""

import os
from concurrent.futures import ThreadPoolExecutor

import anthropic

from .shared.prompts import specialist_prompt

MODEL = os.environ.get("ANTHROPIC_MODEL", "claude-sonnet-4-6")

_DOMAIN_ADDITIONS = """
TEMPUS SPECIALIST RULES:

You are extracting data from curated.tempus.* (a separate catalog, accessible from this workspace).

COLUMN SOURCE OF TRUTH: The TEMPUS SCHEMA section of the prompt lists every table and its
confirmed columns. Use ONLY columns that appear there -- never guess column names.

ROUTING BOUNDARY -- SQL vs CATALOG:
This script handles ONLY data available in the Databricks SQL layer (curated.tempus.*).
Raw variant calls are handled exclusively by tempus_catalog.py on the NFS cluster.

FORBIDDEN TABLES -- NEVER QUERY (belong to tempus_catalog.py):
  somaticpotentiallyactionablemutations
  somaticpotentiallyactionablemutationsvariants
  somaticbiologicallyrelevantvariants
  somaticvariantsofunknownsignificance
  inheritedrelevantvariantsvalues
  inheritedincidentalfindingsvalues
  inheritedvariantsofunknownsignificancevalues

FORBIDDEN COLUMNS -- NEVER SELECT from any table:
  notes, specimen_notes, report_notes          (free-text; not approved)
  diagnosis_originpathlabdiagnosis             (free-text path lab narrative; not approved)
  workflow_details                             (potentially free-text; not approved)
  normalsamplesite                             (normal tissue site; not approved)
  contentsreceivedlabel                        (lab logistics; not approved)
  collectiondate, receiptdate                  (operational specimen dates; not approved)
  diagnosisdate                                (Tempus vendor date; not approved)
  bioinfopipeline, modifiesreportid            (technical report admin; not approved)
  signoutdate                                  (report operational date; not approved as standalone element)
  workflow_reportstatus, workflow_reporttype   (internal Tempus workflow metadata; not approved)
  inheritedrelevantvariants_note               (free-text germline note; not approved)
  inheritedincidentalfindings_note             (free-text germline note; not approved)
  inheritedvariantsofunknownsignificance_note  (free-text germline note; not approved)
  chromosome, pos, ref, alt                    (VCF-level coordinates; catalog only)
  firstname, lastname, dateofbirth, sex        (vendor demographics; EHR is authoritative)
  physician, signingpathologist                (clinician PII; not approved)
  institution                                  (Tempus feed not site-scoped; not approved)

ONE FINAL SELECT ONLY:
The WITH block must contain only CTE definitions. The single SELECT must appear at the
very end. Never generate an intermediate SELECT or ORDER BY inside the WITH block.

NO DATE FIELDS in curated.tempus.`order`.
curated.tempus.`order` requires backticks (ORDER is a SQL reserved word).

COHORT BLOCK -- DO NOT MODIFY:
The cohort CTEs are already embedded above your output. Do NOT define or redefine:
  tempus_patients, tempus_pat_ids, gi_hpb_icd, dx_enc, dx_prob, dx_disch, dx_all,
  dx_ranked, dx_min, patient_demo, excluded_patients, eligible_cohort

Your WITH clause must start exactly as:
  WITH
  tempus_eligible AS (
      SELECT ec.*
      FROM eligible_cohort ec
      INNER JOIN tempus_patients tp ON tp.emrid = ec.mrn
  ),
  t5_base AS (
      SELECT te.PAT_ID, te.mrn, te.index_dx_date, te.cancer_type,
             p.tempusId, p.reportId AS patient_reportId
      FROM tempus_eligible te
      INNER JOIN curated.tempus.patient p ON p.emrid = te.mrn
  ),

Always include PAT_ID and mrn as the first two columns so every output table can
join back to the Epic cohort.

DEMOGRAPHICS FROM TEMPUS VENDOR TABLES -- NEVER SELECT:
Do NOT select firstname, lastname, dateofbirth, or sex from curated.tempus.patient.
If joining curated.tempus.patient, select only: diagnosis (as patient_diagnosis).

CLINICIAN PII -- NEVER SELECT:
Do NOT select physician from curated.tempus.`order` or signingpathologist from
curated.tempus.report.

INSTITUTION COLUMN -- NEVER SELECT:
Do NOT select institution from curated.tempus.`order`.

ORDER FIELDS IN VARIANT/SPECIMEN TABLES -- NEVER SELECT:
The tempus_orders script captures order-level metadata. In all other scripts
(specimens, biomarkers, cnv, fusions, rna_findings) do NOT pull order fields
(test_name, test_code, referencegenome) via an order join -- they fan-out when
a patient has multiple orders. Include only each table's own record fields plus
the join keys (PAT_ID, mrn, tempusId, accessionId as appropriate).
Use SELECT DISTINCT in every final SELECT.

SYNTAX RULES:
- ASCII only, no trailing semicolon, no block comments
- Use TIMESTAMP not DATETIME
- No blank lines between consecutive comment-only lines
"""

SYSTEM_PROMPT = specialist_prompt(_DOMAIN_ADDITIONS)

# ---------------------------------------------------------------------------
# Table definitions
# ---------------------------------------------------------------------------

_TABLE_DEFS = [
    {
        "key": "orders",
        "label": "Orders",
        "grain": "one row per order",
        "source_tables": ["curated.tempus.`order`", "curated.tempus.patient"],
        "always": True,
        "description": (
            "Order metadata joined with patient diagnosis. "
            "Columns: accessionId, tempusOrderId, test_code, test_name, test_description, "
            "referenceGenome from curated.tempus.`order`; "
            "diagnosis AS patient_diagnosis from curated.tempus.patient. "
            "Do NOT include physician, institution, or date fields."
        ),
    },
    {
        "key": "specimens",
        "label": "Specimens",
        "grain": "one row per specimen",
        "source_tables": ["curated.tempus.specimens_v2"],
        "always": True,
        "description": (
            "Specimen metadata. "
            "Columns: accessionId (or equivalent specimen join key), tempusSampleId, "
            "institutiondata_caseid, institutiondata_blockid, tumorpercentage, "
            "samplesite, sampletype, samplecategory, primarysamplesite, "
            "diagnosis_tempusicd10code, diagnosis_tempusicdocodetopography, "
            "diagnosis_tempusicdocodemorphology. "
            "Do NOT include notes, diagnosis_originpathlabdiagnosis, normalsamplesite, "
            "contentsreceivedlabel, collectiondate, or receiptdate."
        ),
    },
    {
        "key": "biomarkers",
        "label": "Biomarkers",
        "grain": "one row per result",
        "source_tables": ["curated.tempus.results"],
        "keywords": [
            "msi", "tmb", "tumor mutational", "hrd", "homologous recombination",
            "ihc", "mmr", "pd-l1", "pdl1",
        ],
        "description": (
            "Biomarker results per report. "
            "Columns: msi_status, tmb_value, tmb_percentile, hrd_result, "
            "hrd_analysistype, hrd_brcadoublehit, hrd_pct_genomewideloh, "
            "hrd_loh_threshold, hrd_rnascore, hrd_rnathreshold, "
            "ihc_antigen_name, ihc_pdl1clone, ihc_mmr_interpretation. "
            "Include a join key (reportId or accessionId) so rows link back to orders."
        ),
    },
    {
        "key": "cnv",
        "label": "Copy Number Variants",
        "grain": "one row per CNV call",
        "source_tables": ["curated.tempus.somaticpotentiallyactionablecopynumbervariants"],
        "keywords": ["cnv", "copy number"],
        "description": (
            "Somatic copy number variant calls. "
            "Columns: accessionId, tempusOrderId, test_name, test_code, "
            "gene, entrezid, hgncid, genedescription, varianttype, variantdescription, display."
        ),
    },
    {
        "key": "fusions",
        "label": "Fusions",
        "grain": "one row per fusion call",
        "source_tables": ["curated.tempus.fusionvariants"],
        "keywords": ["fusion", "rearrangement"],
        "description": (
            "RNA fusion calls. "
            "Columns: accessionId, tempusOrderId, test_name, test_code, "
            "gene5, gene5display, gene5entrezid, gene5hgncid, "
            "gene3, gene3display, gene3entrezid, gene3hgncid, "
            "fusiontype, structuralvariant, genedescription, variantdescription."
        ),
    },
    {
        "key": "rna_findings",
        "label": "RNA Expression Findings",
        "grain": "one row per RNA expression finding",
        "source_tables": ["curated.tempus.rnafindings"],
        "keywords": ["rna finding", "rna mechanism", "rna expression finding"],
        "description": (
            "RNA expression mechanism findings (reported tier). "
            "Columns: accessionId, tempusOrderId, test_name, test_code, "
            "gene, entrezid, hgncid, mechanism."
        ),
    },
]


def _has_element(elements: list, keywords: list) -> bool:
    for e in elements:
        name = e.get("element", "").lower()
        if any(kw.lower() in name for kw in keywords):
            return True
    return False


def _applicable_tables(elements: list) -> list:
    result = []
    for td in _TABLE_DEFS:
        if td.get("always"):
            result.append(td)
        elif _has_element(elements, td["keywords"]):
            result.append(td)
    return result


def _generate_one(
    client: anthropic.Anthropic,
    table_def: dict,
    fields: dict,
    tempus_schema_context: str,
    blocked_list: str,
    element_list: str,
    prot: str,
    pi: str,
) -> str:
    key   = table_def["key"]
    label = table_def["label"]
    grain = table_def["grain"]
    desc  = table_def["description"]
    srcs  = ", ".join(table_def["source_tables"])

    prompt = f"""Generate Databricks SQL -- Script 5 Tempus {label} ({grain}).

IRB Protocol : {prot}
PI           : {pi}

CRITICAL -- COHORT BLOCK IS ALREADY EMBEDDED:
Do NOT write tempus_patients, tempus_pat_ids, gi_hpb_icd, dx_enc, dx_prob, dx_disch,
dx_all, dx_ranked, dx_min, patient_demo, excluded_patients, or eligible_cohort.
These CTEs are already defined above your output.

Your WITH clause must start exactly as:
  WITH
  tempus_eligible AS (
      SELECT ec.*
      FROM eligible_cohort ec
      INNER JOIN tempus_patients tp ON tp.emrid = ec.mrn
  ),
  t5_base AS (
      SELECT te.PAT_ID, te.mrn, te.index_dx_date, te.cancer_type,
             p.tempusId, p.reportId AS patient_reportId
      FROM tempus_eligible te
      INNER JOIN curated.tempus.patient p ON p.emrid = te.mrn
  ),

OUTPUT TABLE: {label}
GRAIN: {grain}
SOURCE TABLE(S): {srcs}

CONTENT:
{desc}

APPROVED TEMPUS ELEMENTS:
{element_list}

DENIED / AMBIGUOUS -- exclude from every SELECT:
{blocked_list}

TEMPUS SCHEMA (available columns per table):
{tempus_schema_context}

Header comment: Script 5 Tempus {label}, {grain}, IRB {prot}, PI {pi}.
Return ONLY valid Databricks SQL -- no markdown fences."""

    with client.messages.stream(
        model=MODEL,
        max_tokens=8192,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": prompt}],
    ) as stream:
        return stream.get_final_text().strip()


def generate(
    client: anthropic.Anthropic,
    fields: dict,
    tempus_elements: list,
    tempus_schema_context: str,
) -> dict:
    """Generate one SQL script per applicable Tempus output table.

    Returns dict[table_key, raw_sql]. The cohort CTE block is NOT yet embedded;
    the orchestrator calls embed_cohort() on each entry before writing.
    """
    irb   = fields["irb_summary"]
    pi    = irb.get("pi_name", "Unknown PI")
    prot  = irb.get("protocol_number", "N/A")

    blocked      = fields["denied"] + fields["ambiguous"]
    blocked_list = "\n".join(f"- {e['element']}" for e in blocked) or "None"

    element_list = "\n".join(
        f"- {e['element']} (tables: {', '.join(e.get('suggested_tables', []))})"
        if e.get("suggested_tables") else f"- {e['element']}"
        for e in tempus_elements
    )

    tables = _applicable_tables(tempus_elements)

    with ThreadPoolExecutor(max_workers=len(tables)) as executor:
        futures = {
            td["key"]: executor.submit(
                _generate_one,
                client, td, fields, tempus_schema_context,
                blocked_list, element_list, prot, pi,
            )
            for td in tables
        }
        return {key: f.result() for key, f in futures.items()}
