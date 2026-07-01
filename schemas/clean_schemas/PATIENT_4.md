# PATIENT_4

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=PATIENT_4

## Description

This table supplements the PATIENT table. It contains basic information about patients.

**Overflow table** for PATIENT (137 cols). Contains additional columns for the same records — join on the shared primary key column.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | EPT |
| Release Version | Rel 2012 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| PAT_ID | VARCHAR (18) | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| INTERPRT_NEEDED_CMT | VARCHAR (254) | Comments regarding the patient's interpreter needs |
| DENT_COMMENT | VARCHAR (254) | This item stores the comment of the current dental classification |
| EPT_LOG_DATE | DATETIME | The date for which a patient level event was last logged. |
| ESRD_G_START_DT | DATETIME | The first date that the acute comorbidity of gastrointestinal bleeding was present during maintenance dialysis treatments for End Stage Renal Disease (ESRD). |
| ESRD_B_START_DT | DATETIME | The first date that the acute comorbidity of bacterial pneumonia was present during maintenance dialysis treatments for End Stage Renal Disease (ESRD). |
| ESRD_P_START_DT | DATETIME | The first date that the acute comorbidity of pericarditis was present during maintenance dialysis treatments for End Stage Renal Disease (ESRD). |
| CMS_OP_ESRD_TRAIN_H | INTEGER | The number of training session that have been performed for a patient's hemodialysis treatment through his/her life time. |
| CMS_OP_ESRD_TRAIN_P | INTEGER | The number of training session that have been performed for a patient's peritoneal dialysis treatment through his/her life time. |
| LANGUAGE_C_CMT | VARCHAR (254) |  |
| FOH_ID | NUMERIC (18,0) | This item stores the filing order history ID for the member. |
| TXP_PAT_YN | VARCHAR (1) |  |
| BLIND_YN | VARCHAR (1) |  |
| DEAF_YN | VARCHAR (1) |  |
| EMPR_COUNTY_C | VARCHAR (66) |  |
| RESEARCH_ID | VARCHAR (18) | Research study and client billing workflows require that an administrative patient record be created for administrative purposes. This item links the administrative patient record to the research study or client (for example, links to RSH_RESEARCH_INFO.RESEARCH_ID). It will not be populated for actual patient records.  This column replaces the column PAT_ENC_4.RESEARCH_ID. Reports must be updated to use the new column PATIENT_4.RESEARCH_ID. |
| DOB_FMT_C | INTEGER |  |
| ALRGY_REV_EPT_CSN | NUMERIC (18,0) | This column contains the source encounter where allergies were most recently reviewed. If allergies were most recently reviewed outside the context of an encounter, the value is blank. |
| OCCUPATION_C | INTEGER |  |
| INDUSTRY_C | INTEGER |  |
| EDUCATION_LEVEL_C | INTEGER |  |
| LOC_EDUCATION_C | INTEGER |  |
| PARENT_EDU_LEVEL_C | INTEGER |  |
| PARENT_LOC_EDU_C | INTEGER |  |
| RES_OF_STATE_C | VARCHAR (66) |  |
| US_CITIZEN_YN | VARCHAR (1) |  |
| PERMANENT_RESIDENT_YN | VARCHAR (1) |  |
| NO_EMAIL_REASON_C | INTEGER |  |
| CNTRY_SUBDIV_CODE_C | INTEGER |  |
| PDS_NHS_NUM_ERR | VARCHAR (254) | This item contains the error message returned by the PDS when an attempt to allocate an NHS number fails. This error should be specific to UK customers. |
| BSN_DOB_FMT_C | INTEGER |  |
| RACE_COLL_MTHD_C | INTEGER |  |
| PDS_NHS_STAT_IND_C | VARCHAR (66) |  |
| SEND_SMS_YN | VARCHAR (1) |  |
| PAT_NO_COMM_PREF_C | INTEGER |  |
| FST_LIVE_BIRTH_AGE | INTEGER | The patient's age at first live birth. |
| RSH_PREF_C | INTEGER |  |
| RSH_PREF_UTC_DTTM | DATETIME (UTC) | Indicates the instant that the patient last indicated an explicit research recruitment preference. |
| RSH_PREF_USER_ID | VARCHAR (18) | Indicates the user who last recorded the patient's explicit research recruitment preference. |
| KIOSK_WORKSTATION_LAST_USED_ID | VARCHAR (18) | Contains the workstation id of the last Welcome instance used by the patient |
| EXTERNAL_DEATH_DATE | DATETIME | The patient's date of death as reported by an external organization. This column is typically populated by importing data through the Patient Load utility. |
| DEATH_DATA_IMPORT_DATE | DATETIME | The date the Patient Load utility populated EXTERNAL_DEATH_DATE for this patient. |
| DEATH_LOC_C | INTEGER |  |
| BIRTH_DT_INACC_YN | VARCHAR (1) |  |
| DEATH_DT_INACC_YN | VARCHAR (1) |  |
| INDIGENOUS_STAT_C | INTEGER |  |
| LOCALITY *(deprecated)* | VARCHAR (50) | *** Deprecated *** In table PATIENT_4, the column LOCALITY (EPT 87124) has been deprecated.   The deprecated column's content/data is no longer available since the locality concept has been merged into the address item storage for international customers.  Name of the locality/neighborhood/suburb in which the patient is usually located. |
| CARER_AVAILABILITY_C | INTEGER |  |
| CARER_RESIDENCY_C | INTEGER |  |
| CARER_REL_TO_PAT_C | VARCHAR (66) |  |
| ACCOMMODATION_TYPE_C | INTEGER |  |
| NEMSMS_ENROLL_YN | VARCHAR (1) |  |
| NEMSMS_ENROLL_UTC_DTTM | DATETIME (UTC) | The instant when the patient's NemSMS status was last checked.  This column only applies to healthcare organizations in Denmark. |
| EXTRACT_STATUS_C *(deprecated)* | INTEGER |  |
| PAT_LIVING_STAT_C | INTEGER |  |
| IS_FETAL_DEMISE_YN | VARCHAR (1) |  |
| ERROR_NEWBORN_YN | VARCHAR (1) |  |
| MEDSYNC_IS_PARTICIPANT_YN | VARCHAR (1) |  |
| MEDSYNC_RECURRENCE | INTEGER | Stores the number of days that are to be between a patient's medication synchronization refills. |
| MEDSYNC_REFILLDATE_DATE | DATETIME | Stores a medication synchronization dispense date for the patient. |
| REFILLMGMT_NOTE_ID | VARCHAR (254) | Stores the ID for a General Use Notes (HNO) record for comments regarding the patient's refill management. |
| IHS_ENROLLMENT_NUM | VARCHAR (40) | This is the American Indian tribal enrollment ID number for the patient. |
| IHS_BENEFICIARY_CLASS_C | INTEGER |  |
| IHS_PRIMARY_TRIBE_C | INTEGER |  |
| IHS_PRIM_TRIBE_BLOOD_QUANTUM_C | INTEGER |  |
| IHS_COMMUNITY_OF_RESIDENCE_C | INTEGER |  |
| IHS_RESIDENCE_SINCE_DATE | DATETIME | Date when the patient first moved to this community of residence (I EPT 4104). |
| IHS_SERVICE_ELIGIBILITY_C | INTEGER |  |
| GENDER_IDENTITY_C | INTEGER |  |
| CURRENT_JOB_START_DATE | DATETIME | The date a patient started in her current job. |
| SEX_ASGN_AT_BIRTH_C | INTEGER |  |
| PREFERENCES_ID | NUMERIC (18,0) | The ID number of the communication preferences record for the patient. |
| DEATH_INFO_SOURCE_C | INTEGER |  |
| BLOOD_REQTS_UTC_DTTM | DATETIME (UTC) | Instant the blood special requirements were last edited |
| BLOOD_REQTS_USER_ID | VARCHAR (18) | Stores the user that set the current special requirements for a patient |
| ADDR_CHG_USER_ID | VARCHAR (18) | The user who initiated the linked address changes. |
| ADDR_CHG_INSTANT_DTTM | DATETIME (Local) | The instant that the linked address changes were initiated. |
| ADDR_CHG_SOURCE | VARCHAR (254) | The source record that initiated the linked address changes. |
| RX_PREF_DELIVERY_MTHD_C | INTEGER |  |
| RX_IS_AUTO_REFILL_YN | VARCHAR (1) |  |
| RX_AUTO_REFILL_PHR_ID | NUMERIC (18,0) | The dispense pharmacy to use for all fills initiated by auto refill. If not set, the owning pharmacy for the prescription being filled will be the dispensing pharmacy for the fill. |
| AUTO_NAME_YN | VARCHAR (1) |  |
| VTJ_LAST_QUERY_UTC_DTTM | DATETIME (UTC) | Instant of the last response received from the Finland Population Register for this patient. |
| BILL_MUNICIPALITY_C | INTEGER |  |
| EDD_BASIS_OB_DT_EVENT_C | INTEGER |  |
| PAT_ADDRESS_ZIP_CODE_ID *(deprecated)* | VARCHAR (50) | *** Deprecated *** In table PATIENT_4, the column PAT_ADDRESS_ZIP_CODE_ID (EPT/1002) has been deprecated. The deprecated column's content/data is no longer available since it is no longer extracted to Clarity.  This links to the EZP record referenced by the patient's zip code and country. |
| VETERAN_DENTAL_CVG_LEVEL_C | INTEGER |  |
| VETERAN_IS_COMBAT_COVERED_YN | VARCHAR (1) |  |
| VETERAN_COMBAT_EXP_DATE | DATETIME | This column stores the expiration date of a patient's combat-level coverage. |
| VETERAN_PRIORITY_GROUP_C | INTEGER |  |
| VETERAN_ENROLLMENT_STATUS_C | INTEGER |  |
| LAST_MAJOR_DEM_UPD_DTTM | DATETIME (Attached) | This item stores the most recent date and time that at least one of this patient's major demographic items was updated in local format. This item is calculated using EPT-85200. |
| LAST_MAJOR_DEM_UPD_UTC_DTTM | DATETIME (UTC) | This item stores the most recent date and time that at least one of this patient's major demographic items was updated in UTC format. |
| LEGACY_HICN | VARCHAR (254) | Stores the patient's Health Insurance Claim Number (HICN) if one was previously available and we've received their Medicare Beneficiary Number (MBI) (stored in PATIENT.MEDICARE_NUM). This value may be needed to look up members during the transition to MBI. |
| RSH_PREF_MYPT_ID | VARCHAR (18) | Indicates the MyChart user who last recorded the patient's explicit research recruitment preference. |
| NEPH_ESRD_START_DT | DATETIME | This item is used to store the date of the patient's first regular chronic dialysis treatment. |
| NEPH_PCRF_LPL_ID | NUMERIC (18,0) | This item is used to store the dialysis patient's primary cause of renal failure. |
| NEPH_2728_VERIFY_YN | VARCHAR (1) |  |
| COS_IS_SEQUESTERED_C | INTEGER |  |

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

_(306 total; showing first 30)_
