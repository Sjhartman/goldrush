# ZC_COUNTRY

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=ZC_COUNTRY

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
| COUNTRY_C | VARCHAR (66) |  |
| NAME | VARCHAR (254) |  |
| TITLE | VARCHAR (254) |  |
| ABBR | VARCHAR (254) |  |
| INTERNAL_ID | VARCHAR (66) |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | COUNTRY_C | ZC_COUNTRY_2 | COUNTRY_2_C | No | No | No |  |
| 1 | COUNTRY_C | ZC_COUNTRY_4 | COUNTRY_4_C | No | No | No |  |
