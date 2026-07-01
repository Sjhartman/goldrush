# CHAT_PARTICIPANT

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=CHAT_PARTICIPANT

## Description

Table containing Secure Chat conversation participants.

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
| LINE | INTEGER | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| USER_ID | VARCHAR (18) | The user ID of a user participating in the conversation. |
| USER_MYPT_ID | VARCHAR (18) | The patient access account ID of a patient or proxy in the conversation. |
| USER_ACTIVE_C | INTEGER |  |
| LST_READ_UTC_DTTM | DATETIME (UTC) | The time the participant last read a message in the conversation. The time is used to generate read receipts whenever a user opens up the conversation. |
| UPDATE_INSTANT_DTTM | DATETIME (UTC) | This indicates the time of the last update that the user would be concerned with. |
| LST_READ_MSG_LN | INTEGER | The line number of the message last read by the participant. |
| LST_READ_MSG_DAT | NUMERIC (18,2) | The DAT of the message last read by the participant. |
| READ_ALL_MSG_YN | VARCHAR (1) |  |
| ADDED_FROM_GROUP_YN | VARCHAR (1) |  |
| UNREAD_MESSAGE_CNT | INTEGER | The number of unread messages in the conversation for this user. Used to cache unread message counts. |
| LAST_IMPORTANT_UTC_DTTM | DATETIME (UTC) | This item stores the last unread important message instant; when a message with a higher than normal priority is sent we set this to the time that the message was sent. |
| USER_PRIORITY_C | INTEGER |  |
| LST_REACTION_LN | INTEGER | Line (of TLK 3500 superitem) of last reaction a user has received for one of their messages. |
| LST_REACT_CONTACT_DATE | DATETIME | DAT of last reaction a user has received for one of their messages. |
| LST_REACTION_UTC_DTTM | DATETIME (UTC) | Instant of last reaction a user has received for one of their messages. |
| LATEST_REACTION_SEEN_UTC_DTTM | DATETIME (UTC) | Instant of latest reaction (by anyone to any message) seen by user |
| SHOW_IN_UNREAD_YN | VARCHAR (1) |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | CONVERSATION_ID | CHAT_CONVERSATIONS | CONVERSATION_ID | No | No | No |  |
| 1 | CONVERSATION_ID | CHAT_CONVERSATION_INFO | CONVERSATION_ID | No | No | No |  |
| 3 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 4 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 4 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 4 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 5 | USER_ID | CLARITY_EMP | USER_ID | Unknown | No | No |  |
| 5 | USER_ID | CLARITY_EMP_2 | USER_ID | Unknown | No | No |  |
| 5 | USER_ID | CLARITY_EMP_3 | USER_ID | Unknown | No | No |  |
| 5 | USER_ID | CLARITY_EMP_4 | USER_ID | No | No | No |  |
| 5 | USER_ID | CLARITY_EMP_DEMO | USER_ID | No | No | No |  |
| 5 | USER_ID | EMP_BASIC_INFO | USER_ID | No | No | No |  |
| 5 | USER_ID | EMP_DOC_SETTINGS | USER_NUMBER_ID | No | No | No |  |
| 5 | USER_ID | F_RX_USER | USER_ID | Unknown | Unknown | No |  |
| 5 | USER_ID | IB_MESSAGE_SETTINGS | USER_ID | No | No | No |  |
| 5 | USER_ID | LOGIN_INFO | USER_NUMBER_ID | No | No | No |  |
| 5 | USER_ID | QC_RESULTS_REVIEW | USER_NUMBER_ID | No | No | No |  |
| 5 | USER_ID | USER_SIDEBAR_RPT | USER_NUMBER_ID | Unknown | No | No |  |
| 5 | USER_ID | V_CUBE_D_USER | USER_ID | Unknown | Unknown | No |  |
| 5 | USER_ID | V_CUBE_RX_USER | USER_ID | Unknown | Unknown | No |  |
| 6 | USER_MYPT_ID | MYC_ACCT_DELETION | MYPT_ID | No | No | No |  |
| 6 | USER_MYPT_ID | MYC_MRG_AUD_TRL | MYPT_ID | No | No | No |  |
| 6 | USER_MYPT_ID | MYC_PATIENT | MYPT_ID | No | No | No |  |
| 6 | USER_MYPT_ID | MYC_PATIENT_2 | MYPT_ID | No | No | No |  |
| 6 | USER_MYPT_ID | V_MYC_TEST_PAT | MYPT_ID | Unknown | Unknown | No |  |
| 7 | USER_ACTIVE_C | ZC_USER_ACTIVE | USER_ACTIVE_C | No | No | No |  |
| 16 | USER_PRIORITY_C | ZC_USER_PRIORITY | USER_PRIORITY_C | No | No | No |  |
