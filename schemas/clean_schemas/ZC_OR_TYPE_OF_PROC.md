# ZC_OR_TYPE_OF_PROC

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=ZC_OR_TYPE_OF_PROC

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | FULL |
| Load Frequency | INCREMENTAL |
| Chronicles INI | N/A |
| Release Version | MU1 - MAY 2001 |
| May contain EHI? | No |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| TYPE_OF_PROC_C | VARCHAR (66) |  |
| NAME | VARCHAR (254) |  |
| TITLE | VARCHAR (254) |  |
| ABBR | VARCHAR (254) |  |
| INTERNAL_ID | VARCHAR (66) |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 5 | INTERNAL_ID | ZC_OR_TYPE_OF_PROC | TYPE_OF_PROC_C | No | No | No |  |
