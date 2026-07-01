# ZC_SIMPLE_GENERIC

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=ZC_SIMPLE_GENERIC

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
| SIMPLE_GENERIC_C | VARCHAR (66) |  |
| NAME | VARCHAR (254) |  |
| TITLE | VARCHAR (254) |  |
| ABBR | VARCHAR (254) |  |
| INTERNAL_ID | VARCHAR (66) |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 5 | INTERNAL_ID | ZC_SIMPLE_GENERIC | SIMPLE_GENERIC_C | No | No | No |  |
