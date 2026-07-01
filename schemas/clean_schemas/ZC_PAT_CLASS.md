# ZC_PAT_CLASS

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=ZC_PAT_CLASS

## Description

This table contains the category information for the patient classes for the hospital encounter.

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
| ADT_PAT_CLASS_C | VARCHAR (66) |  |
| NAME | VARCHAR (254) |  |
| TITLE | VARCHAR (254) |  |
| ABBR | VARCHAR (254) |  |
| INTERNAL_ID | VARCHAR (66) |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ADT_PAT_CLASS_C | ZC_ACCT_CLASS_HA | ACCT_CLASS_HA_C | No | No | No |  |
| 1 | ADT_PAT_CLASS_C | ZC_OVERRIDE_CLASS | OVERRIDE_CLASS_C | No | No | No |  |
