# HSP_TRTMT_TEAM

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=HSP_TRTMT_TEAM

## Description

The HSP_TRTMT_TEAM table contains information on inpatient treatment teams. Each record in this table is based on PAT_ENC_CSN_ID.

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
| PAT_ID | VARCHAR (18) | The ID of the patient with this treatment team member. |
| PAT_ENC_DATE_REAL | No | This is a numeric representation of the date of this contact in your system. The integer portion of the number specifies the date of the contact. The digits after the decimal point indicate multiple contacts on one day. |
| LINE | No | The line number of the treatment team member for the patient. |
| PROV_ID | VARCHAR (18) | The unique ID of the provider who is the treatment team member for the patient. |
| TRTMNT_TEAM_REL_C | VARCHAR (66) |  |
| TRTMNT_TM_BEGIN_DT | 18872 | The date and time the treatment team member started for the patient. |
| TRTMNT_TM_END_DT | 18873 | The date and time the treatment team member ended for the patient. |
| TRTMNT_TM_ED_YN | VARCHAR (1) |  |
| CM_CT_OWNER_ID | VARCHAR (25) | ID of the deployment owner for this contact. |
| PAT_ENC_CSN_ID | NUMERIC (18,0) | A unique serial number for this encounter. This number is unique across all patients and encounters in the system. |
| TEAM_ADD_YN | VARCHAR (1) | Surrogate key used to uniquely identify rows in this (and only this) table on Cogito Cloud only, do not assume the surrogate key in this table will correspond to the surrogate key in another table |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| B-TREE INDEX | EIX_HSP_TRTMT_TEAMENC | PAT_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_HSP_TRTMT_TEAMENC | PAT_ENC_DATE_REAL | 2 | Yes | Yes |  |

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

_(168 total; showing first 30)_
