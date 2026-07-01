# MULT_DISC_DX

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=MULT_DISC_DX

## Description

This table contains information on the defined multidisciplinary diagnoses/problems.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | FULL |
| Load Frequency | WEEKLY - FULL |
| Chronicles INI | INX |
| Release Version | EPIC 2002 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| PROBLEM_ID | VARCHAR (18) | The unique ID for the multidisciplinary diagnoses. |
| NAME | VARCHAR (255) | The name of the multidisciplinary diagnoses. |
| SYSTEM_C | INTEGER |  |
| CM_PHY_OWNER_ID | VARCHAR (25) | ID of the physical deployment owner for this record.  Physical owners will be where the data is hosted, either on the cross-over server or the owner deployment. |
| CM_LOG_OWNER_ID | VARCHAR (25) | ID of the logical deployment owner for this record.  Logical owners show the deployment where the record was created but doesn't represent if the record is a part of version skew. |
| RECORD_STATUS_C | INTEGER |  |
| DISPLAY_NAME | VARCHAR (254) | The display name for the multidisciplinary diagnosis. |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 3 | SYSTEM_C | ZC_SYSTEM | SYSTEM_C | No | No | No |  |
| 4 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 4 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 4 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 5 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 5 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 5 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 6 | RECORD_STATUS_C | ZC_DEL_STATUS | DEL_STATUS_C | No | No | No |  |
| 6 | RECORD_STATUS_C | ZC_EDG_REC_STAT | EDG_REC_STAT_C | No | No | No |  |
| 6 | RECORD_STATUS_C | ZC_ERS_REC_STAT | RECORD_STATUS_C | No | No | No |  |
| 6 | RECORD_STATUS_C | ZC_HCD_REC_STATE | HCD_REC_STATE_C | No | No | No |  |
| 6 | RECORD_STATUS_C | ZC_HFL_RECORD_STAT | HFL_RECORD_STAT_C | No | No | No |  |
| 6 | RECORD_STATUS_C | ZC_IMM_REC_STATUS | IMM_REC_STATUS_C | No | No | No |  |
| 6 | RECORD_STATUS_C | ZC_LLB_STATUS | LLB_STATUS_C | No | No | No |  |
| 6 | RECORD_STATUS_C | ZC_LMA_RECORD_STAT | LMA_RECORD_STAT_C | No | No | No |  |
| 6 | RECORD_STATUS_C | ZC_MEM_REC_STATUS | MEM_REC_STATUS_C | No | No | No |  |
| 6 | RECORD_STATUS_C | ZC_OR_REC_STATUS | OR_REC_STATUS_C | No | No | No |  |
| 6 | RECORD_STATUS_C | ZC_PBA_REC_STAT | PBA_REC_STAT_C | No | No | No |  |
| 6 | RECORD_STATUS_C | ZC_PROV_REC_STATE | PROV_REC_STATE_C | No | No | No |  |
| 6 | RECORD_STATUS_C | ZC_RECORD_STATE_2 | RECORD_STATE_2_C | No | No | No |  |
| 6 | RECORD_STATUS_C | ZC_RECORD_STATE_3 | RECORD_STATE_3_C | No | No | No |  |
| 6 | RECORD_STATUS_C | ZC_RECORD_STATE_4 | RECORD_STATE_4_C | No | No | No |  |
| 6 | RECORD_STATUS_C | ZC_RECORD_STATE_6 | RECORD_STATE_6_C | No | No | No |  |
| 6 | RECORD_STATUS_C | ZC_RECORD_STATE_7 | RECORD_STATE_7_C | No | No | No |  |
| 6 | RECORD_STATUS_C | ZC_RECORD_STAT_EPM | RECORD_STAT_EPM_C | No | No | No |  |
| 6 | RECORD_STATUS_C | ZC_RECORD_STAT_EPP | RECORD_STAT_EPP_C | No | No | No |  |
| 6 | RECORD_STATUS_C | ZC_RECORD_STAT_ETX | RECORD_STAT_ETX_C | No | No | No |  |
| 6 | RECORD_STATUS_C | ZC_RECORD_STAT_HRV | RECORD_STAT_HRV_C | No | No | No |  |
| 6 | RECORD_STATUS_C | ZC_RECORD_STAT_RMC | RECORD_STAT_RMC_C | No | No | No |  |
