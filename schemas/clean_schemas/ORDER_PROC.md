# ORDER_PROC

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=ORDER_PROC

## Description

The ORDER_PROC table enables you to report on the procedures ordered in the clinical system. We have also included patient and contact identification information for each record.

**Primary table** in this group (102 cols). Overflow siblings joined on shared key: ORDER_PROC_2 (100 cols), ORDER_PROC_3 (99 cols), ORDER_PROC_4 (100 cols), ORDER_PROC_5 (99 cols), ORDER_PROC_6 (99 cols), ORDER_PROC_7 (21 cols). Prefer this table for most queries.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | ORD |
| Release Version | EPIC 2000 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| ORDER_PROC_ID | NUMERIC (18,0) | The unique ID of the order record associated with this procedure order. |
| PAT_ID | VARCHAR (18) | The unique ID of the patient record for this order. This column is frequently used to link to the PATIENT table. |
| PAT_ENC_DATE_REAL | No | A unique, internal contact date in decimal format. The integer portion of the number indicates the date of the contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| PAT_ENC_CSN_ID | NUMERIC (18,0) | The unique contact serial number for this contact. This number is unique across patients and encounters in your system. If you use IntraConnect this is the Unique Contact Identifier (UCI). |
| RESULT_LAB_ID | NUMERIC (18,0) | The unique ID of the lab or other resulting agency, such as radiology, that provided the order results. |
| ORDERING_DATE | DATETIME | The date when the procedure order was placed. |
| ORDER_TYPE_C | INTEGER |  |
| PROC_ID | NUMERIC (18,0) | The unique ID of the  procedure record corresponding to this order. This can be used to link to CLARITY_EAP. |
| PROC_CODE | 40 |  |
| DESCRIPTION | VARCHAR (254) | A brief summary of the procedure order. |
| ORDER_CLASS_C | VARCHAR (66) |  |
| AUTHRZING_PROV_ID | VARCHAR (18) | The unique ID of the provider prescribing or authorizing the order. |
| ABNORMAL_YN | VARCHAR (1) |  |
| BILLING_PROV_ID | VARCHAR (18) | The unique ID of the provider under whose name this order should be billed. This might be the same ID as the AUTHRZING_PROV_ID. |
| COSIGNER_USER_ID *(deprecated)* | VARCHAR (18) | This column is no longer used.  Refer to tables ORDER_SIGNED_MED and ORDER_SIGNED_PROC for cosign information.  The deprecated column's content/data is no longer available since it is no longer populated in Chronicles. |
| ORD_CREATR_USER_ID | VARCHAR (18) | The unique identifier of the user who signed the order, or the last person who performed a sign and hold or release action for a signed and held order. |
| LAB_STATUS_C | INTEGER |  |
| ORDER_STATUS_C | INTEGER |  |
| MODIFIER1_ID | VARCHAR (20) | The unique ID of the modifier record.  This is the first modifier entered for the procedure and affects how the procedure is billed. |
| MODIFIER2_ID | VARCHAR (20) | The unique ID of the modifier record.  This is the second modifier entered for the procedure and affects how the procedure is billed. |
| MODIFIER3_ID | VARCHAR (20) | The unique ID of the modifier record.  This is the third modifier entered for the procedure and affects how the procedure is billed. |
| MODIFIER4_ID | VARCHAR (20) | The unique ID of the modifier record.  This is the fourth modifier entered for the procedure and affects how the procedure is billed. |
| QUANTITY | INTEGER | The number of procedures authorized for this order. |
| REASON_FOR_CANC_C | VARCHAR (66) |  |
| FUTURE_OR_STAND | VARCHAR (1) |  |
| STANDING_EXP_DATE | DATETIME | The date when a recurring procedure order expires. |
| FUT_EXPECT_COMP_DT | DATETIME | The date by which each future procedure order should be completed. Displayed in calendar format. |
| STANDING_OCCURS | INTEGER | The number of individual occurrences remaining for this procedure order. |
| STAND_ORIG_OCCUR | INTEGER | The total number of occurrences that a recurring order was authorized for. |
| RESULT_TYPE *(deprecated)* | VARCHAR (8) |  |
| REFERRING_PROV_ID | VARCHAR (18) | The unique ID of the provider who has referred this order, i.e. the referring provider. |
| REFD_TO_LOC_ID | NUMERIC (18,0) | The unique ID of the location record to which this patient was referred. |
| REFD_TO_SPECLTY_C | VARCHAR (66) |  |
| REQUESTED_SPEC_C | VARCHAR (66) |  |
| RFL_PRIORITY *(deprecated)* | VARCHAR (4) |  |
| RFL_CLASS_C | VARCHAR (66) |  |
| RFL_TYPE_C | VARCHAR (66) |  |
| RSN_FOR_RFL_C | VARCHAR (66) |  |
| RFL_NUM_VIS | INTEGER | The number of visits this referral order is authorized for. |
| RFL_EXPIRE_DT | DATETIME | The expiration date for this referral order. |
| INTERFACE_STAT_C | INTEGER |  |
| CPT_CODE *(deprecated)* | VARCHAR (50) |  |
| UPDATE_DATE | No | The date and time the procedure order was extracted from the database. |
| SERV_AREA_ID | No | *** Deprecated *** In table ORDER_PROC, the column SERV_AREA_ID has been deprecated. This column has been replaced by column SERV_AREA_ID in table PAT_ENC. Please reference the replacement column to get the relevant values. |
| ABN_NOTE_ID | VARCHAR (254) | The unique ID of the notes record representing the Advanced Beneficiary Notice form associated with this order. |
| RADIOLOGY_STATUS_C | INTEGER |  |
| INT_STUDY_C | INTEGER |  |
| INT_STUDY_USER_ID | VARCHAR (18) | The unique ID of the employee record who denoted a study as worth being marked for later review, as in for an educational case or for group reading physician review. |
| TECHNOLOGIST_ID | VARCHAR (18) | The unique ID of the employee record of the technologist who performed this procedure. |
| FILMS_USED *(deprecated)* | INTEGER | This column is deprecated and does not extract any data.  The item for which this column was created is no longer in use.  To determine the number of films used for an order, use ORDER_RAD_FILMS.FILMS_USED instead. |
| FILM_SIZE_C *(deprecated)* | INTEGER |  |
| NUMBER_OF_REPEATS *(deprecated)* | INTEGER | This column is deprecated and does not extract any data.  The item for which this column was created is no longer in use.  To determine the number of repeats for a procedure, use ORDER_RAD_REPEATS.NUMBER_REPEATS instead. |
| DOSE *(deprecated)* | INTEGER | This column is deprecated and does not extract any data. The feature for which this column was created is no longer in use. There is no replacement column. |
| PROC_BGN_TIME | 52119 | The date and time when the procedure order (exam) is to begin. |
| PROC_END_TIME | 52129 | The date and time when the exam for the procedure order has ended. |
| RIS_TRANS_ID | VARCHAR (18) | The unique ID of the user record of the transcriptionist for this order. |
| ORDER_INST | DATETIME (Local) | The instant when the order was created. |
| DISPLAY_NAME | VARCHAR (510) | The name of the order as it appears in the patient's record. |
| HV_HOSPITALIST_YN | VARCHAR (1) |  |
| PROV_STATUS *(deprecated)* | VARCHAR (50) |  |
| ORDER_PRIORITY_C | INTEGER |  |
| CHRG_DROPPED_TIME | DATETIME (Local) | The date and time when the charge was generated for the procedure order. |
| PANEL_PROC_ID | NUMERIC (18,0) | The unique ID of the panel procedure record associated with this order. |
| COSIGNER_AUTH_TIME *(deprecated)* | DATETIME | This column is no longer used.  Refer to tables ORDER_SIGNED_MED and ORDER_SIGNED_PROC for cosign information.  The deprecated column's content/data is no longer available since it is no longer populated in Chronicles. |
| COSIGNED_USER_ID *(deprecated)* | VARCHAR (18) | This column is no longer used.  Refer to tables ORDER_SIGNED_MED and ORDER_SIGNED_PROC for cosign information.  The deprecated column's content/data is no longer available since it is no longer populated in Chronicles. |
| STAND_INTERVAL | VARCHAR (254) | The time interval set for a recurring order, indicating the time between one instance of the order and the next instance. |
| DISCRETE_INTERVAL | VARCHAR (66) |  |
| INSTANTIATED_TIME | DATETIME | The date and time of instantiation when a child order is generated from a standing or future order. |
| INSTNTOR_USER_ID | VARCHAR (18) | The unique ID of the user who instantiated the order. |
| DEPT_REF_PROV_ID | NUMERIC (18,0) | The unique ID of the department to which this order is referred. |
| SPECIALTY_DEP_C | VARCHAR (66) |  |
| ORDERING_MODE *(deprecated)* | VARCHAR (50) |  |
| SPECIMEN_TYPE_C | INTEGER |  |
| SPECIMEN_SOURCE_C | INTEGER |  |
| ORDER_TIME | 25 | The date and time when the procedure order was placed. |
| RESULT_TIME | DATETIME (Local) | The most recent date and time when the procedure order was resulted. |
| REVIEW_TIME | DATETIME (Local) | The most recent date and time when the procedure order was reviewed. |
| IS_PENDING_ORD_YN | VARCHAR (1) |  |
| PROC_START_TIME | 7060 | The date and time when the procedure order is to start. |
| PROBLEM_LIST_ID | NUMERIC (18,0) | The unique ID of the problem list record that is associated with this order. This column is mainly used for immunization orders. |
| RSLTS_INTERPRETER | VARCHAR (255) | The name of the principal results interpreter, the person who reviewed and interpreted the results. |
| PROC_ENDING_TIME | 7070 | The date and time when the procedure order is to end. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| SPECIFIED_FIRST_TM | DATETIME (Local) | The first occurrence time specified by a user, if the order was signed with a frequency record containing a schedule of specified dates and times. |
| SCHED_START_TM | DATETIME (Local) | This column stores the scheduling start instant used when the order was last scheduled. |
| SESSION_KEY | VARCHAR (254) | The unique key associated with the order at the time of signing.  Other orders will share this key if they were signed at the same time. |
| PROC_PERF_DEPT_ID | NUMERIC (18,0) | The unique ID of the department where the procedure will take place. |
| PROC_PERF_PROV_ID | VARCHAR (18) | The unique ID of the provider who will be performing the procedure. |
| PROC_PAT_CLASS_C | VARCHAR (66) |  |
| PROC_LATERALITY_C | INTEGER |  |
| PROC_POSSIBLE_YN | VARCHAR (1) |  |
| PROC_DATE | DATETIME | The date when the procedure will be performed. |
| LABCORP_BILL_TYPE_C | VARCHAR (66) |  |
| LABCORP_CLIENT_ID | VARCHAR (192) | The client ID or account ID assigned by the reference lab. |
| LABCORP_CONTROL_NUM | INTEGER | Required information for LabCorp requisition and order messages. |
| NO_CHG_RSN_C | INTEGER |  |
| MRK_RSLT_MSG_IMP_YN | VARCHAR (1) |  |
| CHNG_ORDER_PROC_ID | NUMERIC (18,0) | The unique ID of the changed or reordered procedure order that this procedure replaced. This column is frequently used to link back to ORDER_PROC table. |
| REC_ARCHIVED_YN | No | Indicates whether the Procedure Order record is archived at the record level. |
| HAS_RELEASED_CHILDREN_YN | VARCHAR (1) | Surrogate key used to uniquely identify rows in this (and only this) table on Cogito Cloud only, do not assume the surrogate key in this table will correspond to the surrogate key in another table |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| BITMAP INDEX | EIX_ORDER_PROC_ABNORMAL_YN | ABNORMAL_YN | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_ORDER_PROC_AUTH_PROV_ID | AUTHRZING_PROV_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_ORDER_PROC_CSN_OI | PAT_ENC_CSN_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_ORDER_PROC_CSN_OI | ORDER_INST | 2 | Yes | Yes |  |
| B-TREE INDEX | EIX_ORDER_PROC_CSN_PROC | PROC_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_ORDER_PROC_CSN_PROC | PAT_ENC_CSN_ID | 2 | Yes | Yes |  |
| B-TREE INDEX | EIX_ORDER_PROC_END_EXAM | PROC_END_TIME | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_ORDER_PROC_ORDER_INST | ORDER_INST | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_ORDER_PROC_PAID_CMP | PAT_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_ORDER_PROC_PAID_CMP | PAT_ENC_DATE_REAL | 2 | Yes | Yes |  |
| B-TREE INDEX | EIX_ORDER_PROC_PAID_RES_DTTM | PAT_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_ORDER_PROC_PAID_RES_DTTM | RESULT_TIME | 2 | Yes | Yes |  |
| B-TREE INDEX | EIX_ORDER_PROC_RELAID | RESULT_LAB_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_ORDER_PROC_RESULT_TM | RESULT_TIME | 1 | Yes | Yes |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ORDER_PROC_ID | ADT_ORDERS_ERRORS | ORDER_ID | No | No | No |  |
| 1 | ORDER_PROC_ID | ADT_ORDER_INFORMATION | ORDER_ID | No | No | No |  |
| 1 | ORDER_PROC_ID | APPT_REQUEST | REQUEST_ID | No | No | No |  |
| 1 | ORDER_PROC_ID | CL_ORD_FST_LST_SCH | ORDER_ID | No | No | No |  |
| 1 | ORDER_PROC_ID | DENT_ORD_NOADD | ORDER_ID | No | No | No |  |
| 1 | ORDER_PROC_ID | DUPMED_DISMISS_HH_INFO | ORDER_ID | No | No | No |  |
| 1 | ORDER_PROC_ID | ENDOSCOPY_METRICS | ORDER_ID | Unknown | No | No |  |
| 1 | ORDER_PROC_ID | EXTERNAL_ORDER_INFO | ORDER_ID | No | No | No |  |
| 1 | ORDER_PROC_ID | F_IMG_STUDY | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_PROC_ID | F_IP_HSP_SUM_ORDER | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_PROC_ID | F_LAB_ORDERS | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_PROC_ID | F_MU_OBJ_EH_PLACED_ORDER | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_PROC_ID | F_MU_OBJ_EH_RESULTD_ORDER | ORDER_PROC_ID | Unknown | Unknown | No |  |
| 1 | ORDER_PROC_ID | F_ONC_PRIOR_AUTH_ORDERS | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_PROC_ID | F_OPIOID_ORDERS | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_PROC_ID | F_RX_ORDER | ORDER_MED_ID | Unknown | Unknown | No |  |
| 1 | ORDER_PROC_ID | HH_MED_ORD_IN_POC_DETAIL | ORDER_MED_ID | No | No | No |  |
| 1 | ORDER_PROC_ID | HV_ORDER_PROC | ORDER_PROC_ID | Unknown | No | No |  |
| 1 | ORDER_PROC_ID | MED_DETAILS_EXT_ORD | ORDER_ID | No | No | No |  |
| 1 | ORDER_PROC_ID | MERCHANDISE_ORDER_INFO | ORDER_ID | Yes | No | No |  |
| 1 | ORDER_PROC_ID | MU_EH_QRDA_I_ORDER | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_PROC_ID | ORDERS | ORDER_ID | No | No | No |  |
| 1 | ORDER_PROC_ID | ORDER_AUTH_INFO | ORDER_ID | No | No | No |  |
| 1 | ORDER_PROC_ID | ORDER_MED | ORDER_MED_ID | Unknown | No | No |  |
| 1 | ORDER_PROC_ID | ORDER_MEDINFO | ORDER_MED_ID | Unknown | No | No |  |
| 1 | ORDER_PROC_ID | ORDER_MED_2 | ORDER_ID | Unknown | No | No |  |
| 1 | ORDER_PROC_ID | ORDER_MED_3 | ORDER_ID | Unknown | No | No |  |
| 1 | ORDER_PROC_ID | ORDER_MED_4 | ORDER_ID | Unknown | No | No |  |
| 1 | ORDER_PROC_ID | ORDER_MED_5 | ORDER_ID | Unknown | No | No |  |
| 1 | ORDER_PROC_ID | ORDER_MED_6 | ORDER_MED_ID | Unknown | No | No |  |

_(581 total; showing first 30)_
