# SPEC_AP_RESULT

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=SPEC_AP_RESULT

## Description

This table contains information related to results entered on a specimen's anatomic pathology result.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | OVS |
| Release Version | Rel February 2022 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| SPECIMEN_ID | VARCHAR (18) | The unique identifier (.1 item) for the specimen record. |
| LINE | INTEGER | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| AP_RES_TYPE_C | INTEGER |  |
| AP_RES_NOTE_ID | VARCHAR (254) | The unique ID of this AP specimen result note. |
| AP_RES_STATUS_C | INTEGER |  |
| NOTIF_SENT_UTC_DTTM | DATETIME (UTC) | The first instant when a result notification was sent for this AP result in UTC. |
| ACK_COMM_ID | VARCHAR (45) | The communication that was logged when the result is acknowledged. |
| AP_RES_PUSH_EVAL_C | INTEGER |  |
| NOTIF_SENT_LOCAL_DTTM | DATETIME (Local) | The first instant when a result notification was sent for this AP result in the local time zone. |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | SPECIMEN_ID | AP_SPECIMEN_DESC | SPECIMEN_ID | No | No | No |  |
| 1 | SPECIMEN_ID | EMBRYOLOGY_SPECIMEN | SPECIMEN_ID | No | No | No |  |
| 1 | SPECIMEN_ID | SPEC_DB_MAIN | SPECIMEN_ID | No | No | No |  |
| 3 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 4 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 4 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 4 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 5 | AP_RES_TYPE_C | ZC_AP_RES_TYPE | AP_RES_TYPE_C | No | No | No |  |
| 6 | AP_RES_NOTE_ID | ABN_NOTES | ABN_NOTE_ID | Unknown | No | No |  |
| 6 | AP_RES_NOTE_ID | ABN_NOTE_INFO | NOTE_ID | No | No | No |  |
| 6 | AP_RES_NOTE_ID | CODING_CLA_NOTES | NOTE_ID | Unknown | No | No |  |
| 6 | AP_RES_NOTE_ID | FA_NOTES_QUERY | NOTE_ID | No | No | No |  |
| 6 | AP_RES_NOTE_ID | FIN_ASST_LETTER | NOTE_ID | No | No | No |  |
| 6 | AP_RES_NOTE_ID | FIN_ASST_NOTE | NOTE_ID | No | No | No |  |
| 6 | AP_RES_NOTE_ID | HNO_CVG_REQUEST | NOTE_ID | Unknown | No | No |  |
| 6 | AP_RES_NOTE_ID | HNO_INFO | NOTE_ID | No | No | No |  |
| 6 | AP_RES_NOTE_ID | HNO_INFO_2 | NOTE_ID | No | No | No |  |
| 6 | AP_RES_NOTE_ID | HNO_MYC_LET_INFO | NOTE_ID | No | No | No |  |
| 6 | AP_RES_NOTE_ID | HSP_ACCT_LETTERS | NOTE_ID | Unknown | No | No |  |
| 6 | AP_RES_NOTE_ID | HSP_ACCT_NOTES | NOTE_ID | Unknown | No | No |  |
| 6 | AP_RES_NOTE_ID | LETTER_EXTERNAL_INFO | NOTE_ID | No | No | No |  |
| 6 | AP_RES_NOTE_ID | NOTES_ACCT | NOTE_ID | Unknown | No | No |  |
| 6 | AP_RES_NOTE_ID | NOTES_LAB | NOTE_ID | Unknown | No | No |  |
| 6 | AP_RES_NOTE_ID | NOTES_MC_CLM | NOTE_ID | Unknown | Unknown | No |  |
| 6 | AP_RES_NOTE_ID | NOTES_MC_PBA | NOTE_ID | No | No | No |  |
| 6 | AP_RES_NOTE_ID | NOTES_MC_SER | NOTE_ID | Unknown | Unknown | No |  |
| 6 | AP_RES_NOTE_ID | NOTE_PARENT_NOTE | NOTE_ID | No | No | No |  |
| 6 | AP_RES_NOTE_ID | PATIENT_FYI_FLAGS | NOTE_ID | Unknown | No | No |  |

_(40 total; showing first 30)_
