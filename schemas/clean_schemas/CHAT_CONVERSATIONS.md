# CHAT_CONVERSATIONS

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=CHAT_CONVERSATIONS

## Description

Table containing Secure Chat conversation level items.

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
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| RECORD_NAME *(deprecated)* | VARCHAR (200) | *** Deprecated *** In table CHAT_CONVERSATIONS, the column RECORD_NAME (TLK/.2) has been deprecated. The deprecated column's content/data is no longer available since it is no longer populated in Chronicles. ****** Record name |
| RECORD_STATUS_C | INTEGER |  |
| LST_UPDATE_UTC_DTTM | DATETIME (UTC) | The instant the newest message in the conversation was sent. |
| PURGE_MESSAGE_UTC_DTTM | DATETIME (UTC) | All messages in this conversation sent before this instant should be purged. |
| PAT_ID | VARCHAR (18) | The ID of the patient linked to the conversation. |
| RECORD_CREATION_DATE | DATETIME | Stores the date the record was created |
| INSTANT_OF_UPDATE_DTTM | DATETIME (Local) | Stores the instant the record was last locked/unlocked |
| CONVERSATION_TYPE_C | INTEGER |  |
| PAT_ENC_CSN_ID | NUMERIC (18,0) | The contact serial number (CSN) of the patient encounter associated with this conversation. This item will only be populated for Bedside patient-facing conversations. A value here means the conversation may include a patient or their proxies. |
| PAT_CONVERSATION_THREAD_ID | NUMERIC (18,0) | The ID of the MyChart conversation linked to this Secure Chat conversation. |
| CHAT_CONTEXT_TYPE_C | INTEGER |  |
| LINKED_PUSH_NOTIF_ID | NUMERIC (18,0) | Linked PNN (push notification) record ID to the TLK record that provides additional context about the conversation. |
| ORIGINAL_GROUP_ID | NUMERIC (18,0) | Stores TGR ID of the original group that received a Secure Chat. Used for starting and continuing conversations with additional context with this group. |
| BROADCAST_DEF_ID | NUMERIC (18,0) | A link to the IDT "Broadcast Message" definition. This allows for integration with Cogito/Radar's broadcasts by linking TLK to IDT. It also allows Secure Chat to make use of some IDT items. |
| ACTIVE_ESCALATION_ID | NUMERIC (18,0) | The active Chat Request for the conversation, if applicable. |
| CREATED_BY_USER_ID | VARCHAR (18) | Stores the ID of the user that created this conversation. |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | CONVERSATION_ID | CHAT_CONVERSATION_INFO | CONVERSATION_ID | No | No | No |  |
| 2 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 2 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 2 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 3 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 5 | RECORD_STATUS_C | ZC_RECORD_STATUS_2 | RECORD_STATUS_2_C | No | No | No |  |
| 5 | RECORD_STATUS_C | ZC_RECORD_STS | RECORD_STS_C | No | No | No |  |
| 8 | PAT_ID | ANTICOAG_SELF_REGULATING | PAT_ID | No | No | No |  |
| 8 | PAT_ID | CARE_COORDINATION | PAT_ID | Unknown | No | No |  |
| 8 | PAT_ID | CLAIMS_DERIVE_PAT_FLAGS | PAT_ID | No | No | No |  |
| 8 | PAT_ID | COMMUNITY_RESRC_REVIEWED | PAT_ID | No | No | No |  |
| 8 | PAT_ID | D_PAT_GEOGRAPHIC_CLASS | PAT_ID | Unknown | Unknown | No |  |
| 8 | PAT_ID | EPT_MEM_INFO | PAT_ID | No | No | No |  |
| 8 | PAT_ID | EXT_DATA_LAST_DONE | PAT_ID | No | No | No |  |
| 8 | PAT_ID | F_IBD_ADULT_FORM_PAT | PAT_ID | Unknown | Unknown | No |  |
| 8 | PAT_ID | HH_PAT_INFO | PAT_ID | Unknown | No | No |  |
| 8 | PAT_ID | HM_STATUS_UPD | PAT_ID | No | No | No |  |
| 8 | PAT_ID | IMMNZTN_LAST_REVIEW | PAT_ID | No | No | No |  |
| 8 | PAT_ID | PATIENT | PAT_ID | No | No | No |  |
| 8 | PAT_ID | PATIENT_2 | PAT_ID | No | No | No |  |
| 8 | PAT_ID | PATIENT_3 | PAT_ID | No | No | No |  |
| 8 | PAT_ID | PATIENT_4 | PAT_ID | No | No | No |  |
| 8 | PAT_ID | PATIENT_5 | PAT_ID | No | No | No |  |
| 8 | PAT_ID | PATIENT_6 | PAT_ID | No | No | No |  |
| 8 | PAT_ID | PATIENT_CONF_ADDR | PAT_ID | No | No | No |  |
| 8 | PAT_ID | PATIENT_MISC_COMMENTS | PAT_ID | No | No | No |  |
| 8 | PAT_ID | PATIENT_MYC | PAT_ID | Unknown | No | No |  |
| 8 | PAT_ID | PATIENT_OPT | PAT_ID | No | No | No |  |

_(183 total; showing first 30)_
