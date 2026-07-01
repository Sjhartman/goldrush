# CL_ICD_PX

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=CL_ICD_PX

## Description

The CL_ICD_PX table is the master table for ICD procedures.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | HCD |
| Release Version | MU2 - MAY 2001 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| ICD_PX_ID | VARCHAR (18) | The unique ID of the ICD procedure record. |
| ICD_PX_NAME | VARCHAR (254) | The name of the ICD procedure record. |
| HCD_REC_STATE_C | INTEGER |  |
| PROCEDURE_NAME | VARCHAR (254) | The external name of the ICD procedure. |
| PROC_MASTER_NM | VARCHAR (60) | The external ID of the ICD procedure record. |
| SHORT_PROC_NAME | VARCHAR (60) | The short name for the procedure. |
| BILL_DESC | VARCHAR (254) | The description of the procedure to print on the bill. |
| CM_PHY_OWNER_ID | VARCHAR (25) | ID of the physical deployment owner for this record.  Physical owners will be where the data is hosted, either on the cross-over server or the owner deployment. |
| CM_LOG_OWNER_ID | VARCHAR (25) | ID of the logical deployment owner for this record.  Logical owners show the deployment where the record was created but doesn't represent if the record is a part of version skew. |
| CODE_SET_C *(deprecated)* | INTEGER |  |
| REFERENCE_CODE *(deprecated)* | VARCHAR (20) |  |
| PX_CODE | No |  |
| REF_CODE *(deprecated)* | VARCHAR (20) |  |
| REF_BILL_CODE | 4100 | The ICD Code associated with the procedure record. |
| REF_BILL_CODE_SET_C | 4101 |  |
| INSTANT_OF_UPDATE_DTTM | DATETIME (Local) | The instant when the ICD procedure record was last locked or unlocked before this row was extracted. Changes to the instant of update do not trigger a Clarity extract, so values in this column may not represent the current value in Chronicles. |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 3 | HCD_REC_STATE_C | ZC_DEL_STATUS | DEL_STATUS_C | No | No | No |  |
| 3 | HCD_REC_STATE_C | ZC_EDG_REC_STAT | EDG_REC_STAT_C | No | No | No |  |
| 3 | HCD_REC_STATE_C | ZC_ERS_REC_STAT | RECORD_STATUS_C | No | No | No |  |
| 3 | HCD_REC_STATE_C | ZC_HCD_REC_STATE | HCD_REC_STATE_C | No | No | No |  |
| 3 | HCD_REC_STATE_C | ZC_HFL_RECORD_STAT | HFL_RECORD_STAT_C | No | No | No |  |
| 3 | HCD_REC_STATE_C | ZC_IMM_REC_STATUS | IMM_REC_STATUS_C | No | No | No |  |
| 3 | HCD_REC_STATE_C | ZC_LLB_STATUS | LLB_STATUS_C | No | No | No |  |
| 3 | HCD_REC_STATE_C | ZC_LMA_RECORD_STAT | LMA_RECORD_STAT_C | No | No | No |  |
| 3 | HCD_REC_STATE_C | ZC_MEM_REC_STATUS | MEM_REC_STATUS_C | No | No | No |  |
| 3 | HCD_REC_STATE_C | ZC_OR_REC_STATUS | OR_REC_STATUS_C | No | No | No |  |
| 3 | HCD_REC_STATE_C | ZC_PBA_REC_STAT | PBA_REC_STAT_C | No | No | No |  |
| 3 | HCD_REC_STATE_C | ZC_PROV_REC_STATE | PROV_REC_STATE_C | No | No | No |  |
| 3 | HCD_REC_STATE_C | ZC_RECORD_STATE_2 | RECORD_STATE_2_C | No | No | No |  |
| 3 | HCD_REC_STATE_C | ZC_RECORD_STATE_3 | RECORD_STATE_3_C | No | No | No |  |
| 3 | HCD_REC_STATE_C | ZC_RECORD_STATE_4 | RECORD_STATE_4_C | No | No | No |  |
| 3 | HCD_REC_STATE_C | ZC_RECORD_STATE_6 | RECORD_STATE_6_C | No | No | No |  |
| 3 | HCD_REC_STATE_C | ZC_RECORD_STATE_7 | RECORD_STATE_7_C | No | No | No |  |
| 3 | HCD_REC_STATE_C | ZC_RECORD_STAT_EPM | RECORD_STAT_EPM_C | No | No | No |  |
| 3 | HCD_REC_STATE_C | ZC_RECORD_STAT_EPP | RECORD_STAT_EPP_C | No | No | No |  |
| 3 | HCD_REC_STATE_C | ZC_RECORD_STAT_ETX | RECORD_STAT_ETX_C | No | No | No |  |
| 3 | HCD_REC_STATE_C | ZC_RECORD_STAT_HRV | RECORD_STAT_HRV_C | No | No | No |  |
| 3 | HCD_REC_STATE_C | ZC_RECORD_STAT_RMC | RECORD_STAT_RMC_C | No | No | No |  |
| 8 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 8 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 8 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 9 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 9 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 9 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 15 | REF_BILL_CODE_SET_C | ZC_HCD_CODE_SET | CODE_SET_C | No | No | No |  |
