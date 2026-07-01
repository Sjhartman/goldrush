# PAT_PCP

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=PAT_PCP

## Description

This table contains the Primary Care Provider (PCP) information for your patients over time. It can also contain data about providers that are not PCPs but are still on the patients' EpicCare-Ambulatory care teams.

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
| LINE | No | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| CHANGE_DATE *(deprecated)* | DATETIME | This column is deprecated. This information is now extracted to the CHANGE_DATETIME column in the CARE_TEAM_EDIT_HX table. |
| PCP_PROV_ID | VARCHAR (18) | The unique ID associated with the provider record for this row. This column is frequently used to link to the CLARITY_SER table. |
| EFF_DATE | DATETIME | The date from which the provider is in effect as the member?s PCP. |
| TERM_DATE | DATETIME | The last date for which the provider was the member?s PCP. |
| USER_ID *(deprecated)* | VARCHAR (18) | This column is deprecated. This information is now extracted to the CHANGE_USER_ID column in the CARE_TEAM_EDIT_HX table. |
| CHANGE_REQ_BY_C *(deprecated)* | INTEGER |  |
| SWITCH_REASON_C *(deprecated)* | INTEGER |  |
| PCP_TYPE_C | INTEGER |  |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this Chronicles record. This is populated only if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this Chronicles record was extracted. This is populated only if you use IntraConnect. |
| DELETED_YN | VARCHAR (1) |  |
| SPECIALTY_C | VARCHAR (66) |  |
| RESULTS_C | INTEGER |  |
| ADMIT_NOTIFY_YN | VARCHAR (1) |  |
| PCP_MESSAGE_YN | VARCHAR (1) |  |
| RELATIONSHIP_C | VARCHAR (66) |  |
| OTHER_NAME | VARCHAR (254) | The name for patient care team members that don't have a provider and resource record. |
| OTHER_ADDRESS | VARCHAR (4000) | The address for patient care team members that don't have a provider and resource record.  Lines are delimited with character 9s. |
| OTHER_PHONE | VARCHAR (508) | The phone number for patient care team members that don't have a provider and resource record. |
| OTHER_PAGER | VARCHAR (508) | The pager number for patient care team members that don't have a provider and resource record. |
| OTHER_FAX | VARCHAR (508) | The fax number for patient care team members that don't have a provider and resource record. |
| OTHER_EMAIL | VARCHAR (508) | The email address for patient care team members that don't have a provider and resource record. |
| PCP_HX_COMMENTS | VARCHAR (4000) | Free text comments that can be entered for a provider that is part of the care team for this patient. |
| PCP_ADDRESS_ID | VARCHAR (508) | The unique ID of the address in the provider record that should be used to contact the patient's PCP. This column is frequently used in conjunction with the PCP_PROV_ID column to link to the CLARITY_SER_ADDR table. |

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

_(59 total; showing first 30)_
