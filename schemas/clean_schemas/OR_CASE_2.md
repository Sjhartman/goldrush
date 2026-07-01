# OR_CASE_2

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=OR_CASE_2

## Description

The OR_CASE_2 table enables you to report on surgical and procedural case data. This table has the same basic structure as OR_CASE, but was created as a second table to prevent OR_CASE from getting any larger.

**Overflow table** for OR_CASE (134 cols). Contains additional columns for the same records — join on the shared primary key column.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | ORC |
| Release Version | Summer 2009 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| CASE_ID | VARCHAR (18) | The unique ID for the case request record. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| SURGICAL_RISK_C | INTEGER |  |
| POTENTL_BLOODLOSS_C | INTEGER |  |
| AWARENESS_DT | DATETIME | This column contains the date the patient was made aware of the surgery in the case record. |
| READY_TO_SCHED_C | INTEGER |  |
| SURGEON_REQ_LEN | INTEGER | This column contains the surgeon requested length for the case in the case record. |
| PAT_PAGER_NUM | VARCHAR (126) | This column contains the patient pager number assigned in the case record. |
| SPEC_NEED_RESOLV_DT | DATETIME | This column contains the date special needs were resolved in the case record. |
| AUTH_PROV_ID | VARCHAR (18) | Item to store the authorizing provider for the case. |
| PAT_START_TIME | DATETIME (Local) | Shows the time the patient is scheduled to arrive at the OR. |
| OB_CSECT_TYPE_C | INTEGER |  |
| INSTANT_OF_UPD_DTTM | DATETIME (Local) | Date and time the record was updated. |
| REC_ARCHIVED_YN | No | Indicates whether the Case Request record is archived at the record level. |
| CASE_PULLED_C | INTEGER |  |
| RSN_RETURN_OR_C | INTEGER |  |
| CONSULT_ROOM_C | INTEGER |  |
| INTER_BETWEEN_CASES | INTEGER | The number of days that should be between two cases. |
| PAT_FIRST_AVAIL_DT | DATETIME | The date the patient is first available for surgery. |
| PAT_COMPLEXITY_C | INTEGER |  |
| ANES_APPROVAL_DATE | DATETIME | The date anesthesia was approved. |
| APPROX_HEIGHT | NUMERIC (18,1) | The approximate height of the patient in inches. |
| INS_SELF_PAY_YN | VARCHAR (1) |  |
| PRE_OP_BED_ID | VARCHAR (18) | The patient's pre-op bed can be entered in the case, prior to their arrival. |
| INTRAOP_XRAYS_CMT | VARCHAR (254) | This column displays the comment about  intraop x-ray needs in a case. |
| TRANSLATN_NEEDS_CMT | VARCHAR (254) | This column displays the comment about translation needs in a case. |
| LASER_NEEDS_COMMENT | VARCHAR (254) | This column displays the comment about specific laser needs in a case. |
| PAT_LABEL_PRINTED_C | INTEGER |  |
| READY_TO_SCHED_DTTM | DATETIME (Local) | This column displays the date and time that a case was marked as ready to schedule in order to help end-users prioritize cases when scheduling. |
| IOP_XRAYS_C | INTEGER |  |
| ARE_PROPH_AB_REQ_C | INTEGER |  |
| PAT_SCHED_NOTICE | INTEGER | Store number of days notice patient needs before surgery. |
| CLASS_APPROP_C | INTEGER |  |
| REVISD_CASE_CLASS_C | INTEGER |  |
| PREOP_VISIT_STAT_C | INTEGER |  |
| ADMIT_TYPE_C | VARCHAR (66) |  |
| LAST_CANCELED_CASE_ID | VARCHAR (18) | Stores the id of a canceled case that is linked to the current case. |
| CANCELED_AT_LAST_MINUTE_YN | VARCHAR (1) |  |
| CANCEL_TARGET_DT | DATETIME | Stores the target date associated with the last minute canceled case. The target date is the date by which the last minute canceled case should be rescheduled to avoid a breach. |
| IGNORE_TARGET_DATE_YN | VARCHAR (1) |  |
| IGNORE_TARGET_DATE_REASON_C | INTEGER |  |
| TARGET_IGNORE_SET_BY_USER_ID | VARCHAR (18) | Stores the ID of the user who flags the last minute canceled case to ignore the target date. The target date is the date by which the last minute canceled case should be rescheduled to avoid a breach. |
| LAST_MIN_CANC_ORIGINAL_SURG_DT | DATETIME | Stores the original surgery date associated with the last minute canceled case. Original surgery date is the scheduled surgery date when the case is canceled at the last minute for the first time. |
| VERBAL_ORDER_MODE_C | INTEGER |  |
| IN_OR_TO_PROC_LEN | INTEGER | Records the estimated time to prep the patient from the time wheeled into the room until the procedure starts. |
| CLOSE_TO_OUT_OR_LEN | INTEGER | Records the estimated time between the procedure ending and the patient being wheeled out of the room. |
| POSTOP_BED1_TYPE_C | INTEGER |  |
| POSTOP_BED1_DAYS_NEEDED | INTEGER | The length in days the first post-op bed will be needed. |
| POSTOP_BED1_PROV_ID | VARCHAR (18) | The unique ID of the record used for availability checking of the first post-op bed requested at the time of scheduling. |
| POSTOP_BED2_TYPE_C | INTEGER |  |
| POSTOP_BED2_DAYS_NEEDED | INTEGER | The length in days the second post-op bed will be needed. |
| POSTOP_BED2_PROV_ID | VARCHAR (18) | The unique ID of the record used for availability checking of the second post-op bed requested at the time of scheduling. |
| CASE_REQUESTED_DTTM | DATETIME (Local) | Stores the instant that the case was requested prior to the case being created in the system. Most likely used in emergent cases where the patient is admitted prior to the case being created. |
| INV_QUICK_CASE_YN | VARCHAR (1) |  |
| QUICKCASE_ARRIVCT_C | VARCHAR (66) |  |
| CUSTOM_STATUS_C | INTEGER |  |
| OR_CASE_HIDDEN_YN | VARCHAR (1) |  |
| DECISION_TO_TREAT_DATE | DATETIME | The date that the decision was made to treat the patient. |
| REFERRAL_DATE | DATETIME | The date of the referral. |
| CONSULT_DATE | DATETIME | The date of the consult. |
| CASE_ID_COPIED_FROM | VARCHAR (18) | The Case ID that this case was copied from. |
| IS_RESCHEDULE_YN | VARCHAR (1) |  |
| TARGET_DATE | DATETIME | The date by which the procedure should be performed. This Target Date is calculated by LPP 50723 using rules and associated access targets, as well as Wait 2 Patient Delays documented for this case. |
| WAIT2_PRIORITY_C | INTEGER |  |
| WAIT1_PRIORITY_C | INTEGER |  |
| RESP_FOR_PAYMENT_C | INTEGER |  |
| NO_REFERRAL_FOL_UP_REASON_C | INTEGER |  |
| REFERRAL_SOURCE_C | INTEGER |  |
| REFERRAL_TYPE_C | INTEGER |  |
| FOLLOWUP_APPT_DTTM | 7616 | This item stores the time and date of a patient's post surgical follow-up appointment. |
| WTIS_DX_CAT_C | INTEGER |  |
| WTIS_INTENT_SURGERY_C | INTEGER |  |
| WTIS_PEDIATRIC_YN | VARCHAR (1) |  |
| WTIS_SERVICE_AREA_C | INTEGER |  |
| WTIS_SERVICE_DETAIL_1_C | INTEGER |  |
| WTIS_SERVICE_DETAIL_2_C | INTEGER |  |
| WTIS_PROC_CODE | VARCHAR (254) | This item contains the full WTIS procedure code for a case. |
| WTIS_WAIT_LIST_ID | VARCHAR (20) | Stores the wait list ID of the WTIS wait list for the case. This item is automatically generated by the system based on the case ID. The wait list ID is in the format <case ID> or <case ID>.<unique number>. |
| WTIS_WAIT_LIST_CREATED_YN | VARCHAR (1) |  |
| PREOP_REQUESTED_VISIT_DTTM | 7612 | This column stores the date/time for the requested pre-op visit. |
| GRAVIDITY | INTEGER | The number of times the patient has been pregnant. |
| PARITY | INTEGER | The number of pregnancies the patient has carried to viable gestational age. |
| DESIRED_DTTM | DATETIME (UTC) | The desired date and time to schedule the patient's planned C-section. |
| EST_DUE_DATE | DATETIME | The expected date of delivery/estimated date of confinement. |
| DESIRED_DATE_GEST_AGE | NUMERIC (18,2) | The gestational age, in weeks, of the baby at the time of the desired date of the patient's planned C-section. |
| WTIS_CODE_PROC_C | VARCHAR (66) |  |
| RSN_FOR_QUEUE_C | INTEGER |  |
| SERVICE_TARGET_EFFORT_YN | VARCHAR (1) |  |
| P_CATS_CODE_C | VARCHAR (66) |  |
| EXPECTED_ADMISSION_TIME | DATETIME (Local) | This item stores the time the patient is expected to be admitted for surgery, as documented in the surgical case in I ORC 7617 - EXPECTED ADMISSION TIME. Column PAT_ENC_HSP__EXP_ADMISSION_TIME should be used to report on the expected admission date and time for the admission linked to the surgery (I EPT 10301 - EXPECTED ADMISSION DATE and I EPT 10300 - EXPECTED ADMISSION TIME).  If a time is set in I ORC 7617, the expected admission time in the linked admission is set to that time. If I ORC 7617 is not set, the expected admission time in the linked admission is calculated as the scheduled surgery time (OR_CASE__TIME_SCHEDULED) minus the number of hours in OR_CASE_2__EXPECTED_ADMISSION_TIME_OFFSET. If multiple cases are linked to the same admission, the earliest time from the list of linked cases will be set as the expected admission time on the linked admission. |
| OPERATION_INTENTION_C | INTEGER |  |
| TRIAGE_SCORE | INTEGER | Stores a triage score for the case. This information would be obtained from a third-party. |
| REGISTRY_SCORE | INTEGER | Stores a registry score for the case. This information would be obtained from a third-party. |
| ACATS_CODE_C | VARCHAR (66) |  |
| EXTERNAL_STATUS_C | INTEGER |  |
| PREP_TIME_MOD_YN | VARCHAR (1) |  |
| REC_MAX_WAIT_TIME | NUMERIC (18,2) | Calculated recommended maximum wait time (RMWT) for a case. |
| EXPECTED_ADMISSION_TIME_OFFSET | NUMERIC (18,2) | The number of hours prior to surgery that the patient will be admitted. |
| POSTOP_LEVEL_OF_CARE_C | VARCHAR (66) |  |
| POSTOP_DEPT_ID | NUMERIC (18,0) | This item stores the planned post-op department for this case. |
| CASE_ACCESS_UTC_DTTM | DATETIME (UTC) | Date and time of the last time case entry was opened. |
| RECORD_STATUS_C | INTEGER |  |
| LINK_CREATED_YN | VARCHAR (1) |  |
| CLASS_REVIEW_DATE | DATETIME | The most recent time clinical prioritization was reviewed. |
| CLINICAL_SAFE_DATE | DATETIME | How long clinical prioritization is valid. |
| NHSN_TRAUMA_ORC_YN | VARCHAR (1) |  |
| TRAUMA_CASE_ORC_YN | VARCHAR (1) |  |
| NHSN_EMERG_ORC_YN | VARCHAR (1) |  |
| CENTRAL_INTAKE_NUMBER | VARCHAR (254) | This stores the Central Intake Number also called RAC number. |
| VISIT_DUE_DATE | DATETIME | The Visit Due Date for the case. |
| CASE_VERIFIED_C | INTEGER |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | CASE_ID | OR_CASE | OR_CASE_ID | Unknown | No | No |  |
| 1 | CASE_ID | OR_CASE_3 | CASE_ID | Unknown | No | No |  |
| 1 | CASE_ID | OR_CASE_4 | OR_CASE_ID | No | No | No |  |
| 1 | CASE_ID | OR_CASE_VIRTUAL | OR_CASE_ID | No | No | No |  |
| 1 | CASE_ID | V_OR_CASE_ORR | CASE_ID | Unknown | Unknown | No |  |
| 2 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 2 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 2 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 3 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 4 | SURGICAL_RISK_C | ZC_OR_RISK | RISK_C | No | No | No |  |
| 5 | POTENTL_BLOODLOSS_C | ZC_OR_BLOODLOSS | POTENTL_BLOODLOSS_C | No | No | No |  |
| 7 | READY_TO_SCHED_C | ZC_READY_TO_SCHED | READY_TO_SCHED_C | No | No | No |  |
| 11 | AUTH_PROV_ID | CLARITY_SER | PROV_ID | Unknown | No | No |  |
| 11 | AUTH_PROV_ID | CLARITY_SER_2 | PROV_ID | Unknown | No | No |  |
| 11 | AUTH_PROV_ID | CLARITY_SER_3 | PROV_ID | Unknown | No | No |  |
| 11 | AUTH_PROV_ID | CLARITY_SER_4 | PROV_ID | No | No | No |  |
| 11 | AUTH_PROV_ID | CLARITY_SER_MYC | PROV_ID | Unknown | No | No |  |
| 11 | AUTH_PROV_ID | D_PROV_PRIMARY_HIERARCHY | PROV_ID | Unknown | Unknown | No |  |
| 11 | AUTH_PROV_ID | ED_SER_SETTINGS | PROV_ID | Unknown | No | No |  |
| 11 | AUTH_PROV_ID | EXT_CAL_PROV_CONFIG | PROV_ID | No | No | No |  |
| 11 | AUTH_PROV_ID | OR_SER_EQUIPMENT | PROV_ID | Unknown | No | No |  |
| 11 | AUTH_PROV_ID | OR_SER_ROOM | PROV_ID | Unknown | No | No |  |
| 11 | AUTH_PROV_ID | PROV_BATCH_LTR_GEN | PROV_ID | Unknown | No | No |  |
| 11 | AUTH_PROV_ID | PROV_GROUP | PROV_ID | No | No | No |  |
| 11 | AUTH_PROV_ID | V_CUBE_D_PROVIDER | PROVIDER_ID | Unknown | Unknown | No |  |
| 13 | OB_CSECT_TYPE_C | ZC_OB_CSECT_TYP_CS | OB_CSECT_TYP_CS_C | No | No | No |  |
| 16 | CASE_PULLED_C | ZC_CASE_PULLED | CASE_PULLED_C | No | No | No |  |
| 17 | RSN_RETURN_OR_C | ZC_RSN_RETURN_OR | RSN_RETURN_OR_C | No | No | No |  |

_(136 total; showing first 30)_
