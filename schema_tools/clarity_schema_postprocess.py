"""
Post-processes raw scraped schema markdown into clean, compact markdown,
generates index.md (full descriptions) and index_brief.md (one line per table,
used in excavator classification pass 1).

Usage:
    venv/bin/python tools/postprocess.py              # all raw_schemas/
    venv/bin/python tools/postprocess.py PAT_ENC ...  # specific tables only
"""

import re
import sys
from pathlib import Path

GOLDRUSH_DIR = Path(__file__).parent.parent
SCHEMAS_DIR  = GOLDRUSH_DIR / "schemas" / "raw_schemas"
CLEAN_DIR    = GOLDRUSH_DIR / "schemas" / "clean_schemas"
INDEX_FILE   = GOLDRUSH_DIR / "schemas" / "index.md"
INDEX_BRIEF  = GOLDRUSH_DIR / "schemas" / "index_brief.md"

CLEAN_DIR.mkdir(parents=True, exist_ok=True)

MAX_FK_ROWS = 30

SUBSECTION_LABELS = {
    "primary key",
    "index information",
    "grouped tables",
    "column information",
    "foreign key information",
    "advanced validations",
    "dependent database objects",
}


# ---------------------------------------------------------------------------
# Raw markdown parsing
# ---------------------------------------------------------------------------

def parse_md_rows(text: str) -> list:
    rows = []
    for line in text.splitlines():
        line = line.strip()
        if line.startswith("|") and not re.match(r"^\|[-| :]+\|$", line):
            cells = [c.strip() for c in line.strip("|").split("|")]
            rows.append(cells)
    return rows


def split_sections(text: str) -> dict:
    top: dict          = {}
    current_key        = "__top__"
    current_lines: list = []

    for line in text.splitlines():
        m = re.match(r"^#{1,4}\s+(.+)", line)
        if m:
            top[current_key] = current_lines
            current_key      = m.group(1).strip().lower()
            current_lines    = []
        else:
            current_lines.append(line)
    top[current_key] = current_lines

    sections: dict = {k: "\n".join(v) for k, v in top.items()
                      if k not in ("additional metadata",)}

    meta_body = "\n".join(top.get("additional metadata", []))
    sub_key   = "__meta_top__"
    sub_blocks: dict = {sub_key: []}

    for line in meta_body.splitlines():
        stripped = line.strip()
        if stripped.startswith("|") and not re.match(r"^\|[-| :]+\|$", stripped):
            cells = [c.strip() for c in stripped.strip("|").split("|")]
            if len(cells) == 1 and cells[0].lower() in SUBSECTION_LABELS:
                sub_key           = cells[0].lower()
                sub_blocks[sub_key] = []
                continue
        sub_blocks.setdefault(sub_key, []).append(line)

    sections.update({k: "\n".join(v) for k, v in sub_blocks.items()})
    return sections


# ---------------------------------------------------------------------------
# Extractors
# ---------------------------------------------------------------------------

def extract_description(sections: dict) -> str:
    for body in sections.values():
        for row in parse_md_rows(body):
            for i, cell in enumerate(row):
                if re.match(r"^[Dd]escription\s*:?\s*$", cell.strip(":")):
                    for j in range(i + 1, len(row)):
                        if row[j].strip():
                            return row[j].strip()
    return ""


def extract_metadata(sections: dict) -> dict:
    meta: dict = {}
    label_re   = re.compile(r"^([A-Za-z][A-Za-z /\-#?()]+?):\s*$")
    for body in sections.values():
        for row in parse_md_rows(body):
            i = 0
            while i < len(row) - 1:
                lm  = label_re.match(row[i].strip())
                val = row[i + 1].strip()
                if lm and val and not label_re.match(val) and len(lm.group(1)) < 40:
                    meta[lm.group(1).strip()] = val
                i += 2
    return meta


def extract_columns(sections: dict) -> list:
    body = sections.get("column information", "")
    if not body:
        return []

    rows    = parse_md_rows(body)
    columns = []
    current = None

    for row in rows:
        if (len(row) >= 10
                and re.match(r"^\d+$", row[0])
                and re.match(r"^[A-Z][A-Z0-9_]+$", row[1])):
            if current:
                columns.append(current)
            current = {
                "name":        row[1],
                "type":        row[6] if len(row) > 6 else "",
                "deprecated":  row[7] if len(row) > 7 else "",
                "ehi":         row[11] if len(row) > 11 else "",
                "description": "",
            }
        elif (current is not None
              and len(row) == 4
              and row[0] == "" and row[2] == ""
              and len(row[1]) > 15):
            if not current["description"]:
                current["description"] = row[1]

    if current:
        columns.append(current)
    return columns


def extract_grouped_tables(sections: dict) -> list:
    body   = sections.get("grouped tables", "")
    result = []
    for row in parse_md_rows(body):
        if len(row) >= 3 and re.match(r"^[A-Z][A-Z0-9_]+$", row[0]):
            try:
                col_count = int(row[2].replace(",", ""))
            except ValueError:
                col_count = 0
            result.append({"name": row[0], "columns": col_count})
    return result


def extract_indexes(sections: dict) -> str:
    body = sections.get("index information", "")
    rows = parse_md_rows(body)
    return _rows_to_md(rows) if len(rows) > 1 else ""


def extract_foreign_keys(sections: dict) -> str:
    body = sections.get("foreign key information", "")
    rows = [r for r in parse_md_rows(body) if len(r) >= 4 and any(c for c in r)]
    if len(rows) <= 1:
        return ""
    header = rows[0]
    data   = rows[1:MAX_FK_ROWS + 1]
    suffix = (f"\n\n_({len(rows) - 1} total; showing first {MAX_FK_ROWS})_"
              if len(rows) - 1 > MAX_FK_ROWS else "")
    return _rows_to_md([header] + data) + suffix


def _rows_to_md(rows: list) -> str:
    if not rows:
        return ""
    width = max(len(r) for r in rows)
    def pad(r):
        return r + [""] * (width - len(r))
    lines = ["| " + " | ".join(pad(rows[0])) + " |",
             "| " + " | ".join(["---"] * width) + " |"]
    for row in rows[1:]:
        lines.append("| " + " | ".join(pad(row)) + " |")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Family analysis
# ---------------------------------------------------------------------------

def build_family_notes(all_groups: dict) -> dict:
    seen: dict = {}
    for members in all_groups.values():
        key = frozenset(m["name"] for m in members)
        if key not in seen:
            seen[key] = members

    notes: dict = {}
    for members in seen.values():
        if len(members) < 2:
            continue
        primary = max(members, key=lambda m: m["columns"])
        others  = [m for m in members if m["name"] != primary["name"]]

        for m in members:
            if m["name"] == primary["name"]:
                sibling_str = ", ".join(f"{o['name']} ({o['columns']} cols)" for o in others)
                notes[m["name"]] = (
                    f"**Primary table** in this group ({m['columns']} cols). "
                    f"Overflow siblings joined on shared key: {sibling_str}. "
                    f"Prefer this table for most queries."
                )
            else:
                notes[m["name"]] = (
                    f"**Overflow table** for {primary['name']} ({primary['columns']} cols). "
                    f"Contains additional columns for the same records -- "
                    f"join on the shared primary key column."
                )
    return notes


# ---------------------------------------------------------------------------
# Build clean markdown
# ---------------------------------------------------------------------------

def clean_schema(raw_md: str, table_name: str, family_note: str = "") -> tuple:
    sections    = split_sections(raw_md)
    source      = next((l for l in raw_md.splitlines() if l.startswith("**Source:**")), "")
    description = extract_description(sections)
    meta        = extract_metadata(sections)
    columns     = extract_columns(sections)
    idx_md      = extract_indexes(sections)
    fk_md       = extract_foreign_keys(sections)

    parts = [f"# {table_name}\n"]
    if source:
        parts.append(source + "\n")

    desc_parts = []
    if description:
        desc_parts.append(description)
    if family_note:
        desc_parts.append(family_note)
    if desc_parts:
        parts.append("## Description\n\n" + "\n\n".join(desc_parts) + "\n")

    wanted    = ["Type", "Load Type", "Load Frequency", "Chronicles INI",
                 "Release Version", "Deprecated?", "May contain EHI?"]
    meta_rows = [(k, meta[k]) for k in wanted if k in meta]
    if meta_rows:
        lines = ["| Property | Value |", "| --- | --- |"]
        for k, v in meta_rows:
            lines.append(f"| {k} | {v} |")
        parts.append("## Metadata\n\n" + "\n".join(lines) + "\n")

    if columns:
        lines = ["| Column | Type | Description |", "| --- | --- | --- |"]
        for c in columns:
            dep = " *(deprecated)*" if c["deprecated"].lower() == "yes" else ""
            lines.append(f"| {c['name']}{dep} | {c['type']} | {c['description']} |")
        parts.append("## Columns\n\n" + "\n".join(lines) + "\n")

    if idx_md:
        parts.append(f"## Indexes\n\n{idx_md}\n")
    if fk_md:
        parts.append(f"## Foreign Keys\n\n{fk_md}\n")

    # One-sentence summary for index_brief.md: first 80 chars of description
    brief_desc = description.split(".")[0].strip() if description else ""
    if len(brief_desc) > 90:
        brief_desc = brief_desc[:87] + "..."

    summary = {
        "table":       table_name,
        "description": description[:130].replace("|", "/") if description else "",
        "columns":     ", ".join(c["name"] for c in columns[:8]),
        "family_note": family_note[:120].replace("|", "/") if family_note else "",
        "brief_desc":  brief_desc.replace("|", "/"),
    }
    return "\n".join(parts), summary


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    if not SCHEMAS_DIR.exists():
        print(f"No raw schemas directory at {SCHEMAS_DIR}/. Run tools/scrape_clarity.py first.")
        return

    raw_files = sorted(SCHEMAS_DIR.glob("*.md"))
    if not raw_files:
        print(f"No files in {SCHEMAS_DIR}/. Run tools/scrape_clarity.py first.")
        return

    if len(sys.argv) > 1:
        requested = {a.upper() for a in sys.argv[1:]}
        raw_files = [f for f in raw_files if f.stem.upper() in requested]

    print(f"Processing {len(raw_files)} schema files...")

    # Pass 1: collect family groupings
    all_groups: dict = {}
    for path in raw_files:
        sections = split_sections(path.read_text(encoding="utf-8"))
        group    = extract_grouped_tables(sections)
        if group:
            all_groups[path.stem.upper()] = group

    family_notes = build_family_notes(all_groups)

    # Pass 2: clean each file
    summaries: list = []
    for path in raw_files:
        table_name = path.stem.upper()
        raw_md     = path.read_text(encoding="utf-8")
        note       = family_notes.get(table_name, "")
        clean_md, summary = clean_schema(raw_md, table_name, note)
        (CLEAN_DIR / path.name).write_text(clean_md, encoding="utf-8")
        summaries.append(summary)
        print(f"  {table_name}", flush=True)

    # Write index.md (full descriptions -- reference only, not sent in API calls)
    lines = [
        "# Clarity Schema Index\n",
        "Use this file to identify relevant tables, then load full schemas from `clean_schemas/<TABLE>.md`.\n",
        "| Table | Description | Key Columns | Notes |",
        "| --- | --- | --- | --- |",
    ]
    for s in summaries:
        lines.append(f"| {s['table']} | {s['description']} | {s['columns']} | {s['family_note']} |")
    INDEX_FILE.write_text("\n".join(lines) + "\n", encoding="utf-8")

    # Write index_brief.md (one line per table -- used in excavator classification pass 1)
    brief_lines = [
        "# Clarity Schema Brief Index\n",
        "One line per table. Load full schemas from `clean_schemas/<TABLE>.md` after selection.\n",
    ]
    for s in summaries:
        brief_lines.append(f"{s['table']} -- {s['brief_desc']}")
    INDEX_BRIEF.write_text("\n".join(brief_lines) + "\n", encoding="utf-8")

    print(f"\nDone. {len(summaries)} clean schemas -> {CLEAN_DIR}/")
    print(f"Index     -> {INDEX_FILE}")
    print(f"Brief idx -> {INDEX_BRIEF}")


if __name__ == "__main__":
    main()