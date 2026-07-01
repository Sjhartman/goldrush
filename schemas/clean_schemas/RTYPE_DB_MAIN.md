# RTYPE_DB_MAIN

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=RTYPE_DB_MAIN

## Description

The RTYPE_DB_MAIN table contains information for result type records.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | FULL |
| Load Frequency | WEEKLY - FULL |
| Chronicles INI | OVG |
| Release Version | SPRING 2006 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| RESULT_TYPE_ID | VARCHAR (18) | The unique ID of the result type record. |
| TYPE_OF_DATA_C | INTEGER |  |
| RTM_DFLT_MNEM_PR_ID | VARCHAR (18) | This is the default mnemonic preview report. |
| RESULT_TYPE_NAME | VARCHAR (254) | This is the name of the Result Type record - item OVG .2. |
| TYPE_OF_RES_TYP_C | INTEGER |  |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this Chronicles record. This is populated only if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this Chronicles record was extracted. This is populated only if you use IntraConnect. |
| PREVENT_TAB_RR_YN | VARCHAR (18) |  |
| SHARE_RES_YN | VARCHAR (1) |  |
| STATUS_C | INTEGER |  |
| RECORD_DELETED_C | INTEGER |  |
| DISCRETE_POSITION_C | INTEGER |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | RESULT_TYPE_ID | RTYPE_OT_MISC | RESULT_TYPE_ID | Unknown | No | No |  |
| 2 | TYPE_OF_DATA_C | ZC_TYPE_OF_DATA | TYPE_OF_DATA_C | No | No | No |  |
| 3 | RTM_DFLT_MNEM_PR_ID | REPORT_DETAILS | LRP_ID | No | No | No |  |
| 5 | TYPE_OF_RES_TYP_C | ZC_TYPE_OF_RES_TYP | TYPE_OF_RES_TYP_C | No | No | No |  |
| 6 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 6 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 6 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 7 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 7 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 7 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 10 | STATUS_C | ZC_RTYPE_STAT_CAT | STATUS_CAT_C | No | No | No |  |
| 11 | RECORD_DELETED_C | ZC_DEL_STATUS | DEL_STATUS_C | No | No | No |  |
| 11 | RECORD_DELETED_C | ZC_EDG_REC_STAT | EDG_REC_STAT_C | No | No | No |  |
| 11 | RECORD_DELETED_C | ZC_ERS_REC_STAT | RECORD_STATUS_C | No | No | No |  |
| 11 | RECORD_DELETED_C | ZC_HCD_REC_STATE | HCD_REC_STATE_C | No | No | No |  |
| 11 | RECORD_DELETED_C | ZC_HFL_RECORD_STAT | HFL_RECORD_STAT_C | No | No | No |  |
| 11 | RECORD_DELETED_C | ZC_IMM_REC_STATUS | IMM_REC_STATUS_C | No | No | No |  |
| 11 | RECORD_DELETED_C | ZC_LLB_STATUS | LLB_STATUS_C | No | No | No |  |
| 11 | RECORD_DELETED_C | ZC_LMA_RECORD_STAT | LMA_RECORD_STAT_C | No | No | No |  |
| 11 | RECORD_DELETED_C | ZC_MEM_REC_STATUS | MEM_REC_STATUS_C | No | No | No |  |
| 11 | RECORD_DELETED_C | ZC_OR_REC_STATUS | OR_REC_STATUS_C | No | No | No |  |
| 11 | RECORD_DELETED_C | ZC_PBA_REC_STAT | PBA_REC_STAT_C | No | No | No |  |
| 11 | RECORD_DELETED_C | ZC_PROV_REC_STATE | PROV_REC_STATE_C | No | No | No |  |
| 11 | RECORD_DELETED_C | ZC_RECORD_STATE_2 | RECORD_STATE_2_C | No | No | No |  |
| 11 | RECORD_DELETED_C | ZC_RECORD_STATE_3 | RECORD_STATE_3_C | No | No | No |  |
| 11 | RECORD_DELETED_C | ZC_RECORD_STATE_4 | RECORD_STATE_4_C | No | No | No |  |
| 11 | RECORD_DELETED_C | ZC_RECORD_STATE_6 | RECORD_STATE_6_C | No | No | No |  |
| 11 | RECORD_DELETED_C | ZC_RECORD_STATE_7 | RECORD_STATE_7_C | No | No | No |  |
| 11 | RECORD_DELETED_C | ZC_RECORD_STAT_EPM | RECORD_STAT_EPM_C | No | No | No |  |
| 11 | RECORD_DELETED_C | ZC_RECORD_STAT_EPP | RECORD_STAT_EPP_C | No | No | No |  |

_(34 total; showing first 30)_
