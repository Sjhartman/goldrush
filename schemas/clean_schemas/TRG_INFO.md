# TRG_INFO

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=TRG_INFO

## Description

This table stores treatment day or pathway step information that is contact-independent, such as the treatment day/pathway step status, the reason for canceling or deferring the day/step, the ID of the treatment plan (TPL) record that contains this treatment day or the ID of the pathway (TPL) record that contains this step, etc.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | TRG |
| Release Version | SPRING 2008 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| REGIMEN_ID | NUMERIC (18,0) | The treatment day ID. |
| CM_PHY_OWNER_ID | VARCHAR (25) | ID of the physical deployment owner for this record.  Physical owners will be where the data is hosted, either on the cross-over server or the owner deployment. |
| CM_LOG_OWNER_ID | VARCHAR (25) | ID of the logical deployment owner for this record.  Logical owners show the deployment where the record was created but doesn't represent if the record is a part of version skew. |
| REGIMEN_NAME | VARCHAR (254) | The name of the treatment day in this row. |
| DEFER_DAY_RSN_C | INTEGER |  |
| CANCEL_DAY_RSN_C | INTEGER |  |
| STATUS_COMMENTS | VARCHAR (254) | The status change comments for the treatment day in this row. |
| TRG_TPL_ID | No |  |
| TRG_STATUS_C | INTEGER |  |
| REC_TYPE_C | INTEGER |  |
| SG_PATHWAY_ID | NUMERIC (18,0) | The ID of the pathway (TPL) containing the smart group in this record. |
| GIVEN_EXTER_RSN_C | INTEGER |  |
| REC_ARCHIVED_YN | No | Indicates whether the Treatment Day record is archived at the record level. |
| REC_EVENT_ID | VARCHAR (18) | This item contains the ID of the event used to track reconciliation actions for this day |
| NEEDS_REC_YN | VARCHAR (1) |  |
| TX_REMOVE_REASON_C | INTEGER |  |
| TX_REMOVE_COMMENTS | VARCHAR (254) | The comments entered by the user who removed the treatment. |
| TX_REMOVE_UTC_DTTM | DATETIME (UTC) | The the date and time when the treatment was removed. |
| TX_REMOVE_EMP_ID | VARCHAR (18) | The unique ID of the user who removed the treatment. |
| INSTANT_OF_UPDATE_DTTM | DATETIME (Local) | Instant when record was updated |
| RECORD_STATUS_C | INTEGER |  |
| IS_TREATMENT_DAY_DELETED_YN | VARCHAR (1) |  |
| IS_TRT_DAY_DEL_BY_PLAN_CONV_YN | VARCHAR (1) |  |
| PAT_ID | VARCHAR (18) | The unique ID of the patient associated with this treatment plan, therapy plan, dental plan, BMT plan, or pathway. |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | REGIMEN_ID | DENTAL_VISIT_INFO | REGIMEN_ID | No | No | No |  |
| 1 | REGIMEN_ID | V_EHI_TRG_FILTER | REGIMEN_ID | Unknown | Unknown | No |  |
| 2 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 2 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 2 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 3 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 5 | DEFER_DAY_RSN_C | ZC_DEFER_DAY_RSN | DEFER_DAY_RSN_C | No | No | No |  |
| 6 | CANCEL_DAY_RSN_C | ZC_CANCEL_DAY_RSN | CANCEL_DAY_RSN_C | No | No | No |  |
| 9 | TRG_STATUS_C | ZC_OSQ_STATUS | OSQ_STATUS_C | No | No | No |  |
| 10 | REC_TYPE_C | ZC_REC_TYPE_3 | REC_TYPE_3_C | No | No | No |  |
| 11 | SG_PATHWAY_ID | DENT_TREATMENT | TREATMENT_ID | No | No | No |  |
| 11 | SG_PATHWAY_ID | TPL_HSB_EPT_LINK | TREATMENT_PLAN_ID | Unknown | No | No |  |
| 11 | SG_PATHWAY_ID | TPL_INFO | TREATMENT_PLAN_ID | No | No | No |  |
| 12 | GIVEN_EXTER_RSN_C | ZC_GIVEN_EXTER_RSN | GIVEN_EXTER_RSN_C | No | No | No |  |
| 14 | REC_EVENT_ID | ED_IEV_PAT_INFO | EVENT_ID | Unknown | No | No |  |
| 14 | REC_EVENT_ID | IP_MAR_BARCODE_ITM | EVENT_ID | Unknown | No | No |  |
| 16 | TX_REMOVE_REASON_C | ZC_TX_REMOVE_REASON | TX_REMOVE_REASON_C | No | No | No |  |
| 19 | TX_REMOVE_EMP_ID | CLARITY_EMP | USER_ID | Unknown | No | No |  |
| 19 | TX_REMOVE_EMP_ID | CLARITY_EMP_2 | USER_ID | Unknown | No | No |  |
| 19 | TX_REMOVE_EMP_ID | CLARITY_EMP_3 | USER_ID | Unknown | No | No |  |
| 19 | TX_REMOVE_EMP_ID | CLARITY_EMP_4 | USER_ID | No | No | No |  |
| 19 | TX_REMOVE_EMP_ID | CLARITY_EMP_DEMO | USER_ID | No | No | No |  |
| 19 | TX_REMOVE_EMP_ID | EMP_BASIC_INFO | USER_ID | No | No | No |  |
| 19 | TX_REMOVE_EMP_ID | EMP_DOC_SETTINGS | USER_NUMBER_ID | No | No | No |  |
| 19 | TX_REMOVE_EMP_ID | F_RX_USER | USER_ID | Unknown | Unknown | No |  |
| 19 | TX_REMOVE_EMP_ID | IB_MESSAGE_SETTINGS | USER_ID | No | No | No |  |
| 19 | TX_REMOVE_EMP_ID | LOGIN_INFO | USER_NUMBER_ID | No | No | No |  |
| 19 | TX_REMOVE_EMP_ID | QC_RESULTS_REVIEW | USER_NUMBER_ID | No | No | No |  |

_(67 total; showing first 30)_
