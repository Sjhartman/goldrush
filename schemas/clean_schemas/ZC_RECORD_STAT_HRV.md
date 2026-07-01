# ZC_RECORD_STAT_HRV

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=ZC_RECORD_STAT_HRV

## Description

Category list of the HRV record state (ie. inactive, hidden, etc...)

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | FULL |
| Load Frequency | INCREMENTAL |
| Chronicles INI | N/A |
| Release Version | SPRING 2006 |
| May contain EHI? | No |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| RECORD_STAT_HRV_C | 5 |  |
| NAME | 5 |  |
| TITLE | 5 |  |
| ABBR | 5 |  |
| INTERNAL_ID | 5 |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | RECORD_STAT_HRV_C | ZC_DEL_STATUS | DEL_STATUS_C | No | No | No |  |
| 1 | RECORD_STAT_HRV_C | ZC_EDG_REC_STAT | EDG_REC_STAT_C | No | No | No |  |
| 1 | RECORD_STAT_HRV_C | ZC_ERS_REC_STAT | RECORD_STATUS_C | No | No | No |  |
| 1 | RECORD_STAT_HRV_C | ZC_HCD_REC_STATE | HCD_REC_STATE_C | No | No | No |  |
| 1 | RECORD_STAT_HRV_C | ZC_HFL_RECORD_STAT | HFL_RECORD_STAT_C | No | No | No |  |
| 1 | RECORD_STAT_HRV_C | ZC_IMM_REC_STATUS | IMM_REC_STATUS_C | No | No | No |  |
| 1 | RECORD_STAT_HRV_C | ZC_LLB_STATUS | LLB_STATUS_C | No | No | No |  |
| 1 | RECORD_STAT_HRV_C | ZC_LMA_RECORD_STAT | LMA_RECORD_STAT_C | No | No | No |  |
| 1 | RECORD_STAT_HRV_C | ZC_MEM_REC_STATUS | MEM_REC_STATUS_C | No | No | No |  |
| 1 | RECORD_STAT_HRV_C | ZC_OR_REC_STATUS | OR_REC_STATUS_C | No | No | No |  |
| 1 | RECORD_STAT_HRV_C | ZC_PBA_REC_STAT | PBA_REC_STAT_C | No | No | No |  |
| 1 | RECORD_STAT_HRV_C | ZC_PROV_REC_STATE | PROV_REC_STATE_C | No | No | No |  |
| 1 | RECORD_STAT_HRV_C | ZC_RECORD_STATE_2 | RECORD_STATE_2_C | No | No | No |  |
| 1 | RECORD_STAT_HRV_C | ZC_RECORD_STATE_3 | RECORD_STATE_3_C | No | No | No |  |
| 1 | RECORD_STAT_HRV_C | ZC_RECORD_STATE_4 | RECORD_STATE_4_C | No | No | No |  |
| 1 | RECORD_STAT_HRV_C | ZC_RECORD_STATE_6 | RECORD_STATE_6_C | No | No | No |  |
| 1 | RECORD_STAT_HRV_C | ZC_RECORD_STATE_7 | RECORD_STATE_7_C | No | No | No |  |
| 1 | RECORD_STAT_HRV_C | ZC_RECORD_STAT_EPM | RECORD_STAT_EPM_C | No | No | No |  |
| 1 | RECORD_STAT_HRV_C | ZC_RECORD_STAT_EPP | RECORD_STAT_EPP_C | No | No | No |  |
| 1 | RECORD_STAT_HRV_C | ZC_RECORD_STAT_ETX | RECORD_STAT_ETX_C | No | No | No |  |
| 1 | RECORD_STAT_HRV_C | ZC_RECORD_STAT_RMC | RECORD_STAT_RMC_C | No | No | No |  |
