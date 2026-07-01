# OR_LOG_ADDL_CODES

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=OR_LOG_ADDL_CODES

## Description

This table stores the additional codes for the log.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | ORL |
| Release Version | Rel 2015 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| LOG_ID | VARCHAR (18) | The unique identifier for the log record. |
| LINE | INTEGER | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| OR_LOG_ADDL_CODE_ID | NUMERIC (18,0) | This item stores the additional codes for the log. |

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
| 3 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 4 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 4 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 4 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 5 | OR_LOG_ADDL_CODE_ID | CLARITY_EAP | PROC_ID | No | No | No |  |
| 5 | OR_LOG_ADDL_CODE_ID | CLARITY_EAP_2 | PROC_ID | No | No | No |  |
| 5 | OR_LOG_ADDL_CODE_ID | CLARITY_EAP_3 | PROC_ID | No | No | No |  |
| 5 | OR_LOG_ADDL_CODE_ID | CLARITY_EAP_4 | PROC_ID | No | No | No |  |
| 5 | OR_LOG_ADDL_CODE_ID | CLARITY_EAP_5 | PROC_ID | No | No | No |  |
| 5 | OR_LOG_ADDL_CODE_ID | CLARITY_EAP_IMM | PROC_ID | Unknown | No | No |  |
| 5 | OR_LOG_ADDL_CODE_ID | PROC_CONSENT_CONFIG | PROC_ID | No | No | No |  |

_(32 total; showing first 30)_
