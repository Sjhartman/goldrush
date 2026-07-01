# V_CASE_SCHEDULE_CHANGE

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=V_CASE_SCHEDULE_CHANGE

## Description

The view is designed to simplify reporting on canceled and rescheduled cases. The view contains information about the times when a case is performed, canceled, rescheduled or when the case is marked as procedure not performed on the day of the procedure. The view will only include information of actions on the case that took place within X number of days before the procedure date. This value is set in the view on the Property Value tab. Leave the value blank to return actions that took place after the schedule finalize time. The view is defined with a primary key comprised of CASE_ID, CASE_DATE, and ACTION_DATE. This is principally used to drive Organization Filter functionality. In certain circumstances, this set of columns may not uniquely identify a single row, so it should not be used for that purpose.

## Metadata

| Property | Value |
| --- | --- |
| Type | View |
| Release Version | Rel 2014 |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| CASE_ID | VARCHAR (18) | The unique ID of the procedural case record. |
| LOG_ID | VARCHAR (18) | The unique ID of the procedural log record for this row. |
| ACTION_C | INTEGER |  |
| ACTION_NM | No | The name of the action category value which indicates the audit action performed on the case by the user.  The possible values are 'canceled', 'scheduled', 'moved', 'removed' and 'bumped'. Cases that were shuffled off of the schedule will show as 'removed'. |
| GENERAL_ACTION_NM | No | This column will display the most recent status associated with the case.  The values that this column displays are Canceled, Rescheduled, Scheduled, Procedure not Performed, and Performed. Canceled refers to the cases that were canceled. Rescheduled refers to the cases that have a rescheduling action, such as shuffle, removed or bumped. Procedure not Performed refers to the cases where the log was created but the procedure was not performed. Scheduled refers to the cases that are on the schedule and do not have the patient out of OR time documented.  This column will be used to calculate the number of cases that were canceled or rescheduled or cases marked as procedure was not performed after the log was created. |
| ACTION_DTTM | 5010 | The date and time on which the audit action took place. If the general action for the case is 'Procedure not Performed', the column will return the scheduled start time of the case. |
| AUDIT_USER_ID | VARCHAR (18) | The unique ID assigned to the user record who took the audit action on the case. This ID may be encrypted. If there are multiple rescheduling action on the case on the same action date then the user who last took the case off the schedule will be shown as the audit user. |
| AUDIT_USER_NM | VARCHAR (160) | The name of the user record. This name may be hidden. If there are multiple rescheduling action on the case on the same action date then the user who first took the case off the schedule will be shown as the audit user. |
| AUDIT_USER_NM_WID | .1 | A unique user identifier that consists of the name and the user ID of the user that performed the action on the case. |
| RESCHED_TO_DATE | DATETIME | The date to which the case is rescheduled. This column is only populated if the action is moved, removed or bumped. This column will be null for any other audit action or if the case is taken off the schedule and never rescheduled. |
| ADD_ON_CASE_SCH_YN | VARCHAR (1) |  |
| ACTION_AFTER_SCHED_FINALIZE_YN | No | This column stores whether the action took place after the schedule was finalized. Y indicates that the action took place after the schedule was finalized for the procedure date. N indicates that the action took place before the schedule was finalized for the procedure date.  This column will be used in conjuction with column ADD_ON_CASE_SCH_YN to differentiate the cases which were on the schedule to the ones which were added after the schedule finalized. |
| CANCELLATION_REASON_BUCKET | No | This column will group the cancel reason or procedure not performed reason under general buckets like 'Surgeon/Physician', 'Anesthesia', 'Patient', 'Facility', 'Scheduling', and 'Other'. The column is only populated for the cases where the general action (GENERAL_ACTION_NM) is 'Canceled', 'Rescheduled', or 'Procedure not Performed'.   If the general action (GENERAL_ACTION_NM) associated with the case is 'Canceled' or 'Rescheduled' then the column will show bucket to which the cancel reason belongs. If cancellation reason is not documented, null will be displayed. If the general action (GENERAL_ACTION_NM) associated with the case is 'Procedure not Performed' then the column will show bucket to which the procedure not performed reason belongs. If procedure not performed reason name is not documented, null will be displayed.  Note: Currently the column will not be populated, and is created as a placeholder for the future functionality. This will always be null. |
| CANCELLATION_REASON_NM | No | This column will display the name of the reason documented when the case was canceled, rescheduled, or marked as procedure not performed. The column is only populated for the cases where the general action (GENERAL_ACTION_NM) is 'Canceled', 'Rescheduled', or 'Procedure not Performed'.   If the general action (GENERAL_ACTION_NM) associated with the case is 'Canceled' or 'Rescheduled' then the column will show the cancellation reason name. If the cancellation reason is not documented, null will be displayed. If the general action (GENERAL_ACTION_NM) associated with the case is 'Procedure not Performed' then the column will show the procedure not performed reason name. If the procedure not performed reason name is not documented, null will be displayed. |
| CANCELLATION_COMMENTS | 5090 | This column displays the comments documented by the user when the case is canceled, rescheduled, or marked as procedure not performed. The column is only populated for the cases where the general action (GENERAL_ACTION_NM) is 'Canceled', 'Rescheduled', or 'Procedure not Performed'.   If the general action (GENERAL_ACTION_NM) associated with the case is 'Canceled' or 'Rescheduled' then the column will show canceled comment. If canceled comment is not documented, null will be displayed. If the general action (GENERAL_ACTION_NM) associated with the case is 'Procedure not Performed' then the column will show procedure not performed comment. If procedure not performed comment is not documented, null will be displayed. |
| CANCELLATION_RSN_AND_COMMENTS | No | This column displays the concatenation of reason and comments for cancel, reschedule, or procedure not performed action on a case. The column is only populated for the cases where the general action (GENERAL_ACTION_NM) is 'Canceled', 'Rescheduled', or 'Procedure not Performed'.   If the general action (GENERAL_ACTION_NM) associated with the case is 'Canceled' or 'Rescheduled', then the column will show the concatenation of canceled reason and canceled comment. If canceled comment and canceled reason are not documented, null will be displayed. If the general action (GENERAL_ACTION_NM) associated with the case is 'Procedure not Performed', then the column will show the value from PROC_NOT_PERFORM_PHASE_NM. |
| CANCEL_RESCHED_ACTION_RSN_C | INTEGER |  |
| CANCEL_RESCHED_ACTION_RSN_CMTS | VARCHAR (254) | The comment entered by the user when the case is canceled or rescheduled.This column is only populated where the general action is 'Canceled' or 'Rescheduled'. |
| PROC_NOT_PERFORM_PHASE_C | INTEGER |  |
| PROC_NOT_PERFORM_PHASE_NM | No | The name of the procedure not performed category ID for the phase in which the case was marked as procedure not performed.  This column generally stores the perioperative phase in which the case was marked as procedure not performed. The column is only populated for the case where the general action is 'Procedure not Performed'. |
| PROC_NOT_PERFORM_REASON_C | INTEGER |  |
| PROC_NOT_PERFORM_COMMENTS | VARCHAR (254) | The comment entered by the user when the case is marked as procedure not performed. The column is only populated for the case where the general action is 'Procedure not Performed'. |
| CASE_DTTM | 5030 | The date and time at which the procedure was scheduled. If the action is cancellation, bumped, removed or moved, this is the previous scheduled date and time for the case. |
| CASE_DAY_OF_WEEK | No | Represents the name of the day of the week (Monday, Tuesday, etc.) that the case was scheduled. |
| CASE_DAY_NUM_OF_WEEK | No | Contains a number representing the day of the week in the current locale for the corresponding CALENDAR_DT. The first day of the week is 0 and the last day of the week is 6.  For example, Sunday is the first day of the week in the United States. So Sunday would be 0 and Saturday would be 6 in this column. |
| CASE_MONTH_NUMBER | No | The month in integer form when the case was scheduled. For example, February will be "2". |
| CASE_MONTH_NAME | No | The month name in long form when the case was scheduled. For example, "February". |
| CASE_YEAR | No | This column contains the four-digit year when the case was scheduled. |
| CASE_YEAR_AND_MONTH | No | To help group by month, this column contains the month and year when the case was scheduled. The format is YYYYMM. |
| CASE_WEEK_OF_YEAR | No | The number of the week in the year when the case was scheduled. Depends on the locale definition. |
| CASE_WEEKEND_YN | No | Indicates whether the case was scheduled on a weekend day. Y indicates that the procedure was scheduled on a weekend day. N indicates that the procedure was not scheduled on a weekend. |
| CASE_HOLIDAY_YN | No | Indicates whether the case was scheduled on a holiday. Y indicates that the procedure was scheduled on a holiday. N indicates that the procedure was not scheduled on a holiday. |
| AUDIT_HRS_BEF_PROC | INTEGER | This column stores the number of hours between the action time and the scheduled start time. A positive value indicates that the action was before the scheduled start time of the case, a negative value indicates the action took place after the scheduled start time of the case.  This column can help to answer how many hours before the scheduled start time, on average, cases are being rescheduled/canceled, or how many cases are being canceled within X hours of the scheduled start time. |
| AUDIT_DAYS_BEF_PROC | INTEGER | This column will store the difference in days between action date and procedure date for a case. A positive value tells the action was taken before the procedure date, a negative value tells the action took place after the procedure date.  This column can be used to report on how many days before the procedure date the case got canceled /rescheduled. |
| CASE_LENGTH | INTEGER | The total amount of time required to perform the case. The total time includes the set up and the clean up time. |
| PRIMARY_PROCEDURE_ID | VARCHAR (254) | The ID of the primary procedure for this case/log. The primary procedure is first pulled from the log if there exists a log for the given case. If not, the information is pulled from the case. |
| PRIMARY_PROCEDURE_NM | VARCHAR (200) | The name of the primary procedure for this case/log.The primary procedure is first pulled from the log if there exists a log for the given case. If not, the information is pulled from the case. |
| PRIMARY_PROCEDURE_NM_WID | ORP | A unique procedure identifier that consists of the name and the procedure ID of the first procedure for this case/log. The primary procedure is first pulled from the log if there exists a log for the given case. If not, the information is pulled from the case.  This column is often used for grouping, sorting and display purposes in reports. In order to determine the procedure ID to display it searches in the following order: the procedure code from a linked EAP record if the procedure is using EAP, the primary external ID, procedure internal ID. |
| PRIMARY_PHYSICIAN_ID | 1600 | The name of the primary physician on the first panel for this case/log. The primary physician is first pulled from the log if there exists a log for the given case. If not, the information is pulled from the case. |
| PRIMARY_PHYSICIAN_NM | VARCHAR (200) | The name of the primary physician on the first panel for this case/log. The primary physician is first pulled from the log if there exists a log for the given case. If not, the information is pulled from the case. |
| PRIMARY_PHYSICIAN_NM_WID | No | A unique physician identifier that consists of the name, credentials and the physician ID of the primary physician on the first panel for this case/log. The primary physician is first pulled from the log if there exists a log for the given case. If not, the information is pulled from the case. This column is often used for grouping, sorting and display purposes in reports. |
| PRIMARY_PHYSICIAN_CRED | No | The current credentials for the primary physician. The primary physician is first pulled from the log if there exists a log for the given case. If not, the information is pulled from the case. |
| SERVICE_C | VARCHAR (66) |  |
| SERVICE_NM | No | The name of the service for this case/log. The service information is first pulled from the log if there exists a log for the given case. If not, the information is pulled from the case. |
| PATIENT_CLASS_C | VARCHAR (66) |  |
| PATIENT_CLASS_NM | No | The name of the patient class for this case/log. The patient class is first pulled from the log is there exists a log for the given case. If not, the information is pulled from the case. |
| PATIENT_CLASS_GROUP | No | This column groups the given patient class under Inpatient or Outpatient based on the patient class category value and the grouping specified in the property (P_PATIENT_CLASS_INPATIENT) on the view V_CASE_SCHEDULE_CHANGE. |
| LOCATION_ID | 501 | The unique ID of the location where the procedure is scheduled to be performed. This column is frequently used to link to CLARITY_LOC. |
| LOCATION_NM | VARCHAR (200) | The name of the location where the procedure for this case is scheduled. |
| LOCATION_NM_WID | 501 .2 5110 | A unique location identifier that consists of the name and the location ID where the procedure for this case is scheduled to be performed. This column is often used for grouping, sorting and display purposes in reports. |
| CASE_DATE | DATETIME | The date on which the procedure was scheduled. If the action is cancellation, bumped, removed or moved, this is the previous scheduled date for the case.  This column can be used to filter the cases based on date range or determine if the case was scheduled for the given surgery date. |
| ACTION_DATE | DATETIME | The date on which the audit action took place. If the general action for the case is 'Procedure not Performed', the column will return the case date. |
| INCLUDE_ORG_CANCEL_REPORT_YN | VARCHAR (1) |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | CASE_ID | OR_CASE | OR_CASE_ID | Unknown | Unknown | No |  |
| 1 | CASE_ID | OR_CASE_2 | CASE_ID | Unknown | Unknown | No |  |
| 1 | CASE_ID | OR_CASE_3 | CASE_ID | Unknown | Unknown | No |  |
| 1 | CASE_ID | OR_CASE_4 | OR_CASE_ID | No | Unknown | No |  |
| 1 | CASE_ID | OR_CASE_VIRTUAL | OR_CASE_ID | No | Unknown | No |  |
| 1 | CASE_ID | V_OR_CASE_ORR | CASE_ID | Unknown | Unknown | No |  |
| 2 | LOG_ID | F_LOG_BASED | LOG_ID | Unknown | Unknown | No |  |
| 2 | LOG_ID | OR_LOG | LOG_ID | Unknown | Unknown | No |  |
| 2 | LOG_ID | OR_LOG_2 | LOG_ID | Unknown | Unknown | No |  |
| 2 | LOG_ID | OR_LOG_3 | LOG_ID | No | Unknown | No |  |
| 2 | LOG_ID | OR_LOG_METRIC_DETAILS | LOG_ID | No | Unknown | No |  |
| 2 | LOG_ID | OR_LOG_PRECEDING | LOG_ID | No | Unknown | No |  |
| 2 | LOG_ID | OR_LOG_VIRTUAL | LOG_ID | No | Unknown | No |  |
| 2 | LOG_ID | UK_CRM_PACEMKR_PROC | LOG_ID | No | Unknown | No |  |
| 2 | LOG_ID | V_CASE_CHARGES | LOG_ID | Unknown | Unknown | No |  |
| 2 | LOG_ID | V_CASE_COSTS | LOG_ID | Unknown | Unknown | No |  |
| 2 | LOG_ID | V_CASE_ON_TIME_START | LOG_ID | Unknown | Unknown | No |  |
| 2 | LOG_ID | V_CASE_PHYS_TURNOVER | LOG_ID | Unknown | Unknown | No |  |
| 2 | LOG_ID | V_CASE_ROOM_TURNOVER | LOG_ID | Unknown | Unknown | No |  |
| 2 | LOG_ID | V_CASE_VOLUME | LOG_ID | Unknown | Unknown | No |  |
| 2 | LOG_ID | V_DECISION_TO_INCISION | LOG_ID | Unknown | Unknown | No |  |
| 2 | LOG_ID | V_LOG_BASED | LOG_ID | Unknown | Unknown | No |  |
| 2 | LOG_ID | V_LOG_TIMING_EVENTS | LOG_ID | Unknown | Unknown | No |  |
| 3 | ACTION_C | ZC_OR_AUDIT_ACTION | AUDIT_ACTION_C | No | Unknown | No |  |
| 7 | AUDIT_USER_ID | CLARITY_EMP | USER_ID | Unknown | Unknown | No |  |
| 7 | AUDIT_USER_ID | CLARITY_EMP_2 | USER_ID | Unknown | Unknown | No |  |
| 7 | AUDIT_USER_ID | CLARITY_EMP_3 | USER_ID | Unknown | Unknown | No |  |
| 7 | AUDIT_USER_ID | CLARITY_EMP_4 | USER_ID | No | Unknown | No |  |
| 7 | AUDIT_USER_ID | CLARITY_EMP_DEMO | USER_ID | No | Unknown | No |  |
| 7 | AUDIT_USER_ID | EMP_BASIC_INFO | USER_ID | No | Unknown | No |  |

_(121 total; showing first 30)_
