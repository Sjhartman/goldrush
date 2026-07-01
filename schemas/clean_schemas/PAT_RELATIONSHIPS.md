# PAT_RELATIONSHIPS

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=PAT_RELATIONSHIPS

## Description

Demographic information for patient contacts.

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
| LINE | No | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| CM_PHY_OWNER_ID | VARCHAR (25) | This is the Community ID (CID) of the physical deployment owner for this record.  Physical owners will be where the data is hosted, either on the cross-over server or the owner deployment. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | This is the Community ID (CID) of the logical deployment owner for this record.  Logical owners show the deployment where the record was created but doesn't represent if the record is a part of version skew. This is only populated if you use IntraConnect. |
| PAT_REL_NAME | VARCHAR (254) | The name of the patient's contact. |
| PAT_REL_ADDRESS *(deprecated)* | VARCHAR (254) |  |
| PAT_REL_CITY | VARCHAR (254) | Contact's city of residence |
| PAT_REL_STATE_C | VARCHAR (66) |  |
| PAT_REL_ZIP | VARCHAR (254) | The ZIP code of the patient's contact. |
| PAT_REL_COUNTY_C | VARCHAR (66) |  |
| PAT_REL_COUNTRY_C | VARCHAR (66) |  |
| PAT_REL_HOME_PHONE | VARCHAR (254) | Contact's home phone |
| PAT_REL_WORK_PHONE | VARCHAR (254) | Contact's work phone |
| PAT_REL_MOBILE_PHNE | VARCHAR (254) | Contact's mobile phone |
| PAT_REL_LGL_GUAR_YN | VARCHAR (1) |  |
| PAT_REL_REC_LINK_ID | VARCHAR (18) | Links this contact to a patient record |
| PAT_REL_RELATION_C | VARCHAR (66) |  |
| PAT_REL_PRIM_PH_C | VARCHAR (66) |  |
| PAT_REL_GEN_STR_1 | VARCHAR (254) | Customer labeled string item |
| PAT_REL_GEN_STR_2 | VARCHAR (254) | Customer labeled string item |
| PAT_REL_GEN_STR_3 | VARCHAR (254) | Customer labeled string item |
| PAT_REL_GEN_STR_4 | VARCHAR (254) | Customer labeled string item |
| PAT_REL_GEN_CAT_1_C | VARCHAR (66) |  |
| PAT_REL_GEN_CAT_2_C | VARCHAR (66) |  |
| PAT_REL_GEN_CAT_3_C | VARCHAR (66) |  |
| PAT_REL_GEN_CAT_4_C | VARCHAR (66) |  |
| PAT_REL_HOUSE_NUM | VARCHAR (254) | Contact's House Number |
| PAT_REL_DISTRICT_C | INTEGER |  |
| PAT_REL_HEARING_YN | VARCHAR (1) |  |
| PAT_REL_VISUALLY_YN | VARCHAR (1) |  |
| PAT_REL_IMP_NEEDS_C | INTEGER |  |
| PAT_REL_SPOKEN_C | VARCHAR (66) |  |
| PAT_REL_WRITTEN_C | VARCHAR (66) |  |
| PAT_REL_PREF_LANG_C | VARCHAR (66) |  |
| PAT_REL_INTERPRET_YN | VARCHAR (1) |  |
| PAT_REL_SPL_NEEDS_C | INTEGER |  |
| PAT_REL_NOTIFY_YN | VARCHAR (1) |  |
| PAT_REL_INTERPRE_YN | No |  |
| PAT_LEGAL_REL_C | INTEGER |  |
| PAT_REL_ACT_AGNT_YN | VARCHAR (1) |  |
| PAT_REL_UUID | VARCHAR (100) | Stores the unique id of the emergency contact |
| PAT_REL_EMAIL | VARCHAR (254) | Primary email address of the patient's emergency contact. |
| PAT_REL_RLA_ID | NUMERIC (18,0) | Links this patient contact to the associated Patient Relationships (RLA) patient relationship record. |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| BITMAP INDEX | EIX_PAT_RELATIONSHIPS_OWNER1 | CM_PHY_OWNER_ID | 1 | No | Yes |  |
| BITMAP INDEX | EIX_PAT_RELATIONSHIPS_OWNER2 | CM_LOG_OWNER_ID | 1 | No | Yes |  |

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

_(102 total; showing first 30)_
