# DOC_INFORMATION

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=DOC_INFORMATION

## Description

The DOC_INFORMATION table contains information about documents, including scanned and electronically signed documents.

**Primary table** in this group (101 cols). Overflow siblings joined on shared key: DOC_INFORMATION_2 (101 cols), DOC_INFORMATION_3 (49 cols), DOC_INFORMATION_4 (8 cols). Prefer this table for most queries.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | DCS |
| Release Version | EPIC 2002 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| DOC_INFO_ID | VARCHAR (18) | The unique ID of the document information record. |
| REC_STATE *(deprecated)* | VARCHAR (8) |  |
| DOC_INFO_TYPE_C | VARCHAR (66) |  |
| DOC_GRP_C | VARCHAR (66) |  |
| DOC_STAT_C | INTEGER |  |
| IS_VISIT_SPEC_YN *(deprecated)* | VARCHAR (1) |  |
| DOC_DESCR | VARCHAR (255) | A short free text description of the document described by this document information. |
| DOC_RECV_TIME | 200 | The date and time the document described by this document information was received. |
| RECV_BY_USER_ID | VARCHAR (18) | The employee who received the document described by this document information. This ID may be encrypted. |
| PAT_REP | VARCHAR (80) | The free text name of the person who legally represents the patient described by this document information. |
| DT_ON_DOC | DATETIME | The date which appears on the document described by this document information. |
| DOC_EXPIR_TIME | 240 | The date and time the document described by this document information expires. |
| DOC_LOC | VARCHAR (255) | A short free text description of the location of the paper copy of the document described by this document information. |
| IS_SCANNED_YN | VARCHAR (1) |  |
| SCAN_TIME | 310 | The date and time the document described by this document information was scanned. |
| SCAN_BY_USER_ID | VARCHAR (18) | The employee who scanned the document described by this document information. This ID may be encrypted. |
| SCAN_DEP_ID | NUMERIC (18,0) | The department where the document described by this document information was scanned. |
| SCAN_FILE | VARCHAR (254) | The file name of the scanned image version of the document described by this document information. |
| IS_ESIGNED_YN | VARCHAR (1) |  |
| ESIGN_TIME | 410 | The date and time the document described by this document information was electronically signed. |
| WITNESS_BY_USER_ID | VARCHAR (18) | The employee who witnessed the electronic signing of the document described by this document information. This ID may be encrypted. |
| ESIGN_DEP_ID | NUMERIC (18,0) | The department where the document described by this document information was electronically signed. |
| ESIGN_HTML_FILE | VARCHAR (200) | The file name of either the template HTML file of the document to be electronically signed prior to it being electronically signed or the unique file name of the HTML file of the electronically signed document described by this document information. |
| ESIGN_FILE | VARCHAR (80) | The file name of the electronic signature file of the document described by this document information. |
| ESIGN_KEY | VARCHAR (80) | The private key used to encrypt the electronically signed file of the document described by this document information. |
| ESIGN_DIGEST | VARCHAR (255) | This field should not be extracted beginning with the Spring 2006 version. It is greater than 255 characters and does not have any apparent reporting value.  A string used to encrypt the electronically signed file of the document described by this document information. |
| DOC_REQ_DT | DATETIME | The date when a copy of the type of document described by this document information was requested. |
| IS_REQ_YN | VARCHAR (1) |  |
| DOC_EFF_TIME | 610 | The date and time the document described by this document information becomes effective. |
| IS_EFF_YN | VARCHAR (1) |  |
| DOC_DISCL_DT | DATETIME | The date when a copy of the document described by this document information was last disclosed. |
| DOC_REVOK_DT | DATETIME | The date when the type of document described by this document information was revoked. |
| IS_REVOK_YN | VARCHAR (1) |  |
| CM_PHY_OWNER_ID | VARCHAR (25) | ID of the physical deployment owner for this record.  Physical owners will be where the data is hosted, either on the cross-over server or the owner deployment. |
| CM_LOG_OWNER_ID | VARCHAR (25) | ID of the logical deployment owner for this record.  Logical owners show the deployment where the record was created but doesn't represent if the record is a part of version skew. |
| DOC_LOCATION_C | VARCHAR (66) |  |
| DOC_PT_ID | VARCHAR (18) | The unique ID of the patient associated with the document record. |
| DOC_CSN | NUMERIC (18,0) | This stores the contact serial number of the encounter that this record is attached to, if applicable. |
| DOC_MEM_ID | VARCHAR (18) | Stores EPT id for the member that the document is associated with, used by Tapestry |
| DOC_CLM_ID | NUMERIC (18,0) | Stores Claim (CLM) ID for the claim that the document is associated with, used by Tapestry. |
| DOC_CVG_ID | NUMERIC (18,0) | Stores Coverage (CVG) ID for the coverage that the document is associated with, used by Tapestry. |
| DOC_EPP_ID | NUMERIC (18,0) | Stores EPP id for the benefit plan/rider that the document is associated with, used by Tapestry |
| DOC_NCC_ID | NUMERIC (18,0) | Stores NCC id for the contract that the document is associated with, used by Tapestry |
| DOC_NCS_ID | NUMERIC (18,0) | Stores customer service (NCS) ID for the customer relationship management (CRM) that the document is associated with, used by Tapestry. |
| DOC_NMM_ID | NUMERIC (18,0) | Stores the case master (NMM) ID for the case that the document is associated with, used by Tapestry. |
| DOC_PBA_ID | VARCHAR (18) | Stores PBA id for the PB Account that the document is associated with, used by Tapestry |
| DOC_PPG_ID | VARCHAR (35) | Stores PPG id for the Employer Group that the document is associated with, used by Tapestry |
| DOC_RFL_ID | NUMERIC (18,0) | Stores Referral (RFL) ID for the Referral that the document is associated with, used by Tapestry. |
| DOC_SER_ID | VARCHAR (18) | Stores Provider/Resource Directory ID (SER) for the provider that the document is associated with, used by Tapestry. |
| DOC_VEN_ID | VARCHAR (18) | Stores VEN id for the vendor that the document is associated with, used by Tapestry |
| ALL_AUTH_ORGS_YN | VARCHAR (1) |  |
| RECORD_STATE_C | INTEGER |  |
| SOURCE_ETX_ID | VARCHAR (18) | Stores the SmartText (ETX) ID that this document (DCS) record was created from. |
| SOURCE_ETX_VERSION | VARCHAR (16) | Stores the version of the SmartText used to create this record. |
| DOC_HNO_ID | VARCHAR (254) | The unique ID of the note record associated with this document. |
| SCAN_LWS_ID | VARCHAR (18) | This item stores the id of the workstation where the document was scanned. |
| ESIG_SIGNED_BY | VARCHAR (254) | eSignature of person document was signed by. |
| ESIGNED_REL_C | INTEGER |  |
| DOC_SRVC_DTTM | 247 | The service date and time of the document. |
| SCAN_INST_DTTM | DATETIME (Local) | This item stores the most clinically relevant date for the document. From top to bottom, it looks to the service date/time (I DCS 246/247), the order prioritized instant (I ORD 24), the encounter date, and the import date/time (I DCS 310/315). |
| DOC_STORAGE_LVL_C | INTEGER |  |
| ROI_AUTH_TYPE_C | VARCHAR (66) |  |
| SCAN_FILE_TYPE | VARCHAR (254) | This column stores the file type of the scanned document. |
| SOURCE_DOC | VARCHAR (100) | The identifier for the document (DCS) record's source document.  This column is only populated for DCS records of type Discharge Attachments. If the document was created from a SmartText (ETX) record, this column contains the ID of that ETX record. If the document was created from an HTML document in the References Activity, this column contains the unique identifier from the CRS.mdb file. |
| EXTERNAL_ID | VARCHAR (192) | The ID value that is used for the document in a 3rd party system. |
| REC_ARCHIVED_YN | No | Indicates whether the Document Information record is archived at the record level. |
| DOC_CREAT_DEPT_ID | NUMERIC (18,0) | The department where this document was created. |
| PT_ENT_DRAW_STAT_C | INTEGER |  |
| PT_ENT_DRAWING_CMT | VARCHAR (508) | Holds any associated comments from a patient-entered drawing question. Only present for documents (DCS) records of type 32010 used by MyChart and Welcome. |
| PHOTO_APPROVED_C | INTEGER |  |
| PHOTO_APRV_APPL_C | INTEGER |  |
| WEB_USER_ID | VARCHAR (18) | This item holds the ID of the MyChart user who created this document record, for patient-generated document records. |
| NEED_ENC_YN | VARCHAR (1) |  |
| PERFORMING_PROV_ID | VARCHAR (18) | Used to store the Provider's name who is performing the procedure mentioned in the e-signature consent form. |
| MEDIA_NOTE_LENGTH | NUMERIC (18,2) | This item stores the length, in minutes, of a media note created by a Bedside user.  This value is used when calculating remote storage usage (BLOB) in order to impose upload limits. |
| COMM_AUTH_C | INTEGER |  |
| ESIG_TMPLT_USED | NUMERIC (18,0) | Stores a link to the template used to sign the document |
| TMPLT_SF_CNTCT | NUMERIC (18,0) | Contact of the SmartForm used to collect information for this document. |
| AUTH_INTERNATIONL_YN *(deprecated)* | VARCHAR (1) |  |
| RESEARCH_STUDY_ID | VARCHAR (18) | Stores the ID of the research study associated with this document. |
| FT_CONSENT_PROCS | VARCHAR (1016) | Stores free text procedures for consent documents |
| ORIGINAL_DOC_ID | VARCHAR (18) | Stores the link to the original (unannotated) document. |
| DOC_SPECIALTY_C | INTEGER |  |
| DOC_SRVR_NAME_C | INTEGER |  |
| FMK_CONSENT_RECV_USER_ID | VARCHAR (18) | This is the employee who received this consent for viewing private medications from FMK. This does not get set when this document is not a private medication consent for FMK. |
| DOC_SOURCE_INFO_C | INTEGER |  |
| RX_CUST_ID_TYPE_C | INTEGER |  |
| RX_CUST_ID_NUM | VARCHAR (100) | This item contains the customer ID number. |
| RX_CUST_ID_OWNER_REL_TO_PAT_C *(deprecated)* | INTEGER |  |
| RX_CUST_ID_OWNER_NAME *(deprecated)* | VARCHAR (100) |  |
| RX_CUST_ID_ISSUE_ORG_C | INTEGER |  |
| CE_SERVICE_START_DATE | DATETIME | Service start date for a received Care Everywhere external authorization |
| CE_SERVICE_END_DATE | DATETIME | Service end date for a received Care Everywhere external authorization |
| DOC_PND_APRV_STAT_C | INTEGER |  |
| DOC_REJ_RSN_C | INTEGER |  |
| DOC_REJ_RSN_TEXT | VARCHAR (254) | Rejection reason freetext |
| COMM_ORIG_TYP_C | INTEGER |  |
| COMM_ORIG_LRP_ID | VARCHAR (18) | This item stores the original report (LRP) ID when a report is converted to a PDF. |
| CREATED_STUDY_AMENDMENT | INTEGER | The ID of the research study amendment considered to be the consent version signed for Research Consent type document (DCS) records. Use the RESEARCH_STUDY_ID column to link to RESEARCH_VERSION_INFO table which has the user-entered version number (STUDY_VERSION) as well as other information. |
| EFF_STUDY_AMENDMENT | INTEGER | The ID of the research study amendment considered to be the current effective version for Research Consent type document (DCS) records. Use the RESEARCH_STUDY_ID column to link to RESEARCH_VERSION_INFO table which has the user-entered version number (STUDY_VERSION) as well as other information. |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| B-TREE INDEX | EIX_DOC_INFORMATION_DOCPTID | DOC_PT_ID | 1 | Yes | Yes |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | DOC_INFO_ID | AWM_IMAGE_DATA | DOCUMENT_ID | No | No | No |  |
| 1 | DOC_INFO_ID | DOC_INFORMATION_2 | DOCUMENT_ID | No | No | No |  |
| 1 | DOC_INFO_ID | DOC_INFORMATION_3 | DOCUMENT_ID | No | No | No |  |
| 1 | DOC_INFO_ID | DOC_INFORMATION_4 | DOC_INFO_ID | No | No | No |  |
| 1 | DOC_INFO_ID | DOC_INFO_DICOM | DOCUMENT_ID | No | No | No |  |
| 1 | DOC_INFO_ID | DOC_MC_BROKER_EOP | DOCUMENT_ID | No | No | No |  |
| 1 | DOC_INFO_ID | IMG_ANNOT_SRC | DOCUMENT_ID | No | No | No |  |
| 3 | DOC_INFO_TYPE_C | ZC_DOC_INFO_TYPE | DOC_INFO_TYPE_C | No | No | No |  |
| 4 | DOC_GRP_C | ZC_DOC_GRP | DOC_GRP_C | No | No | No |  |
| 5 | DOC_STAT_C | ZC_DOC_STAT | DOC_STAT_C | No | No | No |  |
| 9 | RECV_BY_USER_ID | CLARITY_EMP | USER_ID | Unknown | No | No |  |
| 9 | RECV_BY_USER_ID | CLARITY_EMP_2 | USER_ID | Unknown | No | No |  |
| 9 | RECV_BY_USER_ID | CLARITY_EMP_3 | USER_ID | Unknown | No | No |  |
| 9 | RECV_BY_USER_ID | CLARITY_EMP_4 | USER_ID | No | No | No |  |
| 9 | RECV_BY_USER_ID | CLARITY_EMP_DEMO | USER_ID | No | No | No |  |
| 9 | RECV_BY_USER_ID | EMP_BASIC_INFO | USER_ID | No | No | No |  |
| 9 | RECV_BY_USER_ID | EMP_DOC_SETTINGS | USER_NUMBER_ID | No | No | No |  |
| 9 | RECV_BY_USER_ID | F_RX_USER | USER_ID | Unknown | Unknown | No |  |
| 9 | RECV_BY_USER_ID | IB_MESSAGE_SETTINGS | USER_ID | No | No | No |  |
| 9 | RECV_BY_USER_ID | LOGIN_INFO | USER_NUMBER_ID | No | No | No |  |
| 9 | RECV_BY_USER_ID | QC_RESULTS_REVIEW | USER_NUMBER_ID | No | No | No |  |
| 9 | RECV_BY_USER_ID | USER_SIDEBAR_RPT | USER_NUMBER_ID | Unknown | No | No |  |
| 9 | RECV_BY_USER_ID | V_CUBE_D_USER | USER_ID | Unknown | Unknown | No |  |
| 9 | RECV_BY_USER_ID | V_CUBE_RX_USER | USER_ID | Unknown | Unknown | No |  |
| 16 | SCAN_BY_USER_ID | CLARITY_EMP | USER_ID | Unknown | No | No |  |
| 16 | SCAN_BY_USER_ID | CLARITY_EMP_2 | USER_ID | Unknown | No | No |  |
| 16 | SCAN_BY_USER_ID | CLARITY_EMP_3 | USER_ID | Unknown | No | No |  |
| 16 | SCAN_BY_USER_ID | CLARITY_EMP_4 | USER_ID | No | No | No |  |
| 16 | SCAN_BY_USER_ID | CLARITY_EMP_DEMO | USER_ID | No | No | No |  |
| 16 | SCAN_BY_USER_ID | EMP_BASIC_INFO | USER_ID | No | No | No |  |

_(467 total; showing first 30)_
