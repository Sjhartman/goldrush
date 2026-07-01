# Goldrush — Architecture

## The Mining Metaphor

| Stage | Tool | What it does |
|---|---|---|
| Stake a claim | `data-claim.py` | Validates an IRB data request against its protocol; produces a structured audit JSON |
| Excavate | `excavator/` | Reads the audit JSON and generates Databricks SQL extraction scripts |
| Refine | `refiner/` *(future)* | Extracts structured features from free-text fields (pathology notes, operative reports) |
| Inspect | `inspector/` *(future)* | Loads all outputs into a Neo4j knowledge graph; provides a local AI agent for natural-language cohort queries |

---

## Directory Structure

```
goldrush/
├── data-claim.py              # IRB compliance validator
├── excavator/                 # SQL generation pipeline
│   ├── orchestrator.py        # Coordinates all specialists; the main entry point
│   ├── cohort.py              # Script 1: Tempus membership + ICD eligibility
│   ├── demographics.py        # Script 2: Patient attributes (sex, race, DOB, MRN)
│   ├── addresses.py           # Script 3: Address history (PAT_ADDR_CHNG_HX)
│   ├── clinical_pathology.py  # Script 4: Staging, mortality, recurrence + HNO notes
│   ├── tempus.py              # Script 5: Tempus genomic data extraction
│   ├── attrition.py           # Script 6: CONSORT attrition counts (deterministic Python)
│   ├── shared/
│   │   ├── prompts.py         # BASE_SYSTEM_PROMPT (Databricks rules + cohort contract)
│   │   ├── databricks.py      # check_sql_syntax(), check_sql_performance()
│   │   ├── schema_validation.py  # validate_sql(), fix_sql_errors()
│   │   └── embedding.py       # _embed_cohort(), _strip_leading_comments(), etc.
│   └── validators/
│       ├── irb_auditor.py     # Claude-based: checks approved/denied element compliance
│       └── contract_checker.py  # Claude-based: verifies cohort contract in each script
├── refiner/
│   └── PLACEHOLDER.md         # Spec for future structured feature extraction phase
├── inspector/
│   └── PLACEHOLDER.md         # Spec for future Neo4j graph + AI agent query phase
├── schemas/
│   ├── epic_clarity_columns.tsv   # Full column list (TABLE, col_name, type) — grep before SQL
│   ├── tempus_columns.tsv         # Tempus column list (table_name, col_name, type)
│   ├── tempus_tables.txt          # Confirmed curated.tempus.* table names
│   ├── index.md                   # Full table index (1,051 tables, ~15K tokens)
│   ├── index_brief.md             # One-line table descriptions (~5K tokens) — used in classification pass 1
│   └── clean_schemas/             # Per-table schema markdown files (scraped + post-processed)
├── tools/
│   ├── scrape_clarity.py          # Scrapes Epic Data Handbook for table schemas
│   ├── postprocess.py             # Cleans raw scraped markdown; builds index.md and index_brief.md
│   ├── collect_schemas.py         # Collects column list into epic_clarity_columns.tsv
│   └── filter_icd10.py            # Filters CMS full ICD-10-CM file to oncology subset
├── ICD10_codes/
│   ├── icd10cm-oncology-2026.csv  # Oncology subset (C, D00-D49, Z15/Z17/Z19/Z80/Z85/Z86)
│   └── icd10cm-order-2026.txt     # Full CMS source file
├── requirements.txt
├── CLAUDE.md
└── ARCHITECTURE.md  ← this file
```

Collaborator data lives **outside** this repo in a sibling directory `goldrush_data/` (not tracked by git):

```
goldrush_data/
└── Dr_Pari_Jafari/
    └── StudyName/                     ← sub-project folder, named by study
        ├── irb_*.pdf                  ← filename must start with "irb"
        ├── request_*.docx             ← filename must start with "request"
        ├── clarifications_*.docx      ← optional
        └── reports/                   ← --output-dir target; all generated outputs land here
            ├── report__*.md           ← data-claim output
            ├── audit__*.json          ← data-claim output → input to excavator
            └── audit__*_[1-6]_*.sql  ← excavator output scripts
```

---

## Pipeline

```
IRB protocol doc + data request
           |
           v
     data-claim.py
           |
     [API call 1] Compliance validation + element approval/denial
     [API call 2] ICD-10 code resolution (only if disease names present,
                  uses prompt caching on oncology CSV)
           |
     audit__*.json   report__*.md
           |
           v
  excavator/orchestrator.py
           |
     [API call 1] classify_and_identify  -- default Tempus codes: XT, XF, RS, XO
                  — pass 1: index_brief.md (~5K tokens) → candidate table list
                  — pass 2: full clean_schemas for candidates → element bucketing
                  Output: clarity_elements, tempus_elements, gap_elements, tables_needed
           |
     [cohort.py]  [API call 2, sequential]
                  Generates Script 1 (must complete before others — output embedded in all)
           |
     ┌─────────────────────────────────────────┐  parallel
     │ demographics.py  [API call 3]           │
     │ addresses.py     [API call 4]           │
     │ clinical_pathology.py [API call 5]      │
     │ tempus.py        [API call 6]           │
     └─────────────────────────────────────────┘
           |
     [attrition.py]  Deterministic Python — no API call
           |
     ┌──────────────────────────────┐  parallel
     │ irb_auditor.py  [API call]   │
     │ contract_checker.py [API call│
     └──────────────────────────────┘
           |
     [schema validation + auto-fix]  Python + targeted Claude calls
           |
     Scripts 1-6 .sql files written to PI subfolder
```

---

## Specialist Architecture

Each excavator module is a **specialist**: it receives only the schemas relevant to its domain and has a system prompt focused on that domain's rules. This is more token-efficient than a monolithic generator and produces better SQL.

### Shared contract (all specialists assume this)

Every large-table CTE must join `eligible_cohort` as its **first** join:

```sql
my_cte AS (
    SELECT ...
    FROM curated.epic_clarity.pat_enc_dx pd
    INNER JOIN eligible_cohort ec ON ec.PAT_ID = pd.PAT_ID  -- cohort first, always
    ...
)
```

`eligible_cohort` exposes: `PAT_ID, mrn, index_dx_date, cancer_type, index_icd10_code, index_dx_source, age_at_dx, age_stratum`

`excluded_patients` exposes: `PAT_ID`

### Specialist → domain → schemas

| Specialist | Domain | Key tables |
|---|---|---|
| `cohort.py` | Eligibility | PAT_ENC_DX, PROBLEM_LIST, HSP_DISCH_DIAG, EDG_CURRENT_ICD10, IDENTITY_ID, curated.tempus.`order`, curated.tempus.patient |
| `demographics.py` | Patient attributes | PATIENT, PATIENT_RACE, ETHNIC_BACKGROUND, ZC_SEX, ZC_MARITAL, IDENTITY_ID |
| `addresses.py` | Address history | PAT_ADDR_CHNG_HX, PATIENT_ADDRESS, ZC_STATE, ZC_COUNTY |
| `clinical_pathology.py` | Outcomes + notes | V_CANCER_STAGING, EXTERNAL_DEATH_REPORTS, ENROLL_INFO, TPL_INFO, HNO_INFO, HNO_NOTE_TEXT, ZC_NOTE_TYPE, ZC_NOTE_TYPE_IP |
| `tempus.py` | Genomic data | curated.tempus.patient, curated.tempus.order, curated.tempus.specimens, curated.tempus.results, curated.tempus.report |

### System prompt structure

```
BASE_SYSTEM_PROMPT (shared/prompts.py)
  — Databricks SQL syntax rules (ASCII, no semicolon, no block comments, DATE_REAL, etc.)
  — Cohort contract (eligible_cohort columns, first-join rule)
  — UNION ALL column count rules
  — No correlated subqueries rule

+ specialist-level additions (inline per module):
  cohort.py     — tempus_patients CTE template, gi_icd10_codes pattern, DATE_REAL conversion
  demographics.py — IDENTITY_ID type 1008, PATIENT_RACE multi-row pattern, ZC decode rules
  addresses.py  — PAT_ADDR_CHNG_HX date range pattern, geocoding context
  clinical_pathology.py — V_CANCER_STAGING column corrections (no stage_ prefix),
                          TPL_INFO column names, HNO_INFO unsigned_yn=NULL for signed notes,
                          ZC_NOTE_TYPE NULL = AP report, COLLECT_LIST aggregation pattern
  tempus.py     — confirmed column lists per table, biomarkers not in SQL (catalog only),
                  backtick required on `order`, t6_base join chain pattern
```

---

## Token Efficiency Design

### Classification: two-tier index

| Tier | File | Size | Purpose |
|---|---|---|---|
| 1 | `index_brief.md` | ~5K tokens | Table name + one-line description. Classification pass 1: candidate selection |
| 2 | `clean_schemas/<TABLE>.md` | ~1-5K tokens each | Full column detail. Only loaded for candidate tables |

Classification call structure:
1. Send `index_brief.md` → get candidate table list (cheap)
2. Load `clean_schemas/` for each candidate → send full schemas → get element bucketing + confirmed table list

This reduces classification input from ~15K tokens (full index) to ~5K (brief) + ~20K (candidates) = ~25K total, but spread across two smaller, more focused calls.

### Parallel generation

After cohort completes (sequential dependency — its CTEs are embedded in all other scripts):

```python
with ThreadPoolExecutor(max_workers=4) as executor:
    f_demo   = executor.submit(demographics.generate, ...)
    f_addr   = executor.submit(addresses.generate, ...)  # only if addresses approved
    f_clin   = executor.submit(clinical_pathology.generate, ...)
    f_tempus = executor.submit(tempus.generate, ...)     # only if Tempus elements exist
```

Wall-clock time for generation: ~1× one-call latency after cohort completes (vs. ~5× sequential).

### Prompt caching

`BASE_SYSTEM_PROMPT` is identical across all specialist calls. Anthropic caches repeated system prompt content at ~10% of normal token cost.

---

## Materialization Modes

Each script is generated in **self-contained** mode by default (full cohort CTE block embedded). This allows any script to run independently via `datalake_connector.py`.

An optional `--materialize` flag generates a **view-referencing** mode for Databricks notebook use:

- Script 1 includes a `CREATE OR REPLACE TEMP VIEW eligible_cohort AS ...` block (commented out by default; uncomment and run before Scripts 2-5)
- Scripts 2-5 reference `eligible_cohort` directly instead of re-embedding 150+ lines of CTEs
- Cohort logic executes once; downstream scripts are dramatically shorter

---

## Validator Agents

Two Claude-based validators run after all scripts are generated, in parallel:

### IRB Compliance Auditor (`validators/irb_auditor.py`)

Gets: audit JSON + all generated SQL scripts

Checks:
- Every SELECT column maps to an approved element
- No denied/ambiguous element appears anywhere
- Population filters (age, date, site) are enforced as WHERE clauses, not left to the analyst
- Row-level restrictions match IRB scope

Cannot be done with Python regex — requires semantic reasoning about element-to-column mapping.

### Cohort Contract Checker (`validators/contract_checker.py`)

Gets: each generated script individually

Checks:
- Every large table scan has `eligible_cohort` as its first JOIN
- No intermediate "raw scan" CTEs for large tables
- No `NOT IN (SELECT ... FROM curated...)` patterns

Supplements (and may eventually replace) the Python `check_sql_performance()` heuristic.

Both validators feed findings into the existing auto-fix loop if issues are found.

---

## Refiner (Future Phase)

`refiner/` is reserved for structured feature extraction from free text. Inputs will be pathology note text extracted by the clinical_pathology excavator. Outputs will be structured clinical features (tumor grade, margin status, lymph node counts, etc.).

See `refiner/PLACEHOLDER.md` for the specification stub.

---

## Inspector (Future Phase)

`inspector/` will load all excavator and refiner outputs into a Neo4j property graph and
expose a local AI agent for natural-language cohort queries. The graph model connects
Patients to Diagnoses, PathologyNotes, ClinicalFeatures, and GenomicOrders. The agent
translates researcher questions into Cypher queries and is constrained to IRB-approved
elements via the same audit JSON that governs the excavator.

See `inspector/PLACEHOLDER.md` for the specification stub.

---

## Known WashU/BJC Environment Constraints

### Databricks SQL
- ASCII only — no Unicode in SQL text or comments
- No trailing semicolon after final SELECT
- No block comments (`/* */`) — use `--` only
- `DATE_REAL` columns (PAT_ENC_DATE_REAL, CONTACT_DATE_REAL) are DOUBLE (days since 1899-12-30) — use `DATE_ADD(DATE '1899-12-30', CAST(col AS INT))`
- DATETIME not supported — use TIMESTAMP or DATE
- UNION ALL column counts must match exactly across all branches

### Data lake access
- Read-only from `curated.epic_clarity.*` and `curated.tempus.*`
- Write access available in scratch schemas for cohort materialization (confirm with data team)
- `datalake_connector.py` runs one SQL file per invocation, no session state

### Tables not in this environment
- `HSP_ACCOUNT` — use `PAT_ENC_HSP` instead
- `ZC_LINE_OF_TREATMENT` — use `line_of_treatment_c` code directly from `TPL_INFO`
- `ZC_RESEARCH_STATUS` — omit or use `record_status_c` directly
- `ZC_DISCH_CODE` — use `ZC_DISCH_DISP`
- `AP_DIAG_CODES`, `LAB_CASE_ADDEND` — do not exist

### Tempus genomic data
- curated.tempus.`order` (backtick required — ORDER is reserved)
- No date fields in `curated.tempus.order` — only: `institution, physician, tempusOrderId, accessionId, test_code, test_name, test_description, tempusId, reportId, referenceGenome`
- Biomarkers (TMB, MSI, tumor purity), variants (BRAF, KRAS, etc.), and report dates are NOT in SQL — they live in Tempus catalog TSV files (Python layer only)
- Authorization: WashU/BJC Tempus data requires I2DB RDC Repository authorization (IRB 201607071, PI: Albert Lai) — `data-claim.py` checks for this automatically

### EDG_CURRENT_ICD10
- No DESCRIPTION column in this environment — only `DX_ID, CODE, LINE`

### HNO_INFO (clinical notes)
- Signed notes: `unsigned_yn IS NULL OR unsigned_yn = 'N'` (NULL = signed; 'Y' = draft)
- Note type: `note_type_noadd_c` (not NOTE_TYPE_C)
- AP/pathology reports frequently have no ZC_NOTE_TYPE mapping (NULL) — include NULL as a valid note type
