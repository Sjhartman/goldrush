# ZC_FINANCIAL_CLASS

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=ZC_FINANCIAL_CLASS

## Description

This table holds the financial class category list. Examples of standard category values in this list are Commercial and Self-Pay.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | FULL |
| Load Frequency | INCREMENTAL |
| Chronicles INI | N/A |
| Release Version | EPIC 2000 |
| May contain EHI? | No |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| FINANCIAL_CLASS | CBD |  |
| NAME | CBD |  |
| TITLE | CBD |  |
| ABBR | CBD |  |
| INTERNAL_ID | CBD |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | FINANCIAL_CLASS | CLARITY_FC | FINANCIAL_CLASS | No | No | No |  |
| 1 | FINANCIAL_CLASS | ZC_ACTN_FIN_CLASS | ACTION_FIN_CLASS | No | No | No |  |
| 1 | FINANCIAL_CLASS | ZC_CUR_FIN_CLASS | CUR_FIN_CLASS | No | No | No |  |
| 1 | FINANCIAL_CLASS | ZC_FC_MEDICAID | FC_MEDICAID_C | No | No | No |  |
| 1 | FINANCIAL_CLASS | ZC_FIN_CLASS | FIN_CLASS_C | No | No | No |  |
| 1 | FINANCIAL_CLASS | ZC_ORIG_FIN_CLASS | ORIGINAL_FIN_CLASS | No | No | No |  |
