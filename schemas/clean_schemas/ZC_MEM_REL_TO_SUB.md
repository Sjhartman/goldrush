# ZC_MEM_REL_TO_SUB

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=ZC_MEM_REL_TO_SUB

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | FULL |
| Load Frequency | INCREMENTAL |
| Chronicles INI | N/A |
| Release Version | EPIC 2002 |
| May contain EHI? | No |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| MEM_REL_TO_SUB_C | INTEGER |  |
| NAME | VARCHAR (254) |  |
| TITLE | VARCHAR (254) |  |
| ABBR | VARCHAR (254) |  |
| INTERNAL_ID | INTEGER |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | MEM_REL_TO_SUB_C | ZC_COB_MEM_RELX | COB_MEM_RELX_C | No | No | No |  |
| 1 | MEM_REL_TO_SUB_C | ZC_MEM_REL_TO_GUAR | MEM_REL_TO_GUAR_C | No | No | No |  |
