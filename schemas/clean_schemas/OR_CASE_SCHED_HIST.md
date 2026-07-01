# OR_CASE_SCHED_HIST

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=OR_CASE_SCHED_HIST

## Description

The OR_CASE_SCHED_HIST table contains OR management system case scheduling history.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | ORC |
| Release Version | MU1 - MAY 2001 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| OR_CASE_ID | VARCHAR (18) | The unique ID of the case record. |
| LINE | No | The number of the line of the OR scheduling history information. |
| ROOM_ID | VARCHAR (18) | The unique ID of the operating room in which the case was scheduled. |
| HIST_DATE | 605 | The date on which the case was scheduled. |
| CM_PHY_OWNER_ID | VARCHAR (25) | ID of the physical deployment owner for this record.  Physical owners will be where the data is hosted, either on the cross-over server or the owner deployment. |
| CM_LOG_OWNER_ID | VARCHAR (25) | ID of the logical deployment owner for this record.  Logical owners show the deployment where the record was created but doesn't represent if the record is a part of version skew. |
| HIST_SCHED_USER_ID | VARCHAR (18) | The ID of the user that scheduled the case. |
| HIST_SCHED_DATE | DATETIME | The date on which the user scheduled the case. |
| HIST_SCHED_TIME | DATETIME (Local) | The time at which the user scheduled the case. |
| MATCH_UNBLOCKED_YN | VARCHAR (1) |  |
| MATCH_SURG_BLOCK_ID | VARCHAR (18) | Stores the matching surgeon block ID of the schedule instance if the match type is a surgeon block. |
| MATCH_SRVC_BLOCK_C | VARCHAR (66) |  |
| MATCH_SG_BLOCK_ID | VARCHAR (18) | Stores the matching surgeon group block ID of the schedule instance if the match type is a surgeon group block. |
| HIST_SCHED_DTTM | 610 | The date and time at which the user scheduled the case. |
| SCHEDULING_SOURCE_C | INTEGER |  |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| BITMAP INDEX | EIX_OR_CASE_SCHED_GROUP | MATCH_SG_BLOCK_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_OR_CASE_SCHED_HIST_ROID | ROOM_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_OR_CASE_SCHED_SCHED_DATE | HIST_SCHED_DATE | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_OR_CASE_SCHED_SCHED_USER | HIST_SCHED_USER_ID | 1 | Yes | Yes |  |
| BITMAP INDEX | EIX_OR_CASE_SCHED_SERVICE | MATCH_SRVC_BLOCK_C | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_OR_CASE_SCHED_SURGEON | MATCH_SURG_BLOCK_ID | 1 | Yes | Yes |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | OR_CASE_ID | OR_CASE | OR_CASE_ID | Unknown | No | No |  |
| 1 | OR_CASE_ID | OR_CASE_2 | CASE_ID | Unknown | No | No |  |
| 1 | OR_CASE_ID | OR_CASE_3 | CASE_ID | Unknown | No | No |  |
| 1 | OR_CASE_ID | OR_CASE_4 | OR_CASE_ID | No | No | No |  |
| 1 | OR_CASE_ID | OR_CASE_VIRTUAL | OR_CASE_ID | No | No | No |  |
| 1 | OR_CASE_ID | V_OR_CASE_ORR | CASE_ID | Unknown | Unknown | No |  |
| 3 | ROOM_ID | CLARITY_SER | PROV_ID | Unknown | No | No |  |
| 3 | ROOM_ID | CLARITY_SER_2 | PROV_ID | Unknown | No | No |  |
| 3 | ROOM_ID | CLARITY_SER_3 | PROV_ID | Unknown | No | No |  |
| 3 | ROOM_ID | CLARITY_SER_4 | PROV_ID | No | No | No |  |
| 3 | ROOM_ID | CLARITY_SER_MYC | PROV_ID | Unknown | No | No |  |
| 3 | ROOM_ID | D_PROV_PRIMARY_HIERARCHY | PROV_ID | Unknown | Unknown | No |  |
| 3 | ROOM_ID | ED_SER_SETTINGS | PROV_ID | Unknown | No | No |  |
| 3 | ROOM_ID | EXT_CAL_PROV_CONFIG | PROV_ID | No | No | No |  |
| 3 | ROOM_ID | OR_SER_EQUIPMENT | PROV_ID | Unknown | No | No |  |
| 3 | ROOM_ID | OR_SER_ROOM | PROV_ID | Unknown | No | No |  |
| 3 | ROOM_ID | PROV_BATCH_LTR_GEN | PROV_ID | Unknown | No | No |  |
| 3 | ROOM_ID | PROV_GROUP | PROV_ID | No | No | No |  |
| 3 | ROOM_ID | V_CUBE_D_PROVIDER | PROVIDER_ID | Unknown | Unknown | No |  |
| 5 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 5 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 5 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 6 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 6 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 6 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 7 | HIST_SCHED_USER_ID | CLARITY_EMP | USER_ID | Unknown | No | No |  |
| 7 | HIST_SCHED_USER_ID | CLARITY_EMP_2 | USER_ID | Unknown | No | No |  |
| 7 | HIST_SCHED_USER_ID | CLARITY_EMP_3 | USER_ID | Unknown | No | No |  |
| 7 | HIST_SCHED_USER_ID | CLARITY_EMP_4 | USER_ID | No | No | No |  |
| 7 | HIST_SCHED_USER_ID | CLARITY_EMP_DEMO | USER_ID | No | No | No |  |

_(56 total; showing first 30)_
