# ISOLATIONS

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=ISOLATIONS

## Description

This table contains patient isolation data.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | ISO |
| Release Version | Rel August 2020 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| ISOLATION_ID | NUMERIC (18,0) | The unique identifier for the isolation record. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| RECORD_STATUS_2_C | INTEGER |  |
| PAT_ID | VARCHAR (18) | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| PAT_ENC_CSN_ID | NUMERIC (18,0) | The unique contact serial number for the contact in which this isolation took place. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| ISOLATION_C | INTEGER |  |
| ISOLATION_STATUS_C | INTEGER |  |
| HOW_ISO_ADDED_C | INTEGER |  |
| ISOLATION_ORDER_ID | NUMERIC (18,0) | The unique identifier of the order that added the isolation. |
| ADDED_UTC_DTTM | DATETIME (UTC) | The UTC date and time when the isolation was added. |
| ADDED_USER_ID | VARCHAR (18) | The unique ID associated with the user record for the user who added this isolation. This column is frequently used to link to the CLARITY_EMP table. |
| REMOVED_UTC_DTTM | DATETIME (UTC) | The UTC date and time when the isolation was removed. |
| REMOVED_USER_ID | VARCHAR (18) | The unique ID associated with the user record for the user who removed this isolation. This column is frequently used to link to the CLARITY_EMP table. |
| COMMENTS | VARCHAR (4000) | The user-entered comments associated with the isolation |
| RECORD_CREATION_DATE | DATETIME | The date when the isolation record was created. |
| ADDED_LOCAL_DTTM | DATETIME (Attached) | Local instant when isolation was added. |
| REMOVED_LOCAL_DTTM | DATETIME (Attached) | Local instant when isolation was removed. |
| INFECTION_LINKS_CALCULATED_YN | VARCHAR (1) | Surrogate key used to uniquely identify rows in this (and only this) table on Cogito Cloud only, do not assume the surrogate key in this table will correspond to the surrogate key in another table |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 2 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 2 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 3 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 4 | RECORD_STATUS_2_C | ZC_RECORD_STATUS_2 | RECORD_STATUS_2_C | No | No | No |  |
| 4 | RECORD_STATUS_2_C | ZC_RECORD_STS | RECORD_STS_C | No | No | No |  |
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

_(263 total; showing first 30)_
