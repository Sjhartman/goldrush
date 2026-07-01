# ALERT

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=ALERT

## Description

The ALERT table contains one record for every alert that was created in Hyperspace. Each record is based on the alert ID and contains key information about the alert such as the patient, patient CSN, alert type, and whether it was seen by a user.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | ALT |
| Release Version | SUMMER 2005 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| ALT_ID | NUMERIC (18,0) | The unique identifier for the alert. |
| CM_PHY_OWNER_ID | VARCHAR (25) | ID of the physical deployment owner for this record.  Physical owners will be where the data is hosted, either on the cross-over server or the owner deployment. |
| CM_LOG_OWNER_ID | VARCHAR (25) | ID of the logical deployment owner for this record.  Logical owners show the deployment where the record was created but doesn't represent if the record is a part of version skew. |
| ALERT_DESC | VARCHAR (254) | A brief description of the alert. |
| MED_ALERT_TYPE_C | INTEGER |  |
| PAT_ID | VARCHAR (18) | The unique patient ID of the patient for whom the alert fired.  You could link it to PATIENT.PAT_ID to get patient specific information. |
| PAT_CSN | NUMERIC (18,0) | The contact serial number for the patient encounter in which the alert was fired. This number is unique across all patients and encounters in your system.  If alerts are triggered in a patient-specific encounter, they are saved in a corresponding encounter. This can be used to join to PAT_ENC.PAT_ENC_CSN_ID to get the encounter information. |
| MED_VENDOR_C | INTEGER |  |
| BPA_LOCATOR_ID | NUMERIC (18,0) | This column contains the information on which locators were triggered that caused the Best Practice Alert to fire. |
| GENERAL_ALT_TYPE_C | INTEGER |  |
| IMMUN_ID | NUMERIC (18,0) | This column contains the information about which immunization caused the immunization?allergy alert to fire. |
| MAR_DUPLICATE_YN | VARCHAR (1) |  |
| UPDATE_DATE | No | The date and time this row was last updated (the last time the table was extracted or this column was backfilled). |
| REC_ARCHIVED_YN | No | Indicates whether the Alert record is archived at the record level. |
| PUMP_ID | VARCHAR (40) | The unique external device ID of the pump selected in response to the warning after trying to program the pump. |
| MAR_ACTION_C | VARCHAR (66) |  |
| MED_ALERT_SUBTYPE_C | INTEGER |  |
| NBA_LOCATOR_ID | NUMERIC (18,0) | The ID of the action record correlated with this next best action event. |
| NBA_PAT_ID | VARCHAR (18) | The patient correlated with this next best action event. |
| NBA_PROV_ID | VARCHAR (18) | The provider correlated with this next best action event. |
| NBA_GUARANTOR_ACCT_ID | NUMERIC (18,0) | The guarantor account correlated with this next best action event. |
| NBA_PROSPECT_RECORD_ID | NUMERIC (18,0) | The prospective patient correlated with this next best action event. |
| NBA_SUBMITTER_RECORD_ID | NUMERIC (18,0) | The submitter correlated with this next best action event. |
| BLOOD_ALERT_BUCKET_C | INTEGER |  |
| RECORD_STATUS_C | INTEGER |  |
| EXPECTED_WKFL_ACTVTIES_C | INTEGER |  |
| ORD_VALID_LPP_ID | NUMERIC (18,0) | The order validation extension that triggered on the patient |
| BPA_IS_PAT_FACING_YN | VARCHAR (1) |  |
| MED_ADVISORY_RECORD_ID | NUMERIC (18,0) | Contains the Anesthesia Intraprocedure medication advisory configuration that generated this alert. |
| MED_ADVISORY_TYPE_C | INTEGER |  |
| HM_TOPIC_ID | NUMERIC (18,0) | This column contains the ID of the Health Maintenance topic correlated with this alert record. |
| PROTOCOL_ID | NUMERIC (18,0) | The unique ID of the protocol the feedback in this alert record is about. |
| ORDER_GROUP_ID | NUMERIC (18,0) | The unique ID of the order group the feedback in this alert record is about. |
| MED_ADVISORY_USER_FEEDBACK_C | INTEGER |  |
| MED_ADVISORY_USER_COMMENT | VARCHAR (500) | This column contains the free text comment left by the user after they documented discrete feedback. |
| SVV_LEAF_LPP_ID | NUMERIC (18,0) | Stores the Extension ID of the record that generated the Sign Visit Validation message, if the message came from an extension. |
| SVV_PROFILE_LPP_ID | NUMERIC (18,0) | Stores the Extension ID listed in the user's profile that resulted in this Sign Visit Validation message. This is only saved if it is different than the value in item 41000. |
| SVV_RULE_ID | VARCHAR (18) | Stores the Rule (CER) ID if this Sign Visit Validation is based on a rule record. |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| B-TREE INDEX | EIX_ALERT_GENALTTYPE | GENERAL_ALT_TYPE_C | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_ALERT_MEDALTTYPE | MED_ALERT_TYPE_C | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_ALERT_PATID | PAT_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_ALERT_PATID | PAT_CSN | 2 | Yes | Yes |  |
| B-TREE INDEX | EIX_ALERT_UPDATE_DATE | UPDATE_DATE | 1 | Yes | Yes |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | Yes | No |  |
| 2 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | Yes | No |  |
| 2 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | Yes | No |  |
| 3 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | Yes | No |  |
| 3 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | Yes | No |  |
| 3 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | Yes | No |  |
| 5 | MED_ALERT_TYPE_C | ZC_MED_ALERT_TYPE | MED_ALERT_TYPE_C | No | Yes | No |  |
| 6 | PAT_ID | ANTICOAG_SELF_REGULATING | PAT_ID | No | Yes | No |  |
| 6 | PAT_ID | CARE_COORDINATION | PAT_ID | Unknown | Yes | No |  |
| 6 | PAT_ID | CLAIMS_DERIVE_PAT_FLAGS | PAT_ID | No | Yes | No |  |
| 6 | PAT_ID | COMMUNITY_RESRC_REVIEWED | PAT_ID | No | Yes | No |  |
| 6 | PAT_ID | D_PAT_GEOGRAPHIC_CLASS | PAT_ID | Unknown | Unknown | No |  |
| 6 | PAT_ID | EPT_MEM_INFO | PAT_ID | No | Yes | No |  |
| 6 | PAT_ID | EXT_DATA_LAST_DONE | PAT_ID | No | Yes | No |  |
| 6 | PAT_ID | F_IBD_ADULT_FORM_PAT | PAT_ID | Unknown | Unknown | No |  |
| 6 | PAT_ID | HH_PAT_INFO | PAT_ID | Unknown | Yes | No |  |
| 6 | PAT_ID | HM_STATUS_UPD | PAT_ID | No | Yes | No |  |
| 6 | PAT_ID | IMMNZTN_LAST_REVIEW | PAT_ID | No | Yes | No |  |
| 6 | PAT_ID | PATIENT | PAT_ID | No | Yes | No |  |
| 6 | PAT_ID | PATIENT_2 | PAT_ID | No | Yes | No |  |
| 6 | PAT_ID | PATIENT_3 | PAT_ID | No | Yes | No |  |
| 6 | PAT_ID | PATIENT_4 | PAT_ID | No | Yes | No |  |
| 6 | PAT_ID | PATIENT_5 | PAT_ID | No | Yes | No |  |
| 6 | PAT_ID | PATIENT_6 | PAT_ID | No | Yes | No |  |
| 6 | PAT_ID | PATIENT_CONF_ADDR | PAT_ID | No | Yes | No |  |
| 6 | PAT_ID | PATIENT_MISC_COMMENTS | PAT_ID | No | Yes | No |  |
| 6 | PAT_ID | PATIENT_MYC | PAT_ID | Unknown | Yes | No |  |
| 6 | PAT_ID | PATIENT_OPT | PAT_ID | No | Yes | No |  |
| 6 | PAT_ID | PAT_ENC_LAST_HX_CT | PAT_ID | Unknown | Unknown | No |  |
| 6 | PAT_ID | PAT_RES_CODE | PAT_ID | No | Yes | No |  |

_(251 total; showing first 30)_
