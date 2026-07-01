# CACHED_USER_TYPE

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=CACHED_USER_TYPE

## Description

This table displays the cached user type data from a user's EMP record.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | EMP |
| Release Version | Rel August 2018 |
| May contain EHI? | No |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| USER_ID | VARCHAR (18) | The unique ID associated with the user record for this row. This column is frequently used to link to the CLARITY_EMP table. |
| LINE | INTEGER | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| CACHED_USER_TYPE_C | INTEGER |  |
| DEPARTMENT_ID | NUMERIC (18,0) | Stores the department corresponding to which a user's type is cached. |
| TEMPLATE_ID | VARCHAR (18) | Stores the template corresponding to which a user's type is cached. |
| CACHE_DATE | DATETIME | Stores the date (in UTC) when a user's type was last saved. |

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
| 5 | CACHED_USER_TYPE_C | ZC_USER_TYPES | USER_TYPES_C | No | No | No |  |
| 6 | DEPARTMENT_ID | BH_DEP | DEPARTMENT_ID | No | No | No |  |
| 6 | DEPARTMENT_ID | CLARITY_DEP | DEPARTMENT_ID | No | No | No |  |
| 6 | DEPARTMENT_ID | CLARITY_DEP_2 | DEPARTMENT_ID | No | No | No |  |
| 6 | DEPARTMENT_ID | CLARITY_DEP_3 | DEPARTMENT_ID | No | No | No |  |
| 6 | DEPARTMENT_ID | CLARITY_DEP_4 | DEPARTMENT_ID | No | No | No |  |
| 6 | DEPARTMENT_ID | CLARITY_DEP_5 | DEPARTMENT_ID | No | No | No |  |
| 6 | DEPARTMENT_ID | CLARITY_DEP_MYC | DEPARTMENT_ID | No | No | No |  |
| 6 | DEPARTMENT_ID | DEPT_QUEUE_MSG_SETTINGS | DEPARTMENT_ID | No | No | No |  |
| 6 | DEPARTMENT_ID | DEPT_VERIFIED_INFO | DEPARTMENT_ID | No | No | No |  |

_(53 total; showing first 30)_
