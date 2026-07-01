# ZC_EMPY_STATUS

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=ZC_EMPY_STATUS

## Description

This table contains information about the employment status category.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | FULL |
| Load Frequency | INCREMENTAL |
| Chronicles INI | N/A |
| Release Version | MU5 - EPIC 2002 |
| May contain EHI? | No |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| EMPY_STATUS_C | EAF |  |
| NAME | EAF |  |
| TITLE | EAF |  |
| ABBR | EAF |  |
| INTERNAL_ID | EAF |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | EMPY_STATUS_C | ZC_EMPY_STAT | EMPY_STAT_C | No | No | No |  |
| 1 | EMPY_STATUS_C | ZC_SUBSCR_EMP_STAT | SUBSCR_EMP_STAT_C | No | No | No |  |
