# ZC_COUNTY

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=ZC_COUNTY

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
| COUNTY_C | VARCHAR (66) |  |
| NAME | VARCHAR (254) |  |
| TITLE | VARCHAR (254) |  |
| ABBR | VARCHAR (254) |  |
| INTERNAL_ID | VARCHAR (66) |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | COUNTY_C | ZC_COUNTY_2 | COUNTY_2_C | No | No | No |  |
| 1 | COUNTY_C | ZC_COUNTY_OVERTIME | COUNTY_OVERTIME_C | No | No | No |  |
