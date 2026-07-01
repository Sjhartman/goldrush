# TC_REQUEST_STATUS_HX

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=TC_REQUEST_STATUS_HX

## Description

This table stores information related to the status change history for Transfer Center requests.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | NCS |
| Release Version | Rel 2018 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| COMM_ID | NUMERIC (18,0) | The unique identifier for the communication record. |
| LINE | INTEGER | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| REQUEST_STATUS_C | INTEGER |  |
| STATUS_UPDATE_UTC_DTTM | DATETIME (UTC) | The datetime at which the request's status changed, stored in UTC. For local time, use TC_REQUEST_STATUS_HX.STATUS_UPDATE_LOCAL_DTTM. |
| STATUS_UPDATE_USER_ID | VARCHAR (18) | This item stores the user who changed the status of the request. |
| DEST_DECLINE_RSN_C | INTEGER |  |
| CANCEL_STATUS_RSN_C | INTEGER |  |
| STATUS_UPDATE_LOCAL_DTTM | DATETIME (Local) | The datetime at which the request's status changed, stored in local time. For UTC, use TC_REQUEST_STATUS_HX.STATUS_UPDATE_UTC_DTTM. |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | COMM_ID | CUST_SERVICE | COMM_ID | Unknown | No | No |  |
| 1 | COMM_ID | CUST_SERVICE_2 | COMM_ID | No | No | No |  |
| 1 | COMM_ID | CUST_SERVICE_TRANSFER | COMM_ID | No | No | No |  |
| 1 | COMM_ID | CUST_SERV_ORG_FILTER_SA | COMM_ID | No | No | No |  |
| 1 | COMM_ID | V_ADT_TC_DEST | COMM_ID | Unknown | Unknown | No |  |
| 1 | COMM_ID | V_ADT_TRANSFER_CENTER | COMM_ID | Unknown | Unknown | No |  |
| 3 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 4 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 4 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 4 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 5 | REQUEST_STATUS_C | ZC_TC_REQUEST_STATUS | TC_REQUEST_STATUS_C | No | No | No |  |
| 7 | STATUS_UPDATE_USER_ID | CLARITY_EMP | USER_ID | Unknown | No | No |  |
| 7 | STATUS_UPDATE_USER_ID | CLARITY_EMP_2 | USER_ID | Unknown | No | No |  |
| 7 | STATUS_UPDATE_USER_ID | CLARITY_EMP_3 | USER_ID | Unknown | No | No |  |
| 7 | STATUS_UPDATE_USER_ID | CLARITY_EMP_4 | USER_ID | No | No | No |  |
| 7 | STATUS_UPDATE_USER_ID | CLARITY_EMP_DEMO | USER_ID | No | No | No |  |
| 7 | STATUS_UPDATE_USER_ID | EMP_BASIC_INFO | USER_ID | No | No | No |  |
| 7 | STATUS_UPDATE_USER_ID | EMP_DOC_SETTINGS | USER_NUMBER_ID | No | No | No |  |
| 7 | STATUS_UPDATE_USER_ID | F_RX_USER | USER_ID | Unknown | Unknown | No |  |
| 7 | STATUS_UPDATE_USER_ID | IB_MESSAGE_SETTINGS | USER_ID | No | No | No |  |
| 7 | STATUS_UPDATE_USER_ID | LOGIN_INFO | USER_NUMBER_ID | No | No | No |  |
| 7 | STATUS_UPDATE_USER_ID | QC_RESULTS_REVIEW | USER_NUMBER_ID | No | No | No |  |
| 7 | STATUS_UPDATE_USER_ID | USER_SIDEBAR_RPT | USER_NUMBER_ID | Unknown | No | No |  |
| 7 | STATUS_UPDATE_USER_ID | V_CUBE_D_USER | USER_ID | Unknown | Unknown | No |  |
| 7 | STATUS_UPDATE_USER_ID | V_CUBE_RX_USER | USER_ID | Unknown | Unknown | No |  |
| 8 | DEST_DECLINE_RSN_C | ZC_TC_DECLINE_RSN | TC_DECLINE_RSN_C | No | No | No |  |
| 9 | CANCEL_STATUS_RSN_C | ZC_TC_CANCEL_RSN | TC_CANCEL_RSN_C | No | No | No |  |
