# ZC_STATE

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=ZC_STATE

## Description

This table contains the categories for state/province.

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
| STATE_C | 70 |  |
| NAME | 70 |  |
| TITLE | 70 |  |
| ABBR | 70 |  |
| INTERNAL_ID | 70 |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | STATE_C | ZC_ALT_INVOICE_STA | ALT_INVOICE_STA_C | No | No | No |  |
| 1 | STATE_C | ZC_LLB_STATE | LLB_STATE_C | No | No | No |  |
| 1 | STATE_C | ZC_REFG_PROV_STATE | REFG_PROV_STATE_C | No | No | No |  |
| 1 | STATE_C | ZC_STATE_HISTORY | STATE_HISTORY_C | No | No | No |  |
| 1 | STATE_C | ZC_SUBSCR_EEP_STE | SUBSCR_EEP_STE_C | No | No | No |  |
| 1 | STATE_C | ZC_TAX_STATE | TAX_STATE_C | No | No | No |  |
