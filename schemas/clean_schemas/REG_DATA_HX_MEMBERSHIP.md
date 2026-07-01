# REG_DATA_HX_MEMBERSHIP

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=REG_DATA_HX_MEMBERSHIP

## Description

History data on the status changes to registry inclusion.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | RDT |
| Release Version | Rel 2015 |
| May contain EHI? | No |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| RECORD_ID | NUMERIC (18,0) | The unique identifier (.1 item) for the registry data record. |
| CONTACT_DATE_REAL | FLOAT | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| LINE | INTEGER | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| CONTACT_DATE | DATETIME | The date of this contact in calendar format. |
| REGISTRY_ID | NUMERIC (18,0) | The HFR ID of the registry for which the inclusion status was changed. |
| CHANGE_INSTANT_UTC_DTTM | DATETIME (UTC) | The instant for which the inclusion status of a registry was changed. |
| STATUS_C | INTEGER |  |
| STATUS_REASON_C | INTEGER | Surrogate key used to uniquely identify rows in this (and only this) table on Cogito Cloud only, do not assume the surrogate key in this table will correspond to the surrogate key in another table |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | RECORD_ID | DM_ACG_RISK | RECORD_ID | Unknown | Yes | No |  |
| 1 | RECORD_ID | DM_ACO | RECORD_ID | Unknown | Yes | No |  |
| 1 | RECORD_ID | DM_ACO_EXT | RECORD_ID | Unknown | Yes | No |  |
| 1 | RECORD_ID | DM_ACTIVE_PAT | RECORD_ID | Unknown | Yes | No |  |
| 1 | RECORD_ID | DM_ADHD | RECORD_ID | Unknown | Yes | No |  |
| 1 | RECORD_ID | DM_ADHD_EXT | RECORD_ID | Unknown | Yes | No |  |
| 1 | RECORD_ID | DM_ADOL_TRANS | RECORD_ID | Unknown | Yes | No |  |
| 1 | RECORD_ID | DM_ADOL_TRANS_EXT | RECORD_ID | Unknown | Yes | No |  |
| 1 | RECORD_ID | DM_ADULT_ADHD | RECORD_ID | Unknown | Yes | No |  |
| 1 | RECORD_ID | DM_ADULT_ASTHMA | RECORD_ID | Unknown | Yes | No |  |
| 1 | RECORD_ID | DM_ADULT_DIABETES | RECORD_ID | Unknown | Yes | No |  |
| 1 | RECORD_ID | DM_ADULT_FTM | RECORD_ID | Unknown | Yes | No |  |
| 1 | RECORD_ID | DM_ADULT_FTM_EXT | RECORD_ID | Unknown | Yes | No |  |
| 1 | RECORD_ID | DM_ADULT_HIV | RECORD_ID | Unknown | Yes | No |  |
| 1 | RECORD_ID | DM_ADULT_HYPERTENSION | RECORD_ID | Unknown | Yes | No |  |
| 1 | RECORD_ID | DM_ADULT_MTF | RECORD_ID | Unknown | Yes | No |  |
| 1 | RECORD_ID | DM_ADULT_MTF_EXT | RECORD_ID | Unknown | Yes | No |  |
| 1 | RECORD_ID | DM_ADULT_OBESITY | RECORD_ID | Unknown | Yes | No |  |
| 1 | RECORD_ID | DM_ALS | RECORD_ID | Unknown | Yes | No |  |
| 1 | RECORD_ID | DM_ANESTHESIA | RECORD_ID | Unknown | Yes | No |  |
| 1 | RECORD_ID | DM_ANESTHESIA_2 | RECORD_ID | Unknown | Yes | No |  |
| 1 | RECORD_ID | DM_ASTHMA | RECORD_ID | Unknown | Yes | No |  |
| 1 | RECORD_ID | DM_ASTHMA_EXT | RECORD_ID | Unknown | Yes | No |  |
| 1 | RECORD_ID | DM_ATRIAL_FIBRILLATION | RECORD_ID | Unknown | Yes | No |  |
| 1 | RECORD_ID | DM_BREAST_HEALTH | RECORD_ID | Unknown | Yes | No |  |
| 1 | RECORD_ID | DM_CAD | RECORD_ID | Unknown | Yes | No |  |
| 1 | RECORD_ID | DM_CAD_DIABETES | RECORD_ID | Unknown | Yes | No |  |
| 1 | RECORD_ID | DM_CAD_EXT | RECORD_ID | Unknown | Yes | No |  |
| 1 | RECORD_ID | DM_CANCER_PATIENT | RECORD_ID | Unknown | Yes | No |  |
| 1 | RECORD_ID | DM_CANCER_PROBLEM | RECORD_ID | Unknown | Yes | No |  |

_(193 total; showing first 30)_
