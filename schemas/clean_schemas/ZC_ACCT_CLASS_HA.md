# ZC_ACCT_CLASS_HA

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=ZC_ACCT_CLASS_HA

## Description

This table contains the category information for account classes.

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
| ACCT_CLASS_HA_C | VARCHAR (66) |  |
| NAME | VARCHAR (254) |  |
| TITLE | VARCHAR (254) |  |
| ABBR | VARCHAR (254) |  |
| INTERNAL_ID | VARCHAR (66) |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ACCT_CLASS_HA_C | ZC_OVERRIDE_CLASS | OVERRIDE_CLASS_C | No | No | No |  |
| 1 | ACCT_CLASS_HA_C | ZC_PAT_CLASS | ADT_PAT_CLASS_C | No | No | No |  |
