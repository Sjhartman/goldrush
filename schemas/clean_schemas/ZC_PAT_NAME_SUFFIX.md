# ZC_PAT_NAME_SUFFIX

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=ZC_PAT_NAME_SUFFIX

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
| PAT_NAME_SUFFIX_C | INTEGER |  |
| NAME | VARCHAR (254) |  |
| TITLE | VARCHAR (254) |  |
| ABBR | VARCHAR (254) |  |
| INTERNAL_ID | INTEGER |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | PAT_NAME_SUFFIX_C | ZC_SUFFIX | SUFFIX_C | No | No | No |  |
