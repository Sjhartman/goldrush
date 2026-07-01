# PATIENT_3

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=PATIENT_3

## Description

This table supplements the information contained in the PATIENT table. It contains basic information about patients, such as the patient's ID, occupation, English fluency, etc.

**Overflow table** for PATIENT (137 cols). Contains additional columns for the same records — join on the shared primary key column.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | EPT |
| Release Version | Summer 2009 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| PAT_ID | VARCHAR (18) | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| LACT_STAT_CUR_C | INTEGER |  |
| LACT_STAT_INST_DTTM | DATETIME (UTC) | The instant when the patient's lactation status was updated. |
| LACT_STAT_CSN | NUMERIC (18,0) | The contact serial number of the encounter in which the lactation status updated. The contact serial number is the unique identifier for the encounter. |
| LACT_STAT_USER_ID | VARCHAR (18) | The unique ID of the user who last updated the patient's lactation status. |
| HM_PLAN_DISP_FLAG *(deprecated)* | VARCHAR (254) | This column is deprecated and does not extract any data. The feature for which this column was created is no longer in use. There is no replacement column. |
| AMBULATORY_STATUS_C | VARCHAR (66) |  |
| OCCUPATION | VARCHAR (254) | A patient's occupation. |
| ADVANCED_DIR_YN | VARCHAR (1) |  |
| ABST_DT | DATETIME | The date of abstraction of the patient record. |
| REC_CREATE_DEPT_ID | NUMERIC (18,0) | The unique ID of the department in which the patient record was created. |
| ALRGY_REV_REAS_C | INTEGER |  |
| HOME_REC_SUBSCRD_YN | VARCHAR (1) | Set when other deployments subscribed this record |
| EPT_UNRSLVED_DAT_YN *(deprecated)* | VARCHAR (1) |  |
| EXTERNAL_ACCESS *(deprecated)* | NUMERIC (18,2) | *** Deprecated *** In table PATIENT_3, the column EXTERNAL_ACCESS (EPT/2600) has been deprecated. The deprecated column's content/data is no longer available since it is no longer populated in Chronicles. ****** This column contains a 1 if a patient was accessed via Identifier on a certain date. |
| EXT_ACC_DATE *(deprecated)* | DATETIME | *** Deprecated *** In table PATIENT_3, the column EXT_ACC_DATE (EPT/2601) has been deprecated. The deprecated column's content/data is no longer available since it is no longer populated in Chronicles. ****** Date of External Access |
| MASTER_PAT_YN | VARCHAR (1) |  |
| ALLOW_HALF_PILLS_YN | VARCHAR (1) |  |
| APPT_REM_TM_C | INTEGER |  |
| APPT_REM_MECH_C | INTEGER |  |
| RCV_MSGS_C | INTEGER |  |
| KIOSK_LAST_USE_DTTM | DATETIME (Local) | Contains the instant the patient last used the Welcome kiosk. |
| KIOSK_LAST_USE_R_C | INTEGER |  |
| KIOSK_LAST_USE_K_ID | VARCHAR (18) | Contains the rule applied that kicked the patient out of their last attempt to use the Welcome kiosk. |
| KIOSK_LAST_USE_DATA | VARCHAR (192) | Contains data related to the last use category that provides additional information about the patient's last use problem. |
| MOTHER_MAIDEN_NAME | VARCHAR (50) | The maiden name of the patient's mother. |
| MOTHER_FIRST_NAME | VARCHAR (50) | The first name of the patient's mother. |
| HMT_DUE_STATUS_DTTM *(deprecated)* | DATETIME (Local) | *** Deprecated *** Updating EPT 18645 will trigger clarity extract of the entire EPT.NOADD_SINGLE table which has a very negative impact on performance.  The date and time when the patient's health maintenance topic due status was last updated.  This column has been replaced by column HM_LAST_UPDATE (EPT/18645) in table PATIENT_HMT_STATUS.  Please reference the replacement column to get the relevant values. |
| L_GROWTH_CHART_USED | VARCHAR (254) |  |
| ALRG_LAST_UPDA_DTTM | DATETIME (Local) | The latest instant in which allergies were updated. |
| PAT_ARCH_STATUS_C | INTEGER |  |
| KI_PHOTO_UPD_DT | DATETIME | Date that the patient photo was updated from the kiosk. |
| PED_BIRTH_LEN_NUM | NUMERIC (18,1) | Newborn birth length stored in inches. |
| PED_BIRTH_WT_NUM | NUMERIC (18,2) | Newborn birth weight stored in ounces. |
| PED_BIRTH_HD_CR_NUM *(deprecated)* | NUMERIC (18,1) |  |
| PED_DISCHRG_WGT_NUM | NUMERIC (18,2) | Newborn discharge weight stored in ounces. |
| PED_APGAR_ONE_C | INTEGER |  |
| PED_APGAR_FIVE_C | INTEGER |  |
| PED_APGAR_TEN_C | INTEGER |  |
| PED_GEST_AGE_NUM | INTEGER | Newborn gestational age at birth. Displays as completed number of weeks, so 37 6/7 = 37. EPT-15308 is a virtual item that is the numeric value of the string entered in EPT-19408 in the Birth History activity. This column replaces the column PED_GEST_AGE in the PATIENT table which has a datatype of varchar. |
| UNOS_PRIM_COD_C | INTEGER |  |
| UNOS_PRIM_COD_SP | VARCHAR (50) | Free text description of the transplant patient's primary cause of death. |
| UNOS_CTRB_COD1_C | INTEGER |  |
| UNOS_CNTB_COD1_SP | VARCHAR (50) | Free text description of the transplant patient's first contributory cause of death. |
| UNOS_CTRB_COD2_C | INTEGER |  |
| UNOS_CNTB_COD2_SP | VARCHAR (50) | Free text description of the transplant patient's second contributory cause of death. |
| NB_DEL_REC_ID | NUMERIC (18,0) | Stores the newborn's delivery record (HSB) ID.  This column can be linked to OB_HSB_DELIVERY.SUMMARY_BLOCK_ID or other Delivery Record tables.  This column can be used to link from admitted newborns to a delivery record using HSP_LD_MOM_CHILD.CHILD_ENC_CSN_ID to PAT_ENC_HSP.PAT_ENC_CSN_ID and from PAT_ENC_HSP.PAT_ID to PATIENT_3.PAT_ID.   This column can be used to link from admitted newborns to a delivery record using HSP_LD_MOM_CH_PEND.CHILD_ENC_CSN_ID to PAT_ENC_HSP.PAT_ENC_CSN_ID and from PAT_ENC_HSP.PAT_ID to PATIENT_3.PAT_ID. |
| NOTIF_PAT_EMAIL_YN | VARCHAR (1) |  |
| NOTIF_PAT_SCHED_YN | VARCHAR (1) |  |
| NOTIF_PAT_CANC_YN | VARCHAR (1) |  |
| NOTIF_PAT_MISSED_YN | VARCHAR (1) |  |
| NOTIF_PAT_CHNG_YN | VARCHAR (1) |  |
| HOW_NOTIF_PAT_C | INTEGER |  |
| CASE_SUPER_PROG_C | VARCHAR (66) |  |
| IMM_CONFIDENTIAL_YN | VARCHAR (1) |  |
| CVG_VERIF_USER_ID | VARCHAR (18) | The unique ID of the user who most recently verified the patient's coverage information. |
| FIRST_APPT_DEPT_ID | NUMERIC (18,0) | The unique ID of the department where the patient had his or her first appointment. |
| PREFERRED_NAME | VARCHAR (254) | The preferred name for the patient. |
| LAST_VERIFIED_BY_ID | VARCHAR (18) | The last user who verified the patient. |
| LEARN_ASSMT_ID | NUMERIC (18,0) | Learning assessment ID. This can be used to check that the learning assessments are being given to the appropriate patients at the appropriate times. |
| CURR_LOC_ID | NUMERIC (18,0) | The unique ID of the most recent confirmed patient location that is associated with the patient. |
| PCOD_CAUSE_DX_ID | NUMERIC (18,0) | Stores the preliminary cause of death for the patient |
| PCOD_REC_USER_ID | VARCHAR (18) | Stores the user that filed the preliminary cause of death |
| PCOD_INST_REC_DTTM | DATETIME (UTC) | Stores the instant that the preliminary cause of death was recorded |
| EMPL_ID_NUM | VARCHAR (254) | The patient's employee identification number. |
| SCHOOL_PHONE | VARCHAR (254) | The patient's school phone number. |
| CONTRACT_ID | NUMERIC (18,0) | The unique ID of the pricing contract that is associated with the patient. |
| AUTO_PT_WO_IND_YN | VARCHAR (1) |  |
| AUTO_PT_WO_FROM_DT | DATETIME | The beginning of the limited date range in which the automatic self-pay write-off applies to the patient. |
| AUTO_PT_WO_TO_DT | DATETIME | The ending of the limited date range in which the automatic self-pay write-off applies to the patient. |
| CVG_LAST_VERIFY_DT | DATETIME | The date that the coverage was last verified. |
| PRIM_FIN_CL_C | VARCHAR (66) |  |
| MC_MEMBER_ONLY_C | INTEGER |  |
| SPOT_UPD_USER_ID | VARCHAR (18) | This item saves the user ID of the person who most recently updated the patient's Spotlight folder in the Synopsis activity by adding a row that previously had not been tracked by any other user. |
| SPOT_UPD_DTTM | DATETIME (UTC) | This item saves the instant when a Synopsis row that had not been tracked by any user was most recently added to the patient's Spotlight folder. |
| IS_TEST_PAT_YN | VARCHAR (1) |  |
| GYN_HX_CMT_NOTE_ID | VARCHAR (254) | ID of HNO (note) record for free-text gynecological information |
| GYN_HX_MENARCHE_AGE | INTEGER | The patient's age at menarche |
| GYN_HX_FST_PREG_AGE | INTEGER | The patient's age at first pregnancy |
| GYN_HX_MO_BRSTFDG | INTEGER | The number of months the patient spent breastfeeding |
| GYN_HX_MENOPAUS_AGE | INTEGER | The patient's age at menopause |
| COMP_APPTS_COUNT | INTEGER | The count of completed appointments for the patient. |
| NOSHOW_APPTS_COUNT | INTEGER | The count of no-show appointments for the patient. |
| FAMILY_GROUPER | VARCHAR (18) | A family identifier that may be used to group family members together. Note that this is not guaranteed to be unique across deployments in IntraConnect. |
| FETUS_YN | VARCHAR (1) |  |
| DENT_CLASS_C | VARCHAR (66) |  |
| DENT_LAST_USER_ID | VARCHAR (18) | This item stores the last user who edited the dental classification of the patient. |
| DENT_INST_DTTM | DATETIME (Local) | This item stores the instant when the dental classification of the patient was last edited. |
| ENGLISH_FLUENCY_C | INTEGER |  |
| FORM_CONFIDENCE_C | INTEGER |  |
| BRANCH_OF_SERVICE_C | INTEGER |  |
| MILITARY_RANK_C | INTEGER |  |
| FMP_C | INTEGER |  |
| PAT_CAT_C | INTEGER |  |
| MIL_COMPONENT_C | INTEGER |  |
| ASGN_MIL_UNIT_ID | NUMERIC (18,0) | This column stores the military unit ID to which the patient is assigned. |
| MIL_PAY_GRADE_C | INTEGER |  |
| TEMP_MIL_UNIT_ID | NUMERIC (18,0) | This column stores the patient's temporary military unit ID. |
| PED_GEST_AGE_DAYS | INTEGER | Newborn gestational age at birth in total number of days |
| PED_BIRTH_HD_CIRCUM | NUMERIC (18,3) | Newborn birth head circumference stored in inches. |
| LAST_USED_GROWTH_CHART_ID | NUMERIC (18,0) | The last Growth Chart used for this patient across all encounters.   To see the logic of which Growth Chart defaults for a patient see the help text for I EPT 19428.  To provide networking from I EPT 19428 to HGC, we have to change the Chronicles data type to numeric from string. For performance reasons (required casting), this column can replace L_GROWTH_CHART_USED. |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | PAT_ID | ANTICOAG_SELF_REGULATING | PAT_ID | No | No | No |  |
| 1 | PAT_ID | CARE_COORDINATION | PAT_ID | Unknown | No | No |  |
| 1 | PAT_ID | CLAIMS_DERIVE_PAT_FLAGS | PAT_ID | No | No | No |  |
| 1 | PAT_ID | COMMUNITY_RESRC_REVIEWED | PAT_ID | No | No | No |  |
| 1 | PAT_ID | D_PAT_GEOGRAPHIC_CLASS | PAT_ID | Unknown | Unknown | No |  |
| 1 | PAT_ID | EPT_MEM_INFO | PAT_ID | No | No | No |  |
| 1 | PAT_ID | EXT_DATA_LAST_DONE | PAT_ID | No | No | No |  |
| 1 | PAT_ID | F_IBD_ADULT_FORM_PAT | PAT_ID | Unknown | Unknown | No |  |
| 1 | PAT_ID | HH_PAT_INFO | PAT_ID | Unknown | No | No |  |
| 1 | PAT_ID | HM_STATUS_UPD | PAT_ID | No | No | No |  |
| 1 | PAT_ID | IMMNZTN_LAST_REVIEW | PAT_ID | No | No | No |  |
| 1 | PAT_ID | PATIENT | PAT_ID | No | No | No |  |
| 1 | PAT_ID | PATIENT_2 | PAT_ID | No | No | No |  |
| 1 | PAT_ID | PATIENT_4 | PAT_ID | No | No | No |  |
| 1 | PAT_ID | PATIENT_5 | PAT_ID | No | No | No |  |
| 1 | PAT_ID | PATIENT_6 | PAT_ID | No | No | No |  |
| 1 | PAT_ID | PATIENT_CONF_ADDR | PAT_ID | No | No | No |  |
| 1 | PAT_ID | PATIENT_MISC_COMMENTS | PAT_ID | No | No | No |  |
| 1 | PAT_ID | PATIENT_MYC | PAT_ID | Unknown | No | No |  |
| 1 | PAT_ID | PATIENT_OPT | PAT_ID | No | No | No |  |
| 1 | PAT_ID | PAT_ENC_LAST_HX_CT | PAT_ID | Unknown | Unknown | No |  |
| 1 | PAT_ID | PAT_RES_CODE | PAT_ID | No | No | No |  |
| 1 | PAT_ID | PROB_LIST_REVIEWED | PAT_ID | No | No | No |  |
| 1 | PAT_ID | REGADDL_PAT | PAT_ID | No | No | No |  |
| 1 | PAT_ID | SCF_FHIR_MAP | PAT_ID | No | No | No |  |
| 1 | PAT_ID | TEETH_REVIEWED | PAT_ID | No | No | No |  |
| 1 | PAT_ID | VALID_PATIENT | PAT_ID | No | No | No |  |
| 1 | PAT_ID | V_PAT_ABO | PAT_ID | Unknown | Unknown | No |  |
| 1 | PAT_ID | V_PAT_FACT | PAT_ID | Unknown | Unknown | No |  |
| 1 | PAT_ID | V_PAT_HX_TOB_USE | PAT_ID | Unknown | Unknown | No |  |

_(382 total; showing first 30)_
