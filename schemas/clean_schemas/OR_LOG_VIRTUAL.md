# OR_LOG_VIRTUAL

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=OR_LOG_VIRTUAL

## Description

The OR_LOG_VIRTUAL table contains virtual items for the OR management system log records.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | ORL |
| Release Version | Rel 2014 |
| May contain EHI? | No |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| LOG_ID | VARCHAR (18) | The unique identifier (.1 item) for the log record. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this Chronicles record. This is populated only if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this Chronicles record was extracted. This is populated only if you use IntraConnect. |
| PRIMARY_ANES_TYPE_C | INTEGER |  |
| RESP_ANES_ID | VARCHAR (18) | The unique ID of the responsible anesthesia provider for the log. The logic first looks to what is documented in Anesthesia and then if nothing is documented, it uses what is documented in OpTime.   For Anesthesia, the responsible anesthesia provider is based on the mode specified in the System Definitions (LSD 1) item 89400. The three options being the provider responsible for the most amount of time, the first responsible, or the last responsible. The staff types considered to be an anesthesia provider are specified in the profile (LPR) settings. For OpTime, the logic to determine who is responsible is based on the first anesthesia provider documented in the room. If no anesthesia provider has a time associated, then the first one listed on the log is used. The staff types associated with an anesthesia provider are specified in the Systems Definitions (EAF 1). |
| PRIMARY_PROC_ID | VARCHAR (254) | The unique ID of the primary procedure for the log. The logic first looks to what is marked as primary on the first panel of the log. If no procedure is marked as primary it then uses the first listed procedure on the first panel of the log. |
| PATIENT_AGE | INTEGER | The patient age at the time of the procedure in years. This can be used as a filter to find logs for patients in different age buckets. |
| NUMBER_OF_PROCS | INTEGER | The total number of procedures on a log. |
| FIRST_CASE_IN_RNG_YN | VARCHAR (1) |  |
| SCH_START_OTS_DTTM | DATETIME (Local) | This is the scheduled start time of the case for on time starts based on system or location settings that gives the option to include or exclude the setup length.   This value is compared to the actual start time, ACT_START_OTS_DTTM, to calculate the minutes late of the case. |
| ACT_START_OTS_DTTM | DATETIME (Local) | This is the actual start time of the case for on time starts based on system or location settings.   This value is compared to the scheduled start time, SCH_START_OTS_DTTM, to calculate the minutes late of the case. |
| MINUTES_LATE | INTEGER | This is the number of minutes between the scheduled start time, SCH_START_OTS_DTTM, and the actual start time, ACT_START_OTS_DTTM. This value is compared to the late start minutes threshold to determine whether or not the case is late. |
| LATE_CASE_YN | VARCHAR (1) |  |
| SCH_END_OTS_DTTM | DATETIME (Local) | This is the scheduled end time of the case based on system or location settings that gives the option to include or exclude the cleanup length.   This value is compared to the actual end time, ACT_END_OTS_DTTM, to calculate the minutes overrun of the case. |
| ACT_END_OTS_DTTM | DATETIME (Local) | This is the actual end time of the case for on time starts based on system or location settings.   This value is compared to the scheduled end time, SCH_END_OTS_DTTM, to calculate the minutes overrun of the case. |
| MINUTES_OVERRUN | INTEGER | This is the number of minutes between the scheduled end time, SCH_END_OTS_DTTM, and the actual end time, ACT_END_OTS_DTTM. |
| FIRST_ANES_ID | VARCHAR (18) | The unique ID of the first documented anesthesia provider for the log. |
| CASE_LEN_MIN_DIFF | INTEGER | This column holds the absolute difference between the scheduled minutes in room and actual minutes in room of the case. |
| CASE_LEN_PCT_DIFF | INTEGER | This column holds percent difference between the scheduled minutes in room and actual minutes in room of the case. The percent is determined by taking the absolute difference between scheduled minutes in room and actual minutes in room and dividing by the actual minutes in room. |
| CASE_LEN_OVER_UND_C | INTEGER |  |
| CASE_LEN_ACCURAT_YN | VARCHAR (1) |  |
| CASE_LEN_MIN_THRESH | INTEGER | This column holds the threshold in minutes used to determine case length accuracy. |
| CASE_CLASS_COMPLIANT_YN | VARCHAR (1) |  |
| CASE_CLASS_THRESHOLD | INTEGER | The threshold in minutes associated with the case classification for this case. |
| INCLUDE_ORG_OTS_REPORT_YN | VARCHAR (1) |  |
| INCLUDE_ORG_VOLUME_REPORT_YN | VARCHAR (1) |  |
| INCLUDE_ORG_CLA_REPORT_YN | VARCHAR (1) |  |
| LOG_EXCLUSION_REASON_C | INTEGER |  |
| USED_SUPPLY_COST_DIFFERENCE | NUMERIC (18,2) | The amount by which a surgical log's used supply cost differs from the used supply cost benchmark for the procedure performed. |
| USED_IMPLANT_COST_DIFFERENCE | NUMERIC (18,2) | The amount by which a surgical log's used implant cost differs from the used implant cost benchmark for the procedure performed. |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | LOG_ID | F_LOG_BASED | LOG_ID | Unknown | Unknown | No |  |
| 1 | LOG_ID | OR_LOG | LOG_ID | Unknown | No | No |  |
| 1 | LOG_ID | OR_LOG_2 | LOG_ID | Unknown | No | No |  |
| 1 | LOG_ID | OR_LOG_3 | LOG_ID | No | No | No |  |
| 1 | LOG_ID | OR_LOG_METRIC_DETAILS | LOG_ID | No | No | No |  |
| 1 | LOG_ID | OR_LOG_PRECEDING | LOG_ID | No | No | No |  |
| 1 | LOG_ID | UK_CRM_PACEMKR_PROC | LOG_ID | No | No | No |  |
| 1 | LOG_ID | V_CASE_CHARGES | LOG_ID | Unknown | Unknown | No |  |
| 1 | LOG_ID | V_CASE_COSTS | LOG_ID | Unknown | Unknown | No |  |
| 1 | LOG_ID | V_CASE_ON_TIME_START | LOG_ID | Unknown | Unknown | No |  |
| 1 | LOG_ID | V_CASE_PHYS_TURNOVER | LOG_ID | Unknown | Unknown | No |  |
| 1 | LOG_ID | V_CASE_ROOM_TURNOVER | LOG_ID | Unknown | Unknown | No |  |
| 1 | LOG_ID | V_CASE_VOLUME | LOG_ID | Unknown | Unknown | No |  |
| 1 | LOG_ID | V_DECISION_TO_INCISION | LOG_ID | Unknown | Unknown | No |  |
| 1 | LOG_ID | V_LOG_BASED | LOG_ID | Unknown | Unknown | No |  |
| 1 | LOG_ID | V_LOG_TIMING_EVENTS | LOG_ID | Unknown | Unknown | No |  |
| 2 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 2 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 2 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 3 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 4 | PRIMARY_ANES_TYPE_C | ZC_OR_ANESTH_TYPE | ANESTHESIA_TYPE_C | No | No | No |  |
| 5 | RESP_ANES_ID | CLARITY_SER | PROV_ID | Unknown | No | No |  |
| 5 | RESP_ANES_ID | CLARITY_SER_2 | PROV_ID | Unknown | No | No |  |
| 5 | RESP_ANES_ID | CLARITY_SER_3 | PROV_ID | Unknown | No | No |  |
| 5 | RESP_ANES_ID | CLARITY_SER_4 | PROV_ID | No | No | No |  |
| 5 | RESP_ANES_ID | CLARITY_SER_MYC | PROV_ID | Unknown | No | No |  |
| 5 | RESP_ANES_ID | D_PROV_PRIMARY_HIERARCHY | PROV_ID | Unknown | Unknown | No |  |
| 5 | RESP_ANES_ID | ED_SER_SETTINGS | PROV_ID | Unknown | No | No |  |

_(54 total; showing first 30)_
