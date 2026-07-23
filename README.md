# Goldrush

A clinical data mining pipeline for WashU/BJC IRB-governed research data requests. Given an IRB protocol and a data request document, Goldrush validates compliance, resolves ICD-10 codes, and generates ready-to-run Databricks SQL extraction scripts.

```
data-claim.py  →  excavator/  →  refiner/ (future)  →  inspector/ (future)
   (validate)      (extract)      (structure)              (graph + query)
```

---

## Stages

| Stage | Tool | What it does |
|---|---|---|
| Stake a claim | `data-claim.py` | Validates an IRB data request; produces a structured audit JSON |
| Excavate | `excavator/orchestrator.py` | Reads the audit JSON; generates Databricks SQL scripts |
| Refine | `refiner/` *(future)* | Extracts structured features from free-text fields |
| Inspect | `inspector/` *(future)* | Neo4j knowledge graph + natural-language cohort query agent |

---

## Setup

```bash
python3 -m venv venv
venv/bin/pip install -r requirements.txt
export ANTHROPIC_API_KEY=<your-key>  # or store in ~/.zshrc to load automatically
```

Use `venv/bin/python` for all commands — do not activate the venv or use system Python.

---

## Running data-claim.py

Validates an IRB protocol against a data request and outputs a compliance report and structured audit JSON.

```bash
# Basic usage
venv/bin/python data-claim.py <irb_document> <request_document>

# With a clarifications document (DOCX ICD tables in clarifications supersede the request)
venv/bin/python data-claim.py <irb_doc> <request_doc> --clarification <clarification_doc>

# Override the I2DB/RDC authorization check (reviewer discretion only)
venv/bin/python data-claim.py <irb_doc> <request_doc> --override-i2db

# Override output directory (default: claim_out/ sibling to input/)
venv/bin/python data-claim.py <irb_doc> <request_doc> --output-dir <path>

# Override ICD reference file
venv/bin/python data-claim.py <irb_doc> <request_doc> --icd-file ICD10_codes/icd10cm-oncology-2026.csv

# Model override
ANTHROPIC_MODEL=claude-opus-4-8 venv/bin/python data-claim.py <irb_doc> <request_doc>
```

Supported document formats: `.pdf`, `.docx`, `.html`, `.htm`, `.txt`, `.md`, `.csv`, `.tsv`

**Outputs** (written to `claim_out/` next to the IRB document):

- `report__*.md` — human-readable compliance report
- `audit__*.json` — structured result with element approvals/denials → input to excavator

---

## Running excavator/orchestrator.py

Reads an audit JSON and generates Databricks SQL extraction scripts for each approved data domain.

```bash
# Basic usage
venv/bin/python excavator/orchestrator.py <path_to_audit_json>

# Materialize cohort as a TEMP VIEW (for Databricks notebook use)
venv/bin/python excavator/orchestrator.py <audit_json> --materialize

# Override Tempus test_code filter (default: XT, XF, RS, XO)
venv/bin/python excavator/orchestrator.py <audit_json> --tempus-codes XT,XF,RS,XO

# Amend existing SQL scripts
venv/bin/python excavator/orchestrator.py --amend <audit_json> "add zip code to demographics"
```

**Outputs** (written to `excavator_out/` next to the audit JSON):

- `audit__*_1_cohort.sql` — Tempus membership + ICD eligibility
- `audit__*_2_demographics.sql` — Patient attributes (sex, race, DOB, MRN)
- `audit__*_3_addresses.sql` — Address history (if addresses approved)
- `audit__*_4_clinical_pathology.sql` — Staging, mortality, recurrence, HNO notes
- `audit__*_5_tempus.sql` — Tempus genomic data (if Tempus elements approved)
- `audit__*_6_attrition.sql` — CONSORT attrition counts
- `audit__*_gap_report.md` — Elements requested but not extractable from SQL
- `audit__*_schema_fixes.md` — Auto-corrections applied (if any)

---

## Folder Convention

Collaborator data lives **outside** this repo in the sibling directory `goldrush_data/` (not tracked by git):

```
goldrush_data/
  Dr_Smith/
    StudyName/
      input/
        irb_smith.pdf          # filename must start with "irb"
        request_smith.docx     # filename must start with "request"
        clarifications.docx    # optional
      claim_out/
        report__*.md
        audit__*.json          # input to excavator
      excavator_out/
        audit__*_1_cohort.sql
        audit__*_2_demographics.sql
        audit__*_3_addresses.sql
        audit__*_4_clinical_pathology.sql
        audit__*_5_tempus.sql
        audit__*_6_attrition.sql
        audit__*_gap_report.md
        audit__*_schema_fixes.md
```

Auto-detection: if the IRB document is inside a folder named `input/`, `data-claim.py` defaults output to `../claim_out/`. If the audit JSON is inside `claim_out/`, the excavator defaults output to `../excavator_out/`. Both accept `--output-dir` to override.

---

## I2DB / Tempus Authorization

WashU/BJC Tempus genomic data requires I2DB Research Data Core Repository authorization (IRB 201607071, PI: Albert Lai). `data-claim.py` checks every IRB document for this reference automatically — if absent, all Tempus elements are denied. Pass `--override-i2db` at reviewer discretion to waive.

---

## Schema Files

Before writing any SQL, grep the local schema files:

```bash
# Epic Clarity
grep -i "^TABLE_NAME\b" schemas/epic_clarity_columns.tsv

# Tempus
grep -i "^ORDER\b" schemas/tempus_columns.tsv
```

Do not guess column names from Epic documentation — this environment's names frequently differ. See `CLAUDE.md` for known differences and `ARCHITECTURE.md` for the full schema maintenance workflow.

---

## Key Databricks SQL Constraints

These are runtime requirements, not style preferences:

- ASCII only in SQL text and comments
- No trailing semicolon after the final SELECT
- No block comments (`/* */`) — use `--` line comments only
- `DATE_REAL` columns are DOUBLE (days since **1840-12-31**) — use `DATE_ADD(DATE '1840-12-31', CAST(col AS INT))`
- DATETIME not supported — use TIMESTAMP or DATE
- UNION ALL branches must have identical column counts
- No correlated subqueries — use LEFT ANTI JOIN or CTE pre-filters

---

## Further Reading

- `ARCHITECTURE.md` — full pipeline design, specialist architecture, token efficiency approach, and environment constraints
- `CLAUDE.md` — schema rules, Databricks SQL rules, and excavator specialist patterns (intended for Claude Code)
