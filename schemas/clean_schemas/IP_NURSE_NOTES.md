# IP_NURSE_NOTES

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=IP_NURSE_NOTES

## Description

This table displays information for nurse notes.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | INP |
| Release Version | Summer 2009 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| INPATIENT_DATA_ID | VARCHAR (18) | The unique identifier for the inpatient record. |
| LINE | No | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| NURSE_NOTE_TYPE_C | INTEGER |  |
| NURSE_NOTE_STATUS_C | INTEGER |  |
| NURSE_AUTHOR_ID | VARCHAR (18) | The ID of the nurse who authored the note. |
| NURSE_NOTE_INST_TM | DATETIME (Local) | The time that the nurse note was saved. |
| NURSE_NOTE_TEXT | VARCHAR (30000) | The text of the nurse note. |
| NURSE_NOTE_COPIED | VARCHAR (254) | Stores the nurse note copied to chart. |
| SR_PRIORITY_C | VARCHAR (66) |  |
| NURSE_NOTE_RICH_TEXT | VARCHAR (30000) | Stores the rich text of a nurse note created from the Sign Out Report or ED Comments activity. |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | INPATIENT_DATA_ID | IP_DATA_STORE | INPATIENT_DATA_ID | No | No | No |  |
| 3 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 4 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 4 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 4 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 5 | NURSE_NOTE_TYPE_C | ZC_NURSE_NOTE_TYPE | NURSE_NOTE_TYPE_C | No | No | No |  |
| 6 | NURSE_NOTE_STATUS_C | ZC_NURSE_NOTE_STAT | NURSE_NOTE_STAT_C | No | No | No |  |
| 7 | NURSE_AUTHOR_ID | CLARITY_EMP | USER_ID | Unknown | No | No |  |
| 7 | NURSE_AUTHOR_ID | CLARITY_EMP_2 | USER_ID | Unknown | No | No |  |
| 7 | NURSE_AUTHOR_ID | CLARITY_EMP_3 | USER_ID | Unknown | No | No |  |
| 7 | NURSE_AUTHOR_ID | CLARITY_EMP_4 | USER_ID | No | No | No |  |
| 7 | NURSE_AUTHOR_ID | CLARITY_EMP_DEMO | USER_ID | No | No | No |  |
| 7 | NURSE_AUTHOR_ID | EMP_BASIC_INFO | USER_ID | No | No | No |  |
| 7 | NURSE_AUTHOR_ID | EMP_DOC_SETTINGS | USER_NUMBER_ID | No | No | No |  |
| 7 | NURSE_AUTHOR_ID | F_RX_USER | USER_ID | Unknown | Unknown | No |  |
| 7 | NURSE_AUTHOR_ID | IB_MESSAGE_SETTINGS | USER_ID | No | No | No |  |
| 7 | NURSE_AUTHOR_ID | LOGIN_INFO | USER_NUMBER_ID | No | No | No |  |
| 7 | NURSE_AUTHOR_ID | QC_RESULTS_REVIEW | USER_NUMBER_ID | No | No | No |  |
| 7 | NURSE_AUTHOR_ID | USER_SIDEBAR_RPT | USER_NUMBER_ID | Unknown | No | No |  |
| 7 | NURSE_AUTHOR_ID | V_CUBE_D_USER | USER_ID | Unknown | Unknown | No |  |
| 7 | NURSE_AUTHOR_ID | V_CUBE_RX_USER | USER_ID | Unknown | Unknown | No |  |
| 11 | SR_PRIORITY_C | ZC_SR_PRIORITY | SR_PRIORITY_C | No | No | No |  |
