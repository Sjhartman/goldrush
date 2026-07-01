# SDD_DATA

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=SDD_DATA

## Description

This table stores defining information about a patient's SDOH data. Each row in this table represents documentation for a single SDOH domain for a single patient.

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
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| RECORD_STATUS_C | INTEGER |  |
| DOMAIN_C | INTEGER |  |
| PAT_ID | VARCHAR (18) | The patient this SDD record stores data for. |
| CONCERNS_PRESENT_YN | VARCHAR (1) |  |
| RECORD_CREATE_UTC_DTTM | DATETIME (UTC) | The instant this record was created. |
| PREDICTED_RISK_CSN_ID | NUMERIC (18,0) | A pointer to the most recent LLM contact (prediction) associated with a domain. |

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
| 5 | DOMAIN_C | ZC_SDOH_ADDRESSED | SDOH_ADDRESSED_C | No | No | No |  |
| 6 | PAT_ID | ANTICOAG_SELF_REGULATING | PAT_ID | No | No | No |  |
| 6 | PAT_ID | CARE_COORDINATION | PAT_ID | Unknown | No | No |  |
| 6 | PAT_ID | CLAIMS_DERIVE_PAT_FLAGS | PAT_ID | No | No | No |  |
| 6 | PAT_ID | COMMUNITY_RESRC_REVIEWED | PAT_ID | No | No | No |  |
| 6 | PAT_ID | D_PAT_GEOGRAPHIC_CLASS | PAT_ID | Unknown | Unknown | No |  |
| 6 | PAT_ID | EPT_MEM_INFO | PAT_ID | No | No | No |  |
| 6 | PAT_ID | EXT_DATA_LAST_DONE | PAT_ID | No | No | No |  |
| 6 | PAT_ID | F_IBD_ADULT_FORM_PAT | PAT_ID | Unknown | Unknown | No |  |
| 6 | PAT_ID | HH_PAT_INFO | PAT_ID | Unknown | No | No |  |
| 6 | PAT_ID | HM_STATUS_UPD | PAT_ID | No | No | No |  |
| 6 | PAT_ID | IMMNZTN_LAST_REVIEW | PAT_ID | No | No | No |  |
| 6 | PAT_ID | PATIENT | PAT_ID | No | No | No |  |
| 6 | PAT_ID | PATIENT_2 | PAT_ID | No | No | No |  |
| 6 | PAT_ID | PATIENT_3 | PAT_ID | No | No | No |  |
| 6 | PAT_ID | PATIENT_4 | PAT_ID | No | No | No |  |
| 6 | PAT_ID | PATIENT_5 | PAT_ID | No | No | No |  |
| 6 | PAT_ID | PATIENT_6 | PAT_ID | No | No | No |  |
| 6 | PAT_ID | PATIENT_CONF_ADDR | PAT_ID | No | No | No |  |
| 6 | PAT_ID | PATIENT_MISC_COMMENTS | PAT_ID | No | No | No |  |
| 6 | PAT_ID | PATIENT_MYC | PAT_ID | Unknown | No | No |  |
| 6 | PAT_ID | PATIENT_OPT | PAT_ID | No | No | No |  |

_(41 total; showing first 30)_
