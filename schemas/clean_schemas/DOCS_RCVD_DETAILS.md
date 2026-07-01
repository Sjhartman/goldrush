# DOCS_RCVD_DETAILS

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=DOCS_RCVD_DETAILS

## Description

Details about received documents, including request audit information.

**Primary table** in this group (108 cols). Overflow siblings joined on shared key: DOCS_RCVD_DETAILS_2 (99 cols), DOCS_RCVD_DETAILS_3 (57 cols). Prefer this table for most queries.

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
| CONTACT_DATE_REAL | No | This is a numeric representation of the date of this encounter in your system. The integer portion of the number specifies the date of the encounter. The digits after the decimal point indicate multiple visits on one day. |
| CONTACT_DATE | DATETIME | The date of this contact in calendar format. |
| CM_PHY_OWNER_ID | VARCHAR (25) | Physical owner item |
| CM_LOG_OWNER_ID | VARCHAR (25) | Logical Owner Item |
| CM_CT_OWNER_ID | VARCHAR (25) | Contact owner item |
| CONTACT_SERIAL_NUM | NUMERIC (22,0) | The unique contact serial number (CSN) of the Received Document contact. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| CONTACT_NUM | INTEGER |  |
| DOCUMENT_EXT | VARCHAR (308) | UUID for this document |
| DOCUMENT_ORIGIN_C | INTEGER |  |
| DOCUMENT_RQST_CSN | NUMERIC (18,0) | Patient contact CSN linked to this document request |
| DOC_RQST_WKSTN_ID | VARCHAR (18) | Contains the workstation ID where the document request was initiated |
| DOCUMENT_CONTEXT_C | INTEGER |  |
| DOCUMENT_DEP_ID | NUMERIC (18,0) | ID of the login department where the user was logged in when the document request was initiated |
| DOCUMENT_DESC | VARCHAR (254) | Free text description of the contents of the document |
| DOC_STYLESHEET | VARCHAR (254) | Location of the stylesheet for this document |
| CEID | VARCHAR (184) | The patient Care Everywhere ID used for this request |
| STRUCT_TYPE_C | INTEGER |  |
| RECV_INST | DATETIME (Local) | Instant the document was received from the remote organization |
| CUR_STATUS_C | INTEGER |  |
| DOC_KIND_C | INTEGER |  |
| RQST_TOKEN | VARCHAR (184) | Message request information |
| REQUEST_REASON_C | INTEGER |  |
| REQUEST_EXPLNATION | VARCHAR (254) | Free text explanation for requesting the document |
| REQUEST_VST_PRV_ID | VARCHAR (18) | The unique ID associated with the provider record for the search if the contact has no provider. This column is frequently used to link to the CLARITY_SER table. |
| RECORD_CREATE_INST | DATETIME (Local) | Instant of creation |
| REC_CREATE_USR_ID | VARCHAR (192) |  |
| REQUEST_ROLE_ID | NUMERIC (18,0) | Primary role for the user making the document request |
| CONSENT_DOC_REC_ID | VARCHAR (18) | If authorization was required for this document request then the ID of the document information record (DCS) for the authorization will be stored here. |
| CONSENT_REQ_YN | VARCHAR (1) |  |
| DOCUMENT_LOC_C | INTEGER |  |
| DISC_DATA_FILE_DTTM | DATETIME (Local) | The date and time when the discrete data was filed. |
| HAS_ALG_INFO_YN | VARCHAR (1) |  |
| HAS_PROB_INFO_YN | VARCHAR (1) |  |
| HAS_MED_INFO_YN | VARCHAR (1) |  |
| CHANGES_ONLY_YN | VARCHAR (1) |  |
| SAME_AS_REQ_YN | VARCHAR (1) |  |
| LETTER_CSN | NUMERIC (18,0) | Stores the Contact Serial Number (CSN) of the patient contact where additional information in this received document record is stored. |
| REFERRAL_ID | NUMERIC (18,0) | This item stores the referral record identifier for the referral on the local organization associated with this received document record. |
| LETTER_ID | VARCHAR (254) | This item stores the note record identifier of the letter associated with this received document record. |
| LETTER_NUM | INTEGER | Stores the letter number of the letter associated with this external document record. The letter number corresponds to a line number in EPT related group 20200 which stores patient letters. |
| EXT_MED_MSG_ACUT_YN | VARCHAR (1) |  |
| EOW_ID | VARCHAR (18) | The In Basket message (EOW) that triggered this request. |
| HAS_VTL_INFO_YN | VARCHAR (1) |  |
| EXT_PRES_ERROR_C | INTEGER |  |
| PAT_NAME | VARCHAR (254) | Patient name column. When a document is received from an external system, it will contain certain metadata supplied by the sending system regarding the document. This column contains the patient name that was received in the document's metadata. |
| PAT_FAMILY_NAME | VARCHAR (194) | Patient family name column. When a document is received from an external system, it will contain certain metadata supplied by the sending system regarding the document. This column contains the patient's family name that was received in the document's metadata. |
| PAT_NAME_SUFFIX | VARCHAR (192) | Patient name suffix column. When a document is received from an external system, it will contain certain metadata supplied by the sending system regarding the document. This column contains the patient's name's suffix that was received in the document's metadata. |
| PAT_CITY | VARCHAR (50) | The patient city received as a part of a document from an external system. |
| PAT_STATE_C | VARCHAR (66) |  |
| PAT_ZIP | VARCHAR (20) | The patient's postal code. When a document is received from an external system, it contains certain metadata supplied by the sending system regarding the document. This column contains the patient's postal code that was received in the document's metadata. |
| PAT_COUNTRY_C | VARCHAR (66) |  |
| PAT_SEX_C | VARCHAR (66) |  |
| PAT_DOB_DT | DATETIME | Patient date of birth column. When a document is received from an external system, it will contain certain metadata supplied by the sending system regarding the document. This column contains the patient's date of birth that was received in the document's metadata. |
| SUBSET_TITLE | VARCHAR (254) | Stores the title of the submission set received in an incoming Provide and Register message. Its value is supplied by the sending system. |
| SUBSET_CMT | VARCHAR (255) | Submission set comments column. This column stores the comments associated with a submission set received in an incoming Provide and Register message. Its value is supplied by the sending system. |
| AUTHOR_ID | VARCHAR (254) | Author ID column. This column stores the author ID associated with a document or submission set received in an incoming Provide and Register message. Its value is supplied by the sending system. This may be an ID from any codeset, and the codeset is not included in the document submission. |
| AUTHOR_NAME | VARCHAR (254) | Author name column. This column stores the author name associated with a document or submission set received in an incoming Provide and Register message. Its value is supplied by the sending system. |
| PAT_DEST_ID | VARCHAR (184) | The patient destination identifier for this external document received from the sending organization. |
| PROCESSING_STATUS_C | INTEGER |  |
| DEST_LOC_DXO_ID | NUMERIC (18,0) | The destination location organization record (DXO) ID to which the message is sent (set only if it is different from local organization record ID). |
| CE_TOKEN | VARCHAR (184) | This column contains the patient Care Everywhere token from the source organization of the received document. |
| CREAT_INST_DTTM | DATETIME (Local) | Instant the received document was created in the sender organization |
| PAT_SSN | VARCHAR (20) | Patient's Social Security Number (SSN) from an incoming message. |
| PAT_HOME_PH | VARCHAR (250) | Patient's home phone number. |
| PAT_WORK_PH | VARCHAR (250) | Patient's work phone number from an incoming message. |
| PAT_CELL_PH | VARCHAR (250) | Patient's mobile phone number. |
| SRC_LOC_DXO_ID | NUMERIC (18,0) | The document source location organization ID from which the message is sent. It is set only if it is different from the source organization ID (I DXR 70). |
| CE_ENABLED_YN *(deprecated)* | VARCHAR (1) |  |
| DOC_AUTHOR_EMP_ID | VARCHAR (18) | The linked User (EMP) ID of the document authors |
| HAS_IMM_INFO_YN | VARCHAR (1) |  |
| PHR_DIG_SIG_INS_DTTM | DATETIME (UTC) | The instant at which the pharmacy digitally signed the external e-prescription after it is accepted through the incoming pharmacy e-prescribing interface. |
| ERX_CONTROLLED_YN | VARCHAR (1) |  |
| PHR_DIG_SIGNATURE | VARCHAR (1000) | The pharmacy's cryptographic signature of the medication summary generated for a valid controlled external e-prescription when it is accepted through the incoming pharmacy e-prescribing interface. |
| INTF_REF_MEDLOOP_C | INTEGER |  |
| INTF_ID | NUMERIC (18,0) | Interface Id that created the DXR record. |
| INTF_MSG *(deprecated)* | INTEGER |  |
| INTF_PHRM_REF_NUM | VARCHAR (35) | The prescription number of the denied refill request received in the NewRx message in a Denied New Prescription to Follow workflow. |
| INC_CONTEXT_C | INTEGER |  |
| ROOT_NODE | VARCHAR (64) | Root node of the document stored in this contact |
| CONTENT_LOCALE | VARCHAR (20) | Stores the locale associated with the document stored in this contact |
| MSG_PRIORITY_C | VARCHAR (66) |  |
| AUTHOR_ADDRESS | VARCHAR (254) | This item stores the address of the document author. |
| AUTHOR_PHONE | VARCHAR (254) | This item stores the phone number of the document author. |
| HAS_PROC_INFO_YN | VARCHAR (1) |  |
| UNSUPPORTED_NEHTA_YN | VARCHAR (1) |  |
| SENDER_LOC_ID | NUMERIC (18,0) | EAF ID of the message's sender. |
| SENDER_PROV_ID | VARCHAR (18) | SER ID of the message's sender. |
| ERX_SIG_TYPE_C | INTEGER |  |
| HAS_EVENT_INFO_YN | VARCHAR (1) |  |
| TRANSFORM_KEY | VARCHAR (30) | This item stores the document version or other key that is used to specify the correct transform. |
| HAS_GOAL_INFO_YN | VARCHAR (1) |  |
| HAS_RESULT_INFO_YN | VARCHAR (1) |  |
| HAS_PCC_NOTE_YN | VARCHAR (1) |  |
| HAS_HM_YN | VARCHAR (1) |  |
| HAS_CARE_TEAM_YN | VARCHAR (1) |  |
| HAS_SOCIAL_HX_YN | VARCHAR (1) |  |
| HAS_FAMILY_HX_YN | VARCHAR (1) |  |
| HAS_SURG_HX_YN | VARCHAR (1) |  |
| HAS_DX_INFO_YN | VARCHAR (1) |  |
| HAS_ASSMT_INFO_YN | VARCHAR (1) |  |
| PAT_HOUSENUMBER | VARCHAR (12) | Patient's house number from an incoming message. |
| GIVEN_NAME_INIT | VARCHAR (192) | The initials for the person's given names. |
| SPOUSE_LAST_NAME | VARCHAR (192) | The spouse's last name. |
| SPOUSE_L_NAM_PREFIX | VARCHAR (192) | The spouse's last name prefix. |
| PAT_LST_NAME_PREFIX | VARCHAR (192) | The last name prefix. |
| PAT_PREF_NAM | VARCHAR (192) | The patient's preferred name. |
| RCVD_DOC_SIZE | INTEGER | Stores the size of a received document as the number of bytes of the raw content. |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | DOCUMENT_ID | DOCS_RCVD | DOCUMENT_ID | Unknown | No | No |  |
| 1 | DOCUMENT_ID | DOCS_RCVD_FMK_INFO | DOCUMENT_ID | No | No | No |  |
| 1 | DOCUMENT_ID | V_EHI_DXR_LINKED_PATS | DOCUMENT_ID | Unknown | Unknown | No |  |
| 4 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 4 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 4 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 5 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 5 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 5 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 6 | CM_CT_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 6 | CM_CT_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 6 | CM_CT_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 10 | DOCUMENT_ORIGIN_C | ZC_DOCUMENT_ORIGIN | DOCUMENT_ORIGIN_C | No | No | No |  |
| 11 | DOCUMENT_RQST_CSN | ALT_ORD_PROV_SINGL | PAT_ENC_CSN_ID | Unknown | No | No |  |
| 11 | DOCUMENT_RQST_CSN | AN_RELINK_INFO | PAT_ENC_CSN_ID | No | No | No |  |
| 11 | DOCUMENT_RQST_CSN | DENT_ORTH_EXAM_NOTES | PAT_ENC_CSN_ID | No | No | No |  |
| 11 | DOCUMENT_RQST_CSN | FAC_CHG_OVERRIDE | PAT_ENC_CSN_ID | No | No | No |  |
| 11 | DOCUMENT_RQST_CSN | FAM_HX_PAT_ONLY | PAT_ENC_CSN_ID | No | No | No |  |
| 11 | DOCUMENT_RQST_CSN | F_ED_ENCOUNTERS | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 11 | DOCUMENT_RQST_CSN | F_HH_CERT_ATTRIBUTES | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 11 | DOCUMENT_RQST_CSN | F_HH_OASIS_SINGLE | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 11 | DOCUMENT_RQST_CSN | F_HH_OASIS_SINGLE_2 | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 11 | DOCUMENT_RQST_CSN | F_HH_OASIS_SINGLE_3 | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 11 | DOCUMENT_RQST_CSN | F_HH_OASIS_SINGLE_4 | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 11 | DOCUMENT_RQST_CSN | F_HH_OASIS_SINGLE_5 | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 11 | DOCUMENT_RQST_CSN | F_IBD_ADULT_FORM_ENC | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 11 | DOCUMENT_RQST_CSN | F_IBD_FORM_RESP | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 11 | DOCUMENT_RQST_CSN | F_IP_HSP_ADMISSION | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 11 | DOCUMENT_RQST_CSN | F_IP_HSP_SEPSIS3 | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 11 | DOCUMENT_RQST_CSN | F_IRIS_ENC | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |

_(437 total; showing first 30)_
