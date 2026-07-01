# PAT_MRN_HX

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=PAT_MRN_HX

## Description

*** Deprecated *** Some of the deprecated table's data is no longer populated in Chronicles and is no longer available, the rest can be found in the replacement tables listed in the Replacement Objects grid.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | EPT |
| Release Version | SUMMER 2005 |
| May contain EHI? | No |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| PAT_ID | VARCHAR (18) | This column contains the patient record's internal ID (.1). |
| LINE | No | The line number for the MRN History information associated with this record. Multiple pieces of information can be associated with this record. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The physical owner of the record. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The logical owner of the record. |
| MRN_HX | VARCHAR (254) | The unique internal ID of the source patient involved in the Identity event. |
| MRN_HX_CHANGE_INST | DATETIME (Local) | Instant of MRN change. |
| MRN_HX_CHANGE_STAF | VARCHAR (254) | User who made the change to the MRN. |
| MRN_HX_PAT_NAME | VARCHAR (254) | The name associated with the record involved in the MRN History event. |
| MRN_HX_DOB | DATETIME | Previous date of birth. |
| MRN_HX_ALIAS | VARCHAR (254) | The aliases associated with the record involved in the MRN History event. |
| MRN_HX_LOC_PRIM_ID | VARCHAR (254) | Previous primary location. |
| MRN_HX_LOC_PERM_ID | VARCHAR (254) | Pervious permanent chart location. |
| DATE_MRN_CHANGE | DATETIME | The date of the MRN History event in calendar format. |
| UNMRG_MRGEVENT_ID | NUMERIC (18,0) | Merge Event for Non-CE Merges |
| UNMRG_MPTSOURCE_ID | VARCHAR (254) | Source patient's MPT record ID. |
| UNMRG_MPTTARGET_ID | VARCHAR (254) | Target patient's MPT record ID. |
| UNMRG_UNMERGED_YN | VARCHAR (1) |  |
| UNMRG_PREUMGMPT_ID | VARCHAR (254) | Pre-unmerged MPT ID. |
| UNMRG_INSTANT | DATETIME (Local) | The date and time when the record in the MRN History event was unmerged from the patient. |
| UNMRG_HUMRPT_ID | NUMERIC (18,0) | Record ID for overlay resolution report for this unmerge. |
| UNMRG_STAFF | VARCHAR (254) | User who unmerged the records. |
| MRN_HX_EMPL | VARCHAR (254) | The employee ID associated with the record involved in the MRN History event. |
| PTNTL_UNMRGE_USR_ID *(deprecated)* | VARCHAR (18) | *** Deprecated *** The deprecated column's content/data is no longer available since it is no longer populated in Chronicles  The user who marked the merge event as a potential unmerge. |
| POTENTL_UNMRGE_DTTM *(deprecated)* | DATETIME (Local) | *** Deprecated *** The deprecated column's content/data is no longer available since it is no longer populated in Chronicles  The date the potential unmerge was made. |
| MARK_FOR_UNMERGE_C *(deprecated)* | INTEGER |  |
