# REG_DATA_HX_METRICS

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=REG_DATA_HX_METRICS

## Description

This is the history of the registry data's metrics and their associated values.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | RDT |
| Release Version | Rel 2014 |
| May contain EHI? | No |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| RDT_ID | NUMERIC (18,0) | The unique identifier (.1 item) for the registry data record. |
| CONTACT_DATE_REAL | FLOAT | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| LINE | INTEGER | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| CONTACT_DATE | DATETIME | The date of this contact in calendar format. |
| HX_MET_ID | VARCHAR (18) | The ID of the historical metric. |
| HX_MET_LAST_UPD_DTTM | DATETIME (UTC) | The UTC instant at which the metric was updated for this registry data record. |
| HX_MET_STRING_VAL | VARCHAR (1000) | Historical data for RDT 230 (String value). |
| HX_MET_VAL_DESC_C | INTEGER |  |
| HX_MET_UNIT | VARCHAR (100) | Historical data for RDT 235 (Unit). |
| HX_LINKED_DATE | DATETIME | Historical data for RDT 240 (Linked date). |
| HX_MET_DATE_DESC_C | INTEGER |  |
| HX_ASSOC_INI | VARCHAR (3) | Historical data for RDT 250 (Associated INI). |
| HX_ASSOC_ITEM | VARCHAR (10) | Historical data for RDT 260 (Associated item). |
| HX_ASSOC_ID | VARCHAR (25) | Historical data for RDT 270 (Associated ID). |
| HX_ASSOC_COMMENTS | VARCHAR (254) | Historical data for RDT 280 (Associated comments). |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | RDT_ID | DM_ACG_RISK | RECORD_ID | Unknown | No | No |  |
| 1 | RDT_ID | DM_ACO | RECORD_ID | Unknown | No | No |  |
| 1 | RDT_ID | DM_ACO_EXT | RECORD_ID | Unknown | No | No |  |
| 1 | RDT_ID | DM_ACTIVE_PAT | RECORD_ID | Unknown | No | No |  |
| 1 | RDT_ID | DM_ADHD | RECORD_ID | Unknown | No | No |  |
| 1 | RDT_ID | DM_ADHD_EXT | RECORD_ID | Unknown | No | No |  |
| 1 | RDT_ID | DM_ADOL_TRANS | RECORD_ID | Unknown | No | No |  |
| 1 | RDT_ID | DM_ADOL_TRANS_EXT | RECORD_ID | Unknown | No | No |  |
| 1 | RDT_ID | DM_ADULT_ADHD | RECORD_ID | Unknown | No | No |  |
| 1 | RDT_ID | DM_ADULT_ASTHMA | RECORD_ID | Unknown | No | No |  |
| 1 | RDT_ID | DM_ADULT_DIABETES | RECORD_ID | Unknown | No | No |  |
| 1 | RDT_ID | DM_ADULT_FTM | RECORD_ID | Unknown | No | No |  |
| 1 | RDT_ID | DM_ADULT_FTM_EXT | RECORD_ID | Unknown | No | No |  |
| 1 | RDT_ID | DM_ADULT_HIV | RECORD_ID | Unknown | No | No |  |
| 1 | RDT_ID | DM_ADULT_HYPERTENSION | RECORD_ID | Unknown | No | No |  |
| 1 | RDT_ID | DM_ADULT_MTF | RECORD_ID | Unknown | No | No |  |
| 1 | RDT_ID | DM_ADULT_MTF_EXT | RECORD_ID | Unknown | No | No |  |
| 1 | RDT_ID | DM_ADULT_OBESITY | RECORD_ID | Unknown | No | No |  |
| 1 | RDT_ID | DM_ALS | RECORD_ID | Unknown | No | No |  |
| 1 | RDT_ID | DM_ANESTHESIA | RECORD_ID | Unknown | No | No |  |
| 1 | RDT_ID | DM_ANESTHESIA_2 | RECORD_ID | Unknown | No | No |  |
| 1 | RDT_ID | DM_ASTHMA | RECORD_ID | Unknown | No | No |  |
| 1 | RDT_ID | DM_ASTHMA_EXT | RECORD_ID | Unknown | No | No |  |
| 1 | RDT_ID | DM_ATRIAL_FIBRILLATION | RECORD_ID | Unknown | No | No |  |
| 1 | RDT_ID | DM_BREAST_HEALTH | RECORD_ID | Unknown | No | No |  |
| 1 | RDT_ID | DM_CAD | RECORD_ID | Unknown | No | No |  |
| 1 | RDT_ID | DM_CAD_DIABETES | RECORD_ID | Unknown | No | No |  |
| 1 | RDT_ID | DM_CAD_EXT | RECORD_ID | Unknown | No | No |  |
| 1 | RDT_ID | DM_CANCER_PATIENT | RECORD_ID | Unknown | No | No |  |
| 1 | RDT_ID | DM_CANCER_PROBLEM | RECORD_ID | Unknown | No | No |  |

_(192 total; showing first 30)_
