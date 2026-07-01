# PROBLEM_LIST

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=PROBLEM_LIST

## Description

The PROBLEM_LIST table contains data from patients' problem lists in the clinical system. The data in this table reflects the current status of all problems on the patient's problem list. In the clinical system, each problem is marked as active until it becomes (and is marked) Resolved or Deleted. At that point, by default, it will not be displayed in the application. However, any problem ever entered on this list is stored in the database and will exist in this table. Deleted and resolved problems can be viewed in the application by simply marking a checkbox to show them. Note that deleted and resolved problems can be restored by undeleting them (an option in the application). When a deleted problem is restored, its status is changed to active and the deleted date is returned to null.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | LPL |
| Release Version | EPIC 2000 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| PROBLEM_LIST_ID | NUMERIC (18,0) | The unique ID of this Problem List entry. |
| PAT_ID | VARCHAR (18) | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| DX_ID | NUMERIC (18,0) | The unique ID of the diagnosis record associated with the entry in the patient?s Problem List. Note: This is NOT the ICD9 diagnosis code. It is an internal identifier that is typically not visible to a user. |
| ICD9_CODE | No | *** Deprecated *** In table PROBLEM_LIST, the column ICD9_CODE (EDG Translation) has been deprecated. Link to the CLARITY_EDG table using PROBLEM_LIST.DX_ID column. Refer to the Diagnosis and ICD Procedure Updates section of https://galaxy.epic.com/redirect.aspx?documentid=1577542 to determine the correct column to use. |
| DESCRIPTION | VARCHAR (200) | The display name of the problem. Only contains data if the default display name is changed. |
| NOTED_DATE | DATETIME | Represents the first possible date that a problem could have been noted/onset on. By default, this is the problem's date of entry into the problem list. The intent of this field is to allow users to change this date to the date the problem was first diagnosed if that is different than the entry date.  A problem's noted date is documented as a fuzzy date, meaning that it can capture approximate date data ("2012", "1/2012") or exact data ("3/5/2012"). This column captures the earliest date of the effective range. See NOTED_END_DATE for the latest counterpart. For example, if 2012 is documented in hyperspace, then NOTED_DATE will be 1/1/2012 and NOTED_END_DATE will be 12/31/2012. |
| RESOLVED_DATE | DATETIME | The date the problem was resolved in calendar format. |
| DATE_OF_ENTRY | DATETIME | This is the date the specific problem was last edited (i.e., a change was made, either in status, priority, etc.). |
| ENTRY_USER_ID | VARCHAR (18) | The unique ID of the system user who last edited the problem in the patient?s Problem List. This ID may be encrypted. |
| STATUS *(deprecated)* | VARCHAR (10) |  |
| CLASS_OF_PROBLEM *(deprecated)* | VARCHAR (25) |  |
| PRIORITY *(deprecated)* | VARCHAR (25) |  |
| UPDATE_DATE | No | *** Deprecated *** This column is not reliably populated, row update tracking should be used instead. ****** The extract date and time of the record for this table. |
| CM_PHY_OWNER_ID | VARCHAR (25) | ID of the physical deployment owner for this record.  Physical owners will be where the data is hosted, either on the cross-over server or the owner deployment. |
| CM_LOG_OWNER_ID | VARCHAR (25) | ID of the logical deployment owner for this record.  Logical owners show the deployment where the record was created but doesn't represent if the record is a part of version skew. |
| DX_EXTERNAL_ID *(deprecated)* | VARCHAR (250) | *** Deprecated *** In table PROBLEM_LIST, the column DX_EXTERNAL_ID (EDG 40) has been deprecated. Link to the CLARITY_EDG table using PROBLEM_LIST.DX_ID column. Refer to the Diagnosis and ICD Procedure Updates section of https://galaxy.epic.com/redirect.aspx?documentid=1577542 to determine the correct column to use. |
| PROBLEM_CMT | VARCHAR (1024) | The preview text (first characters) of the Overview note entered for a Problem List entry. |
| CHRONIC_YN | VARCHAR (1) |  |
| SHOW_IN_MYC_YN | VARCHAR (1) |  |
| PROBLEM_EPT_CSN *(deprecated)* | NUMERIC (18,0) |  |
| PRINCIPAL_PL_YN *(deprecated)* | VARCHAR (1) |  |
| HOSPITAL_PL_YN *(deprecated)* | VARCHAR (1) |  |
| PROBLEM_STATUS_C | INTEGER |  |
| CLASS_OF_PROBLEM_C | INTEGER |  |
| PRIORITY_C | INTEGER |  |
| OVERVIEW_NOTE_ID | VARCHAR (254) | This item is a link to the note record that contains the overview note pertaining to this problem record. |
| STAGE_ID | NUMERIC (18,0) | The unique ID of the cancer stage record associated with the entry in the patient?s Problem List. |
| PROBLEM_TYPE_C | INTEGER |  |
| CHRON_MED_ID *(deprecated)* | NUMERIC (18,0) | The chronic medications information for the problem. NOTE: this column is deprecated since item LPL 5000 is not populated for the record type that this table is extracting. |
| CHRON_MED_STRT_DATE *(deprecated)* | DATETIME | The chronic medications start date for the problem. NOTE: this column is deprecated since item LPL 5010 is not populated for the record type that this table is extracting. |
| IS_PRESENT_ON_ADM_C *(deprecated)* | INTEGER |  |
| REC_ARCHIVED_YN | No | Indicates whether the Problem List record is archived at the record level. |
| CREATING_ORDER_ID | NUMERIC (18,0) | The order ID of the order that created the problem. |
| NO_STAGE_REASON_C | INTEGER |  |
| NO_STAGE_COMMENT | VARCHAR (255) | For a problem that could be staged, stores a free-text comment explaining why the problem was not staged. |
| NO_STAGE_USER_ID | VARCHAR (18) | For a problem that could be staged, stores the user who chose not to stage it. |
| NO_STAGE_DTTM | DATETIME (UTC) | For a problem that could be staged, stores the instant when a user flagged it to not be staged. |
| TREAT_SUMM_STATUS_C | INTEGER |  |
| NOTED_END_DATE | DATETIME | Represents the last possible date that a problem could have been noted/onset on.   A problem's noted date is documented as a fuzzy date, meaning that it can capture approximate date data ("2012", "1/2012") or exact data ("3/5/2012"). This column captures the latest date of the effective range. See NOTED_DATE for the earliest counterpart. For example, if 2012 is documented in hyperspace, then NOTED_DATE will be 1/1/2012 and NOTED_END_DATE will be 12/31/2012.  Note that the value may be empty, even if NOTED_DATE is populated |
| EXTERNAL_PROBLEM_IDENT | VARCHAR (192) | Store the external ID for a problem list LPL record |
| ENTRY_HOST_MODULE_C | INTEGER |  |
| REL_GOALS_PROBLEM_LIST_CSN_ID | NUMERIC (18,0) | Stores the CSN (contact serial number I.E. unique contact identifier) of the last related goals contact that was edited. |
| REL_GOALS_INST_DTTM | DATETIME (Local) | Stores the instant of the last related goals contact that was edited. |
| PROB_STAGE_STATUS_C | INTEGER |  |
| DIAG_START_DATE | DATETIME | Represents the earliest possible date that a problem could have been diagnosed on. The latest possible date is stored in DIAG_END_DATE. If these values are the same, then the date is exact rather than fuzzy. For a problem or condition affecting a patient, the diagnosis date is defined as the date when a qualified professional first recognized the presence of that condition with sufficient certainty, regardless of whether it was fully characterized at that time. For diseases such as cancer, this may be the earliest date of a clinical diagnosis from before it was histologically confirmed, not the date of confirmation if that occurred later. |
| DIAG_END_DATE | DATETIME | Represents the last possible date that a problem could have been diagnosed on. The earliest possible date is stored in DIAG_START_DATE. If these values are the same, then the date is exact rather than fuzzy. For a problem or condition affecting a patient, the diagnosis date is defined as the date when a qualified professional first recognized the presence of that condition with sufficient certainty, regardless of whether it was fully characterized at that time. For diseases such as cancer, this may be the earliest date of a clinical diagnosis from before it was histologically confirmed, not the date of confirmation if that occurred later. |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| B-TREE INDEX | EIX_PROBLEM_LIST_DXID | DX_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_PROBLEM_LIST_PAID | PAT_ID | 1 | Yes | Yes |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | PROBLEM_LIST_ID | ADVERSE_EVENT_INFO | ADVERSE_EVENT_ID | No | No | No |  |
| 1 | PROBLEM_LIST_ID | ALLERGY | ALLERGY_ID | Unknown | No | No |  |
| 1 | PROBLEM_LIST_ID | COMPLICATIONS | PROBLEM_LIST_ID | No | No | No |  |
| 1 | PROBLEM_LIST_ID | HH_PBLST_INFO | PROBLEM_LIST_ID | Unknown | No | No |  |
| 1 | PROBLEM_LIST_ID | IMMUNE | IMMUNE_ID | Unknown | No | No |  |
| 1 | PROBLEM_LIST_ID | PL_SYSTEMS | PROBLEM_LIST_ID | Unknown | No | No |  |
| 1 | PROBLEM_LIST_ID | PROBLEM_LIST_ALL | PROBLEM_LIST_ID | No | No | No |  |
| 1 | PROBLEM_LIST_ID | PROB_TXP_MODIFIERS | PROBLEM_LIST_ID | Unknown | No | No |  |
| 1 | PROBLEM_LIST_ID | V_IMMUNIZATION_ADMINS | IMMUNE_ID | Unknown | Unknown | No |  |
| 2 | PAT_ID | ANTICOAG_SELF_REGULATING | PAT_ID | No | No | No |  |
| 2 | PAT_ID | CARE_COORDINATION | PAT_ID | Unknown | No | No |  |
| 2 | PAT_ID | CLAIMS_DERIVE_PAT_FLAGS | PAT_ID | No | No | No |  |
| 2 | PAT_ID | COMMUNITY_RESRC_REVIEWED | PAT_ID | No | No | No |  |
| 2 | PAT_ID | D_PAT_GEOGRAPHIC_CLASS | PAT_ID | Unknown | Unknown | No |  |
| 2 | PAT_ID | EPT_MEM_INFO | PAT_ID | No | No | No |  |
| 2 | PAT_ID | EXT_DATA_LAST_DONE | PAT_ID | No | No | No |  |
| 2 | PAT_ID | F_IBD_ADULT_FORM_PAT | PAT_ID | Unknown | Unknown | No |  |
| 2 | PAT_ID | HH_PAT_INFO | PAT_ID | Unknown | No | No |  |
| 2 | PAT_ID | HM_STATUS_UPD | PAT_ID | No | No | No |  |
| 2 | PAT_ID | IMMNZTN_LAST_REVIEW | PAT_ID | No | No | No |  |
| 2 | PAT_ID | PATIENT | PAT_ID | No | No | No |  |
| 2 | PAT_ID | PATIENT_2 | PAT_ID | No | No | No |  |
| 2 | PAT_ID | PATIENT_3 | PAT_ID | No | No | No |  |
| 2 | PAT_ID | PATIENT_4 | PAT_ID | No | No | No |  |
| 2 | PAT_ID | PATIENT_5 | PAT_ID | No | No | No |  |
| 2 | PAT_ID | PATIENT_6 | PAT_ID | No | No | No |  |
| 2 | PAT_ID | PATIENT_CONF_ADDR | PAT_ID | No | No | No |  |
| 2 | PAT_ID | PATIENT_MISC_COMMENTS | PAT_ID | No | No | No |  |
| 2 | PAT_ID | PATIENT_MYC | PAT_ID | Unknown | No | No |  |
| 2 | PAT_ID | PATIENT_OPT | PAT_ID | No | No | No |  |

_(195 total; showing first 30)_
