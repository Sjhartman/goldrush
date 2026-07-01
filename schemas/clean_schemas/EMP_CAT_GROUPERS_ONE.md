# EMP_CAT_GROUPERS_ONE

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=EMP_CAT_GROUPERS_ONE

## Description

This table contains information about the first category report grouper in user records.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | EMP |
| Release Version | Rel 2015 |
| May contain EHI? | No |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| USER_NUMBER_ID | VARCHAR (18) | The unique ID associated with the user record for this row. This column is frequently used to link to the CLARITY_EMP table. |
| LINE | INTEGER | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| CAT_RPT_GRP_ONE_C | VARCHAR (66) |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | USER_NUMBER_ID | CLARITY_EMP | USER_ID | Unknown | No | No |  |
| 1 | USER_NUMBER_ID | CLARITY_EMP_2 | USER_ID | Unknown | No | No |  |
| 1 | USER_NUMBER_ID | CLARITY_EMP_3 | USER_ID | Unknown | No | No |  |
| 1 | USER_NUMBER_ID | CLARITY_EMP_4 | USER_ID | No | No | No |  |
| 1 | USER_NUMBER_ID | CLARITY_EMP_DEMO | USER_ID | No | No | No |  |
| 1 | USER_NUMBER_ID | EMP_BASIC_INFO | USER_ID | No | No | No |  |
| 1 | USER_NUMBER_ID | EMP_DOC_SETTINGS | USER_NUMBER_ID | No | No | No |  |
| 1 | USER_NUMBER_ID | F_RX_USER | USER_ID | Unknown | Unknown | No |  |
| 1 | USER_NUMBER_ID | IB_MESSAGE_SETTINGS | USER_ID | No | No | No |  |
| 1 | USER_NUMBER_ID | LOGIN_INFO | USER_NUMBER_ID | No | No | No |  |
| 1 | USER_NUMBER_ID | QC_RESULTS_REVIEW | USER_NUMBER_ID | No | No | No |  |
| 1 | USER_NUMBER_ID | USER_SIDEBAR_RPT | USER_NUMBER_ID | Unknown | No | No |  |
| 1 | USER_NUMBER_ID | V_CUBE_D_USER | USER_ID | Unknown | Unknown | No |  |
| 1 | USER_NUMBER_ID | V_CUBE_RX_USER | USER_ID | Unknown | Unknown | No |  |
| 3 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 4 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 4 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 4 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 5 | CAT_RPT_GRP_ONE_C | ZC_EMP_CAT_RPT_GRP_ONE | EMP_CAT_RPT_GRP_ONE_C | No | No | No |  |
