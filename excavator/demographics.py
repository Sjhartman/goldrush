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

ZC decode rules:
- sex_c -> join ZC_SEX on sex_c, select NAME
- ethnic_background_c -> join ZC_ETHNIC_BACKGROUND on ethnic_background_c, select NAME
- marital_status_c -> join ZC_MARITAL on marital_status_c, select NAME
- language_c -> join ZC_LANGUAGE on language_c, select NAME

PATIENT table cohort join (cohort first, always):
    FROM curated.epic_clarity.patient pt
    INNER JOIN eligible_cohort ec ON ec.PAT_ID = pt.PAT_ID

DO NOT include address columns -- address history is a separate script (Script 3).
DO NOT include staging, mortality, enrollment, or treatment plan columns.
"""

SYSTEM_PROMPT = specialist_prompt(_DOMAIN_ADDITIONS)

_DEMO_TABLES = {
    "PATIENT", "PATIENT_RACE", "ETHNIC_BACKGROUND", "IDENTITY_ID",
    "ZC_SEX", "ZC_PATIENT_RACE", "ZC_ETHNIC_BACKGROUND", "ZC_MARITAL",
    "ZC_LANGUAGE", "ZC_LANGUAGE_BSLN",
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

The following CTEs are already defined in the embedded cohort block -- reference them
directly, do NOT redefine or redeclare any of them:
- `eligible_cohort (PAT_ID, mrn, index_dx_date, cancer_type, age_at_dx, age_stratum)`
- `excluded_patients (PAT_ID)`

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
