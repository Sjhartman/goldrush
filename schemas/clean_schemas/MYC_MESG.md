# MYC_MESG

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=MYC_MESG

## Description

This table contains information on messages sent to and from web-based chart system patients.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | WMG |
| Release Version | EPIC 2002 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| MESSAGE_ID | VARCHAR (18) | The unique ID used to identify a web-based chart system message record. A new record is created each time a patient sends a message from a web-based chart system to a system user and each time a system user sends a message to a web-based chart system patient. |
| CREATED_TIME | DATETIME (Local) | The date and time the web-based chart system message record was created in local time. |
| MYC_MSG_TYP_C | VARCHAR (66) |  |
| PARENT_MESSAGE_ID | VARCHAR (18) | The unique ID of the original message in a chain of web-based chart system messages between patients and system users. |
| INBASKET_MSG_ID | VARCHAR (18) | The unique ID of the system message associated with the web-based chart system message. An example is when a patient sends a message to a system user. |
| PAT_ID | VARCHAR (18) | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| PAT_ENC_DATE_REAL | No | A unique, internal contact date in decimal format. The integer portion of the number indicates the date of the contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| FROM_USER_ID | VARCHAR (18) | The unique ID of the system user who sent a web-based chart system message to a patient. |
| TO_USER_ID | VARCHAR (18) | The unique ID of the system user who was sent a web-based chart system message from a patient. |
| TOFROM_PAT_C | INTEGER |  |
| NOTALLOW_REPLY_YN | VARCHAR (1) |  |
| REPLY_DIRECT_YN | VARCHAR (1) |  |
| ORIGINAL_TO | VARCHAR (40) | If a message sent from a web-based chart system patient is re-routed from its intended destination, then the ID of the original recipient is stored in the field. Most commonly this occurs when a system user does not accept messages directly from web-based chart system patients. In this case, the message will be re-routed to a pool, but the employee ID of the system user will be stored here. The ID of the final destination is stored in MODIFIED_TO. |
| MODIFIED_TO *(deprecated)* | VARCHAR (40) |  |
| RQSTD_PHARMACY_ID | NUMERIC (18,0) | The unique ID of the pharmacy selected by the patient from the drop down list when sending a Medication Renewal Request message. |
| SMTP_SENT_TIME *(deprecated)* | DATETIME | This column is deprecated and does not extract any data. The item for which this column was created is no longer in use. To determine the SMTP sent time, use MYC_INST_SMTP_TM in the PAT_MYC_SMTP_MSG table. |
| SMTP_EMAIL *(deprecated)* | VARCHAR (255) | This column is deprecated and does not extract any data. The item for which this column was created is no longer in use. To determine the SMTP sent time, use MYC_SMTP_MSG_EMAIL in the PAT_MYC_SMTP_MSG table. |
| SMTP_RESULT_CODE *(deprecated)* | VARCHAR (255) | This column is deprecated and does not extract any data. The item for which this column was created is no longer in use. To determine the SMTP sent time, use MYC_SMTP_MSG_CODE in the PAT_MYC_SMTP_MSG table. |
| SMTP_RESPONSE *(deprecated)* | VARCHAR (255) | This column is deprecated and does not extract any data. The item for which this column was created is no longer in use. To determine the SMTP sent time, use MYC_SMTP_MSG_RESP in the PAT_MYC_SMTP_MSG table. |
| PROXY_PAT_ID | VARCHAR (18) | The unique ID of the Proxy patient who sent the message. This is populated only if the message was sent by one patient (the Proxy) on behalf of another patient. |
| UPDATE_DATE | No | The date and time that this web-based chart system message record was pulled into enterprise reporting. |
| REQUEST_SUBJECT | VARCHAR (255) | This field is only used for medical advice request messages and indicates the subject selected by the patient from the drop down list. |
| PROV_ID | VARCHAR (18) | The provider that was used in routing the patient access message. The provider may vary depending on message type. |
| DEPARTMENT_ID | NUMERIC (18,0) | The department used in routing the patient access message. The department may vary depending on message type. |
| RESP_METH_C | INTEGER |  |
| RESP_INFO | VARCHAR (255) | Some response types will include additional information, such as a phone number.  If such data exists for the chosen response method, it will be stored in this field. |
| SUBJECT | VARCHAR (255) | The subject line of the web-based chart system message. |
| CONFIDENTIAL_YN | VARCHAR (254) |  |
| PAT_OWNER_ID | VARCHAR (18) | The unique ID of the patient who marked this message as confidential. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| PAT_ENC_CSN_ID | NUMERIC (18,0) | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| NOT_HANDLED_TIME | DATETIME (Attached) | When messages are being tracked/handled, this item will have the creation instant. Having a value in this item means that it has not been handled yet.  When it has been handled, this value will be deleted and MYC_MESG.FINAL_HANDLED_TIME will be set. |
| FINAL_HANDLED_TIME | DATETIME (Local) | When messages are being tracked/handled, this item will have the handled instant. Having a value in this item means that the message has been handled.  Prior to being handled, this item will not have a value and MYC_MESG.NOT_HANDLED_TIME will be set to the creation timestamp. To determine how long it took for a message to be handled, calculate the difference between MYC_MESG.CREATED_TIME and MYC_MESG.FINAL_HANDLED_TIME |
| FINAL_AUDIT_LINE | INTEGER | When messages are being tracked/handled, MYC_MESG.FINAL_HANDLED_TIME will have the handled instant.  MYC_MESG.FINAL_AUDIT_LINE will have the line pointer into the audit trail table (MYC_MESG_AUDIT) for the line row that caused the message to be final handled. Prior to being handled, this item will not have a value and MYC_MESG.NOT_HANDLED_TIME will be set to the creation timestamp. |
| TARGET_DEPL_ID | VARCHAR (25) | The unique ID of the deployment where this web-based chart system message was originally routed. Used for cross-deployment messaging. |
| EOW_READ_STATUS_C | INTEGER |  |
| BILL_ACCT_ID | NUMERIC (18,0) | The unique ID of the guarantor account associated with this web-based chart system message. |
| BILL_ACCT_TYPE_C | INTEGER |  |
| BILL_ACCT_HAR_ID | NUMERIC (18,0) | The unique ID of the hospital account associated with this web-based chart system message. |
| RELATED_MESSAGE_ID | VARCHAR (18) | The unique ID of the parent message of the original message chain. This applies only when the system is configured to allow patients to reply to messages associated with closed encounters by creating a new message chain. This item is populated for the message that starts a new chain. |
| PROXY_WPR_ID | VARCHAR (18) | The unique ID of the web-based chart system proxy patient associated with this message. |
| WPR_OWNER_WPR_ID | VARCHAR (18) | The unique ID of the web-based chart system patient who owns this message. |
| CR_TX_CARD_ID | NUMERIC (18,0) | The unique ID of the credit card used for this transaction. |
| CR_TX_MERCHANT_ID | NUMERIC (18,0) | The unique ID of the credit card merchant used to process this transaction. |
| CR_TX_MYPT_ID | VARCHAR (18) | The unique ID of the web-based chart system patient associated with this transaction. |
| CR_TX_AMOUNT_AUTH | NUMERIC (18,2) | The amount authorized for this transaction. |
| INCL_VIEWERS_C | INTEGER |  |
| PAT_HX_QUESR_ID | VARCHAR (18) | The unique ID of the history questionnaire associated with this message. |
| HX_QUESR_CONTEXT_C | INTEGER |  |
| HX_QUESR_PROV_ID | VARCHAR (18) | The unique ID of the provider associated with the questionnaire. |
| HX_QUESR_ENCPROV_ID | VARCHAR (18) | The unique ID of the provider associated with the appointment that the questionnaire is linked to. |
| HX_QUESR_APPT_DAT | INTEGER | The appointment contact date (DAT) if the questionnaire is linked to an appointment. |
| HX_QUESR_FILED_YN | VARCHAR (1) |  |
| DELIVERY_DTTM | DATETIME (UTC) | The instant that this message is scheduled for delivery to the patient. This item may not be populated. In the event that this item is not populated, then the instant the message is created is used to determine when the patient can view the message. |
| RECORD_STATUS_C | INTEGER |  |
| OUTBOX_PAT_ID | VARCHAR (18) | The ID of the patient receiving a message. |
| INBOX_PAT_ID | VARCHAR (18) | The ID of the patient receiving a message. |
| INST_UPD_DTTM | DATETIME (Local) | The date and time when the message was updated. |
| CR_TX_TYPE_C | INTEGER |  |
| HX_QUESR_REVIEW_YN | VARCHAR (1) |  |
| QUESR_ANS_METHOD_ID | NUMERIC (18,0) | Stores how the questionnaire answers were submitted (e.g. MyChart, Welcome). |
| HX_QUESR_ENC_CSN_ID | NUMERIC (18,0) | The unique contact serial number for the appt contact if questionnaire is linked to an appt. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| OUTREACH_RUN_ID | NUMERIC (18,0) | This is the campaign outreach configuration template associated with this message. |
| RENEWAL_REQ_SRC_C | INTEGER |  |
| REQ_PHARM_FREE_TEXT | VARCHAR (508) | If the selected pharmacy was entered by the user as free-text, then it is stored here. |
| UNREAD_NOTIF_UTC_DTTM | DATETIME (UTC) | When to notify the sender if the patient hasn't read this message |
| UNREAD_NOTIF_HX_UTC_DTTM | DATETIME (UTC) | Stores the Unread Notification Instant for historical and display purposes |
| FRM_PAT_TO_NAME | VARCHAR (255) | Stores a display name that indicates the user's intention when they sent this message |
| TO_PAT_FRM_NAME | VARCHAR (255) | Stores the display name of the sender when the message is sent to the patient. It is only used by imported messages. |
| FIN_ASST_TRACKER_ID | NUMERIC (18,0) | The ID of the Social Care decision (I FNT .1) associated with this patient message. |
| HX_QUESR_EDIT_MYPT_ID | VARCHAR (18) | Stores the Patient Access Account (WPR) record for the user who last made changes to an in progress history questionnaire |
| HX_QUESR_EDIT_INST_DTTM | DATETIME (UTC) | Stores the time at which changes were last made to an in progress history questionnaire |
| BUSINESS_DAYS_TO_HANDLE | INTEGER | Stores the number of business days it took to handle this message. It is calculated by getting the date when the message was created and the date when the message was handled and finding the number of business days between those two dates. This is not updated when the list of holidays is updated and represents a snapshot of the difference when the message was handled. |
| IS_AUTO_YN | VARCHAR (1) |  |
| REFERRAL_ID | NUMERIC (18,0) | The unique ID of the referral this message is associated with. |
| COMM_ID | NUMERIC (18,0) | The customer service record ID corresponding to the message |
| AUTH_REQUEST_ID | NUMERIC (18,0) | The authorization request this message is associated with. |
| INFO_REQ_CSN_ID | NUMERIC (18,0) | The Information Request this message is associated with. |
| NON_HX_QUESR_WITH_HX_DATA_YN | VARCHAR (1) |  |
| MSG_FORALL_AUTHOR_YN | VARCHAR (1) |  |
| OUTREACH_CSN_ID | NUMERIC (18,0) | The unique contact serial number (CSN) of the outreach contact that sent the message. |
| PAT_DTREE_ANSWER_ID | VARCHAR (18) | HQA ID for storing the decision tree answer record. |
| HX_QUESR_FILED_USER_ID | VARCHAR (18) | The ID of the user who marked the history submission as done. |
| HX_QUESR_FILED_LOCAL_DTTM | DATETIME (Local) | The instant (in local time) that the history questionnaire submission was marked as done. |
| BDSD_UPDATE_TAG_C | INTEGER |  |
| MESG_SOURCE_WORKFLOW_C | INTEGER |  |
| CHARACTER_CNT | INTEGER | The character count of the message body. |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | MESSAGE_ID | MYC_MESG_FRST_LAST | MESSAGE_ID | Unknown | Unknown | No |  |
| 1 | MESSAGE_ID | V_MYC_MESG | MESSAGE_ID | Unknown | Unknown | No |  |
| 3 | MYC_MSG_TYP_C | ZC_MYC_MSG_TYP | MYC_MSG_TYP_C | No | No | No |  |
| 4 | PARENT_MESSAGE_ID | MYC_MESG | MESSAGE_ID | Unknown | No | No |  |
| 4 | PARENT_MESSAGE_ID | MYC_MESG_FRST_LAST | MESSAGE_ID | Unknown | Unknown | No |  |
| 4 | PARENT_MESSAGE_ID | V_MYC_MESG | MESSAGE_ID | Unknown | Unknown | No |  |
| 5 | INBASKET_MSG_ID | IB_MESSAGES | MSG_ID | No | No | No |  |
| 5 | INBASKET_MSG_ID | IB_MESSAGES_2 | MSG_ID | No | No | No |  |
| 5 | INBASKET_MSG_ID | IB_MESSAGES_3 | MSG_ID | No | No | No |  |
| 5 | INBASKET_MSG_ID | IB_MESSAGES_4 | MSG_ID | No | No | No |  |
| 5 | INBASKET_MSG_ID | IB_MESSAGES_5 | MSG_ID | No | No | No |  |
| 5 | INBASKET_MSG_ID | IB_SMART_ROUTE_MESSAGE | MSG_ID | No | No | No |  |
| 5 | INBASKET_MSG_ID | MYC_IB_MESSAGES | MSG_ID | No | No | No |  |
| 5 | INBASKET_MSG_ID | PROC_CHG_REQUEST | MSG_ID | No | No | No |  |
| 5 | INBASKET_MSG_ID | V_ECL_NAR_TURNAROUND | MSG_ID | Unknown | Unknown | No |  |
| 5 | INBASKET_MSG_ID | V_ECL_STADM_NAR_TURNAROUND | MSG_ID | Unknown | Unknown | No |  |
| 5 | INBASKET_MSG_ID | V_OR_TIME_REQ_MSG_METRICS | MSG_ID | Unknown | Unknown | No |  |
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

_(646 total; showing first 30)_
