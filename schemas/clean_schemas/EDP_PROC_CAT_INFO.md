# EDP_PROC_CAT_INFO

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=EDP_PROC_CAT_INFO

## Description

This table contains information about procedure categories. Procedure categories are used to group together related procedures, such as all GI orderable procedures.

**Primary table** in this group (101 cols). Overflow siblings joined on shared key: EDP_PROC_CAT_INF_2 (51 cols). Prefer this table for most queries.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | FULL |
| Load Frequency | WEEKLY - FULL |
| Chronicles INI | EDP |
| Release Version | Summer 2009 |
| May contain EHI? | No |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| PROC_CAT_ID | VARCHAR (254) | The unique ID of the procedure category record for this row. |
| SCHED_FOR_OUTPAT_YN | VARCHAR (1) |  |
| USE_VT_SPEC_REST_C | INTEGER |  |
| PROMPT_FOR_VT_YN | VARCHAR (1) |  |
| MAMMO_RELATED_YN | VARCHAR (1) |  |
| PROC_CAT_NAME | VARCHAR (200) | The name of this procedure category. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| STATUS_C | INTEGER |  |
| ABBR | VARCHAR (50) | The abbreviation for this procedure category. |
| GL_NUM_DEBIT | VARCHAR (127) | The debit General Ledger number for this procedure category. |
| DEBIT_GL_TYPE_C | VARCHAR (66) |  |
| GL_NUM_CREDIT | VARCHAR (127) | The credit General Ledger number for this procedure category. |
| CREDIT_GL_TYPE_C | VARCHAR (66) |  |
| EXCISE_TAX_YN | VARCHAR (1) |  |
| PRICE_CHANGE_DATE | DATETIME | The price change date for this procedure category. |
| BILLING_CAT_C | VARCHAR (66) |  |
| ORDER_TYPE_C | INTEGER |  |
| NORMAL_DROP_YN | VARCHAR (1) |  |
| REF_DROP_YN | VARCHAR (1) |  |
| FUTURE_DROP_YN | VARCHAR (1) |  |
| DEF_ORDER_CLASS_C | VARCHAR (66) |  |
| RFL_DEF_DEP_ID | NUMERIC (18,0) | The default referral department for this procedure category. |
| RFL_DEF_DEP_SPEC_C | VARCHAR (66) |  |
| PROV_ADDR_PPT_ID | NUMERIC (18,0) | The referral provider address Programming Point for this procedure category. |
| RFL_DEF_TYPE_C | VARCHAR (66) |  |
| RFL_DEF_REASON_C | VARCHAR (66) |  |
| RFL_DEF_NUM_VISITS | INTEGER | The default referral number of visits for this procedure category. |
| RFL_DEF_EXP_DATE | VARCHAR (100) | The default referral expiration date for this procedure category. |
| RFL_SCHED_BY_DATE | VARCHAR (100) | The default referral schedule date for this procedure category. |
| RFL_DEF_PROV_SPC_C | VARCHAR (66) |  |
| RFL_DEF_LOC_ID | NUMERIC (18,0) | The default referral location for this procedure category. |
| OVR_RES_OVR_NORM | INTEGER | Orderdue result override for normal orders for this procedure category. |
| OVR_RES_OVR_REF | INTEGER | Orderdue result override for referrals for this procedure category. |
| OVR_RES_OVR_FUT | INTEGER | Orderdue result override for future orders for this procedure category. |
| LPP_FOR_NORM | VARCHAR (100) | Programming point used for normal orders for this procedure category. |
| LPP_FOR_REF | VARCHAR (100) | Programming point used for referrals for this procedure category. |
| LPP_FOR_FUT | VARCHAR (100) | Programming point used for future orders for this procedure category. |
| CAT_STATUS_C | INTEGER |  |
| EXPECTED_DATE | VARCHAR (100) | The expected date of the procedure when the default procedure status is future. |
| DATE_APPROX_YN | VARCHAR (1) |  |
| EXP_DATE | VARCHAR (100) | The expiration date for this procedure category. |
| REL_TYPE_C | INTEGER |  |
| REL_INTERVAL_C | VARCHAR (66) |  |
| REL_COUNT | INTEGER | The release count for this procedure category. |
| MAX_ORDERABLE | INTEGER | Maximum quantity that can be ordered for this procedure category. |
| SHOW_ORD_DET_C | INTEGER |  |
| OP_DETAIL_DESC | VARCHAR (254) | The outpatient detail screen description for this procedure category. |
| IP_DETAIL_DESC | VARCHAR (254) | The inpatient detail screen description for this procedure category. |
| OP_DUP_INTRVL | NUMERIC (10,4) | Stores the converted duplicate check interval, in hours, from column OP_DUP_INTRVL_STR. |
| OP_DUP_INTRVL_STR | VARCHAR (80) | The lookback time for duplicate checking in outpatient. |
| IP_DUP_INTRVL | NUMERIC (10,4) | Stores the converted duplicate check interval, in hours, from column IP_DUP_INTRVL_STR. |
| IP_DUP_INTRVL_STR | VARCHAR (80) | The lookback time for duplicate checking in inpatient. |
| REPORT_PPT_ID | NUMERIC (18,0) | The programming point used to generate a report for this procedure category in inpatient. |
| OP_REPORT_PPT_ID | NUMERIC (18,0) | The programming point used to generate a report for this procedure category in outpatient. |
| SCHED_GROUPER_C | INTEGER |  |
| SILENT_SCHEDULE_C | INTEGER |  |
| SIL_SCHED_PRV_ID | VARCHAR (18) | The silent schedule provider for this procedure category. |
| SIL_SCHED_DEP_ID | NUMERIC (18,0) | The silent schedule department for this procedure category. |
| SIL_SCHED_LPP_ID | NUMERIC (18,0) | The silent schedule programming point for this procedure category. |
| PROC_CAT_COMB_YN | VARCHAR (1) |  |
| MAX_DURATION | INTEGER | Maximum allowed duration for this procedure category. |
| DEF_STAND_INTVL_ID | VARCHAR (18) | The default interval or frequency of occurrence for this procedure category. |
| DEF_STAND_COUNT | INTEGER | The default standing order count for this procedure category when it is placed as a standing order. |
| IP_COUNT_TYPE_C | INTEGER |  |
| DEF_TIME_PRI_C | VARCHAR (18) |  |
| FILTER_TYPE_C | INTEGER |  |
| IP_DEF_ORD_CLS_C | VARCHAR (66) |  |
| OP_DEF_PRIORITY_C | INTEGER |  |
| IP_DEF_PRIORITY_C | INTEGER |  |
| DAYS_AFT_ST_DT | INTEGER | Order review notification configuration for this procedure category.. |
| UNIT_AFT_ST_DT_C | INTEGER |  |
| DAYS_BEF_END_DT | INTEGER | Expiring Orders configuration for this procedure category. |
| UNIT_BEF_END_DT_C | INTEGER |  |
| USE_EXPIRING_YN | VARCHAR (1) |  |
| REV_ONLY_ONCE_YN | VARCHAR (1) |  |
| TASK_TEMPL_ID | VARCHAR (18) | The Task Template associated with this procedure category. |
| BGN_AFTQNR_LPP_ID | NUMERIC (18,0) | The programming point record triggered after Imaging Order Questionnaire answers are saved during begin exam. |
| END_AFTQNR_LPP_ID | NUMERIC (18,0) | The programming point record triggered after Imaging Order Questionnaire answers are saved during end exam. |
| NOTE_TEMPLATE_ID *(deprecated)* | VARCHAR (18) | *** Deprecated *** In table EDP_PROC_CAT_INFO, the column NOTE_TEMPLATE_ID (EDP/52009) has been deprecated. The deprecated column's content/data is no longer available since it is no longer populated in Chronicles.  Note writer template to be used for the procedure category. |
| STUDY_ADV_ACT_ID | NUMERIC (18,0) | The advantage activity for Study Review for the procedure category. |
| TRANS_ADV_ACT_ID | NUMERIC (18,0) | The advantage activity for Transcription Entry for the procedure category. |
| REV_RES_ADV_ACT_ID | NUMERIC (18,0) | The advantage activity for Revise Results. This will override the settings at the department and the system level. This can be overriden at the procedure level. |
| TCH_VN_PX_TOPIC | VARCHAR (192) | Tech navigator procedure topic for this procedure category. |
| TECH_VN_BE_PX_TP_ID | NUMERIC (18,0) | Begin Exam navigator procedure level topic for this procedure category. |
| BILLPROV_OVR_LPP_ID *(deprecated)* | NUMERIC (18,0) | *** Deprecated *** {Item has been discontinued due to lack of use/need.}  Stores the procedure category level billing provider override programming point. |
| CTL_SHEET_ROUTINE | VARCHAR (254) | Control sheet routine for the procedure category. |
| RIS_RES_CODE_LBL | VARCHAR (30) | Replaces the "Result Code" field label in Study Review with a different value for the procedure category. |
| RES_CODE_REQ_YN | VARCHAR (1) |  |
| REL_PRI_CONFIG_ID | NUMERIC (18,0) | The relevant priors configuration for the procedure category level. |
| RIS_SIGNAGAIN_R_YN | VARCHAR (1) |  |
| PRINT_LET_SIGN_YN | VARCHAR (1) |  |
| OB_US_QUICKFORM_ID | VARCHAR (18) | The form that will be used on the findings tab of the OB Ultrasound entry activity. |
| OB_US_MOM_FORM_ID | VARCHAR (18) | The form that will display for baby-specific findings when the user reads and interprets this procedure category as part of Ultrasound Reporting. |
| MODALITY_TYPE_C | INTEGER |  |
| HIDE_IN_RSLT_REV_YN | VARCHAR (1) |  |
| SUM_FINDING_TGT_ID | NUMERIC (18,0) | Text generation template to use for this orderable procedure in Study Review's Summary Statement control. |
| PROTOCOL_GROUPER_C | INTEGER |  |
| PRI_PHYS_SIG_REQ_YN | VARCHAR (1) |  |
| PRIOR_STAT_CONFIG_C | INTEGER |  |
| HIDE_VAR_RSLT_REV_YN | VARCHAR (1) |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | PROC_CAT_ID | EDP_FILM_DATA | PROC_CAT_ID | Unknown | No | No |  |
| 1 | PROC_CAT_ID | EDP_PROC_CAT_INF_2 | PROC_CAT_ID | Unknown | No | No |  |
| 3 | USE_VT_SPEC_REST_C | ZC_USE_VT_SPEC_RES | USE_VT_SPEC_RES_C | No | No | No |  |
| 7 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 7 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 7 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 8 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 8 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 8 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 9 | STATUS_C | ZC_DEL_STATUS | DEL_STATUS_C | No | No | No |  |
| 9 | STATUS_C | ZC_EDG_REC_STAT | EDG_REC_STAT_C | No | No | No |  |
| 9 | STATUS_C | ZC_ERS_REC_STAT | RECORD_STATUS_C | No | No | No |  |
| 9 | STATUS_C | ZC_HCD_REC_STATE | HCD_REC_STATE_C | No | No | No |  |
| 9 | STATUS_C | ZC_HFL_RECORD_STAT | HFL_RECORD_STAT_C | No | No | No |  |
| 9 | STATUS_C | ZC_IMM_REC_STATUS | IMM_REC_STATUS_C | No | No | No |  |
| 9 | STATUS_C | ZC_LLB_STATUS | LLB_STATUS_C | No | No | No |  |
| 9 | STATUS_C | ZC_LMA_RECORD_STAT | LMA_RECORD_STAT_C | No | No | No |  |
| 9 | STATUS_C | ZC_MEM_REC_STATUS | MEM_REC_STATUS_C | No | No | No |  |
| 9 | STATUS_C | ZC_OR_REC_STATUS | OR_REC_STATUS_C | No | No | No |  |
| 9 | STATUS_C | ZC_PBA_REC_STAT | PBA_REC_STAT_C | No | No | No |  |
| 9 | STATUS_C | ZC_PROV_REC_STATE | PROV_REC_STATE_C | No | No | No |  |
| 9 | STATUS_C | ZC_RECORD_STATE_2 | RECORD_STATE_2_C | No | No | No |  |
| 9 | STATUS_C | ZC_RECORD_STATE_3 | RECORD_STATE_3_C | No | No | No |  |
| 9 | STATUS_C | ZC_RECORD_STATE_4 | RECORD_STATE_4_C | No | No | No |  |
| 9 | STATUS_C | ZC_RECORD_STATE_6 | RECORD_STATE_6_C | No | No | No |  |
| 9 | STATUS_C | ZC_RECORD_STATE_7 | RECORD_STATE_7_C | No | No | No |  |
| 9 | STATUS_C | ZC_RECORD_STAT_EPM | RECORD_STAT_EPM_C | No | No | No |  |
| 9 | STATUS_C | ZC_RECORD_STAT_EPP | RECORD_STAT_EPP_C | No | No | No |  |
| 9 | STATUS_C | ZC_RECORD_STAT_ETX | RECORD_STAT_ETX_C | No | No | No |  |
| 9 | STATUS_C | ZC_RECORD_STAT_HRV | RECORD_STAT_HRV_C | No | No | No |  |

_(177 total; showing first 30)_
