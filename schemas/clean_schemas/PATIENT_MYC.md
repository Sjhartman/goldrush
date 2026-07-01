# PATIENT_MYC

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=PATIENT_MYC

## Description

This table contains web-based chart system-related data items that are stored in the Patient (EPT) master file. These items generally relate to web-based chart system account activation and account status, and also include the last verification date for different types of patient information that can be verified through the web-based chart system.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | EPT |
| Release Version | EPIC 2002 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| PAT_ID | VARCHAR (18) | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| PAT_ACCESS_CODE | VARCHAR (40) | The patient's current web-based chart system access code. This value is checked when a patient attempts to log in to the web-based chart system for the first time. |
| PAT_ACCESS_CODE_TM | DATETIME (UTC) | This is a timestamp indicating when the access code in field PAT_ACCESS_CODE was created. |
| PAT_ACCESS_STAT_C | INTEGER |  |
| MYCHART_STATUS_C | INTEGER |  |
| RECV_EMAIL_YN *(deprecated)* | VARCHAR (1) |  |
| ACCESSCODE_STAT_C | INTEGER |  |
| DEACT_ACCT_YN | VARCHAR (1) |  |
| CODE_FOR_PROXY_YN | VARCHAR (1) |  |
| MYCHART_EXP_DATE | DATETIME | The expiration date (if one has been set) of the web-based chart system account. When this date is reached, the web-based chart system user is no longer allowed to login to the system. |
| MYPT_ID | VARCHAR (18) | The unique ID of the web-based chart system patient account. |
| LAST_MERGE_FROM | VARCHAR (12) | If this patient record is the destination of a previous merging, and the source record has web-based chart system activity, then this item stores the time instant of the merging. |
| ALT_WEBSTE_STAT_C | INTEGER |  |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| MYC_PAT_TYPE_C | INTEGER |  |
| DEM_VERIF_DT | DATETIME | Date of last demographics verification by patient or his/her proxy from MyChart. |
| INS_VERIF_DT | DATETIME | Date of last insurance verification by patient or his/her proxy from MyChart |
| FAILED_ATTEMPTS | INTEGER | This item stores the number of times a correct MyChart activation code has been used with incorrect validation data. |
| R_E_L_PAT_VERIF_DT | DATETIME | The date when race, ethnicity, and language information was last verified by the patient online using the patient portal. |
| MYC_DEFER_DTTM | DATETIME (UTC) | Stores the date and time in UTC that a user last chose to defer the MyChart Signup question.  This is used when users click Ask Later on the MyChart Signup window. |
| MEDS_PAT_VERIF_DT | DATETIME | The date that the patient last used MyChart or Welcome to verify and/or update their medications. |
| ALRGY_PAT_VERIF_DT | DATETIME | The date that the patient last used MyChart or Welcome to verify and/or update their allergies. |
| PROB_PAT_VERIF_DT | DATETIME | The date that the patient last used MyChart or Welcome to verify and/or update their problems. |
| PCP_PAT_VERIF_DT | DATETIME | The date that patients last used Welcome to verify and/or update their primary care provider. |
| HCA_PAT_VERIF_DT | DATETIME | The date that the patient last used MyChart or Welcome to verify and/or update their health care agents. |
| INST_ACTV_CODE | VARCHAR (64) | This item stores the instant activation code. This is like the activation code but it's time-sensitive. |
| INST_ACTV_UTC_DTTM | DATETIME (UTC) | This item stores the timestamp of when the instant activation code was generated. This is how we ensure that the instant activation code is time-sensitive. |
| NOTIF_TM_ZNE_C | INTEGER |  |
| PAT_MYC3_ENR_STAT_C | INTEGER |  |
| LAST_LABS_VIEW_DTTM | DATETIME (Local) | The last time when the patient or proxies viewed patient's result list (including IP results) in MyChart. |
| LAST_QNR_SCORE_UTC_DTTM | DATETIME (UTC) | Stores the instant when the patient last generated a questionnaire score that is viewable in MyChart. |
| PAT_MYC_LAST_QNR_RESP_UTC_DTTM | DATETIME (UTC) | Stores the last instant when the patient submitted a response for a patient-entered questionnaire containing a patient-entered question that can be viewed over-time in MyChart. |
| PREF_PHR_VERIF_INST_UTC_DTTM | DATETIME (UTC) | The last instant that a patient's preferred pharmacies were updated or verified. |
| PREF_PHR_VERIF_AUDIT_CONTEXT_C | INTEGER |  |
| PREF_PHR_VERIF_USER_ID | VARCHAR (18) | The user that last updated or verified the patient's preferred pharmacies. |
| PREF_PHR_VERIF_MYPT_ID | VARCHAR (18) | The MyChart user that last updated or verified the patient's preferred pharmacies. |
| DEFAULT_PREF_NAME_YN | VARCHAR (1) |  |

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

_(71 total; showing first 30)_
