# PATIENT_2

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=PATIENT_2

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
| Release Version | SPRING 2007 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| PAT_ID | VARCHAR (18) | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| RECORD_TYPE_6_C | INTEGER |  |
| BIRTH_TM | 110 | The date and time of the patient's birth in 24 hour format. |
| DEATH_TM | 115 | The date and time of the patient's death in 24 hour format. |
| FAX | VARCHAR (254) | The patient's fax number. |
| CITIZENSHIP_C | VARCHAR (66) |  |
| MED_HX_NOTE_ID | VARCHAR (254) | This column contains a link to the General Use Notes (HNO) meds history note for this patient. |
| IS_ADOPTED_YN | VARCHAR (1) |  |
| HEARING_IMPAIRED_YN *(deprecated)* | VARCHAR (1) |  |
| VISUALLY_IMPAIRE_YN *(deprecated)* | VARCHAR (1) |  |
| BIRTH_HOSPITAL | VARCHAR (254) | Capture the name of the hospital where the patient was born or first seen after a non-hospital birth. |
| ALRGY_UPD_INST | 17740 | The PATIENT table extracts the last date on which the patient's allergy information was verified. For more granularity, this table extracts the instant (date and time) that this information was verified. |
| BIRTH_CITY | VARCHAR (254) | The patient's city of birth. |
| BIRTH_ST_C | VARCHAR (66) |  |
| OB_CONVERSION_YN | VARCHAR (1) |  |
| SCHOOL_C | INTEGER |  |
| REFERRAL_SOURCE_ID | VARCHAR (18) | The unique ID of the provider or other source that referred the patient to the facility. This is distinct from the encounter-specific referral source in PAT_ENC. |
| AMBRX_DOSING_WEIGHT *(deprecated)* | FLOAT | The column is deprecated and does not extract any data. Instead of using this column, use recent value of Clarity column WEIGHT in Clarity table PAT_ENC to get the recent patient's weight. |
| AMBRX_DOSE_WT_INST *(deprecated)* | DATETIME | The column is deprecated and does not extract any data. Instead of using this column, use recent value of Clarity column VITALS_TAKEN_TM in Clarity table PAT_ENC_2 to get the recent date and time the patient's weight was taken. |
| PAT_NAME_RECORD_ID | VARCHAR (50) | The networked item that points to the patient's name record (EAN). |
| TMP_HOUSE_NUM | VARCHAR (254) | Contains the house number of the patient's temporary address. |
| TMP_DISTRICT_C | INTEGER |  |
| COMM_METHOD_C | INTEGER |  |
| FOSTER_CHILD_YN | VARCHAR (1) |  |
| CONF_PAT_REAL_NAME | VARCHAR (192) | The real name of a confidential patient. |
| PAT_CONF_NM_REC_ID | VARCHAR (50) | The networked item pointing to the name record for the patient's confidential name. |
| ACTIVE_IER_ID | VARCHAR (18) | Link to active Identity History (IER) record for this patient. |
| OTH_CITY | VARCHAR (254) | Contains the city for the patient's prescription address, which can be used by pharmacy to determine where to mail prescriptions. |
| OTH_ZIP | VARCHAR (192) | Contains the zip code for the patient's prescription address, which can be used by pharmacy to determine where to mail prescriptions. |
| OTH_PHONE | VARCHAR (254) | Contains the phone number for the patient's prescription address, which can be used by pharmacy to determine where to mail prescriptions. |
| OTH_EMAIL | VARCHAR (254) | Contains the email for the patient's prescription address, which can be used by pharmacy to determine where to mail prescriptions. |
| OTH_CONTACT_PERSON | VARCHAR (254) | Contains the contact person for the patient's prescription address, which can be used by pharmacy to determine where to mail prescriptions. |
| OTH_HOUSE_NUMBER | VARCHAR (254) | Contains the house number for the patient's prescription address, which can be used by pharmacy to determine where to mail prescriptions. |
| OTH_DISTRICT_C | INTEGER |  |
| OTH_COUNTY_C | VARCHAR (66) |  |
| OTH_COUNTRY_C | VARCHAR (66) |  |
| OTH_START_DATE | DATETIME | Contains the start date for the patient's prescription address, which can be used by pharmacy to determine where to mail prescriptions. |
| OTH_END_DATE | DATETIME | Contains the end date for the patient's prescription address, which can be used by pharmacy to determine where to mail prescriptions. |
| DEF_ADDRESS_C | VARCHAR (66) |  |
| OTH_STATE_C | VARCHAR (66) |  |
| MAIDEN_NAME | VARCHAR (254) | The patient's maiden name. |
| EMPR_CITY | VARCHAR (254) | The city of the patient's employer. |
| EMPR_STATE_C | VARCHAR (66) |  |
| EMPR_ZIP | VARCHAR (254) | The ZIP code of the patient's employer. |
| EMPR_COUNTRY_C | VARCHAR (66) |  |
| EMPR_PHONE | VARCHAR (254) | The phone number of the patient's employer. |
| BILL_INSTRUCT_C | INTEGER |  |
| PAT_ASSIST_C | INTEGER |  |
| BILL_COMMENT | VARCHAR (254) | General comments regarding patient billing instruction |
| TEMP_PAT_FLAG_C | INTEGER |  |
| EOB_ADDRESS_C | INTEGER |  |
| TEMP_NAME_YN | VARCHAR (1) |  |
| EMPR_HOUSE_NUM | VARCHAR (20) | The house number of the patient's employer. |
| EMPR_DISTRICT_C | INTEGER |  |
| CHART_ABSTD_YN | VARCHAR (1) |  |
| MOTHER_HEIGHT | NUMERIC (18,2) | Height of the patient's mother.  This is used for calculations in the Growth Charts activity. |
| FATHER_HEIGHT | NUMERIC (18,2) | Height of the patient's father.  This is used for calculations in the Growth Charts activity. |
| PAT_VERIFICATION_ID | NUMERIC (18,0) | Verification record for this patient |
| ALRGY_REV_STAT_C | INTEGER |  |
| ALRGY_REV_CMT | VARCHAR (300) | This item stores a comment associated with the review of allergies. |
| REVERSE_NATL_ID | VARCHAR (50) | Used to store reverse National Identifier in an indexed item for patient search of partial National Identifier. |
| ADV_DIR_REV_DT | DATETIME | The date on which a user last reviewed the patient's advanced directive. |
| ADV_DIR_REV_USER_ID | VARCHAR (18) | The user who last reviewed the patient's advanced directive. |
| LIVING_ARRANGE_C | INTEGER |  |
| DRIVER_LIC_EXP_DATE | DATETIME | The expiration date for the patient's drivers license. |
| LAST_ACCESS_DATE *(deprecated)* | DATETIME | *** Deprecated *** In table PATIENT_2, the column LAST_ACCESS_DATE has been deprecated. The deprecated column's content/data is no longer available since it is no longer populated in Chronicles. |
| PED_COMMENT | VARCHAR (28000) | Free-text pediatric comments. |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| B-TREE INDEX | EIX_PATIENT_2_ACTIVE_IER | PAT_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_PATIENT_2_ACTIVE_IER | ACTIVE_IER_ID | 2 | Yes | Yes |  |
| B-TREE INDEX | EIX_PATIENT_2_ACTIVE_IER_ONLY | ACTIVE_IER_ID | 1 | Yes | Yes |  |

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
| 1 | PAT_ID | V_PAT_HX_TOB_USE | PAT_ID | Unknown | Unknown | No |  |

_(126 total; showing first 30)_
