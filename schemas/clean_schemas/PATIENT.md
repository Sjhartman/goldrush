# PATIENT

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=PATIENT

## Description

The PATIENT table contains one record for each patient in your system. The data contained in each record consists of demographics, PCP and primary location information, registration information, and other information.

**Primary table** in this group (137 cols). Overflow siblings joined on shared key: PATIENT_2 (69 cols), PATIENT_3 (103 cols), PATIENT_4 (101 cols), PATIENT_5 (101 cols), PATIENT_6 (40 cols). Prefer this table for most queries.

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
| PAT_ID | VARCHAR (18) | The unique ID of the patient record for this row. This column is frequently used by other tables to link to PATIENT. |
| PAT_NAME | VARCHAR (200) | The patient?s name in the format Lastname, Firstname MI. |
| ADD_LINE_1 | VARCHAR (50) | This column, although not deprecated, should no longer be used. Instead you should use the column ADDRESS (EPT 50) in table PAT_ADDRESS. Patient addresses can contain an unlimited number of lines. Previously you could only access the first two lines with the columns PATIENT.ADD_LINE_1 and PATIENT.ADD_LINE_2. Now, there is a new table, called PAT_ADDRESS, which allows you to get all lines of the patient's permanent address. We have chosen not to deprecate PATIENT.ADD_LINE_1 and PATIENT.ADD_LINE_2 because doing so would break any custom reports that use these columns.  To use the new column, join column PATIENT.PAT_ID to table PAT_ADDRESS on column PAT_ID and get the ADDRESS value and also the LINE value. Each PAT_ID value represents a different patient, and each LINE value represents a different line of that patient's address. |
| ADD_LINE_2 | VARCHAR (50) | This column, although not deprecated, should no longer be used. Instead you should use the column ADDRESS (EPT 50) in table PAT_ADDRESS. Patient addresses can contain an unlimited number of lines. Previously you could only access the first two lines with the columns PATIENT.ADD_LINE_1 and PATIENT.ADD_LINE_2. Now, there is a new table, called PAT_ADDRESS, which allows you to get all lines of the patient's permanent address. We have chosen not to deprecate PATIENT.ADD_LINE_1 and PATIENT.ADD_LINE_2 because doing so would break any custom reports that use these columns.  To use the new column, join column PATIENT.PAT_ID to table PAT_ADDRESS on column PAT_ID and get the ADDRESS value and also the LINE value. Each PAT_ID value represents a different patient, and each LINE value represents a different line of that patient's address. |
| CITY | VARCHAR (50) | The city in which the patient lives. |
| STATE_C | VARCHAR (66) |  |
| COUNTY_C | VARCHAR (66) |  |
| COUNTRY_C | VARCHAR (66) |  |
| ZIP | VARCHAR (60) | The ZIP Code area in which the patient lives. |
| HOME_PHONE | VARCHAR (192) | The patient?s home phone number. |
| WORK_PHONE | VARCHAR (50) | The patient?s work phone number. |
| EMAIL_ADDRESS | VARCHAR (255) | The patient?s e-mail address. |
| RESTRICTED_YN | VARCHAR (1) |  |
| PAT_STATUS *(deprecated)* | VARCHAR (10) |  |
| BIRTH_DATE | 110 | The date on which the patient was born. |
| SEX *(deprecated)* | VARCHAR (1) |  |
| ETHNIC_GROUP_C | INTEGER |  |
| MARITAL_STATUS_C | INTEGER |  |
| RELIGION_C | INTEGER |  |
| LANGUAGE_C | VARCHAR (66) |  |
| SSN | VARCHAR (192) | The patient?s Social Security Number. This number is formatted as 999-99-9999, and a single trailing alphabetic character is also allowed. |
| REG_DATE | DATETIME | The date on which the last patient verification occurred.  If a patient was verified and then re-verified at a later date, this column will show the re-verified date.  This column will be null for patients that have never been verified. |
| REG_STATUS_C | VARCHAR (66) |  |
| EPICCARE_PAT_YN | VARCHAR (1) |  |
| MEDICARE_NUM | VARCHAR (254) | The patient?s Medicare-assigned identification number, if applicable. |
| MEDICAID_NUM | VARCHAR (20) | Patient's Medicaid ID. |
| POWER_OF_ATTRNY_YN | VARCHAR (1) |  |
| POWER_OF_ATTRNY_DT | DATETIME | The last date the patient was asked about power of attorney, not the date the patient designated a power of attorney or filed it with the facility. |
| ADV_DIRECTIVE_YN | VARCHAR (1) |  |
| ADV_DIRECTIVE_DATE | DATETIME | The date a living will was received from the patient. |
| DEF_FIN_CLASS_C | VARCHAR (66) |  |
| FIN_STATUS_C | INTEGER |  |
| CUR_PCP_PROV_ID | VARCHAR (18) | The unique ID of the provider record for the patient?s current General Primary Care Provider as of the enterprise reporting extract. This ID may be encrypted. |
| CLAIM_ALERT_C | INTEGER |  |
| CUR_PRIM_LOC_ID | NUMERIC (18,0) | The unique ID of the location record for the patient?s Primary Location as of the time of the enterprise reporting extract. This column is retrieved from the item Primary Location. |
| LEGAL_STATUS_C | INTEGER |  |
| VETERAN_STATUS_C | VARCHAR (66) |  |
| MOTHER_PAT_ID | VARCHAR (18) | The unique ID of the system patient record belonging to the mother of this patient. This item is populated if the mother?s record is linked to the patient record in enterprise registration system Registration?s emergency contacts. This ID may be encrypted. |
| FATHER_PAT_ID | VARCHAR (18) | The unique ID of the system patient record belonging to the father of this patient. This item is populated if the father?s record is linked to the patient record in enterprise registration system Registration?s emergency contacts. This ID may be encrypted. |
| BIRTH_LOC_ID *(deprecated)* | NUMERIC (18,0) | This item was used in a previous version, and is no longer populated. Do not report on this item. |
| BIRTH_STATUS_C | INTEGER |  |
| BIRTH_WRIST_BAND | VARCHAR (25) | The identifier on the newborn?s wrist or ankle band. This item is populated by ADT. |
| PED_BIRTH_LEN *(deprecated)* | VARCHAR (20) | In table PATIENT, the column PED_BIRTH_LEN (EPT/19400) has been deprecated. This column has been replaced by column PED_BIRTH_LEN_NUM (EPT/15300) in PATIENT_3. To lookup the deprecated columns' value after the Clarity Compass upgrade, use the column PED_BIRTH_LEN_NUM in table PATIENT_3.  This column which has a datatype of VARCHAR is replaced with a column whose datatype is NUMERIC. This will allow report writers to use numeric comparison operators on this column. The deprecated column's data is no longer available since it is no longer extracted to Clarity. |
| PED_BIRTH_WT *(deprecated)* | VARCHAR (12) | In table PATIENT, the column PED_BIRTH_WT (EPT/19401) has been deprecated. This column has been replaced by column PED_BIRTH_WT_NUM (EPT/15301) in PATIENT_3. To lookup the deprecated columns' value after the Clarity Compass upgrade, use the column PED_BIRTH_WT_NUM in table PATIENT_3.  This column which has a datatype of VARCHAR is replaced with a column whose datatype is NUMERIC. This will allow report writers to use numeric comparison operators on this column. |
| PED_APGAR_ONE *(deprecated)* | VARCHAR (255) | In table PATIENT, the column PED_APGAR_ONE (EPT/19405) has been deprecated. This column has been replaced by column PED_APGAR_ONE_C (EPT/15305) in PATIENT_3. To lookup the deprecated columns' value after the Clarity Compass upgrade, use the column PED_APGAR_ONE_C in table PATIENT_3.  This column which has a datatype of VARCHAR is replaced with a column whose datatype is NUMERIC. This will allow report writers to use numeric comparison operators on this column. |
| PED_APGAR_TWO *(deprecated)* | VARCHAR (255) | In table PATIENT, the column PED_APGAR_TWO (EPT/19406) has been deprecated. This column has been replaced by column PED_APGAR_FIVE_C (EPT/15306) in PATIENT_3. To lookup the deprecated columns' value after the Clarity Compass upgrade, use the column PED_APGAR_FIVE_C in table PATIENT_3.  This column which has a datatype of VARCHAR is replaced with a column whose datatype is NUMERIC. This will allow report writers to use numeric comparison operators on this column. |
| PED_APGAR_TEN *(deprecated)* | VARCHAR (255) | In table PATIENT, the column PED_APGAR_TEN (EPT/19407) has been deprecated. This column has been replaced by column PED_APGAR_TEN_C (EPT/15307) in PATIENT_3. To lookup the deprecated columns' value after the Clarity Compass upgrade, use the column PED_APGAR_TEN_C in table PATIENT_3.  This column which has a datatype of VARCHAR is replaced with a column whose datatype is NUMERIC. This will allow report writers to use numeric comparison operators on this column. |
| PED_COMMENT | VARCHAR (508) | Free-text pediatric comments. The first 255 characters. Longer version found at PATIENT_2__PED_COMMENT. |
| PED_MULT_BIRTH_ORD | INTEGER | For multiple births, the place in the birth order of the current newborn patient. |
| PED_MULT_BIRTH_TOT | INTEGER | The total number of births during the mother?s labor and delivery of this newborn patient. |
| EPIC_PAT_ID | VARCHAR (18) | The unique ID assigned to the patient record (EPT .1). This ID may be hidden in a public view of the PATIENT table. |
| REC_CREATE_DATE | DATETIME | The date the patient record was created in the system. |
| CREATE_USER_ID | VARCHAR (18) | The unique ID of the system user who entered this patient?s record. This ID may be encrypted. |
| PRIM_CVG_ID | No |  |
| PRIM_EPM_ID | No |  |
| PRIM_EPP_ID | No |  |
| PRIM_FC | EPM |  |
| PERM_CHART_LOC_C | INTEGER |  |
| CUR_CHART_LOC_C | INTEGER |  |
| PAT_MRN_ID | VARCHAR (102) | The patient's medical record number (MRN), of the type associated with the patient's current primary location. |
| DEATH_DATE | 115 | The date of death for the patient. |
| UPDATE_DATE | No | The time this patient record was pulled into enterprise reporting. |
| EOB_FLAG_YN | VARCHAR (1) |  |
| REC_CREATE_PAT_ID | VARCHAR (18) | The unique ID of the system user who created this patient?s record. This ID may be encrypted.   NOTE: For historical reasons, the column name ends in PAT_ID and cannot be changed; despite its name, it does not link to patient ID. It instead links to CLARITY_EMP.USER_ID. |
| ORGAN_DONOR_YN | VARCHAR (1) |  |
| TMP_ADDR_LINE_1 | VARCHAR (50) | This column, although not deprecated, should no longer be used. Instead you should use the column TEMP_ADDRESS (EPT 5430) in table PAT_TEMP_ST_ADDR. Patient addresses can contain an unlimited number of lines. Previously you could only access the first two lines with the columns PATIENT.TMP_ADDR_LINE_1 and PATIENT.TMP_ADDR_LINE_2. PAT_TEMP_ST_ADDR allows you to get all lines of the patient's temporary address. We have chosen not to deprecate PATIENT.TMP_ADDR_LINE_1 and PATIENT.TMP_ADDR_LINE_2 because doing so would break any custom reports that use these columns.  To use the new column, join column PATIENT.PAT_ID to table PAT_TEMP_ST_ADDR on column PAT_ID and get the TEMP_ADDRESS and LINE values. Each PAT_ID value represents a different patient, and each LINE value represents a different line of that patient's temporary address. |
| TMP_ADDR_LINE_2 | VARCHAR (50) | This column, although not deprecated, should no longer be used. Instead you should use the column TEMP_ADDRESS (EPT 5430) in table PAT_TEMP_ST_ADDR. Patient addresses can contain an unlimited number of lines. Previously you could only access the first two lines with the columns PATIENT.TMP_ADDR_LINE_1 and PATIENT.TMP_ADDR_LINE_2. PAT_TEMP_ST_ADDR allows you to get all lines of the patient's temporary address. We have chosen not to deprecate PATIENT.TMP_ADDR_LINE_1 and PATIENT.TMP_ADDR_LINE_2 because doing so would break any custom reports that use these columns.  To use the new column, join column PATIENT.PAT_ID to table PAT_TEMP_ST_ADDR on column PAT_ID and get the TEMP_ADDRESS and LINE values. Each PAT_ID value represents a different patient, and each LINE value represents a different line of that patient's temporary address. |
| TMP_CITY | VARCHAR (40) | Contains the city in which the patient is temporarily residing. |
| TMP_STATE_C | VARCHAR (66) |  |
| TMP_COUNTRY_C | VARCHAR (66) |  |
| TMP_ZIP | VARCHAR (50) | Contains the ZIP Code in which the patient is temporarily residing. |
| TMP_HOME_PHONE | VARCHAR (50) | Contains the temporary phone number where the patient can be reached. |
| TMP_COUNTY_C | VARCHAR (66) |  |
| TMP_ADDR_START_DT | DATETIME | Contains the starting effective date of the patients temporary address information. |
| TMP_ADDR_END_DT | DATETIME | Contains the ending effective date of the patients temporary address information. |
| TMP_CARE_OF_PERSON | VARCHAR (254) | Contains the name of the contact person for the patient at the temporary residence. |
| IS_MAIL_BLOCKED_YN *(deprecated)* | VARCHAR (1) |  |
| IS_PHONE_REMNDR_YN | VARCHAR (1) |  |
| CASE_SPVSR_USER_ID | VARCHAR (18) | The user ID of the person in charge of this patient's case. |
| PAT_LAST_NAME | VARCHAR (200) | The last name of the patient. |
| PAT_FIRST_NAME | VARCHAR (200) | The first name of the patient. |
| PAT_MIDDLE_NAME | VARCHAR (508) | The middle name of the patient. |
| PAT_TITLE_C | VARCHAR (66) |  |
| PAT_NAME_SUFFIX_C | INTEGER |  |
| SPECIAL_STATUS_C | INTEGER |  |
| LANG_CARE_C | VARCHAR (66) |  |
| LANG_WRIT_C | VARCHAR (66) |  |
| PROXY_PAT_YN | VARCHAR (1) |  |
| PROXY_NAME | VARCHAR (50) | The name of the proxy for the patient. |
| PROXY_PHONE | VARCHAR (50) | The phone number of the proxy for the patient. |
| PROXY_PACK_YN | VARCHAR (1) |  |
| EMPLOYER_ID | VARCHAR (254) | This is the unique ID of the patient's employer if the item linking the patient to an employer (I EAF 6410) is set to 1.  This is free text if the item linking the patient to an employer (I EAF 6410) is set to 2. |
| EMPY_STATUS_C | INTEGER |  |
| CM_PHY_OWNER_ID | VARCHAR (25) | ID of the physical deployment owner for this record.  Physical owners will be where the data is hosted, either on the cross-over server or the owner deployment. |
| CM_LOG_OWNER_ID | VARCHAR (25) | ID of the logical deployment owner for this record.  Logical owners show the deployment where the record was created but doesn't represent if the record is a part of version skew. |
| ALRGY_UPD_DATE | DATETIME | The most recent date on which the patient's allergy information was verified. |
| ALRGY_UPD_USER_ID | VARCHAR (18) | The user id (EMP_ID) of the user to most recently verify the patient's allergy information. |
| GUARDIAN_NAME | VARCHAR (254) | The name of the patient's legal guardian, if any. |
| PREF_CLIN_ZIP | VARCHAR (254) | The zip code of the patient's preferred clinic. |
| PREF_PCP_SEX_C | VARCHAR (66) |  |
| PREF_PCP_SPEC_C | VARCHAR (66) |  |
| PREF_PCP_LANG_C | VARCHAR (66) |  |
| COUNTRY_OF_ORIG_C | VARCHAR (66) |  |
| COMM_PREF_LTR_C | INTEGER |  |
| PED_BIRTH_HEAD_CIR *(deprecated)* | VARCHAR (254) | In table PATIENT, the column PED_BIRTH_HEAD_CIR (EPT/19402) has been deprecated. This column has been replaced by column PED_BIRTH_HD_CR_NUM (EPT/15302) in PATIENT_3. To lookup the deprecated columns' value after the Clarity Compass upgrade, use the column PED_BIRTH_HD_CR_NUM in table PATIENT_3.  This column which has a datatype of VARCHAR is replaced with a column whose datatype is NUMERIC. This will allow report writers to use numeric comparison operators on this column. |
| PED_DISCHRG_WT *(deprecated)* | VARCHAR (254) | In table PATIENT, the column PED_DISCHRG_WT (EPT/19400) has been deprecated. This column has been replaced by column PED_DISCHRG_WGT_NUM (EPT/15303) in PATIENT_3. To lookup the deprecated columns' value after the Clarity Compass upgrade, use the column PED_DISCHRG_WGT_NUM in table PATIENT_3.  This column which has a datatype of VARCHAR is replaced with a column whose datatype is NUMERIC. This will allow report writers to use numeric comparison operators on this column. |
| PED_CESAREAN_YN | VARCHAR (1) |  |
| PED_GEST_AGE | VARCHAR (254) | Displays a newborns gestational age in weeks as a VARCHAR. For example 38 4/7 would indicate a gestation age of 38 weeks a 4 days.  Column PED_GEST_AGE_NUM (EPT/15308) in PATIENT_3 displays gestational age numerically as total number of completed weeks. Column PED_GEST_AGE_NUM in table PATIENT_3 has a datatype of NUMERIC.  This will allow report writers to use numeric comparison operators on that column. |
| PED_NOUR_METH_C | INTEGER |  |
| PED_DELIVR_METH_C | VARCHAR (66) |  |
| PED_MULTI_BIRTH_YN | VARCHAR (1) |  |
| EDD_DT | DATETIME | The patient's Expected Date of Delivery. |
| EDD_ENTERED_DT | DATETIME | Date the Expected Date of Delivery was entered. |
| EDD_CMT | VARCHAR (1000) | Expected Date of Delivery comment. |
| INTRPTR_NEEDED_YN | VARCHAR (1) |  |
| PCP_DON_CHART_YN | VARCHAR (1) |  |
| PAT_HAS_IOL_YN | VARCHAR (1) |  |
| SPECIES_C | VARCHAR (66) |  |
| PED_BIRTH_LABOR | VARCHAR (254) | Stores the duration of labor related to a patient's birth history. |
| PED_HOSP_DAYS | VARCHAR (254) | Stores the number of days spent in the hospital related to a patient's birth history. |
| PED_HOSP_NAME | VARCHAR (254) | Stores the name of the hospital where the patient was born as part of birth history. |
| PED_HOSP_LOCATION | VARCHAR (254) | Stores the hospital location where the patient was born as part of birth history. |
| MEDS_LAST_REV_TM | DATETIME (Local) | Stores the last time the encounter medications list was reviewed. |
| MEDS_LST_REV_USR_ID | VARCHAR (18) | Stores the last user to review the encounter medications list. |
| SELF_VERIF_DATE | DATETIME | Date of last self-verification at the patient kiosk. |
| SELF_VERIF_STATU_YN | VARCHAR (1) |  |
| SELF_EC_VERIF_DATE | DATETIME | Most recent date patient marked their emergency contact information as verified. |
| SELF_EC_VERIF_ST_YN | VARCHAR (1) |  |
| LAST_MYC_ASKED_DATE | DATETIME | Last date the patient was asked to sign up for mychart from kiosk |
| EMPR_ID_CMT | VARCHAR (254) | A free text comment that can be entered when the value that is considered to be "Other" is selected as the employer. This option is available only if your organization has chosen to link the patient employer to the Employer (EEP) master file in the Facility Profile. |
| HOUSE_NUM | VARCHAR (254) | House Number address field, added to support international address formats. |
| DISTRICT_C | INTEGER |  |
| PAT_STATUS_C | VARCHAR (66) |  |
| MEDS_LAST_REV_CSN | NUMERIC (18,0) | Stores the contact serial number of the encounter in which the patient's current medications list was last reviewed. |
| SEX_C | VARCHAR (66) |  |
| RECORD_STATE_C | INTEGER | Surrogate key used to uniquely identify rows in this (and only this) table on Cogito Cloud only, do not assume the surrogate key in this table will correspond to the surrogate key in another table |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| B-TREE INDEX | EIX_PATIENT_CUPCPRID | CUR_PCP_PROV_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_PATIENT_CUPRLOID | CUR_PRIM_LOC_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_PATIENT_EPPAID | EPIC_PAT_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_REC_CREATE_DATE | REC_CREATE_DATE | 1 | Yes | Yes |  |

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
| 1 | PAT_ID | V_PAT_HX_TOB_USE | PAT_ID | Unknown | Unknown | No |  |

_(450 total; showing first 30)_
