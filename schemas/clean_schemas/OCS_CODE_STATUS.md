# OCS_CODE_STATUS

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=OCS_CODE_STATUS

## Description

This table contains information about patient code statuses, which are mainly used for documenting compliance reasons and quality. This table replaces the older IP_CODE_STATUS table.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | OCS |
| Release Version | SPRING 2007 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| OCS_ID | VARCHAR (30) | The unique ID for the code status record. |
| CM_PHY_OWNER_ID | VARCHAR (25) | Stores the physical owner of the record |
| CM_LOG_OWNER_ID | VARCHAR (25) | Stores the logical owner for the record |
| OCS_NAME | VARCHAR (200) | The name of the code status record. |
| OCS_STATUS_C | INTEGER |  |
| CODE_STATUS_C | VARCHAR (66) |  |
| ACTIVATED_INST | DATETIME (Local) | The instant at which the code status (full code, DNR, etc.) was created. |
| USER_ID | VARCHAR (18) | The unique identifier of the user that created the code status |
| ORDER_ID | NUMERIC (18,0) | The unique identifier for the code status order record. |
| COMMENTS | VARCHAR (450) | The comment associated with the code status. |
| INACTIVATED_INST | DATETIME (Local) | The instant at which the code status was inactivated. |
| CONTEXT_C | INTEGER |  |
| PATIENT_ID | VARCHAR (18) | The patient for which this code status was recorded. |
| PATIENT_CSN | NUMERIC (18,0) | The Contact Serial Number of the encounter in which the code status order was placed. |
| REC_ARCHIVED_YN | No | Indicates whether the Code Status record is archived at the record level. |
| ACTV_UTC_DTTM | DATETIME (UTC) | Holds the instant the code status was activated in UTC time. |
| INACTV_UTC_DTTM | DATETIME (UTC) | The instant at which the code status was inactivated in UTC time. |
| VERBAL_ORDER_ID | VARCHAR (254) | The unique identifier of the home care order that created this code status record. |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| BITMAP INDEX | EIX_OCS_CODE_STATUS_ORDER_ID | ORDER_ID | 1 | Yes | Yes |  |
| BITMAP INDEX | EIX_OCS_CODE_STATUS_PATIENT_ID | PATIENT_ID | 1 | Yes | Yes |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 2 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 2 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 3 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 5 | OCS_STATUS_C | ZC_RECORD_STATUS_2 | RECORD_STATUS_2_C | No | No | No |  |
| 5 | OCS_STATUS_C | ZC_RECORD_STS | RECORD_STS_C | No | No | No |  |
| 6 | CODE_STATUS_C | ZC_CODE_STATUS | CD_STATUS_C | No | No | No |  |
| 8 | USER_ID | CLARITY_EMP | USER_ID | Unknown | No | No |  |
| 8 | USER_ID | CLARITY_EMP_2 | USER_ID | Unknown | No | No |  |
| 8 | USER_ID | CLARITY_EMP_3 | USER_ID | Unknown | No | No |  |
| 8 | USER_ID | CLARITY_EMP_4 | USER_ID | No | No | No |  |
| 8 | USER_ID | CLARITY_EMP_DEMO | USER_ID | No | No | No |  |
| 8 | USER_ID | EMP_BASIC_INFO | USER_ID | No | No | No |  |
| 8 | USER_ID | EMP_DOC_SETTINGS | USER_NUMBER_ID | No | No | No |  |
| 8 | USER_ID | F_RX_USER | USER_ID | Unknown | Unknown | No |  |
| 8 | USER_ID | IB_MESSAGE_SETTINGS | USER_ID | No | No | No |  |
| 8 | USER_ID | LOGIN_INFO | USER_NUMBER_ID | No | No | No |  |
| 8 | USER_ID | QC_RESULTS_REVIEW | USER_NUMBER_ID | No | No | No |  |
| 8 | USER_ID | USER_SIDEBAR_RPT | USER_NUMBER_ID | Unknown | No | No |  |
| 8 | USER_ID | V_CUBE_D_USER | USER_ID | Unknown | Unknown | No |  |
| 8 | USER_ID | V_CUBE_RX_USER | USER_ID | Unknown | Unknown | No |  |
| 9 | ORDER_ID | ADT_ORDERS_ERRORS | ORDER_ID | No | No | No |  |
| 9 | ORDER_ID | ADT_ORDER_INFORMATION | ORDER_ID | No | No | No |  |
| 9 | ORDER_ID | APPT_REQUEST | REQUEST_ID | No | No | No |  |
| 9 | ORDER_ID | CL_ORD_FST_LST_SCH | ORDER_ID | No | No | No |  |
| 9 | ORDER_ID | DENT_ORD_NOADD | ORDER_ID | No | No | No |  |
| 9 | ORDER_ID | DUPMED_DISMISS_HH_INFO | ORDER_ID | No | No | No |  |
| 9 | ORDER_ID | ENDOSCOPY_METRICS | ORDER_ID | Unknown | No | No |  |

_(250 total; showing first 30)_
