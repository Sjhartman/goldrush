# IP_FREQUENCY

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=IP_FREQUENCY

## Description

This table contains data on discrete frequency (EFQ) records.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | EFQ |
| Release Version | EPIC 2002 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| FREQ_ID | VARCHAR (18) | The unique ID for the frequency record. |
| FREQ_NAME | VARCHAR (70) | The name of the frequency record. |
| FREQ_TYPE | INTEGER |  |
| APPLIES_TO *(deprecated)* | INTEGER |  |
| NUMBER_OF_TIMES | FLOAT | This determines how often a task is to be scheduled (the meaning varies depending on if the type is frequency or period). Only integers are allowed as we move forward, but historical frequency records could contain decimals. |
| TIME_UNIT | INTEGER |  |
| NOW_YN | VARCHAR (1) |  |
| PRN_YN | VARCHAR (1) |  |
| END_OF_RANGE *(deprecated)* | INTEGER | This determines the end of the range for this frequency. |
| IS_COMMON_YN | VARCHAR (1) |  |
| FREQ_PERIOD | INTEGER |  |
| CM_PHY_OWNER_ID | VARCHAR (25) | ID of the physical deployment owner for this record.  Physical owners will be where the data is hosted, either on the cross-over server or the owner deployment. |
| CM_LOG_OWNER_ID | VARCHAR (25) | ID of the logical deployment owner for this record.  Logical owners show the deployment where the record was created but doesn't represent if the record is a part of version skew. |
| DUP_DOSE_INT | INTEGER | Duplicate Dose Interval. This is the number of hours to consider an off-schedule occurrence to count for the standard time. The first standard time will be skipped if the off-schedule occurrence is within this interval. |
| MISSED_DOSE_INT | INTEGER | Missed Dose Interval. This is the number of hours after the standard time to auto-schedule an occurrence at the start time. This only applies if there is no off-schedule occurrence and scheduling starts at a point after the standard time. If the interval between the previous standard time and the scheduling start point is less than this setting, an occurrence will auto-schedule at the start point. |
| IP_COUNT | INTEGER | Enter the default count for orders with this frequency. Both Count and Count Type are necessary to determine the default end date and/or end time of the order. If the Default Count Type field is blank, the default count does not appear in the Order Composer. |
| IP_COUNT_TYPE_C | INTEGER |  |
| END_DURATION | FLOAT | End Duration is used to determine the default end date and end time of an order placed with a When type frequency. It is the number of hours the order should remain on the MAR before being marked as inactive. |
| UNTIL_DISCONTINU_YN | VARCHAR (1) |  |
| SPEC_TYPE_C | INTEGER |  |
| CYCLE_LENGTH | NUMERIC (3,0) | The cycle length of this frequency. |
| ALLOW_CHANGE_DAY_YN | VARCHAR (1) |  |
| RECORD_STATE_C | INTEGER |  |
| DISPLAY_NAME | VARCHAR (254) | This column holds the display name of the frequency. |
| GENERIC_FREQ_ID | VARCHAR (18) | The generic frequency record for this frequency. |
| WHEN_TIME_C | INTEGER |  |
| PRN_PAR_LEVEL | INTEGER | This column stores the PRN PAR level for dispensing for this frequency. |
| KEEP_DEF_START_T_YN | VARCHAR (1) |  |
| SEL_DO_NOT_DISP_YN | VARCHAR (1) |  |
| DELIV_DEST_DEP_ID | NUMERIC (18,0) | The unique ID of the department which is the delivery destination override for this frequency. |
| PERDAY_MULTDAYS_YN | VARCHAR (1) |  |
| MAX_INTERVAL | INTEGER | Determines the maximum interval between doses of orders in a Followed By group. |
| UNTIL_SPECIFIED_YN | VARCHAR (1) |  |
| MAR_RESTR_RESCH_YN | VARCHAR (1) |  |
| RESTR_MED_YN | VARCHAR (1) |  |
| TREAT_CONTINUOUS_YN | VARCHAR (1) |  |
| NOTIFICATION_GROUPING_SYSTEM_C | INTEGER |  |
| SIG_TIME_UNIT_C | INTEGER |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | FREQ_ID | FREQ_INCL_OR_EXCL_DEPS | FREQ_ID | No | No | No |  |
| 1 | FREQ_ID | FREQ_INCL_OR_EXCL_FACS | FREQ_ID | No | No | No |  |
| 1 | FREQ_ID | FREQ_INCL_OR_EXCL_LEDS | FREQ_ID | No | No | No |  |
| 3 | FREQ_TYPE | ZC_FREQ_TYPE | FREQ_TYPE_C | No | No | No |  |
| 6 | TIME_UNIT | ZC_NEAREST_MED_TIM | NEAREST_MED_TIM_C | No | No | No |  |
| 11 | FREQ_PERIOD | ZC_FREQ_PERIOD | FREQ_PERIOD_C | No | No | No |  |
| 12 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 12 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 12 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 13 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 13 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 13 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 17 | IP_COUNT_TYPE_C | ZC_STND_TP | STND_TP_C | No | No | No |  |
| 20 | SPEC_TYPE_C | ZC_SPEC_TYPE_2 | SPEC_TYPE_2_C | No | No | No |  |
| 23 | RECORD_STATE_C | ZC_RECORD_STATUS | RECORD_STATUS_C | No | No | No |  |
| 25 | GENERIC_FREQ_ID | FREQ_INCL_OR_EXCL_DEPS | FREQ_ID | No | No | No |  |
| 25 | GENERIC_FREQ_ID | FREQ_INCL_OR_EXCL_FACS | FREQ_ID | No | No | No |  |
| 25 | GENERIC_FREQ_ID | FREQ_INCL_OR_EXCL_LEDS | FREQ_ID | No | No | No |  |
| 25 | GENERIC_FREQ_ID | IP_FREQUENCY | FREQ_ID | No | No | No |  |
| 26 | WHEN_TIME_C | ZC_WHEN_TIME | WHEN_TIME_C | No | No | No |  |
| 30 | DELIV_DEST_DEP_ID | BH_DEP | DEPARTMENT_ID | No | No | No |  |
| 30 | DELIV_DEST_DEP_ID | CLARITY_DEP | DEPARTMENT_ID | No | No | No |  |
| 30 | DELIV_DEST_DEP_ID | CLARITY_DEP_2 | DEPARTMENT_ID | No | No | No |  |
| 30 | DELIV_DEST_DEP_ID | CLARITY_DEP_3 | DEPARTMENT_ID | No | No | No |  |
| 30 | DELIV_DEST_DEP_ID | CLARITY_DEP_4 | DEPARTMENT_ID | No | No | No |  |
| 30 | DELIV_DEST_DEP_ID | CLARITY_DEP_5 | DEPARTMENT_ID | No | No | No |  |
| 30 | DELIV_DEST_DEP_ID | CLARITY_DEP_MYC | DEPARTMENT_ID | No | No | No |  |
| 30 | DELIV_DEST_DEP_ID | DEPT_QUEUE_MSG_SETTINGS | DEPARTMENT_ID | No | No | No |  |
| 30 | DELIV_DEST_DEP_ID | DEPT_VERIFIED_INFO | DEPARTMENT_ID | No | No | No |  |
| 30 | DELIV_DEST_DEP_ID | DEP_BATCH_LTR_GEN | DEPARTMENT_ID | No | No | No |  |

_(40 total; showing first 30)_
