# PAT_ENC_HSP

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=PAT_ENC_HSP

## Description

This table is the primary table for hospital encounter information. A hospital encounter is a contact in the patient record created through an ADT workflow such as preadmission, admission, ED Arrival, discharge, and hospital outpatient visit (HOV) contacts. These contact types have the ADT flag (I EPT 10101) set to 1. This table excludes all other contacts.

**Primary table** in this group (133 cols). Overflow siblings joined on shared key: PAT_ENC_HSP_2 (78 cols). Prefer this table for most queries.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | EPT |
| Release Version | EPIC 2000 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| PAT_ID | VARCHAR (18) | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| PAT_ENC_DATE_REAL | FLOAT | This is a numeric representation of the date of this contact in your system. The integer portion of the number specifies the date of the contact. The digits after the decimal point indicate multiple contacts on one day. |
| PAT_ENC_CSN_ID | NUMERIC (18,0) | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| ADT_CONTACT | INTEGER | Index used to look at patient contacts of type ADT. |
| ADT_INITIAL | VARCHAR (12) | Index used to look at patient contacts where the patient is currently admitted. |
| ADT_PAT_CLASS_C | VARCHAR (66) |  |
| ADT_BILLING_TYPE_C | INTEGER |  |
| ADT_PATIENT_STAT_C | INTEGER |  |
| LEVEL_OF_CARE_C | VARCHAR (66) |  |
| PENDING_DISCH_TIME | 10200 | The date and time of the pending discharge for this patient contact. |
| DISCH_CODE_C | VARCHAR (66) |  |
| ADT_ATHCRT_STAT_C | INTEGER |  |
| ADT_LAST_RVW_DT | DATETIME | The date of last review of the ADT authorization/certification status for this patient contact. |
| ADT_NEXT_RVW_DT | DATETIME | The date of next review of the ADT authorization/certification status for this patient contact. |
| PREADM_UNDO_RSN_C | INTEGER |  |
| EXP_ADMISSION_TIME | 10301 | The date and time of the expected admission for this patient contact. |
| EXP_LEN_OF_STAY | INTEGER | The expected length of stay in days of the admission for this patient contact. |
| EXP_DISCHARGE_DATE | DATETIME | The date of expected discharge of the admission for this patient contact. |
| ADMIT_CATEGORY_C | INTEGER |  |
| ADMIT_SOURCE_C | VARCHAR (66) |  |
| TYPE_OF_ROOM_C | VARCHAR (66) |  |
| RSN_FOR_ROOM_C | INTEGER |  |
| TYPE_OF_BED_C | VARCHAR (66) |  |
| RSN_FOR_BED_C | VARCHAR (66) |  |
| BELONG_CLAIM_NO | VARCHAR (80) | The external ID for claiming the belongings for this patient contact. |
| BELONG_RECV_TIME | 10401 | The instant that the belongings were received for this patient contact. |
| BELONG_RECV_PERS | VARCHAR (80) | The name of the person who received the belongings for this patient contact. |
| BELONG_LOCATION | VARCHAR (255) | Free text description where the belongings received are stored for this patient contact. |
| DELIVERY_TYPE_C | VARCHAR (66) |  |
| LABOR_STATUS_C | INTEGER |  |
| ER_INJURY | VARCHAR (255) | Free text description of injury for this patient contact. |
| ADT_ARRIVAL_TIME | 10820 | The date and time of arrival for this patient contact. |
| ADT_ARRIVAL_STS_C | INTEGER |  |
| HOSP_ADMSN_TIME | 18850 | The date and time that the patient was first admitted to the facility, bedded in the ED, or confirmed for an HOV for this contact, regardless of patient's base patient class. |
| ADMIT_CONF_STAT_C | INTEGER |  |
| HOSP_DISCH_TIME | 18855 | The hospital discharge date and time for this patient contact. |
| DISCH_CONF_STAT_C | INTEGER |  |
| DISCHARGE_PROV_ID | VARCHAR (18) | The unique ID of the provider who discharged the patient from this patient contact. |
| ADMISSION_PROV_ID | VARCHAR (18) | The unique ID of the provider who admitted the patient for this patient contact. |
| HOSP_ADMSN_TYPE_C | VARCHAR (66) |  |
| DEPARTMENT_ID | NUMERIC (18,0) | The ID number of the unit for the most recent location of the patient for this patient contact. |
| ADT_SERV_AREA_ID | NUMERIC (18,0) | The ID number of the service area for the most recent location of the patient for this patient contact. |
| ROOM_ID | VARCHAR (18) | The ID number of the room for the most recent location of the patient for this patient contact. |
| BED_ID | VARCHAR (18) | The ID number of the bed for the most recent location of the patient for this patient contact. |
| HOSP_SERV_C | VARCHAR (66) |  |
| MEANS_OF_DEPART_C | INTEGER |  |
| DISCH_DISP_C | VARCHAR (66) |  |
| DISCH_DEST_C | VARCHAR (66) |  |
| TRANSFER_FROM_C | INTEGER |  |
| PAT_CONTACT_MPI_NO | No |  |
| HSP_ACCOUNT_ID | NUMERIC (18,0) | The unique ID number of the hospital account for this patient contact. |
| MEANS_OF_ARRV_C | VARCHAR (66) |  |
| BILL_NUM_TYPE_C | INTEGER |  |
| BILL_NUM | VARCHAR (50) | An account number (or billing number) for this patient contact. This may be an external ID. |
| RELIG_AFFIL_YN | VARCHAR (1) |  |
| ACUITY_LEVEL_C | VARCHAR (66) |  |
| PAT_ESCORTED_BY_C | INTEGER |  |
| HOSPIST_NEEDED_YN | VARCHAR (1) |  |
| ACCOMMODATION_C | VARCHAR (66) |  |
| ACCOM_REASON_C | INTEGER |  |
| ADM_EVENT_ID | No | The ID number of the admission event record from the ADT master file for this patient stay. |
| DIS_EVENT_ID | No | The ID number of the discharge event record from the ADT master file for this patient stay. |
| INPATIENT_DATA_ID | VARCHAR (18) | The unique ID of the Inpatient Data Store record. |
| IP_EPISODE_ID | NUMERIC (18,0) | The unique ID of the Inpatient episode record. This includes discharges from the ED. |
| PVT_HSP_ENC_C | INTEGER |  |
| CONTACT_DATE | DATETIME | This column refers to the date an admission was created, not necessarily the date of admission.  This column is not overly useful for reporting purposes and generally should not be used. |
| ED_EPISODE_ID | NUMERIC (18,0) | The unique ID of the Inpatient episode record for the ED visit. |
| ED_DISPOSITION_C | VARCHAR (66) |  |
| ED_DISP_TIME | DATETIME (Local) | The date and time that the disposition was entered. |
| FOLLOWUP_PROV_ID | VARCHAR (18) | The follow-up provider for the patient. |
| PROV_CONT_INFO | VARCHAR (254) | The contact information for the patient's follow-up provider. |
| ED_AREA_OF_CARE_ID | NUMERIC (18,0) | The unique ID for the primary area of care for the patient during their stay in the ED. |
| CM_CT_OWNER_ID | VARCHAR (25) | ID of the deployment owner for this contact. |
| OSHPD_ADMSN_SRC_C | INTEGER |  |
| OSHPD_LICENSURE_C | INTEGER |  |
| OSHPD_ROUTE_C | INTEGER |  |
| INP_ADM_DATE | 10290 | Date-time of the inpatient admission. This is the date/time during the hospital encounter when the patient first received a base patient class of inpatient. This can be different than the value for the admission date if the patient was assigned an emergency or outpatient base patient class. |
| COPY_TO_PCP_YN | VARCHAR (1) |  |
| ADOPTION_CASE_YN | VARCHAR (1) |  |
| PREOP_TEACHING_C | INTEGER |  |
| PREOP_PRN_EVAL_C | INTEGER |  |
| PREOP_PH_SCREEN_C | INTEGER |  |
| LABOR_ACT_BIRTH_C | INTEGER |  |
| LABOR_FEED_TYPE_C | INTEGER |  |
| ER_BADGE_NUMBER | VARCHAR (254) | Free text entry of Patient badge number in Emergency Department - that can be interfaced to a third party system for patient tracking. |
| PROC_SERV_C | INTEGER |  |
| CANCEL_USER_ID | VARCHAR (18) | The user who canceled the newly created contact. |
| ED_DEPARTURE_TIME | 49020 | Date and time the patient left the ED. |
| TRIAGE_DATETIME | 10831 | The date and the time the patient was triaged. |
| TRIAGE_STATUS_C | INTEGER |  |
| BELONG_REL_PERS | VARCHAR (80) | The person who released the patient's personal belongings. |
| BELONG_REL_DATE | 10408 | The date and time the patient's belongings were released. |
| BELONG_STORE_LOC_C | INTEGER |  |
| EDDISP_EDIT_USER_ID | VARCHAR (18) | ED DISPOSITION EDIT USER |
| EDDISP_EDIT_INST | DATETIME (Local) | ED DISPOSITION EDIT INSTANT |
| INP_ADM_EVENT_ID | NUMERIC (18,0) | The event record for the hospital encounter where the patient first received a base patient class of inpatient, making them an inpatient. |
| INP_ADM_EVENT_DATE | No | Instant of the event creation of the event which caused a patient to become an inpatient patient class. |
| INP_DWNGRD_EVNT_ID | No | Column to return the event ID of the event that last downgrades the patient from an inpatient patient class to a non-inpatient patient class. |
| INP_DWNGRD_DATE | No | Column that returns the effective date and time of a patients latest downgrade from an inpatient patient class. |
| INP_DWNGRD_EVNT_DT | No | Column to return the event date and time of the last event that downgrades a patient from an inpatient patient class to a non-inpatient patient class. |
| OP_ADM_DATE | 10293 | The date and time during the hospital encounter when the patient first received a base patient class of outpatient. |
| EMER_ADM_DATE | 10296 | The date and time during the hospital encounter when the patient first received a base patient class of emergency. |
| OP_ADM_EVENT_ID | NUMERIC (18,0) | The event record for the hospital encounter where the patient first received a base patient class of outpatient. |
| EMER_ADM_EVENT_ID | NUMERIC (18,0) | The event record for the hospital encounter where the patient first received a base patient class of emergency. |
| PREREG_SOURCE_C | INTEGER |  |
| HOV_CONF_STATUS_C | INTEGER |  |
| RELIG_NEEDS_VISIT_C | INTEGER |  |
| INSTANT_OF_ENTRY_TM | DATETIME (Local) | The instant this contact was created in the system. |
| DISCHARGE_CAT_C | INTEGER |  |
| EXP_DISCHARGE_TIME | DATETIME (Local) | The time of expected discharge of the admission for this patient contact. |
| BILL_ATTEND_PROV_ID | VARCHAR (18) | Billing Attending Provider - The attending provider that is or will be specified on the hospital account and claim when billed. |
| OB_LD_LABORING_YN | VARCHAR (1) |  |
| OB_LD_LABOR_TM | DATETIME (Local) | The date and time at which labor began. |
| TRIAGE_ID_TAG | VARCHAR (184) | The trauma identifier assigned to patient. This number is frequently associated with a pre-printed trauma packet that is used when an accident or other incident results in many patients arriving at the hospital in a short time period. |
| ED_FU_EDIT_USER_ID | VARCHAR (18) | The unique ID of the user who last edited ED follow-up info for this encounter. This column is frequently used to link to CLARITY_EMP. |
| ED_FU_EDIT_INST | DATETIME (Local) | The last instant when ED follow-up info was edited for this encounter. |
| TRIAGE_ID_TAG_CMT | VARCHAR (184) | A free-text comment that can be entered along with the trauma identifier or triage ID assigned to the patient. |
| REFERRING_DEPT_ID | NUMERIC (18,0) | The department that referred the patient for surgery |
| TPLNT_BILL_STAT_C | INTEGER |  |
| ACTL_DELIVRY_METH_C | VARCHAR (66) |  |
| PRENATAL_CARE_C | INTEGER |  |
| AMBULANCE_CODE_C | INTEGER |  |
| MSE_DATE | 10833 | Indicates the date and time of the patient's medical screening exam (MSE). |
| ADMIT_PROV_TEXT | VARCHAR (254) | The free text admitting provider for the encounter. |
| ATTEND_PROV_TEXT | VARCHAR (254) | The free text attending provider for the encounter. |
| PROV_PRIM_TEXT | VARCHAR (254) | The free text primary care provider for the encounter |
| PROV_PRIM_TEXT_PHON | VARCHAR (254) | The free text phone number for the primary care provider. |
| HOSPITAL_AREA_ID | NUMERIC (18,0) | This field identifies the hospital area associated with the hospital unit in this patient contact. |
| ADMIT_ADDR_ID | VARCHAR (100) | Address ID for attending provider (EPT 18867) |
| CHIEF_COMPLAINT_C | VARCHAR (66) |  |
| NEED_FIN_CLR_YN | VARCHAR (1) |  |
| MU_HOSP_ADMSN_TIME | DATETIME (Local) | The date and time the patient was admitted to inpatient or roomed in ED. It will look at item EPT 10290 to see if it is populated. If yes, it will be populated with the instant the patient was first inpatient (EPT 10290 and 10291). Otherwise, it will look at which version of the standard unique patient denominator is being used (LSD 34062) and whether the patient was an ED patient (EPT 10296 and 10297). If the standard unique patient denominator being used in LSD 34062 is the all ED patients denominator, this item will be populated with the hospital admission date and time (EPT 18850 and 18851). If the patient was not inpatient and not seen in the ED, this item will be null. If the standard unique patient denominator being using in LSD 34062 is the ED to Observation patients only denominator, if the patient was seen in the ED and was an observation patient, this item will be populated with the hospital admission date and time (EPT 18850 and 18851).      If the settings for excluding newborns are present and the encounter is for a newborn, this item will be null. |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| B-TREE INDEX | EIX_PAT_ENC_HSPENC | PAT_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_PAT_ENC_HSPENC | PAT_ENC_DATE_REAL | 2 | Yes | Yes |  |
| B-TREE INDEX | EIX_PAT_ENC_HSP_ACCT_CSN | HSP_ACCOUNT_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_PAT_ENC_HSP_ACCT_CSN | PAT_ENC_CSN_ID | 2 | Yes | Yes |  |
| B-TREE INDEX | EIX_PAT_ENC_HSP_ADATSTC | ADT_ATHCRT_STAT_C | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_PAT_ENC_HSP_ADPRID | ADMISSION_PROV_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_PAT_ENC_HSP_ADTINIT | ADT_INITIAL | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_PAT_ENC_HSP_EXADTI | EXP_ADMISSION_TIME | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_PAT_ENC_HSP_EXDIDA | EXP_DISCHARGE_DATE | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_PAT_ENC_HSP_HOADTI | HOSP_ADMSN_TIME | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_PAT_ENC_HSP_HODITI | HOSP_DISCH_TIME | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_PAT_ENC_HSP_ID_ADM_DISCH | PAT_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_PAT_ENC_HSP_ID_ADM_DISCH | INP_ADM_DATE | 2 | Yes | Yes |  |
| B-TREE INDEX | EIX_PAT_ENC_HSP_ID_ADM_DISCH | HOSP_DISCH_TIME | 3 | Yes | Yes |  |
| B-TREE INDEX | EIX_PAT_ENC_HSP_INPADMDT | INP_ADM_DATE | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_PAT_ENC_HSP_INP_DATA_ID | INPATIENT_DATA_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_PAT_ENC_HSP_MU_HOADTI | MU_HOSP_ADMSN_TIME | 1 | No | Yes |  |
| B-TREE INDEX | EIX_PAT_ENC_HSP_PEDITI | PENDING_DISCH_TIME | 1 | Yes | Yes |  |

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
| 1 | PAT_ID | PATIENT_3 | PAT_ID | No | No | No |  |
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

_(565 total; showing first 30)_
