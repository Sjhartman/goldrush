# PAT_LIST_INFO

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=PAT_LIST_INFO

## Description

The PAT_LIST_INFO table contains the no-add, single response patient list information.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | FULL |
| Load Frequency | WEEKLY - FULL |
| Chronicles INI | ERS |
| Release Version | MU3 - EPIC 2002 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| LIST_ID | VARCHAR (18) | Unique Patient List ID |
| LIST_DESCRIPTION | VARCHAR (255) | Description of the patient list. |
| RECORD_STATUS_C | INTEGER |  |
| LIST_TYPE_C | INTEGER |  |
| MASTER_LIST_ID *(deprecated)* | VARCHAR (18) |  |
| LIST_SUBTYPE_C | INTEGER |  |
| LIST_OWNER | VARCHAR (12) | The owner of the patient list. |
| LIST_CREATOR_ID | VARCHAR (18) | The list creator or owner in gui system |
| DISPLAY_NAME | VARCHAR (255) | The name of the patient list as it is displayed in gui system |
| PDA_REPORT_ID *(deprecated)* | VARCHAR (18) | *** Deprecated ***  In table PAT_LIST_INFO, the column PDA_REPORT_ID (ERS/34100) has been deprecated. The deprecated column's content/data is no longer available since it is no longer populated in Chronicles.  The ID of the report to be displayed by default when you view a patient list downloaded to a PDA:  gui system only |
| DEFAULT_REPORT_ID | VARCHAR (18) | The ID of the report to be displayed in the Reports window when you select a list: GUI system only. |
| SYSTEM_LIST_YN *(deprecated)* | VARCHAR (1) |  |
| CM_PHY_OWNER_ID | VARCHAR (25) | ID of the physical deployment owner for this record.  Physical owners will be where the data is hosted, either on the cross-over server or the owner deployment. |
| CM_LOG_OWNER_ID | VARCHAR (25) | ID of the logical deployment owner for this record.  Logical owners show the deployment where the record was created but doesn't represent if the record is a part of version skew. |
| USE_COMP_SEC_YN | VARCHAR (1) |  |
| AVAIL_TO_ALL_YN | VARCHAR (1) |  |
| LOGIN_LIST_YN | VARCHAR (1) |  |
| LAST_PROP_MOD_DTTM | DATETIME (Local) | Instant of last property change. |
| LAST_ADDREM_DTTM | DATETIME (Local) | Instant of last add remove. |
| COL_HEAD_CHG *(deprecated)* | INTEGER | In table PAT_LIST_INFO, the column COL_HEAD_CHG (ERS-34055) has been deprecated. The deprecated column's data is no longer available since it is no longer populated in Chronicles. |
| SYSTEM_LIST_GRP_C | VARCHAR (66) |  |
| AUTO_MYLST_DISP_NAM | VARCHAR (255) | The display name which a My List is given when it is auto-created for a new user using this My List Template. This column is only populated for records of type "My List Template". |
| LINKED_TEMPLATE_ID | VARCHAR (18) | Stores the ID of the template that the My List was generated from. |
| LAST_SYNC_UPDT_DTTM | DATETIME (UTC) | For My Lists, stores the last time the list was synced to its template. For My List Templates, stores the last time the template was updated. |
| REMINDER_LIST_YN | VARCHAR (1) |  |
| SPR_RICH_FEAT_YN | VARCHAR (1) |  |
| PARENT_LIST_ID | VARCHAR (18) | Displays the ID of the parent list that created this list, if it is associated with a parent list. |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | LIST_ID | ERS_CUSTOM_FOLDER | LIST_ID | Unknown | No | No |  |
| 3 | RECORD_STATUS_C | ZC_DEL_STATUS | DEL_STATUS_C | No | No | No |  |
| 3 | RECORD_STATUS_C | ZC_EDG_REC_STAT | EDG_REC_STAT_C | No | No | No |  |
| 3 | RECORD_STATUS_C | ZC_ERS_REC_STAT | RECORD_STATUS_C | No | No | No |  |
| 3 | RECORD_STATUS_C | ZC_HCD_REC_STATE | HCD_REC_STATE_C | No | No | No |  |
| 3 | RECORD_STATUS_C | ZC_HFL_RECORD_STAT | HFL_RECORD_STAT_C | No | No | No |  |
| 3 | RECORD_STATUS_C | ZC_IMM_REC_STATUS | IMM_REC_STATUS_C | No | No | No |  |
| 3 | RECORD_STATUS_C | ZC_LLB_STATUS | LLB_STATUS_C | No | No | No |  |
| 3 | RECORD_STATUS_C | ZC_LMA_RECORD_STAT | LMA_RECORD_STAT_C | No | No | No |  |
| 3 | RECORD_STATUS_C | ZC_MEM_REC_STATUS | MEM_REC_STATUS_C | No | No | No |  |
| 3 | RECORD_STATUS_C | ZC_OR_REC_STATUS | OR_REC_STATUS_C | No | No | No |  |
| 3 | RECORD_STATUS_C | ZC_PBA_REC_STAT | PBA_REC_STAT_C | No | No | No |  |
| 3 | RECORD_STATUS_C | ZC_PROV_REC_STATE | PROV_REC_STATE_C | No | No | No |  |
| 3 | RECORD_STATUS_C | ZC_RECORD_STATE_2 | RECORD_STATE_2_C | No | No | No |  |
| 3 | RECORD_STATUS_C | ZC_RECORD_STATE_3 | RECORD_STATE_3_C | No | No | No |  |
| 3 | RECORD_STATUS_C | ZC_RECORD_STATE_4 | RECORD_STATE_4_C | No | No | No |  |
| 3 | RECORD_STATUS_C | ZC_RECORD_STATE_6 | RECORD_STATE_6_C | No | No | No |  |
| 3 | RECORD_STATUS_C | ZC_RECORD_STATE_7 | RECORD_STATE_7_C | No | No | No |  |
| 3 | RECORD_STATUS_C | ZC_RECORD_STAT_EPM | RECORD_STAT_EPM_C | No | No | No |  |
| 3 | RECORD_STATUS_C | ZC_RECORD_STAT_EPP | RECORD_STAT_EPP_C | No | No | No |  |
| 3 | RECORD_STATUS_C | ZC_RECORD_STAT_ETX | RECORD_STAT_ETX_C | No | No | No |  |
| 3 | RECORD_STATUS_C | ZC_RECORD_STAT_HRV | RECORD_STAT_HRV_C | No | No | No |  |
| 3 | RECORD_STATUS_C | ZC_RECORD_STAT_RMC | RECORD_STAT_RMC_C | No | No | No |  |
| 4 | LIST_TYPE_C | ZC_LIST_TYPE | LIST_TYPE_C | No | No | No |  |
| 6 | LIST_SUBTYPE_C | ZC_LIST_SUBTYPE | LIST_SUBTYPE_C | No | No | No |  |
| 8 | LIST_CREATOR_ID | CLARITY_EMP | USER_ID | Unknown | No | No |  |
| 8 | LIST_CREATOR_ID | CLARITY_EMP_2 | USER_ID | Unknown | No | No |  |
| 8 | LIST_CREATOR_ID | CLARITY_EMP_3 | USER_ID | Unknown | No | No |  |
| 8 | LIST_CREATOR_ID | CLARITY_EMP_4 | USER_ID | No | No | No |  |
| 8 | LIST_CREATOR_ID | CLARITY_EMP_DEMO | USER_ID | No | No | No |  |

_(51 total; showing first 30)_
