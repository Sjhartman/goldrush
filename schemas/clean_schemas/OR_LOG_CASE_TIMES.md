# OR_LOG_CASE_TIMES

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=OR_LOG_CASE_TIMES

## Description

The OR_LOG_CASE_TIMES table contains OR management system log timing information.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | ORL |
| Release Version | MU1 - MAY 2001 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| LOG_ID | VARCHAR (18) | The unique ID of the surgical log referred to by the case times. |
| LINE | No | The number of the line of the tracking event in the surgical log. |
| TRACKING_EVENT_C | VARCHAR (66) |  |
| TRACKING_TIME_IN | DATETIME (Local) | The date and time at which the patient was moved into the corresponding item in the event column in the surgical log. |
| TRACKING_TIME_OUT | DATETIME (Local) | The date and time at which the patient was moved out of the corresponding item in the event column in the surgical log. |
| TRACKING_TIME_ELPS | INTEGER | The total amount of time in seconds for the event in the surgical log. |
| TRACK_EVENT_TYPE_C | INTEGER |  |
| TRACKING_STATUS_C | INTEGER |  |
| TRACKING_STAT_INST | DATETIME (Local) | The instant at which the status took effect. |
| CM_PHY_OWNER_ID | VARCHAR (25) | ID of the physical deployment owner for this record.  Physical owners will be where the data is hosted, either on the cross-over server or the owner deployment. |
| CM_LOG_OWNER_ID | VARCHAR (25) | ID of the logical deployment owner for this record.  Logical owners show the deployment where the record was created but doesn't represent if the record is a part of version skew. |
| TRACKING_PAT_LOCATION_EVNT_ID | NUMERIC (18,0) | The patient location that triggered this event to be documented. |
| TRACKING_LOCATION_ID | NUMERIC (18,0) | The patient location that the patient was moved to when a patient location change triggered the event. |
| INTERVAL_EVENT_UPDATE_UTC_DTTM | DATETIME (UTC) | The instant of update for a case tracking event. |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| B-TREE INDEX | EIX_CASE_TIMES_TRACKING_EVNT_C | TRACKING_EVENT_C | 1 | Yes | Yes |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | LOG_ID | F_LOG_BASED | LOG_ID | Unknown | Unknown | No |  |
| 1 | LOG_ID | OR_LOG | LOG_ID | Unknown | No | No |  |
| 1 | LOG_ID | OR_LOG_2 | LOG_ID | Unknown | No | No |  |
| 1 | LOG_ID | OR_LOG_3 | LOG_ID | No | No | No |  |
| 1 | LOG_ID | OR_LOG_METRIC_DETAILS | LOG_ID | No | No | No |  |
| 1 | LOG_ID | OR_LOG_PRECEDING | LOG_ID | No | No | No |  |
| 1 | LOG_ID | OR_LOG_VIRTUAL | LOG_ID | No | No | No |  |
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
| 3 | TRACKING_EVENT_C | ZC_OR_PAT_EVENTS | TRACKING_EVENT_C | No | No | No |  |
| 7 | TRACK_EVENT_TYPE_C | ZC_OR_EVENT_TYPE | TRACK_EVENT_TYPE_C | No | No | No |  |
| 8 | TRACKING_STATUS_C | ZC_OR_PAT_STATUS | CASE_PROGRESS_C | No | No | No |  |
| 10 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 10 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 10 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 11 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 11 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 11 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 12 | TRACKING_PAT_LOCATION_EVNT_ID | CL_PLC | LOCATION_EVNT_ID | Unknown | No | No |  |
| 13 | TRACKING_LOCATION_ID | CL_PLF | RECORD_ID | No | No | No |  |
