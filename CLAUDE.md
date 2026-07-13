# CLAUDE.md — Goldrush

This file provides guidance to Claude Code when working in this repository.

## What Goldrush Is

A three-stage clinical data mining pipeline for WashU/BJC IRB-governed research data requests.

```
data-claim.py  →  excavator/  →  refiner/ (future)  →  inspector/ (future)
   (validate)      (extract)      (structure)              (graph + query)
```

**data-claim.py** validates an IRB data request against its protocol, resolves ICD-10 codes, and outputs a structured audit JSON.

**excavator/** reads the audit JSON and generates Databricks SQL scripts to extract the approved data elements from `curated.epic_clarity.*` and `curated.tempus.*`.

**refiner/** (not yet built) will extract structured clinical features from free text produced by the excavator (pathology notes, operative reports, etc.).

See `ARCHITECTURE.md` for the full design.

---

## Running data-claim.py

Use `venv/bin/python` — do NOT activate the venv or use system Python.

```bash
# Single mode
venv/bin/python data-claim.py <irb_document> <request_document>

# With clarifications (DOCX ICD tables in the clarification supersede the request)
venv/bin/python data-claim.py <irb_doc> <request_doc> --clarification <clarification_doc>

# Override the I2DB/RDC authorization check (reviewer discretion only)
venv/bin/python data-claim.py <irb_doc> <request_doc> --override-i2db

# Override output directory (default: claim_out/ next to input/, or next to IRB doc)
venv/bin/python data-claim.py <irb_doc> <request_doc> --output-dir <path>

# Override ICD reference file
venv/bin/python data-claim.py <irb_doc> <request_doc> --icd-file ICD10_codes/icd10cm-oncology-2026.csv

# Model override
ANTHROPIC_MODEL=claude-opus-4-8 venv/bin/python data-claim.py <irb_doc> <request_doc>
```

Supported document formats: `.pdf`, `.docx`, `.html`, `.htm`, `.txt`, `.md`, `.csv`, `.tsv`

Outputs written next to the IRB document (into the PI subfolder):

- `report__*.md` — human-readable compliance report
- `audit__*.json` — full structured result + token usage → **input to excavator**

---

## Running excavator/orchestrator.py

```bash
venv/bin/python excavator/orchestrator.py <path_to_audit_json>

# Materialize cohort as TEMP VIEW (for Databricks notebook use)
venv/bin/python excavator/orchestrator.py <audit_json> --materialize

# Override Tempus test_code filter (default: XT, XF, RS, XO)
venv/bin/python excavator/orchestrator.py <audit_json> --tempus-codes XT,XF,RS,XO

# Amend existing SQL scripts
venv/bin/python excavator/orchestrator.py --amend <audit_json> "add zip code to demographics"
```

Outputs written next to the audit JSON (into the PI subfolder):

- `audit__*_1_cohort.sql`
- `audit__*_2_demographics.sql`
- `audit__*_3_addresses.sql` (if addresses approved)
- `audit__*_4_clinical_pathology.sql`
- `audit__*_5_tempus.sql` (if Tempus elements approved)
- `audit__*_6_attrition.sql`
- `audit__*_gap_report.md`
- `audit__*_schema_fixes.md` (if auto-corrections applied)

---

## Research Group Folder Convention

Collaborator data lives **outside** this repo in the sibling directory `goldrush_data/` (not tracked by git). Each PI has a subfolder. The standard layout within a PI folder uses three sibling directories that the tools auto-detect:

```
goldrush_data/
  Dr_Smith/
    input/                             ← source documents (IRB, request, clarifications)
      irb_smith.pdf                    ← filename must start with "irb"
      request_smith.docx               ← filename must start with "request"
      clarifications.docx              ← optional, passed via --clarification
    claim_out/                         ← data-claim.py writes here automatically
      report__*.md
      audit__*.json                    ← input to excavator
    excavator_out/                     ← excavator writes here automatically
      audit__*_1_cohort.sql
      audit__*_2_demographics.sql
      audit__*_3_addresses.sql
      audit__*_4_clinical_pathology.sql
      audit__*_5_tempus.sql
      audit__*_6_attrition.sql
      audit__*_gap_report.md
      audit__*_schema_fixes.md
```

**Auto-detection rules:**

- `data-claim.py`: if the IRB document is inside a folder named `input/`, outputs default to `../claim_out/`
- `excavator/orchestrator.py`: if the audit JSON is inside a folder named `claim_out/`, outputs default to `../excavator_out/`
- Both tools accept `--output-dir <path>` to override the default.

A PI with multiple concurrent studies may have multiple sets of input/claim_out/excavator_out folders (e.g., name the parent by study: `Dr_Smith/EOCRC_2026/input/`, `Dr_Smith/Breast_2026/input/`).

---

## Schema Files — Always Check Before Writing SQL

### Epic Clarity

Before writing ANY `curated.epic_clarity` SQL, grep the column list:

```bash
grep -i "^TABLE_NAME\b" schemas/epic_clarity_columns.tsv
```

Format: `table_name\tcol_name\ttype` (tab-separated, table names in UPPER CASE).

Do NOT guess column names — this environment's names frequently differ from standard Epic documentation.

Known differences:

- `HNO_INFO`: signed filter is `unsigned_yn IS NULL OR unsigned_yn = 'N'`; note type is `note_type_noadd_c`
- `EDG_CURRENT_ICD10`: no DESCRIPTION column — only `DX_ID, CODE, LINE`
- `AP_DIAG_CODES`, `LAB_CASE_ADDEND`: do not exist in this environment
- `V_CANCER_STAGING`: notoriously poorly filled — **never use as a primary source for staging**. Always include as supplementary data only and flag in comments.
- `PROBLEM_LIST`: date columns are **timestamps**, not DATE_REAL floats. Use `CAST(pl.noted_date AS DATE)` directly — never `DATE_ADD(DATE '1840-12-31', CAST(pl.noted_date AS INT))` or any variant. `DATE_OF_ENTRY_REAL` does not exist; `date_of_entry` is also a timestamp and must be cast the same way.

### Tempus

Before writing ANY `curated.tempus` SQL, grep the Tempus column list:

```bash
grep -i "^ORDER\b" schemas/tempus_columns.tsv
```

Format: `table_name\tcol_name\ttype`

Confirmed `curated.tempus.order` columns (complete list):
`institution, physician, tempusOrderId, accessionId, test_code, test_name, test_description, tempusId, reportId, referenceGenome`

**No date fields. No biomarker fields.** TMB, MSI, tumor purity, variant calls, and report sign-out dates are NOT in SQL — they live in Tempus catalog TSV files (Python layer only).

Backtick required: `curated.tempus.\`order\`` (ORDER is a SQL reserved word).

**Do not use `curated.tempus.specimens_v2`.** It is missing rows that exist in `curated.tempus.specimens`. Use `curated.tempus.specimens` as the primary specimen source. Note that `specimens` does not have `primarysamplesite`, `sampletype`, `tempusSampleId`, or diagnosis ICD fields -- those only exist in `specimens_v2`. If those columns are needed, LEFT JOIN `specimens_v2` on `(tempusId, reportId)` to fill them in where available, but treat `specimens` as the authoritative row source.

`curated.tempus.specimens` columns: `collectionDate`, `receiptDate`, `sampleCategory`, `sampleSite`, `contentsReceivedLabel`, `notes`, `institutionData_caseId`, `institutionData_blockId`, `institutionData_tumorPercentage`, `tempusId`, `reportId`

---

## Databricks SQL Rules — Hard Requirements

These are not style preferences — violations cause runtime errors.

1. **ASCII only.** No Unicode in SQL text or comments. No em dash, en dash, right arrow, box-drawing chars, smart quotes, curly brackets.
2. **No trailing semicolon** after the final SELECT.
3. **Nothing after the final SELECT** — no block comments, no secondary queries.
4. **No block comments** (`/* ... */`) — use `--` line comments only.
5. **DATE_REAL columns** (PAT_ENC_DATE_REAL, CONTACT_DATE_REAL, etc.) are stored as DOUBLE (days since 1840-12-31). Never `CAST(col AS DATE)`. Use: `DATE_ADD(DATE '1840-12-31', CAST(col AS INT))` — WashU/BJC epoch is 1840-12-31, NOT the standard Epic/Excel 1899-12-30 (empirically verified against PAT_ENC and PAT_ENC_DX).
6. **DATETIME not supported** — use TIMESTAMP or DATE.
7. **UNION ALL column counts** must match exactly across all branches. One NULL per line with an alias matching the first branch.
8. **No correlated subqueries** (`NOT IN (SELECT ... FROM large_table)`). Use LEFT ANTI JOIN or a CTE pre-filter.
9. **No blank lines between consecutive comment-only lines.** Databricks SQL editor treats them as statement boundaries.

---

## Excavator Specialist Rules

### Cohort contract (every specialist must follow)

Every large-table CTE must join `eligible_cohort` as its FIRST join:

```sql
-- CORRECT
my_cte AS (
    SELECT ...
    FROM curated.epic_clarity.pat_enc_dx pd
    INNER JOIN eligible_cohort ec ON ec.PAT_ID = pd.PAT_ID  -- first
    LEFT JOIN curated.epic_clarity.edg_current_icd10 ei ON ei.DX_ID = pd.DX_ID
)

-- WRONG — full table scan before cohort filter
raw_cte AS (SELECT ... FROM curated.epic_clarity.pat_enc_dx),  -- no cohort join
filtered AS (SELECT ... FROM raw_cte JOIN eligible_cohort ...)  -- too late
```

Large tables that require this treatment: `PAT_ENC_DX, PROBLEM_LIST, HSP_DISCH_DIAG, HSP_ACCT_DX_LIST, PAT_ENC, PAT_ENC_HSP, PATIENT, EDG_CURRENT_ICD10, EXTERNAL_DEATH_REPORTS, V_CANCER_STAGING, TPL_INFO, ENROLL_INFO, HNO_INFO, HNO_NOTE_TEXT`

### Cohort CTE available columns

```
eligible_cohort: PAT_ID, mrn, index_dx_date, cancer_type,
                 index_icd10_code, index_dx_source, age_at_dx, age_stratum
excluded_patients: PAT_ID
```

### Tempus join chain (Script 5)

```sql
t5_base AS (
    SELECT ec.PAT_ID, ec.mrn, ec.index_dx_date, ec.cancer_type,
           p.tempusId, p.reportId AS patient_reportId
    FROM eligible_cohort ec
    INNER JOIN curated.tempus.patient p ON p.emrid = ec.mrn
)
-- subsequent CTEs join via t5_base.tempusId
```

### Cohort performance pattern (Script 1)

```sql
-- 1. Tempus membership (emrid only)
tempus_patients AS (SELECT DISTINCT p.emrid ...)

-- 2. Bridge emrid → PAT_ID (enables large-table pre-filtering)
tempus_pat_ids AS (
    SELECT DISTINCT p.PAT_ID FROM curated.epic_clarity.patient p
    INNER JOIN tempus_patients tp ON tp.emrid = p.PAT_MRN_ID
)

-- 3. Pre-filter ICD lookup to qualifying codes only
gi_icd10_codes AS (SELECT DX_ID, CODE FROM curated.epic_clarity.edg_current_icd10 WHERE ...)

-- 4. dx_raw: patient filter FIRST, then ICD filter — never unfiltered
dx_raw AS (
    SELECT ped.PAT_ID, ...
    FROM curated.epic_clarity.pat_enc_dx ped
    INNER JOIN tempus_pat_ids tpi ON tpi.PAT_ID = ped.PAT_ID   -- patient filter first
    INNER JOIN gi_icd10_codes gic ON gic.DX_ID  = ped.DX_ID    -- ICD filter second
    ...
)
```

---

## I2DB / Tempus Authorization

WashU/BJC Tempus genomic data is sourced from the Institute for Informatics, Data Science, and Biostatistics (I2DB) Research Data Core (RDC) Repository — IRB ID: **201607071**, PI: **Albert Lai**.

`data-claim.py` checks every IRB document for reference to: "I2DB", "Institute for Informatics", "Research Data Core", "RDC", "IRB 201607071", or "Albert Lai". If absent, Tempus elements are auto-denied and the status is set to DENIED.

Pass `--override-i2db` at reviewer discretion to waive this check.

---

## ICD-10 Reference

Oncology ICD-10 codes are in `ICD10_codes/icd10cm-oncology-2026.csv`. This covers:

- `C` — all malignant neoplasms
- `D00–D49` — in situ and benign neoplasms
- `Z15, Z17, Z19, Z80, Z85, Z86` — genetic susceptibility, receptor status, family/personal history

To regenerate (when the annual CMS file updates):

```bash
python schema_tools/filter_icd10.py
```

---

## Schema Maintenance (schema_tools/)

All scripts in `schema_tools/` are run manually on the cluster. Goldrush is an archive for these scripts — it does not run them automatically.

### Rebuild the Clarity table index

```bash
# Scrape Epic Data Handbook for new/updated tables
python schema_tools/scrape_clarity_handbook.py

# Post-process into clean_schemas/ and regenerate index.md + index_brief.md
python schema_tools/clarity_schema_postprocess.py
```

`index_brief.md` (one-line per table, ~5K tokens) is used in excavator classification pass 1.
`index.md` (full descriptions, ~15K tokens) is NOT sent in any API call — it's a reference only.
`clean_schemas/<TABLE>.md` files are loaded on demand after pass 1 identifies candidate tables.

### Collect Databricks column list (Epic Clarity)

Run in a Databricks notebook:

```python
names = [row.tableName.upper() for row in spark.sql("SHOW TABLES IN curated.epic_clarity").collect()]
print("\n".join(names))
```

Paste output into `schemas/clarity_tables.txt`, then:

```bash
python schema_tools/scrape_databricks_schemas.py
```

This produces `schemas/epic_clarity_columns.tsv`.

### Collect Tempus catalog schema

Update `CATALOG_DIR` in `schema_tools/tempus_catalog_schema.py` to the current catalog version, then run on the cluster:

```bash
python schema_tools/tempus_catalog_schema.py
```

Output is written to `tempus_catalog_schema.txt` in whichever directory the script is run from. Copy the result into `schemas/` and check it into goldrush after each catalog version update.

---

## Dependencies

All scripts share a single venv at the goldrush root:

```bash
python3 -m venv venv
venv/bin/pip install -r requirements.txt
```

Required packages: `anthropic >= 0.101.0`, `python-docx`, `beautifulsoup4`

Environment variable: `ANTHROPIC_API_KEY` (routes to WashU secure endpoint — no changes needed)
