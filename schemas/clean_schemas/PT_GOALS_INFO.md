# PT_GOALS_INFO

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=PT_GOALS_INFO

## Description

This table contains data in the Discrete Goals (IGO) master file that is no-add data.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | IGO |
| Release Version | Summer 2009 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| GOAL_ID | VARCHAR (18) | The unique identifier for the goal record. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| USER_ID | VARCHAR (18) | The user ID of the person who entered this goal. |
| GOAL_TEMPLATE_ID | NUMERIC (18,0) | Stores the goal template used to create this record |
| GOAL_TEMPLATE_DAT | NUMERIC (18,2) | Stores the Goal Template Contact |
| PAT_ID | VARCHAR (18) | The unique ID of the patient who is associated with this goal. |
| CREATE_INST_DTTM | DATETIME (Local) | The instant this goal was created. |
| GOAL_USAGE_C | INTEGER |  |
| REC_VAL_COMPLIAN_YN | VARCHAR (1) |  |
| MOST_RECENT_VALUE | VARCHAR (100) | Contains the most recent compliance value for the goal |
| RECENT_VALUE_I_DTTM | DATETIME (Local) | The instant that the most recent compliance value was recorded |
| REC_VALUE_CHEC_DTTM | DATETIME (Local) | The instant that this goal was checked to determine its most recent compliance value |
| AMB_GOAL_TYPE_C | INTEGER |  |
| REC_ARCHIVED_YN | No | Indicates whether the Goal record is archived at the record level. |
| MYC_CREATE_USER_ID | VARCHAR (18) | Stores the ID of patient account record of the MyChart (Epic Patient Portal) user who created the goal. |
| GOAL_STATUS_C | INTEGER |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | GOAL_ID | GOAL | GOAL_ID | Unknown | No | No |  |
| 2 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 2 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 2 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 3 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 4 | USER_ID | CLARITY_EMP | USER_ID | Unknown | No | No |  |
| 4 | USER_ID | CLARITY_EMP_2 | USER_ID | Unknown | No | No |  |
| 4 | USER_ID | CLARITY_EMP_3 | USER_ID | Unknown | No | No |  |
| 4 | USER_ID | CLARITY_EMP_4 | USER_ID | No | No | No |  |
| 4 | USER_ID | CLARITY_EMP_DEMO | USER_ID | No | No | No |  |
| 4 | USER_ID | EMP_BASIC_INFO | USER_ID | No | No | No |  |
| 4 | USER_ID | EMP_DOC_SETTINGS | USER_NUMBER_ID | No | No | No |  |
| 4 | USER_ID | F_RX_USER | USER_ID | Unknown | Unknown | No |  |
| 4 | USER_ID | IB_MESSAGE_SETTINGS | USER_ID | No | No | No |  |
| 4 | USER_ID | LOGIN_INFO | USER_NUMBER_ID | No | No | No |  |
| 4 | USER_ID | QC_RESULTS_REVIEW | USER_NUMBER_ID | No | No | No |  |
| 4 | USER_ID | USER_SIDEBAR_RPT | USER_NUMBER_ID | Unknown | No | No |  |
| 4 | USER_ID | V_CUBE_D_USER | USER_ID | Unknown | Unknown | No |  |
| 4 | USER_ID | V_CUBE_RX_USER | USER_ID | Unknown | Unknown | No |  |
| 5 | GOAL_TEMPLATE_ID | GOAL_TEMPLATES | GOAL_TEMPLATE_ID | No | No | No |  |
| 7 | PAT_ID | ANTICOAG_SELF_REGULATING | PAT_ID | No | No | No |  |
| 7 | PAT_ID | CARE_COORDINATION | PAT_ID | Unknown | No | No |  |
| 7 | PAT_ID | CLAIMS_DERIVE_PAT_FLAGS | PAT_ID | No | No | No |  |
| 7 | PAT_ID | COMMUNITY_RESRC_REVIEWED | PAT_ID | No | No | No |  |
| 7 | PAT_ID | D_PAT_GEOGRAPHIC_CLASS | PAT_ID | Unknown | Unknown | No |  |
| 7 | PAT_ID | EPT_MEM_INFO | PAT_ID | No | No | No |  |
| 7 | PAT_ID | EXT_DATA_LAST_DONE | PAT_ID | No | No | No |  |
| 7 | PAT_ID | F_IBD_ADULT_FORM_PAT | PAT_ID | Unknown | Unknown | No |  |

_(62 total; showing first 30)_
