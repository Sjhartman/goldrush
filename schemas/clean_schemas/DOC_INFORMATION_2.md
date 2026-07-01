# DOC_INFORMATION_2

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=DOC_INFORMATION_2

## Description

The DOC_INFORMATION table contains information about documents, including scanned and electronically signed documents.

**Overflow table** for DOC_INFORMATION (101 cols). Contains additional columns for the same records — join on the shared primary key column.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | DCS |
| Release Version | Rel 2018 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| DOCUMENT_ID | VARCHAR (18) | The unique identifier (.1 item) for the document record. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| COMM_ORIG_HNO_ID | VARCHAR (254) | This item stores the original letter (HNO) ID when a letter is converted to a PDF. |
| DOC_REP_CONTEXT_C | INTEGER |  |
| DOC_RDI_ID | NUMERIC (18,0) | Stores the linked form (RDI) that contains key-value pairs. |
| DOCUMENT_FAX_NUM | VARCHAR (60) | This column stores the fax number of the organization where the referral originated. |
| COMM_ORIG_RDI_ID | NUMERIC (18,0) | This item stores the original form (RDI) ID when a form is converted to a PDF. |
| PURGE_TIME_STAMP_UTC_DTTM | DATETIME (UTC) | This item stores the time stamp used by the purge batch job to determine if the DCS should be purged. |
| RSH_LAST_UPDATE_USER_ID | VARCHAR (18) | The last user who updated the research data capture form. |
| RSH_LAST_UPDATE_UTC_DTTM | DATETIME (UTC) | The last instant this data capture form was updated. |
| RSH_FORM_STAT_C | INTEGER |  |
| DOC_SPEC_TYPE_C | VARCHAR (66) |  |
| DOC_SUBSPECIALTY_C | VARCHAR (66) |  |
| TMPLT_SF_FORM_ID | VARCHAR (18) | The unique ID of the SmartForm used to collect information for this document. Should be used in conjunction with DOC_INFORMATION.TMPLT_SF_CNTCT to identify the SmartForm Record. |
| RSH_FORM_NAME | VARCHAR (100) | The instance name for the research data capture form. |
| DOCUMENT_USAGE_C | INTEGER |  |
| DOCUMENT_GROUP_DOCUMENT_ID | VARCHAR (18) | The unique ID of the document record that is considered the primary document in the group this document record belongs to. |
| SCAN_SIG_SOURCE_C | INTEGER |  |
| BLOB_CATEGORY_C | INTEGER |  |
| RX_CUST_ID_OWNER_NAM_RECORD_ID | VARCHAR (50) | This item contains a pointer to the name record of the owner of the customer ID used to pick up the prescriptions for the patient from outpatient pharmacies. |
| IS_MISSING_DATA_YN | VARCHAR (1) |  |
| DOC_RLS_MYCHART_UTC_DTTM | DATETIME (UTC) | Tracks whether and when a document has been released to MyChart to be signed. |
| DOC_CNR_ID | NUMERIC (18,0) | The unique ID of the compounding and repackaging batch associated with the document. |
| DOC_CON_RLS_YN | VARCHAR (1) |  |
| ESIG_ACCESSIBLE_PDF_FILE | VARCHAR (192) | Stores the file name for the accessible PDF of this document on the BLOB. |
| SERIES_SEQ_NUM | INTEGER | The sequence number of the series in a DICOM study (attribute 0020,0011). |
| PS_SERIES_UID | VARCHAR (254) | The instance UID of the series that has the presentation state for the image. |
| PS_UID | VARCHAR (254) | The presentation state instance UID for the image. |
| IMAGE_SEQUENCE_NUM | INTEGER | The image sequence number within the series (attribute 0020,0013). |
| IMG_SLCT_TYPE_C | INTEGER |  |
| FILE_CREATION_TIME | VARCHAR (20) | Stores the timestamp in HL7 format of when the file was created on the blob or DMS server. |
| FILE_LAST_UPD_TIME | VARCHAR (20) | Timestamp in HL7 format of when the image was last updated. |
| FILE_TYPE | VARCHAR (150) | Mime type of the image/document. |
| CLN_DOC_SRC_APT_PAT_ENC_CSN_ID | NUMERIC (18,0) | The appointment that a Document Information (DCS) record was attached to before it was moved to a Clinical Documentation Only encounter. |
| ENROLL_ID | NUMERIC (18,0) | The unique ID of the research study association that has been linked to this document. |
| FILE_CREATION_DTTM | DATETIME (UTC) | Stores the file creation time of the document on the Web Blob Server (WBS) |
| DOC_TKLR_C | INTEGER |  |
| PDF_FILE_KEY | VARCHAR (254) | Holds the key for a PDF representation of the file for this DCS |
| RX_DISPENSE_SIG_DISCLAIMER | VARCHAR (100) | The disclaimer text that the pharmacy customer consented to by providing an electronic signature during an ambulatory pharmacy sale. |
| RX_SIG_DISCLAIMER_TRANSLATED | VARCHAR (4000) | The translated disclaimer text that the pharmacy customer consented to by providing an electronic signature during an ambulatory pharmacy sale. |
| DOC_DEL_RSN_C | INTEGER |  |
| DEFERRED_GEN_STATUS_C | INTEGER |  |
| DISC_TRANSL_LANGUAGE_ID | NUMERIC (18,0) | Gets the language of the translated disclaimer text that the pharmacy customer consented to by providing an electronic signature during an ambulatory pharmacy sale. |
| DOC_TX_ID | NUMERIC (18,0) | Stores ETR ID for the service-line on a claim that the document is associated with, used by Tapestry |
| COMMUNICATION_JOB | VARCHAR (100) | This item links back to the original communication that created this shell DCS record. |
| COMMUNICATION_ID | NUMERIC (18,0) | This item links back to the original communication that created this shell DCS record. |
| START_DOC_PERIOD_DATE | DATETIME | Start date of document period. |
| END_DOC_PERIOD_DATE | DATETIME | End date of document period. |
| CLM_ATTACH_CTL_NUM | VARCHAR (80) | Attachment control number for electronic attachments. This is used to identify electronic attachments for a claim in an ANSI X12 275. |
| CLM_PROV_ACCT_NUM | VARCHAR (192) | Provider submitted account number for electronic attachments. This is used to identify electronic attachments for a claim in an ANSI X12 275. |
| CLAIM_VENDOR_ID | VARCHAR (18) | Vendor record matched to during an ANSI X12 275 load. This is used to identify electronic attachments for a claim in an ANSI X12 275. |
| CLAIM_VENDOR_NPI | NUMERIC (10,0) | NPI of the vendor sent in ANSI X12 275. This is used to identify electronic attachments for a claim in an ANSI X12 275. |
| COPIED_FROM_DOCUMENT_ID | VARCHAR (18) | This item links to the original DCS record that this record was copied from. |
| DOCUMENT_IDENT_SOURCE_C | INTEGER |  |
| EOB_MEMBER_SHARE_AMOUNT | NUMERIC (18,2) | Total amount a member is responsible for, for all the claims included in an Explanation of Benefits document. |
| DOC_SOURCE_ROI_ID | VARCHAR (254) | Stores the ROI ID used to generate a composite document (DCS). A composite document represents one or more contexts which is included in the ROI. |
| WORKQUEUE_EVALUATE_YN | VARCHAR (1) |  |
| DISC_OCR_PLAN_ID | NUMERIC (18,0) | The plan we picked out according to the response from insurance OCR |
| DISC_OCR_STATUS_C | INTEGER |  |
| RX_CUST_ID_BIRTH_DATE | DATETIME | The date of birth of the customer ID holder. |
| RX_CUST_ID_CITY | VARCHAR (254) | The city component of the address from the customer ID. |
| RX_CUST_ID_STATE_C | VARCHAR (66) |  |
| RX_CUST_ID_ZIP | VARCHAR (254) | The postal code component of the address from the customer ID. |
| RX_CUST_ID_COUNTY_C | VARCHAR (66) |  |
| RX_CUST_ID_COUNTRY_C | VARCHAR (66) |  |
| RX_CUST_ID_DISTRCT_C | INTEGER |  |
| RX_CUST_ID_HOUSE_NUM | VARCHAR (254) | The house number component of the address from the customer ID. |
| SELECTED_FOR_INDEX_REVIEW_YN | VARCHAR (1) |  |
| CUR_INDEXING_REVIEW_STATUS_C | INTEGER |  |
| CUR_CHT_CORR_TSK_CCA_ID | NUMERIC (18,0) | This column contains the active chart correction task associated with this document, if any. If a document is flagged on a patient's chart, the chart correction task will be added here and the document will be queued for document corrections. Once document correction is complete, this item will be removed to indicate there are no more chart correction tasks for this document. The flagging and completion of document correction will record this chart correction task in item DCS 25005. |
| CREATED_BY_USER_ID | VARCHAR (18) | The user who created the document. |
| CREATED_INST_UTC_DTTM | DATETIME (UTC) | The date and time the document was created. |
| INDEXED_BY_USER_ID | VARCHAR (18) | The user who indexed the document. |
| INDEXED_INST_UTC_DTTM | DATETIME (UTC) | The date and time the document was indexed. |
| PAGES_INDEXED_NUM | INTEGER | The number of pages originally indexed on the document. |
| DOC_BATCH_TYPE_C | INTEGER |  |
| INDEXING_REVIEWED_BY_USER_ID | VARCHAR (18) | The user who performed indexing review on the document. |
| INDEXING_REVIEW_DEPT_ID | NUMERIC (18,0) | The department where the document was indexing reviewed. |
| DOC_HFR_REGISTRY_ID | NUMERIC (18,0) | Stores the HFR (Form template) ID to be used to create the RDI (Abstraction). |
| BILLING_SERV_AREA_ID | NUMERIC (18,0) | This column indicates the service area that the document was indexed to. This column is used specifically for billing workflows. |
| DOC_APPEAL_GRV_ID | NUMERIC (18,0) | Stores the TAG ID for the appeal or grievance that the document is associated with. |
| REQUESTED_FILE_SAVE_PATH | VARCHAR (4000) | The path that the user initially requested the file be saved to when the file was created. |
| TEMP_ENCRYPTED_FILE | VARCHAR (254) | The WBS key that points to an encrypted version of the file which will be downloaded through Hyperdrive. |
| FILE_CREATION_TEMPLATE_ID | NUMERIC (18,0) | The unique ID of the file template associated with this document. |
| SWEPT_FILE_SIZE | INTEGER | The size of the file this document was swept from |
| SWEPT_FILE_DIRECTORY | VARCHAR (240) | The filepath of the directory this document was swept from |
| ORIGINATING_STARNODE_CLIENT | VARCHAR (36) | The Starnode client this document originated from |
| MY_FILES_INST_UTC_DTTM | DATETIME (UTC) | This item holds the UTC instant that this DCS record became available in the My Files Activity. |
| DEPTH_CAPT_STATUS_C | INTEGER |  |
| LINK_DEPTH_DCS_ID | VARCHAR (18) | Stores the ID for the DCS record of the depth map taken with the image. |
| DEPTH_ACCURACY_C | INTEGER |  |
| DEPTH_QUALITY_C | INTEGER |  |
| WAIT_ESIG_CONFIRM_YN | VARCHAR (1) |  |
| BILL_DOC_PMT_LINK_YN | VARCHAR (1) |  |
| BILL_FILE_NM | VARCHAR (192) | This item stores the original filename. This should have the same value as DCS 3002 (Original Filename). |
| NETWORK_UNIQUE_IDENT | VARCHAR (192) | Stores a unique identifier generated by the organization that originally created the document. This contains an identifier that is unique across the Aura network, both to the environment and within the environment that generated it. |
| SCAN_OS_USER | VARCHAR (91) | Operating system of the user logged in. May not be populated or accurate for all workflows |
| SCAN_CLIENT_OS_USER | VARCHAR (64) | Contains the username of the user logged in to the client operating system (e.g., the user's Windows user name). May not be populated or accurate for all workflows. |
| CLM_ATTACH_UNLINKED_YN | VARCHAR (1) |  |
| SWEPT_FILE_NAME | VARCHAR (192) | The name of the file this document was swept from during directory sweep including the extension |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | DOCUMENT_ID | AWM_IMAGE_DATA | DOCUMENT_ID | No | No | No |  |
| 1 | DOCUMENT_ID | DOC_INFORMATION | DOC_INFO_ID | No | No | No |  |
| 1 | DOCUMENT_ID | DOC_INFORMATION_3 | DOCUMENT_ID | No | No | No |  |
| 1 | DOCUMENT_ID | DOC_INFORMATION_4 | DOC_INFO_ID | No | No | No |  |
| 1 | DOCUMENT_ID | DOC_INFO_DICOM | DOCUMENT_ID | No | No | No |  |
| 1 | DOCUMENT_ID | DOC_MC_BROKER_EOP | DOCUMENT_ID | No | No | No |  |
| 1 | DOCUMENT_ID | IMG_ANNOT_SRC | DOCUMENT_ID | No | No | No |  |
| 2 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 2 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 2 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 3 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 4 | COMM_ORIG_HNO_ID | ABN_NOTES | ABN_NOTE_ID | Unknown | No | No |  |
| 4 | COMM_ORIG_HNO_ID | ABN_NOTE_INFO | NOTE_ID | No | No | No |  |
| 4 | COMM_ORIG_HNO_ID | CODING_CLA_NOTES | NOTE_ID | Unknown | No | No |  |
| 4 | COMM_ORIG_HNO_ID | FA_NOTES_QUERY | NOTE_ID | No | No | No |  |
| 4 | COMM_ORIG_HNO_ID | FIN_ASST_LETTER | NOTE_ID | No | No | No |  |
| 4 | COMM_ORIG_HNO_ID | FIN_ASST_NOTE | NOTE_ID | No | No | No |  |
| 4 | COMM_ORIG_HNO_ID | HNO_CVG_REQUEST | NOTE_ID | Unknown | No | No |  |
| 4 | COMM_ORIG_HNO_ID | HNO_INFO | NOTE_ID | No | No | No |  |
| 4 | COMM_ORIG_HNO_ID | HNO_INFO_2 | NOTE_ID | No | No | No |  |
| 4 | COMM_ORIG_HNO_ID | HNO_MYC_LET_INFO | NOTE_ID | No | No | No |  |
| 4 | COMM_ORIG_HNO_ID | HSP_ACCT_LETTERS | NOTE_ID | Unknown | No | No |  |
| 4 | COMM_ORIG_HNO_ID | HSP_ACCT_NOTES | NOTE_ID | Unknown | No | No |  |
| 4 | COMM_ORIG_HNO_ID | LETTER_EXTERNAL_INFO | NOTE_ID | No | No | No |  |
| 4 | COMM_ORIG_HNO_ID | NOTES_ACCT | NOTE_ID | Unknown | No | No |  |
| 4 | COMM_ORIG_HNO_ID | NOTES_LAB | NOTE_ID | Unknown | No | No |  |
| 4 | COMM_ORIG_HNO_ID | NOTES_MC_CLM | NOTE_ID | Unknown | Unknown | No |  |
| 4 | COMM_ORIG_HNO_ID | NOTES_MC_PBA | NOTE_ID | No | No | No |  |

_(647 total; showing first 30)_
