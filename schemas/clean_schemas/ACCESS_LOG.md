# ACCESS_LOG

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=ACCESS_LOG

## Description

The ACCESS_LOG table contains the basic access information of each activity, such as the time the event occurred and process ID.  This table contains only those metrics with an Access History log type; the ACCESS_WRKF table contains metrics with a Workflow Activity log type.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | APPEND |
| Load Frequency | AUDIT |
| Chronicles INI | N/A |
| Release Version | MU13 - MAY 2001 |
| May contain EHI? | No |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| ACCESS_INSTANT | No | The UTC instant when this access history event was logged into the system. This value may be on or after the time the event actually occurred, which is stored in ACCESS_TIME. After completing the primary key conversion detailed in SLG 2591452, use ACCESS_TIME to filter any query on ACCESS_LOG. |
| PROCESS_ID | No | The unique ID of the Cach? process for the Hyperspace connection to Chronicles. |
| ACCESS_TIME | No | The date and time when the access history event happened.  After completing the primary key conversion detailed in SLG 2591452, use this column to filter any query on ACCESS_LOG. |
| METRIC_ID | NUMERIC (18,0) | The unique ID of the metric that specifies what action has been taken by the user. |
| USER_ID | No | The unique ID of the user who was logged in when this access history event occurred. This column is frequently used to link to the CLARITY_EMP table. |
| WORKSTATION_ID | VARCHAR (254) | The identifier of the workstation on which this access history event occurred. |
| PAT_ID | No | The unique ID of the patient record associated with this access history event. This column is frequently used to link to the PATIENT table. |
| CSN | No | The unique contact serial number corresponding to this access history event.  If this event is associated with a patient encounter record, the encounter data should be retrieved by linking ACCESS_LOG.CSN to PAT_ENC.PAT_ENC_CSN_ID.  Note that not all event records will have associated patient encounter data. |
| ACCESS_ACTION_C | INTEGER |  |
| DEPLOYMENT_ID | No | The Community ID (CID) of the instance that this access history event occurred on. This is only populated if you use IntraConnect. |
| AUDIT_SESSION_ID | No | The unique ID of the audit session during which this event occurred.  This column is used to link to the AUDIT_SESSION table. |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| BITMAP INDEX | EIX_ACCLG_DPLY_ID | DEPLOYMENT_ID | 1 | No | Yes |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 4 | METRIC_ID | ACCESS_LOG_METRIC | METRIC_ID | Unknown | Yes | No |  |
| 4 | METRIC_ID | F_ACCESS_LOG_METRIC_NAME | METRIC_ID | Unknown | Unknown | No |  |
| 5 | USER_ID | CLARITY_EMP | USER_ID | Unknown | Yes | No |  |
| 5 | USER_ID | CLARITY_EMP_2 | USER_ID | Unknown | Yes | No |  |
| 5 | USER_ID | CLARITY_EMP_3 | USER_ID | Unknown | Yes | No |  |
| 5 | USER_ID | CLARITY_EMP_4 | USER_ID | No | Yes | No |  |
| 5 | USER_ID | CLARITY_EMP_DEMO | USER_ID | No | Yes | No |  |
| 5 | USER_ID | EMP_BASIC_INFO | USER_ID | No | Yes | No |  |
| 5 | USER_ID | EMP_DOC_SETTINGS | USER_NUMBER_ID | No | Yes | No |  |
| 5 | USER_ID | F_RX_USER | USER_ID | Unknown | Unknown | No |  |
| 5 | USER_ID | IB_MESSAGE_SETTINGS | USER_ID | No | Yes | No |  |
| 5 | USER_ID | LOGIN_INFO | USER_NUMBER_ID | No | Yes | No |  |
| 5 | USER_ID | QC_RESULTS_REVIEW | USER_NUMBER_ID | No | Yes | No |  |
| 5 | USER_ID | USER_SIDEBAR_RPT | USER_NUMBER_ID | Unknown | Yes | No |  |
| 5 | USER_ID | V_CUBE_D_USER | USER_ID | Unknown | Unknown | No |  |
| 5 | USER_ID | V_CUBE_RX_USER | USER_ID | Unknown | Unknown | No |  |
| 6 | WORKSTATION_ID | CLARITY_LWS | WORKSTN_IDENTIFIER | Unknown | Unknown | Yes |  |
| 7 | PAT_ID | ANTICOAG_SELF_REGULATING | PAT_ID | No | Yes | No |  |
| 7 | PAT_ID | CARE_COORDINATION | PAT_ID | Unknown | Yes | No |  |
| 7 | PAT_ID | CLAIMS_DERIVE_PAT_FLAGS | PAT_ID | No | Yes | No |  |
| 7 | PAT_ID | COMMUNITY_RESRC_REVIEWED | PAT_ID | No | Yes | No |  |
| 7 | PAT_ID | D_PAT_GEOGRAPHIC_CLASS | PAT_ID | Unknown | Unknown | No |  |
| 7 | PAT_ID | EPT_MEM_INFO | PAT_ID | No | Yes | No |  |
| 7 | PAT_ID | EXT_DATA_LAST_DONE | PAT_ID | No | Yes | No |  |
| 7 | PAT_ID | F_IBD_ADULT_FORM_PAT | PAT_ID | Unknown | Unknown | No |  |
| 7 | PAT_ID | HH_PAT_INFO | PAT_ID | Unknown | Yes | No |  |
| 7 | PAT_ID | HM_STATUS_UPD | PAT_ID | No | Yes | No |  |
| 7 | PAT_ID | IMMNZTN_LAST_REVIEW | PAT_ID | No | Yes | No |  |
| 7 | PAT_ID | PATIENT | PAT_ID | No | Yes | No |  |
| 7 | PAT_ID | PATIENT_2 | PAT_ID | No | Yes | No |  |

_(54 total; showing first 30)_
