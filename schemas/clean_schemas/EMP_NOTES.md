# EMP_NOTES

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=EMP_NOTES

## Description

This table extracts the free text notes recorded about the user.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | EMP |
| Release Version | SPRING 2008 |
| May contain EHI? | No |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| USER_ID | VARCHAR (18) | The unique ID associated with the user record for this row. This column is frequently used to link to the CLARITY_EMP table. |
| LINE | No | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record was extracted. This is only populated if you use IntraConnect. |
| NOTES | VARCHAR (508) | The free text notes regarding this user. |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | USER_ID | CLARITY_EMP | USER_ID | Unknown | No | No |  |
| 1 | USER_ID | CLARITY_EMP_2 | USER_ID | Unknown | No | No |  |
| 1 | USER_ID | CLARITY_EMP_3 | USER_ID | Unknown | No | No |  |
| 1 | USER_ID | CLARITY_EMP_4 | USER_ID | No | No | No |  |
| 1 | USER_ID | CLARITY_EMP_DEMO | USER_ID | No | No | No |  |
| 1 | USER_ID | EMP_BASIC_INFO | USER_ID | No | No | No |  |
| 1 | USER_ID | EMP_DOC_SETTINGS | USER_NUMBER_ID | No | No | No |  |
| 1 | USER_ID | F_RX_USER | USER_ID | Unknown | Unknown | No |  |
| 1 | USER_ID | IB_MESSAGE_SETTINGS | USER_ID | No | No | No |  |
| 1 | USER_ID | LOGIN_INFO | USER_NUMBER_ID | No | No | No |  |
| 1 | USER_ID | QC_RESULTS_REVIEW | USER_NUMBER_ID | No | No | No |  |
| 1 | USER_ID | USER_SIDEBAR_RPT | USER_NUMBER_ID | Unknown | No | No |  |
| 1 | USER_ID | V_CUBE_D_USER | USER_ID | Unknown | Unknown | No |  |
| 1 | USER_ID | V_CUBE_RX_USER | USER_ID | Unknown | Unknown | No |  |
| 3 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 4 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 4 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 4 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
