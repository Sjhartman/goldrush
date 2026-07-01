# IP_FLO_GP_DATA

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=IP_FLO_GP_DATA

## Description

This table contains generic information about flowsheet groups/rows.

**Primary table** in this group (102 cols). Overflow siblings joined on shared key: IP_FLO_GP_DATA_2 (21 cols). Prefer this table for most queries.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | FLO |
| Release Version | EPIC 2002 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| FLO_MEAS_ID | VARCHAR (18) | The unique ID of the flowsheet group/row. |
| FLO_MEAS_NAME | VARCHAR (254) | The name given to the flowsheet group/row. |
| FLO_DIS_NAME *(deprecated)* | VARCHAR (254) |  |
| FLO_ROW_NAME *(deprecated)* | VARCHAR (256) |  |
| VALUE_TYPE_NAME *(deprecated)* | VARCHAR (50) |  |
| MIN_VALUE *(deprecated)* | NUMERIC (18,5) |  |
| MAX_VALUE *(deprecated)* | NUMERIC (18,5) |  |
| UNIT *(deprecated)* | VARCHAR (254) |  |
| MULTI_SELECT_YN *(deprecated)* | VARCHAR (1) |  |
| PREF_FLO_MEAS_ID *(deprecated)* | VARCHAR (18) |  |
| DESCRIPTION *(deprecated)* | VARCHAR (428) |  |
| DEF_MIN_WARN_VAL *(deprecated)* | NUMERIC (18,5) |  |
| DEF_MAX_WARN_VAL *(deprecated)* | NUMERIC (18,5) |  |
| BKGROUND_COLOR_C *(deprecated)* | INTEGER |  |
| CUSTOM_FORMULA *(deprecated)* | VARCHAR (2048) |  |
| INTAKE_TYPE_C *(deprecated)* | INTEGER |  |
| OUTPUT_TYPE_C *(deprecated)* | INTEGER |  |
| DUPLICATABLE_YN *(deprecated)* | VARCHAR (1) |  |
| CM_PHY_OWNER_ID | VARCHAR (25) | ID of the physical deployment owner for this record.  Physical owners will be where the data is hosted, either on the cross-over server or the owner deployment. |
| CM_LOG_OWNER_ID | VARCHAR (25) | ID of the logical deployment owner for this record.  Logical owners show the deployment where the record was created but don't represent if the record is a part of version skew. |
| FLO_ADMIN_GRP_C *(deprecated)* | INTEGER |  |
| FLO_MED_UNIT_C *(deprecated)* | INTEGER |  |
| LDA_PROPERTIES_ID *(deprecated)* | VARCHAR (18) |  |
| LDA_ASSOC_LUMEN_C *(deprecated)* | INTEGER |  |
| SITE_ROW_ID | VARCHAR (18) | This item stores the row ID of the site row that is used for the Line/Drain/Airway group. |
| RECORD_STATE_C | INTEGER |  |
| LOGICAL_OWNER | VARCHAR (25) | ID of the logical deployment owner for this record.  Logical owners show the deployment where the record was created but don't represent if the record is a part of version skew. |
| PHYSICAL_OWNER | VARCHAR (25) | ID of the physical deployment owner for this record.  Physical owners will be where the data is hosted, either on the cross-over server or the owner deployment. |
| IS_RELEASE_FLAG_YN *(deprecated)* | VARCHAR (1) |  |
| ALLOW_COMPLETE_YN *(deprecated)* | VARCHAR (1) |  |
| ABBREVIATION *(deprecated)* | VARCHAR (6) |  |
| CHG_TRIG_TYPE_C *(deprecated)* | INTEGER |  |
| COPY_FORWARD_YN *(deprecated)* | VARCHAR (1) |  |
| MIN_DIA_BP *(deprecated)* | INTEGER |  |
| MAX_DIA_BP *(deprecated)* | INTEGER |  |
| CUSTOM_LIST_PP_ID *(deprecated)* | NUMERIC (18,0) |  |
| IS_HOW_ABBR_YN *(deprecated)* | VARCHAR (1) |  |
| MIN_WARN_VAL_DIABP *(deprecated)* | INTEGER |  |
| MAX_WARN_VAL_DIABP *(deprecated)* | INTEGER |  |
| DECIMAL_PLACES *(deprecated)* | INTEGER |  |
| AFTER_FILE_PT_ID *(deprecated)* | NUMERIC (18,0) |  |
| CATEGORY_INI *(deprecated)* | VARCHAR (3) |  |
| CATEGORY_ITEM *(deprecated)* | VARCHAR (254) |  |
| SUMMARY_METHOD_C *(deprecated)* | INTEGER |  |
| PROG_POINT_ID *(deprecated)* | NUMERIC (18,0) |  |
| CHG_PROC_ID *(deprecated)* | NUMERIC (18,0) |  |
| CHG_QTY_TYPE_C *(deprecated)* | INTEGER |  |
| CHG_SPEC_VAL *(deprecated)* | INTEGER |  |
| CHG_QTY_ROW_ID *(deprecated)* | VARCHAR (18) |  |
| CHG_PROC_ON_ID *(deprecated)* | NUMERIC (18,0) |  |
| CHG_PROC_OFF_ID *(deprecated)* | NUMERIC (18,0) |  |
| CONT_SHOW_LINE_YN *(deprecated)* | INTEGER |  |
| ALLOW_COMP_YN | VARCHAR (1) |  |
| DISP_NAME | VARCHAR (1000) | The display name given to the flowsheet group/row. |
| ABBR_P | VARCHAR (6) | This item holds the six character abbreviation for this row. |
| ROW_TYP_C | INTEGER |  |
| CHG_TRG_TYPE_C | INTEGER |  |
| VAL_TYPE_C | INTEGER |  |
| CPY_FWD_YN | VARCHAR (1) |  |
| UNITS | VARCHAR (254) | This determines the units that will display with the value in the additional information window. |
| MULTI_SEL_YN | VARCHAR (1) |  |
| SHOW_ABBR_YN *(deprecated)* | VARCHAR (1) |  |
| DISPLAY_ALLLIST_YN *(deprecated)* | INTEGER |  |
| INTAKE_TYP_C | INTEGER |  |
| OUTPUT_TYP_C | INTEGER |  |
| DUPLICATEABLE_YN | VARCHAR (1) |  |
| AFTER_FILE_LPP_ID | NUMERIC (18,0) | This is the programming point you would like called when data is filed for this row. |
| CAT_INI | VARCHAR (3) | This is the INI which contains the item that stores the category list. |
| CAT_ITEM | VARCHAR (20) | This is the item number in the INI which stores the category list. |
| CHG_ROW_QTY_TYPE_C | INTEGER |  |
| CHG_ROW_QTY_ROW_ID | VARCHAR (18) | This is the row ID that will be used to enter the quantity value for the charge trigger for this row. |
| REPORT_ID *(deprecated)* | VARCHAR (18) | *** Deprecated *** In table IP_FLO_GP_DATA, the column REPORT_ID (FLO 895) has been deprecated.  The deprecated column's content/data is no longer available since it is no longer populated in Chronicles.  This is the report that will be seen in the Doc Flowsheet activity in Hyperspace when the user is in this flowsheet row/group and the "Details" report is viewed. |
| MYCHART_CALC_C | INTEGER |  |
| CAN_BE_GRAPHED_YN | VARCHAR (1) |  |
| MINVALUE | INTEGER | The minimum value allowed in this row. |
| MIN_DIASTOLIC_BP | INTEGER | This item holds the minimum value allowed for the diastolic value of blood pressure. |
| MAX_VAL | INTEGER | The maximum value allowed in this row. |
| MAX_DIASTOLIC_BP | INTEGER | This item holds the maximum value allowed for the diastolic value of the blood pressure. |
| MIN_WARN_VAL | INTEGER | The minimum value allowed before an entry is marked with a warning flag. |
| MIN_WARN_DIA_BP | INTEGER | This item holds the minimum warning value for the diastolic blood pressure value. |
| MAX_WARN_VAL | INTEGER | The maximum value allowed before an entry is marked with a warning flag. |
| MAX_WARN_DIA_BP | INTEGER | This item holds the maximum warning blood pressure value. |
| GRAPH_COLOR_C | INTEGER |  |
| GRAPH_COLOR_DIA_C | INTEGER |  |
| GRAPH_ICON_C | VARCHAR (66) |  |
| GRAPH_ICON_DIA_C | VARCHAR (66) |  |
| IP_FLO_REPORT_ID *(deprecated)* | VARCHAR (18) |  |
| MYC_CALC_IDNT_C *(deprecated)* | INTEGER |  |
| IP_CUSTLST_GRPH_YN *(deprecated)* | VARCHAR (1) |  |
| IP_VOLUME_ROW_ID *(deprecated)* | VARCHAR (18) |  |
| INST_NOADD_EDIT | DATETIME (Local) | This is the instant of a flowsheet edit. |
| NOADD_ITEMS_EDITED | VARCHAR (1000) | This holds the items edited last. |
| CASCADE_LOGIC *(deprecated)* | VARCHAR (254) | This item is the compiled cascading condition. |
| ADD_START_REMOVE_YN | VARCHAR (1) |  |
| IO_OCC_YN | VARCHAR (1) |  |
| FLO_ROW_STATUS_C | INTEGER |  |
| MIN_AGE | INTEGER | This item determines the minimum age to display the row. |
| MAX_AGE | INTEGER | This determines the maximum age to display the row. |
| SEX_C | VARCHAR (66) |  |
| TASK_TEMPLATE_ID | VARCHAR (18) | This is the Task Template (LTT) record that will fire upon adding Doc Flowsheet groups, rows, and LDAs to a patient's encounter. Task Template records can create Task records to be used on the Work List or as auto-completing "due" reminders of clinical documentation that needs to be done by a certain time or at some scheduled interval. Task Template records can also be used to build clinical documentation (Doc Flowsheet rows, Patient Education records, etc.) into a patient's encounter. |
| DISPLAY_ALL_LIST_YN | VARCHAR (1) | Surrogate key used to uniquely identify rows in this (and only this) table on Cogito Cloud only, do not assume the surrogate key in this table will correspond to the surrogate key in another table |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | FLO_MEAS_ID | FLO_CNTX_INFO | ID | No | No | No |  |
| 1 | FLO_MEAS_ID | IP_FLO_GP_DATA_2 | FLO_MEAS_ID | No | No | No |  |
| 19 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | CM_PHY_OWNER_ID | Unknown | Unknown | Yes |  |
| 19 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 19 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 19 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 20 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | CM_LOG_OWNER_ID | Unknown | Unknown | Yes |  |
| 20 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 20 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 20 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 25 | SITE_ROW_ID | FLO_CNTX_INFO | ID | No | No | No |  |
| 25 | SITE_ROW_ID | IP_FLO_GP_DATA | FLO_MEAS_ID | No | No | No |  |
| 25 | SITE_ROW_ID | IP_FLO_GP_DATA_2 | FLO_MEAS_ID | No | No | No |  |
| 26 | RECORD_STATE_C | ZC_DEL_STATUS | DEL_STATUS_C | No | No | No |  |
| 26 | RECORD_STATE_C | ZC_EDG_REC_STAT | EDG_REC_STAT_C | No | No | No |  |
| 26 | RECORD_STATE_C | ZC_ERS_REC_STAT | RECORD_STATUS_C | No | No | No |  |
| 26 | RECORD_STATE_C | ZC_HCD_REC_STATE | HCD_REC_STATE_C | No | No | No |  |
| 26 | RECORD_STATE_C | ZC_HFL_RECORD_STAT | HFL_RECORD_STAT_C | No | No | No |  |
| 26 | RECORD_STATE_C | ZC_IMM_REC_STATUS | IMM_REC_STATUS_C | No | No | No |  |
| 26 | RECORD_STATE_C | ZC_LLB_STATUS | LLB_STATUS_C | No | No | No |  |
| 26 | RECORD_STATE_C | ZC_LMA_RECORD_STAT | LMA_RECORD_STAT_C | No | No | No |  |
| 26 | RECORD_STATE_C | ZC_MEM_REC_STATUS | MEM_REC_STATUS_C | No | No | No |  |
| 26 | RECORD_STATE_C | ZC_OR_REC_STATUS | OR_REC_STATUS_C | No | No | No |  |
| 26 | RECORD_STATE_C | ZC_PBA_REC_STAT | PBA_REC_STAT_C | No | No | No |  |
| 26 | RECORD_STATE_C | ZC_PROV_REC_STATE | PROV_REC_STATE_C | No | No | No |  |
| 26 | RECORD_STATE_C | ZC_RECORD_STATE_2 | RECORD_STATE_2_C | No | No | No |  |
| 26 | RECORD_STATE_C | ZC_RECORD_STATE_3 | RECORD_STATE_3_C | No | No | No |  |
| 26 | RECORD_STATE_C | ZC_RECORD_STATE_4 | RECORD_STATE_4_C | No | No | No |  |
| 26 | RECORD_STATE_C | ZC_RECORD_STATE_6 | RECORD_STATE_6_C | No | No | No |  |
| 26 | RECORD_STATE_C | ZC_RECORD_STATE_7 | RECORD_STATE_7_C | No | No | No |  |

_(60 total; showing first 30)_
