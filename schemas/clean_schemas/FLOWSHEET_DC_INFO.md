# FLOWSHEET_DC_INFO

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=FLOWSHEET_DC_INFO

## Description

This table displays no add item information for device variable records (FDC).  This includes basic items such as record, name, ID, creation date, items edited, etc.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | FDC |
| Release Version | Summer 2009 |
| May contain EHI? | No |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| RECORD_ID | NUMERIC (18,0) | The unique identifier (.1 item) for the variable record. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| VARIABLE_NAME | VARCHAR (254) | The name of this FDC record. |
| RECORD_STATE_C | INTEGER |  |
| VARIABLE_ID | INTEGER | The variable ID for this record. |
| SPECIAL_TYPE_C | VARCHAR (66) |  |
| UNIT_C | INTEGER |  |
| CONVERSION_LPP_ID | NUMERIC (18,0) | This column stores the ID of the programming point that will be used to convert the data. |
| DEV_DATA_LKBK_TIME | INTEGER | This column stores the amount of time the lookback override pulls device data. |
| DEV_DATA_LKFWD_TIME | INTEGER | This column stores the amount of time the lookforward override pulls device data. |
| INST_NO_ADD_ED_DTTM *(deprecated)* | DATETIME | *** Deprecated *** In table FLOWSHEET_DC_INFO, the column INST_NO_ADD_ED_DTTM (FDC/9030) has been deprecated. The deprecated column's data is no longer available since it is no longer populated in Chronicles. |
| NO_ADD_ITM_ED *(deprecated)* | VARCHAR (254) | *** Deprecated *** In table FLOWSHEET_DC_INFO, the column NO_ADD_ITM_ED (FDC/9040) has been deprecated. The deprecated column's data is no longer available since it is no longer populated in Chronicles. |
| REC_CREATE_DATE | DATETIME | Stores the record creation date. |
| VENTILATOR_CLASS_C | INTEGER |  |

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
| 7 | SPECIAL_TYPE_C | ZC_SPECIAL_TYPE | SPECIAL_TYPE_C | No | No | No |  |
| 8 | UNIT_C | ZC_UNIT_2 | UNIT_2_C | No | No | No |  |

_(32 total; showing first 30)_
