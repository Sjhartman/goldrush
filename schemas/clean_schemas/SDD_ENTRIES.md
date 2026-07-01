# SDD_ENTRIES

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=SDD_ENTRIES

## Description

This table stores basic info about Social Driver entries. Each row represents one documentation of a need or risk for the patient in a given domain. This data includes the score that defines the severity of this need or risk.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | SDD |
| Release Version | Rel November 2022 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| SDOH_DATA_ID | NUMERIC (18,0) | The unique identifier (.1 item) for the social driver data record. |
| CONTACT_DATE_REAL | FLOAT | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| LINE | INTEGER | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| CONTACT_DATE | DATETIME | The date of this contact in calendar format. |
| ENTRY_DOM_CONFIG_ID | NUMERIC (18,0) | Stores the source SDC that this entry contains data for. |
| ENTRY_EFFECTIVE_UTC_DTTM | DATETIME (UTC) | Stores the instant at which an entry in SDD was considered active. |
| ENTRY_INTERPRETATION | VARCHAR (200) | Stores the interpretation this entry is reporting. This might be the output of a scoring rule or some other scoring value. |
| ENTRY_CONCERN_LVL_C | INTEGER |  |
| ENTRY_EXT_REF_IDENTIFIER | VARCHAR (174) | Stores a deduplicated DXR reference ID of an SDOH entry that occurred on this contact's date. |
| ENTRY_CALC_FSD_ID | VARCHAR (18) | Stores the FSD ID of the most recently documented flowsheet data for this entry |
| ENTRY_CALC_FSD_LINE | INTEGER | Stores the FSD line of the most recently documented flowsheet data for this entry |
| ENTRY_PAT_ENC_CSN_ID | NUMERIC (18,0) | Stores the CSN of the encounter where this entry was filed |
| ENTRY_TYPE_C | INTEGER |  |
| ENTRY_USER_ID | VARCHAR (18) | Stores the user who documented this entry |
| ENTRY_DX_ID | NUMERIC (18,0) | Stored the networked EDG for a diagnosis-based SDD entry |
| ENTRY_SCORE_FSD_ID | VARCHAR (18) | Stores the FSD ID where the score from a custom formula flowsheet was originally stored |
| ENTRY_SCORE_FSD_LINE | INTEGER | Stores the FSD line where the score from a custom formula flowsheet was originally stored |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | SDOH_DATA_ID | SDD_DATA | SDOH_DATA_ID | No | No | No |  |
| 5 | ENTRY_DOM_CONFIG_ID | SDOH_DOM_CONFIG_INFO | DOM_CONFIG_ID | No | No | No |  |
| 8 | ENTRY_CONCERN_LVL_C | ZC_FIN_RESOURCE_RISK | FIN_RESOURCE_RISK_C | No | No | No |  |
| 10 | ENTRY_CALC_FSD_ID | IP_FLWSHT_REC | FSD_ID | No | No | No |  |
| 10 | ENTRY_CALC_FSD_ID | V_EHI_FSD_FILTER | FSD_ID | Unknown | Unknown | No |  |
| 12 | ENTRY_PAT_ENC_CSN_ID | ALT_ORD_PROV_SINGL | PAT_ENC_CSN_ID | Unknown | No | No |  |
| 12 | ENTRY_PAT_ENC_CSN_ID | AN_RELINK_INFO | PAT_ENC_CSN_ID | No | No | No |  |
| 12 | ENTRY_PAT_ENC_CSN_ID | DENT_ORTH_EXAM_NOTES | PAT_ENC_CSN_ID | No | No | No |  |
| 12 | ENTRY_PAT_ENC_CSN_ID | FAC_CHG_OVERRIDE | PAT_ENC_CSN_ID | No | No | No |  |
| 12 | ENTRY_PAT_ENC_CSN_ID | FAM_HX_PAT_ONLY | PAT_ENC_CSN_ID | No | No | No |  |
| 12 | ENTRY_PAT_ENC_CSN_ID | F_ED_ENCOUNTERS | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 12 | ENTRY_PAT_ENC_CSN_ID | F_HH_CERT_ATTRIBUTES | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 12 | ENTRY_PAT_ENC_CSN_ID | F_HH_OASIS_SINGLE | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 12 | ENTRY_PAT_ENC_CSN_ID | F_HH_OASIS_SINGLE_2 | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 12 | ENTRY_PAT_ENC_CSN_ID | F_HH_OASIS_SINGLE_3 | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 12 | ENTRY_PAT_ENC_CSN_ID | F_HH_OASIS_SINGLE_4 | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 12 | ENTRY_PAT_ENC_CSN_ID | F_HH_OASIS_SINGLE_5 | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 12 | ENTRY_PAT_ENC_CSN_ID | F_IBD_ADULT_FORM_ENC | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 12 | ENTRY_PAT_ENC_CSN_ID | F_IBD_FORM_RESP | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 12 | ENTRY_PAT_ENC_CSN_ID | F_IP_HSP_ADMISSION | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 12 | ENTRY_PAT_ENC_CSN_ID | F_IP_HSP_SEPSIS3 | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 12 | ENTRY_PAT_ENC_CSN_ID | F_IRIS_ENC | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 12 | ENTRY_PAT_ENC_CSN_ID | F_MU_OBJ_EH_ADMISSION | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 12 | ENTRY_PAT_ENC_CSN_ID | F_MU_QM_EH_2014_ED_VISIT | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 12 | ENTRY_PAT_ENC_CSN_ID | F_MU_QM_EH_2014_IP_ADMSN | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 12 | ENTRY_PAT_ENC_CSN_ID | F_QM_AMI | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 12 | ENTRY_PAT_ENC_CSN_ID | F_QM_CAC | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 12 | ENTRY_PAT_ENC_CSN_ID | F_QM_HBIPS | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 12 | ENTRY_PAT_ENC_CSN_ID | F_QM_HEART_FAILURE | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 12 | ENTRY_PAT_ENC_CSN_ID | F_QM_IMMUNIZATION | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |

_(145 total; showing first 30)_
