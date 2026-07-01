"""
Specialist: clinical outcomes + pathology notes (Script 4).

Generates two extraction passes in parallel:
  - Clinical outcomes: staging (supplementary), mortality, recurrence, enrollment,
    treatment plans
  - Pathology/clinical notes: HNO_INFO + HNO_NOTE_TEXT

Both are combined into a single script via UNION ALL in long/stacked format.
"""

import os
from concurrent.futures import ThreadPoolExecutor

import anthropic

from .shared.prompts import specialist_prompt

MODEL = os.environ.get("ANTHROPIC_MODEL", "claude-sonnet-4-6")

_DOMAIN_ADDITIONS = """
CLINICAL_PATHOLOGY SPECIALIST RULES:

OUTPUT STRUCTURE:
- Long/stacked format using UNION ALL across result domains.
- Each domain is a CTE that produces rows with a consistent column set:
    pat_id, mrn, index_dx_date, cancer_type,
    result_domain, source_record_id, source_date, subtype_label,
    icd10_code, icd10_description, text_content
- result_domain label examples: 'STAGING', 'MORTALITY', 'RECURRENCE_ENC',
  'RECURRENCE_PL', 'ENROLLMENT', 'TPL', 'CLINICAL_NOTE_PATH'

V_CANCER_STAGING -- SUPPLEMENTARY ONLY:
- This table is notoriously poorly filled in this environment.
- NEVER use it as the primary or sole source for staging data.
- Include it as one supplementary domain in the stacked output.
- Add a SQL comment on the CTE: "-- NOTE: V_CANCER_STAGING is poorly filled;
  use as supplementary only; verify staging via pathology notes"
- Column name corrections (NO stage_ prefix on any column):
    contact_date (NOT stage_contact_date)
    classification_name (NOT stage_classification)
    staging_date is the date the stage was recorded

TPL_INFO column corrections (exact names):
    display_name (NOT plan_display_name)
    eff_end_date (NOT plan_eff_end_date)
    plan_status_c -- decode via ZC_PLAN_STATUS
    dc_reason_c   -- decode via ZC_DC_REASON
    trt_goal_c    -- decode via ZC_TRT_GOAL
    line_of_treatment_c -- no ZC_ table; expose code directly

HNO_INFO (clinical notes) -- environment-specific rules:
- Signed notes filter: unsigned_yn IS NULL OR unsigned_yn = 'N'
  (NULL means signed; 'Y' means draft -- exclude drafts)
- Note type column: note_type_noadd_c (NOT NOTE_TYPE_C)
- Not deleted: delete_instant_dttm IS NULL
- LEFT JOIN ZC_NOTE_TYPE on note_type_noadd_c
- AP/pathology reports frequently have no ZC_NOTE_TYPE mapping (NULL) --
  include NULL as a valid note type (do NOT exclude it)
- Use COALESCE(znt.name, znti.name) AS note_type_name with LEFT JOIN ZC_NOTE_TYPE_IP
  on ip_note_type_c for the secondary lookup

HNO_NOTE_TEXT aggregation pattern:
    TRANSFORM(SORT_ARRAY(COLLECT_LIST(STRUCT(nt.line, nt.note_text))), x -> x.note_text)
      AS note_text_lines
    Filter: is_archived_yn = 'N'
    GROUP BY all non-aggregate columns

Every CTE reading HNO_INFO or HNO_NOTE_TEXT MUST join eligible_cohort as its FIRST join.
Do NOT include recurrence detection from ICD codes if not an approved element.
Do NOT include demographics, address, or Tempus columns.
"""

SYSTEM_PROMPT = specialist_prompt(_DOMAIN_ADDITIONS)

_NOTE_TYPES = (
    "Procedures",
    "Op Note",
    "Post-Procedure Note",
    "Pre-Procedure Note",
    "Result Encounter Note",
    "Consults",
    "Consults, Subsequent",
    "Discharge Summary",
    "Hospital Course",
    "H&P",
    "Interval H&P Note",
)

_NOTE_TABLES    = {"HNO_INFO", "HNO_NOTE_TEXT", "ZC_NOTE_TYPE", "ZC_NOTE_TYPE_IP"}
_CLINICAL_SKIP  = _NOTE_TABLES


def _clinical_prompt(fields: dict, clarity_elements: list, schemas: dict) -> str:
    element_list = "\n".join(f"- {e['element']}" for e in clarity_elements)
    blocked      = fields["denied"] + fields["ambiguous"]
    blocked_list = "\n".join(f"- {e['element']}" for e in blocked) or "None"

    clinical_schemas = {k: v for k, v in schemas.items() if k not in _CLINICAL_SKIP}
    schema_block = "\n\n---\n\n".join(
        f"TABLE: {k}\n{v}" for k, v in clinical_schemas.items()
    )

    return f"""Generate Databricks SQL -- Script 4 Part A: Clinical Outcomes (staging, mortality,
recurrence, enrollment, treatment plans). This will be UNION ALLed with Part B (notes).

The following CTEs are already defined in the embedded cohort block -- reference them
directly, do NOT redefine or redeclare any of them:
- `eligible_cohort (PAT_ID, mrn, index_dx_date, cancer_type, age_at_dx, age_stratum)`
- `excluded_patients (PAT_ID)`

Use result_domain labels for each CTE: STAGING, MORTALITY, RECURRENCE_ENC,
RECURRENCE_PL, ENROLLMENT, TPL. The final SELECT must produce this exact column set:
    pat_id, mrn, index_dx_date, cancer_type,
    result_domain, source_record_id, source_date, subtype_label,
    icd10_code, icd10_description, text_content

APPROVED ELEMENTS (clinical outcomes relevant to this script):
{element_list}

DENIED / AMBIGUOUS -- exclude from every SELECT:
{blocked_list}

SCHEMAS:
{schema_block}

Header comment: Script 4 Part A of 6, Clinical Outcomes.
Return ONLY valid Databricks SQL -- no markdown fences."""


def _notes_prompt(fields: dict, clarity_elements: list, schemas: dict) -> str:
    element_list = "\n".join(f"- {e['element']}" for e in clarity_elements)
    blocked      = fields["denied"] + fields["ambiguous"]
    blocked_list = "\n".join(f"- {e['element']}" for e in blocked) or "None"

    note_type_list = "\n".join(f"    '{t}'," for t in _NOTE_TYPES)
    note_schemas = {k: v for k, v in schemas.items() if k in _NOTE_TABLES}
    schema_block = "\n\n---\n\n".join(f"TABLE: {k}\n{v}" for k, v in note_schemas.items())

    return f"""Generate Databricks SQL -- Script 4 Part B: Pathology and Clinical Notes.
This will be UNION ALLed with Part A (clinical outcomes).

The following CTEs are already defined in the embedded cohort block -- reference them
directly, do NOT redefine or redeclare any of them:
- `eligible_cohort (PAT_ID, mrn, index_dx_date, cancer_type, age_at_dx, age_stratum)`
- `excluded_patients (PAT_ID)`

Generate exactly TWO extraction CTEs named `s4_note_headers` and `s4_clinical_notes`:

s4_note_headers -- reads HNO_INFO joined to eligible_cohort (cohort first). Apply:
  - Signed notes: (unsigned_yn IS NULL OR unsigned_yn = 'N')
  - Not deleted: delete_instant_dttm IS NULL
  - Note service date: CAST(COALESCE(date_of_servic_dttm, create_instant_dttm) AS DATE)
  - Date range: >= DATE '1998-01-01' AND < DATE '2026-01-01'
  - LEFT JOIN ZC_NOTE_TYPE on note_type_noadd_c (alias znt)
  - LEFT JOIN ZC_NOTE_TYPE_IP on ip_note_type_c (alias znti)
  - Expose COALESCE(znt.name, znti.name) AS note_type_name
  - Note type filter: note_type_name IS NULL (unmapped -- include AP reports) OR IN:
{note_type_list}

s4_clinical_notes -- joins s4_note_headers to HNO_NOTE_TEXT on note_id:
  - Filter: is_archived_yn = 'N'
  - Aggregate: TRANSFORM(SORT_ARRAY(COLLECT_LIST(STRUCT(nt.line, nt.note_text))), x -> x.note_text) AS note_text_lines
  - GROUP BY all non-aggregate columns

Final SELECT from s4_clinical_notes -- must match the Part A column set exactly:
    PAT_ID AS pat_id, mrn, index_dx_date, cancer_type,
    'CLINICAL_NOTE_PATH' AS result_domain,
    note_id AS source_record_id,
    note_service_date AS source_date,
    note_type_name AS subtype_label,
    NULL AS icd10_code,
    NULL AS icd10_description,
    ARRAY_JOIN(note_text_lines, '\\n') AS text_content
ORDER BY pat_id, result_domain, source_date, source_record_id

DENIED / AMBIGUOUS -- exclude from every SELECT:
{blocked_list}

SCHEMAS:
{schema_block}

Header comment: Script 4 Part B of 6, Pathology and Clinical Notes.
Return ONLY valid Databricks SQL -- no markdown fences."""


def generate(
    client: anthropic.Anthropic,
    fields: dict,
    clarity_elements: list,
    schemas: dict,
) -> str:
    """
    Generate Script 4 (clinical outcomes + pathology notes) in two parallel passes,
    then combine into a single script using UNION ALL.
    Returns the combined raw SQL (fences not yet stripped).
    """
    def call(prompt):
        return client.messages.create(
            model=MODEL,
            max_tokens=16384,
            system=SYSTEM_PROMPT,
            messages=[{"role": "user", "content": prompt}],
        ).content[0].text.strip()

    p_clinical = _clinical_prompt(fields, clarity_elements, schemas)
    p_notes    = _notes_prompt(fields, clarity_elements, schemas)

    include_notes = any(k in schemas for k in _NOTE_TABLES)

    if include_notes:
        with ThreadPoolExecutor(max_workers=2) as ex:
            f_clin  = ex.submit(call, p_clinical)
            f_notes = ex.submit(call, p_notes)
            clinical_sql = f_clin.result()
            notes_sql    = f_notes.result()
        return _merge_parts(clinical_sql, notes_sql)
    else:
        return call(p_clinical)


def _merge_parts(clinical_sql: str, notes_sql: str) -> str:
    """
    Combine two SQL scripts by appending a UNION ALL.
    The clinical script provides the WITH block; the notes script's CTEs are appended.
    """
    from .shared.embedding import strip_fences, _strip_leading_comments
    clinical_sql = strip_fences(clinical_sql)
    notes_sql    = strip_fences(notes_sql)

    # Extract just the CTEs and final SELECT from the notes script
    # and combine into one script via UNION ALL on the final SELECT
    separator = "\n\nUNION ALL\n\n"

    # Find the final SELECT in notes_sql to append it as UNION ALL
    import re
    # Strip any leading WITH block from notes_sql (it references eligible_cohort
    # which is already in clinical_sql's embedded cohort block)
    notes_body = _strip_leading_comments(notes_sql)
    # Remove the leading WITH keyword since we're appending CTEs
    notes_body = re.sub(r'^\s*WITH\b', ',', notes_body, count=1, flags=re.IGNORECASE)

    # Find the final SELECT in clinical_sql -- insert notes CTEs before it
    lines = clinical_sql.splitlines()
    final_select_idx = None
    depth = 0
    for i, line in enumerate(lines):
        stripped = re.sub(r'--[^\n]*', '', line)
        depth += stripped.count('(') - stripped.count(')')
        if depth == 0 and re.match(r'\s*SELECT\b', stripped, re.IGNORECASE):
            # Check this isn't inside a CTE
            final_select_idx = i
            break

    if final_select_idx is None:
        # Fallback: just concatenate with UNION ALL comment
        return (clinical_sql.rstrip()
                + "\n\n-- UNION ALL with pathology notes (Script 4 Part B)\n-- "
                + "Combine manually if merge failed:\n"
                + notes_sql)

    # Insert notes CTEs after the last CTE closing paren but before the final SELECT
    clinical_pre  = "\n".join(lines[:final_select_idx])
    clinical_post = "\n".join(lines[final_select_idx:])
    return clinical_pre + "\n" + notes_body.split("SELECT")[0].rstrip() + "\n\n" + clinical_post + separator + "SELECT pat_id, mrn, index_dx_date, cancer_type, result_domain, source_record_id, source_date, subtype_label, icd10_code, icd10_description, text_content FROM s4_clinical_notes ORDER BY pat_id, result_domain, source_date"
