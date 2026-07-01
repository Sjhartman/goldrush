# V_LOG_TIMING_EVENTS

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=V_LOG_TIMING_EVENTS

## Description

The V_LOG_TIMING_EVENTS view contains information about case timing events associated with a procedural case.

## Metadata

| Property | Value |
| --- | --- |
| Type | View |
| Release Version | Rel 2014 |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| LOG_ID | VARCHAR (18) | The unique ID of the procedural log record for this row. |
| CASE_ID | VARCHAR (18) | This column stores the case ID (ORC) for this log. |
| SCHED_SETUP_START_DTTM | DATETIME (Local) | The instant the case setup is scheduled to start. |
| SCHED_IN_ROOM_DTTM | DATETIME (Local) | The instant the patient is scheduled to be in the room. |
| SCHED_OUT_ROOM_DTTM | DATETIME (Local) | The instant the patient is scheduled to be out of the room. |
| SCHED_CLEANUP_COMP_DTTM | DATETIME (Local) | The instant the case cleanup is scheduled to be completed. |
| PATIENT_IN_FACILITY_DTTM | DATETIME (Local) | The instant documented in the log that the patient arrived in the facility. |
| PATIENT_IN_PREPROCEDURE_DTTM | DATETIME (Local) | The instant documented in the log that the patient arrived in preprocedure. |
| ROOM_SETUP_START_DTTM | DATETIME (Local) | The instant documented in the log that the room setup started for the case. |
| ROOM_READY_DTTM | DATETIME (Local) | The instant documented in the log that the room is ready for the case to begin. |
| ANESTHESIA_START_DTTM | DATETIME (Local) | The instant documented in the log that the anesthesia has started for the patient. |
| PREPROCEDURE_COMP_DTTM | DATETIME (Local) | The instant documented in the log that patient care was completed in preprocedure. |
| PATIENT_IN_ROOM_DTTM | DATETIME (Local) | The instant documented in the log that patient arrived in the procedure room. |
| ANESTHESIA_INDUCTION_DTTM | DATETIME (Local) | The instant documented in the log that anesthesia was induced for the patient. |
| ANESTHESIA_READY_DTTM | DATETIME (Local) | The instant documented in the log that anesthesia was ready for the procedure to begin. |
| PROCEDURE_START_DTTM | DATETIME (Local) | The instant documented in the log that first procedure started or incision was made. |
| PROCEDURE_COMP_DTTM | DATETIME (Local) | The instant documented in the log that last procedure was completed or final incision was closed. |
| PATIENT_OUT_ROOM_DTTM | DATETIME (Local) | The instant documented in the log that patient left the procedure room. |
| ROOM_CLEANUP_START_DTTM | DATETIME (Local) | The instant documented in the log that the room started to be cleaned. |
| ROOM_CLEANUP_COMP_DTTM | DATETIME (Local) | The instant documented in the log that the room was completed being cleaned. |
| PATIENT_IN_RECOVERY_DTTM | DATETIME (Local) | The instant documented in the log that patient arrived in recovery. |
| ANESTHESIA_STOP_DTTM | DATETIME (Local) | The instant documented in the log that patient anesthesia care was completed. |
| RECOVERY_COMP_DTTM | DATETIME (Local) | The instant documented in the log that patient care was completed in recovery. |
| PATIENT_OUT_RECOVERY_DTTM | DATETIME (Local) | The instant documented in the log that patient left recovery. |
| PATIENT_IN_PHASEII_DTTM | DATETIME (Local) | The instant documented in the log that patient arrived in phase II. |
| PHASEII_COMP_DTTM | DATETIME (Local) | The instant documented in the log that patient care was completed in phase II. |
| PATIENT_OUT_PHASEII_DTTM | DATETIME (Local) | The instant documented in the log that patient left phase II. |
| MINUTES_IN_FAC_TO_SCH_IN_ROOM | INTEGER | The minutes between the instants documented for the patient arriving in the facility and the patient scheduled to be in the procedure room. |
| MINUTES_PRE_COMP_TO_SCH_IN_RM | INTEGER | The minutes between the instants documented for the patient having care completed in preprocedure and the patient scheduled to be in the procedure room. |
| MINUTES_IN_FAC_TO_IN_PREOP | INTEGER | The minutes between the instants documented for the patient arriving in facility and arriving in preprocedure. |
| MINUTES_IN_PREOP_TO_PREOP_COMP | INTEGER | The minutes between the instants documented for the patient arriving in preprocedure and preprocedure care being completed. |
| MINUTES_PREOP_COMP_TO_IN_ROOM | INTEGER | The minutes between the instants documented for preprocedure care being completed and the patient arriving in the procedure room. |
| MINUTES_IN_PREOP_TO_IN_ROOM | INTEGER | The minutes between the instants documented for the patient arriving in preprocedure and the patient arriving in the procedure room. |
| MINUTES_IN_ROOM_TO_ANES_INDUC | INTEGER | The minutes between the instants documented for the patient arriving in the procedure room and anesthesia induction for the patient. |
| MINUTES_IN_ROOM_TO_ANES_READY | INTEGER | The minutes between the instants documented for the patient arriving in the procedure room and anesthesia being marked as ready for the procedure to begin. |
| MINUTES_PROC_START_TO_COMP | INTEGER | The minutes between the instants documented for the procedure start and the procedure being completed. This can also be considered as the time between the first incision open to final incision close. |
| MINUTES_PROC_COMP_TO_OUT_ROOM | INTEGER | The minutes between the instants documented for the procedure being completed and when the patient left the procedure room. |
| MINUTES_IN_ROOM_TO_OUT_ROOM | INTEGER | The minutes between the instants documented for the patient arriving in the procedure room and when the patient left the procedure room. |
| MINUTES_IN_REC_TO_OUT_REC | INTEGER | The minutes between the instants documented for the patient arriving in recovery and the patient leaving recovery. |
| MINUTES_REC_COMP_TO_OUT_REC | INTEGER | The minutes between the instants documented for recovery care being completed and the patient leaving recovery. |
| MINUTES_IN_PHII_TO_OUT_PHII | INTEGER | The minutes between the instants documented for the patient arriving in phase II and the patient leaving phase II. |
| MINUTES_PHII_COMP_TO_OUT_PHII | INTEGER | The minutes between the instants documented for phase II care being completed and the patient leaving phase II. |
| MINUTES_SCH_IN_ROOM_TO_SCH_OUT | INTEGER | The minutes between the instants documented for the patient scheduled to be in the procedure room and the patient scheduled to be out of the procedure room. |
| CASE_REQUEST_DTTM | DATETIME (Local) | The instant the case is requested. |
| MINUTES_REQUEST_TO_IN_ROOM | INTEGER | The minutes between the instants documented for the case request and the patient arriving in the procedure room. |
| ANESTHESIA_EMERGENCE_DTTM | DATETIME (Local) | The instant documented in the log that the patient emerged from anesthesia. |
| ANESTHESIA_SIGNOFF_DTTM | DATETIME (Local) | The instant documented in the anesthesia record that the patient was marked as ready for procedure. |
| ANESTHESIA_CLOSE_DTTM | DATETIME (Local) | The instant the anesthesia record was closed. |
| MINUTES_INDUCTION_TO_EMERGENCE | INTEGER | The minutes between the instants documented for patient induction to emergence. |
| ANESTHESIA_LAST_ADDENDUM_DTTM | DATETIME (Local) | The instant the last addendum to the anesthesia record was signed. |
| MINUTES_ANSTOP_TO_LASTADDENDUM | INTEGER | The minutes between the instants documented for anesthesia stop and the last addendum to the anesthesia record. |
| MINUTES_ANSTART_TO_ANSTOP | INTEGER | The minutes between the instants documented for anesthesia start and anesthesia stop. |

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
| 1 | LOG_ID | V_LOG_BASED | LOG_ID | Unknown | Unknown | No |  |
| 2 | CASE_ID | OR_CASE | OR_CASE_ID | Unknown | Unknown | No |  |
| 2 | CASE_ID | OR_CASE_2 | CASE_ID | Unknown | Unknown | No |  |
| 2 | CASE_ID | OR_CASE_3 | CASE_ID | Unknown | Unknown | No |  |
| 2 | CASE_ID | OR_CASE_4 | OR_CASE_ID | No | Unknown | No |  |
| 2 | CASE_ID | OR_CASE_VIRTUAL | OR_CASE_ID | No | Unknown | No |  |
| 2 | CASE_ID | V_OR_CASE_ORR | CASE_ID | Unknown | Unknown | No |  |
