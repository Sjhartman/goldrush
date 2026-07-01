# CHAT_MESSAGE

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=CHAT_MESSAGE

## Description

Table containing Secure Chat message info.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | TLK |
| Release Version | Rel November 2021 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| CONVERSATION_ID | NUMERIC (18,0) | The unique identifier (.1 item) for the secure chat conversation record. |
| CONTACT_DATE_REAL | FLOAT | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| LINE | INTEGER | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| CONTACT_DATE | DATETIME | The date of this contact in calendar format. |
| INST_SENT_UTC_DTTM | DATETIME (UTC) | The instant the message was sent. |
| MESSAGE_TYPE_C | INTEGER |  |
| MESSAGE_PRIORITY_C | INTEGER |  |
| SENDER_USER_ID | VARCHAR (18) | The ID of the user that sent the message. |
| SENDER_MYPT_ID | VARCHAR (18) | The ID of the MyChart user who sent a Secure Chat message. |
| PAT_MESSAGE_ID | VARCHAR (18) | The ID of the MyChart message linked to this Secure Chat message. |
| DESCRIPTION_SS | VARCHAR (3000) | Description of the order or saved work linked to this message |
| MESSAGE_IS_EDITED_YN | VARCHAR (1) |  |
| PRIORITY_CHANGE_REASON_C | INTEGER |  |
| SENDER_LOGIN_DEPARTMENT_ID | NUMERIC (18,0) | This item contains the DEP ID of the department that the user who sent this message was logged into. |
| SENDER_CLIENT_APP_TARGET_C | INTEGER |  |
| INST_SENT_LOCAL_DTTM | DATETIME (Local) | The local instant the message was sent. |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | CONVERSATION_ID | CHAT_CONVERSATIONS | CONVERSATION_ID | No | No | No |  |
| 1 | CONVERSATION_ID | CHAT_CONVERSATION_INFO | CONVERSATION_ID | No | No | No |  |
| 1 | CONVERSATION_ID | CHAT_CONTACT | CONVERSATION_ID | No | No | No |  |
| 2 | CONTACT_DATE_REAL | CONTACT_DATE_REAL |  |  |  |  |  |
| 6 | MESSAGE_TYPE_C | ZC_CHAT_MESSAGE_TYPE | CHAT_MESSAGE_TYPE_C | No | No | No |  |
| 7 | MESSAGE_PRIORITY_C | ZC_USER_PRIORITY | USER_PRIORITY_C | No | No | No |  |
| 8 | SENDER_USER_ID | CLARITY_EMP | USER_ID | Unknown | No | No |  |
| 8 | SENDER_USER_ID | CLARITY_EMP_2 | USER_ID | Unknown | No | No |  |
| 8 | SENDER_USER_ID | CLARITY_EMP_3 | USER_ID | Unknown | No | No |  |
| 8 | SENDER_USER_ID | CLARITY_EMP_4 | USER_ID | No | No | No |  |
| 8 | SENDER_USER_ID | CLARITY_EMP_DEMO | USER_ID | No | No | No |  |
| 8 | SENDER_USER_ID | EMP_BASIC_INFO | USER_ID | No | No | No |  |
| 8 | SENDER_USER_ID | EMP_DOC_SETTINGS | USER_NUMBER_ID | No | No | No |  |
| 8 | SENDER_USER_ID | F_RX_USER | USER_ID | Unknown | Unknown | No |  |
| 8 | SENDER_USER_ID | IB_MESSAGE_SETTINGS | USER_ID | No | No | No |  |
| 8 | SENDER_USER_ID | LOGIN_INFO | USER_NUMBER_ID | No | No | No |  |
| 8 | SENDER_USER_ID | QC_RESULTS_REVIEW | USER_NUMBER_ID | No | No | No |  |
| 8 | SENDER_USER_ID | USER_SIDEBAR_RPT | USER_NUMBER_ID | Unknown | No | No |  |
| 8 | SENDER_USER_ID | V_CUBE_D_USER | USER_ID | Unknown | Unknown | No |  |
| 8 | SENDER_USER_ID | V_CUBE_RX_USER | USER_ID | Unknown | Unknown | No |  |
| 9 | SENDER_MYPT_ID | MYC_ACCT_DELETION | MYPT_ID | No | No | No |  |
| 9 | SENDER_MYPT_ID | MYC_MRG_AUD_TRL | MYPT_ID | No | No | No |  |
| 9 | SENDER_MYPT_ID | MYC_PATIENT | MYPT_ID | No | No | No |  |
| 9 | SENDER_MYPT_ID | MYC_PATIENT_2 | MYPT_ID | No | No | No |  |
| 9 | SENDER_MYPT_ID | V_MYC_TEST_PAT | MYPT_ID | Unknown | Unknown | No |  |
| 10 | PAT_MESSAGE_ID | MYC_MESG | MESSAGE_ID | Unknown | No | No |  |
| 10 | PAT_MESSAGE_ID | MYC_MESG_FRST_LAST | MESSAGE_ID | Unknown | Unknown | No |  |
| 10 | PAT_MESSAGE_ID | V_MYC_MESG | MESSAGE_ID | Unknown | Unknown | No |  |
| 13 | PRIORITY_CHANGE_REASON_C | ZC_PRIORITY_CHANGE_REASON | PRIORITY_CHANGE_REASON_C | No | No | No |  |
| 14 | SENDER_LOGIN_DEPARTMENT_ID | BH_DEP | DEPARTMENT_ID | No | No | No |  |

_(48 total; showing first 30)_
