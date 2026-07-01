# ZC_TAX_STATE

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=ZC_TAX_STATE

## Description

The category table for the state.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | FULL |
| Load Frequency | INCREMENTAL |
| Chronicles INI | N/A |
| Release Version | Rel 2010 |
| May contain EHI? | No |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| TAX_STATE_C | 50 |  |
| NAME | 50 |  |
| TITLE | 50 |  |
| ABBR | 50 |  |
| INTERNAL_ID | 50 |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | TAX_STATE_C | ZC_ALT_INVOICE_STA | ALT_INVOICE_STA_C | No | No | No |  |
| 1 | TAX_STATE_C | ZC_LLB_STATE | LLB_STATE_C | No | No | No |  |
| 1 | TAX_STATE_C | ZC_REFG_PROV_STATE | REFG_PROV_STATE_C | No | No | No |  |
| 1 | TAX_STATE_C | ZC_STATE | STATE_C | No | No | No |  |
| 1 | TAX_STATE_C | ZC_STATE_HISTORY | STATE_HISTORY_C | No | No | No |  |
| 1 | TAX_STATE_C | ZC_SUBSCR_EEP_STE | SUBSCR_EEP_STE_C | No | No | No |  |
