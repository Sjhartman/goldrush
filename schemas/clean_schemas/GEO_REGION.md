# GEO_REGION

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=GEO_REGION

## Description

The GEO_REGION table contains information about geographical regions. This includes codes to identify these regions.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | EGW |
| Release Version | Rel 2018 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| GEO_REGION_ID | NUMERIC (18,0) | The unique identifier for the geographical region record. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| GEO_REGION_NAME | VARCHAR (150) | The record name for the geographical region record. |
| RECORD_STATE_C | INTEGER |  |
| GEO_REGION_TYPE_C | INTEGER |  |
| INACTIVE_DATE | DATETIME | Specifies the date on which the geographical region is no longer active. |
| APP_EXCHANGE_OWNER | VARCHAR (50) | Stores a record identifier used to help identify the corresponding App Exchange owner. |
| APP_EXCHANGE_RECORD | VARCHAR (30) | Stores a record identifier used to help identify the corresponding App Exchange record. |
| PARENT_GEO_REGION_ID | NUMERIC (18,0) | Specifies the parent region for the region |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 2 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 2 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 3 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 5 | RECORD_STATE_C | ZC_DEL_STATUS | DEL_STATUS_C | No | No | No |  |
| 5 | RECORD_STATE_C | ZC_EDG_REC_STAT | EDG_REC_STAT_C | No | No | No |  |
| 5 | RECORD_STATE_C | ZC_ERS_REC_STAT | RECORD_STATUS_C | No | No | No |  |
| 5 | RECORD_STATE_C | ZC_HCD_REC_STATE | HCD_REC_STATE_C | No | No | No |  |
| 5 | RECORD_STATE_C | ZC_HFL_RECORD_STAT | HFL_RECORD_STAT_C | No | No | No |  |
| 5 | RECORD_STATE_C | ZC_IMM_REC_STATUS | IMM_REC_STATUS_C | No | No | No |  |
| 5 | RECORD_STATE_C | ZC_LLB_STATUS | LLB_STATUS_C | No | No | No |  |
| 5 | RECORD_STATE_C | ZC_LMA_RECORD_STAT | LMA_RECORD_STAT_C | No | No | No |  |
| 5 | RECORD_STATE_C | ZC_MEM_REC_STATUS | MEM_REC_STATUS_C | No | No | No |  |
| 5 | RECORD_STATE_C | ZC_OR_REC_STATUS | OR_REC_STATUS_C | No | No | No |  |
| 5 | RECORD_STATE_C | ZC_PBA_REC_STAT | PBA_REC_STAT_C | No | No | No |  |
| 5 | RECORD_STATE_C | ZC_PROV_REC_STATE | PROV_REC_STATE_C | No | No | No |  |
| 5 | RECORD_STATE_C | ZC_RECORD_STATE_2 | RECORD_STATE_2_C | No | No | No |  |
| 5 | RECORD_STATE_C | ZC_RECORD_STATE_3 | RECORD_STATE_3_C | No | No | No |  |
| 5 | RECORD_STATE_C | ZC_RECORD_STATE_4 | RECORD_STATE_4_C | No | No | No |  |
| 5 | RECORD_STATE_C | ZC_RECORD_STATE_6 | RECORD_STATE_6_C | No | No | No |  |
| 5 | RECORD_STATE_C | ZC_RECORD_STATE_7 | RECORD_STATE_7_C | No | No | No |  |
| 5 | RECORD_STATE_C | ZC_RECORD_STAT_EPM | RECORD_STAT_EPM_C | No | No | No |  |
| 5 | RECORD_STATE_C | ZC_RECORD_STAT_EPP | RECORD_STAT_EPP_C | No | No | No |  |
| 5 | RECORD_STATE_C | ZC_RECORD_STAT_ETX | RECORD_STAT_ETX_C | No | No | No |  |
| 5 | RECORD_STATE_C | ZC_RECORD_STAT_HRV | RECORD_STAT_HRV_C | No | No | No |  |
| 5 | RECORD_STATE_C | ZC_RECORD_STAT_RMC | RECORD_STAT_RMC_C | No | No | No |  |
| 6 | GEO_REGION_TYPE_C | ZC_GEO_REGION_TYPE | GEO_REGION_TYPE_C | No | No | No |  |
| 10 | PARENT_GEO_REGION_ID | GEO_REGION | GEO_REGION_ID | No | No | No |  |
