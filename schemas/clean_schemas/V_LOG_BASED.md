# V_LOG_BASED

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=V_LOG_BASED

## Description

This view brings together fields needed from logs and cases that are used to report on KPI metrics.

## Metadata

| Property | Value |
| --- | --- |
| Type | View |
| Release Version | Rel 2012 |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| LOG_ID | VARCHAR (18) | The unique ID of the procedural log record for this row. |
| CASE_ID | VARCHAR (18) | This column stores the case ID (ORC) for this log. |
| PAT_ID | VARCHAR (18) | The unique ID of the patient associated with the procedural log record. |
| PAT_AGE | INTEGER | The patient age at the time of the procedure in years. This can be used as a filter to find logs for patients in different age buckets. |
| PATIENT_CLASS_C | VARCHAR (66) |  |
| PATIENT_CLASS_NM | No | The name of the category value for patient class for this log. |
| PATIENT_CLASS_GROUP | No | This column groups the patient class as to whether it is considered Inpatient or Outpatient based on the patient class category value and the grouping specified as a property on the view. |
| CASE_CLASS_C | INTEGER |  |
| CASE_CLASS_NM | No | The name of the category value that identifies the classification for this log. |
| LOG_STATUS_C | INTEGER |  |
| LOG_STATUS_NM | No | The name of the category value for the status of this log. |
| ADD_ON_CASE_MAN_YN | VARCHAR (1) |  |
| ADD_ON_CASE_SCH_YN | VARCHAR (1) |  |
| PRIMARY_PHYSICIAN_ID | VARCHAR (18) | The unique ID of the primary physician on the first panel for this log. This column is frequently used to link to CLARITY_SER. |
| PRIMARY_PHYSICIAN_NM | VARCHAR (200) | The name of the primary physician on the first panel for this log. |
| PRIMARY_PHYSICIAN_NM_WID | .2 .1 6000 | A unique identifier that consists of the name, credentials and the ID of the primary physician on the first panel for this log. This column is often used for grouping, sorting and display purposes in reports. |
| PRIMARY_PHYSICIAN_CRED | No | The current credentials for the primary physician. |
| SECONDARY_PHYSICIAN_ID | VARCHAR (18) | The unique ID of the secondary physician on the first panel for this log. The secondary physician is the first one listed with any of the roles specified in the view property on V_LOG_BASED. This column is frequently used to link to CLARITY_SER. |
| SECONDARY_PHYSICIAN_NM | VARCHAR (200) | The name of secondary physician on the first panel for this log. The secondary physician is the first one listed with any of the roles specified in the view property. |
| SECONDARY_PHYSICIAN_NM_WID | .2 .1 6000 | A unique identifier that consists of the name, credentials and the ID of the secondary physician on the first panel for this log. This column is often used for grouping, sorting and display purposes in reports. |
| SECONDARY_PHYSICIAN_CRED | No | The current credentials for the secondary physician. |
| SERVICE_C | VARCHAR (66) |  |
| SERVICE_NM | No | The name of the category value that indicates the service for this log. |
| PRIMARY_PROCEDURE_ID | VARCHAR (254) | The unique ID of the primary procedure for the log. The logic first looks to what is marked as primary on the first panel of the log. If no procedure is marked as primary it then uses the first listed procedure on the first panel of the log. |
| PRIMARY_PROCEDURE_NM | VARCHAR (200) | The name of the primary procedure for this log. |
| PRIMARY_PROCEDURE_NM_WID | ORP | A unique procedure identifier that consists of the name and the procedure ID of the primary procedure for this log. This column is often used for grouping, sorting and display purposes in reports. In order to determine the procedure ID to display it searches in the following order: the procedure code from a linked EAP record if the procedure is using EAP, the primary external ID, procedure internal ID. |
| LOCATION_ID | NUMERIC (18,0) | The unique ID of the location where the procedure was performed. This column is frequently used to link to CLARITY_LOC. |
| LOCATION_NM | VARCHAR (200) | The name of the location where the procedure for this log was performed. |
| LOCATION_NM_WID | .2 | A unique location identifier that consists of the location name and ID in which the procedural log was performed. This column is often used for grouping, sorting and display purposes in reports. |
| ROOM_ID | VARCHAR (18) | The unique ID of the room in which the procedure in the procedural log was performed. This column is frequently used to link to CLARITY_SER. |
| ROOM_NM | VARCHAR (200) | The name of the room in which the procedure for this log was performed. |
| ROOM_NM_WID | .2 | A unique room identifier that consists of the room name and ID in which the procedural log was performed. This column is often used for grouping, sorting and display purposes in reports. |
| PRIMARY_CIRCULATOR_ID | VARCHAR (18) | The unique ID of the first circulator documented in the room by staff time. If no staff times have been documented then this column returns the first one listed. |
| PRIMARY_CIRCULATOR_NM | VARCHAR (200) | The name of the first circulator documented in the room by staff time. If no staff times have been documented then this column returns the first one listed. |
| PRIMARY_CIRCULATOR_NM_WID | .2 .1 6000 | A unique identifier that consists of the name, credentials and the ID of the first circulator documented in the room by staff time. If no staff times have been documented then this column returns the first one listed. This column is often used for grouping, sorting and display purposes in reports. |
| PRIMARY_CIRCULATOR_CRED | No | The current credentials for the first circulator documented in the room by staff time. |
| PRIMARY_SURG_TECH_ID | VARCHAR (18) | The unique ID of the first surgical tech documented in the room by staff time. If no staff times have been documented then this column returns the first one listed. |
| PRIMARY_SURG_TECH_NM | VARCHAR (200) | The name of the first surgical tech documented in the room by staff time. If no staff times have been documented then this column returns the first one listed. |
| PRIMARY_SURG_TECH_NM_WID | .2 .1 6000 | A unique identifier that consists of the name, credentials and the ID of the first surgical tech documented in the room by staff time. If no staff times have been documented then this column returns the first one listed. This column is often used for grouping, sorting and display purposes in reports. |
| PRIMARY_SURG_TECH_CRED | No | The current credentials for the first surgical tech documented in the room by staff time. |
| FIRST_ANES_ID | VARCHAR (18) | The unique ID of the first documented anesthesia provider for the log. |
| FIRST_ANES_NM | VARCHAR (200) | The name of the first anesthesia provider documented in the room by staff time. If no staff times have been documented then this column returns the first one listed. |
| FIRST_ANES_NM_WID | .2 .1 6000 | A unique identifier that consists of the name, credentials and the ID of the first anesthesia provider documented in the room by staff time. If no staff times have been documented then this column returns the first one listed. This column is often used for grouping, sorting and display purposes in reports. |
| FIRST_ANES_CRED | No | The current credentials for the first anesthesia provider documented in the room by staff time. |
| PROC_DATE | DATETIME | The date on which the case was performed. |
| PROC_DAY_NUM_OF_WEEK | No | Contains a number representing the day of the week that the procedure was performed in the current locale for the corresponding CALENDAR_DT. The first day of the week is 0 and the last day of the week is 6.  For example, Sunday is the first day of the week in the United States. So Sunday would be 0 and Saturday would be 6 in this column. |
| PROC_DAY_OF_WEEK | No | Represents the name of the day of the week (Monday, Tuesday, etc.) that the procedure was performed. |
| PROC_MONTH_NUMBER | No | The month in integer form that the procedure was performed. For example, February will be "2". |
| PROC_MONTH_NAME | No | The month name in long form that the procedure was performed. For example, "February". |
| PROC_YEAR | No | This column contains the four-digit year that the procedure was performed. |
| PROC_YEAR_AND_MONTH | No | To help group by month, this column contains the month and year that the procedure was performed. The format is YYYYMM. |
| PROC_WEEK_OF_YEAR | No | The number of the week in the year that the procedure was performed. |
| PROC_WEEKEND_YN | No | Indicates whether the procedure was performed on a weekend day. "Y" indicates that the procedure was performed on a weekend day. "N" indicates that the procedure was not performed on a weekend day. |
| PROC_HOLIDAY_YN | No | Indicates whether the procedure was performed on a holiday. "Y" indicates that the procedure was performed on a holiday. "N" indicates that the procedure was not performed on a holiday. |
| NUMBER_OF_PROCEDURES | INTEGER | The total number of procedures on a log. |
| NUMBER_OF_PANELS | INTEGER | The number of panels in the surgical log. |
| PROC_NOT_PERF_C | INTEGER |  |
| PROC_NOT_PERF_NM | No | The reason why the procedure was not performed. |
| IN_OR_DTTM | DATETIME (Local) | The date and time documented in the log that the patient arrived in the procedure room. |
| OUT_OR_DTTM | DATETIME (Local) | The date and time documented in the log that the patient left the procedure room. |
| MINUTES_IN_OR | INTEGER | The minutes between the instants documented for the patient arriving in the procedure room and when the patient left the procedure room. |
| COUNT_IN_OR | No | If IN_OR_DTTM is populated then this column will be 1. Represents that the patient was in the procedure room. |
| PRIMARY_PREOP_NURSE_ID | VARCHAR (18) | The unique ID of the first nurse assigned to Preprocedure for this log. |
| PRIMARY_PREOP_NURSE_NM | VARCHAR (200) | The name of the first nurse assigned to Preprocedure for this log. |
| PRIMARY_PREOP_NURSE_NM_WID | .2 .1 6000 | A unique identifier that consists of the name, credentials and the ID for the first nurse assigned to Preprocedure for this log. This column is often used for grouping, sorting and display purposes in reports. |
| PRIMARY_PREOP_NURSE_CRED | No | The current credentials for the first nurse assigned to Preprocedure for this log. |
| IN_PREOP_DTTM | DATETIME (Local) | The date and time documented in the log that the patient arrived in preprocedure. |
| OUT_PREOP_DTTM | DATETIME (Local) | The date and time documented in the log that the patient's care was completed in preprocedure. |
| MINUTES_IN_PREOP | INTEGER | The minutes between the instants documented for the patient arriving in preprocedure and preprocedure care being completed. |
| COUNT_IN_PREOP | No | If IN_PREOP_DTTM is populated then this column will be 1. Represents that the patient was in Preprocedure. |
| PRIMARY_RECOVERY_NURSE_ID | VARCHAR (18) | The unique ID of first nurse assigned to Recovery for this log. |
| PRIMARY_RECOVERY_NURSE_NM | VARCHAR (200) | The name of first nurse assigned to Recovery for this log. |
| PRIMARY_RECOVERY_NURSE_NM_WID | .2 .1 6000 | A unique identifier that consists of the name, credentials and the ID of the first nurse assigned to Recovery for this log. This column is often used for grouping, sorting and display purposes in reports. |
| PRIMARY_RECOVERY_NURSE_CRED | No | The current credentials for the first nurse assigned to Recovery for this log. |
| IN_RECOVERY_DTTM | DATETIME (Local) | The date and time documented in the log that the patient arrived in recovery. |
| COMP_RECOVERY_DTTM | DATETIME (Local) | The date and time documented in the log that the patient's care was completed in recovery. |
| OUT_RECOVERY_DTTM | DATETIME (Local) | The date and time documented in the log that the patient left recovery. |
| MINUTES_BOARD_RECOVERY | INTEGER | The minutes between the instants documented for recovery care being completed and the patient leaving recovery. |
| MINUTES_IN_RECOVERY | INTEGER | The minutes between the instants documented for the patient arriving in recovery and the patient leaving recovery. |
| COUNT_IN_RECOVERY | No | If IN_RECOVERY_DTTM is populated then this column will be 1. Represents that the patient was in Recovery. |
| PRIMARY_PHASEII_NURSE_ID | VARCHAR (18) | The unique ID of first nurse assigned for Phase II for this log. |
| PRIMARY_PHASEII_NURSE_NM | VARCHAR (200) | The name of first nurse assigned for Phase II for this log. |
| PRIMARY_PHASEII_NURSE_NM_WID | .2 .1 6000 | A unique identifier that consists of the name, credentials and the ID for the first nurse assigned for Phase II for this log. This column is often used for grouping, sorting and display purposes in reports. |
| PRIMARY_PHASEII_NURSE_CRED | No | The current credentials for the first nurse assigned for Phase II for this log. |
| IN_PHASEII_DTTM | DATETIME (Local) | The date and time documented in the log that the patient arrived in phase II. |
| COMP_PHASEII_DTTM | DATETIME (Local) | The date and time documented in the log that the patient's care was completed in phase II. |
| OUT_PHASEII_DTTM | DATETIME (Local) | The date and time documented in the log that the patient left phase II. |
| MINUTES_BOARD_PHASEII | INTEGER | The minutes between the instants documented for phase II care being completed and the patient leaving phase II. |
| MINUTES_IN_PHASEII | INTEGER | The minutes between the instants documented for the patient arriving in phase II and the patient leaving phase II. |
| COUNT_IN_PHASEII | No | If IN_PHASEII_DTTM is populated then this column will be 1. Represents that the patient was in Phase II. |
| CASE_SCHEDULED_START_DTTM | DATETIME (Local) | The date and time at which the case was scheduled to be performed. |
| SETUP_LENGTH | INTEGER | The amount of time in minutes required to set up at the beginning of the case. |
| CLEANUP_LENGTH | INTEGER | The amount of time in minutes required to clean up at the end of the case. |
| CASE_SCHEDULED_END_DTTM | DATETIME (Local) | The date and time at which the case was scheduled to end. |
| ROOM_PREVIOUS_LOG_ID | VARCHAR (18) | The unique ID of the procedural log that precedes the procedural log record within the same room on the same day. The In Room event times are used to determine the order of the procedural logs. |
| ROOM_PREVIOUS_CASE_ID | VARCHAR (18) | The unique ID of the procedural case record (ORC) for the case that immediately precedes the current case on the same day in the same room. |
| RESP_ANES_ID | VARCHAR (18) | The unique ID of the responsible anesthesia provider for the log. The logic first looks to what is documented in Anesthesia and then if nothing is documented, it uses what is documented in OpTime.   For Anesthesia, the responsible anesthesia provider is based on the mode specified in the System Definitions (LSD 1) item 89400. The three options being the provider responsible for the most amount of time, the first responsible, or the last responsible. The staff types considered to be an anesthesia provider are specified in the profile (LPR) settings. For OpTime, the logic to determine who is responsible is based on the first anesthesia provider documented in the room. If no anesthesia provider has a time associated, then the first one listed on the log is used. The staff types associated with an anesthesia provider are specified in the Systems Definitions (EAF 1). |
| RESP_ANES_NM | VARCHAR (200) | The name of the responsible anesthesia provider associated with the log. |
| RESP_ANES_NM_WID | .2 .1 6000 | A unique identifier that consists of the name, credentials and the ID of the responsible anesthesia provider for the log. This column is often used for grouping, sorting and display purposes in reports. |
| RESP_ANES_CRED | No | The current credentials for the responsible anesthesia provider for this log. |
| PRIMARY_ANES_TYPE_C | INTEGER |  |
| PRIMARY_ANES_TYPE_NM | No | The name of the category value for the primary anesthesia type associated with a case. |
| LOG_EXCLUSION_REASON_C | INTEGER |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | LOG_ID | F_LOG_BASED | LOG_ID | Unknown | Unknown | No |  |
| 1 | LOG_ID | OR_LOG | LOG_ID | Unknown | Unknown | No |  |
| 1 | LOG_ID | OR_LOG_2 | LOG_ID | Unknown | Unknown | No |  |
| 1 | LOG_ID | OR_LOG_3 | LOG_ID | No | Unknown | No |  |
| 1 | LOG_ID | OR_LOG_METRIC_DETAILS | LOG_ID | No | Unknown | No |  |
| 1 | LOG_ID | OR_LOG_PRECEDING | LOG_ID | No | Unknown | No |  |
| 1 | LOG_ID | OR_LOG_VIRTUAL | LOG_ID | No | Unknown | No |  |
| 1 | LOG_ID | UK_CRM_PACEMKR_PROC | LOG_ID | No | Unknown | No |  |
| 1 | LOG_ID | V_CASE_CHARGES | LOG_ID | Unknown | Unknown | No |  |
| 1 | LOG_ID | V_CASE_COSTS | LOG_ID | Unknown | Unknown | No |  |
| 1 | LOG_ID | V_CASE_ON_TIME_START | LOG_ID | Unknown | Unknown | No |  |
| 1 | LOG_ID | V_CASE_PHYS_TURNOVER | LOG_ID | Unknown | Unknown | No |  |
| 1 | LOG_ID | V_CASE_ROOM_TURNOVER | LOG_ID | Unknown | Unknown | No |  |
| 1 | LOG_ID | V_CASE_VOLUME | LOG_ID | Unknown | Unknown | No |  |
| 1 | LOG_ID | V_DECISION_TO_INCISION | LOG_ID | Unknown | Unknown | No |  |
| 1 | LOG_ID | V_LOG_TIMING_EVENTS | LOG_ID | Unknown | Unknown | No |  |
| 2 | CASE_ID | OR_CASE | OR_CASE_ID | Unknown | Unknown | No |  |
| 2 | CASE_ID | OR_CASE_2 | CASE_ID | Unknown | Unknown | No |  |
| 2 | CASE_ID | OR_CASE_3 | CASE_ID | Unknown | Unknown | No |  |
| 2 | CASE_ID | OR_CASE_4 | OR_CASE_ID | No | Unknown | No |  |
| 2 | CASE_ID | OR_CASE_VIRTUAL | OR_CASE_ID | No | Unknown | No |  |
| 2 | CASE_ID | V_OR_CASE_ORR | CASE_ID | Unknown | Unknown | No |  |
| 3 | PAT_ID | ANTICOAG_SELF_REGULATING | PAT_ID | No | Unknown | No |  |
| 3 | PAT_ID | CARE_COORDINATION | PAT_ID | Unknown | Unknown | No |  |
| 3 | PAT_ID | CLAIMS_DERIVE_PAT_FLAGS | PAT_ID | No | Unknown | No |  |
| 3 | PAT_ID | COMMUNITY_RESRC_REVIEWED | PAT_ID | No | Unknown | No |  |
| 3 | PAT_ID | D_PAT_GEOGRAPHIC_CLASS | PAT_ID | Unknown | Unknown | No |  |
| 3 | PAT_ID | EPT_MEM_INFO | PAT_ID | No | Unknown | No |  |
| 3 | PAT_ID | EXT_DATA_LAST_DONE | PAT_ID | No | Unknown | No |  |
| 3 | PAT_ID | F_IBD_ADULT_FORM_PAT | PAT_ID | Unknown | Unknown | No |  |

_(249 total; showing first 30)_
