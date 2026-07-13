"""
Specialist: cohort temporal diagnoses (ad hoc supplement).

Fully deterministic -- no API call.
Generates a longitudinal ALL-diagnoses table for cohort patients.
One row per unique (PAT_ID, mrn, dx_date, icd10_code, icd10_description, dx_source).
Sources: PAT_ENC_DX, PROBLEM_LIST, HSP_DISCH_DIAG.
No ICD code filter -- all codes returned (GI/HPB, Z15, comorbidities).
ICD-10 description resolved via CLARITY_EDG.dx_name (LEFT JOIN on dx_id).
"""

from .shared.embedding import _strip_leading_comments, extract_cte_block


def generate(cohort_sql: str, fields: dict) -> str:
    """
    Build a self-contained temporal diagnoses script.

    Returns all EHR-coded diagnoses for eligible cohort patients across
    all dates and all ICD-10 codes. One row per
    (PAT_ID, mrn, dx_date, icd10_code, icd10_description, dx_source)
    after deduplication.
    """
    irb  = fields["irb_summary"]
    pi   = irb.get("pi_name", "Unknown PI")
    prot = irb.get("protocol_number", "N/A")

    cte_block = _strip_leading_comments(extract_cte_block(cohort_sql))

    header = (
        "-- =============================================================================\n"
        f"-- Cohort Temporal Diagnoses: all EHR-coded diagnoses for cohort patients\n"
        f"-- IRB Protocol: {prot}\n"
        f"-- PI: {pi}\n"
        "-- Purpose: Longitudinal diagnosis history across all dates and ICD-10 codes.\n"
        "--          One row per (PAT_ID, mrn, dx_date, icd10_code, icd10_description, dx_source).\n"
        "--          Sources: PAT_ENC_DX, PROBLEM_LIST, HSP_DISCH_DIAG.\n"
        "--          No ICD code filter -- GI/HPB, Z15, and comorbidities all included.\n"
        "--          ICD-10 description from CLARITY_EDG.dx_name (NULL if unmapped).\n"
        "-- =============================================================================\n"
    )

    body = (
        "WITH\n"
        + cte_block.lstrip("WITH").lstrip()
        + ",\n"
        "\n"
        "-- ---------------------------------------------------------------------------\n"
        "-- Temporal diagnoses: all encounter diagnoses (no ICD code filter)\n"
        "-- Eligible cohort join is first to enforce push-down pre-filtering.\n"
        "-- CLARITY_EDG provides ICD-10 description via dx_id.\n"
        "-- ---------------------------------------------------------------------------\n"
        "td_enc AS (\n"
        "    SELECT\n"
        "        ped.PAT_ID,\n"
        "        DATE_ADD(DATE '1840-12-31', CAST(ped.PAT_ENC_DATE_REAL AS INT)) AS dx_date,\n"
        "        ei.CODE  AS icd10_code,\n"
        "        ce.dx_name AS icd10_description,\n"
        "        'PAT_ENC_DX' AS dx_source\n"
        "    FROM curated.epic_clarity.pat_enc_dx ped\n"
        "    INNER JOIN eligible_cohort ec ON ec.PAT_ID = ped.PAT_ID\n"
        "    INNER JOIN curated.epic_clarity.edg_current_icd10 ei ON ei.DX_ID = ped.DX_ID\n"
        "    LEFT  JOIN curated.epic_clarity.clarity_edg ce ON ce.dx_id = ei.dx_id\n"
        "    WHERE ped.PAT_ENC_DATE_REAL IS NOT NULL\n"
        "),\n"
        "\n"
        "-- ---------------------------------------------------------------------------\n"
        "-- Temporal diagnoses: all problem list entries (no ICD code filter)\n"
        "-- Excludes deleted problems (PROBLEM_STATUS_C = 3).\n"
        "-- ---------------------------------------------------------------------------\n"
        "td_prob AS (\n"
        "    SELECT\n"
        "        pl.PAT_ID,\n"
        "        CAST(pl.NOTED_DATE AS DATE)            AS dx_date,\n"
        "        ei.CODE  AS icd10_code,\n"
        "        ce.dx_name AS icd10_description,\n"
        "        'PROBLEM_LIST' AS dx_source\n"
        "    FROM curated.epic_clarity.problem_list pl\n"
        "    INNER JOIN eligible_cohort ec ON ec.PAT_ID = pl.PAT_ID\n"
        "    INNER JOIN curated.epic_clarity.edg_current_icd10 ei ON ei.DX_ID = pl.DX_ID\n"
        "    LEFT  JOIN curated.epic_clarity.clarity_edg ce ON ce.dx_id = ei.dx_id\n"
        "    WHERE pl.NOTED_DATE IS NOT NULL\n"
        "      AND pl.PROBLEM_STATUS_C != 3\n"
        "),\n"
        "\n"
        "-- ---------------------------------------------------------------------------\n"
        "-- Temporal diagnoses: all inpatient discharge diagnoses (no ICD code filter)\n"
        "-- ---------------------------------------------------------------------------\n"
        "td_disch AS (\n"
        "    SELECT\n"
        "        hdd.PAT_ID,\n"
        "        DATE_ADD(DATE '1840-12-31', CAST(hdd.PAT_ENC_DATE_REAL AS INT)) AS dx_date,\n"
        "        ei.CODE  AS icd10_code,\n"
        "        ce.dx_name AS icd10_description,\n"
        "        'HSP_DISCH_DIAG' AS dx_source\n"
        "    FROM curated.epic_clarity.hsp_disch_diag hdd\n"
        "    INNER JOIN eligible_cohort ec ON ec.PAT_ID = hdd.PAT_ID\n"
        "    INNER JOIN curated.epic_clarity.edg_current_icd10 ei ON ei.DX_ID = hdd.DX_ID\n"
        "    LEFT  JOIN curated.epic_clarity.clarity_edg ce ON ce.dx_id = ei.dx_id\n"
        "    WHERE hdd.PAT_ENC_DATE_REAL IS NOT NULL\n"
        "),\n"
        "\n"
        "-- ---------------------------------------------------------------------------\n"
        "-- Union all three diagnosis sources\n"
        "-- ---------------------------------------------------------------------------\n"
        "td_all AS (\n"
        "    SELECT PAT_ID, dx_date, icd10_code, icd10_description, dx_source FROM td_enc\n"
        "    UNION ALL\n"
        "    SELECT PAT_ID, dx_date, icd10_code, icd10_description, dx_source FROM td_prob\n"
        "    UNION ALL\n"
        "    SELECT PAT_ID, dx_date, icd10_code, icd10_description, dx_source FROM td_disch\n"
        ")\n"
        "\n"
        "SELECT DISTINCT\n"
        "    td.PAT_ID,\n"
        "    ec.mrn,\n"
        "    td.dx_date,\n"
        "    td.icd10_code,\n"
        "    td.icd10_description,\n"
        "    td.dx_source\n"
        "FROM td_all td\n"
        "INNER JOIN eligible_cohort ec ON ec.PAT_ID = td.PAT_ID\n"
        "ORDER BY\n"
        "    td.PAT_ID,\n"
        "    td.dx_date,\n"
        "    td.icd10_code\n"
    )

    return header + body