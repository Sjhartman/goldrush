# CL_QANSWER_QA

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=CL_QANSWER_QA

## Description

This table contains the questions and answers for questionnaire answer records. It also includes audit information such as when the question was answered and by whom.

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
| LINE | No | Line count of the answers in the questionnaire record. |
| QUEST_ID | VARCHAR (18) | The unique ID of the question for this record. |
| QUEST_DAT | No | Holds the date this response was entered into the system.  Source: HQA 110  NOTE: This should not be used to join to the overtime questions table (e.g. CL_QQUEST_OVTM). Rather, use the foreign key comprised of the QUEST_ID and QUEST_DATE_REAL columns to join to those tables. |
| QUEST_ANSWER | VARCHAR (2000) | The answer to the question for this record.   For answers to questions of the networked or category response type, use the VARCHAR_ANSWER or NUMERIC_ANSWER columns to see the raw record or category IDs.  To use this column as a number in a calculation, use FLOAT_ANSWER.  To use this column as a datetime, use DATETIME_ANSWER.  To use this column as a time, use TIME_ANSWER. |
| QUEST_COMMENT | VARCHAR (2000) | The comment for the question for this record. |
| QUEST_LINE_NUM | INTEGER | The line number for the question for this record. |
| QUEST_EDIT_USER_ID | VARCHAR (18) | The unique ID of the user associated with this record. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| QUESTION_INSTANT | DATETIME (Local) | Stores the instant a question was answered. |
| QUEST_DATE_REAL | FLOAT | The unique, internal contact date of the associated question record in decimal format. The integer portion of the number indicates the date of the question record contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. Along with QUEST_ID, this forms the foreign key to overtime question tables (e.g. CL_QQUEST_OVTM). |
| VARCHAR_ANSWER | No | For questions of networked or category response types where the linked INI and item is string (aka varchar) based, this column will hold either a record ID or category ID. These are useful for linking directly to other tables such as CLARITY_SER for provider-linked questions, or ZC tables for category response types.   If you are unsure what types of records these IDs hold, consult CL_QQUEST_OVTM for the question ID in the QUEST_ID column and use the RESP_INI and RESP_ITEM columns. |
| NUMERIC_ANSWER | No | For questions of networked or category response types where the linked INI and item is numeric (integer) based, this column holds either a record ID or category ID. |
| FLOAT_ANSWER | No | The answer to the question for this record converted into a floating point value. |
| IS_NULL | No | Specifies if there was no response to a question (set to 1 - Yes). |
| QUESTION_SDI | VARCHAR (50) | The SmartData identifier of the SmartData element that this patient-entered custom history question uses. |
| QUESN_SDI_FILED_YN | VARCHAR (1) |  |
| DATETIME_ANSWER | No | Stores questionnaire answer data in a datetime format that includes hours and seconds. |
| TIME_ANSWER | No | The answer to the question for this record, formatted as a time value. This is the preferred column for reporting on answers to questions with the response type (LQL 110) of 3-Time.  Source: HQA 120 |
| SCORE_STD_ERR | NUMERIC (18,4) | The standard error on the score calculated by the computerized adaptive testing (CAT) algorithm |
| DOC_INFO_ID | VARCHAR (18) | The unique identifier of a document uploaded for a question. |
| SCORING_METHOD_C | INTEGER |  |
| FOL_UP_PAR_QUEST_ID | VARCHAR (18) | The question ID (LQL) of the parent question for which this follow-up question is answered. |
| PAT_LOC_DOC_ID | VARCHAR (18) | Stores the ID of the drawing record (DCS) submitted by the patient in the locale in which he answered the question if the locale is different from the base locale. |
| ANSWER_SEVERITY_C | INTEGER |  |
| ANSWER_DISPLAY_NAME | VARCHAR (250) | Virtual item. This item only has data for networked question answers. For networked question answers, this displays the name of the networked record selected by the user at the time the answer was made. |
| DYNAMIC_QUEST_ENTITY_ID | NUMERIC (18,0) | The ID of the DQE record this question is related to |
| QUEST_INITIAL_ANSWER | VARCHAR (2000) | Contains the pre-populated answer for the question if one is available. |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| B-TREE INDEX | EIX_QANSWER_QA_INST | QUESTION_INSTANT | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_QANSWER_QA_IS_NULL | IS_NULL | 1 | Yes | Yes |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ANSWER_ID | CL_QANSWER | ANSWER_ID | Unknown | No | No |  |
| 1 | ANSWER_ID | DTREE_ANSWER | DTREE_ANSWER_ID | No | No | No |  |
| 1 | ANSWER_ID | V_SELF_TRIAGE_STATS | DTREE_ANSWER_ID | Unknown | Unknown | No |  |
| 3 | QUEST_ID | CL_QQUEST | QUEST_ID | No | No | No |  |
| 3 | QUEST_ID | CL_QQUEST_OVTM | QUEST_ID | Unknown | Unknown | Yes |  |
| 8 | QUEST_EDIT_USER_ID | CLARITY_EMP | USER_ID | Unknown | No | No |  |
| 8 | QUEST_EDIT_USER_ID | CLARITY_EMP_2 | USER_ID | Unknown | No | No |  |
| 8 | QUEST_EDIT_USER_ID | CLARITY_EMP_3 | USER_ID | Unknown | No | No |  |
| 8 | QUEST_EDIT_USER_ID | CLARITY_EMP_4 | USER_ID | No | No | No |  |
| 8 | QUEST_EDIT_USER_ID | CLARITY_EMP_DEMO | USER_ID | No | No | No |  |
| 8 | QUEST_EDIT_USER_ID | EMP_BASIC_INFO | USER_ID | No | No | No |  |
| 8 | QUEST_EDIT_USER_ID | EMP_DOC_SETTINGS | USER_NUMBER_ID | No | No | No |  |
| 8 | QUEST_EDIT_USER_ID | F_RX_USER | USER_ID | Unknown | Unknown | No |  |
| 8 | QUEST_EDIT_USER_ID | IB_MESSAGE_SETTINGS | USER_ID | No | No | No |  |
| 8 | QUEST_EDIT_USER_ID | LOGIN_INFO | USER_NUMBER_ID | No | No | No |  |
| 8 | QUEST_EDIT_USER_ID | QC_RESULTS_REVIEW | USER_NUMBER_ID | No | No | No |  |
| 8 | QUEST_EDIT_USER_ID | USER_SIDEBAR_RPT | USER_NUMBER_ID | Unknown | No | No |  |
| 8 | QUEST_EDIT_USER_ID | V_CUBE_D_USER | USER_ID | Unknown | Unknown | No |  |
| 8 | QUEST_EDIT_USER_ID | V_CUBE_RX_USER | USER_ID | Unknown | Unknown | No |  |
| 9 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 9 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 9 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 10 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 10 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 10 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 12 | QUEST_DATE_REAL | CL_QQUEST_OVTM | CONTACT_DATE_REAL | Unknown | Unknown | Yes |  |
| 22 | DOC_INFO_ID | AWM_IMAGE_DATA | DOCUMENT_ID | No | No | No |  |
| 22 | DOC_INFO_ID | DOC_INFORMATION | DOC_INFO_ID | No | No | No |  |
| 22 | DOC_INFO_ID | DOC_INFORMATION_2 | DOCUMENT_ID | No | No | No |  |
| 22 | DOC_INFO_ID | DOC_INFORMATION_3 | DOCUMENT_ID | No | No | No |  |

_(46 total; showing first 30)_
