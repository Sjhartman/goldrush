# ZC_LANGUAGE

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=ZC_LANGUAGE

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
| LANGUAGE_C | VARCHAR (66) |  |
| NAME | VARCHAR (254) |  |
| TITLE | VARCHAR (254) |  |
| ABBR | VARCHAR (254) |  |
| INTERNAL_ID | VARCHAR (66) |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | LANGUAGE_C | ZC_PREF_PCP_LANG | PREF_PCP_LANG_C | No | No | No |  |
| 5 | INTERNAL_ID | ZC_LANGUAGE | LANGUAGE_C | No | No | No |  |
| 5 | INTERNAL_ID | ZC_PREF_PCP_LANG | PREF_PCP_LANG_C | No | No | No |  |
