# OR_CASE_AUDIT_TRL

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=OR_CASE_AUDIT_TRL

## Description

The OR_CASE_AUDIT_TRL table contains OR management system case audit trail information.

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
| LINE | No | The number of the line of the audit information for the case. |
| AUDIT_ACTION_C | INTEGER |  |
| AUDIT_USER_ID | VARCHAR (18) | The unique ID of the user who performed the action on the case. |
| AUDIT_DATE | 5010 | The date on which the audit action took place. |
| AUDIT_REQUEST_BY | VARCHAR (254) | The name of the person who requested that the audit action performed. |
| AUDIT_COMMENTS | VARCHAR (600) | The comments related to the audit action performed. |
| CM_PHY_OWNER_ID | VARCHAR (25) | ID of the physical deployment owner for this record.  Physical owners will be where the data is hosted, either on the cross-over server or the owner deployment. |
| CM_LOG_OWNER_ID | VARCHAR (25) | ID of the logical deployment owner for this record.  Logical owners show the deployment where the record was created but doesn't represent if the record is a part of version skew. |
| AUDIT_SCHED_TO_DAT | DATETIME | Stores the date to which the case was scheduled for scheduling actions. |
| AUDIT_SCHED_TO_TIM | DATETIME (Local) | Stores the time at which the case was scheduled for scheduling actions. |
| AUDIT_SCHED_TO_OR | VARCHAR (18) | Stores the OR in which the case was scheduled for scheduling actions. |
| AUDIT_UNSCHED_DATE | DATETIME | Stores the date from which the case was unscheduled for unschedule actions. |
| AUDIT_UNSCHED_TIME | DATETIME (Local) | Stores the time from which the case was unscheduled for unschedule actions. |
| AUDIT_UNSCHED_OR | VARCHAR (18) | Stores the OR from which the case was unscheduled for unschedule actions. |
| AUDIT_SCHED_FINALIZE_DTTM | DATETIME (Attached) | Stores the schedule finalized date and time based on a given procedure date for a case. The logic looks to Location or System Definitions for schedule finalized definition to calculate the schedule finalized time for a given case. |
| AUDIT_HRS_BEF_PROC | INTEGER | This column stores the number of hours between the action time and the scheduled start time. This column is populated when the action is scheduled, rescheduled, or canceled. Otherwise this column is null. |
| AUDIT_DAYS_BEF_PROC | INTEGER | This column stores the difference in days between audit date and procedure date for a case. This column is populated when the action is scheduled, rescheduled, or canceled. Otherwise this column is null. |
| AUDIT_RESCHED_TO_DT | DATETIME | This column stores the next scheduled date for the case if the rescheduling action took place. The rescheduling action includes the actions of moved, removed, and bumped. |
| AUDIT_ADD_ON_SCH_YN | VARCHAR (1) |  |
| AUDIT_CANCEL_RSN_C | INTEGER |  |
| AUDIT_CANCEL_CMT *(deprecated)* | VARCHAR (254) |  |
| AUDIT_LOC_ID | NUMERIC (18,0) | This column stores the location from which a case is canceled or rescheduled. |
| AUDIT_INCLUDE_ORG_CANC_RPT_YN | VARCHAR (1) |  |
| AUDIT_CANC_COMMENTS | VARCHAR (254) | This item stores the comments entered each time a case was canceled or rescheduled. |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| B-TREE INDEX | EIX_OR_CASE_AUDIT_TRL_AUACC | AUDIT_ACTION_C | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_OR_CASE_AUDIT_TRL_AUUSID | AUDIT_USER_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_OR_CASE_AUDIT_TRL_SCH_DATE | AUDIT_SCHED_TO_DAT | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_OR_CASE_AUDIT_TRL_SCH_OR | AUDIT_SCHED_TO_OR | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_OR_CASE_AUDIT_TRL_UNSC_DTE | AUDIT_UNSCHED_DATE | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_OR_CASE_AUDIT_TRL_UNSC_OR | AUDIT_UNSCHED_OR | 1 | Yes | Yes |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | OR_CASE_ID | OR_CASE | OR_CASE_ID | Unknown | No | No |  |
| 1 | OR_CASE_ID | OR_CASE_2 | CASE_ID | Unknown | No | No |  |
| 1 | OR_CASE_ID | OR_CASE_3 | CASE_ID | Unknown | No | No |  |
| 1 | OR_CASE_ID | OR_CASE_4 | OR_CASE_ID | No | No | No |  |
| 1 | OR_CASE_ID | OR_CASE_VIRTUAL | OR_CASE_ID | No | No | No |  |
| 1 | OR_CASE_ID | V_OR_CASE_ORR | CASE_ID | Unknown | Unknown | No |  |
| 3 | AUDIT_ACTION_C | ZC_OR_AUDIT_ACTION | AUDIT_ACTION_C | No | No | No |  |
| 4 | AUDIT_USER_ID | CLARITY_EMP | USER_ID | Unknown | No | No |  |
| 4 | AUDIT_USER_ID | CLARITY_EMP_2 | USER_ID | Unknown | No | No |  |
| 4 | AUDIT_USER_ID | CLARITY_EMP_3 | USER_ID | Unknown | No | No |  |
| 4 | AUDIT_USER_ID | CLARITY_EMP_4 | USER_ID | No | No | No |  |
| 4 | AUDIT_USER_ID | CLARITY_EMP_DEMO | USER_ID | No | No | No |  |
| 4 | AUDIT_USER_ID | EMP_BASIC_INFO | USER_ID | No | No | No |  |
| 4 | AUDIT_USER_ID | EMP_DOC_SETTINGS | USER_NUMBER_ID | No | No | No |  |
| 4 | AUDIT_USER_ID | F_RX_USER | USER_ID | Unknown | Unknown | No |  |
| 4 | AUDIT_USER_ID | IB_MESSAGE_SETTINGS | USER_ID | No | No | No |  |
| 4 | AUDIT_USER_ID | LOGIN_INFO | USER_NUMBER_ID | No | No | No |  |
| 4 | AUDIT_USER_ID | QC_RESULTS_REVIEW | USER_NUMBER_ID | No | No | No |  |
| 4 | AUDIT_USER_ID | USER_SIDEBAR_RPT | USER_NUMBER_ID | Unknown | No | No |  |
| 4 | AUDIT_USER_ID | V_CUBE_D_USER | USER_ID | Unknown | Unknown | No |  |
| 4 | AUDIT_USER_ID | V_CUBE_RX_USER | USER_ID | Unknown | Unknown | No |  |
| 8 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 8 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 8 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 9 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 9 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 9 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 12 | AUDIT_SCHED_TO_OR | CLARITY_SER | PROV_ID | Unknown | No | No |  |
| 12 | AUDIT_SCHED_TO_OR | CLARITY_SER_2 | PROV_ID | Unknown | No | No |  |
| 12 | AUDIT_SCHED_TO_OR | CLARITY_SER_3 | PROV_ID | Unknown | No | No |  |

_(84 total; showing first 30)_
