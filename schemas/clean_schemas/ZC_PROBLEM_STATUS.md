# ZC_PROBLEM_STATUS

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=ZC_PROBLEM_STATUS

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | FULL |
| Load Frequency | INCREMENTAL |
| Chronicles INI | N/A |
| Release Version | SPRING 2008 |
| May contain EHI? | No |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| PROBLEM_STATUS_C | 160 |  |
| NAME | 160 |  |
| TITLE | 160 |  |
| ABBR | 160 |  |
| INTERNAL_ID | 160 |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | PROBLEM_STATUS_C | ZC_HX_STATUS | HX_STATUS_C | No | No | No |  |
