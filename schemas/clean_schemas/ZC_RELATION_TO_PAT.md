# ZC_RELATION_TO_PAT

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=ZC_RELATION_TO_PAT

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | FULL |
| Load Frequency | INCREMENTAL |
| Chronicles INI | N/A |
| Release Version | SPRING 2006 |
| May contain EHI? | No |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| RELATION_TO_PAT_C | INTEGER |  |
| NAME | VARCHAR (254) |  |
| TITLE | VARCHAR (254) |  |
| ABBR | VARCHAR (254) |  |
| INTERNAL_ID | INTEGER |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | RELATION_TO_PAT_C | ZC_ESIG_RELATION | ESIG_RELATION_C | No | No | No |  |
