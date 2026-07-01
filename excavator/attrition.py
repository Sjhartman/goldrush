"""
Specialist: attrition report (Script 6).

Fully deterministic Python -- no API call.
Embeds the cohort CTE block and generates a CONSORT attrition count
plus an excluded-patient list (toggled by commenting/uncommenting).
"""

from .shared.embedding import _strip_leading_comments, extract_cte_block


def generate(cohort_sql: str, fields: dict) -> str:
    """
    Build a self-contained Script 6 (attrition + excluded patient list).

    OUTPUT A: CONSORT attrition counts (default -- run as-is)
    OUTPUT B: One row per excluded patient with the first triggering code
              (uncomment the second SELECT block to run)
    """
    irb  = fields["irb_summary"]
    pi   = irb.get("pi_name", "Unknown PI")
    prot = irb.get("protocol_number", "N/A")

    cte_block = _strip_leading_comments(extract_cte_block(cohort_sql))

    excl_diagnoses = fields.get("exclusion_diagnoses", [])
    like_parts     = []
    comment_lines  = []
    for excl in excl_diagnoses:
        codes     = excl.get("icd10_codes", [])
        qualifier = excl.get("qualifier_condition")
        for code in codes:
            c = code.strip()
            suffix = f"  -- conditional: {qualifier}" if qualifier else ""
            like_parts.append(f"ei.CODE LIKE '{c}%'{suffix}")
            comment_lines.append(
                f"--   {c}" + (f" [conditional: {qualifier}]" if qualifier else "")
            )

    if like_parts:
        excl_where   = "    " + "\n    OR ".join(like_parts)
        excl_comment = "\n".join(comment_lines)
    else:
        excl_where   = "    1=0  -- no exclusion criteria"
        excl_comment = "--   (none)"

    header = f"""\
-- ============================================================
-- Script 6 of 6: Attrition Report + Excluded Patient List
-- IRB Protocol : {prot}
-- PI           : {pi}
-- Exclusion criteria:
{excl_comment}
-- ============================================================
-- OUTPUT A (default): Attrition / CONSORT counts -- run as-is
-- OUTPUT B          : Excluded patients with reason -- uncomment
--                     the second SELECT block and run separately
-- ============================================================
"""

    body = f"""\
WITH
{cte_block.lstrip('WITH').lstrip()}
,
-- -------------------------------------------------------
-- s6_excl_dx_ids: DX_IDs matching any exclusion criterion.
-- Self-contained -- built from EDG_CURRENT_ICD10 using the
-- exact exclusion code list from the data request.
-- Prefixed s6_ to avoid collision with cohort-block CTEs.
-- -------------------------------------------------------
s6_excl_dx_ids AS (
    SELECT DISTINCT ei.DX_ID, ei.CODE AS icd10_code
    FROM curated.epic_clarity.edg_current_icd10 ei
    WHERE
{excl_where}
),
-- -------------------------------------------------------
-- s6_excl_raw: one row per (excluded_patient, source, code)
-- scanning enc, problem list, and hospital discharge dx.
-- -------------------------------------------------------
s6_excl_raw AS (
    SELECT ped.PAT_ID, ex.icd10_code, 'enc_dx'       AS excl_source
    FROM   curated.epic_clarity.pat_enc_dx  ped
    JOIN   s6_excl_dx_ids                   ex  ON ex.DX_ID = ped.DX_ID
    JOIN   excluded_patients                ep  ON ep.PAT_ID = ped.PAT_ID
    UNION ALL
    SELECT pl.PAT_ID, ex.icd10_code,  'problem_list' AS excl_source
    FROM   curated.epic_clarity.problem_list pl
    JOIN   s6_excl_dx_ids                    ex ON ex.DX_ID = pl.DX_ID
    JOIN   excluded_patients                 ep ON ep.PAT_ID = pl.PAT_ID
    UNION ALL
    SELECT hd.PAT_ID, ex.icd10_code,  'hsp_disch'    AS excl_source
    FROM   curated.epic_clarity.hsp_disch_diag hd
    JOIN   s6_excl_dx_ids                      ex ON ex.DX_ID = hd.DX_ID
    JOIN   excluded_patients                   ep ON ep.PAT_ID = hd.PAT_ID
),
-- First triggering code per excluded patient (alphabetical by code)
s6_first_excl AS (
    SELECT PAT_ID, icd10_code AS first_excl_icd10, excl_source AS first_excl_source
    FROM   s6_excl_raw
    QUALIFY ROW_NUMBER() OVER (PARTITION BY PAT_ID ORDER BY icd10_code, excl_source) = 1
),
-- -------------------------------------------------------
-- Attrition counts
-- -------------------------------------------------------
s6_counts AS (
    SELECT 'step_01_pre_exclusion'  AS step,
           COUNT(DISTINCT PAT_ID)   AS n
    FROM   (SELECT PAT_ID FROM excluded_patients
            UNION ALL
            SELECT PAT_ID FROM eligible_cohort) all_pre
    UNION ALL
    SELECT 'step_02_excluded'       AS step,
           COUNT(DISTINCT PAT_ID)   AS n
    FROM   excluded_patients
    UNION ALL
    SELECT 'step_03_eligible_cohort' AS step,
           COUNT(DISTINCT PAT_ID)    AS n
    FROM   eligible_cohort
),
-- Excluded patient summary with MRN
s6_excl_summary AS (
    SELECT
        ep.PAT_ID,
        p.PAT_MRN_ID                    AS mrn,
        fe.first_excl_icd10             AS exclusion_trigger_code,
        fe.first_excl_source            AS exclusion_trigger_source
    FROM   excluded_patients                      ep
    LEFT JOIN curated.epic_clarity.patient        p   ON p.PAT_ID = ep.PAT_ID
    LEFT JOIN s6_first_excl                       fe  ON fe.PAT_ID = ep.PAT_ID
)

-- ============================================================
-- OUTPUT A: Attrition / CONSORT table
-- ============================================================
SELECT step, n AS patient_count
FROM   s6_counts
ORDER BY step

-- ============================================================
-- OUTPUT B: Excluded patients with reason (run separately)
-- ============================================================
-- SELECT PAT_ID, mrn, exclusion_trigger_code, exclusion_trigger_source
-- FROM   s6_excl_summary
-- ORDER BY exclusion_trigger_code, PAT_ID
"""
    return header + body