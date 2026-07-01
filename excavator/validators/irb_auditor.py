"""
IRB Compliance Auditor.

Makes a Claude API call to semantically verify that every SELECT column in
the generated SQL maps to an approved data element and that no denied/ambiguous
element appears anywhere. Cannot be done with Python regex -- requires semantic
reasoning about element-to-column mapping.
"""

import json
import os

import anthropic

MODEL = os.environ.get("ANTHROPIC_MODEL", "claude-sonnet-4-6")

_AUDIT_TOOL = {
    "name": "submit_irb_audit",
    "description": "Submit the IRB compliance audit result.",
    "input_schema": {
        "type": "object",
        "properties": {
            "passed": {
                "type": "boolean",
                "description": "True if no IRB compliance violations were found",
            },
            "violations": {
                "type": "array",
                "description": "List of compliance violations found",
                "items": {
                    "type": "object",
                    "properties": {
                        "script":      {"type": "string", "description": "Which script (e.g. Script 2 demographics)"},
                        "column":      {"type": "string", "description": "Column or expression that violates compliance"},
                        "issue":       {"type": "string", "description": "Why this is a violation"},
                        "severity":    {"type": "string", "enum": ["ERROR", "WARN"]},
                        "remediation": {"type": "string", "description": "How to fix it"},
                    },
                    "required": ["script", "column", "issue", "severity", "remediation"],
                },
            },
            "summary": {
                "type": "string",
                "description": "One paragraph summarizing the audit outcome",
            },
        },
        "required": ["passed", "violations", "summary"],
    },
}


def audit(
    client: anthropic.Anthropic,
    fields: dict,
    scripts: dict,
) -> dict:
    """
    Audit all generated SQL scripts for IRB compliance.

    fields: the extract_fields() dict from the audit JSON
    scripts: {label: sql_text} e.g. {"cohort": "...", "demographics": "..."}

    Returns the tool input dict with keys: passed, violations, summary.
    """
    approved_list = "\n".join(f"- {e['element']}: {e.get('rationale', '')}"
                              for e in fields["approved"])
    denied_list   = "\n".join(f"- {e['element']}: {e.get('rationale', e.get('reason', ''))}"
                              for e in fields["denied"] + fields["ambiguous"]) or "None"

    pop_filters = fields["request_summary"].get("population_filters", [])
    pop_text    = "\n".join(f"- {f}" for f in pop_filters) if pop_filters else "None specified"

    scripts_block = "\n\n".join(
        f"=== {label.upper()} ===\n{sql}"
        for label, sql in scripts.items()
        if sql
    )

    prompt = f"""You are an IRB compliance auditor reviewing Databricks SQL scripts generated
for a governed clinical data request.

Your job is to verify:
1. Every SELECT column maps to an approved data element (or is a necessary join key / cohort attribute).
2. No denied or ambiguous element appears in any SELECT clause, CTE output, or derived expression.
3. Population scope filters (age thresholds, date ranges, site restrictions) are enforced as WHERE
   clauses -- the scripts do not return a superset and leave filtering to the analyst.
4. Row-level restrictions in the IRB approval are implemented correctly.

APPROVED ELEMENTS (only these may appear in SELECT output):
{approved_list}

DENIED / AMBIGUOUS ELEMENTS (must not appear anywhere in SELECT output):
{denied_list}

APPROVED POPULATION SCOPE (must be enforced as WHERE filters, not post-hoc):
{pop_text}

GENERATED SQL SCRIPTS:
{scripts_block}

Review each script carefully. Call submit_irb_audit with your findings.
Be conservative -- flag anything semantically equivalent to a denied element even if
the column name differs (e.g. a 'social_security_number' column for a denied 'SSN' element).
Do not flag cohort attributes (PAT_ID, mrn, index_dx_date, cancer_type, age_at_dx,
age_stratum) or standard join keys as violations."""

    response = client.messages.create(
        model=MODEL,
        max_tokens=4096,
        tools=[_AUDIT_TOOL],
        tool_choice={"type": "tool", "name": "submit_irb_audit"},
        messages=[{"role": "user", "content": prompt}],
    )
    for block in response.content:
        if block.type == "tool_use" and block.name == "submit_irb_audit":
            return block.input

    return {"passed": True, "violations": [], "summary": "Audit call returned no structured output."}


def print_audit_result(result: dict) -> None:
    passed     = result.get("passed", True)
    violations = result.get("violations", [])
    summary    = result.get("summary", "")

    symbol = "OK" if passed else "FAIL"
    print(f"\nIRB Compliance Audit: {symbol}")
    if summary:
        print(f"  {summary}")
    if violations:
        errors = [v for v in violations if v.get("severity") == "ERROR"]
        warns  = [v for v in violations if v.get("severity") == "WARN"]
        for v in errors:
            print(f"  [ERROR] {v['script']}: {v['column']} -- {v['issue']}")
            print(f"          Remediation: {v['remediation']}")
        for v in warns:
            print(f"  [WARN]  {v['script']}: {v['column']} -- {v['issue']}")