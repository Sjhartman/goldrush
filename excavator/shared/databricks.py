"""
Databricks SQL syntax and performance checks.
No API calls -- pure text analysis.
"""

import re

# Tables large enough that scanning them more than once is worth flagging
_LARGE_TABLES = {
    'PAT_ENC_DX', 'PROBLEM_LIST', 'HSP_DISCH_DIAG', 'HSP_ACCT_DX_LIST',
    'PAT_ENC', 'PAT_ENC_HSP', 'CLARITY_EDG', 'EDG_CURRENT_ICD10',
    'PATIENT', 'EXTERNAL_DEATH_REPORTS', 'ENROLL_INFO', 'TPL_INFO',
    'V_CANCER_STAGING', 'PAT_ADDR_CHNG_HX', 'IDENTITY_ID',
    'HNO_INFO', 'HNO_NOTE_TEXT',
}


def _top_level_commas(sql: str) -> list:
    """Return (line_number, char_position) of every comma at CTE depth 0."""
    depth = 0
    in_comment = False
    result = []
    i = 0
    while i < len(sql):
        c = sql[i]
        if in_comment:
            if c == '\n':
                in_comment = False
        elif sql[i:i+2] == '--':
            in_comment = True
            i += 2
            continue
        elif c == '(':
            depth += 1
        elif c == ')':
            depth -= 1
        elif c == ',' and depth == 0:
            result.append((sql[:i].count('\n') + 1, i))
        i += 1
    return result


def check_sql_syntax(sql: str, label: str) -> list:
    """
    Detect Databricks-specific syntax problems.
    Returns list of (severity, message).
    severity: 'ERROR' for definite failures, 'WARN' for likely problems.
    """
    issues = []
    lines = sql.splitlines()

    # Blank line sandwiched between two comment-only lines
    for i, line in enumerate(lines):
        if line.strip() == '':
            prev = next((lines[j].strip() for j in range(i - 1, -1, -1)
                         if lines[j].strip()), '')
            nxt  = next((lines[j].strip() for j in range(i + 1, len(lines))
                         if lines[j].strip()), '')
            if prev.startswith('--') and nxt.startswith('--'):
                issues.append(('ERROR',
                    f"line {i + 1}: blank line between comment blocks "
                    f"(Databricks treats this as a statement boundary)"))

    # Consecutive top-level commas
    commas = _top_level_commas(sql)
    for idx in range(1, len(commas)):
        prev_line, prev_pos = commas[idx - 1]
        curr_line, curr_pos = commas[idx]
        between = sql[prev_pos + 1:curr_pos]
        has_real_code = any(
            ln.strip() and not ln.strip().startswith('--')
            for ln in between.splitlines()
        )
        if not has_real_code:
            issues.append(('ERROR',
                f"lines {prev_line}-{curr_line}: double top-level comma "
                f"(only comments between them)"))

    # Trailing semicolon
    if sql.rstrip().endswith(';'):
        issues.append(('ERROR', "trailing semicolon after final SELECT"))

    # Non-ASCII characters
    for i, line in enumerate(lines):
        bad = [c for c in line if ord(c) > 127]
        if bad:
            issues.append(('ERROR',
                f"line {i + 1}: non-ASCII characters {bad[:3]} "
                f"(Databricks tokeniser rejects Unicode in SQL text)"))
            break

    # Block comments
    if '/*' in sql:
        issues.append(('WARN', "block comment /* */ found -- use -- line comments only"))

    # DATETIME type
    for i, line in enumerate(lines):
        if re.search(r'\bDATETIME\b', line, re.IGNORECASE):
            issues.append(('ERROR',
                f"line {i + 1}: DATETIME is not a valid Databricks type -- use TIMESTAMP"))
            break

    return issues


def check_sql_performance(sql: str, label: str) -> list:
    """
    Detect SQL performance anti-patterns.
    Returns list of (severity, message).
    """
    issues = []

    # Count raw-table scans (FROM + JOIN references)
    raw_refs = re.findall(
        r'(?:FROM|JOIN)\s+curated\.epic_clarity\.(\w+)',
        sql, re.IGNORECASE
    )
    counts = {}
    for t in raw_refs:
        counts[t.upper()] = counts.get(t.upper(), 0) + 1
    for table, n in sorted(counts.items()):
        if n > 1 and table in _LARGE_TABLES:
            issues.append(('WARN',
                f"{table} scanned {n}x -- merge into one CTE or use an alias"))

    # Correlated NOT IN with a subquery that hits a raw table
    corr = re.compile(
        r'\bNOT\s+IN\s*\(\s*SELECT\b[^)]{0,400}FROM\s+curated',
        re.IGNORECASE | re.DOTALL
    )
    for m in corr.finditer(sql):
        ln = sql[:m.start()].count('\n') + 1
        issues.append(('ERROR',
            f"line {ln}: NOT IN (SELECT ... FROM curated...) -- "
            f"correlated subquery causes repeated full-table scan; "
            f"use LEFT ANTI JOIN instead"))

    # IN (SELECT PAT_ID FROM <CTE>) on a raw-table scan without cohort join
    in_sub = re.compile(
        r'\bIN\s*\(\s*SELECT\s+PAT_ID\s+FROM\s+(\w+)\s*\)',
        re.IGNORECASE
    )
    for m in in_sub.finditer(sql):
        cte_name = m.group(1)
        ln = sql[:m.start()].count('\n') + 1
        snippet = sql[max(0, m.start()-300):m.start()]
        outer = re.findall(r'FROM\s+curated\.epic_clarity\.(\w+)', snippet, re.IGNORECASE)
        if outer and outer[-1].upper() in _LARGE_TABLES:
            issues.append(('WARN',
                f"line {ln}: {outer[-1]} filtered by IN (SELECT PAT_ID FROM {cte_name}) -- "
                f"consider INNER JOIN {cte_name} for better push-down"))

    return issues


def run_quality_checks(sql: str, label: str) -> bool:
    """Run both checkers, print results, return True if any ERRORs found."""
    syn  = check_sql_syntax(sql, label)
    perf = check_sql_performance(sql, label)
    all_issues = syn + perf
    if not all_issues:
        return False
    errors = [m for s, m in all_issues if s == 'ERROR']
    warns  = [m for s, m in all_issues if s == 'WARN']
    if errors:
        print(f"  {label}: {len(errors)} syntax error(s), {len(warns)} perf warning(s)")
        for m in errors:
            print(f"    [ERROR] {m}")
        for m in warns:
            print(f"    [WARN]  {m}")
    elif warns:
        print(f"  {label}: {len(warns)} perf warning(s)")
        for m in warns:
            print(f"    [WARN]  {m}")
    return bool(errors)
