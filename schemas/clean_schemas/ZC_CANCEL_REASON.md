# ZC_CANCEL_REASON

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=ZC_CANCEL_REASON

## Description

This table contains category values for EPT 7300, indicating the cancel reason for the appointment.

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
| CANCEL_REASON_C | INTEGER |  |
| NAME | VARCHAR (254) |  |
| TITLE | VARCHAR (254) |  |
| ABBR | VARCHAR (254) |  |
| INTERNAL_ID | INTEGER |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | CANCEL_REASON_C | V_ZC_CANCEL_REASON | CANCEL_REASON_C | Unknown | Unknown | No |  |
