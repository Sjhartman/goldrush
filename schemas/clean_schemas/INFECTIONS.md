# INFECTIONS

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=INFECTIONS

## Description

This table contains basic information about patient infections.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | INF |
| Release Version | Rel August 2019 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| INFECTION_ID | NUMERIC (18,0) | The unique identifier for the infection record. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| RECORD_STATUS_C | INTEGER |  |
| INFECTION_RECORD_TYPE_C | INTEGER |  |
| PAT_ID | 100 | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| PAT_ENC_CSN_ID | NUMERIC (18,0) | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| INFECTION_TYPE_C | INTEGER |  |
| INF_STATUS_C | INTEGER |  |
| HOW_ADDED_C | INTEGER |  |
| ADD_UTC_DTTM | DATETIME (UTC) | The UTC date and time that the infection was added to the patient chart. |
| ADD_USER_ID | VARCHAR (18) | The unique ID associated with the user who added the infection. This column is frequently used to link to the CLARITY_EMP table. |
| RESOLVE_UTC_DTTM | DATETIME (UTC) | The UTC date and time that the infection was resolved in the patient chart. |
| RESOLVE_USER_ID | VARCHAR (18) | The unique ID associated with the user who resolved the infection. This column is frequently used to link to the CLARITY_EMP table. |
| EXPIRATION_DATE | DATETIME | The date when the infection is set to automatically expire. |
| DOESNT_EXPIRE_YN | VARCHAR (1) |  |
| REVIEW_DATE | DATETIME | The date that the infection should be reviewed. |
| ONSET_DATE | DATETIME | The date that the infection began. |
| COMMENTS | VARCHAR (4000) | User-entered comments associated with the infection. |
| SPECIMEN_TYPE_C | INTEGER |  |
| SPECIMEN_SOURCE_C | INTEGER |  |
| RECORD_CREATION_DATE | DATETIME | The date the infection record was created. |
| ADD_LOCAL_DTTM | DATETIME (Attached) | The local date and time that the infection was added to the patient chart. |
| RESOLVE_LOCAL_DTTM | DATETIME (Attached) | The local date and time that the infection was resolved in the patient chart. |
| ISOLATION_LINKS_CALCULATED_YN | VARCHAR (1) |  |
| REQUIRED_ISOLATION_OPTION_C | INTEGER |  |
| COMMENT_UTC_DTTM | DATETIME (UTC) | The UTC date and time that the current comment was saved. |
| COMMENT_USER_ID | VARCHAR (18) | The unique ID associated with the user who entered the current comment. This column is frequently used to link to the CLARITY_EMP table. |

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
| 5 | INFECTION_RECORD_TYPE_C | ZC_INFECTION_RECORD_TYPE | INFECTION_RECORD_TYPE_C | No | No | No |  |
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

_(211 total; showing first 30)_
