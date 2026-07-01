# CL_QANSWER

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=CL_QANSWER

## Description

This table contains general information about questionnaire answer records. For example, the questionnaire the answer record is for, the date it was answered, and whether the answer record is closed.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | HQA |
| Release Version | MU4 - MAY 2001 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| ANSWER_ID | VARCHAR (18) | The unique ID of the questionnaire answer record. |
| FORM_ID | VARCHAR (18) | The unique ID of the questionnaire form associated with the questionnaire answer. |
| QUESTIONNAIRE_DAT | DATETIME | Holds the date on which a questionnaire was entered. This column should not be used to join to overtime questionnaire tables (e.g. CL_QFORM_QUEST and CL_QFORM_OVTM). Rather, use the foreign key comprised of the FORM_ID and FORM_DATE_REAL columns to join to those tables. |
| IS_CLOSED | VARCHAR (1) |  |
| CM_PHY_OWNER_ID | VARCHAR (25) | ID of the physical deployment owner for this record.  Physical owners will be where the data is hosted, either on the cross-over server or the owner deployment. |
| CM_LOG_OWNER_ID | VARCHAR (25) | ID of the logical deployment owner for this record.  Logical owners show the deployment where the record was created but doesn't represent if the record is a part of version skew. |
| QF_VERIFY_HVR_ID *(deprecated)* | INTEGER | This column is deprecated and does not extract any data. To report on verifications associated with questionnaire answers, use the QF_VERIFY_HVR_ID column in CL_QANSWER_VERIFY. |
| IMG_ANSWER_SET_NAME | VARCHAR (192) | Used by Imaging One Click Normals Setup activity for populating picklists. |
| FORM_DATE_REAL | FLOAT | The unique, internal contact date of the associated questionnaire record in decimal format. The integer portion of the number indicates the date of the questionnaire record contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. Along with FORM_ID, this forms the foreign key to overtime questionnaire tables (e.g. CL_QFORM_QUEST and CL_QFORM_OVTM). |
| REC_CREATE_USER_ID | VARCHAR (18) | The unique ID of the user who created this record. |
| REC_ARCHIVED_YN | No | Indicates whether the Questionaire Answer record is archived at the record level. |
| PE_HX_REVIEWED_YN | VARCHAR (1) |  |
| PE_HX_DONE_YN | VARCHAR (1) |  |
| ENROLL_ID | NUMERIC (18,0) | The unique identifier of the research study-patient association for the questionnaire. |
| IMG_PROC_ORDER_ID | NUMERIC (18,0) | Virtual item that returns the record ID for the ORD that points to the given Questionnaire Answer |
| PAT_ID | VARCHAR (18) | The unique ID (EPT .1) of the patient subject for whom this record was created. This column is frequently used to link to the PATIENT table. |
| WORKFLOW_DURATION | INTEGER | The amount of time (in seconds) that was spent answering the patient-entered questionnaire. |
| FURTHEST_QUESTION_ID | VARCHAR (18) | The furthest question in the questionnaire that was answered by the user. This is only populated for Patient-Entered Questionnaires. |
| PARENT_ANSWER_ID | VARCHAR (18) | The parent questionnaire response that was branched from to get to this questionnaire. |
| CONFIDENTIAL_YN | VARCHAR (1) |  |
| UNREL_LQF_LQL_YN | VARCHAR (1) |  |
| DYNAMIC_GROUPER_ID | NUMERIC (18,0) | The ID of the DQG record that holds the questionnaire for these responses. |
| RELATED_AUTH_BUNDLE_ID | NUMERIC (18,0) | Contains the authorization bundle (ATB) record that these answers are associated with. |
| REALTIME_TX_CSN_ID | NUMERIC (18,0) | Contains the CSN of the RTX record that these answers were generated as a response to. The RTX record may be purged, but this is still used to form the reference on the QuestionnaireResponse FHIR resource. |
| REALTIME_TX_SERVICE_LINE | INTEGER | Contains the line in the services table of the RTX record these questions are associated with. Used in part to generate the FHIR ID for part of the QuestionnaireReponse resource for these items. |
| DTR_ANSWER_STATUS_C | INTEGER |  |
| DTR_ANSWERS_FINALIZED_YN | VARCHAR (1) |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ANSWER_ID | DTREE_ANSWER | DTREE_ANSWER_ID | No | No | No |  |
| 1 | ANSWER_ID | V_SELF_TRIAGE_STATS | DTREE_ANSWER_ID | Unknown | Unknown | No |  |
| 2 | FORM_ID | CL_QFORM | FORM_ID | No | No | No |  |
| 2 | FORM_ID | CL_QFORM1 | FORM_ID | Unknown | No | No |  |
| 2 | FORM_ID | CL_QFORM_OVTM | FORM_ID | Unknown | Unknown | Yes |  |
| 2 | FORM_ID | DECISION_TREE_INFO | DTREE_ID | No | No | No |  |
| 2 | FORM_ID | QUESR_INSTRUCTIONS | FORM_ID | No | No | No |  |
| 5 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 5 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 5 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 6 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 6 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 6 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 9 | FORM_DATE_REAL | CL_QFORM_OVTM | CONTACT_DATE_REAL | Unknown | Unknown | Yes |  |
| 10 | REC_CREATE_USER_ID | CLARITY_EMP | USER_ID | Unknown | No | No |  |
| 10 | REC_CREATE_USER_ID | CLARITY_EMP_2 | USER_ID | Unknown | No | No |  |
| 10 | REC_CREATE_USER_ID | CLARITY_EMP_3 | USER_ID | Unknown | No | No |  |
| 10 | REC_CREATE_USER_ID | CLARITY_EMP_4 | USER_ID | No | No | No |  |
| 10 | REC_CREATE_USER_ID | CLARITY_EMP_DEMO | USER_ID | No | No | No |  |
| 10 | REC_CREATE_USER_ID | EMP_BASIC_INFO | USER_ID | No | No | No |  |
| 10 | REC_CREATE_USER_ID | EMP_DOC_SETTINGS | USER_NUMBER_ID | No | No | No |  |
| 10 | REC_CREATE_USER_ID | F_RX_USER | USER_ID | Unknown | Unknown | No |  |
| 10 | REC_CREATE_USER_ID | IB_MESSAGE_SETTINGS | USER_ID | No | No | No |  |
| 10 | REC_CREATE_USER_ID | LOGIN_INFO | USER_NUMBER_ID | No | No | No |  |
| 10 | REC_CREATE_USER_ID | QC_RESULTS_REVIEW | USER_NUMBER_ID | No | No | No |  |
| 10 | REC_CREATE_USER_ID | USER_SIDEBAR_RPT | USER_NUMBER_ID | Unknown | No | No |  |
| 10 | REC_CREATE_USER_ID | V_CUBE_D_USER | USER_ID | Unknown | Unknown | No |  |
| 10 | REC_CREATE_USER_ID | V_CUBE_RX_USER | USER_ID | Unknown | Unknown | No |  |
| 14 | ENROLL_ID | ENROLL_INFO | ENROLL_ID | No | No | No |  |
| 14 | ENROLL_ID | LAR_RCVD_DOC | ENROLL_ID | No | No | No |  |

_(150 total; showing first 30)_
