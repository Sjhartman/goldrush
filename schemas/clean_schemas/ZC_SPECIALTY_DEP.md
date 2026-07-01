# ZC_SPECIALTY_DEP

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=ZC_SPECIALTY_DEP

## Description

This table contains the category information for department specialties.

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
| SPECIALTY_DEP_C | VARCHAR (66) |  |
| NAME | VARCHAR (254) |  |
| TITLE | VARCHAR (254) |  |
| ABBR | VARCHAR (254) |  |
| INTERNAL_ID | VARCHAR (66) |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | SPECIALTY_DEP_C | ZC_DEP_SPECIALTY | DEP_SPECIALTY_C | No | No | No |  |
| 1 | SPECIALTY_DEP_C | ZC_REFD_TO_SPEC | REFD_TO_SPEC_C | No | No | No |  |
| 1 | SPECIALTY_DEP_C | ZC_REFD_TO_SPECLTY | REFD_TO_SPECLTY_C | No | No | No |  |
