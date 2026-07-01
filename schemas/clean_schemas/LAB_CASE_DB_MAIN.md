# LAB_CASE_DB_MAIN

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=LAB_CASE_DB_MAIN

## Description

The main table for Lab Anatomic Pathology cases. It contains mostly items that do not change much over time.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | REQ |
| Release Version | Summer 2009 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| CASE_ID | NUMERIC (18,0) | The unique identifier for the case record. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| CASE_ACCESSION_DTTM | DATETIME (Local) | The instant that the case was accessioned. Currently, 'accessioned' means the time when the case is first accepted in Case Builder. |
| CASE_RECEIVED_DTTM | DATETIME (Local) | The instant that the case was received.  This is equivalent to the instant when the first specimen on the case was received. |
| CASE_OVERDUE_DTTM | DATETIME (Local) | The instant when the case is considered overdue.  This is equivalent to the Case Accession Instant plus the Case Expected Length. |
| CASE_PAT_ID | VARCHAR (18) | Stores the patient record ID that this case is linked to. |
| CASE_GROUPER_ID | NUMERIC (18,0) | Stores the Requisition Grouper record ID that this case is linked to. |
| CASE_PAT_CONTACT | VARCHAR (91) | Stores the patient contact that this case is linked to. |
| CASE_LAB_ID | VARCHAR (18) | Stores the laboratory associated with this case. |
| DATE_ENTR_DT | DATETIME | Stores the date the case was created. |
| CASE_COLL_DTTM | DATETIME (Local) | The date and time when the case was first collected. |
| CASE_SIGNOUT_DTTM | DATETIME (Local) | The date and time when the case was completely signed out. |
| CONTAINER_ID | VARCHAR (18) | The unique identifier of the tracking container associated with this case record. |
| CASE_TASK_ADD_DTTM | 135 | The latest date and time when a task was added to the case. |
| INSTANT_PAT_ASSOC_UTC_DTTM | DATETIME (UTC) | The date and time when the patient was associated with the case. |
| CASE_SUBSPECIALTY_C | INTEGER |  |
| ASSIGNED_PATH_USER_ID | VARCHAR (18) | The unique identifier of the user assigned to the case with a role of Staff Pathologist. |
| ASSIGNED_CYTOTECH_USER_ID | VARCHAR (18) | The unique identifier of the user assigned to the case with a role of Cytotechnologist. |
| PAT_ASSOC_DTTM | DATETIME (Local) | The date and time when the patient was associated with the case in the lab's time zone. |
| LAST_TASK_ADDED_UTC_DTTM | DATETIME (UTC) | The last date and time in UTC that a task was added to this case. |
| CASE_ACCESSION_UTC_DTTM | DATETIME (UTC) | The date and time that the case was accessioned, in UTC |
| PRIMARY_SPECIMEN_ID | VARCHAR (18) | The unique ID of the primary specimen on the case. |
| SERVICE_LINE_PROVIDERTEAM_ID | NUMERIC (18,0) | The unique ID of the provider team which represents the service line assigned to the case. |
| PRIM_SPEC_OVRIDE_USER_ID | VARCHAR (18) | The unique ID of the user who overrode the primary specimen of this case. This column is frequently used to link to the CLARITY_EMP table. |
| PRIM_SPEC_OVRIDE_UTC_DTTM | DATETIME (UTC) | UTC date and time of when the primary specimen was overridden by the user |
| CTZN_OVRIDE_USER_ID | VARCHAR (18) | The unique ID of the user who overrode the categorization of this case. This column is frequently used to link to the CLARITY_EMP table. |
| CTZN_OVRIDE_UTC_DTTM | DATETIME (UTC) | UTC date and time of when either the subspecialty or service categorization of the case were overridden |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | CASE_ID | EXT_ID_BUNDLE_MAP_DB_MAIN | MAPPING_ID | No | No | No |  |
| 1 | CASE_ID | ID_BUNDLE_DEMOG_DB_MAIN | DEMOG_ID | No | No | No |  |
| 1 | CASE_ID | REQ_ALL_MAIN | REQUISITION_ID | No | No | No |  |
| 1 | CASE_ID | REQ_DB_MAIN | REQUISITION_ID | Unknown | No | No |  |
| 2 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 2 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 2 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 3 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 7 | CASE_PAT_ID | ANTICOAG_SELF_REGULATING | PAT_ID | No | No | No |  |
| 7 | CASE_PAT_ID | CARE_COORDINATION | PAT_ID | Unknown | No | No |  |
| 7 | CASE_PAT_ID | CLAIMS_DERIVE_PAT_FLAGS | PAT_ID | No | No | No |  |
| 7 | CASE_PAT_ID | COMMUNITY_RESRC_REVIEWED | PAT_ID | No | No | No |  |
| 7 | CASE_PAT_ID | D_PAT_GEOGRAPHIC_CLASS | PAT_ID | Unknown | Unknown | No |  |
| 7 | CASE_PAT_ID | EPT_MEM_INFO | PAT_ID | No | No | No |  |
| 7 | CASE_PAT_ID | EXT_DATA_LAST_DONE | PAT_ID | No | No | No |  |
| 7 | CASE_PAT_ID | F_IBD_ADULT_FORM_PAT | PAT_ID | Unknown | Unknown | No |  |
| 7 | CASE_PAT_ID | HH_PAT_INFO | PAT_ID | Unknown | No | No |  |
| 7 | CASE_PAT_ID | HM_STATUS_UPD | PAT_ID | No | No | No |  |
| 7 | CASE_PAT_ID | IMMNZTN_LAST_REVIEW | PAT_ID | No | No | No |  |
| 7 | CASE_PAT_ID | PATIENT | PAT_ID | No | No | No |  |
| 7 | CASE_PAT_ID | PATIENT_2 | PAT_ID | No | No | No |  |
| 7 | CASE_PAT_ID | PATIENT_3 | PAT_ID | No | No | No |  |
| 7 | CASE_PAT_ID | PATIENT_4 | PAT_ID | No | No | No |  |
| 7 | CASE_PAT_ID | PATIENT_5 | PAT_ID | No | No | No |  |
| 7 | CASE_PAT_ID | PATIENT_6 | PAT_ID | No | No | No |  |
| 7 | CASE_PAT_ID | PATIENT_CONF_ADDR | PAT_ID | No | No | No |  |
| 7 | CASE_PAT_ID | PATIENT_MISC_COMMENTS | PAT_ID | No | No | No |  |
| 7 | CASE_PAT_ID | PATIENT_MYC | PAT_ID | Unknown | No | No |  |

_(119 total; showing first 30)_
