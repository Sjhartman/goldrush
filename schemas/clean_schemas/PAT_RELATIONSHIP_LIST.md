# PAT_RELATIONSHIP_LIST

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=PAT_RELATIONSHIP_LIST

## Description

This table includes the majority of patient contact demographic info, general relationship info, and patient-level relationship info. The records included in this table are Patient Relationships (RLA) records.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | RLA |
| Release Version | Rel 2018 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| PAT_RELATIONSHIP_ID | NUMERIC (18,0) | The unique identifier for the patient contact record. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| RECORD_STATUS_C | INTEGER |  |
| PAT_ID | VARCHAR (18) | The unique ID of the patient this patient contact is added to. |
| PAT_CONTACT_PAT_ID | VARCHAR (18) | EPT ID of the patient contact involved in the relationship. |
| PAT_LEVEL_RELATIONSHIP_YN | VARCHAR (1) |  |
| SSN | VARCHAR (192) | Patient contact's national identifier. |
| NAME | VARCHAR (254) | Patient contact's name.  This column only displays names that are stored directly on patient contact records and will be blank for patient contact records that are linked to different patient records.  Use the PAT_RELATIONSHIP_RECORD_NAME column instead if you want a single column that will display the names of both linked and unlinked patient contact records. |
| GENDER_C | INTEGER |  |
| BIRTH_DATE | DATETIME | Patient contact's date of birth. |
| HOUSE_NUM | VARCHAR (254) | Patient contact's house number. |
| CITY | VARCHAR (254) | Patient contact's city of residence. |
| STATE_C | VARCHAR (66) |  |
| ZIP_CODE | VARCHAR (254) | Patient contact's postal code. |
| DISTRICT_C | INTEGER |  |
| COUNTY_C | VARCHAR (66) |  |
| COUNTRY_C | VARCHAR (66) |  |
| OCCUPATION | VARCHAR (254) | Patient contact's occupation. |
| INTERP_NEEDED_YN | VARCHAR (1) |  |
| HEARING_IMPAIRED_YN | VARCHAR (1) |  |
| VISUALLY_IMPAIRED_YN | VARCHAR (1) |  |
| SPEC_NEED_IMPAIR_C | INTEGER |  |
| RECORD_CREATION_DATE | DATETIME | The date when the patient contact was created. |
| PREFERRED_LANGUAGE_C | VARCHAR (66) |  |
| DISPLAY_SEQUENCE | INTEGER | Stores the order in which patient-level contacts display. |
| SOCIAL_CLOSENESS_C | INTEGER |  |
| SAME_HOUSEHOLD_YN | VARCHAR (1) |  |
| SUPPORT_NETWORK_YN | VARCHAR (1) |  |
| CUSTODY_C | INTEGER |  |
| GUARDIAN_YN | VARCHAR (1) |  |
| PROTECTION_ORDER_YN | VARCHAR (1) |  |
| LAST_REV_DTTM | DATETIME (Attached) | Indicates the last instant that this record's relationship information was reviewed or updated from a patient-level encounter. |
| LAST_REV_USER_ID | VARCHAR (18) | The unique ID of the user who most recently reviewed or updated this patient contact's information from a patient-level encounter. |
| NOTIFY_ON_ADMSN_YN | VARCHAR (1) |  |
| LEGAL_RELATION_C | INTEGER |  |
| ACTV_HLTHCR_AGENT_YN | VARCHAR (1) |  |
| GENERIC_CAT_1_C | VARCHAR (66) |  |
| GENERIC_CAT_2_C | VARCHAR (66) |  |
| GENERIC_CAT_3_C | VARCHAR (66) |  |
| GENERIC_CAT_4_C | VARCHAR (66) |  |
| GENERIC_STRING_1 | VARCHAR (254) | Customer-labeled string item. |
| GENERIC_STRING_2 | VARCHAR (254) | Customer-labeled string item. |
| GENERIC_STRING_3 | VARCHAR (254) | Customer-labeled string item. |
| GENERIC_STRING_4 | VARCHAR (254) | Customer-labeled string item. |
| AUTH_LETTER_RECIPIENT_YN | VARCHAR (1) |  |
| SEND_LETTERS_BY_DEFAULT_YN | VARCHAR (1) |  |
| COMPETENCY_CODE_C *(deprecated)* | INTEGER |  |
| LIMITATION_CODE_C | INTEGER |  |
| RESPONSIBILITY_CODE_C | INTEGER |  |
| AUTHORITY_CODE_C | INTEGER |  |
| BUSINESS_IDENT | VARCHAR (254) | The unique ID of the business for a supervisory patient contact. |
| ORDER_ISSUED_YN *(deprecated)* | VARCHAR (1) |  |
| PENDING_PAT_LEGAL_RELATION_C | INTEGER |  |
| ACP_UPD_REJECTION_REASON_C | INTEGER |  |
| ACP_UPD_REJECTION_REASON_TEXT | VARCHAR (254) | The patient-facing rejection reason for an update to the advance care plan (ACP). |
| ACP_UPD_MYCHART_USER_ID | VARCHAR (18) | The unique ID of the MyChart user who updated the advance care plan (ACP). |
| IMPACT_OF_RELATIONSHIP_C | INTEGER |  |
| PAT_RELATIONSHIP_RECORD_NAME | VARCHAR (200) | The name of the patient contact record. If the patient contact record is linked to a different patient's record, the name will come from the patient record. Otherwise, it will come from the name stored directly on the patient contact record.  If your organization does not allow users to link patient contacts to other patient records, this column will act the same as the NAME column in this table. |
| ORDER_ISSUED_TASK_C | INTEGER |  |
| SG_NRICFIN_TYPE_C | INTEGER |  |
| SG_OTHER_IDENT | VARCHAR (192) | Separate form of identification from national identifier, used in Singapore environments. |
| SG_OTHER_ID_TYPE_C | INTEGER |  |
| CREATION_SOURCE_C | INTEGER |  |
| LIVING_STATUS_C | VARCHAR (66) |  |
| PAT_CONTACT_ROW_TYPE_C | INTEGER |  |
| ORG_FACILITY_ID | NUMERIC (18,0) | The unique ID of the facility linked to a patient contact. |
| ORG_RELIG_AFFL_ID | VARCHAR (18) | The unique ID of the religious affiliation linked to an organization patient contact. |
| ORG_WEBSITE | VARCHAR (250) | A website URL for the organization patient contact. |
| ORG_FAX_NUMBER | VARCHAR (250) | The fax number for an organization patient contact. |
| ORG_PRIMARY_CONTACT | VARCHAR (250) | The representative or point person for an organization contact. |
| ORG_PRIMARY_CONTACT_PHONE | VARCHAR (250) | The phone number for the organization primary contact. |
| ORG_DEPARTMENT_ID | NUMERIC (18,0) | The unique ID of the department linked to a patient contact. |
| MYPT_ID | VARCHAR (18) | The unique id of the MyChart account associated with the patient contact, primarily for the purpose of granting the contact proxy access to the patient. |
| FREETEXT_COMMENT | VARCHAR (256) | A free text comment on the contact |
| UUID | VARCHAR (100) | The universally unique identifier (UUID) for the patient contact |
| FINLAND_GUARD_DIR_C | INTEGER |  |
| FINLAND_LEGAL_RES_YN | VARCHAR (1) |  |
| FINLAND_RES_START_DATE | DATETIME | The date on which a dependent began to reside with a guardian, according to VRK. |
| FINLAND_RES_END_DATE | DATETIME | The date on which a dependent ceased to reside with a guardian, according to VRK. |
| FINLAND_COURT_ORDER_C | INTEGER |  |
| PRIMARY_OR_FIRST_PHONE | VARCHAR (254) | The phone number of a patient contact. This is the primary phone number if one is marked primary, otherwise this is the first phone number listed for the patient contact. If the patient contact is linked to another record, this phone number is from the linked record, otherwise this phone number is from the patient contact record. |
| EMERG_CONTACT_YN | VARCHAR (1) |  |
| FINLAND_GUARDIANSHIP_FREE_TEXT | VARCHAR (5000) | This column contains additional free text guardianship information about patient contact records received from the DVV (population register). |
| COMM_ACSS_C | INTEGER |  |
| SHOW_VIDEO_INVITE_YN | VARCHAR (1) | Surrogate key used to uniquely identify rows in this (and only this) table on Cogito Cloud only, do not assume the surrogate key in this table will correspond to the surrogate key in another table |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 2 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 2 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 3 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 4 | RECORD_STATUS_C | ZC_RECORD_STATUS_2 | RECORD_STATUS_2_C | No | No | No |  |
| 4 | RECORD_STATUS_C | ZC_RECORD_STS | RECORD_STS_C | No | No | No |  |
| 5 | PAT_ID | ANTICOAG_SELF_REGULATING | PAT_ID | No | No | No |  |
| 5 | PAT_ID | CARE_COORDINATION | PAT_ID | Unknown | No | No |  |
| 5 | PAT_ID | CLAIMS_DERIVE_PAT_FLAGS | PAT_ID | No | No | No |  |
| 5 | PAT_ID | COMMUNITY_RESRC_REVIEWED | PAT_ID | No | No | No |  |
| 5 | PAT_ID | D_PAT_GEOGRAPHIC_CLASS | PAT_ID | Unknown | Unknown | No |  |
| 5 | PAT_ID | EPT_MEM_INFO | PAT_ID | No | No | No |  |
| 5 | PAT_ID | EXT_DATA_LAST_DONE | PAT_ID | No | No | No |  |
| 5 | PAT_ID | F_IBD_ADULT_FORM_PAT | PAT_ID | Unknown | Unknown | No |  |
| 5 | PAT_ID | HH_PAT_INFO | PAT_ID | Unknown | No | No |  |
| 5 | PAT_ID | HM_STATUS_UPD | PAT_ID | No | No | No |  |
| 5 | PAT_ID | IMMNZTN_LAST_REVIEW | PAT_ID | No | No | No |  |
| 5 | PAT_ID | PATIENT | PAT_ID | No | No | No |  |
| 5 | PAT_ID | PATIENT_2 | PAT_ID | No | No | No |  |
| 5 | PAT_ID | PATIENT_3 | PAT_ID | No | No | No |  |
| 5 | PAT_ID | PATIENT_4 | PAT_ID | No | No | No |  |
| 5 | PAT_ID | PATIENT_5 | PAT_ID | No | No | No |  |
| 5 | PAT_ID | PATIENT_6 | PAT_ID | No | No | No |  |
| 5 | PAT_ID | PATIENT_CONF_ADDR | PAT_ID | No | No | No |  |
| 5 | PAT_ID | PATIENT_MISC_COMMENTS | PAT_ID | No | No | No |  |
| 5 | PAT_ID | PATIENT_MYC | PAT_ID | Unknown | No | No |  |
| 5 | PAT_ID | PATIENT_OPT | PAT_ID | No | No | No |  |
| 5 | PAT_ID | PAT_ENC_LAST_HX_CT | PAT_ID | Unknown | Unknown | No |  |

_(185 total; showing first 30)_
