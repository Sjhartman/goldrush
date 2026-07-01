# ORDER_MED

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=ORDER_MED

## Description

The ORDER_MED table enables you to report on medications ordered in EpicCare (prescriptions). We have also included patient and contact identification information for each record.

**Primary table** in this group (139 cols). Overflow siblings joined on shared key: ORDER_MED_2 (75 cols), ORDER_MED_3 (87 cols), ORDER_MED_4 (100 cols), ORDER_MED_5 (94 cols), ORDER_MED_6 (44 cols), ORDER_MED_7 (52 cols), ORDER_MED_8 (7 cols), ORDER_MED_SIG (4 cols). Prefer this table for most queries.

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
| ORDER_MED_ID | NUMERIC (18,0) | The unique ID of the order record associated with this medication order. This is an internal unique identifier for ORD master file records in this table and cannot be used to link to CLARITY_MEDICATION. |
| PAT_ID | VARCHAR (18) | The unique ID of the patient record for this line. This column is frequently used to link to the PATIENT table. |
| PAT_ENC_DATE_REAL | No | A unique, internal contact date in decimal format. The integer portion of the number indicates the date of the contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| PAT_ENC_CSN_ID | NUMERIC (18,0) | The unique contact serial number (CSN) for the patient contact associated with this medication order. This number is unique across patients and encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| ORDERING_DATE | DATETIME | The date when the medication order was placed. |
| ORDER_CLASS_C | VARCHAR (66) |  |
| PHARMACY_ID | NUMERIC (18,0) | The unique ID of the pharmacy record that is associated with this medication order. This column is frequently used to link to the RX_PHR table. This field is only populated if the clinical system user selects a specific pharmacy from the  list, otherwise the field is null. This field is only populated by the ambulatory clinical system, not the pharmacy system. |
| COSIGNER_USER_ID *(deprecated)* | VARCHAR (18) | In table ORDER_MED, the column COSIGNER_USER_ID has been deprecated.   Refer to tables ORDER_SIGNED_MED and ORDER_SIGNED_PROC for cosign information.  The deprecated column's content/data is no longer available since it is no longer populated in Chronicles. |
| ORD_CREATR_USER_ID | VARCHAR (18) | The EMP ID (.1) of the user who signed the order (for a non-signed and held order) or the last person who performed a sign and hold or release action for a signed and held order. |
| MEDICATION_ID | NUMERIC (18,0) | The unique ID of the medication record that is associated with this order. In some circumstances, for example when Intelligent Medication Selection selects an IMS mixture, this column may contain template records that do not represent real medications. For this reason, it is recommended to use the Clarity column ORDER_MEDINFO.DISPENSABLE_MED_ID when reporting on medication orders. |
| DESCRIPTION | VARCHAR (255) | The description of the order. This information is found in the Order field of clinical system?s Order Detail window. |
| SIG *(deprecated)* | VARCHAR (450) |  |
| DOSAGE | VARCHAR (255) | The dispensation amount for the prescription entered by the user in the orders activity. This amount is stored as a string in the orders database. |
| QUANTITY | VARCHAR (200) | The quantity of the prescription being dispensed as entered by the user. |
| REFILLS | VARCHAR (20) | The number of refills allowed for this prescription as entered by the user. |
| START_DATE | DATETIME | The date when the medication order started. The date appears in calendar format. |
| END_DATE | DATETIME | The date when the medication order is to end. |
| DISP_AS_WRITTEN_YN | VARCHAR (1) |  |
| RSN_FOR_DISCON_C | INTEGER |  |
| MED_PRESC_PROV_ID | VARCHAR (18) | The unique ID of the provider who has prescribed or authorized the medication order. The value in this column matches the value in the AUTHRZING_PROV_ID column. |
| NONFRM_XCPT_CD_C | INTEGER |  |
| PANEL_MED_ID | NUMERIC (18,0) | The unique ID of the medication panel that is associated with this medication order. This column is only populated if the medication order was originally placed as part of a panel. |
| SERV_AREA_ID | No | *** Deprecated *** In table ORDER_MED, the column SERV_AREA_ID has been deprecated. This column has been replaced by column SERV_AREA_ID in table PAT_ENC. Please reference the replacement column to get the relevant values. |
| UPDATE_DATE | No | The date and time when this row was created or last updated in Clarity. |
| ORDER_INST | DATETIME (Local) | The date and time the order was placed. The date appears in calendar format. |
| DISPLAY_NAME | VARCHAR (510) | The name of the medication as it appears on the medication record itself. |
| AS_MEDICATION_ID | NUMERIC (18,0) | The unique ID of the brand name medication originally chosen by the ordering user. This column is blank if the user did not chose a brand name record.  It is recommended to use the Clarity column ORDER_MEDINFO.DISPENSABLE_MED_ID when reporting on medication orders. Use AS_MEDICATION_ID if specifically searching for orders that were originally selected from a preference list as a brand name medication. |
| HV_HOSPITALIST_YN | VARCHAR (1) |  |
| PROV_STATUS *(deprecated)* | VARCHAR (255) |  |
| ORDER_PRIORITY_C | INTEGER |  |
| COSIGN_AUTH_TIME *(deprecated)* | DATETIME | This column is no longer used.  Refer to tables ORDER_SIGNED_MED and ORDER_SIGNED_PROC for cosign information.  The deprecated column's content/data is no longer available since it is no longer populated in Chronicles. |
| COSIGN_USER_ID *(deprecated)* | VARCHAR (18) | This column is no longer used.  Refer to tables ORDER_SIGNED_MED and ORDER_SIGNED_PROC for cosign information.  The deprecated column's content/data is no longer available since it is no longer populated in Chronicles. |
| MED_ROUTE_C | INTEGER |  |
| DISCON_USER_ID | VARCHAR (18) | The unique ID of the user who discontinued the order. |
| DISCON_TIME | DATETIME (UTC) | The date and time when the medication order was discontinued. The date appears in calendar format. |
| CHNG_ORDER_MED_ID | NUMERIC (18,0) | The unique ID of the changed or reordered medication order that this order replaced. This column is frequently used to link back to the ORDER_MED table. |
| PEND_APPR_USER_ID | VARCHAR (18) | The unique ID of the user who approved a pended order. |
| PEND_APPR_FLAG *(deprecated)* | VARCHAR (255) |  |
| PEND_REF_REAS_C | INTEGER |  |
| HV_DISCR_FREQ_ID | VARCHAR (18) | The unique ID of the discrete frequency record associated with this medication order. This column is frequently used to link to the IP_FREQUENCY table. |
| HV_DISCRETE_DOSE | VARCHAR (254) | The discrete dose for a medication as entered by the user in the orders activity. |
| HV_DOSE_UNIT_C | INTEGER |  |
| ORDERING_MODE *(deprecated)* | VARCHAR (255) |  |
| HV_IS_SELF_ADM_YN | VARCHAR (1) |  |
| ORDER_START_TIME | DATETIME (Local) | The date and time when the medication order is to start. The date appears in calendar format. |
| ORDER_END_TIME | 7069 | The date and time when the medication order is scheduled to end. The date appears in calendar format. |
| HV_VERBAL_YN *(deprecated)* | VARCHAR (1) |  |
| HV_VERBAL_PROV_ID *(deprecated)* | VARCHAR (18) | This column is no longer used.  Refer to tables ORDER_SIGNED_MED and ORDER_SIGNED_PROC for verbal information.  The deprecated column's content/data is no longer available since it is no longer populated in Chronicles. |
| HV_VBL_CSG_USER_ID *(deprecated)* | VARCHAR (18) | This column is no longer used.  Refer to tables ORDER_SIGNED_MED and ORDER_SIGNED_PROC for verbal information.  The deprecated column's content/data is no longer available since it is no longer populated in Chronicles. |
| HV_VBL_MSG_USER_ID *(deprecated)* | VARCHAR (18) | This column is no longer used.  Refer to tables ORDER_SIGNED_MED and ORDER_SIGNED_PROC for verbal information.  The deprecated column's content/data is no longer available since it is no longer populated in Chronicles. |
| VERB_CSGN_TIME *(deprecated)* | DATETIME | This column is no longer used.  Refer to tables ORDER_SIGNED_MED and ORDER_SIGNED_PROC for verbal information.  The deprecated column's content/data is no longer available since it is no longer populated in Chronicles. |
| NON_FORMULARY_YN | VARCHAR (1) |  |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| ORDER_STATUS_C | INTEGER |  |
| WORKSTATION_ID | VARCHAR (18) | The unique ID of the workstation record where this order was placed. This column is frequently used to link to the CLARITY_LWS table. |
| AUTHRZING_PROV_ID | VARCHAR (18) | The unique ID of the provider who has prescribed or authorized the medication order. The value in this column matches the value in the MED_PRESC_PROV_ID column. |
| ORD_PROV_ID | VARCHAR (18) | The unique ID of the provider listed as the ordering provider. |
| RX_SESSRPT_DONE_YN | VARCHAR (254) |  |
| MIN_DISCRETE_DOSE | NUMERIC (19,4) | The minimum ordered dose amount for the medication as specified by the user in the orders activity. |
| MAX_DISCRETE_DOSE | NUMERIC (19,4) | The maximum ordered dose amount for the medication as specified by the user in the orders activity. |
| DOSE_UNIT_C | INTEGER |  |
| IS_PENDING_ORD_YN | VARCHAR (254) |  |
| BULK_DISP_YN | VARCHAR (254) |  |
| PROVIDER_TYPE_C | INTEGER |  |
| PAT_LOC_ID | NUMERIC (18,0) | The unique ID of the patient's encounter department at the time of signing the medication order. This column is frequently used to link to the CLARITY_DEP table. |
| MODIFY_TRACK_C | VARCHAR (1) |  |
| SPECIFIED_FIRST_TM | DATETIME (Local) | If the order was placed with a Specified frequency (the frequency's Type (I EFQ 50) item has a value of 1) and the user specified a first occurrence time, the time specified is stored in this column. |
| SCHED_START_TM | DATETIME (Local) | The date and time at which an order was scheduled to begin. The date appears in calendar format. |
| ACT_ORDER_C | INTEGER |  |
| PAT_CSN_ID *(deprecated)* | NUMERIC (18,0) | This column is no longer used. Use PAT_ENC_CSN_ID instead. |
| EXP_AFT_START_DATE | DATETIME | The number of days after the start date that the medication order will expire based on the setting in the medication record. The date appears in calendar format. |
| EXP_BEF_END_DATE | DATETIME | The number of days before the end date that the medication order will expire based on the setting in the medication record. The date appears in calendar format. |
| MED_COMMENTS | VARCHAR (1000) | Comments for a medication order, as entered by the ordering user when entering the order. |
| USER_SEL_MED_ID | NUMERIC (18,0) | The unique ID of the orderable medication that is evaluated for Intelligent Medication Selection (IMS). This item is blank if the order is not evaluated for IMS.  It is recommended to use the Clarity column ORDER_MEDINFO.DISPENSABLE_MED_ID when reporting on medication orders. Use USER_SEL_MED_ID if searching for medication orders that were evaluated by IMS. |
| USER_SEL_ERX_DAT | DATETIME | The date that the medication record was actually selected by the user.  This item is populated only if Intelligent Medication Selection (IMS) replaced the original user-selected medication with another medication record. |
| REQ_RNVERIFY_YN | VARCHAR (1) |  |
| MDL_ID | NUMERIC (18,0) | The unique ID of the medication problem list record that is associated with this medication order. This column is frequently used to link to the MDL_MD_PRBLM_LIST table. |
| LASTDOSE | VARCHAR (128) | Comments for the last administered dose of a medication entered in the medication documentation navigator section. |
| INFORMANT_C | INTEGER |  |
| AMB_MED_DISP_NAME | VARCHAR (700) | The name of the ambulatory medication. |
| MRU_EVAL_RXDISP_ID | NUMERIC (18,0) | The unique ID of the department record that is associated with the most recent unit evaluated for Rx dispense logic. Most of the time this will store the current unit the patient is in except for the cases where the current unit is set to ignore Rx dispense logic on transfers. This column is frequently used to link to the CLARITY_DEP table. |
| MRCA_EVAL_RXDISP_ID | NUMERIC (18,0) | The unique ID of the care area that is associated with most recent care area evaluated for Rx dispense logic. This column usually stores the current care area in the patient's department, unless the current unit is set to ignore Rx dispense logic during transfers. This column is frequently used to link to the ED_CARE_AREA_INFO table. |
| CALC_RATE_FRM_VD_YN | VARCHAR (1) |  |
| WEIGHT_BASED_YN | VARCHAR (1) |  |
| WEIGHT_REVIEW_YN | VARCHAR (1) |  |
| ORD_TM_WEIGHT | NUMERIC (18,1) | The patient's last reviewed weight at the time the medication was ordered. |
| ORDER_TIME_WT_INST | DATETIME (Local) | The date and time when a new weight is recorded for a patient for a weight based medication review. |
| REVIEW_WEIGHT | NUMERIC (18,1) | The patient's last non-reviewed weight at the time the medication was ordered. |
| REVIEW_WEIGHT_INST | DATETIME (Local) | The instant when the patient's last non-reviewed weight was entered prior to when the medication was ordered. |
| REFILLS_REMAINING | NUMERIC (18,0) | The number of refills remaining in the medication. |
| MED_REFILL_PROV_ID | VARCHAR (18) | The unique ID of the provider who authorized the medication refill order. |
| OLD_ORDER_ID | NUMERIC (18,0) | The unique ID of the order record that points to the parent medication for refills. |
| OLD_ORDER_DAT | VARCHAR (12) | The internal contact date of the parent medication in integer format.  Used to identify the parent medication and will only be populated for child orders.  This does not link to CONTACT_DATE_REAL. |
| RULE_BASED_ORD_T_YN | VARCHAR (1) |  |
| RESUME_STATUS_C | INTEGER |  |
| USER_ID_OF_PROV | VARCHAR (254) | The unique ID of the user record that is linked to the provider ID in the AUTHRZING_PROV_ID column. |
| LOGIN_DEP_ID | NUMERIC (18,0) | The unique ID of the login department record for the user signing the order. |
| SESSION_KEY | VARCHAR (254) | The session key of this medication order. When a group of orders are signed simultaneously, they share a session key value. |
| ORDERING_MODE_C | INTEGER |  |
| PEND_APPROVE_FLAG_C | INTEGER |  |
| PROV_STATUS_C | INTEGER |  |
| NF_POST_VERIF_YN | VARCHAR (1) |  |
| EXT_ELG_SOURCE_ID | VARCHAR (254) | External eligibility source ID |
| EXT_ELG_MEMBER_ID | VARCHAR (254) | External eligibility member ID |
| EXT_FORMULARY_ID | VARCHAR (254) | External formulary ID |
| EXT_COVERAGE_ID | VARCHAR (254) | External coverage ID |
| EXT_COPAY_ID | VARCHAR (254) | This column contains the external copay ID for an order. |
| EXT_PHARMACY_TYPE_C | INTEGER |  |
| EXT_FORMULARY_STAT | VARCHAR (10) | External Formulary Status |
| EXT_COV_AGE_LMT_YN | VARCHAR (1) |  |
| EXT_COV_EXCLUS_YN | VARCHAR (1) |  |
| EXT_COV_SEX_LMT_YN | VARCHAR (1) |  |
| EXT_COV_MED_NCST_YN | VARCHAR (1) |  |
| EXT_COV_PRI_AUTH_YN | VARCHAR (1) |  |
| EXT_COV_QNTY_LMT_YN | VARCHAR (1) |  |
| EXT_COV_LNK_DRUG_YN | VARCHAR (1) |  |
| EXT_COV_LNK_SMRY_YN | VARCHAR (1) |  |
| EXT_COV_STEP_MED_YN | VARCHAR (1) |  |
| EXT_COV_STEP_THR_YN | VARCHAR (1) |  |
| EXT_COV_TEXT_MSG_YN | VARCHAR (1) |  |
| USR_SEL_IMS_YN | VARCHAR (1) |  |
| INDICATION_COMMENTS | VARCHAR (300) | The comment entered for the indications of use for this order. |
| DOSE_ADJ_TYPE_C | INTEGER |  |
| DOSE_ADJ_OVERRID_YN | VARCHAR (1) |  |
| MAX_DOSE | NUMERIC (18,4) | The maximum allowed dose for this medication order. |
| MAX_DOSE_UNIT_C | INTEGER |  |
| PRN_COMMENT | VARCHAR (450) | The user-entered comments for why the as needed (PRN) medication should be administered. |
| INST_OF_UPDATE_TM | DATETIME (Local) | The day and time the order record was last updated. |
| PEND_ACTION_C | INTEGER |  |
| MED_DIS_DISP_QTY | NUMERIC (19,4) | This item stores the discrete dispense quantity when discrete dispense is enabled. |
| MED_DIS_DISP_UNIT_C | INTEGER |  |
| END_BEFORE_CMP_INST | 7065 | The default end date and time of a completed order.  When an order is completed, we will store the system calculated end date and time (which may differ from the actual completion time) in this column in the event the completion is reversed and the defaults need to be restored. |
| BSA_BASED_YN | VARCHAR (1) |  |
| BSA_REVIEW_YN | VARCHAR (1) |  |
| ORD_TM_BSA | NUMERIC (18,2) | The patient's last reviewed BSA at the time this order was placed. |
| REVIEW_BSA | NUMERIC (18,2) | The patient's last non-reviewed body surface areas (BSA) at the time the medication was ordered. |
| LAST_DOSE_TIME | VARCHAR (254) | Store the time that a PTA med was last taken. |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| BITMAP INDEX | EIX_ORDER_MED_AUTH_PROV_ID | AUTHRZING_PROV_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_ORDER_MED_CSN_INST | PAT_ENC_CSN_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_ORDER_MED_CSN_INST | ORDER_INST | 2 | Yes | Yes |  |
| B-TREE INDEX | EIX_ORDER_MED_DISCON_INST | DISCON_TIME | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_ORDER_MED_ID_INCL_OSEDIMO | PAT_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_ORDER_MED_ID_INCL_OSEDIMO | ORDERING_DATE | 2 | Yes | No |  |
| B-TREE INDEX | EIX_ORDER_MED_ID_INCL_OSEDIMO | START_DATE | 3 | Yes | No |  |
| B-TREE INDEX | EIX_ORDER_MED_ID_INCL_OSEDIMO | END_DATE | 4 | Yes | No |  |
| B-TREE INDEX | EIX_ORDER_MED_ID_INCL_OSEDIMO | DISCON_TIME | 5 | Yes | No |  |
| B-TREE INDEX | EIX_ORDER_MED_ID_INCL_OSEDIMO | IS_PENDING_ORD_YN | 6 | Yes | No |  |
| B-TREE INDEX | EIX_ORDER_MED_ID_INCL_OSEDIMO | MDL_ID | 7 | Yes | No |  |
| B-TREE INDEX | EIX_ORDER_MED_ID_INCL_OSEDIMO | ORDERING_MODE_C | 8 | Yes | No |  |
| B-TREE INDEX | EIX_ORDER_MED_MEID | MEDICATION_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_ORDER_MED_ORD_INST | ORDER_INST | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_ORDER_MED_PAID_CMP | PAT_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_ORDER_MED_PAID_CMP | PAT_ENC_DATE_REAL | 2 | Yes | Yes |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ORDER_MED_ID | ADT_ORDERS_ERRORS | ORDER_ID | No | No | No |  |
| 1 | ORDER_MED_ID | ADT_ORDER_INFORMATION | ORDER_ID | No | No | No |  |
| 1 | ORDER_MED_ID | APPT_REQUEST | REQUEST_ID | No | No | No |  |
| 1 | ORDER_MED_ID | CL_ORD_FST_LST_SCH | ORDER_ID | No | No | No |  |
| 1 | ORDER_MED_ID | DENT_ORD_NOADD | ORDER_ID | No | No | No |  |
| 1 | ORDER_MED_ID | DUPMED_DISMISS_HH_INFO | ORDER_ID | No | No | No |  |
| 1 | ORDER_MED_ID | ENDOSCOPY_METRICS | ORDER_ID | Unknown | No | No |  |
| 1 | ORDER_MED_ID | EXTERNAL_ORDER_INFO | ORDER_ID | No | No | No |  |
| 1 | ORDER_MED_ID | F_IMG_STUDY | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_MED_ID | F_IP_HSP_SUM_ORDER | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_MED_ID | F_LAB_ORDERS | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_MED_ID | F_MU_OBJ_EH_PLACED_ORDER | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_MED_ID | F_MU_OBJ_EH_RESULTD_ORDER | ORDER_PROC_ID | Unknown | Unknown | No |  |
| 1 | ORDER_MED_ID | F_ONC_PRIOR_AUTH_ORDERS | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_MED_ID | F_OPIOID_ORDERS | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_MED_ID | F_RX_ORDER | ORDER_MED_ID | Unknown | Unknown | No |  |
| 1 | ORDER_MED_ID | HH_MED_ORD_IN_POC_DETAIL | ORDER_MED_ID | No | No | No |  |
| 1 | ORDER_MED_ID | HV_ORDER_PROC | ORDER_PROC_ID | Unknown | No | No |  |
| 1 | ORDER_MED_ID | MED_DETAILS_EXT_ORD | ORDER_ID | No | No | No |  |
| 1 | ORDER_MED_ID | MERCHANDISE_ORDER_INFO | ORDER_ID | Yes | No | No |  |
| 1 | ORDER_MED_ID | MU_EH_QRDA_I_ORDER | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_MED_ID | ORDERS | ORDER_ID | No | No | No |  |
| 1 | ORDER_MED_ID | ORDER_AUTH_INFO | ORDER_ID | No | No | No |  |
| 1 | ORDER_MED_ID | ORDER_MEDINFO | ORDER_MED_ID | Unknown | No | No |  |
| 1 | ORDER_MED_ID | ORDER_MED_2 | ORDER_ID | Unknown | No | No |  |
| 1 | ORDER_MED_ID | ORDER_MED_3 | ORDER_ID | Unknown | No | No |  |
| 1 | ORDER_MED_ID | ORDER_MED_4 | ORDER_ID | Unknown | No | No |  |
| 1 | ORDER_MED_ID | ORDER_MED_5 | ORDER_ID | Unknown | No | No |  |
| 1 | ORDER_MED_ID | ORDER_MED_6 | ORDER_MED_ID | Unknown | No | No |  |
| 1 | ORDER_MED_ID | ORDER_MED_7 | ORDER_ID | No | No | No |  |

_(598 total; showing first 30)_
