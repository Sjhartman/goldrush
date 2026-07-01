# CARE_TEAM_EDIT_HX

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=CARE_TEAM_EDIT_HX

## Description

This table holds information about how the patient care team was edited. A patient care team is a group of providers affiliated with a patient record; these providers are either directly or indirectly concerned with the patient's care.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | EPT |
| Release Version | Summer 2009 |
| May contain EHI? | No |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| PAT_ID | VARCHAR (18) | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| LINE | No | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| CHANGE_DATETIME | DATETIME (Local) | The instant the change was made to this patient's care team. |
| CHANGE_USER_ID | VARCHAR (18) | The unique ID of the user that made the change to this patient's care team. This column is frequently used to link to the CLARITY_EMP table. |
| CHANGE_TYPE_C | INTEGER |  |
| PROV_ID | VARCHAR (18) | The unique ID associated with the provider record for this row. This column is frequently used to link to the CLARITY_SER table. |
| SPECIALTY_NEW_C | VARCHAR (66) |  |
| CHANGE_REQ_BY_NEW_C | INTEGER |  |
| PCP_TYPE_C | INTEGER |  |
| EFF_NEW_DT | DATETIME | The new value (at the instant of the change) of Item EPT 80104, "Effective Date." |
| TERMINATION_NEW_DT | DATETIME | The new value (at the instant of the change) of Item EPT 80105, "Termination Date." |
| SWITCH_REASON_NEW_C | INTEGER |  |
| COMMENTS_NEW | VARCHAR (4000) | The new value (at the instant of the change) of Item EPT 80108, "Comments." Although Hyperspace will allow users to enter up to 4681 characters in this field for the sake of backwards compatibility, entries will be truncated at 4000 characters in Clarity. |
| SER_ADDRESS_NEW_ID | VARCHAR (508) | The new value (at the instant of the change) of Item EPT 80110, "Provider Address ID." |
| RESULTS_NEW_C | INTEGER |  |
| ED_NOTIF_NEW_YN | VARCHAR (1) |  |
| PCP_MESSAGE_NEW_YN | VARCHAR (1) |  |
| RELATIONSHIP_NEW_C | VARCHAR (66) |  |
| LINE_NUM | NUMERIC (18,0) | The line number identifying the patient care team entry that was adjusted. |

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

_(76 total; showing first 30)_
