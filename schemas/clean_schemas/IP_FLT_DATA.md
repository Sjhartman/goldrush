# IP_FLT_DATA

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=IP_FLT_DATA

## Description

This table contains information related to defined flowsheet templates.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | FLT |
| Release Version | EPIC 2002 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| TEMPLATE_ID | VARCHAR (18) | The unique ID for the flowsheet template. |
| TEMPLATE_NAME | VARCHAR (192) | The name given to the template record. |
| DISPLAY_NAME | VARCHAR (192) | The display name associated with this template. |
| GROUP_COL_WIDTH | INTEGER | The width set for the data columns in this template. |
| NAME_COL_WIDTH | INTEGER | The width set for the name columns in this template. |
| TIME_INTERVAL | INTEGER | The time (in minutes) spanned by each column in the flowsheet when not in compact view. |
| CM_PHY_OWNER_ID | VARCHAR (25) | ID of the physical deployment owner for this record.  Physical owners will be where the data is hosted, either on the cross-over server or the owner deployment. |
| CM_LOG_OWNER_ID | VARCHAR (25) | ID of the logical deployment owner for this record.  Logical owners show the deployment where the record was created but doesn't represent if the record is a part of version skew. |
| REPORT_TEMPLATE_ID | VARCHAR (18) | FLT ID of reporting template |
| LINK_TEXT_LPP_ID | NUMERIC (18,0) | Summary Sentence Link Text LPP |
| LINK_REPORT_ID | VARCHAR (18) | Summary Sentence Report ID |
| FS_COL_START_TIME | DATETIME (Local) | Flowsheet start time column offset |
| RECORD_STATE_C | INTEGER |  |
| RESTRICT_ROWS_YN | VARCHAR (1) |  |
| MINS_HIDE_CASCADE | INTEGER | The time (in minutes) the Cascading Flowsheet window will be hidden from the user, even if trigger conditions are met. |
| PAT_ENTD_FLT_PRC_ID | NUMERIC (18,0) | Stores procedure ID so that when this procedure is ordered, flowsheet is also ordered for patients. This is used in MyChart. |
| PEF_ED_METH_C *(deprecated)* | INTEGER |  |
| PAT_ENTD_FLT_CMT_YN | VARCHAR (1) |  |
| PAT_ENTD_FLT_EDT_DA *(deprecated)* | INTEGER | *** Deprecated *** In table IP_FLT_DATA, the column  PAT_ENTD_FLT_EDT_DA (FLT/32020) has been deprecated.   The deprecated column's content/data is no longer available since it is no longer populated in Chronicles.  The number of days for which a patient can edit patient-entered flowsheet data. |
| PEF_FLBAR_YN | VARCHAR (1) |  |
| SINGLE_COLUMN_YN | VARCHAR (1) |  |
| TOOLBAR_NAME | VARCHAR (192) | The toolbar name associated with the flowsheet template. |
| ALLOW_ACCORDION_C | INTEGER |  |
| PAT_ENTD_FLT_NAME | VARCHAR (254) | This table contains the optional patient facing name used if this flowsheet template is being used for the Patient-Entered Flowsheets feature. |
| ALLOW_AVR_YN | VARCHAR (1) |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 7 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | CM_PHY_OWNER_ID | Unknown | Unknown | Yes |  |
| 7 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 7 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 7 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 8 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | CM_LOG_OWNER_ID | Unknown | Unknown | Yes |  |
| 8 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 8 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 8 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 9 | REPORT_TEMPLATE_ID | IP_FLT_DATA | TEMPLATE_ID | No | No | No |  |
| 10 | LINK_TEXT_LPP_ID | CLARITY_LPP | LPP_ID | Unknown | No | No |  |
| 11 | LINK_REPORT_ID | REPORT_DETAILS | LRP_ID | No | No | No |  |
| 13 | RECORD_STATE_C | ZC_DEL_STATUS | DEL_STATUS_C | No | No | No |  |
| 13 | RECORD_STATE_C | ZC_EDG_REC_STAT | EDG_REC_STAT_C | No | No | No |  |
| 13 | RECORD_STATE_C | ZC_ERS_REC_STAT | RECORD_STATUS_C | No | No | No |  |
| 13 | RECORD_STATE_C | ZC_HCD_REC_STATE | HCD_REC_STATE_C | No | No | No |  |
| 13 | RECORD_STATE_C | ZC_HFL_RECORD_STAT | HFL_RECORD_STAT_C | No | No | No |  |
| 13 | RECORD_STATE_C | ZC_IMM_REC_STATUS | IMM_REC_STATUS_C | No | No | No |  |
| 13 | RECORD_STATE_C | ZC_LLB_STATUS | LLB_STATUS_C | No | No | No |  |
| 13 | RECORD_STATE_C | ZC_LMA_RECORD_STAT | LMA_RECORD_STAT_C | No | No | No |  |
| 13 | RECORD_STATE_C | ZC_MEM_REC_STATUS | MEM_REC_STATUS_C | No | No | No |  |
| 13 | RECORD_STATE_C | ZC_OR_REC_STATUS | OR_REC_STATUS_C | No | No | No |  |
| 13 | RECORD_STATE_C | ZC_PBA_REC_STAT | PBA_REC_STAT_C | No | No | No |  |
| 13 | RECORD_STATE_C | ZC_PROV_REC_STATE | PROV_REC_STATE_C | No | No | No |  |
| 13 | RECORD_STATE_C | ZC_RECORD_STATE_2 | RECORD_STATE_2_C | No | No | No |  |
| 13 | RECORD_STATE_C | ZC_RECORD_STATE_3 | RECORD_STATE_3_C | No | No | No |  |
| 13 | RECORD_STATE_C | ZC_RECORD_STATE_4 | RECORD_STATE_4_C | No | No | No |  |
| 13 | RECORD_STATE_C | ZC_RECORD_STATE_6 | RECORD_STATE_6_C | No | No | No |  |
| 13 | RECORD_STATE_C | ZC_RECORD_STATE_7 | RECORD_STATE_7_C | No | No | No |  |
| 13 | RECORD_STATE_C | ZC_RECORD_STAT_EPM | RECORD_STAT_EPM_C | No | No | No |  |
| 13 | RECORD_STATE_C | ZC_RECORD_STAT_EPP | RECORD_STAT_EPP_C | No | No | No |  |

_(43 total; showing first 30)_
