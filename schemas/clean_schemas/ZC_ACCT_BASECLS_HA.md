# ZC_ACCT_BASECLS_HA

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=ZC_ACCT_BASECLS_HA

## Description

This table contains the category information for account base classes.

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
| ACCT_BASECLS_HA_C | INTEGER |  |
| NAME | VARCHAR (254) |  |
| TITLE | VARCHAR (254) |  |
| ABBR | VARCHAR (254) |  |
| INTERNAL_ID | INTEGER |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ACCT_BASECLS_HA_C | ZC_OVERRIDE_BASE | OVERRIDE_BASE_C | No | No | No |  |
