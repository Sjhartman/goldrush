"""
SQL post-processing utilities: stripping fences, extracting CTE blocks,
embedding the cohort CTE block into extraction scripts.
"""

import re


def strip_fences(sql: str) -> str:
    """Remove markdown code fences if Claude included them despite instructions."""
    sql = sql.strip()
    if sql.startswith("```"):
        first_newline = sql.find('\n')
        sql = sql[first_newline + 1:] if first_newline != -1 else sql[3:]
        last_fence = sql.rfind('```')
        if last_fence != -1:
            sql = sql[:last_fence].rstrip()
    return sql.strip()


def extract_cte_block(sql: str) -> str:
    """Return everything up to and including the closing paren of the last CTE.

    Tracks bracket depth while skipping string literals and comments so that
    nested parens inside CTE bodies don't confuse the search.
    """
    depth = 0
    last_close = -1
    in_line = in_block = in_str = False
    q = None
    i = 0
    while i < len(sql):
        c = sql[i]
        if in_line:
            if c == '\n':
                in_line = False
        elif in_block:
            if sql[i:i+2] == '*/':
                in_block = False
                i += 1
        elif in_str:
            if c == q:
                in_str = False
        else:
            if sql[i:i+2] == '--':
                in_line = True
                i += 1
            elif sql[i:i+2] == '/*':
                in_block = True
                i += 1
            elif c in ("'", '"', '`'):
                in_str = True
                q = c
            elif c == '(':
                depth += 1
            elif c == ')':
                depth -= 1
                if depth == 0:
                    last_close = i
        i += 1
    return sql[:last_close + 1].strip() if last_close != -1 else sql


def _strip_leading_comments(sql: str) -> str:
    """Remove leading comment lines and blank lines, returning SQL starting at WITH."""
    lines = sql.splitlines(keepends=True)
    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped and not stripped.startswith('--') and not stripped.startswith('/*'):
            return ''.join(lines[i:])
    return sql


def _collapse_comment_blanks(text: str) -> str:
    """Remove blank lines that fall between consecutive comment-only lines.

    A blank line between two pure-comment blocks is treated as a statement
    boundary by the Azure Databricks SQL editor.
    """
    lines = text.splitlines(keepends=True)
    result = []
    for i, line in enumerate(lines):
        if line.strip() == '':
            prev_code = next(
                (lines[j].strip() for j in range(i - 1, -1, -1) if lines[j].strip()),
                None
            )
            next_code = next(
                (lines[j].strip() for j in range(i + 1, len(lines)) if lines[j].strip()),
                None
            )
            if (prev_code and prev_code.startswith('--') and
                    next_code and next_code.startswith('--')):
                continue
        result.append(line)
    return ''.join(result)


def _strip_first_leading_comma(text: str) -> str:
    """Remove the leading comma from the first non-blank, non-comment line."""
    lines = text.splitlines(keepends=True)
    for i, line in enumerate(lines):
        stripped = line.strip()
        if not stripped or stripped.startswith('--'):
            continue
        if stripped.startswith(','):
            lines[i] = line.replace(',', '', 1)
        break
    return ''.join(lines)


def embed_cohort(cohort_sql: str, extraction_sql: str) -> str:
    """Prepend the cohort CTE block into an extraction script.

    cohort_sql must already be normalised (fences stripped, column names fixed).
    extraction_sql should be stripped of fences before calling.
    The result is a self-contained query that reads only from the data lake.
    """
    cte_block = _strip_leading_comments(extract_cte_block(cohort_sql))

    extraction = extraction_sql.replace(
        'curated.epic_clarity.eligible_cohort', 'eligible_cohort'
    )

    with_pos = None
    pos = 0
    for line in extraction.splitlines(keepends=True):
        code_part = re.sub(r'--[^\n]*', '', line)
        m = re.search(r'\bWITH\b', code_part, re.IGNORECASE)
        if m:
            with_pos = pos + m.start()
            with_end = pos + m.end()
            break
        pos += len(line)

    if with_pos is not None:
        header     = extraction[:with_pos]
        after_with = _strip_first_leading_comma(extraction[with_end:])
        return header + cte_block + ',\n' + _collapse_comment_blanks(after_with)
    return cte_block + ',\n' + _collapse_comment_blanks(_strip_first_leading_comma(extraction))


def normalize_cohort_sql(sql: str) -> str:
    """Strip fences, fix canonical column name, normalize CTE name."""
    import re as _re
    sql = strip_fences(sql)
    sql = sql.replace('index_cancer_type', 'cancer_type')
    sql = _re.sub(r'\bfinal_cohort\b', 'eligible_cohort', sql)
    sql = _re.sub(r'\bDATETIME\b', 'TIMESTAMP', sql)
    sql = _collapse_comment_blanks(sql)
    return sql


def normalize_extraction_sql(sql: str) -> str:
    """Strip fences, replace DATETIME, collapse comment blanks."""
    import re as _re
    sql = strip_fences(sql)
    sql = _re.sub(r'\bDATETIME\b', 'TIMESTAMP', sql)
    sql = _collapse_comment_blanks(sql)
    return sql
