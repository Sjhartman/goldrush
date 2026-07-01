# inspector/ — Placeholder

## Purpose

The `inspector/` stage will load the structured outputs produced by the refiner into a
Neo4j knowledge graph and expose a local AI agent that lets researchers query their cohort
data using natural language.

## Planned inputs

- Structured feature tables produced by `refiner/` (CSV or Parquet, one row per note)
- Tabular SQL outputs produced by `excavator/` (demographics, clinical_pathology, tempus, etc.)
- Audit JSON from `data-claim.py` (for IRB-approved element scope — only approved fields
  are loaded into the graph)

## Planned outputs

- A populated Neo4j database representing the cohort as a property graph
- A local AI agent interface (CLI or notebook) for natural-language queries over the graph

## Graph model (preliminary)

Nodes:
- `Patient` — PAT_ID, MRN, demographics
- `Diagnosis` — ICD-10 code, date, source
- `PathologyNote` — note_id, date, note type
- `ClinicalFeature` — feature name, value (from refiner output: grade, margin, staging, etc.)
- `GenomicOrder` — tempusOrderId, test_code, reportId

Relationships:
- `(Patient)-[:HAS_DIAGNOSIS]->(Diagnosis)`
- `(Patient)-[:HAS_NOTE]->(PathologyNote)`
- `(PathologyNote)-[:EXTRACTED_FEATURE]->(ClinicalFeature)`
- `(Patient)-[:HAS_GENOMIC_ORDER]->(GenomicOrder)`

## AI agent design (preliminary)

- Local agent powered by the Claude API
- Translates researcher natural-language questions into Cypher queries
- Returns results as formatted tables or narrative summaries
- Constrained to the approved element scope from the audit JSON (same IRB enforcement
  as the excavator)
- Maintains conversation context across queries within a session

## Design notes

- Neo4j instance runs locally (Docker or native install) — no external graph service
- Graph is rebuilt per-run from refiner + excavator outputs; the database is not a
  persistent store between pipeline versions
- Cypher generation will reuse the `BASE_SYSTEM_PROMPT` IRB compliance rules from
  `excavator/shared/prompts.py`
- Authentication/authorization: the same IRB audit JSON that gates excavator element
  selection will gate which node properties the agent is permitted to query

## Status

Not yet implemented. Depends on `refiner/` being complete. See `refiner/PLACEHOLDER.md`
for the upstream specification.
