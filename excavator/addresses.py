"""
Specialist: address history (Script 3).

Extracts residential address history from PAT_ADDR_CHNG_HX and current address
from PATIENT_ADDRESS. Output is in long format -- one row per address period per patient.
"""

import os

import anthropic

from .shared.prompts import specialist_prompt

MODEL = os.environ.get("ANTHROPIC_MODEL", "claude-sonnet-4-6")

_DOMAIN_ADDITIONS = """
ADDRESSES SPECIALIST RULES:

OUTPUT STRUCTURE:
- Long format: one row per address period per patient.
- Include effective date range (eff_start_date, eff_end_date) for historical records.
- Current address (PATIENT_ADDRESS) has no end date -- set eff_end_date to NULL.
- Combine historical (PAT_ADDR_CHNG_HX) and current (PATIENT_ADDRESS) using UNION ALL.

PAT_ADDR_CHNG_HX table:
- Contains historical address changes with effective date ranges.
- Key columns: addr_1, addr_2, city, state_c (decode via ZC_STATE), zip, county_c,
  eff_start_date, eff_end_date.
- Cohort join (first join, always):
    FROM curated.epic_clarity.pat_addr_chng_hx a
    INNER JOIN eligible_cohort ec ON ec.PAT_ID = a.PAT_ID

PATIENT_ADDRESS table:
- Contains the current address. No effective date range.
- Join on PAT_ID to eligible_cohort as first join.

ZC_STATE decode: join on state_c, select NAME as state_name.
ZC_COUNTY decode: join on county_c, select NAME as county_name.

GEOCODING CONTEXT:
- Downstream geocoding will join on ZIP and/or full address string.
- Always include zip (VARCHAR, may be 5-digit or 9-digit) as a separate column.
- Include addr_1 and city as separate columns -- do not concatenate pre-emptively.

DO NOT include demographic columns (sex, race, DOB) -- those are in Script 2.
"""

SYSTEM_PROMPT = specialist_prompt(_DOMAIN_ADDITIONS)


def generate(
    client: anthropic.Anthropic,
    fields: dict,
    clarity_elements: list,
    schemas: dict,
) -> str:
    """
    Generate the address history SQL (Script 3).
    Returns raw SQL (fences not yet stripped).
    """
    element_list = "\n".join(f"- {e['element']}" for e in clarity_elements)
    blocked      = fields["denied"] + fields["ambiguous"]
    blocked_list = "\n".join(f"- {e['element']}" for e in blocked) or "None"

    addr_schemas = {k: v for k, v in schemas.items()
                    if any(kw in k for kw in (
                        "PAT_ADDR", "PATIENT_ADDRESS", "ZC_STATE", "ZC_COUNTY",
                    ))}
    schema_block = "\n\n---\n\n".join(f"TABLE: {k}\n{v}" for k, v in addr_schemas.items())

    prompt = f"""Generate Databricks SQL -- Script 3 of 6: Address History.

The following CTEs are already defined in the embedded cohort block -- reference them
directly, do NOT redefine or redeclare any of them:
- `eligible_cohort (PAT_ID, mrn, index_dx_date, cancer_type, age_at_dx, age_stratum)`
- `excluded_patients (PAT_ID)`

APPROVED ELEMENTS (address history only):
{element_list}

DENIED / AMBIGUOUS -- exclude from every SELECT:
{blocked_list}

SCHEMAS:
{schema_block}

Header comment: Script 3 of 6, Address History.
Return ONLY valid Databricks SQL -- no markdown fences."""

    response = client.messages.create(
        model=MODEL,
        max_tokens=8192,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": prompt}],
    )
    return response.content[0].text.strip()
