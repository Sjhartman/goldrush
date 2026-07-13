"""
Specialist: cohort definition (Script 1).

Generates the patient eligibility CTE block. This script must complete before
all others -- its output is embedded into every extraction script.

Minimum output CTE `eligible_cohort` exposes:
    PAT_ID, mrn, index_dx_date, cancer_type, index_icd10_code,
    index_dx_source, age_at_dx, age_stratum

When identified data (patient name, date of birth) is approved, eligible_cohort
also includes: pat_name, birth_date.
"""

import os

import anthropic

from .shared.prompts import specialist_prompt

MODEL = os.environ.get("ANTHROPIC_MODEL", "claude-sonnet-4-6")

TEMPUS_DEFAULT_TEST_CODES = ["XT", "XF", "RS", "XO"]

_DOMAIN_ADDITIONS = """
COHORT SPECIALIST RULES:

This script is COHORT ONLY. Do NOT extract any data elements beyond what is needed
to define patient eligibility and assign the index diagnosis date.

REQUIRED OUTPUT COLUMNS -- name them exactly and output them in this exact order:
    PAT_ID, mrn, pat_name, birth_date, age_at_dx, cancer_type,
    index_icd10_code, age_stratum, index_dx_source, index_dx_date
Use `cancer_type` -- NOT `index_cancer_type`.
The final SELECT must follow this column order exactly.

APPROVED IDENTIFIERS -- include these additional columns when they appear in the
approved elements (the patient_demo CTE already selects them for age arithmetic):
- If patient name is approved: include PAT_NAME aliased as `pat_name`
- If date of birth is approved: include BIRTH_DATE (already aliased as `birth_date`)
Add them to both eligible_cohort and the final SELECT.

REQUIRED CTE NAMES (downstream scripts reference these by name after embedding):
- Name the exclusion patients CTE exactly `excluded_patients` (NOT excl_patients, excl_pt)
- Name the cohort CTE exactly `eligible_cohort`

PERFORMANCE PATTERN -- three-layer pre-filter (mandatory):

Step 1 -- Tempus membership (emrid only):
    tempus_patients AS (
        SELECT DISTINCT p.emrid
        FROM curated.tempus.`order` o
        INNER JOIN curated.tempus.patient p ON p.tempusId = o.tempusId
        WHERE p.emrid IS NOT NULL
          AND (<tempus_like_block>)
    )

Step 2 -- Bridge emrid to PAT_ID (enables large-table push-down):
    tempus_pat_ids AS (
        SELECT DISTINCT p.PAT_ID
        FROM curated.epic_clarity.patient p
        INNER JOIN tempus_patients tp ON tp.emrid = p.PAT_MRN_ID
        WHERE p.PAT_MRN_ID IS NOT NULL
    )

Step 3 -- Pre-filter ICD lookup to qualifying codes only:
    <cohort_icd_cte> AS (
        SELECT DX_ID, CODE
        FROM curated.epic_clarity.edg_current_icd10
        WHERE CODE LIKE 'C15%' OR CODE LIKE 'C16%' OR ...
    )

Step 4 -- dx_raw: patient filter FIRST, then ICD filter -- never unfiltered:
    dx_raw AS (
        SELECT ped.PAT_ID, ...
        FROM curated.epic_clarity.pat_enc_dx ped
        INNER JOIN tempus_pat_ids tpi ON tpi.PAT_ID = ped.PAT_ID  -- patient filter first
        INNER JOIN <cohort_icd_cte> gic ON gic.DX_ID = ped.DX_ID  -- ICD filter second
        ...
    )

DATE_REAL CONVERSION for diagnosis dates:
    PAT_ENC_DATE_REAL, CONTACT_DATE_REAL are DOUBLE (days since 1840-12-31 -- WashU epoch):
    DATE_ADD(DATE '1840-12-31', CAST(col AS INT))

AGE ARITHMETIC (MANDATORY -- apply in BOTH excluded_patients AND eligible_cohort):
    CORRECT:   DATEDIFF(index_dx_date, birth_date) / 365.25
    WRONG:     DATEDIFF(index_dx_date, birth_date) / 365
    WRONG:     DATEDIFF(index_dx_date, birth_date) < 18 * 365
Using a flat 365 underestimates age across leap years. Always use 365.25.
The excluded_patients threshold and the eligible_cohort age columns MUST use identical
365.25 divisor arithmetic so they can never disagree on boundary cases.

MOLECULAR / GENOMIC POPULATION FILTERS:
Molecular filters (gene mutations, alterations, biomarkers -- BRAF, KRAS, RAS, NRAS,
HER2, TMB, MSI, tumor purity, fusion, copy number, any named gene) require explicit
authorization in BOTH the IRB protocol AND the data request or clarification document
before they may appear in the cohort SQL.

If a molecular filter is authorized in both documents: implement it only using confirmed
curated.tempus table columns (see SCHEMAS). Do NOT invent table or column names.
Only curated.tempus.`order` and curated.tempus.patient are confirmed; any other
Tempus table or column must appear in the provided SCHEMAS before you may use it.

If a molecular filter appears only in the population_filters list but is NOT explicitly
confirmed in both the IRB protocol and the data request or clarification, treat it as
a downstream-only filter: omit it from the cohort SQL entirely.
When in doubt, omit the molecular filter -- downstream analysis can apply it later.

DATE RANGE: Apply the correct authorized date window to the dx source CTEs. Priority:
1. If rdc_authorization.present is true and rdc_authorization.is_prospective is true:
   apply only a lower-bound filter (dx_date >= DATE 'rdc_authorization.date_start').
   Do NOT apply any upper cutoff -- prospective means ongoing with no end date.
2. If rdc_authorization.present is true and is_prospective is false:
   apply both bounds (>= date_start AND <= date_end).
3. If no rdc_authorization: use the main IRB retrospective date range if stated.
The main IRB's retrospective EHR cutoff (e.g. section 1.24 05/31/2022) is a separate
data pathway -- do not apply it when RDC is the authorized data source.

INDEX DIAGNOSIS DATE: use ROW_NUMBER() OVER (PARTITION BY PAT_ID ORDER BY dx_date ASC)
on the unioned dx_all CTE, then filter WHERE rn = 1. Do NOT mix MIN() aggregate with
FIRST_VALUE() window functions in the same CTE -- that pattern causes a MISSING_AGGREGATION
error in Databricks SQL when dx_date is not in the GROUP BY. The correct two-step is:
    dx_ranked AS (SELECT ..., ROW_NUMBER() OVER (...) AS rn FROM dx_all)
    dx_min    AS (SELECT ... FROM dx_ranked WHERE rn = 1)

ELIGIBLE_COHORT must INNER JOIN tempus_patients tp ON tp.emrid = <mrn expression>.
Do NOT add address or ZIP availability as a cohort filter.
Do NOT re-implement the three-layer performance pattern in any extraction script.
"""

SYSTEM_PROMPT = specialist_prompt(_DOMAIN_ADDITIONS)


def _tempus_like_block(codes: list) -> str:
    conditions = [f"o.test_code LIKE '%{c}%'" for c in codes]
    return ("\n               OR ".join(conditions)) if conditions else "1=0"


def _build_excl_text(exclusion_diagnoses: list) -> str:
    if not exclusion_diagnoses:
        return "None specified"
    unconditional = []
    conditional   = []
    for excl in exclusion_diagnoses:
        codes     = excl.get("icd10_codes", [])
        qualifier = excl.get("qualifier_condition")
        label     = excl.get("as_specified", "")[:100]
        if not codes:
            continue
        codes_str = ", ".join(codes)
        if qualifier:
            conditional.append(
                f"- {codes_str}\n"
                f"  CONDITION: {qualifier}\n"
                f"  Implement as a compound filter: "
                f"(code LIKE '<code>%' AND <condition>)\n"
                f"  Original label: {label}"
            )
        else:
            unconditional.append(f"- {codes_str}  ({label})")
    parts = []
    if unconditional:
        parts.append("Unconditional exclusions (plain ICD-10 code filter):")
        parts.extend(unconditional)
    if conditional:
        if unconditional:
            parts.append("")
        parts.append("Conditional exclusions (compound filter required):")
        parts.extend(conditional)
    return "\n".join(parts)


def generate(
    client: anthropic.Anthropic,
    fields: dict,
    clarity_elements: list,
    schemas: dict,
    tempus_codes: list = None,
) -> str:
    """
    Generate the cohort definition SQL (Script 1).
    Returns the raw SQL string (fences not yet stripped).
    """
    codes      = tempus_codes if tempus_codes is not None else TEMPUS_DEFAULT_TEST_CODES
    like_block = _tempus_like_block(codes)

    import json
    element_list    = "\n".join(f"- {e['element']}" for e in clarity_elements)
    request_context = json.dumps({
        "irb_summary":       fields["irb_summary"],
        "request_summary":   fields["request_summary"],
        "icd_code_analysis": fields["icd_code_analysis"],
    }, indent=2)
    rdc_auth     = fields.get("rdc_authorization", {}) or {}
    rdc_present  = rdc_auth.get("present", False)
    rdc_start    = rdc_auth.get("date_start")
    rdc_end      = rdc_auth.get("date_end")
    rdc_prosp    = rdc_auth.get("is_prospective", False)
    if rdc_present and rdc_start:
        if rdc_prosp:
            rdc_block = (
                f"RDC AUTHORIZATION PRESENT (I2DB IRB {rdc_auth.get('irb_id', '')}, "
                f"PI: {rdc_auth.get('pi', '')}).\n"
                f"This RDC is prospective/ongoing. Apply a lower-bound date filter only: "
                f"dx_date >= DATE '{rdc_start}'. Do NOT apply any upper cutoff."
            )
        else:
            rdc_block = (
                f"RDC AUTHORIZATION PRESENT (I2DB IRB {rdc_auth.get('irb_id', '')}, "
                f"PI: {rdc_auth.get('pi', '')}).\n"
                f"Apply both bounds: dx_date >= DATE '{rdc_start}' AND dx_date <= DATE '{rdc_end}'."
            )
    else:
        rdc_block = "No RDC authorization found -- use main IRB date range from request context if stated."
    blocked      = fields["denied"] + fields["ambiguous"]
    blocked_list = "\n".join(f"- {e['element']}" for e in blocked) or "None"
    pop_filters  = fields["request_summary"].get("population_filters", [])
    pop_text     = "\n".join(f"- {f}" for f in pop_filters) if pop_filters else "None specified"
    excl_text    = _build_excl_text(fields.get("exclusion_diagnoses", []))

    cohort_tables = {k: v for k, v in schemas.items()
                     if any(kw in k for kw in (
                         "PAT_ENC", "PATIENT", "EDG", "PROBLEM",
                         "HSP_ACCT", "HSP_DISCH", "HSP_ADMIT",
                         "IDENTITY", "ZC_SEX", "ZC_PATIENT_RACE",
                         "ZC_ETHNIC", "ZC_PROBLEM",
                     ))}
    schema_block = "\n\n---\n\n".join(f"TABLE: {k}\n{v}" for k, v in cohort_tables.items())

    prompt = f"""Generate Databricks SQL -- COHORT DEFINITION (Script 1 of 6).

TEMPUS FILTER -- use this exact like_block in the tempus_patients CTE:
    WHERE p.emrid IS NOT NULL
      AND ({like_block})

APPROVED ELEMENTS (cohort and index-date definition only -- no extraction):
{element_list}

REQUEST CONTEXT:
{request_context}

RDC DATE WINDOW:
{rdc_block}

APPROVED POPULATION SCOPE -- enforce ALL as WHERE inclusion filters:
{pop_text}

REQUESTED EXCLUSION CRITERIA -- enforce ALL as WHERE exclusion filters:
{excl_text}

DENIED / AMBIGUOUS -- exclude from every SELECT:
{blocked_list}

SCHEMAS:
{schema_block}

Add a header comment noting this is Script 1 of 6 with IRB protocol number and PI.
Return ONLY valid Databricks SQL -- no markdown fences."""

    response = client.messages.create(
        model=MODEL,
        max_tokens=16384,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": prompt}],
    )
    return response.content[0].text.strip()
