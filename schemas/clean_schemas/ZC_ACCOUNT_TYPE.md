# ZC_ACCOUNT_TYPE

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=ZC_ACCOUNT_TYPE

## Description

This table contains the category definitions for guarantor account type (e.g. Personal/Family, etc.)

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
| ACCOUNT_TYPE_C | EAF |  |
| NAME | EAF |  |
| TITLE | EAF |  |
| ABBR | EAF |  |
| INTERNAL_ID | EAF |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ACCOUNT_TYPE_C | ZC_ACCT_TYPE_2 | ACCT_TYPE_2_C | No | No | No |  |
