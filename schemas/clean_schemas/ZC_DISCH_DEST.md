# ZC_DISCH_DEST

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=ZC_DISCH_DEST

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
| DISCH_DEST_C | VARCHAR (66) |  |
| NAME | VARCHAR (254) |  |
| TITLE | VARCHAR (254) |  |
| ABBR | VARCHAR (254) |  |
| INTERNAL_ID | VARCHAR (66) |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | DISCH_DEST_C | ZC_DISCH_DESTIN_HA | DISCH_DESTIN_HA_C | No | No | No |  |
| 5 | INTERNAL_ID | ZC_DISCH_DEST | DISCH_DEST_C | No | No | No |  |
| 5 | INTERNAL_ID | ZC_DISCH_DESTIN_HA | DISCH_DESTIN_HA_C | No | No | No |  |
