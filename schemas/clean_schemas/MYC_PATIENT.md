# MYC_PATIENT

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=MYC_PATIENT

## Description

The MYC_PATIENT table contains one row for each web-based chart system account. The data contained in each row consists of basic account information related to logins and passwords, as well as data that the patient has entered and stored in web-based chart system.

**Primary table** in this group (102 cols). Overflow siblings joined on shared key: MYC_PATIENT_2 (16 cols). Prefer this table for most queries.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | WPR |
| Release Version | EPIC 2002 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| MYPT_ID | VARCHAR (18) | The unique ID of the patient's web-based chart system account record. |
| PAT_ID | VARCHAR (18) | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| PROXY_ACCOUNT_YN | VARCHAR (1) |  |
| LOGIN_NAME | VARCHAR (128) | The patient's login name for the web-based chart system. |
| MYC_STATUS_C *(deprecated)* | INTEGER |  |
| LAST_LOGIN_TIME | DATETIME (Local) | A timestamp indicating the last time the web-based chart system patient successfully logged in. |
| NUM_FAILED_LOGINS | INTEGER | The number of consecutive failed logins. This item goes back to zero after a successful login. |
| FORCE_PWD_CHG_YN | VARCHAR (1) |  |
| LAST_PW_CHANGE | DATETIME | The date when the web-based chart system password was last changed. |
| MINIMUM_PW_AGE *(deprecated)* | INTEGER | *** Deprecated *** Item discontinued ****** This column is deprecated and does not extract any data. There is no replacement for this column. |
| MAXIMUM_PW_AGE *(deprecated)* | INTEGER | *** Deprecated *** Item discontinued ****** This column is deprecated and does not extract any data. There is no replacement for this column. |
| RESPONSE_PREF_C | INTEGER |  |
| OTHER_RESP_PREF | VARCHAR (255) | If the web-based chart system patient chooses a value of Other in RESPONSE_PREF_C and enters custom text, then the custom text is stored in this item. |
| MYCHART_EXP_DATE | DATETIME | The expiration date (if one has been set) of the web-based chart system account. When this date is reached, the web-based chart system user is no longer allowed to login to the system. |
| SEND_EMAIL_YN *(deprecated)* | VARCHAR (1) |  |
| WALLET_ID | NUMERIC (18,0) | This column is deprecated and does not extract any data. The feature for which this column was created is no longer in use. There is no replacement column. |
| WL_PROBLEMS_ID | NUMERIC (18,0) | The unique ID of the web-based chart system note  concerning problems entered by the patient into the wallet card. |
| WL_MEDS_ID | NUMERIC (18,0) | The unique ID of the web-based chart system note concerning medications entered by the patient into the wallet card. |
| WL_ALLERGIES_ID | NUMERIC (18,0) | The unique ID of the web-based chart system note  concerning allergies entered by the patient into the wallet card. |
| EMPLOYER_NAME | VARCHAR (255) | Free text Employer name entered by the web-based chart system patient in the Insurance section of Your Health Record in the web-based chart system. |
| INSURANCE_NAME | VARCHAR (255) | Free text Insurance Provider name entered by the web-based chart system patient in the Insurance section of Your Health Record in the web-based chart system. |
| GROUP_NUM | VARCHAR (60) | Free text Group Number entered by the web-based chart system patient in the Insurance section of Your Health Record in the web-based chart system. |
| MEMBER_NUM | VARCHAR (60) | Free text Member ID entered by the web-based chart system patient in the Insurance section of Your Health Record in the web-based chart system. |
| INS_PHONE_NUM | VARCHAR (50) | Free text Contact Phone number entered by the web-based chart system patient in the Insurance section of Your Health Record in the web-based chart system. |
| PROB_MYCNOTE_ID | NUMERIC (18,0) | The unique ID of the note that the patient added to the Current Health Issues section of the web-based chart system. |
| MEDS_MYCNOTE_ID | NUMERIC (18,0) | The unique ID of the note that the patient added to the Medications section of the web-based chart system. |
| ALLERGY_MYCNOTE_ID | NUMERIC (18,0) | The unique ID of the note that the patient added to the Allergies section of the web-based chart system. |
| IMMUNE_MYCNOTE_ID | NUMERIC (18,0) | The unique ID of the note that the patient added to the Immunization History section of the web-based chart system. |
| RMINDR_MYCNOTE_ID | NUMERIC (18,0) | The unique ID of the note that the patient added to the Health Reminders section of the web-based chart system. |
| FAM_HX_MYCNOTE_ID | NUMERIC (18,0) | The unique ID of the note that the patient added to the Family Medical History section of the web-based chart system. |
| SURG_HX_MYCNOTE_ID | NUMERIC (18,0) | The unique ID of the note that the patient added to the Surgical History section of the web-based chart system. |
| MED_HX_MYCNOTE_ID | NUMERIC (18,0) | The unique ID of the note that the patient added to the Medical History section of the web-based chart system. |
| FAM_STS_MYCNOTE_ID | NUMERIC (18,0) | The unique ID of the note that the patient added to the Family Status section of the web-based chart system. |
| SOC_HX_MYCNOTE_ID | NUMERIC (18,0) | The unique ID of the note that the patient added to the Social History section of the web-based chart system. |
| LAST_ACCESS_TIME | DATETIME (Local) | This item stores the instant when the patient last elected not to be shown the Terms & Conditions page. |
| UPDATE_DATE | No | *** Deprecated *** In table MYC_PATIENT, the column UPDATE_DATE has been deprecated.  This column should no longer be used to track updates to MYC_PATIENT. Flip "Track row updates?" to "Yes" in the Information Activity to enable capturing of row updates on MYC_PATIENT using ESP_CR_ALTERED_ROWS.   The date and that time this web-based chart system account record was pulled into enterprise reporting. |
| ALT_LOGIN_NAME | VARCHAR (254) | The login name for this web-based chart system patient at the alternate website. |
| ALT_LAST_LOGN_TIME | DATETIME (Local) | A timestamp indicating the last time the web-based chart system patient successfully logged in to the alternate website. |
| ALT_FAIL_LOGN_ATMT | INTEGER | The number of consecutive failed login attempts on the alternate website. This item goes back to zero after a successful login. |
| ALT_FORCE_PWD_YN | VARCHAR (254) |  |
| ALT_LAST_PSWD_UPDT | DATETIME | The date when the web-based chart system password was last changed for the alternate website. |
| MIN_ALT_PSWD_AGE *(deprecated)* | INTEGER | *** Deprecated *** Item discontinued ****** This column is deprecated and does not extract any data. There is no replacement for this column. |
| MAX_ALT_PSWD_AGE *(deprecated)* | INTEGER | *** Deprecated *** Item discontinued ****** This column is deprecated and does not extract any data. There is no replacement for this column. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| MYC_ACCT_TYPE_C | INTEGER |  |
| PROXY_LAST_ACCESS | DATETIME (Local) | This item stores the instant when the patient last elected not to be shown the Proxy Disclaimer page. |
| NON_PATIENT_YN | VARCHAR (1) |  |
| ACCESS_CODE | VARCHAR (192) | Access code that can be used to sign up for MyChart.  Gets deleted upon use. |
| ACCESS_CODE_TM | DATETIME (UTC) | Timestamp -- instant when access code was created. |
| CITY | VARCHAR (254) | Non-patient proxy address data - city field |
| STATE_C | VARCHAR (66) |  |
| ZIP | VARCHAR (254) | Non-patient proxy address data - ZIP code field |
| COUNTRY_C | VARCHAR (66) |  |
| COUNTY_C | VARCHAR (66) |  |
| HOUSE_NUM | VARCHAR (254) | Non-patient proxy address data - house number field |
| DISTRICT_C | INTEGER |  |
| LAST_PW_CHANGE_DTTM | DATETIME (Local) | Records the instant that password for this MyChart account was last  changed.  Time zone is local time. |
| HOME_PHONE | VARCHAR (128) | The patient account's home phone number. |
| MOBILE_PHONE | VARCHAR (128) | The patient account's mobile phone number. |
| WORK_PHONE | VARCHAR (128) | The patient account's work phone number. |
| PAT_NAME | VARCHAR (254) | Contains the Patient's Name as stored in the MyChart (WPR) record. |
| MOBILE_TC_ACPT_DTTM | DATETIME (Local) | Stores the instant when the MyChart Terms and Conditions was last accepted by the user.  Prior to May 2020, this applied only to MyChart Mobile Terms and Conditions. Starting in May 2020, this applies to both MyChart Mobile and MyChart Web Terms and Conditions. |
| MOBILE_PRXYDIS_DTTM | DATETIME (Local) | Stores the instant when the MyChart Proxy Disclaimer was last accepted by the user.  Prior to May 2020, this applied only to MyChart Mobile Proxy Disclaimer. Starting in May 2020, this applies to both MyChart Mobile and MyChart Web Proxy Disclaimer. |
| DOB_DT | DATETIME | The patient's date of birth. |
| SEX_C | VARCHAR (66) |  |
| STATUS_CAT_C | INTEGER |  |
| PAT_SITE_ID | NUMERIC (18,0) | Site identifier where the patient logs in. |
| PROV_TEXT_ID | NUMERIC (18,0) | Patient's providers |
| FAIL_PWD_RST_TRY | INTEGER | The number of failed password reset attempts. |
| ALT_LAST_TERMS_TM | DATETIME (Local) | Alternate Website, instant user accepted terms and cond w/no display |
| UNMERGE_INST_DTTM | DATETIME (UTC) | If this record was unmerged from another record, the instant of unmerge is stored |
| UNMRGD_CPY_WPR_ID | VARCHAR (18) | A WPR record (MyChart account) merge occurs when two EPT records (patient records) are found to represent the same patient, and each EPT was associated with a different WPR. A merge occurs between a "source" and "target" WPR. The target survives the merge. The source is deleted from Chronicles. When a merge occurs, a copy is made of the source and target WPRs.   An unmerge occurs when it is determined that two WPRs were merged in error. In effect, the merged WPR is split back into two WPRs. It occurs when a "former source" is pulled from a "former target." When an unmerge occurs, two more copies are made. One copy is of the former target. The other is a copy of the copy of the source.  I WPR 90 is set to the WPR that was copied from.   The target WPR of a merge has these items set accordingly: - I WPR 470 has a line for the source WPR appended to it. - I WPR 480 has a line for the target WPR appended to it. - I WPR 700 is set to the copy of a source WPR. - I WPR 710 is set to the copy of the target WPR.  The former source resulting from an unmerge has this item set accordingly: - I WPR 760 is set to the former target before the unmerge. |
| UNMRGD_SRC_MPT_ID | VARCHAR (192) | points to the source MPT id for the unmerge |
| FAILED_ATTEMPTS | INTEGER | This item stores the number of times a correct MyChart activation code has been used with incorrect validation data. |
| BEDSIDE_LOCK_STS_C | INTEGER |  |
| BEDSD_TC_ACPT_DTTM | DATETIME (Local) | Stores the instant when the Bedside Terms and Conditions file was last accepted. |
| BEDSD_PRXYDIS_DTTM | DATETIME (Local) | Stores the instant when the Bedside Proxy Disclaimer was last accepted by the user. |
| BEDSIDE_UNLOCK_FAIL | INTEGER | Tracks the number of failed unlock / authentication attempts since the last successful attempt.  If this number is equal the the number of maximum allowed failed attempts, the user will be considered locked. |
| SEND_SMS_YN | VARCHAR (1) |  |
| BEDSD_TC_ACPT_DTTM_DTTM | No |  |
| BEDSD_PRXYDIS_DTTM_DTTM | No |  |
| EXT_RECORD_YN | VARCHAR (1) |  |
| TICKLER_REV_UTC_DTTM | DATETIME (UTC) | Instant of the last time notification settings have been reviewed via the notification settings alert or notification preferences page within MyChart. |
| NONPAT_INST_ACTV_CODE | VARCHAR (64) | This item stores the instant activation code for a non-patient. This is like the activation code but it's time-sensitive. |
| NONPAT_INST_ACTV_UTC_DTTM | DATETIME (UTC) | This item stores the timestamp of when the instant activation code was generated for a non-patient. This is how we ensure that the instant activation code is time-sensitive. |
| PREF_ID | NUMERIC (18,0) | The ID number of the communication preferences record for the MyChart user. |
| TWOFA_OPT_IN_C | INTEGER |  |
| LST_HTG_V_UTC_DTTM | DATETIME (UTC) | Stores the time users last viewed their Happy Together links and status |
| TWOFA_DONE_UTC_DTTM | DATETIME (UTC) | Contains the last successful completion of two-factor authentication for a given user. |
| PREM_BILL_PAPERLS_STAT_C | INTEGER |  |
| SECURE_EMAIL | VARCHAR (192) | The validated email address of the MyChart user. This email has been verified as reachable and belonging to the user. |
| SECURE_MOBILE | VARCHAR (128) | The validated SMS of the MyChart user. This SMS has been verified as reachable and belonging to the user. |
| SIGNATURE_METHOD_C | INTEGER |  |
| TEMP_ACTIVE_C | INTEGER |  |
| DISMISSED_RR_DIGEST_CARD_YN | VARCHAR (1) |  |
| HIDE_COVID_QCK_ACSS_YN *(deprecated)* | VARCHAR (1) |  |
| KNOWN_DEVICE_FAILED_LOGINS_CNT | INTEGER | Stores the number of failed login attempts across a user's known devices since a successful login. |
| REMEMBER_WEB_DEVICES_YN | VARCHAR (1) |  |
| EXT_ACCT_CREATION_SRC_C | INTEGER | Surrogate key used to uniquely identify rows in this (and only this) table on Cogito Cloud only, do not assume the surrogate key in this table will correspond to the surrogate key in another table |
| SSN | VARCHAR (192) | Non-patient user's social security number. |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| B-TREE INDEX | EIX_MYC_PATIENT_LALOTI | LAST_LOGIN_TIME | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_MYC_PATIENT_MYEXDA | MYCHART_EXP_DATE | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_MYC_PATIENT_PAID | PAT_ID | 1 | Yes | Yes |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | MYPT_ID | MYC_ACCT_DELETION | MYPT_ID | No | No | No |  |
| 1 | MYPT_ID | MYC_MRG_AUD_TRL | MYPT_ID | No | No | No |  |
| 1 | MYPT_ID | MYC_PATIENT_2 | MYPT_ID | No | No | No |  |
| 1 | MYPT_ID | V_MYC_TEST_PAT | MYPT_ID | Unknown | Unknown | No |  |
| 2 | PAT_ID | ANTICOAG_SELF_REGULATING | PAT_ID | No | No | No |  |
| 2 | PAT_ID | CARE_COORDINATION | PAT_ID | Unknown | No | No |  |
| 2 | PAT_ID | CLAIMS_DERIVE_PAT_FLAGS | PAT_ID | No | No | No |  |
| 2 | PAT_ID | COMMUNITY_RESRC_REVIEWED | PAT_ID | No | No | No |  |
| 2 | PAT_ID | D_PAT_GEOGRAPHIC_CLASS | PAT_ID | Unknown | Unknown | No |  |
| 2 | PAT_ID | EPT_MEM_INFO | PAT_ID | No | No | No |  |
| 2 | PAT_ID | EXT_DATA_LAST_DONE | PAT_ID | No | No | No |  |
| 2 | PAT_ID | F_IBD_ADULT_FORM_PAT | PAT_ID | Unknown | Unknown | No |  |
| 2 | PAT_ID | HH_PAT_INFO | PAT_ID | Unknown | No | No |  |
| 2 | PAT_ID | HM_STATUS_UPD | PAT_ID | No | No | No |  |
| 2 | PAT_ID | IMMNZTN_LAST_REVIEW | PAT_ID | No | No | No |  |
| 2 | PAT_ID | PATIENT | PAT_ID | No | No | No |  |
| 2 | PAT_ID | PATIENT_2 | PAT_ID | No | No | No |  |
| 2 | PAT_ID | PATIENT_3 | PAT_ID | No | No | No |  |
| 2 | PAT_ID | PATIENT_4 | PAT_ID | No | No | No |  |
| 2 | PAT_ID | PATIENT_5 | PAT_ID | No | No | No |  |
| 2 | PAT_ID | PATIENT_6 | PAT_ID | No | No | No |  |
| 2 | PAT_ID | PATIENT_CONF_ADDR | PAT_ID | No | No | No |  |
| 2 | PAT_ID | PATIENT_MISC_COMMENTS | PAT_ID | No | No | No |  |
| 2 | PAT_ID | PATIENT_MYC | PAT_ID | Unknown | No | No |  |
| 2 | PAT_ID | PATIENT_OPT | PAT_ID | No | No | No |  |
| 2 | PAT_ID | PAT_ENC_LAST_HX_CT | PAT_ID | Unknown | Unknown | No |  |
| 2 | PAT_ID | PAT_RES_CODE | PAT_ID | No | No | No |  |
| 2 | PAT_ID | PROB_LIST_REVIEWED | PAT_ID | No | No | No |  |
| 2 | PAT_ID | REGADDL_PAT | PAT_ID | No | No | No |  |
| 2 | PAT_ID | SCF_FHIR_MAP | PAT_ID | No | No | No |  |

_(75 total; showing first 30)_
