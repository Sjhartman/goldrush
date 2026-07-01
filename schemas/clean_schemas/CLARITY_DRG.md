# CLARITY_DRG

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=CLARITY_DRG

## Description

This table contains information for the DRG (Diagnosis Related Groups) master file.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | DRG |
| Release Version | EPIC 2000 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| DRG_ID | VARCHAR (18) | The unique identifier of the Diagnoses Related Group record. This is not the DRG code. |
| DRG_NAME | VARCHAR (223) | The name of the Diagnoses Related Group name. |
| RECORD_STATE *(deprecated)* | VARCHAR (20) |  |
| DRG_NUMBER | VARCHAR (12) | The non-overtime diagnosis-related group (DRG) code. |
| CM_PHY_OWNER_ID | VARCHAR (25) | ID of the physical deployment owner for this record.  Physical owners will be where the data is hosted, either on the cross-over server or the owner deployment. |
| CM_LOG_OWNER_ID | VARCHAR (25) | ID of the logical deployment owner for this record.  Logical owners show the deployment where the record was created but doesn't represent if the record is a part of version skew. |
| NON_MPI_WEIGHT | NUMERIC (20,4) | Use for DRG Weight when the DRG masterfile is not MPI enabled. |
| NON_MPI_TRIM_PTS | NUMERIC (18,2) | Use for DRG Trim Points when the DRG master file is not MPI enabled. |
| NON_MPI_AMLOS | NUMERIC (18,2) | Use for DRG Arithmetic Mean when the DRG Masterfile is not MPI Enabled. |
| NON_MPI_GMLOS | NUMERIC (18,2) | Use DRG Geometric mean when the DRG masterfile is not MPI enabled. |
| GROUPER_1_C | INTEGER |  |
| GROUPER_2_C | INTEGER |  |
| GROUPER_3_C | INTEGER |  |
| RECORD_STATE_C | INTEGER |  |
| DRG_CASE_TYPE_C | INTEGER |  |
| MSDRG_FAMILY_C | INTEGER |  |
| PATIENT_FRIENDLY_NAME | VARCHAR (250) | Patient-friendly name to display in billing communications such as letters. Otherwise patient-facing billing communication will use the DRG family (DRG-530) or, if that does not exist, the record name (DRG-.2). |
| DRG_CODE_SET_C | VARCHAR (66) |  |
| DRG_MDC_C | INTEGER |  |
| DRG_COMPLICATION_C | INTEGER | Surrogate key used to uniquely identify rows in this (and only this) table on Cogito Cloud only, do not assume the surrogate key in this table will correspond to the surrogate key in another table |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 5 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 5 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 5 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 6 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 6 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 6 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 11 | GROUPER_1_C | ZC_GROUPER_1_2 | GROUPER_1_2_C | No | No | No |  |
| 12 | GROUPER_2_C | ZC_GROUPER_2_2 | GROUPER_2_2_C | No | No | No |  |
| 13 | GROUPER_3_C | ZC_GROUPER_3 | GROUPER_3_C | No | No | No |  |
| 14 | RECORD_STATE_C | ZC_DEL_STATUS | DEL_STATUS_C | No | No | No |  |
| 14 | RECORD_STATE_C | ZC_EDG_REC_STAT | EDG_REC_STAT_C | No | No | No |  |
| 14 | RECORD_STATE_C | ZC_ERS_REC_STAT | RECORD_STATUS_C | No | No | No |  |
| 14 | RECORD_STATE_C | ZC_HCD_REC_STATE | HCD_REC_STATE_C | No | No | No |  |
| 14 | RECORD_STATE_C | ZC_HFL_RECORD_STAT | HFL_RECORD_STAT_C | No | No | No |  |
| 14 | RECORD_STATE_C | ZC_IMM_REC_STATUS | IMM_REC_STATUS_C | No | No | No |  |
| 14 | RECORD_STATE_C | ZC_LLB_STATUS | LLB_STATUS_C | No | No | No |  |
| 14 | RECORD_STATE_C | ZC_LMA_RECORD_STAT | LMA_RECORD_STAT_C | No | No | No |  |
| 14 | RECORD_STATE_C | ZC_MEM_REC_STATUS | MEM_REC_STATUS_C | No | No | No |  |
| 14 | RECORD_STATE_C | ZC_OR_REC_STATUS | OR_REC_STATUS_C | No | No | No |  |
| 14 | RECORD_STATE_C | ZC_PBA_REC_STAT | PBA_REC_STAT_C | No | No | No |  |
| 14 | RECORD_STATE_C | ZC_PROV_REC_STATE | PROV_REC_STATE_C | No | No | No |  |
| 14 | RECORD_STATE_C | ZC_RECORD_STATE_2 | RECORD_STATE_2_C | No | No | No |  |
| 14 | RECORD_STATE_C | ZC_RECORD_STATE_3 | RECORD_STATE_3_C | No | No | No |  |
| 14 | RECORD_STATE_C | ZC_RECORD_STATE_4 | RECORD_STATE_4_C | No | No | No |  |
| 14 | RECORD_STATE_C | ZC_RECORD_STATE_6 | RECORD_STATE_6_C | No | No | No |  |
| 14 | RECORD_STATE_C | ZC_RECORD_STATE_7 | RECORD_STATE_7_C | No | No | No |  |
| 14 | RECORD_STATE_C | ZC_RECORD_STAT_EPM | RECORD_STAT_EPM_C | No | No | No |  |
| 14 | RECORD_STATE_C | ZC_RECORD_STAT_EPP | RECORD_STAT_EPP_C | No | No | No |  |
| 14 | RECORD_STATE_C | ZC_RECORD_STAT_ETX | RECORD_STAT_ETX_C | No | No | No |  |
| 14 | RECORD_STATE_C | ZC_RECORD_STAT_HRV | RECORD_STAT_HRV_C | No | No | No |  |

_(36 total; showing first 30)_
