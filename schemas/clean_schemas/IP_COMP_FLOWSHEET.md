# IP_COMP_FLOWSHEET

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=IP_COMP_FLOWSHEET

## Description

This table displays completed flowsheet row information for Inpatient (INP) records.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | INP |
| Release Version | Summer 2009 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| INPATIENT_DATA_ID | VARCHAR (18) | The unique identifier for the inpatient record. |
| LINE | No | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| COMPLETE_FLOW_ROWS | VARCHAR (254) | The flowsheet ID of completed rows is stored here. If the row is of duplicable type, it stores the flowsheet ID and line number. |
| ROW_STATUS_C | INTEGER |  |
| UPDATE_INSTANT_TM | DATETIME (Local) | The instant the row was updated. |
| UPDATE_USER_ID | VARCHAR (18) | Stores the unpadded User ID of the user that updated the row status. |
| UPDATE_REASON_C | VARCHAR (66) |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | INPATIENT_DATA_ID | IP_DATA_STORE | INPATIENT_DATA_ID | No | No | No |  |
| 3 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 4 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 4 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 4 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 6 | ROW_STATUS_C | ZC_ROW_STATUS | ROW_STATUS_C | No | No | No |  |
| 8 | UPDATE_USER_ID | CLARITY_EMP | USER_ID | Unknown | No | No |  |
| 8 | UPDATE_USER_ID | CLARITY_EMP_2 | USER_ID | Unknown | No | No |  |
| 8 | UPDATE_USER_ID | CLARITY_EMP_3 | USER_ID | Unknown | No | No |  |
| 8 | UPDATE_USER_ID | CLARITY_EMP_4 | USER_ID | No | No | No |  |
| 8 | UPDATE_USER_ID | CLARITY_EMP_DEMO | USER_ID | No | No | No |  |
| 8 | UPDATE_USER_ID | EMP_BASIC_INFO | USER_ID | No | No | No |  |
| 8 | UPDATE_USER_ID | EMP_DOC_SETTINGS | USER_NUMBER_ID | No | No | No |  |
| 8 | UPDATE_USER_ID | F_RX_USER | USER_ID | Unknown | Unknown | No |  |
| 8 | UPDATE_USER_ID | IB_MESSAGE_SETTINGS | USER_ID | No | No | No |  |
| 8 | UPDATE_USER_ID | LOGIN_INFO | USER_NUMBER_ID | No | No | No |  |
| 8 | UPDATE_USER_ID | QC_RESULTS_REVIEW | USER_NUMBER_ID | No | No | No |  |
| 8 | UPDATE_USER_ID | USER_SIDEBAR_RPT | USER_NUMBER_ID | Unknown | No | No |  |
| 8 | UPDATE_USER_ID | V_CUBE_D_USER | USER_ID | Unknown | Unknown | No |  |
| 8 | UPDATE_USER_ID | V_CUBE_RX_USER | USER_ID | Unknown | Unknown | No |  |
| 9 | UPDATE_REASON_C | ZC_UPDATE_REASON | UPDATE_REASON_C | No | No | No |  |
