# LAB_SMT_NOADD

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=LAB_SMT_NOADD

## Description

Table for no-add single response items on the submitter record.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | FULL |
| Load Frequency | WEEKLY - FULL |
| Chronicles INI | SMT |
| Release Version | SPRING 2007 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| RECORD_ID | NUMERIC (18,0) | The unique identifier for the submitter record. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this Chronicles record. This is populated only if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this Chronicles record was extracted. This is populated only if you use IntraConnect. |
| RECORD_NAME | VARCHAR (200) | The name of the submitter record. |
| RECORD_STATUS_C | INTEGER |  |
| PARENT_SUBMITTER_ID | NUMERIC (18,0) | Enter the parent submitter of this submitter. |
| SHARE_PAT_YN | VARCHAR (1) |  |
| EMR_PARTICIPANT_C | INTEGER |  |
| DEFAULT_BILL_MTHD_C | INTEGER |  |
| LOCK_DEF_BILL_TO_YN | VARCHAR (1) |  |
| QUES_ANS_1_C | INTEGER |  |
| QUES_ANS_2_C | INTEGER |  |
| QUES_ANS_3_C | INTEGER |  |
| QUES_ANS_4_C | INTEGER |  |
| QUES_ANS_5_C | INTEGER |  |
| RECORD_CREATION_DT | DATETIME | Stores the date the record was created |
| INSTANT_UPDATE_TIME | DATETIME (Local) | Stores the instant the record was last locked/unlocked |
| TIME_ZONE_C | INTEGER |  |
| WAYPOINT_SUBMITTER_YN | VARCHAR (1) |  |
| DONATION_FACILITY_TYPE_C | INTEGER | Surrogate key used to uniquely identify rows in this (and only this) table on Cogito Cloud only, do not assume the surrogate key in this table will correspond to the surrogate key in another table |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 2 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 2 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 3 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 5 | RECORD_STATUS_C | ZC_RECORD_STATUS_2 | RECORD_STATUS_2_C | No | No | No |  |
| 5 | RECORD_STATUS_C | ZC_RECORD_STS | RECORD_STS_C | No | No | No |  |
| 6 | PARENT_SUBMITTER_ID | LAB_SMT_NOADD | RECORD_ID | Unknown | No | No |  |
| 8 | EMR_PARTICIPANT_C | ZC_EMR_PARTICIPANT | EMR_PARTICIPANT_C | No | No | No |  |
| 9 | DEFAULT_BILL_MTHD_C | ZC_DEF_BILL_MTHD | DEFAULT_BILL_MTHD_C | No | No | No |  |
| 11 | QUES_ANS_1_C | ZC_QUES_ANS_1 | QUES_ANS_1_C | No | No | No |  |
| 12 | QUES_ANS_2_C | ZC_QUES_ANS_2 | QUES_ANS_2_C | No | No | No |  |
| 13 | QUES_ANS_3_C | ZC_QUES_ANS_3 | QUES_ANS_3_C | No | No | No |  |
| 14 | QUES_ANS_4_C | ZC_QUES_ANS_4 | QUES_ANS_4_C | No | No | No |  |
| 15 | QUES_ANS_5_C | ZC_QUES_ANS_5 | QUES_ANS_5_C | No | No | No |  |
| 18 | TIME_ZONE_C | ZC_TIMEZONE | TIME_ZONE_C | No | No | No |  |
| 20 | DONATION_FACILITY_TYPE_C | ZC_DONATION_FACILITY_TYPE | DONATION_FACILITY_TYPE_C | No | No | No |  |
