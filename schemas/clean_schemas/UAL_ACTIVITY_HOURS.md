# UAL_ACTIVITY_HOURS

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=UAL_ACTIVITY_HOURS

## Description

This table stores user action log data about how activities were used within workspace actions summarized by hour of the day. Each row represents an activity in which a user took actions on a workstation for an hour of the day, summarized by workspace kind and subkind.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | APPEND |
| Load Frequency | INCREMENTAL |
| Chronicles INI | N/A |
| Release Version | Rel February 2019 |
| May contain EHI? | No |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| UAL_ACTIVITY_HOUR_KEY | No | Surrogate key used to uniquely identify the user action log activity hour. |
| USER_ID | No | The unique ID of the user who visited the activity from the workstation during the hour. This column is frequently used to link to the CLARITY_EMP table. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| WORKSTATION_ID | No | The unique identifier of the workstation record from which the user visited activities during the hour. |
| ACTIVITY_HOUR_DTTM | No | The hour during which the user visited the activity from the workstation using the time zone of the workstation record. |
| ACTIVITY_HOUR_UTC_DTTM | No | The UTC hour during which the user visited the activity from the workstation. |
| WORKSPACE_KIND | No | The descriptor of the workspace record which uniquely identifies the workspace when combined with the workspace subkind. |
| WORKSPACE_SUBKIND | No | The context in which the clinical workspace was opened which uniquely identifies the workspace when combined with the workspace kind. |
| PAT_ENC_CSN_ID | No | The unique contact serial number for the patient encounter for which the activity was used. |
| ACTIVITY_ID | No | The unique identifier of the activity record opened during the hour. |
| EPIC_RELEASED_ACTIVITY_ID | No | The E2N ID of the Epic-released E2N record mapped to the value in ACTIVITY_ID. For Epic-released E2N records, this will be the same as the value in ACTIVITY_ID. |
| HISTORY_POINT_INI | No | The INI of the history point of the activity. For example, if the user were in a particular flowsheet template in the flowsheets activity, this would be 'FLT.' |
| HISTORY_POINT_ID | No | The record ID or category ID of the history point of the activity. For example, if the user were in a particular flowsheet template in the flowsheets activity, this would be the FLT ID.  This can either be an FLT ID, LVN ID, LCE ID, LQT ID, or a category ID.  If HISTORY_POINT_ITEM is null, this is a record ID, so use HISTORY_POINT_INI to identify the record type.  Otherwise, this is a category ID, so use HISTORY_POINT_INI and HISTORY_POINT_ITEM to determine the source INI and item. Join to the ALL_CATEGORIES table using the HISTORY_POINT_ID, HISTORY_POINT_INI, and HISTORY_POINT_ITEM columns to get the category title. |
| EPIC_RELEASED_HISTORY_POINT_ID | No | The LVN ID of the Epic-released LVN record mapped to the value in HISTORY_POINT_ID. For Epic-released LVN records, this will be the same as the value in HISTORY_POINT_ID. If this HISTORY_POINT_INI is not "LVN," this column will be NULL. |
| PANE_FOCUS_TYPE_C | No | The category ID for the type of pane focus from which the activity was used. This is usually the same as the internal ID. If you use Intraconnect, this is the Community ID (CID). |
| NUMBER_OF_MINUTES_ACTIVE | No |  |
| ACTIVITY_VISIT_COUNT | No | *** Deprecated *** The deprecated column's content/data is no longer available in Clarity because it is inaccurate.  The number of times the user visited the activity during the hour. |
| CLIENT_APP_TARGET_C | No | The client application from which the user visited the activity. |
| NUMBER_OF_SECONDS_ACTIVE | No | The number of seconds the user spent in the activity during the hour. |
| HISTORY_POINT_ITEM | No | The source category item for the history point, if it's a category ID. This column can be used with HISTORY_POINT_INI and HISTORY_POINT_ID to join to ALL_CATEGORIES and get the category title for the history point.  For example, if the history point is an InBasket message type, which is stored in I EOW 30, this column would be 30, HISTORY_POINT_INI would be 'EOW,' and HISTORY_POINT_ID would be the category ID of the message type. |
| NUMBER_OF_SECONDS_ACTIVE_Q1 | No | The number of seconds the user spent in the activity during the first quarter of the hour. |
| NUMBER_OF_SECONDS_ACTIVE_Q2 | No | The number of seconds the user spent in the activity during the second quarter of the hour. |
| NUMBER_OF_SECONDS_ACTIVE_Q3 | No | The number of seconds the user spent in the activity during the third quarter of the hour. |
| NUMBER_OF_SECONDS_ACTIVE_Q4 | No | The number of seconds the user spent in the activity during the fourth quarter of the hour. |
| CONNECTION_MODE_C | No | The app's connection mode and the network connectivity status of the application when the user accessed the activity. |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | USER_ID | CLARITY_EMP | USER_ID | Unknown | Yes | No |  |
| 2 | USER_ID | CLARITY_EMP_2 | USER_ID | Unknown | Yes | No |  |
| 2 | USER_ID | CLARITY_EMP_3 | USER_ID | Unknown | Yes | No |  |
| 2 | USER_ID | CLARITY_EMP_4 | USER_ID | No | Yes | No |  |
| 2 | USER_ID | CLARITY_EMP_DEMO | USER_ID | No | Yes | No |  |
| 2 | USER_ID | EMP_BASIC_INFO | USER_ID | No | Yes | No |  |
| 2 | USER_ID | EMP_DOC_SETTINGS | USER_NUMBER_ID | No | Yes | No |  |
| 2 | USER_ID | F_RX_USER | USER_ID | Unknown | Unknown | No |  |
| 2 | USER_ID | IB_MESSAGE_SETTINGS | USER_ID | No | Yes | No |  |
| 2 | USER_ID | LOGIN_INFO | USER_NUMBER_ID | No | Yes | No |  |
| 2 | USER_ID | QC_RESULTS_REVIEW | USER_NUMBER_ID | No | Yes | No |  |
| 2 | USER_ID | USER_SIDEBAR_RPT | USER_NUMBER_ID | Unknown | Yes | No |  |
| 2 | USER_ID | V_CUBE_D_USER | USER_ID | Unknown | Unknown | No |  |
| 2 | USER_ID | V_CUBE_RX_USER | USER_ID | Unknown | Unknown | No |  |
| 3 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | Yes | No |  |
| 3 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | Yes | No |  |
| 3 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | Yes | No |  |
| 4 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | Yes | No |  |
| 4 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | Yes | No |  |
| 4 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | Yes | No |  |
| 5 | WORKSTATION_ID | CLARITY_LWS | WORKSTATION_ID | No | Yes | No |  |
| 5 | WORKSTATION_ID | CLARITY_LWS_2 | WORKSTATION_ID | No | Yes | No |  |
| 5 | WORKSTATION_ID | CLARITY_LWS_3 | WORK_STATION_2_ID | No | Yes | No |  |
| 5 | WORKSTATION_ID | CLARITY_LWS_4 | WORKSTATION_ID | No | Yes | No |  |
| 5 | WORKSTATION_ID | WS_DEFINITION | WORKSTATION_ID | No | Yes | No |  |
| 10 | PAT_ENC_CSN_ID | ALT_ORD_PROV_SINGL | PAT_ENC_CSN_ID | Unknown | Yes | No |  |
| 10 | PAT_ENC_CSN_ID | AN_RELINK_INFO | PAT_ENC_CSN_ID | No | Yes | No |  |
| 10 | PAT_ENC_CSN_ID | DENT_ORTH_EXAM_NOTES | PAT_ENC_CSN_ID | No | Yes | No |  |
| 10 | PAT_ENC_CSN_ID | FAC_CHG_OVERRIDE | PAT_ENC_CSN_ID | No | Yes | No |  |
| 10 | PAT_ENC_CSN_ID | FAM_HX_PAT_ONLY | PAT_ENC_CSN_ID | No | Yes | No |  |

_(149 total; showing first 30)_
