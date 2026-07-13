"""
Schema validation against the actual data lake column list.
Validates curated.epic_clarity references and curated.tempus references.
Auto-fix uses a Claude API call to correct detected errors.
"""

import csv
import re
from pathlib import Path

import anthropic

GOLDRUSH_DIR   = Path(__file__).parent.parent.parent
SCHEMAS_DIR    = GOLDRUSH_DIR / "schemas"
COLUMNS_FILE   = SCHEMAS_DIR / "epic_clarity_columns.tsv"
TEMPUS_COLUMNS = SCHEMAS_DIR / "tempus_columns.tsv"

# All Tempus tables whose columns are passed to the specialist LLM.
# When a versioned (_v2) table supersedes an older one, include only the newer version.
TEMPUS_SCHEMA_TABLES = [
    # Core identifiers / order
    "patient",
    "order",
    "report",
    "specimens_v2",       # preferred over specimens
    "results",
    # Somatic variants (clinically reported -- flat, one row per variant)
    "somaticpotentiallyactionablemutations",
    "somaticpotentiallyactionablemutationsvariants",  # has allelicFraction (VAF)
    "somaticbiologicallyrelevantvariants",            # includes fusions, has allelicFraction
    "somaticvariantsofunknownsignificance",           # somatic VUS, has allelicFraction
    "somaticpotentiallyactionablecopynumbervariants", # CNV
    # RNA fusions
    "fusionvariants",
    "rnafindings",
    # Germline findings (clinically reported -- flat, one row per variant)
    "inheritedrelevantvariantsvalues",
    "inheritedincidentalfindingsvalues",
    "inheritedvariantsofunknownsignificancevalues",
]

_MODEL = None  # set at runtime from env or default


def _get_model():
    import os
    global _MODEL
    if _MODEL is None:
        _MODEL = os.environ.get("ANTHROPIC_MODEL", "claude-sonnet-4-6")
    return _MODEL


def load_actual_schema() -> dict:
    """Load epic_clarity_columns.tsv into {TABLE_UPPER: {COL_UPPER, ...}}."""
    if not COLUMNS_FILE.exists():
        return {}
    schema = {}
    with open(COLUMNS_FILE, encoding="utf-8") as f:
        for row in csv.DictReader(f, delimiter="\t"):
            table = row["table_name"].upper()
            col   = row["col_name"].upper()
            schema.setdefault(table, set()).add(col)
    return schema


def load_tempus_schema() -> dict:
    """Load tempus_columns.tsv into {TABLE_LOWER: {col_lower, ...}}."""
    if not TEMPUS_COLUMNS.exists():
        return {}
    schema = {}
    with open(TEMPUS_COLUMNS, encoding="utf-8") as f:
        for row in csv.DictReader(f, delimiter="\t"):
            table = row["table_name"].lower()
            col   = row["col_name"].lower()
            schema.setdefault(table, set()).add(col)
    return schema


def build_tempus_schema_context(tempus_schema: dict) -> str:
    """Build a schema block for all Tempus tables used by the specialist."""
    lines = []
    for t in TEMPUS_SCHEMA_TABLES:
        cols = tempus_schema.get(t)
        if cols:
            lines.append(f"curated.tempus.{t}: {', '.join(sorted(cols))}")
    return "\n".join(lines)


def validate_sql(sql: str, actual_schema: dict, label: str) -> list:
    """
    Check every curated.epic_clarity table/column reference in the SQL against
    the actual column list. Returns a list of (severity, message) tuples.
    """
    if not actual_schema:
        return []

    errors = []
    sql_no_comments = re.sub(r'--[^\n]*', '', sql)

    cte_names = {m.upper() for m in re.findall(r'\b(\w+)\s+AS\s*\(', sql, re.IGNORECASE)}

    _SQL_KW = {
        'WHERE', 'ON', 'INNER', 'LEFT', 'RIGHT', 'OUTER', 'CROSS', 'JOIN',
        'GROUP', 'ORDER', 'HAVING', 'UNION', 'LIMIT', 'OFFSET', 'AND', 'OR',
        'NOT', 'IN', 'IS', 'NULL', 'AS', 'FROM', 'SELECT', 'WITH', 'BY',
        'SET', 'INTO', 'USING', 'LATERAL', 'TABLESAMPLE', 'PIVOT', 'UNPIVOT',
    }

    alias_to_table = {}
    ambiguous_aliases = set()
    for m in re.finditer(
        r'(?:FROM|JOIN)\s+curated\.epic_clarity\.(\w+)(?:\s+(?:AS\s+)?(\w+))?',
        sql_no_comments, re.IGNORECASE
    ):
        table = m.group(1).upper()
        raw   = m.group(2)
        alias = (raw.upper() if raw and raw.upper() not in _SQL_KW else table)
        if alias in alias_to_table and alias_to_table[alias] != table:
            ambiguous_aliases.add(alias)
        else:
            alias_to_table[alias] = table

        if table not in actual_schema:
            errors.append(("ERROR", f"Table not in data lake: curated.epic_clarity.{m.group(1)}"))

    for m in re.finditer(
        r'(?:FROM|JOIN)\s+curated\.tempus\.\S+\s+(?:AS\s+)?(\w+)',
        sql_no_comments, re.IGNORECASE
    ):
        alias = m.group(1).upper()
        if alias in _SQL_KW:
            continue
        if alias in alias_to_table:
            ambiguous_aliases.add(alias)

    for m in re.finditer(r'(?:FROM|JOIN)\s+(\w+)\s+(?:AS\s+)?(\w+)', sql_no_comments, re.IGNORECASE):
        cte_ref = m.group(1).upper()
        alias   = m.group(2).upper()
        if alias in _SQL_KW:
            continue
        if cte_ref in cte_names and alias in alias_to_table:
            ambiguous_aliases.add(alias)

    for m in re.finditer(r'\)\s+(?:AS\s+)?(\w+)', sql_no_comments, re.IGNORECASE):
        alias = m.group(1).upper()
        if alias in _SQL_KW:
            continue
        if alias in alias_to_table:
            ambiguous_aliases.add(alias)

    seen = set()
    for m in re.finditer(r'\b([A-Za-z_]\w*)\.([A-Za-z_]\w*)\b', sql_no_comments):
        alias = m.group(1).upper()
        col   = m.group(2).upper()

        if alias not in alias_to_table or alias in cte_names or alias in ambiguous_aliases:
            continue
        if alias in ("CURATED", "EPIC_CLARITY"):
            continue

        table = alias_to_table[alias]
        key   = (table, col)
        if key in seen:
            continue
        seen.add(key)

        if table in actual_schema and col not in actual_schema[table]:
            errors.append(("ERROR", f"{table}.{col} -- column not found in data lake"))

    return errors


def validate_tempus_sql(sql: str, tempus_schema: dict, label: str) -> list:
    """
    Check every curated.tempus.<table>.<col> reference in the SQL.
    Returns list of (severity, message). Report-only -- no auto-fix.
    """
    if not tempus_schema:
        return []

    errors = []
    sql_no_comments = re.sub(r'--[^\n]*', '', sql)

    for m in re.finditer(
        r'curated\.tempus\.`?(\w+)`?\.(\w+)',
        sql_no_comments, re.IGNORECASE
    ):
        table = m.group(1).lower()
        col   = m.group(2).lower()
        if table in tempus_schema and col not in tempus_schema[table]:
            errors.append(("ERROR",
                f"curated.tempus.{table}.{col} -- column not found in tempus schema"))

    return errors


_FIX_TOOL = {
    "name": "submit_sql_fix",
    "description": "Submit the corrected SQL and a list of every fix applied.",
    "input_schema": {
        "type": "object",
        "properties": {
            "fixed_sql": {"type": "string"},
            "fixes": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "wrong":     {"type": "string"},
                        "corrected": {"type": "string"},
                        "table":     {"type": "string"},
                        "reason":    {"type": "string"},
                    },
                    "required": ["wrong", "corrected", "table", "reason"],
                },
            },
        },
        "required": ["fixed_sql", "fixes"],
    },
}


def fix_sql_errors(
    client: anthropic.Anthropic,
    sql: str,
    errors: list,
    actual_schema: dict,
) -> tuple:
    """
    Make a Claude API call to correct schema validation errors.
    Returns (fixed_sql, list_of_fix_dicts).
    """
    error_tables = set()
    for _, msg in errors:
        m = re.match(r'([A-Z_]+)\.', msg)
        if m:
            error_tables.add(m.group(1).upper())
        m2 = re.search(r'epic_clarity\.(\w+)', msg, re.IGNORECASE)
        if m2:
            error_tables.add(m2.group(1).upper())

    schema_context = "\n".join(
        f"{t}: {', '.join(sorted(actual_schema[t]))}"
        for t in sorted(error_tables)
        if t in actual_schema
    )
    error_list = "\n".join(f"- {msg}" for _, msg in errors)

    prompt = f"""The SQL below has column or table reference errors found by a schema validator.
Fix ONLY the specific errors listed. Do not change any other SQL logic, structure, or comments.

ERRORS TO FIX:
{error_list}

ACTUAL COLUMNS FOR THE AFFECTED TABLES (from the real data lake):
{schema_context}

SQL:
{sql}

Call submit_sql_fix with the corrected SQL and one fix entry per change made."""

    with client.messages.stream(
        model=_get_model(),
        max_tokens=32768,
        tools=[_FIX_TOOL],
        tool_choice={"type": "tool", "name": "submit_sql_fix"},
        messages=[{"role": "user", "content": prompt}],
    ) as stream:
        response = stream.get_final_message()
    for block in response.content:
        if block.type == "tool_use" and block.name == "submit_sql_fix":
            if "fixed_sql" not in block.input:
                print("  WARNING: fix call response truncated, returning original SQL")
                return sql, []
            return block.input["fixed_sql"], block.input.get("fixes", [])
    raise RuntimeError("Fix call did not return structured output")


def build_fix_log(irb_summary: dict, fix_results: dict, timestamp: str) -> str:
    """Build a markdown fix log recording every auto-correction applied."""
    irb = irb_summary
    lines = [
        f"# Schema Fix Log -- {irb.get('pi_name', 'Unknown PI')} "
        f"(IRB #{irb.get('protocol_number', 'N/A')})",
        f"_Generated: {timestamp}_\n",
        "Corrections applied automatically after validating generated SQL against "
        "the actual `curated.epic_clarity` column list (`epic_clarity_columns.tsv`).\n",
        "Review each fix before running the SQL in production.\n",
    ]
    for label, result in fix_results.items():
        fixes = result.get("fixes", [])
        if not result.get("had_errors"):
            lines += [f"## {label} -- OK (no fixes needed)", ""]
            continue
        lines += [
            f"## {label} -- {len(fixes)} fix(es) applied",
            "",
            "| Wrong reference | Corrected to | Table | Reason |",
            "| --- | --- | --- | --- |",
        ]
        for f in fixes:
            w = f.get("wrong", "?").replace("|", "/")
            c = f.get("corrected", "?").replace("|", "/")
            t = f.get("table", "?").replace("|", "/")
            r = f.get("reason", "").replace("|", "/")
            lines.append(f"| `{w}` | `{c}` | {t} | {r} |")
        lines.append("")
    return "\n".join(lines)
