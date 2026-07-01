# ZC_ORDER_CLASS

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=ZC_ORDER_CLASS

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
| ORDER_CLASS_C | VARCHAR (66) |  |
| NAME | VARCHAR (254) |  |
| TITLE | VARCHAR (254) |  |
| ABBR | VARCHAR (254) |  |
| INTERNAL_ID | VARCHAR (66) |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ORDER_CLASS_C | ZC_LLB_ORDER_CLASS | LLB_ORDER_CLASS_C | No | No | No |  |
| 1 | ORDER_CLASS_C | ZC_PANEL_INP_CLASS | PANEL_INP_CLASS_C | No | No | No |  |
| 1 | ORDER_CLASS_C | ZC_PNL_PROC_CLASS | PNL_PROC_CLASS_C | No | No | No |  |
