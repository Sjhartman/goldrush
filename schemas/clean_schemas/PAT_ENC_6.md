# PAT_ENC_6

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=PAT_ENC_6

## Description

This table supplements the PAT_ENC, PAT_ENC_2, PAT_ENC_3, PAT_ENC_4, and PAT_ENC_5  tables. It contains additional information related to patient encounters or appointments.

**Overflow table** for PAT_ENC (143 cols). Contains additional columns for the same records — join on the shared primary key column.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | EPT |
| Release Version | Rel 2018 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| PAT_ENC_CSN_ID | NUMERIC (18,0) | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| PAT_ID | VARCHAR (18) | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| PAT_ENC_DATE_REAL | FLOAT | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| CONTACT_DATE | DATETIME | The date of this contact in calendar format. |
| CM_CT_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this contact. This is only populated if you use IntraConnect. |
| LINKED_ENC_CSN | NUMERIC (18,0) | The unique contact serial number of the visit that represents the official visit. Intended for (FINLAND) ad hoc encounters that need to be associated with an official visit. |
| PATIENT_ID_METHOD_C | INTEGER |  |
| PATIENT_ID_METHOD_TEXT | VARCHAR (100) | Free text version of, or in addition to, the discrete patient identification method (EPT-1160). |
| LMP_PRECISION_C | INTEGER |  |
| PLANNED_BILL_AREA_ID | NUMERIC (18,0) | Used to track what the bill area was for an appointment at the time of check in. |
| AVS_PRINT_INSULIN_YN | VARCHAR (1) |  |
| BCRA_BRCA_GENE_MUT_C | INTEGER |  |
| SVC_TARGET_EFFORT_YN | VARCHAR (1) |  |
| OUTPAT_VISIT_GRP_C | INTEGER |  |
| PSYCH_ARRIVAL_C | INTEGER |  |
| PLAN_RECUR_TREAT_YN | VARCHAR (1) |  |
| HUS_VISIT_TYPE_C | INTEGER |  |
| SOCIAL_SRVC_AREA_C | INTEGER |  |
| EXT_LTC_PAT_YN | VARCHAR (1) |  |
| VETERAN_ENC_MED_CVG_C | INTEGER |  |
| VETERAN_BILLING_CODE_C | INTEGER |  |
| APPT_EXPECTED_DATE *(deprecated)* | DATETIME | *** Deprecated *** In table PAT_ENC_6, the column APPT_EXPECTED_DATE has been deprecated.   This column has data that is not properly extracted to Clarity. Additionally, it is deprecated due to its lack of use and meaningfulness. |
| ED_REF_CALLBAK_D_ID | NUMERIC (18,0) | The ID number of the department from which the patient is being referred to the ED. |
| EXTMED_REC_YR_YN | VARCHAR (1) |  |
| EXTPROB_REC_YR_YN | VARCHAR (1) |  |
| EXTALGY_REC_YR_YN | VARCHAR (1) |  |
| APPT_LETTER_MSG_PRIORITY_C | VARCHAR (66) |  |
| RFV_USED_TO_SCHED_C | VARCHAR (66) |  |
| BMI_PERCENTILE | NUMERIC (18,2) | This item stores the patient's BMI percentile. This item will be null for ages greater than 20, and is calculated based on the patient's height, weight, and sex. |
| BMI_PERCENTILE_HGC_ID | NUMERIC (18,0) | This item stores the ID of the HGC record used for calculation of EPT 87002 - BMI Percentile. |
| SPEC_BILL_SVC_ID *(deprecated)* | NUMERIC (18,0) |  |
| KANTA_PLD_STTNG_YN | VARCHAR (1) |  |
| KANTA_PLD_USER_ID | VARCHAR (18) | The last user to set the "Send data from other encounters" item |
| KANTA_PLD_DTTM | DATETIME (UTC) | The last instant that "Send data from other encounters" was set |
| CREATION_ORD_ID | NUMERIC (18,0) | The ID number of the order which created the patient contact. |
| EXT_TX_STATUS_C | INTEGER |  |
| EXT_TX_STATUS_CMT | VARCHAR (254) | An optional item used to document the encounter's External Transportation Comments. There is no standard functionality that is driven by this item. This item can be used to driver reporting, confirmation errors, or WQ activities. |
| EXT_ACCM_STATUS_C | INTEGER |  |
| EXT_ACCM_STATUS_CMT | VARCHAR (254) | An optional item used to document the encounter's External Accommodation Comments. There is no standard functionality that is driven by this item. This item can be used to driver reporting, confirmation errors, or workqueue activities. |
| VISIT_TYPE_ADDED_BY_FORM_YN | VARCHAR (1) |  |
| FIN_OUT_MTCH_ORG_ID | NUMERIC (18,0) | Identifies the organizer for an incoming outsourced service event corresponding to the matching query response. |
| FIN_OUT_ORG_LOC_ID | NUMERIC (18,0) | Identifies the organizer location for an incoming outsourced service event corresponding to the matching query response. |
| FIN_OUT_ORG_DEP_ID | NUMERIC (18,0) | Identifies the organizer department for an incoming outsourced service event corresponding to the matching query response. |
| LATE_CANCEL_YN | VARCHAR (1) |  |
| GAIL_LIFETIME_RISK *(deprecated)* | NUMERIC (18,3) |  |
| GAIL_5_YR_RISK *(deprecated)* | NUMERIC (18,3) |  |
| SG_AT_RISK_IND_C | INTEGER |  |
| SG_FC_STATUS_C | INTEGER |  |
| MYC_SCHED_HM_TOPIC_ID | NUMERIC (18,0) | This item contains the Health Maintenance Topic ID associated with the Reason for Visit that is used to schedule an appointment through MyChart. This means it may be the subtopic if the scheduled topic was a combo topic. |
| ELIG_QUERIED_YN | VARCHAR (1) |  |
| ELIG_NUM_PLANS | INTEGER | This item indicates the number of eligibility plans that were available for selection in this encounter. Plans that were manually removed are not counted. |
| ELIG_PLAN_REMOVED_YN | VARCHAR (1) |  |
| ELIG_AUTO_VERIFY_YN | VARCHAR (1) |  |
| ELIG_PLAN_SELECT_YN | VARCHAR (1) |  |
| SELF_ARR_ATTEMPT_C | INTEGER |  |
| SG_MOH_URGENCY_C | INTEGER |  |
| SG_NAMED_REFERRAL_YN | VARCHAR (1) |  |
| SG_PAT_REQUEST_YN | VARCHAR (1) |  |
| SG_TREATMENT_PROG_C | INTEGER |  |
| SG_APPT_RATIONALE_C | INTEGER |  |
| EVISIT_RFV_C | INTEGER |  |
| EVISIT_YN | VARCHAR (1) |  |
| EVISIT_TLH_ALLOWED_SUBLOC_C | INTEGER |  |
| EVISIT_TLH_ALLOWED_LOC_C | INTEGER |  |
| APPT_LETTER_BAT_PRINT_UTC_DTTM | DATETIME (UTC) | Tracks the last instant this appointment had a batch letter printed via a batch job based on batch template 16 since the appointment was created or updated. |
| RIDE_TO_STATUS_C | INTEGER |  |
| RIDE_FROM_STATUS_C | INTEGER |  |
| RIDE_TO_COMMENT | VARCHAR (200) | Holds a free-text comment relating to the Status of a Ride To an appointment, which is held in column RIDE_TO_STATUS_C. |
| RIDE_FROM_COMMENT | VARCHAR (200) | Holds a free-text comment relating to the Status of a Ride From an appointment, which is held in column RIDE_FROM_STATUS_C. |
| APPT_AUTH_STATUS_C | INTEGER |  |
| FI_THL_ENC_FOLLOW_UP_IDENT | VARCHAR (500) | This item stores the value of the Finland THL Hilmo data element "Seurantatietueen tunnus" for an encounter without a hospital account. |
| APPT_PAGED_DTTM | DATETIME (Attached) | The date and time that the patient was paged after checking in for their appointment. |
| EVISIT_NEW_STATUS_C | INTEGER |  |
| TO_VISIT_RIDE_SOURCE_C | INTEGER |  |
| FROM_VISIT_RIDE_SOURCE_C | INTEGER |  |
| TELEHEALTH_MODE_C | INTEGER |  |
| LAST_CHKIN_USER_ID | VARCHAR (18) | The last person to check-in an appointment. |
| LAST_SIGNIN_USER_ID | VARCHAR (18) | The last person to sign-in an appointment. |
| LAST_CHKOUT_USER_ID | VARCHAR (18) | The last person to check-out an appointment. |
| APPT_SCHEDULING_MODE_C | INTEGER |  |
| LAB_RESP_USER_ID | VARCHAR (18) | The unique ID of the phlebotomist (EMP) currently responsible for the patient's lab draws for this encounter. |
| EXT_MEDS_UPD_INST_UTC_DTTM | DATETIME (UTC) | Contains the most recent instant of update for external medications in external orders encounters. |
| INTF_PRIMARY_PAT_ENC_CSN_ID | NUMERIC (18,0) | Contains the CSN of the primary interface contact for this encounter. |
| OVERRIDE_BCRA_NUM_BIOPSY_C | INTEGER |  |
| OVERRIDE_BCRA_RACE_C | INTEGER |  |
| OVERRIDE_GAIL_FACTOR_USER_ID | VARCHAR (18) | The user who overrode the factors for the Gail model. |
| OVERRIDE_GAIL_FACTOR_DTTM | DATETIME (Local) | The instant when the Gail factors were overridden. |
| VETERAN_COVERAGE_ENC_YN | VARCHAR (1) |  |
| VISIT_DUE_DATE | DATETIME | The date the visit must take place by. |
| ADJUD_TO_PHARMACY_COVERAGE_YN | VARCHAR (1) |  |
| TLH_APRV_SUBLOC_C | INTEGER |  |
| TLH_APRV_LOC_C | INTEGER |  |
| ENC_CLOSE_UTC_DTTM | DATETIME (UTC) | The instant the visit was closed |
| SPLIT_FILING_ORDER_YN | VARCHAR (1) |  |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| B-TREE INDEX | EIX_PAT_ENC_6_CONTACT | PAT_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_PAT_ENC_6_CONTACT | PAT_ENC_DATE_REAL | 2 | Yes | Yes |  |

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

_(687 total; showing first 30)_
