# CHAT_MESSAGE_CONTENT

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=CHAT_MESSAGE_CONTENT

## Description

Table for PHI message contents sent in secure chat.

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
| MSG_TEXT | VARCHAR (3500) | Stores the message text for a single secure chat message. Note: It is stored in a super-item, because the super-item global structure is more efficient. No additional items should be added to its super item. |
| MEDIA_DOCUMENT_ID | VARCHAR (18) | This item stores a link to a media record containing information about the media file sent in a Secure Chat message. |
| LINK_CONTENT_TYPE_C | INTEGER |  |
| LINK_REPORT_INFO_ID | NUMERIC (18,0) | The SlicerDicer Session ID linked to in this message. |
| LINK_DASHBOARD_ID | NUMERIC (18,0) | Dashboard ID linked to in this message |
| LINK_ORDER_SESSION_EVENT_ID | VARCHAR (18) | Store the pended order session that is linked to this message in the conversation. |
| LINK_ORDER_SESSION_EVENT_LINE | INTEGER | Store the event line for the pended order session that is linked to this message in the conversation. |
| LINK_RDS_PAT_ENC_CSN_ID | NUMERIC (18,0) | Stores the patient CSN to link the message to the patient in the remote dual sign workflow |
| LINK_PENDING_ADT_EVENT_PEND_ID | VARCHAR (18) | Store the ID for the pending ADT event (PND) that is linked to this message in the conversation. |
| LINK_TRANSFER_CENTER_COMM_ID | NUMERIC (18,0) | Store the ID for the Transfer Center request (NCS) that is linked to this message in the conversation. |
| ORDER_ID | NUMERIC (18,0) | Signed Order linked to in this message. |
| CAPTION_SS | VARCHAR (500) | Caption of the order or saved work linked to this message. |
| DESCRIPTION_SS | VARCHAR (3000) | Description of the order or saved work linked to this message. |
| ORDER_SNAPSHOT_UTC_DTTM | DATETIME (UTC) | The instant at which order data for this message line was current. |
| RECORD_CONTACT | NUMERIC (18,2) | Record contact linked to the chat message |
| LINKED_AUTH_REQUEST_ID | NUMERIC (18,0) | The unique ID of the authorization request (AUG) linked to this conversation. |
| ESCALATION_ID | NUMERIC (18,0) | Chat request linked to this message. |
| LINKED_TREATMENT_PLAN_ID | NUMERIC (18,0) | The unique ID of the treatment plan or therapy plan (TPL) record linked to the message. |
| LINK_PUSH_NOTIF_ID | NUMERIC (18,0) | Contains the ID of the push notification (PNN) record the attachment is related to. |
| LINKED_MOUTH_ID | NUMERIC (18,0) | The unique ID of the patient mouth record linked to the message. |
| LINKED_DENT_PLAN_ID | NUMERIC (18,0) | The unique ID of the dental treatment plan record linked to the message. |
| LINKED_ACTION_C | INTEGER |  |
| SHIFT_BUNDLE_ID | NUMERIC (18,0) | Stores the ID of the Staffing Plan (SHB) linked to the message. |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | CONVERSATION_ID | CHAT_CONVERSATIONS | CONVERSATION_ID | No | No | No |  |
| 1 | CONVERSATION_ID | CHAT_CONVERSATION_INFO | CONVERSATION_ID | No | No | No |  |
| 1 | CONVERSATION_ID | CHAT_CONTACT | CONVERSATION_ID | No | No | No |  |
| 2 | CONTACT_DATE_REAL | CONTACT_DATE_REAL |  |  |  |  |  |
| 6 | MEDIA_DOCUMENT_ID | AWM_IMAGE_DATA | DOCUMENT_ID | No | No | No |  |
| 6 | MEDIA_DOCUMENT_ID | DOC_INFORMATION | DOC_INFO_ID | No | No | No |  |
| 6 | MEDIA_DOCUMENT_ID | DOC_INFORMATION_2 | DOCUMENT_ID | No | No | No |  |
| 6 | MEDIA_DOCUMENT_ID | DOC_INFORMATION_3 | DOCUMENT_ID | No | No | No |  |
| 6 | MEDIA_DOCUMENT_ID | DOC_INFORMATION_4 | DOC_INFO_ID | No | No | No |  |
| 6 | MEDIA_DOCUMENT_ID | DOC_INFO_DICOM | DOCUMENT_ID | No | No | No |  |
| 6 | MEDIA_DOCUMENT_ID | DOC_MC_BROKER_EOP | DOCUMENT_ID | No | No | No |  |
| 6 | MEDIA_DOCUMENT_ID | IMG_ANNOT_SRC | DOCUMENT_ID | No | No | No |  |
| 7 | LINK_CONTENT_TYPE_C | ZC_LINK_CONTENT_TYPE | LINK_CONTENT_TYPE_C | No | No | No |  |
| 8 | LINK_REPORT_INFO_ID | REPORT_INFO | REPORT_INFO_ID | No | No | No |  |
| 8 | LINK_REPORT_INFO_ID | V_REPORT_SETTINGS_FACT | REPORT_INFO_ID | Unknown | Unknown | No |  |
| 9 | LINK_DASHBOARD_ID | DASHBOARD_INFO | DASHBOARD_ID | No | No | No |  |
| 10 | LINK_ORDER_SESSION_EVENT_ID | ED_IEV_PAT_INFO | EVENT_ID | Unknown | No | No |  |
| 10 | LINK_ORDER_SESSION_EVENT_ID | IP_MAR_BARCODE_ITM | EVENT_ID | Unknown | No | No |  |
| 12 | LINK_RDS_PAT_ENC_CSN_ID | ALT_ORD_PROV_SINGL | PAT_ENC_CSN_ID | Unknown | No | No |  |
| 12 | LINK_RDS_PAT_ENC_CSN_ID | AN_RELINK_INFO | PAT_ENC_CSN_ID | No | No | No |  |
| 12 | LINK_RDS_PAT_ENC_CSN_ID | DENT_ORTH_EXAM_NOTES | PAT_ENC_CSN_ID | No | No | No |  |
| 12 | LINK_RDS_PAT_ENC_CSN_ID | FAC_CHG_OVERRIDE | PAT_ENC_CSN_ID | No | No | No |  |
| 12 | LINK_RDS_PAT_ENC_CSN_ID | FAM_HX_PAT_ONLY | PAT_ENC_CSN_ID | No | No | No |  |
| 12 | LINK_RDS_PAT_ENC_CSN_ID | F_ED_ENCOUNTERS | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 12 | LINK_RDS_PAT_ENC_CSN_ID | F_HH_CERT_ATTRIBUTES | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 12 | LINK_RDS_PAT_ENC_CSN_ID | F_HH_OASIS_SINGLE | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 12 | LINK_RDS_PAT_ENC_CSN_ID | F_HH_OASIS_SINGLE_2 | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 12 | LINK_RDS_PAT_ENC_CSN_ID | F_HH_OASIS_SINGLE_3 | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 12 | LINK_RDS_PAT_ENC_CSN_ID | F_HH_OASIS_SINGLE_4 | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 12 | LINK_RDS_PAT_ENC_CSN_ID | F_HH_OASIS_SINGLE_5 | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |

_(264 total; showing first 30)_
