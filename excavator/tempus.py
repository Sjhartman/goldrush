"""
Specialist: Tempus genomic data extraction (Script 5).

Joins eligible_cohort -> curated.tempus.patient -> other Tempus tables via tempusId.
Self-contained: cohort CTE block is embedded by the orchestrator before writing.
"""

import os

import anthropic

from .shared.prompts import specialist_prompt

MODEL = os.environ.get("ANTHROPIC_MODEL", "claude-sonnet-4-6")

_DOMAIN_ADDITIONS = """
TEMPUS SPECIALIST RULES:

You are extracting data from curated.tempus.* (a separate catalog, accessible from this workspace).

CONFIRMED COLUMN LISTS -- use ONLY these columns (no others exist in the SQL layer):

curated.tempus.patient:
    institution, emrid, tempusId, reportId, accessionId, test_code, test_name,
    test_description, referenceGenome

curated.tempus.`order` (backtick required -- ORDER is a SQL reserved word):
    institution, physician, tempusOrderId, accessionId, test_code, test_name,
    test_description, tempusId, reportId, referenceGenome

curated.tempus.specimens:
    tempusId, accessionId, collectionSite, specimenType, tumorPercentage,
    collectionDate, reportId

curated.tempus.results:
    tempusId, reportId, resultType, biomarkerName, biomarkerValue, unit,
    interpretation, methodology

curated.tempus.report:
    tempusId, reportId, reportType, signOutDate, signingPathologist, pipeline

NO DATE FIELDS in curated.tempus.`order` -- only use date fields from specimens or report.
NO BIOMARKER FIELDS (TMB, MSI, tumor purity, variant calls) in SQL -- these live in
catalog TSV files and are matched at the Python layer. Do NOT attempt to extract them.

FIRST CTE must be `t5_base` (exactly):
    t5_base AS (
        SELECT ec.PAT_ID,
               ec.mrn,
               ec.index_dx_date,
               ec.cancer_type,
               p.tempusId,
               p.reportId AS patient_reportId
        FROM eligible_cohort ec
        INNER JOIN curated.tempus.patient p ON p.emrid = ec.mrn
    )

Subsequent CTEs join via t5_base.tempusId to the relevant Tempus tables.
All Tempus joins are LEFT JOIN (a patient may have multiple orders or no results).

SYNTAX RULES:
- curated.tempus.`order` requires backticks (ORDER is reserved)
- ASCII only, no trailing semicolon, no block comments
- Do NOT redefine eligible_cohort or any cohort-block CTE
- Use TIMESTAMP not DATETIME
- No blank lines between consecutive comment-only lines
"""

SYSTEM_PROMPT = specialist_prompt(_DOMAIN_ADDITIONS)


def generate(
    client: anthropic.Anthropic,
    fields: dict,
    tempus_elements: list,
    tempus_schema_context: str,
) -> str:
    """
    Generate Script 5 (Tempus data extraction).
    Returns raw SQL (fences not yet stripped).
    """
    irb  = fields["irb_summary"]
    pi   = irb.get("pi_name", "Unknown PI")
    prot = irb.get("protocol_number", "N/A")

    blocked      = fields["denied"] + fields["ambiguous"]
    blocked_list = "\n".join(f"- {e['element']}" for e in blocked) or "None"

    element_list = "\n".join(
        f"- {e['element']} (tables: {', '.join(e.get('suggested_tables', []))})"
        if e.get('suggested_tables') else f"- {e['element']}"
        for e in tempus_elements
    )

    prompt = f"""Generate Databricks SQL -- Script 5 of 6: Tempus Genomic Data Extraction.

IRB Protocol : {prot}
PI           : {pi}

The following CTE is already defined in the embedded cohort block -- reference it directly,
do NOT redefine or redeclare it:
- `eligible_cohort (PAT_ID, mrn, index_dx_date, cancer_type, age_at_dx, age_stratum)`

APPROVED TEMPUS ELEMENTS TO EXTRACT:
{element_list}

DENIED / AMBIGUOUS -- exclude from every SELECT:
{blocked_list}

TEMPUS SCHEMA (available columns per table):
{tempus_schema_context}

Header comment: Script 5 of 6, Tempus genomic data extraction, IRB {prot}, PI {pi}.
Return ONLY valid Databricks SQL -- no markdown fences."""

    response = client.messages.create(
        model=MODEL,
        max_tokens=16384,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": prompt}],
    )
    return response.content[0].text.strip()
