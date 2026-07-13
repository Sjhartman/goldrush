"""
Specialist: patient demographics (Script 2).

Extracts patient attributes: sex, race, ethnicity, date of birth, MRN,
marital status, language, enterprise identity IDs, insurance coverage class.
One row per patient.
"""

import json
import os

import anthropic

from .shared.prompts import specialist_prompt

MODEL = os.environ.get("ANTHROPIC_MODEL", "claude-sonnet-4-6")

_DOMAIN_ADDITIONS = """
DEMOGRAPHICS SPECIALIST RULES:

OUTPUT STRUCTURE:
- One row per patient. Do NOT use UNION ALL to stack multiple record types.
- The main SELECT produces exactly one row per patient with all demographic columns.
- Multi-row sources (identity IDs, insurance) are defined as separate CTEs but are NOT
  selected in the main output -- they are available for analysts to query by joining on PAT_ID.
- Do NOT self-censor columns based on assumptions about PHI or data minimization.
  Only exclude what is explicitly listed in DENIED / AMBIGUOUS.

IDENTITY_ID table:
- IDENTITY_TYPE_ID = 1008 is the enterprise MRN at BJH/WashU.
- May contain multiple rows per patient for different identity systems.
- Join on PAT_ID, filter to identity_type_id = 1008 for the BJH MRN.

PATIENT_RACE table:
- Contains one row per race entry per patient (patients may have multiple).
- Decode patient_race_c by joining ZC_PATIENT_RACE on patient_race_c, select NAME.
- Aggregate multiple races into a list (COLLECT_LIST or CONCAT_WS).

Confirmed PATIENT column names (use exactly as listed):
- Sex:       PATIENT.sex  (already a decoded string -- NO ZC join needed)
- Ethnicity: PATIENT.ethnic_group_c -> join ZC_ETHNIC_GROUP on ethnic_group_c, select name
- Race:      PATIENT_RACE.patient_race_c -> join ZC_PATIENT_RACE on patient_race_c, select name
- MRN:       PATIENT.pat_mrn_id
- Name:      PATIENT.pat_name (or pat_first_name, pat_last_name, pat_middle_name)
- DOB:       PATIENT.birth_date
- Death:     PATIENT.death_date

ZC tables that do NOT exist in this data lake -- never reference them:
- ZC_MARITAL, ZC_ETHNIC_BACKGROUND, ZC_SEX (sex_c column does not exist; use PATIENT.sex)

ETHNIC BACKGROUND (detailed multi-row table):
- ETHNIC_BACKGROUND table: columns are pat_id, line, ethnic_bkgrnd_c
- Decode ethnic_bkgrnd_c by joining ZC_ETHNIC_BKGRND (NOT ZC_ETHNIC_BACKGROUND) on ethnic_bkgrnd_c
- ZC_ETHNIC_BKGRND columns: ethnic_bkgrnd_c, name, title, abbr
- OMB HIGH-LEVEL ethnicity: PATIENT.ethnic_group_c -> join ZC_ETHNIC_GROUP on ethnic_group_c
- Column alias for OMB ethnicity category: use `ethnicity_omb_category` (OMB = Office of Management and Budget, NOT OMG)

PATIENT table cohort join (cohort first, always):
    FROM curated.epic_clarity.patient pt
    INNER JOIN eligible_cohort ec ON ec.PAT_ID = pt.PAT_ID

FORBIDDEN CTEs -- NEVER define any of these; they are already in the embedded cohort block:
    tempus_patients, tempus_pat_ids, cohort_icd, gi_hpb_icd, gi_hpb_icd_codes,
    dx_enc, dx_prob, dx_disch, dx_all, dx_index, dx_index_detail, dx_min, dx_final,
    dx_index_code, patient_demo, excluded_patients, eligible_cohort

Your WITH clause must begin immediately with a demographics-specific CTE (e.g.,
patient_demographics, race_agg, identity_ids). If you find yourself writing
tempus_patients or any other name from the FORBIDDEN list above, delete that block
and start from eligible_cohort instead.

COLUMN INCLUSION RULE: Only include columns that map to an approved element in this
request. Standard demographics columns (sex, race, ethnicity, birth date, death date,
MRN, patient name) are generally safe. Do NOT include marital_status_c or language_c
unless they appear explicitly in the APPROVED ELEMENTS list for this request.

DO NOT include address columns -- address history is a separate script (Script 3).
DO NOT include staging, mortality, enrollment, or treatment plan columns.
"""

SYSTEM_PROMPT = specialist_prompt(_DOMAIN_ADDITIONS)

_DEMO_TABLES = {
    "PATIENT", "PATIENT_RACE", "IDENTITY_ID",
    "ZC_PATIENT_RACE", "ZC_ETHNIC_GROUP",
}


def generate(
    client: anthropic.Anthropic,
    fields: dict,
    clarity_elements: list,
    schemas: dict,
) -> str:
    """
    Generate the demographics SQL (Script 2).
    Returns raw SQL (fences not yet stripped).
    """
    element_list = "\n".join(f"- {e['element']}" for e in clarity_elements)
    blocked      = fields["denied"] + fields["ambiguous"]
    blocked_list = "\n".join(f"- {e['element']}" for e in blocked) or "None"

    demo_schemas = {k: v for k, v in schemas.items()
                    if any(kw in k for kw in (
                        "PATIENT", "ETHNIC", "IDENTITY",
                        "ZC_SEX", "ZC_PATIENT_RACE", "ZC_ETHNIC",
                        "ZC_MARITAL", "ZC_LANGUAGE",
                    ))}
    schema_block = "\n\n---\n\n".join(f"TABLE: {k}\n{v}" for k, v in demo_schemas.items())

    prompt = f"""Generate Databricks SQL -- Script 2 of 6: Patient Demographics.

IMPORTANT: This script is embedded after Script 1. The following CTEs already exist --
do NOT write them; start your WITH clause with a demographics-specific CTE instead:
  eligible_cohort, excluded_patients, tempus_patients, tempus_pat_ids,
  cohort_icd, gi_hpb_icd, dx_enc, dx_prob, dx_disch, dx_all,
  dx_index, dx_index_detail, patient_demo

eligible_cohort columns available: PAT_ID, mrn, index_dx_date, cancer_type,
  index_icd10_code, index_dx_source, age_at_dx, age_stratum

APPROVED ELEMENTS (demographics only -- no staging, notes, addresses, or Tempus):
{element_list}

DENIED / AMBIGUOUS -- exclude from every SELECT:
{blocked_list}

SCHEMAS:
{schema_block}

Header comment: Script 2 of 6, Patient Demographics.
Return ONLY valid Databricks SQL -- no markdown fences."""

    response = client.messages.create(
        model=MODEL,
        max_tokens=16384,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": prompt}],
    )
    return response.content[0].text.strip()
