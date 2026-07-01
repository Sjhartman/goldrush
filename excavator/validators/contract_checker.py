"""
Cohort Contract Checker.

Makes a Claude API call to verify that every large-table scan in a script
joins eligible_cohort as its first join. Supplements the Python heuristic
in databricks.py with semantic reasoning for edge cases.
"""

import os

import anthropic

MODEL = os.environ.get("ANTHROPIC_MODEL", "claude-sonnet-4-6")

_LARGE_TABLES_LIST = (
    "PAT_ENC_DX, PROBLEM_LIST, HSP_DISCH_DIAG, HSP_ACCT_DX_LIST, PAT_ENC, PAT_ENC_HSP, "
    "PATIENT, EDG_CURRENT_ICD10, EXTERNAL_DEATH_REPORTS, V_CANCER_STAGING, TPL_INFO, "
    "ENROLL_INFO, HNO_INFO, HNO_NOTE_TEXT, PAT_ADDR_CHNG_HX, IDENTITY_ID"
)

_CONTRACT_TOOL = {
    "name": "submit_contract_check",
    "description": "Submit the cohort contract check result for one SQL script.",
    "input_schema": {
        "type": "object",
        "properties": {
            "passed": {
                "type": "boolean",
                "description": "True if all large-table CTEs join eligible_cohort as their first join",
            },
            "violations": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "cte_name":    {"type": "string"},
                        "table":       {"type": "string"},
                        "issue":       {"type": "string"},
                        "remediation": {"type": "string"},
                    },
                    "required": ["cte_name", "table", "issue", "remediation"],
                },
            },
        },
        "required": ["passed", "violations"],
    },
}


def check_script(
    client: anthropic.Anthropic,
    label: str,
    sql: str,
) -> dict:
    """
    Check one SQL script for cohort contract compliance.
    Returns dict with keys: passed, violations.
    """
    prompt = f"""You are reviewing a Databricks SQL script for cohort contract compliance.

THE CONTRACT: Every CTE that reads a large raw table MUST join `eligible_cohort` as
its VERY FIRST join. An intermediate "raw scan" CTE that reads the large table without
a cohort join -- even if a subsequent CTE joins eligible_cohort -- is a violation.

LARGE TABLES REQUIRING THIS TREATMENT:
{_LARGE_TABLES_LIST}

Also check:
- No NOT IN (SELECT ... FROM curated...) patterns (use LEFT ANTI JOIN instead)
- No CTE redefines eligible_cohort or excluded_patients

SCRIPT ({label}):
{sql}

Call submit_contract_check with your findings. Be precise about which CTE and table
each violation involves and how to fix it."""

    response = client.messages.create(
        model=MODEL,
        max_tokens=2048,
        tools=[_CONTRACT_TOOL],
        tool_choice={"type": "tool", "name": "submit_contract_check"},
        messages=[{"role": "user", "content": prompt}],
    )
    for block in response.content:
        if block.type == "tool_use" and block.name == "submit_contract_check":
            return block.input

    return {"passed": True, "violations": []}


def check_all(
    client: anthropic.Anthropic,
    scripts: dict,
) -> dict:
    """
    Check all scripts in parallel. Returns {label: result_dict}.
    """
    from concurrent.futures import ThreadPoolExecutor

    results = {}

    def _check(label_sql):
        label, sql = label_sql
        if not sql:
            return label, {"passed": True, "violations": []}
        return label, check_script(client, label, sql)

    with ThreadPoolExecutor(max_workers=4) as ex:
        futures = {ex.submit(_check, item): item[0] for item in scripts.items()}
        for future in futures:
            label, result = future.result()
            results[label] = result

    return results


def print_contract_results(results: dict) -> None:
    any_fail = any(not r.get("passed") for r in results.values())
    status   = "FAIL" if any_fail else "OK"
    print(f"\nCohort Contract Check: {status}")
    for label, result in results.items():
        violations = result.get("violations", [])
        if not violations:
            print(f"  {label}: OK")
        else:
            print(f"  {label}: {len(violations)} violation(s)")
            for v in violations:
                print(f"    CTE {v['cte_name']} / {v['table']}: {v['issue']}")
                print(f"    Fix: {v['remediation']}")