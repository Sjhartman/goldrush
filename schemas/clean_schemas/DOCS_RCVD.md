# DOCS_RCVD

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=DOCS_RCVD

## Description

High level information about received documents.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | DXR |
| Release Version | SPRING 2007 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| DOCUMENT_ID | NUMERIC (22,0) | This item stores the Received Document record ID. |
| CM_PHY_OWNER_ID | VARCHAR (25) | Physical owner item |
| CM_LOG_OWNER_ID | VARCHAR (25) | Logical Owner Item |
| TYPE_C | INTEGER |  |
| PAT_ID | VARCHAR (18) | The unique ID of the patient for this received document. |
| DOC_SOURCE_ORG_ID | NUMERIC (18,0) | Source organization record for this document |
| DOC_SET | VARCHAR (308) | Specifies the Set ID for these documents. |
| ENC_EVENT_IDENT | VARCHAR (308) | The event identifier for the event contained in this document. Applies only to Encounter Summary records. |
| AUTHOR_INST_ID | NUMERIC (18,0) | Specifies the Author Institution that created the document. |
| REPOSITORY_ID | VARCHAR (85) | The unique ID of the repository holding the received document. |
| INVLD_REASON_C | INTEGER |  |
| DUPL_OF_REC_ID | NUMERIC (22,0) | If the invalidation reason is Duplicate Resolution, this item stores the record identifier of the primary duplicate record. |
| INVLD_INSTANT_TM | DATETIME (Local) | This item stores the instant this received document was invalidated. |
| DOCUMENT_FILE_NAME | VARCHAR (128) | Stores the file name for the document on the BLOB server |
| SENDER_REFERRALID | VARCHAR (192) | This item stores the referral ID for Care Everywhere Referral-type external document records as received from the outside organization. The format is OID^ID, where the ID is usually a record ID at the outside organization. |
| SENDER_LETTERID | VARCHAR (192) | This item stores the letter ID for the Letter stored in this DXR record as received from the outside organization. The format is OID^ID, where the ID is usually a record ID at the outside organization. |
| PHR_ID | NUMERIC (18,0) | The unique ID of the pharmacy that sent this received document. |
| EXT_MED_CONTEXT_C | INTEGER |  |
| DOC_CONTENT_TYPE_C | INTEGER |  |
| EXTERNAL_EPT_CSN | NUMERIC (22,0) | For received documents from external systems that Epic rehosts, this stores the patient encounter Contact Serial Number (CSN). |
| REHOSTED_DOC_YN | VARCHAR (1) |  |
| ATTACHED_DOC_ID | VARCHAR (18) | This item stores the ID of the document record, which contains the attached document that was received. |
| MEDCOM_TYPE_C | INTEGER |  |
| EPISODE_UUID | VARCHAR (36) | Stores a UUID identifying an episode of care |
| RECORD_STATE_C | INTEGER |  |
| DOC_EPSD_IDENT | VARCHAR (100) | The episode identifier of the episode contained in this document. |
| INVLD_USER_ID | VARCHAR (18) | The unique ID of the user that invalidated this received document. |
| SOURCE_CLAIM_ID | NUMERIC (18,0) | Stores the linked claim record that the information in this DXR record was derived from |
| INVLD_RLS_CONV_IDENT | VARCHAR (32) | The unique identifier of the release conversion that invalidated this document. Only populated in rows where the invalidation reason (INVLD_REASON_C) is 19 (representing Release Conversion). |
| INVLD_UNLINK_REASON_C | INTEGER |  |
| DOC_CONTENT_TYPE | VARCHAR (508) | This is the type of document stored in the record. For Care Everywhere Encounter Summaries, this is the type of encounter stored in this record. |
| CAN_HAVE_RESTRICTED_ENC_YN | VARCHAR (1) |  |
| EXT_MED_PBM_IDENT | VARCHAR (91) | This item stores the PBM ID for the patient. |
| RECEIVED_CLINICAL_NOTE_ID | VARCHAR (254) | The ID of the note record automatically created in the local chart from the received clinical note information. |
| AMBIENT_EXTERNAL_CLIENT | VARCHAR (40) | Stores the ambient recording session's external vendor client ID |
| RX_DOC_LEGACY_KEY | VARCHAR (50) | Legacy Pharmacy Patient Identifier. Used in Legacy Pharmacy Patient DXR records to determine which patient record in the legacy system the data originated from. Information is formatted using the record ID of the Patient ID type and patient identifier. If an exact match is found in a subsequent import, the data in this record is overwritten. If an exact match is not found, a new DXR for the patient is created. |
| RX_DOCUMENT_STATUS_C | INTEGER |  |
| COVERAGE_ID | NUMERIC (18,0) | This item stores the CVG ID for which document is being requested. |
| RESEARCH_ID | VARCHAR (18) | The unique identifier (.1 item) for the Research Study Record |
| PNR_PARENT_DOCUMENT_ID | NUMERIC (22,0) | Stores the parent PNR Document List ID in cases where this DXR is a child that was split out of the parent. |
| DATA_ORIG_SRC_ORGANIZATION_ID | NUMERIC (18,0) | This item is set for documents that contain data that was forwarded from an organization external to the source organization in I DXR 70. This is used by Cosmos and Payor Platform to identify the source of unreconciled data. |
| RX_TRANSFER_STATUS_C | INTEGER |  |
| RX_TRANSFER_TO_PHARMACY_ID | NUMERIC (18,0) | This item is used during electronic prescription transfers between two pharmacies. This is the pharmacy the prescription was transferred to. |
| RX_TRANSFER_FROM_PHARMACY_ID | NUMERIC (18,0) | This item is used during electronic prescription transfers between two pharmacies. This is the pharmacy the prescription was transferred from. |
| RX_TRANSFER_TO_USER_ID | VARCHAR (18) | This item is used during electronic prescription transfers between two pharmacies. This is the user for the transfer to pharmacy that authorized the transfer. |
| RX_TRANSFER_FROM_USER_NAME | VARCHAR (254) | This item is used during electronic prescription transfers between two pharmacies. This is the user for the transfer from pharmacy that authorized the transfer. |
| RX_TRANSFER_COMMENTS | VARCHAR (254) | This item is used during electronic prescription transfers between two pharmacies. This contains the comments associated with the transfer. |
| RX_TRANSFER_REQ_DOCUMENT_ID | NUMERIC (22,0) | The electronic prescription transfer request document associated with this electrionc prescription transfer response. |
| AMBNT_RECORD_START_UTC_DTTM | DATETIME (UTC) | The UTC date and time that the first recording was started for an Ambient session. |
| AMBNT_FLOWSHEET_FILED_UTC_DTTM | DATETIME (UTC) | The UTC date and time that Flowsheet data associated with an Ambient session was most recently filed. |
| DATA_ORIG_SRC_ORG_NAME | VARCHAR (100) | Name of the original source organization in a document containing unreconciled data. Only populated when the original source organization could not be mapped to a value in DATA_ORIG_SRC_ORGANIZATION_ID. |
| DATA_ORIG_SRC_ORG_IDENTIFIER | VARCHAR (100) | Unique ID to identify the original source organization in a document containing unreconciled data. Only populated when the original source organization could not be mapped to a value in DATA_ORIG_SRC_ORGANIZATION_ID. |
| EXT_DEMOG_ID | NUMERIC (18,0) | Holds a pointer to the REQ record that holds the identifier and demographics that this external document was loaded with, linking this external document data record to an ID bundle. |
| AMBNT_DD_FILED_UTC_DTTM | DATETIME (UTC) | The UTC instant that discrete data associated with an Ambient session was most recently filed. |
| CONVERSATION_IDENT | VARCHAR (100) | Stores an identifier to associate this document with a specific conversation |
| RFL_NOTE_EXTERNAL_IDENT | VARCHAR (192) | The externally-assigned globally unique identifier for the referral  note. |
| CLEANUP_REASON_C | INTEGER |  |
| INVALIDATION_COMMENT | VARCHAR (254) | Free-text comment providing additional context for the data invalidation. |
| RX_TRANSFER_TO_USER_NAME | VARCHAR (254) | This item is used during electronic prescription transfers between two pharmacies. This is the user for the transfer to pharmacy that authorized the transfer. |
| PERFORMANCE_PERIOD_ID | NUMERIC (18,0) | The Value-Based Performance Period that the abstracted medical record data first applies to. |
| AMBNT_PIPE_WKFL_C | INTEGER |  |
| AMBNT_PROCESS_REQ_UTC_DTTM | DATETIME (UTC) | Stores the instant at which the user last requested processing of this session's audio data. Once this is set, the user will not be able to create additional recordings or request processing again. |
| BOOKMARK_LIST_ID | NUMERIC (18,0) | Stores the Reading List (Bookmark List) that is associated with the abstracted data. |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | DOCUMENT_ID | DOCS_RCVD_FMK_INFO | DOCUMENT_ID | No | No | No |  |
| 1 | DOCUMENT_ID | V_EHI_DXR_LINKED_PATS | DOCUMENT_ID | Unknown | Unknown | No |  |
| 2 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 2 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 2 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 3 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 4 | TYPE_C | ZC_DOCUMENT_TYPE | DOCUMENT_TYPE_C | No | No | No |  |
| 5 | PAT_ID | ANTICOAG_SELF_REGULATING | PAT_ID | No | No | No |  |
| 5 | PAT_ID | CARE_COORDINATION | PAT_ID | Unknown | No | No |  |
| 5 | PAT_ID | CLAIMS_DERIVE_PAT_FLAGS | PAT_ID | No | No | No |  |
| 5 | PAT_ID | COMMUNITY_RESRC_REVIEWED | PAT_ID | No | No | No |  |
| 5 | PAT_ID | D_PAT_GEOGRAPHIC_CLASS | PAT_ID | Unknown | Unknown | No |  |
| 5 | PAT_ID | EPT_MEM_INFO | PAT_ID | No | No | No |  |
| 5 | PAT_ID | EXT_DATA_LAST_DONE | PAT_ID | No | No | No |  |
| 5 | PAT_ID | F_IBD_ADULT_FORM_PAT | PAT_ID | Unknown | Unknown | No |  |
| 5 | PAT_ID | HH_PAT_INFO | PAT_ID | Unknown | No | No |  |
| 5 | PAT_ID | HM_STATUS_UPD | PAT_ID | No | No | No |  |
| 5 | PAT_ID | IMMNZTN_LAST_REVIEW | PAT_ID | No | No | No |  |
| 5 | PAT_ID | PATIENT | PAT_ID | No | No | No |  |
| 5 | PAT_ID | PATIENT_2 | PAT_ID | No | No | No |  |
| 5 | PAT_ID | PATIENT_3 | PAT_ID | No | No | No |  |
| 5 | PAT_ID | PATIENT_4 | PAT_ID | No | No | No |  |
| 5 | PAT_ID | PATIENT_5 | PAT_ID | No | No | No |  |
| 5 | PAT_ID | PATIENT_6 | PAT_ID | No | No | No |  |
| 5 | PAT_ID | PATIENT_CONF_ADDR | PAT_ID | No | No | No |  |
| 5 | PAT_ID | PATIENT_MISC_COMMENTS | PAT_ID | No | No | No |  |
| 5 | PAT_ID | PATIENT_MYC | PAT_ID | Unknown | No | No |  |
| 5 | PAT_ID | PATIENT_OPT | PAT_ID | No | No | No |  |

_(185 total; showing first 30)_
