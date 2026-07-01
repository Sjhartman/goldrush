# refiner/ — Placeholder

## Purpose

The `refiner/` stage will extract structured clinical features from free text produced by
the excavator, particularly:

- Pathology report text (from `HNO_NOTE_TEXT` via the clinical_pathology excavator)
- Operative notes
- Consult letters

## Planned inputs

- Free-text note files produced by `excavator/clinical_pathology.py` (Script 4)
- IRB audit JSON (for approved element scope, same as excavator)

## Planned outputs

Structured feature tables in CSV or Parquet format, one row per note, with extracted fields:
- Tumor grade (e.g. `grade_G1`, `grade_G2`, `grade_G3`)
- Margin status (`margin_positive`, `margin_negative`, `margin_not_reported`)
- Lymph node summary (`nodes_examined`, `nodes_positive`)
- Resection type (`R0`, `R1`, `R2`)
- Staging (pT/pN/pM) from pathology synoptic sections

## Design notes

- Extraction will be prompt-based (Claude API), not regex-based
- One API call per note batch (notes are chunked to stay within context limits)
- Output schema is fixed per IRB — the audit JSON's `approved_elements` list constrains which
  features are extracted
- Will reuse `excavator/shared/prompts.py` BASE_SYSTEM_PROMPT for IRB compliance rules

## Status

Not yet implemented. The excavator generates the raw text; this stage structures it.
