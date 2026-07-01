# PAT_ENC_2

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=PAT_ENC_2

## Description

This table supplements the PAT_ENC table. It contains additional information related to patient encounters or appointments.

**Overflow table** for PAT_ENC (143 cols). Contains additional columns for the same records — join on the shared primary key column.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | EPT |
| Release Version | SPRING 2007 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| PAT_ENC_CSN_ID | NUMERIC (18,0) | The unique system identifier of the patient encounter. Contact serial number is unique across all patients and all contacts. |
| PAT_ID | VARCHAR (18) | The unique system identifier of the patient record (EPT dot one). |
| PAT_ENC_DATE_REAL | No | This is a numeric representation of the date of this encounter in your system. The integer portion of the number specifies the date of the encounter. The digits after the decimal point indicate multiple visits on one day. |
| CONTACT_DATE | DATETIME | The date on which this patient encounter took place. |
| CM_CT_OWNER_ID | VARCHAR (25) | The contact owner in a CareEverywhere community. |
| MERGE_CT_PRV_EXT_ID | VARCHAR (254) | If it is discovered that 2 patient encounters are actually representing the same appointment, the two can be merged. If this has happened, this column will contain the previous contact external ID. |
| CHECK_IN_NO_VISI_YN | VARCHAR (1) |  |
| COPAY_COINS_FLAG | VARCHAR (254) | Set to 1 if copay is coinsurance. |
| CAN_LET_C | NUMERIC (18,0) |  |
| REQ_CHRT_PULL_TM | DATETIME (Local) | This column contains the date and time when Chart Pull requested for this patient encounter. |
| SUP_PROV_ID | VARCHAR (18) | This column contains the provider ID of the supervising provider for this patient encounter. |
| SUP_PROV_C | VARCHAR (66) |  |
| SUP_PROV_REV_TM | DATETIME (Local) | This column contains the date and time when the supervising provider submitted his or her review |
| MEDS_REQUEST_PHR_ID | NUMERIC (18,0) | The pharmacy identifier from which the medications were requested. |
| MEDS_REQUEST_LWS_ID *(deprecated)* | VARCHAR (18) |  |
| MEDS_REQUEST_OP_C | INTEGER |  |
| PHYS_BP | VARCHAR (270) | This contains the patient's blood pressure that was entered during the patient encounter. |
| VITALS_TAKEN_TM | DATETIME (Local) | Holds the time the vitals were taken |
| PHYS_TEMP_SRC_C | VARCHAR (66) |  |
| PAT_PAIN_SCORE_C | VARCHAR (66) |  |
| PAT_PAIN_LOC_C | VARCHAR (66) |  |
| PAT_PAIN_EDU_YN | VARCHAR (1) |  |
| PAT_PAIN_CMT | VARCHAR (260) | This column contains comments that were entered pertaining to the patient's pain |
| PAT_PAIN_SCALE_CAT | VARCHAR (600) | This item stores the pain scale category under which the pain score is collected. |
| SMOKING_STATUS_C | INTEGER |  |
| PHYS_SPO2 | INTEGER | Contains the blood oxygen saturation value for this encounter. |
| SYS_GEN_LOS_ID | NUMERIC (18,0) | This column contains the system generated Level of Service information to link to the procedures tables. |
| REF_SRC_ADD_ID | VARCHAR (254) | This provides a link to the address of the referring provider. To obtain the address information, join to the table CLARITY_SER_ADDR on the ADDR_UNIQUE_ID column. If you use IntraConnect, you need to also join the REF_SRC_ADD_PROV_ID column to CLARITY_SER_ADDR.PROV_ID. |
| DOC_HX_SOURCE_C | INTEGER |  |
| APPT_LET_C | NUMERIC (18,0) |  |
| PARENT_ENC_CSN_ID | NUMERIC (18,0) | This item is a link to an encounter's parent encounter through the parent's contact serial number. The contact serial number is the unique identifier for the encounter. |
| SYNC_IP_DATA_C | INTEGER |  |
| APPTMT_LET_INST | DATETIME (Local) | If an appointment letter has been printed for this patient encounter, this column will list the date and time it was printed. If multiple letters were printed, we'll list the date and time of the most recent one. |
| RESULT_LET_INST | DATETIME (Local) | If a result letter has been printed for this patient encounter, this column will list the date and time it was printed. If multiple letters were printed, we'll list the date and time of the most recent one. |
| ENC_FORM_INST | DATETIME (Local) | If an encounter form has been printed for this patient encounter, this column will list the date and time it was printed. If multiple forms were printed, we'll list the date and time of the most recent one. |
| RESCHED_LET_INST | DATETIME (Local) | If a reschedule letter has been printed for this patient encounter, this column will list the date and time it was printed. If multiple letters were printed, we'll list the date and time of the most recent one. |
| FOLLOW_LET_INST | DATETIME (Local) | If a follow-up letter has been printed for this patient encounter, this column will list the date and time it was printed. If multiple letters were printed, we'll list the date and time of the most recent one. |
| PHYS_PEAK_FLOW | INTEGER | This column contains a measurement of the flow of air from the lungs: Peak Flow. If this column contains data, the measurement was taken during the associated encounter. |
| ENC_SPEC_C | VARCHAR (66) |  |
| INPATIENT_FLAG | VARCHAR (66) |  |
| SCHED_FROM_KIOSK_ID | VARCHAR (18) | This indicates the LWS ID of the kiosk that was used to schedule this appointment. |
| CHECK_OUT_KIOSK_ID | VARCHAR (18) | This indicates the LWS ID of the kiosk that was used to check out this appointment. |
| LD_STATUS_YN | VARCHAR (1) |  |
| ADT_PAT_CLASS_C | VARCHAR (66) |  |
| OTHER_BLOCK_ID | NUMERIC (18,0) | Stores "Other" Summary Blocks (non-IP, ED, OpTime) |
| OTHER_BLOCK_TYPE_C | INTEGER |  |
| FRST_CLIN_ACSS_DTTM | DATETIME (Local) | Item used to store the instant of first clinical access of the contact.  This is used to limit the documentation to 24 hours. |
| ORIG_ENC_TYPE_C *(deprecated)* | VARCHAR (66) |  |
| BILL_NUM | VARCHAR (50) | Billing number, often used as an identifier in downstream systems. |
| COMM_USER_CONTEXT_C | VARCHAR (66) |  |
| IP_DOC_CONTACT_CSN | NUMERIC (18,0) | For Hospital Outpatient Visit (HOV) encounters, this column stores the unique contact serial number for the patient contact which is used for clinical documentation.  This can be set for appointment contacts if they are not converted to HOVs. |
| TEMP_PT_HIS_C | INTEGER |  |
| REF_SRC_ADD_PROV_ID | VARCHAR (18) | The unique ID associated with the provider record selected as the referring provider. This column can be used in conjunction with the REF_SRC_ADD_ID column to join to the CLARITY_SER_ADDR table to report on the particular address a user chose when selecting a referring provider. |
| PRIMARY_PROCONT_ID | VARCHAR (18) | The unique ID of the provider that is the primary contact for this patient encounter. |
| PRIMARY_TEAM_ID | NUMERIC (18,0) | The unique ID of the primary Provider Care Team for this patient encounter. |
| RESEARCH_STUDY_ID | VARCHAR (18) | This column is not used by the Research Enrollment functionality introduced in Summer 2009. Patient encounters linked to Research Enrollments can be found in the ENROLL_LINKED_CSN table. With the old Research workflows, this column is the unique ID of the research study associated with this patient encounter.  This column will be populated for patient encounters marked as linked to a research study in older workflows or clients in new workflows. |
| MCIR_VACCINE_CODE_C | INTEGER |  |
| VISIT_POS_ID | NUMERIC (18,0) | The unique ID of the facility that was the place of service for this encounter. |
| NO_INTERP_RSN_C | INTEGER |  |
| CVG_ADD_DT | DATETIME | The add date returned in the response message by the payor for the encounter. The add date is defined as the date that the payor added the patient as being covered. |
| CHTS_TO_PULL_SEL_YN | VARCHAR (1) |  |
| FARM_WORKER_C | INTEGER |  |
| KIOSK_HH_QUEST_ID | VARCHAR (18) | The unique ID of the health history template that is assigned to the patient encounter. |
| KIOSK_ACCOMPANY_C | VARCHAR (66) |  |
| ENC_VERIFICATION_ID | NUMERIC (18,0) | Verification record for an encounter. |
| D_ENC_CHGS_DRPD_YN *(deprecated)* | VARCHAR (1) |  |
| HSP_ACCT_ADVISOR_YN | VARCHAR (1) |  |
| HSP_ACT_ADV_USER_ID | VARCHAR (18) | The unique ID of the user who used the Hospital Account Advisor to create or assign the encounter's initial hospital account. |
| HSP_ACCT_ADV_DTTM | DATETIME (Local) | If the Hospital Account Advisor is turned on, this item records the date and time that the advisor's recommendation was accepted or rejected. |
| VISIT_VERIFIED_YN | VARCHAR (1) |  |
| VERIF_VISIT_DT | DATETIME | The current date the visit contact was verified. |
| VERIF_DATE_INIT_DT | DATETIME | The initial date the visit contact was verified. |
| VERIF_USER_ID | VARCHAR (254) | This collects the user ID of the user who verified the visit. |
| ENC_LACT_STAT_C | INTEGER |  |
| PAT_LACT_CMNT | VARCHAR (254) | The comments entered when the patient's lactation status has been edited. |
| COSIGNER_USER_ID | VARCHAR (18) | The unique ID of the user who cosigned the patient's chart. |
| COSIGN_MSG_ID | VARCHAR (18) | The unique ID associated with the In Basket chart cosign message. |
| COSIGN_REV_INS_DTTM | DATETIME (Local) | The date and time the chart was cosigned. |
| CHART_FORMS_SET_ID | NUMERIC (18,0) | The unique ID of the charting form sets that were used in the encounter. |
| SCAN_CONTACT_INFO *(deprecated)* | VARCHAR (508) | *** Deprecated ***  In table PAT_ENC_2, the column SCAN_CONTACT_INFO (EPT/18178) has been deprecated.  The deprecated column's content/data is no longer available since it is no longer populated in Chronicles.   . |
| PAR_DICT_COUNTER | INTEGER | The counter for partial dictation. |
| IS_LOS_UPDATE_C | INTEGER |  |
| PRIMARY_DX_NAME *(deprecated)* | VARCHAR (254) | *** Deprecated *** In table PAT_ENC_2, the column PRIMARY_DX_NAME (EPT 18419) has been deprecated. The deprecated column's content/data is no longer available since it is no longer populated in Chronicles. |
| FORM_ID_COUNTER | INTEGER | Stores the counter of form IDs. |
| CONSNT_REV_USER_ID | VARCHAR (18) | The unique ID of the user who reviewed patient consent. |
| VISIT_PAYOR_ID | NUMERIC (18,0) | The unique ID of the payor that is associated with this encounter. |
| VISIT_PLAN_ID | NUMERIC (18,0) | The unique ID of the plan that is associated with this encounter. |
| SOCIO_SRC_C | INTEGER |  |
| TEL_ENC_MSG_RGRDING | VARCHAR (254) | Free-text field containing user entered information regarding a telephone encounter message. |
| ENC_AR_INT_STAT_C | INTEGER |  |
| MSG_PRIORITY_C | INTEGER |  |
| RESEARCH_ENC_FLG_C | INTEGER |  |
| FAM_SPOUSE_NAME | VARCHAR (254) | The name of the patient's spouse |
| MSG_CALLER_NAME | VARCHAR (254) | The name of the caller who left this message |
| CONSENT_EXP_DATE | DATETIME | This is the expiration date of any consent forms that are attached to the patient. |
| CV_ACC4_PAT_RESP_YN | VARCHAR (1) |  |
| FAMILY_MEM_PREFIX_C | INTEGER |  |
| AVS_REFUSED_DTTM | DATETIME (UTC) | The date and time when an end user documented that the patient declined the After Visit Summary. |
| AVS_LAST_PRINT_DTTM | DATETIME (UTC) | Records the instant the After Visit Summary was last printed |
| MED_LIST_UPDATE_DTTM | DATETIME (UTC) | If a patient's prescriptions or Facility-Administered Medications (FAMs) are updated (signed, modified, or discontinued; or other med reconciliation actions are changed) after the After Visit Summary (AVS) has been printed, this item is updated to hold a timestamp indicating the last time that such updates were made. It is left blank if no AVS has been printed yet. |
| AVS_REFUSED_DT_DTTM *(deprecated)* | DATETIME (UTC) |  |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| B-TREE INDEX | EIX_OTHER_BLOCK_ID | OTHER_BLOCK_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_PAT_ENC_2_CODA | CONTACT_DATE | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_PAT_ENC_2_COSIGNER | COSIGNER_USER_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_PAT_ENC_RELATED_CONTACT | PAT_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_PAT_ENC_RELATED_CONTACT | PAT_ENC_DATE_REAL | 2 | Yes | Yes |  |
| BITMAP INDEX | EIX_PAT_ENC_RELATED_OWNER1 | CM_CT_OWNER_ID | 1 | No | Yes |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | PAT_ENC_CSN_ID | ALT_ORD_PROV_SINGL | PAT_ENC_CSN_ID | Unknown | No | No |  |
| 1 | PAT_ENC_CSN_ID | AN_RELINK_INFO | PAT_ENC_CSN_ID | No | No | No |  |
| 1 | PAT_ENC_CSN_ID | DENT_ORTH_EXAM_NOTES | PAT_ENC_CSN_ID | No | No | No |  |
| 1 | PAT_ENC_CSN_ID | FAC_CHG_OVERRIDE | PAT_ENC_CSN_ID | No | No | No |  |
| 1 | PAT_ENC_CSN_ID | FAM_HX_PAT_ONLY | PAT_ENC_CSN_ID | No | No | No |  |
| 1 | PAT_ENC_CSN_ID | F_ED_ENCOUNTERS | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 1 | PAT_ENC_CSN_ID | F_HH_CERT_ATTRIBUTES | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 1 | PAT_ENC_CSN_ID | F_HH_OASIS_SINGLE | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 1 | PAT_ENC_CSN_ID | F_HH_OASIS_SINGLE_2 | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 1 | PAT_ENC_CSN_ID | F_HH_OASIS_SINGLE_3 | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 1 | PAT_ENC_CSN_ID | F_HH_OASIS_SINGLE_4 | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 1 | PAT_ENC_CSN_ID | F_HH_OASIS_SINGLE_5 | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 1 | PAT_ENC_CSN_ID | F_IBD_ADULT_FORM_ENC | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 1 | PAT_ENC_CSN_ID | F_IBD_FORM_RESP | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 1 | PAT_ENC_CSN_ID | F_IP_HSP_ADMISSION | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 1 | PAT_ENC_CSN_ID | F_IP_HSP_SEPSIS3 | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 1 | PAT_ENC_CSN_ID | F_IRIS_ENC | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 1 | PAT_ENC_CSN_ID | F_MU_OBJ_EH_ADMISSION | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 1 | PAT_ENC_CSN_ID | F_MU_QM_EH_2014_ED_VISIT | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 1 | PAT_ENC_CSN_ID | F_MU_QM_EH_2014_IP_ADMSN | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 1 | PAT_ENC_CSN_ID | F_QM_AMI | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 1 | PAT_ENC_CSN_ID | F_QM_CAC | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 1 | PAT_ENC_CSN_ID | F_QM_HBIPS | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 1 | PAT_ENC_CSN_ID | F_QM_HEART_FAILURE | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 1 | PAT_ENC_CSN_ID | F_QM_IMMUNIZATION | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 1 | PAT_ENC_CSN_ID | F_QM_PC_BABY | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 1 | PAT_ENC_CSN_ID | F_QM_PC_MOM | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 1 | PAT_ENC_CSN_ID | F_QM_PNEUMONIA | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 1 | PAT_ENC_CSN_ID | F_SCHED_APPT | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 1 | PAT_ENC_CSN_ID | HAUD_ENC | ENC_CSN | Unknown | Unknown | No |  |

_(666 total; showing first 30)_
