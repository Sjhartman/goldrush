# ENROLL_INFO

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=ENROLL_INFO

## Description

The ENROLL_INFO table contains information about patient enrollments in research studies, including status, alias, start and end dates, and last modified user and instant.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | LAR |
| Release Version | Summer 2009 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| ENROLL_ID | NUMERIC (18,0) | The unique ID of the patient-study association record for this row. This column is frequently used to link to the ENROLL_INFO table. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| RECORD_STATUS_C | INTEGER |  |
| RESEARCH_STUDY_ID | VARCHAR (18) | Unique ID of the associated Research Study record. |
| PAT_ID | VARCHAR (18) | Unique ID of the associated Patient record. |
| ENROLL_STATUS_C | INTEGER |  |
| STUDY_ALIAS | VARCHAR (45) | Patient's alias for the study enrollment. |
| ENROLL_START_DT | DATETIME | Start date of the patient's enrollment in the study. |
| ENROLL_END_DT | DATETIME | End date of the patient's enrollment in the study. |
| ENROLL_CMT_NOTE_ID | VARCHAR (254) | The ID number for comments/notes associated with the enrollment. |
| LAST_MOD_DTTM | DATETIME (Attached) | Instant the enrollment information was last modified. |
| LAST_MOD_USER_ID | VARCHAR (18) | User who modified the enrollment information last. |
| RECORD_CREATION_DT | DATETIME | Stores the date the record was created. |
| RECORD_NAME | VARCHAR (200) | The name of this User Enrollment record. |
| CR_BY_INTERFACE_YN | VARCHAR (1) |  |
| STUDY_BRANCH_ID | VARCHAR (48) | For a patient enrolled in a research study that has multiple branches (or arms), this item stores the ID of the specific branch of that study to which the patient is assigned. |
| LAST_MOD_SOURCE_C | INTEGER |  |
| RSH_MYC_STATUS_C | INTEGER |  |
| MYC_VIEWED_UTC_DTTM | DATETIME (UTC) | The date and time in UTC that a patient first viewed this enrollment as a MyChart recruitment request. |
| MYC_APPROVING_EMP_ID | VARCHAR (18) | Either the user who was asked to approve this MyChart recruitment request if it is still awaiting approval, or the one who did approve or decline the request. |
| ADVERSE_EVENT_REVIEW_UTC_DTTM | DATETIME (UTC) | The date and time of last review for the adverse events for this study association. |
| ADVERSE_EVENT_REVIEW_USER_ID | VARCHAR (18) | The unique ID of the last reviewing user for the adverse events for this study association. |
| RECRUITMENT_QUESR_ANSWER_ID | VARCHAR (18) | The unique identifier of the recruitment questionnaire answers for this study association. |
| MYC_RESPONSE_TYPE_C | INTEGER |  |
| FIRST_INVITATION_SENT_YN | VARCHAR (1) |  |
| FIRST_INVITE_LAST_MOD_SOURCE_C | INTEGER |  |
| FIRST_INVITATION_SENT_UTC_DTTM | DATETIME (UTC) | The UTC instant at which the first research study invitation was sent for this patient-study invitation. |
| LAST_DEMO_AUTH_TOKEN | VARCHAR (64) | The last demographic authentication token that was generated for this patient-study association. |
| OPA_MANUAL_OUTREACH_UTC_DTTM | DATETIME (UTC) | The UTC instant at which the first manual OPA outreach was performed for this patient-study association. |
| OPA_AUTO_OUTREACH_UTC_DTTM | DATETIME (UTC) | The UTC instant at which the first automatic OPA outreach was performed for this patient-study association. |
| PAT_INITIATED_INTEREST_C | INTEGER | Surrogate key used to uniquely identify rows in this (and only this) table on Cogito Cloud only, do not assume the surrogate key in this table will correspond to the surrogate key in another table |
| CREATION_COMM_ID | NUMERIC (18,0) | The unique ID of the CRM case that resulted in the creation of the study association record. |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ENROLL_ID | LAR_RCVD_DOC | ENROLL_ID | No | No | No |  |
| 2 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 2 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 2 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 3 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 4 | RECORD_STATUS_C | ZC_RECORD_STATUS_2 | RECORD_STATUS_2_C | No | No | No |  |
| 4 | RECORD_STATUS_C | ZC_RECORD_STS | RECORD_STS_C | No | No | No |  |
| 5 | RESEARCH_STUDY_ID | CLARITY_RSH | RESEARCH_ID | Unknown | Unknown | No |  |
| 5 | RESEARCH_STUDY_ID | RSH_MULTISITE_INFO | RESEARCH_ID | No | No | No |  |
| 5 | RESEARCH_STUDY_ID | RSH_RCVD_DOC | RESEARCH_ID | No | No | No |  |
| 5 | RESEARCH_STUDY_ID | RSH_RESEARCH_INFO | RESEARCH_ID | No | No | No |  |
| 5 | RESEARCH_STUDY_ID | RSH_RESEARCH_INFO_2 | RESEARCH_ID | No | No | No |  |
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

_(129 total; showing first 30)_
