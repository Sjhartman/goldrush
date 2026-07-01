# OR_CASE

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=OR_CASE

## Description

The OR_CASE table contains OR management system case records.

**Primary table** in this group (134 cols). Overflow siblings joined on shared key: OR_CASE_2 (112 cols), OR_CASE_3 (104 cols), OR_CASE_4 (10 cols). Prefer this table for most queries.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | ORC |
| Release Version | MU1 - MAY 2001 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| OR_CASE_ID | VARCHAR (18) | The unique ID of the procedural case record. |
| CASE_NAME | VARCHAR (200) | The name of the surgical case record. |
| SURGERY_DATE | DATETIME | The date on which the surgery is scheduled to take place. |
| CASE_TYPE_C | INTEGER |  |
| CASE_CLASS_C | INTEGER |  |
| PAT_ID | VARCHAR (18) | The unique ID of the patient associated with the procedural case record. |
| PAT_AGE | INTEGER | The age of the patient associated with the surgical case. |
| PAT_CLASS_C | VARCHAR (66) |  |
| SERVICE_C | VARCHAR (66) |  |
| NUM_OF_PANELS | INTEGER | The total number of procedure panels in the surgical case record. A panel is a grouping of surgical procedures performed together. |
| EXP_DATE | DATETIME | The date on which this surgical case expires. The case should be scheduled on or before this date. |
| REQ_FROM_WEB_YN | VARCHAR (1) |  |
| REQUESTED_BY | VARCHAR (255) | The name of the person who requested that the surgical case be created. |
| REQUEST_BY_PHONE | VARCHAR (80) | The phone number of the person who requested that the case be created. |
| SETUP_OFFSET | INTEGER | The amount of time in minutes required to set up at the beginning of the case. |
| CLEANUP_OFFSET | INTEGER | The amount of time in minutes required to clean up at the end of the case. |
| START_AT_OR_AFTER | DATETIME (Local) | The time of day before which the case cannot begin. |
| START_AT_OR_BEFORE | DATETIME (Local) | The time of day after which the case cannot begin. |
| TOTAL_TIME_NEEDED | INTEGER | The total amount of time required to perform the case. |
| REFERRING_PROV_ID | VARCHAR (18) | The unique ID of the physician who referred the patient associated with the case. |
| PREOP_XRAYS_YN | VARCHAR (1) |  |
| PREOP_VISIT_YN | VARCHAR (1) |  |
| LATEX_ALLERGIC_YN | VARCHAR (1) |  |
| OR_ID | VARCHAR (18) | The unique ID of the room the case is scheduled to be performed. This column is frequently used to link to CLARITY_SER. |
| LOC_ID | NUMERIC (18,0) | The unique ID of the location where the procedure is scheduled to be performed. This column is frequently used to link to CLARITY_LOC. |
| PRIORITY_C | INTEGER |  |
| ADD_ON_CASE_YN | VARCHAR (1) |  |
| SCHED_STATUS_C | INTEGER |  |
| CASE_PROGRESS_C | VARCHAR (66) |  |
| CANCEL_REASON_C | INTEGER |  |
| CANCEL_USER_ID | VARCHAR (18) | The unique ID of the user who most recently canceled the case or removed it from the schedule. This column will remain populated even if the case is put back on the schedule. This column is frequently used to link to CLARITY_EMP. |
| CANCEL_COMMENTS | VARCHAR (255) | The comments entered by the user that canceled the case. |
| CANCEL_DATE | DATETIME | The most recent date on which the case was canceled or removed from the schedule. This column will remain populated even if the case is put back on the schedule. |
| TIME_SCHEDULED | 530 | The date and time at which the case is scheduled to be performed on the surgery date. |
| VOID_REASON_C | INTEGER |  |
| CANCEL_CHKIN_RSN_C | INTEGER |  |
| TOUCHED_BY_EOD_YN | VARCHAR (1) |  |
| CHECKIN_INSTANT | DATETIME (Local) | The date and time at which the case was checked-in. |
| PATIENT_ESCORT | VARCHAR (254) | The person escorting the patient for the surgery. This is a free text value. |
| PANEL1_START_AT | INTEGER | Indicates at what time within the case panel 1 should begin. This is measured in minutes relative to the beginning of the case. |
| PANEL1_LENGTH | INTEGER | The total amount of time required for panel 1 to be performed. This includes the times of all the procedures within the panel. |
| PANEL2_START_AT | INTEGER | Indicates at what time within the case panel 2 should begin. This is measured in minutes relative to the beginning of the case. |
| PANEL2_LENGTH | INTEGER | The total amount of time required for panel 2 to be performed. This includes the times of all the procedures within the panel. |
| PANEL3_START_AT | INTEGER | Indicates at what time within the case panel 3 should begin. This is measured in minutes relative to the beginning of the case. |
| PANEL3_LENGTH | INTEGER | The total amount of time required for panel 3 to be performed. This includes the times of all the procedures within the panel. |
| PANEL4_START_AT | INTEGER | Indicates at what time within the case panel 4 should begin. This is measured in minutes relative to the beginning of the case. |
| PANEL4_LENGTH | INTEGER | The total amount of time required for panel 4 to be performed. This includes the times of all the procedures within the panel. |
| PANEL5_START_AT | INTEGER | Indicates at what time within the case panel 5 should begin. This is measured in minutes relative to the beginning of the case. |
| PANEL5_LENGTH | INTEGER | The total amount of time required for panel 5 to be performed. This includes the times of all the procedures within the panel. |
| RECORD_CREATE_DATE | DATETIME | The date on which the case was created. |
| REC_CREATE_USER_ID | VARCHAR (18) | The unique ID of the user who created the case. |
| PRE_OP_DX *(deprecated)* | VARCHAR (255) | The free text description of the pre-op diagnosis for the case.  This column has been deprecated. The column had no KBSQL code prior to deprecation, and so was extracting null values. Further, this column would have only been able to extract line 1 of this item. Please use column PRE_OP_DX in table OR_CASE_PREOPDX instead. |
| SPECIAL_NEEDS *(deprecated)* | VARCHAR (255) | The special needs for the patient associated with the case.  This column has been deprecated. The column had no KBSQL code prior to deprecation, and so was extracting null values. Further, this column would have only been able to extract line 1 of this item. Please use column SPECIAL_NEEDS in table OR_CASE_SPECNEED instead. |
| ADT_CSN | NUMERIC (18,0) | Contact serial number for an Admission Discharge Transfer (ADT) admit contact. |
| TRANSLATOR *(deprecated)* | VARCHAR (40) |  |
| POSTOP_DEST *(deprecated)* | VARCHAR (40) |  |
| IOP_XRAYS_YN *(deprecated)* | VARCHAR (1) |  |
| CASE_REQST_USER_ID | VARCHAR (18) | The unique ID of the user who placed the web request. |
| PEND_STATUS *(deprecated)* | VARCHAR (30) |  |
| SHUFFLE_USER_ID | VARCHAR (18) | The unique ID of the user who placed the case in the shuffle depot. |
| PICKLIST_PRINT_YN | VARCHAR (1) |  |
| FORMS_PRINTED_YN | VARCHAR (1) |  |
| CONFIDENTIAL_YN | VARCHAR (1) |  |
| PAT_LEVEL_C | INTEGER |  |
| INTL_PATIENT_YN | VARCHAR (1) |  |
| PAIN_MGMT_C | INTEGER |  |
| ADMIT_DATE | DATETIME | The date on which the patient was admitted. |
| LENGTH_OF_STAY | INTEGER | The length of the patient's stay while admitted. |
| RESEARCH_IND_C | INTEGER |  |
| CASE_CONFIRMED_YN | VARCHAR (1) |  |
| REQ_BY_PHONE | VARCHAR (50) | The phone number of the person who requested that the case be created. |
| PROPH_AB_REQ_YN *(deprecated)* | VARCHAR (1) |  |
| WEIGHT | NUMERIC (12,2) | The approximate weight of the patient in pounds. |
| ADMIT_SOURCE_C | VARCHAR (66) |  |
| ADMITTING_SRVC_C | VARCHAR (66) |  |
| ADMITTING_PHYS_ID | VARCHAR (192) | The unique ID of the admitting physician. |
| ADMIT_BED_TYPE_C | VARCHAR (66) |  |
| ADD_ON_DATE | DATETIME | The date the case first shows up as an add-on. |
| MODIFIED_CASE_LEN | INTEGER | The length of the case, in minutes, if it has been shortened or lengthened. |
| PAT_START_TIME *(deprecated)* | DATETIME | This column has been replaced by column PAT_START_TIME in table OR_CASE_2. It shows the time the patient is scheduled to arrive at the OR. |
| PAT_TOTAL_TIME | INTEGER | The amount of time in minutes for which the patient is present. |
| BUMPED_CASE_YN | VARCHAR (1) |  |
| BUMPED_INSTANT | DATETIME (Local) | The date and time at which the case was bumped. |
| VOID_COMMENTS | VARCHAR (254) | The free text comments entered when the case was voided. |
| CM_PHY_OWNER_ID | VARCHAR (25) | ID of the physical deployment owner for this record.  Physical owners will be where the data is hosted, either on the cross-over server or the owner deployment. |
| CM_LOG_OWNER_ID | VARCHAR (25) | ID of the logical deployment owner for this record.  Logical owners show the deployment where the record was created but doesn't represent if the record is a part of version skew. |
| CASE_ACCEPTED_YN | VARCHAR (1) |  |
| PROJ_START_INST | DATETIME (Local) | The projected date and time for the start of this case. |
| PROJ_END_INST | DATETIME (Local) | The projected date and time for the end of this case. |
| REAL_TIME_OR_ID | VARCHAR (18) | Store the surgery case's operating room according to the log. |
| CASE_ORDER_ID *(deprecated)* | NUMERIC (18,0) | Stores the Order Record ID (ORD) for the case. |
| PANEL1_IS_COMB_YN | VARCHAR (1) |  |
| PANEL2_IS_COMB_YN | VARCHAR (1) |  |
| PANEL3_IS_COMB_YN | VARCHAR (1) |  |
| PANEL4_IS_COMB_YN | VARCHAR (1) |  |
| PANEL5_IS_COMB_YN | VARCHAR (1) |  |
| PANEL1_DEF_LEN | NUMERIC (18,2) | The panel length defaulted by the system for Panel 1. |
| PANEL2_DEF_LEN | NUMERIC (18,2) | The panel length defaulted by the system for Panel 2. |
| PANEL3_DEF_LEN | NUMERIC (18,2) | The panel length defaulted by the system for Panel 3. |
| PANEL4_DEF_LEN | NUMERIC (18,2) | The panel length defaulted by the system for Panel 4. |
| PANEL5_DEF_LEN | NUMERIC (18,2) | The panel length defaulted by the system for Panel 5. |
| PANEL1_LEN_MOD_YN | VARCHAR (1) |  |
| PANEL2_LEN_MOD_YN | VARCHAR (1) |  |
| PANEL3_LEN_MOD_YN | VARCHAR (1) |  |
| PANEL4_LEN_MOD_YN | VARCHAR (1) |  |
| PANEL5_LEN_MOD_YN | VARCHAR (1) |  |
| REQUESTED_DATE | DATETIME | The preferred date requested for this case. |
| REQUESTED_TIME | DATETIME (Local) | The time (of the day) requested for this case. |
| EXP_ADM_DTE_OFFSET | INTEGER | Stores the number of days prior to the day of surgery, the patient is expected to be admitted. |
| CASE_VERIFIED_YN *(deprecated)* | VARCHAR (1) |  |
| PAT_SOUND_LIKE *(deprecated)* | VARCHAR (30) | *** Deprecated *** In table OR_CASE, the column PAT_SOUND_LIKE (ORC/478) has been deprecated. The deprecated column's content is no longer available since it is no longer populated in Chronicles.  Patient's name "sounds like" string. |
| EXP_ADM_TIME_OFFSET *(deprecated)* | INTEGER |  |
| PAT_ALLERGIES_YN | VARCHAR (1) |  |
| PAT_HEALTH_ISSUE_YN | VARCHAR (1) |  |
| FILMS_FOR_SURGER_YN | VARCHAR (1) |  |
| PREOP_VISIT_NEED_YN | VARCHAR (1) |  |
| PREOP_VISIT_COMP_YN | VARCHAR (1) |  |
| LOG_ID | VARCHAR (18) | This columns stores the log ID for this case. |
| CASE_ACCEPT_NEED_YN | VARCHAR (1) |  |
| IS_CLINICAL_TRL_YN | VARCHAR (1) |  |
| PEND_STATUS_C | VARCHAR (66) |  |
| POSTOP_DEST_C | VARCHAR (66) |  |
| TRANSLATOR_C | VARCHAR (66) |  |
| PTA_LAST_UPD_DATE | DATETIME | Stores the date the procedure time was last updated in the case |
| CASE_BEGIN_INSTANT | DATETIME (Local) | Stores the datetime instant in which the case began. |
| CASE_END_INSTANT | DATETIME (Local) | Stores the datetime instant in which the case ended. |
| PRINTED_INSTANT | DATETIME (Local) | Stores the instant at which the case was printed (applies only for RTF printing). |
| MULT_PROC_COMP_YN | VARCHAR (1) |  |
| USING_EAP_YN | VARCHAR (1) |  |
| ANESTHESIA_C | INTEGER |  |
| CASE_SOURCE_DEPL_ID | VARCHAR (25) | ID of the source deployment that created the case through cross deployment scheduling. |
| PRIMARY_PHYSICIAN_ID | VARCHAR (18) | The primary surgeon from panel 1 of the case, as scheduled. This column is frequently used to link to CLARITY_SER. |
| PRIMARY_PERFORMING_PROV_ID | VARCHAR (18) | Stores the primary performing surgeon/provider for panel 1 as scheduled; used by reports for faster searching. This is only relevant if the system is configured to allow other surgeon/provider roles to be considered the primary performing provider in I EAF 54347. |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| B-TREE INDEX | EIX_OR_CASE_LOG_ID | LOG_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_OR_CASE_LOID | LOC_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_OR_CASE_ORDER_ID | CASE_ORDER_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_OR_CASE_ORID | OR_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_OR_CASE_PAID | PAT_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_OR_CASE_REAL_OR | REAL_TIME_OR_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_OR_CASE_SUDA | SURGERY_DATE | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_OR_CASE_TIME_SCHEDULED | TIME_SCHEDULED | 1 | Yes | Yes |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | OR_CASE_ID | OR_CASE_2 | CASE_ID | Unknown | No | No |  |
| 1 | OR_CASE_ID | OR_CASE_3 | CASE_ID | Unknown | No | No |  |
| 1 | OR_CASE_ID | OR_CASE_4 | OR_CASE_ID | No | No | No |  |
| 1 | OR_CASE_ID | OR_CASE_VIRTUAL | OR_CASE_ID | No | No | No |  |
| 1 | OR_CASE_ID | V_OR_CASE_ORR | CASE_ID | Unknown | Unknown | No |  |
| 4 | CASE_TYPE_C | ZC_OR_CASE_TYPE | CASE_TYPE_C | No | No | No |  |
| 5 | CASE_CLASS_C | ZC_OR_CASE_CLASS | CASE_CLASS_C | No | No | No |  |
| 6 | PAT_ID | ANTICOAG_SELF_REGULATING | PAT_ID | No | No | No |  |
| 6 | PAT_ID | CARE_COORDINATION | PAT_ID | Unknown | No | No |  |
| 6 | PAT_ID | CLAIMS_DERIVE_PAT_FLAGS | PAT_ID | No | No | No |  |
| 6 | PAT_ID | COMMUNITY_RESRC_REVIEWED | PAT_ID | No | No | No |  |
| 6 | PAT_ID | D_PAT_GEOGRAPHIC_CLASS | PAT_ID | Unknown | Unknown | No |  |
| 6 | PAT_ID | EPT_MEM_INFO | PAT_ID | No | No | No |  |
| 6 | PAT_ID | EXT_DATA_LAST_DONE | PAT_ID | No | No | No |  |
| 6 | PAT_ID | F_IBD_ADULT_FORM_PAT | PAT_ID | Unknown | Unknown | No |  |
| 6 | PAT_ID | HH_PAT_INFO | PAT_ID | Unknown | No | No |  |
| 6 | PAT_ID | HM_STATUS_UPD | PAT_ID | No | No | No |  |
| 6 | PAT_ID | IMMNZTN_LAST_REVIEW | PAT_ID | No | No | No |  |
| 6 | PAT_ID | PATIENT | PAT_ID | No | No | No |  |
| 6 | PAT_ID | PATIENT_2 | PAT_ID | No | No | No |  |
| 6 | PAT_ID | PATIENT_3 | PAT_ID | No | No | No |  |
| 6 | PAT_ID | PATIENT_4 | PAT_ID | No | No | No |  |
| 6 | PAT_ID | PATIENT_5 | PAT_ID | No | No | No |  |
| 6 | PAT_ID | PATIENT_6 | PAT_ID | No | No | No |  |
| 6 | PAT_ID | PATIENT_CONF_ADDR | PAT_ID | No | No | No |  |
| 6 | PAT_ID | PATIENT_MISC_COMMENTS | PAT_ID | No | No | No |  |
| 6 | PAT_ID | PATIENT_MYC | PAT_ID | Unknown | No | No |  |
| 6 | PAT_ID | PATIENT_OPT | PAT_ID | No | No | No |  |
| 6 | PAT_ID | PAT_ENC_LAST_HX_CT | PAT_ID | Unknown | Unknown | No |  |
| 6 | PAT_ID | PAT_RES_CODE | PAT_ID | No | No | No |  |

_(252 total; showing first 30)_
