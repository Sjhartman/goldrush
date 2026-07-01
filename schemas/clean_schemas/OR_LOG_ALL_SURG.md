# OR_LOG_ALL_SURG

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=OR_LOG_ALL_SURG

## Description

The OR_LOG_ALL_SURG table contains OR management system log surgeons.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | ORL |
| Release Version | MU1 - MAY 2001 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| LOG_ID | VARCHAR (18) | The unique ID of the surgical log which refers to the surgeon. |
| LINE | No | The number of the line of the surgeon in this surgical log. |
| SURG_ID | VARCHAR (18) | The unique ID of the surgeon. |
| ROLE_C | INTEGER |  |
| SERVICE_C | VARCHAR (66) |  |
| START_TIME | DATETIME (Local) | The start date and time for the surgeon in the surgical log. |
| END_TIME | DATETIME (Local) | The end date and time for the surgeon in the surgical log. |
| TOTAL_LENGTH | INTEGER | The total time a surgeon was needed in the surgical log in seconds. |
| PANEL | INTEGER | The panel number in the surgical log in which the surgeon was involved. |
| CM_PHY_OWNER_ID | VARCHAR (25) | ID of the physical deployment owner for this record.  Physical owners will be where the data is hosted, either on the cross-over server or the owner deployment. |
| CM_LOG_OWNER_ID | VARCHAR (25) | ID of the logical deployment owner for this record.  Logical owners show the deployment where the record was created but doesn't represent if the record is a part of version skew. |
| RTLS_OFF_YN | VARCHAR (1) |  |
| TIME_SOURCE_STATUS_C | INTEGER |  |
| START_TIME_CMT | VARCHAR (254) | The start time comment for the surgeon in the surgical log. |
| END_TIME_CMT | VARCHAR (254) | The end time comment for the surgeon in the surgical log. |
| START_TIME_DOCU_ID | VARCHAR (18) | The unique ID of the EMP user who documented the start time for each surgeon associated with any panel of the surgical log. |
| END_TIME_DOCU_ID | VARCHAR (18) | The unique ID of the EMP user who documented the end time for each surgeon associated with any panel of the surgical log. |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| B-TREE INDEX | EIX_OR_LOG_ALL_SURG_ROLE_C | ROLE_C | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_OR_LOG_ALL_SURG_SUID | SURG_ID | 1 | Yes | Yes |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | LOG_ID | F_LOG_BASED | LOG_ID | Unknown | Unknown | No |  |
| 1 | LOG_ID | OR_LOG | LOG_ID | Unknown | No | No |  |
| 1 | LOG_ID | OR_LOG_2 | LOG_ID | Unknown | No | No |  |
| 1 | LOG_ID | OR_LOG_3 | LOG_ID | No | No | No |  |
| 1 | LOG_ID | OR_LOG_METRIC_DETAILS | LOG_ID | No | No | No |  |
| 1 | LOG_ID | OR_LOG_PRECEDING | LOG_ID | No | No | No |  |
| 1 | LOG_ID | OR_LOG_VIRTUAL | LOG_ID | No | No | No |  |
| 1 | LOG_ID | UK_CRM_PACEMKR_PROC | LOG_ID | No | No | No |  |
| 1 | LOG_ID | V_CASE_CHARGES | LOG_ID | Unknown | Unknown | No |  |
| 1 | LOG_ID | V_CASE_COSTS | LOG_ID | Unknown | Unknown | No |  |
| 1 | LOG_ID | V_CASE_ON_TIME_START | LOG_ID | Unknown | Unknown | No |  |
| 1 | LOG_ID | V_CASE_PHYS_TURNOVER | LOG_ID | Unknown | Unknown | No |  |
| 1 | LOG_ID | V_CASE_ROOM_TURNOVER | LOG_ID | Unknown | Unknown | No |  |
| 1 | LOG_ID | V_CASE_VOLUME | LOG_ID | Unknown | Unknown | No |  |
| 1 | LOG_ID | V_DECISION_TO_INCISION | LOG_ID | Unknown | Unknown | No |  |
| 1 | LOG_ID | V_LOG_BASED | LOG_ID | Unknown | Unknown | No |  |
| 1 | LOG_ID | V_LOG_TIMING_EVENTS | LOG_ID | Unknown | Unknown | No |  |
| 3 | SURG_ID | CLARITY_SER | PROV_ID | Unknown | No | No |  |
| 3 | SURG_ID | CLARITY_SER_2 | PROV_ID | Unknown | No | No |  |
| 3 | SURG_ID | CLARITY_SER_3 | PROV_ID | Unknown | No | No |  |
| 3 | SURG_ID | CLARITY_SER_4 | PROV_ID | No | No | No |  |
| 3 | SURG_ID | CLARITY_SER_MYC | PROV_ID | Unknown | No | No |  |
| 3 | SURG_ID | D_PROV_PRIMARY_HIERARCHY | PROV_ID | Unknown | Unknown | No |  |
| 3 | SURG_ID | ED_SER_SETTINGS | PROV_ID | Unknown | No | No |  |
| 3 | SURG_ID | EXT_CAL_PROV_CONFIG | PROV_ID | No | No | No |  |
| 3 | SURG_ID | OR_SER_EQUIPMENT | PROV_ID | Unknown | No | No |  |
| 3 | SURG_ID | OR_SER_ROOM | PROV_ID | Unknown | No | No |  |
| 3 | SURG_ID | PROV_BATCH_LTR_GEN | PROV_ID | Unknown | No | No |  |
| 3 | SURG_ID | PROV_GROUP | PROV_ID | No | No | No |  |
| 3 | SURG_ID | V_CUBE_D_PROVIDER | PROVIDER_ID | Unknown | Unknown | No |  |

_(67 total; showing first 30)_
