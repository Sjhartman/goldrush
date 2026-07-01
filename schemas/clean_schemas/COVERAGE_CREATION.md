# COVERAGE_CREATION

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=COVERAGE_CREATION

## Description

*** Deprecated *** The table has been replaced by the ENTRY_DATE column on Clarity table COVERAGE_4.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | CVG |
| Release Version | Rel August 2018 |
| May contain EHI? | No |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| CVG_ID | NUMERIC (18,0) | The unique identifier (.1 item) for the coverage record. |
| CONTACT_DATE_REAL | FLOAT | A unique contact date in decimal format representing the date the coverage is created. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| CONTACT_DATE | DATETIME | The date when the coverage is created. |
