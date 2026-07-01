# ZC_PAT_RELATION

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=ZC_PAT_RELATION

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | FULL |
| Load Frequency | INCREMENTAL |
| Chronicles INI | N/A |
| Release Version | FALL 2004 |
| May contain EHI? | No |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| PAT_RELATION_C | VARCHAR (66) |  |
| NAME | VARCHAR (254) |  |
| TITLE | VARCHAR (254) |  |
| ABBR | VARCHAR (254) |  |
| INTERNAL_ID | VARCHAR (66) |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | PAT_RELATION_C | ZC_EMERG_PAT_REL | EMERG_PAT_REL_C | No | No | No |  |
| 1 | PAT_RELATION_C | ZC_PAT_REL_RELATIO | PAT_REL_RELATIO_C | No | No | No |  |
| 2 | NAME | ZC_EMERG_PAT_REL | EMERG_PAT_REL_C | No | No | No |  |
| 2 | NAME | ZC_PAT_RELATION | PAT_RELATION_C | No | No | No |  |
| 2 | NAME | ZC_PAT_REL_RELATIO | PAT_REL_RELATIO_C | No | No | No |  |
| 3 | TITLE | ZC_EMERG_PAT_REL | EMERG_PAT_REL_C | No | No | No |  |
| 3 | TITLE | ZC_PAT_RELATION | PAT_RELATION_C | No | No | No |  |
| 3 | TITLE | ZC_PAT_REL_RELATIO | PAT_REL_RELATIO_C | No | No | No |  |
| 4 | ABBR | ZC_EMERG_PAT_REL | EMERG_PAT_REL_C | No | No | No |  |
| 4 | ABBR | ZC_PAT_RELATION | PAT_RELATION_C | No | No | No |  |
| 4 | ABBR | ZC_PAT_REL_RELATIO | PAT_REL_RELATIO_C | No | No | No |  |
| 5 | INTERNAL_ID | ZC_EMERG_PAT_REL | EMERG_PAT_REL_C | No | No | No |  |
| 5 | INTERNAL_ID | ZC_PAT_RELATION | PAT_RELATION_C | No | No | No |  |
| 5 | INTERNAL_ID | ZC_PAT_REL_RELATIO | PAT_REL_RELATIO_C | No | No | No |  |
