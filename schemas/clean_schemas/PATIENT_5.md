# PATIENT_5

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=PATIENT_5

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
| Release Version | Rel 2018 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| PAT_ID | VARCHAR (18) | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| PHYSICAL_IMPAIRED_C | INTEGER |  |
| MEMORY_IMPAIRED_C | INTEGER |  |
| SPEECH_IMPAIRED_C | INTEGER |  |
| DISABLED_VETERAN_C | INTEGER |  |
| VA_RECOGNIZED_C | INTEGER |  |
| HEARING_IMPAIRED_C | INTEGER |  |
| VISUALLY_IMPAIRED_C | INTEGER |  |
| DIFFICULTY_DRESS_BATHE_C | INTEGER |  |
| DIFFICULTY_WITH_ERRAND_C | INTEGER |  |
| ADDR_START_DATE | DATETIME | The start date of this patient's permanent address. |
| CORRSP_CITY | VARCHAR (254) | The city associated with the patient's correspondence address. |
| CORRSP_STATE_C | VARCHAR (66) |  |
| CORRSP_ZIP | VARCHAR (20) | The zip code of the patient's correspondence address. |
| CORRSP_COUNTY_C | VARCHAR (66) |  |
| CORRSP_COUNTRY_C | VARCHAR (66) |  |
| CORRSP_START_DATE | DATETIME | The start date of the patient's correspondence address. |
| CORRSP_END_DATE | DATETIME | The end date of the patient's correspondence address. |
| SC_FIRST_HOME_MUN_DATE | DATETIME | Date of when the social care client's first home municipality was registered. |
| SC_PERM_FORM_OF_RES_C | INTEGER |  |
| SC_GROUNDS_FOR_RES_PERM_C | INTEGER |  |
| SC_RES_PERMIT_VALID_TO_DATE | DATETIME | Date the social care client's residence permit is valid to. |
| SC_QUALFD_FOR_ARA_HOUSING_YN | VARCHAR (1) |  |
| SC_TYPE_OF_RELATIONSHIP_C | INTEGER |  |
| SOCIAL_CARE_PASSPORT_TYPE_C | INTEGER |  |
| SOCIAL_CARE_PASSPORT_EXP_DATE | DATETIME | Date passport expires. |
| CORRSP_HOUSE_NUM | VARCHAR (254) | The house number of the patient's correspondence address. |
| CORRSP_DISTRICT_C | INTEGER |  |
| RSH_PREFS_ANSWER_ID | VARCHAR (18) | The unique ID of the questionnaire answers of the patient's most recent research preference questionnaire submission. |
| RSH_PREFS_ANSWER_DATE | DATETIME | The local date that the patient's most recent research preference questionnaire was submitted. |
| RX_AUTO_REFILL_DELIV_MTHD_C | INTEGER |  |
| PAT_CREAT_WKFLW_C | INTEGER |  |
| UTILITY_RUN_IDENT | INTEGER | The identifier of a particular run for a utility that created this patient. |
| PAT_PHOTO | VARCHAR (254) | This stores the file name of the current patient photo. |
| PEND_PAT_PHOTO | VARCHAR (255) | This stores the file name of a photo pending approval to be added to the chart.  It has most likely been submitted by the patient via Welcome or MyChart. |
| TYPE_AND_SCR_ELIG_YN | VARCHAR (1) |  |
| SG_DOC_ID | VARCHAR (192) | Stores the document ID for the patient |
| SG_DOC_TYPE_C | INTEGER |  |
| SG_DOC_EXPIRY_DATE | DATETIME | Stores the document expiration date for the patient |
| SG_SOCIAL_PRIORITY_YN | VARCHAR (1) |  |
| PERMANENT_ADDR_IS_VALID_C | INTEGER |  |
| PERMANENT_ADDR_VALID_MTHD_C | INTEGER |  |
| PERMANENT_ADDR_VALID_UTC_DTTM | DATETIME (UTC) | The UTC date and time when the permanent address was last validated. |
| PERMANENT_ADDR_VALID_USER_ID | VARCHAR (18) | The unique ID of the end user that last validated the permanent address. |
| TMP_ADDR_IS_VALID_C | INTEGER |  |
| TMP_ADDR_VALID_MTHD_C | INTEGER |  |
| TMP_ADDR_VALID_UTC_DTTM | DATETIME (UTC) | The UTC date and time when the temporary address was last validated. |
| TMP_ADDR_VALID_USER_ID | VARCHAR (18) | The unique ID of the end user that last validated the temporary address. |
| CORRSP_ADDR_IS_VALID_C | INTEGER |  |
| CORRSP_ADDR_VALID_MTHD_C | INTEGER |  |
| CORRSP_ADDR_VALID_UTC_DTTM | DATETIME (UTC) | The UTC date and time when the correspondence address was last validated. |
| CORRSP_ADDR_VALID_USER_ID | VARCHAR (18) | The unique ID of the end user that last validated the correspondence address. |
| PERMANENT_ADDR_VALID_DTTM | DATETIME (Local) | The local date and time when the permanent address was last validated. |
| TMP_ADDR_VALID_DTTM | DATETIME (Local) | The local date and time when the temporary address was last validated. |
| CORRSP_ADDR_VALID_DTTM | DATETIME (Local) | The local date and time when the correspondence address was last validated. |
| NEPH_PCRF_DX_ID | NUMERIC (18,0) | Stores a dialysis patient's primary cause of renal failure diagnosis. |
| RSN_NO_PAT_REL_C | INTEGER |  |
| YAQ_INFOQRY_LAST_RESP_UTC_DTTM *(deprecated)* | DATETIME (UTC) |  |
| YAQ_ADDRQRY_LAST_RESP_UTC_DTTM *(deprecated)* | DATETIME (UTC) |  |
| YAQ_INFOQRY_LAST_ERR_C | VARCHAR (66) |  |
| YAQ_ADDRQRY_LAST_ERR_C | VARCHAR (66) |  |
| RES_SPONSOR | VARCHAR (254) | The name of the person or entity sponsoring the patient's resident status. |
| IQAMA_VALID_YN | VARCHAR (1) |  |
| CONSENT_ABILITY_YN | VARCHAR (1) |  |
| SCHOOL_DISTRICT_NUM | VARCHAR (254) | School district number. |
| PAT_ADDR_IS_UNDELIV_YN | VARCHAR (1) |  |
| MIGRATION_TYPE_C | INTEGER |  |
| MIGRANT_COUNTRY_C | VARCHAR (66) |  |
| BIOMTRC_ENROLL_STAT_C | INTEGER |  |
| BIOMTRC_KI_LAST_ASKED_DATE | DATETIME | This item holds the last date that biometric enrollment was asked of the patient by Welcome. |
| EMPLOYED_IN_HEALTHCARE_YN | VARCHAR (1) |  |
| CONGREGATE_CARE_RESIDENT_YN | VARCHAR (1) |  |
| REG_BIRTH_MOM_NATL_IDENT | VARCHAR (192) | The national identifier (HETU) of the patient's birth mother. This is set by the Finland population register query (VRK). |
| SEEN_DOMESTIC_TRAVEL_ALERT_YN | VARCHAR (1) |  |
| DEATH_INFO_INSTANCE_ID | VARCHAR (25) | The unique identifier (.1 item) for the community instance from which the death notification came. |
| KI_SELF_GUAR_ACCT_VERIF_DATE | DATETIME | This item indicates the most recent date the patient verified whether the self-guarantor billing information is correct in Welcome. |
| KI_SELF_GUAR_ACCT_VERIF_STS_C | INTEGER |  |
| SCHOOL_NAME | VARCHAR (254) | Name of the patient's school |
| SCHOOL_DISTRICT_FREE_TEXT | VARCHAR (254) | The name of the patient's school district |
| ROLE_AT_SCHOOL_C | INTEGER |  |
| TRAVEL_VERIF_BY_PAT_UTC_DTTM | DATETIME (UTC) | Instant when the patient or a patient representative last verified travel history in Welcome or MyChart. |
| PAT_PHONETIC_NAME | VARCHAR (200) | Stores the phonetic spelling of the patient's name. |
| PAT_RETIREMENT_DATE | DATETIME | The date of a patient's retirement for MSPQ purposes. |
| SPOUSE_RETIREMENT_DATE | DATETIME | The date of a patient's spouse's retirement for MSPQ purposes. |
| DRIVERS_LICENSE_NUM | VARCHAR (254) | The patient's driver's license number. |
| DRIVERS_LICENSE_STATE_C | VARCHAR (66) |  |
| EMPLOYMENT_HIRE_DATE | DATETIME | The date that a patient was hired at their employer. |
| EMPLOYER_FAX | VARCHAR (256) | the fax number of the patient's employer. |
| WORK_PHONE | VARCHAR (254) | The patient's work phone number. |
| H1B_WORK_VISA_YN | VARCHAR (1) |  |
| STUDENT_VISA_YN | VARCHAR (1) |  |
| BIRTH_COUNTY_C | VARCHAR (66) |  |
| CORRESP_CONTACT | VARCHAR (254) | This name of the contact person associated with a patient's correspondence address. |
| CUR_INP_SUMMARY_BLOCK_ID | NUMERIC (18,0) | The current Inpatient summary block ID. |
| PREFERRED_FORM_ADDRESS | VARCHAR (254) | How the patient prefers to be addressed. |
| PAT_ACADEMIC_DEGREE_C | VARCHAR (66) |  |
| PREFERRED_NAME_TYPE_C | INTEGER |  |
| AHCIC_NUM | VARCHAR (192) | The patient's AHCIC number. |

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

_(181 total; showing first 30)_
