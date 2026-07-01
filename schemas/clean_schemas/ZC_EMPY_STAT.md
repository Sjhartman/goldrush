# ZC_EMPY_STAT

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=ZC_EMPY_STAT

## Description

This table will be deprecated in a future release. You should use ZC_EMPY_STATUS when reporting on this category list.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | FULL |
| Load Frequency | INCREMENTAL |
| Chronicles INI | N/A |
| Release Version | Summer 2009 |
| May contain EHI? | No |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| EMPY_STAT_C | 271 |  |
| NAME | 271 |  |
| TITLE | 271 |  |
| ABBR | 271 |  |
| INTERNAL_ID | 271 |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | EMPY_STAT_C | ZC_EMPY_STATUS | EMPY_STATUS_C | No | No | No |  |
| 1 | EMPY_STAT_C | ZC_SUBSCR_EMP_STAT | SUBSCR_EMP_STAT_C | No | No | No |  |
