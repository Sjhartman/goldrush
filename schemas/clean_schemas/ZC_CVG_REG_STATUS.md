# ZC_CVG_REG_STATUS

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=ZC_CVG_REG_STATUS

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | FULL |
| Load Frequency | INCREMENTAL |
| Chronicles INI | N/A |
| Release Version | MU4 - EPIC 2002 |
| May contain EHI? | No |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| CVG_REG_STATUS_C | VARCHAR (66) |  |
| NAME | VARCHAR (254) |  |
| TITLE | VARCHAR (254) |  |
| ABBR | VARCHAR (254) |  |
| INTERNAL_ID | VARCHAR (66) |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | CVG_REG_STATUS_C | ZC_GUAR_VERIF_STAT | GUAR_VERIF_STAT_C | No | No | No |  |
| 1 | CVG_REG_STATUS_C | ZC_REG_STATUS | REG_STATUS_C | No | No | No |  |
