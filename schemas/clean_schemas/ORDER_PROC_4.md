# ORDER_PROC_4

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=ORDER_PROC_4

## Description

The ORDER_PROC_4 table enables you to report on the procedures ordered in the clinical system. This procedure table has the same basic structure as ORDER_PROC, but was created as a fourth table to prevent ORDER_PROC_3 from getting any larger.

**Overflow table** for ORDER_PROC (102 cols). Contains additional columns for the same records — join on the shared primary key column.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | ORD |
| Release Version | Rel 2012 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| ORDER_ID | NUMERIC (18,0) | The unique ID of the order record for this row. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| QUESR_SERIES_ID | NUMERIC (18,0) | This item stores the questionnaire series that the patient is being assigned to using this order. |
| QUESR_SERIES_ANS_ID | NUMERIC (18,0) | Contains a pointer to the assignment record (HQW) created whne the questionnaire series is assigned to the patient. |
| LAST_MAMMO_ORD_ID | NUMERIC (18,0) | The last breast procedure that was performed on this patient prior to this order. |
| LAST_MAMMO_LOC_ID | NUMERIC (18,0) | Where the last breast procedure was performed. If it was performed by the current organization, this field will be empty |
| LAST_MAMMO_PROC_NAM | VARCHAR (254) | The last breast procedure that was performed. This field allows you to freely specify a procedure name in case it was performed outside the organization. |
| LAST_MAMMO_DATE | DATETIME | The date when the last breast procedure was performed. |
| LAST_MAMMO_WEIGHT | NUMERIC (18,2) | The patient's weight (oz.) at the last breast procedure. |
| EXAM_MAMMO_WEIGHT | NUMERIC (18,2) | The patient's weight (oz.) at the time of this procedure. |
| LAST_MAM_WT_RECD_DT | DATETIME | The date when the weight at last breast procedure was recorded. |
| EXAM_MAM_WT_RECD_DT | DATETIME | The date when patient's current weight was recorded. |
| MAM_HX_REVD_USER_ID | VARCHAR (18) | The last person to review the last breast procedure information. |
| MAMMO_BASELINE_YN | VARCHAR (1) |  |
| LAST_MAMMO_EXT_YN | VARCHAR (1) |  |
| MAMMO_WEIGHT_CHANGE | NUMERIC (18,2) | The patient's weight change (oz.). |
| MAM_WT_CHNG_RECD_DT | NUMERIC (18,2) | The date the patient's weight change was recorded. |
| CASELOG_PREF_CRD_ID | VARCHAR (254) | The preference card in the case (ORC) or log (ORL) that this order is associated with. |
| MAM_HORMONE_NONE_YN | VARCHAR (1) |  |
| MAMMO_HX_REVD_DTTM | DATETIME (UTC) | The instant the last breast procedure information was reviewed. |
| MAM_HORMNE_REV_U_ID | VARCHAR (18) | The last user to review the hormone history. |
| MAM_HORMNE_REV_DTTM | DATETIME (UTC) | The instant the hormone history was last reviewed. |
| BREAST_SELF_EXAM_C | INTEGER |  |
| RIS_LTR_NOT_NEED_YN | VARCHAR (1) |  |
| MQSA_EXCLD_ON_DTTM | DATETIME (UTC) | Instant on which this order was excluded from MQSA reports. |
| MQSA_EXCLD_RSN_ID | VARCHAR (254) | Free text explanation of why this order is excluded from MQSA statistics. Use this column to join to the HNO_NOTE_TEXT table on the NOTE_ID column to obtain the reason text. |
| MQSA_EXCLD_USER_ID | VARCHAR (18) | User that excluded this order from mammography MQSA reports. |
| REQ_PER_PERIOD | INTEGER | Requested units/visits per period.  This along with the Requested periods (REQ_PERIODS) determines the total 'requested units'. |
| REQ_FREQ_C | INTEGER |  |
| REQ_PERIODS | INTEGER | Requested periods. Requested units per period (REQ_PER_PERIOD) along with the requested periods determines the total 'requested units'. |
| APPR_PER_PERIOD | INTEGER | Approved units/visits per period. This along with the approved periods (APPR_PERIODS) determines the total 'approved units'. |
| APPR_FREQ_C | INTEGER |  |
| APPR_PERIODS | INTEGER | Approved periods.  Also known as duration. Approved units per period (APPR_PER_PERIOD) along with the approved periods determines the total 'approved units'. |
| PROC_LNC_ID | NUMERIC (18,0) | LOINC ID associated with the procedure. |
| PROC_LNC_SOURCE_C | INTEGER |  |
| ABNORMAL_NOADD_YN | VARCHAR (1) |  |
| NUM_IMGS_PERFORMED | INTEGER | The number of images performed by a tech during the imaging exam linked to this order. This number is a total for the exam and includes images done on other procedures linked to the same appointment. |
| IPROC_STATUS_C | INTEGER |  |
| SPEC_DRAW_TYPE_C | INTEGER |  |
| TYPE_SNOMED_SRC_C | INTEGER |  |
| SOURCE_SNOMED_SRC_C | INTEGER |  |
| POTENTIAL_ADDON_YN | VARCHAR (1) |  |
| SELECTED_ADDON_YN | VARCHAR (1) |  |
| ADDON_PERFORMED_YN | VARCHAR (1) |  |
| ANTICOAG_INR_GOAL_C | INTEGER |  |
| ANTICOAG_RESP_POOL_ID | NUMERIC (18,0) | Pool of providers responsible for a patient on anticoagulation therapy. |
| ANTICOAG_NEXT_INR_DT | DATETIME | The date of the next International Normalized Ratio (INR) check for a patient on anticoagulation therapy. |
| ANTICOAG_WEEKLY_MAX_DOSE | NUMERIC (18,1) | Weekly maximum dose of anticoagulant for a patient on anticoagulation therapy. |
| ANTICOAG_TARGET_END_DT | DATETIME | Targeted end date for the patient's anticoagulation therapy. |
| ANTICOAG_INDEFINITE_YN | VARCHAR (1) |  |
| IPROC_STATUS_INST_DTTM | DATETIME (Local) | The instant of the last Imaging and Procedure (IProc) status update of an order. |
| SCREENING_FORM_ID | NUMERIC (18,0) | The unique ID of the screening form linked to the order. |
| SUBMITTER_ID | NUMERIC (18,0) | The unique ID of the external site (submitter) associated that originally placed the order. |
| BILL_TO_SUBMITTER_C | INTEGER |  |
| INDICATION_COMMENTS | VARCHAR (300) | The comment entered for the indications of use for this order. |
| COLL_END_DT | DATETIME | This is the end date for an observation. This typically equates to the end date of a specimen collection or the end date of a procedure. |
| COLL_END_TM | DATETIME | This is the end time for an observation. This typically equates to the end time of a specimen collection or the end time of a procedure. |
| COLL_AMT | VARCHAR (254) | The amount of specimen that was collected. The identifier for the units for this amount are in COLL_AMT_UNIT_ID. |
| COLL_AMT_UNIT_ID | NUMERIC (18,0) | The unique identifier for unit of the specimen collection amount (COLL_AMT) for this order. |
| DEST_ANCILLARY_C | INTEGER |  |
| INTENDED_MGMT_C | INTEGER |  |
| RFL_DIF_PROB_YN | VARCHAR (1) |  |
| PROC_INSTR_SAVED_YN | VARCHAR (1) |  |
| REF_TO_PROV_ADDR_ID | VARCHAR (254) | Address selected for the referred-to provider. Format: {External provider ID}-{Address Line #} |
| WORKSTATION_ID | VARCHAR (18) | The unique ID of the workstation record where this order was placed. This column is frequently used to link to the CLARITY_LWS table. |
| REFLEX_SOURCE_C | INTEGER |  |
| DEST_ANCLY_OVRIDE_YN | VARCHAR (1) |  |
| BREAST_IMG_TYPE_C | INTEGER |  |
| ROUT_THREAD_ID | NUMERIC (18,0) | Stores In Basket message thread created when signing an order (Ex: During E-Consult workflow) |
| NOT_CHARGE_FLAG_YN *(deprecated)* | VARCHAR (1) |  |
| NOT_CHARGE_REASON_C *(deprecated)* | INTEGER |  |
| NOT_CHARGE_USER_ID *(deprecated)* | VARCHAR (18) |  |
| NOT_CHARGE_COMMENT *(deprecated)* | VARCHAR (508) |  |
| IMG_PRIMARY_ORD_ID | NUMERIC (18,0) | The order ID (.1) of the primary order containing an order's linked images. |
| OTX_LBL_PRT_ID | NUMERIC (18,0) | The item will hold the label printer filled in the multi-step or multi-step collection form and will be used by the interface. |
| SCHED_DUR | INTEGER | The amount of time (in minutes) the order will contribute to an appointment |
| SCHED_DUR_IS_CALC_YN | VARCHAR (1) |  |
| SCHED_DUR_BUFFER | INTEGER | The amount of time (in minutes) that should be added to system calculated scheduling duration as a buffer. |
| SCHED_TOL_BEF | INTEGER | How far before the expected date for the order the appointment can still be safely made. |
| SCHED_TOL_AFTR | INTEGER | How long after the expected date for the order the appointment can still be safely made. |
| SCHED_TOL_NO_RESTR_BEF_YN | VARCHAR (1) |  |
| SCHED_TOL_NO_RESTR_AFTR_YN | VARCHAR (1) |  |
| NOT_CHARGE_UTC_DTTM *(deprecated)* | DATETIME (UTC) |  |
| SCHED_STATUS_C | INTEGER |  |
| RETURN_REASON_C | INTEGER |  |
| LAST_SCHEDULED_UTC_DTTM | DATETIME (UTC) | The date and time when the order was last scheduled or linked to an existing appointment. This information does not apply to and is not populated for standing orders. |
| REMOVAL_INSTANT_DTTM | DATETIME (Attached) | The date and time when the order was removed from the schedule orders workqueue or worklist. The information is only populated for orders that are currently removed and were removed manually by a user. |
| REMOVED_BY_USER_ID | VARCHAR (18) | The unique ID of the user who removed the order from the order scheduling worklist or workqueue. |
| REMOVAL_COMMENTS | VARCHAR (254) | Free text comments entered by the user who removed an order from the scheduling workqueue or worklist explaining why the order was removed. |
| RETURN_RSN_REMOVE_C | INTEGER |  |
| PROTOCOLLED_ORD_ID | NUMERIC (18,0) | For an order that was placed from an imaging protocol, this item contains the protocolled imaging procedure order from which the order was placed. This item can be used to help associate contrast, medication, and point-of-care lab test orders with the protocolled procedure orders for which they were placed. |
| PROTOCOL_SOURCE_ID | NUMERIC (18,0) | This item stores a pointer to the last order record that had its protocol edited by a user. When a protocol is edited this item should be populated on the order record that was edited. When a protocol is copied forward to another order record, this item should be populated on the destination order. |
| FINAL_APPROVAL_YN | VARCHAR (1) |  |
| GEN_CAT_C | INTEGER |  |
| PRIME_SER_RECIPIENT_ID | VARCHAR (18) | Stores SER of primary recipient. This is used to store the primary recipient for a result that has been received on the incoming interface. This item stores the recipient if it is an SER record. Also see items 2131 and 2132. Results Routing does not consider this item as it is only used for audit trail purposes. |
| PRIME_EAF_RECIPIENT_ID | NUMERIC (18,0) | Stores EAF of primary recipient. This is used to store the primary recipient for a result that has been received on the incoming interface. This item stores the recipient if it is an EAF record. Also see items 2130 and 2132. Results Routing does not consider this item as it is only used for audit trail purposes. |
| PRIME_TEX_RECIPIENT | VARCHAR (254) | Stores free text of primary recipient. This is used to store the primary recipient for a result that has been received on the incoming interface. This item stores the recipient if it is not an SER or EAF record. Also see items 2130 and 2131. Results Routing does not consider this item as it is only used for audit trail purposes. |
| CC_SER_RECIPIENT_ID | VARCHAR (18) | Stores SER of CC recipient. This is used to store the cc recipient for a result that has been received on the incoming interface. This item stores the recipient if it is an SER record. Also see items 2134 and 2135. Results Routing does not consider this item as it is only used for audit trail purposes. |
| CC_EAF_RECIPIENT_ID | NUMERIC (18,0) | Stores EAF of CC recipient. This is used to store the CC recipient for a result that has been received on the incoming interface. This item stores the recipient if it is an EAF record. Also see items 2133 and 2135. Results Routing does not consider this item as it is only used for audit trail purposes. |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ORDER_ID | ADT_ORDERS_ERRORS | ORDER_ID | No | No | No |  |
| 1 | ORDER_ID | ADT_ORDER_INFORMATION | ORDER_ID | No | No | No |  |
| 1 | ORDER_ID | APPT_REQUEST | REQUEST_ID | No | No | No |  |
| 1 | ORDER_ID | CL_ORD_FST_LST_SCH | ORDER_ID | No | No | No |  |
| 1 | ORDER_ID | DENT_ORD_NOADD | ORDER_ID | No | No | No |  |
| 1 | ORDER_ID | DUPMED_DISMISS_HH_INFO | ORDER_ID | No | No | No |  |
| 1 | ORDER_ID | ENDOSCOPY_METRICS | ORDER_ID | Unknown | No | No |  |
| 1 | ORDER_ID | EXTERNAL_ORDER_INFO | ORDER_ID | No | No | No |  |
| 1 | ORDER_ID | F_IMG_STUDY | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_ID | F_IP_HSP_SUM_ORDER | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_ID | F_LAB_ORDERS | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_ID | F_MU_OBJ_EH_PLACED_ORDER | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_ID | F_MU_OBJ_EH_RESULTD_ORDER | ORDER_PROC_ID | Unknown | Unknown | No |  |
| 1 | ORDER_ID | F_ONC_PRIOR_AUTH_ORDERS | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_ID | F_OPIOID_ORDERS | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_ID | F_RX_ORDER | ORDER_MED_ID | Unknown | Unknown | No |  |
| 1 | ORDER_ID | HH_MED_ORD_IN_POC_DETAIL | ORDER_MED_ID | No | No | No |  |
| 1 | ORDER_ID | HV_ORDER_PROC | ORDER_PROC_ID | Unknown | No | No |  |
| 1 | ORDER_ID | MED_DETAILS_EXT_ORD | ORDER_ID | No | No | No |  |
| 1 | ORDER_ID | MERCHANDISE_ORDER_INFO | ORDER_ID | Yes | No | No |  |
| 1 | ORDER_ID | MU_EH_QRDA_I_ORDER | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_ID | ORDERS | ORDER_ID | No | No | No |  |
| 1 | ORDER_ID | ORDER_AUTH_INFO | ORDER_ID | No | No | No |  |
| 1 | ORDER_ID | ORDER_MED | ORDER_MED_ID | Unknown | No | No |  |
| 1 | ORDER_ID | ORDER_MEDINFO | ORDER_MED_ID | Unknown | No | No |  |
| 1 | ORDER_ID | ORDER_MED_2 | ORDER_ID | Unknown | No | No |  |
| 1 | ORDER_ID | ORDER_MED_3 | ORDER_ID | Unknown | No | No |  |
| 1 | ORDER_ID | ORDER_MED_4 | ORDER_ID | Unknown | No | No |  |
| 1 | ORDER_ID | ORDER_MED_5 | ORDER_ID | Unknown | No | No |  |
| 1 | ORDER_ID | ORDER_MED_6 | ORDER_MED_ID | Unknown | No | No |  |

_(608 total; showing first 30)_
