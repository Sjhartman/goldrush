# OR_PROC

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=OR_PROC

## Description

The OR_PROC table contains OR management system procedures.

**Primary table** in this group (101 cols). Overflow siblings joined on shared key: OR_PROC_2 (17 cols). Prefer this table for most queries.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | FULL |
| Load Frequency | WEEKLY - FULL |
| Chronicles INI | ORP |
| Release Version | MU1 - MAY 2001 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| OR_PROC_ID | VARCHAR (254) | The unique internal ID of the surgical procedure record. |
| PROC_NAME | VARCHAR (200) | The name of the surgical procedure record. |
| INACTIVE_YN | VARCHAR (1) |  |
| ABBREV | VARCHAR (16) | The abbreviation of the surgical procedure. |
| PROC_MOD_YN *(deprecated)* | VARCHAR (1) |  |
| USESETNGS_FROM_ID *(deprecated)* | VARCHAR (254) | *** Deprecated *** In table OR_PROC, the column USESETNGS_FROM_ID (ORP/70) has been deprecated. The deprecated column's data is no longer available since it is no longer populated in Chronicles. ****** The unique internal ID of the surgical procedure that this procedure is using settings from. |
| TYPE_OF_PROC_C | VARCHAR (66) |  |
| USE_CALC_TIMES_YN | VARCHAR (1) |  |
| START_BEFORE_TIME | DATETIME (Local) | The time at which this procedure much be scheduled before. |
| START_AFTER_TIME | DATETIME (Local) | The time at which this procedure must be scheduled after. |
| SETUP_LENGTH | INTEGER | The setup time in minutes required for this procedure. |
| CLEANUP_LENGTH | INTEGER | The cleanup time in minutes required for this procedure. |
| TIME_REQUIRED | INTEGER | The amount of time in minutes required for the procedure when it is not performed with any other procedures in the case. |
| TIME_REQ_MULTIPLE | INTEGER | The amount of time in minutes required for the procedure when it is performed along with other procedures in a case. |
| POSITION_C | INTEGER |  |
| LRB_C | INTEGER |  |
| OPERATING_REGION_C | INTEGER |  |
| PAT_HEAD_POS_C | INTEGER |  |
| RIGHT_ARM_POS_C | INTEGER |  |
| LEFT_ARM_POS_C | INTEGER |  |
| RIGHT_LEG_POS_C | INTEGER |  |
| LEFT_LEG_POS_C | INTEGER |  |
| ANESTHESIA_TYPE_C | INTEGER |  |
| CHARGE_CODE | VARCHAR (20) | The charge code associated with the procedure for billing purposes. |
| PICKLIST_ID | VARCHAR (18) | The unique internal ID of the pick list for this procedure. |
| MOD_MAX_AGE *(deprecated)* | INTEGER | *** Deprecated *** The deprecated column's data was never populated in Chronicles.  The maximum age modifier for the pick list. This item is not currently used. |
| MOD_MIN_AGE *(deprecated)* | INTEGER | *** Deprecated *** The deprecated column's data was never populated in Chronicles.  The minimum age modifier for the pick list. This item is not currently used. |
| MOD_SEX_NAME | INTEGER |  |
| MOD_MIN_AGE_NUM *(deprecated)* | INTEGER | *** Deprecated *** The deprecated column's data was never populated in Chronicles.  The minimum age modifier for the pick list. This item is not currently used. |
| MOD_MIN_AGE_NAME *(deprecated)* | INTEGER |  |
| MOD_MAX_AGE_NUM *(deprecated)* | INTEGER | *** Deprecated *** The deprecated column's data was never populated in Chronicles.  The maximum age modifier for the pick list. This item is not currently used. |
| MOD_MAX_AGE_NAME *(deprecated)* | INTEGER |  |
| MOD_SER_INDEX_ID *(deprecated)* | VARCHAR (18) |  |
| MOD_EAF_INDEX_ID *(deprecated)* | NUMERIC (18,0) |  |
| MOD_ORP_INDEX_ID *(deprecated)* | VARCHAR (254) |  |
| RECORD_CREATE_DATE | DATETIME | The date on which this procedure record was created. |
| REC_CREATE_USER_ID | VARCHAR (18) | The unique ID of the user who created this procedure record. |
| PATIENT_INST *(deprecated)* | VARCHAR (254) |  |
| PROC_DESC *(deprecated)* | VARCHAR (254) |  |
| PROC_NOTES *(deprecated)* | VARCHAR (254) |  |
| SCHED_INSTRS *(deprecated)* | VARCHAR (254) |  |
| XRAY_REQS *(deprecated)* | VARCHAR (254) |  |
| LAB_REQS *(deprecated)* | VARCHAR (254) |  |
| NURSING_NOTES *(deprecated)* | VARCHAR (254) |  |
| PREOP_PREP_NOTES *(deprecated)* | VARCHAR (254) |  |
| POSITION_NOTES *(deprecated)* | VARCHAR (254) |  |
| PRIMARY_EXT_ID | VARCHAR (30) | The primary external ID for this procedure. This is the ID which the user sees on displays within OR management system. |
| BASE_COST | NUMERIC (12,2) | The base cost for the procedure. |
| WOUND_CLASS_C | INTEGER |  |
| WOUND_LOC_C | INTEGER |  |
| PL_GEN_DEFAULT_C | INTEGER |  |
| PMODS_INDEX_1 *(deprecated)* | VARCHAR (40) |  |
| COST_TABLE_ID | NUMERIC (18,0) | The unique ID of the cost table associated with this procedure. |
| USE_AVG_STG_FRM_ID | VARCHAR (254) | The unique ID of the procedure record used as a source for time averaging settings. |
| CM_PHY_OWNER_ID | VARCHAR (25) | ID of the physical deployment owner for this record.  Physical owners will be where the data is hosted, either on the cross-over server or the owner deployment. |
| CM_LOG_OWNER_ID | VARCHAR (25) | ID of the logical deployment owner for this record.  Logical owners show the deployment where the record was created but doesn't represent if the record is a part of version skew. |
| PROC_LEVEL_C | INTEGER |  |
| MOD_SVC_INDEX_C *(deprecated)* | VARCHAR (66) |  |
| PMODS_ORP_SER_SVC *(deprecated)* | VARCHAR (91) | *** Deprecated *** The deprecated column's data is no longer available since it is no longer populated in Chronicles.  This index stores a string of the format "PROCEDURE_ID^SURGEON_ID^SERVICE_CATEGORY". |
| PMODS_ORP_EAF_SVC *(deprecated)* | VARCHAR (91) | *** Deprecated *** The deprecated column's data is no longer available since it is no longer populated in Chronicles.  This index stores a string of the format "PROCEDURE_ID^LOCATION_ID^SERVICE_CATEGORY". |
| CHARGE_CODE_ID | NUMERIC (18,0) | The charge code (EAP) id used to generate costs for the procedure. |
| RPT_GRP1_C | INTEGER |  |
| RPT_GRP2_C | INTEGER |  |
| RPT_GRP3_C | INTEGER |  |
| RPT_GRP4_C | INTEGER |  |
| RPT_GRP5_C | INTEGER |  |
| RPT_GRP6_C | INTEGER |  |
| RPT_GRP7_C | INTEGER |  |
| RPT_GRP8_C | INTEGER |  |
| RPT_GRP9_C | INTEGER |  |
| RPT_GRP10_C | INTEGER |  |
| RPT_GRP1_STR | VARCHAR (255) | Report Grouper for Single Response String value |
| RPT_GRP2_STR | VARCHAR (255) | Report Grouper for Single Response String value |
| RPT_GRP3_STR | VARCHAR (255) | Report Grouper for Single Response String value |
| RPT_GRP4_STR | VARCHAR (255) | Report Grouper for Single Response String value |
| RPT_GRP5_STR | VARCHAR (255) | Report Grouper for Single Response String value |
| RPT_GRP1_NUM | FLOAT | Report Grouper for Single Response Numeric value |
| RPT_GRP2_NUM | FLOAT | Report Grouper for Single Response Numeric value |
| RPT_GRP3_NUM | FLOAT | Report Grouper for Single Response Numeric value |
| RPT_GRP4_NUM | FLOAT | Report Grouper for Single Response Numeric value |
| RPT_GRP5_NUM | FLOAT | Report Grouper for Single Response Numeric value |
| CPT_BENEFITS_ID | NUMERIC (18,0) | This CPT(R) code will be used when calculating benefits related information for the procedure. |
| UPD_SURG_HIST_YN | VARCHAR (1) |  |
| SURG_HIST_PROC_ID | NUMERIC (18,0) | The procedure code that will be added to the patient's surgical history if the current procedure is performed on a patient. |
| REQ_IMP_YN | VARCHAR (1) |  |
| OR_BILLING_CAT_C | INTEGER |  |
| STUDY_ORDER_EAP_ID | NUMERIC (18,0) | Stores the EAP record that should be used as the type of study to result when this procedure is performed in a case. |
| REQ_OB_CONTACT_YN | VARCHAR (1) |  |
| LAPAROSCOPIC_YN | VARCHAR (1) |  |
| PRNT_PCK_YN | VARCHAR (1) |  |
| PREF_GROUP_ID *(deprecated)* | VARCHAR (254) | *** Deprecated *** In table OR_PROC, the column PREF_GROUP_ID (ORP/72) has been deprecated. The deprecated column's data is no longer available since it is no longer populated in Chronicles. ****** Specify the preference group that this procedure is a part of. If this is specified, the preference cards from the preference group will be used while scheduling. |
| AVG_LEN_FOR_BILL | INTEGER | This item stores average procedure length in minutes for billing purposes. Additional timing charges will be sent if surgery takes more time than specified in this item. |
| LAST_BCA_DATETIME | DATETIME (Local) | This item stores the instant when the preference card report was last sent to or removed from BCA. |
| LAST_BCA_ACTION_C | INTEGER |  |
| REC_TYP_C | INTEGER |  |
| ENDOSCOPIC_YN | VARCHAR (1) |  |
| COUNTS_NEEDED_YN | VARCHAR (1) |  |
| MIN_IMP_CHRG_EXPECT | NUMERIC (18,2) | The minimum amount of implant charges that are expected for the procedure when it is performed. |
| PAT_PREP_LENGTH | INTEGER | Patient preparation time for this procedure. This is the time from when the patient enters the room until the procedure starts. The patient preparation time in a surgical case is the highest of the patient preparation time for individual procedures. |
| PAT_CLOSING_LENGTH | INTEGER | Patient closing time for this procedure. This is the time from procedure stop until the patient leaves the room. The patient closing time in a surgical case is the highest of the patient preparation time for individual procedures. |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| B-TREE INDEX | EIX_OR_PROC_ANTYC | ANESTHESIA_TYPE_C | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_OR_PROC_CHCO | CHARGE_CODE | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_OR_PROC_COTAID | COST_TABLE_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_OR_PROC_INYN | INACTIVE_YN | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_OR_PROC_LEVELIND | PROC_LEVEL_C | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_OR_PROC_MOD_SVC | MOD_SVC_INDEX_C | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_OR_PROC_MOEAINID | MOD_EAF_INDEX_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_OR_PROC_MOORINID | MOD_ORP_INDEX_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_OR_PROC_MOSEINID | MOD_SER_INDEX_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_OR_PROC_ORP_CHARGE | CHARGE_CODE_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_OR_PROC_ORP_EAF_SVC | PMODS_ORP_EAF_SVC | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_OR_PROC_ORP_SER_SVC | PMODS_ORP_SER_SVC | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_OR_PROC_PIID | PICKLIST_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_OR_PROC_PREXID | PRIMARY_EXT_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_OR_PROC_PRMOYN | PROC_MOD_YN | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_OR_PROC_RECRUSID | REC_CREATE_USER_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_OR_PROC_TYOFPRC | TYPE_OF_PROC_C | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_OR_PROC_USAVSTFRID | USE_AVG_STG_FRM_ID | 1 | Yes | Yes |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | OR_PROC_ID | OR_PROC_2 | OR_PROC_ID | No | No | No |  |
| 1 | OR_PROC_ID | OR_PROC_CONSENT_CONFIG | PROC_ID | No | No | No |  |
| 7 | TYPE_OF_PROC_C | ZC_OR_TYPE_OF_PROC | TYPE_OF_PROC_C | No | No | No |  |
| 15 | POSITION_C | ZC_OR_POSITION | POSITION_C | No | No | No |  |
| 15 | POSITION_C | ZC_OR_POS_BODY | OR_POS_BODY_C | No | No | No |  |
| 16 | LRB_C | ZC_OR_LRB | LRB_C | No | No | No |  |
| 17 | OPERATING_REGION_C | ZC_OR_OP_REGION | OPERATING_REGION_C | No | No | No |  |
| 18 | PAT_HEAD_POS_C | ZC_OR_HEAD_POS | PAT_HEAD_POS_C | No | No | No |  |
| 18 | PAT_HEAD_POS_C | ZC_OR_POS_HEAD | OR_POS_HEAD_C | No | No | No |  |
| 19 | RIGHT_ARM_POS_C | ZC_OR_ARM_POS | RIGHT_ARM_POS_C | No | No | No |  |
| 19 | RIGHT_ARM_POS_C | ZC_OR_POS_LT_ARM | OR_POS_LT_ARM_C | No | No | No |  |
| 19 | RIGHT_ARM_POS_C | ZC_OR_POS_RT_ARM | OR_POS_RT_ARM_C | No | No | No |  |
| 20 | LEFT_ARM_POS_C | ZC_OR_ARM_POS | RIGHT_ARM_POS_C | No | No | No |  |
| 20 | LEFT_ARM_POS_C | ZC_OR_POS_LT_ARM | OR_POS_LT_ARM_C | No | No | No |  |
| 20 | LEFT_ARM_POS_C | ZC_OR_POS_RT_ARM | OR_POS_RT_ARM_C | No | No | No |  |
| 21 | RIGHT_LEG_POS_C | ZC_OR_LEG_POS | RIGHT_LEG_POS_C | No | No | No |  |
| 21 | RIGHT_LEG_POS_C | ZC_OR_POS_LT_LEG | OR_POS_LT_LEG_C | No | No | No |  |
| 21 | RIGHT_LEG_POS_C | ZC_OR_POS_RT_LEG | OR_POS_RT_LEG_C | No | No | No |  |
| 22 | LEFT_LEG_POS_C | ZC_OR_LEG_POS | RIGHT_LEG_POS_C | No | No | No |  |
| 22 | LEFT_LEG_POS_C | ZC_OR_POS_LT_LEG | OR_POS_LT_LEG_C | No | No | No |  |
| 22 | LEFT_LEG_POS_C | ZC_OR_POS_RT_LEG | OR_POS_RT_LEG_C | No | No | No |  |
| 23 | ANESTHESIA_TYPE_C | ZC_OR_ANESTH_TYPE | ANESTHESIA_TYPE_C | No | No | No |  |
| 25 | PICKLIST_ID | OR_PKLST | PICK_LIST_ID | No | No | No |  |
| 37 | REC_CREATE_USER_ID | CLARITY_EMP | USER_ID | Unknown | No | No |  |
| 37 | REC_CREATE_USER_ID | CLARITY_EMP_2 | USER_ID | Unknown | No | No |  |
| 37 | REC_CREATE_USER_ID | CLARITY_EMP_3 | USER_ID | Unknown | No | No |  |
| 37 | REC_CREATE_USER_ID | CLARITY_EMP_4 | USER_ID | No | No | No |  |
| 37 | REC_CREATE_USER_ID | CLARITY_EMP_DEMO | USER_ID | No | No | No |  |
| 37 | REC_CREATE_USER_ID | EMP_BASIC_INFO | USER_ID | No | No | No |  |
| 37 | REC_CREATE_USER_ID | EMP_DOC_SETTINGS | USER_NUMBER_ID | No | No | No |  |

_(99 total; showing first 30)_
