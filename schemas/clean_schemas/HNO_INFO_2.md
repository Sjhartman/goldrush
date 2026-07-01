# HNO_INFO_2

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=HNO_INFO_2

## Description

This table contains common information from General Use Notes items. This table focuses on one time only data while other HNO tables (e.g., NOTES_ACCT, CODING_CLA_NOTES) contain the data for different note types.

**Overflow table** for HNO_INFO (102 cols). Contains additional columns for the same records — join on the shared primary key column.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | HNO |
| Release Version | Rel 2017 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| NOTE_ID | VARCHAR (254) | The note ID for the note record. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| BOOK_CONFRM_DATETIM_DTTM | DATETIME (UTC) | The instant a booking confirmation was scheduled to occur. |
| RELEVANT_REC_EVENT_ID | VARCHAR (18) | Holds the Events (IEV) record which contains records marked relevant to the Note such as problems, allergies, lab results, etc. |
| WAS_PRECHARTED_YN | VARCHAR (1) |  |
| GROUP_NOTE_ID | VARCHAR (254) | This item stores the group note ID for notes that are created in a group documentation context. |
| QN_MESSAGE_TYPE_C | NUMERIC (38,0) |  |
| LETTER_DEST_C | INTEGER |  |
| LETTER_PAT_ID | VARCHAR (18) | The unique ID of the patient that this letter is for. This column is only populated if this row is for a Customer Relationship Management letter. |
| LETTER_FINAL_UTC_DTTM | DATETIME (UTC) | The instant the letter was finalized. This column is only populated if this row is for a Customer Relationship Management letter. |
| HNO_RECORD_TYPE_C | INTEGER |  |
| RFL_NOTE_PURPOSE_C | INTEGER |  |
| LET_ENC_DEPARTMENT_ID | NUMERIC (18,0) | Stores the department from which the letter was sent |
| LET_TO_FACILITY_ID | NUMERIC (18,0) | Stores the facility to which the referral communication letter was sent. |
| LET_TO_DEPARTMENT_ID | NUMERIC (18,0) | Stores the department to which the referral communication letter was sent. |
| LET_TO_PROV_ID | VARCHAR (18) | Stores the provider to which the referral communication letter was sent. |
| RFL_LETTER_ENC_CSN | NUMERIC (18,0) | Stores the encounter in which the referral communication letter was written |
| CONV_MSG_CID | NUMERIC (38,0) | This item contains the Community ID (CID) of a related In Basket Message (EOW) record. |
| CREATION_ACTION_GROUP_ID | NUMERIC (18,0) | The action group that triggered the creation of the note. |
| OUTREACH_TEMPLATE_ID | NUMERIC (18,0) | This item stores the campaign outreach template that created the letter. |
| SHARE_W_PAT_AVAIL_YN | VARCHAR (1) |  |
| SOURCE_EDITS_CSN | NUMERIC (18,0) | Stores a Contact Serial Number (CSN) pointer to the General Use Notes (HNO) record that holds edits to the parent note while an attestation is in progress. |
| STARTING_SMARTTEXT_ID | VARCHAR (18) | This item holds the SmartText that started the note. |
| STARTING_SMARTPHRASE_ID | NUMERIC (18,0) | This item holds the SmartPhrase that started the note. |
| STARTING_SMARTLINK_ID | NUMERIC (18,0) | This item holds the SmartLink that started the note. |
| STARTING_METHOD_C | INTEGER |  |
| RFL_TRANSACTION_TYPE_C | INTEGER |  |
| EXT_ORG_ID | NUMERIC (18,0) | Linked organization ID for the note source. |
| EXT_DOC_EVNT_ID | VARCHAR (174) | External autoreconciled note event identifier |
| EXT_NOTE_TYPE | VARCHAR (256) | Autoreconciled external note type name |
| EXT_DUP_NOTE_ID | VARCHAR (254) | Autoreconciled extneral note duplicate source note |
| EXT_DUP_NOTE_C | INTEGER |  |
| EXT_UNIQ_IDENT | VARCHAR (192) | Globally unique identifier provided by the external system. |
| PARENT_NOTE_ID | VARCHAR (254) | The parent note ID of a soft-deleted transcription record. |
| READY_TO_VIEW_PROV_ID | VARCHAR (18) | The provider who was selected to review the note and sign. |
| ACTIVE_C | INTEGER |  |
| EXT_SOURCE_TYPE_C | INTEGER |  |
| EXT_AUTHOR | VARCHAR (700) | Name of the external note's author. The name is stored as pieces delimited by character 127 and is ordered as follows: Last Name, Last Name from Spouse, First Name, Middle Name, Last Name Prefix, Spouse Last Name Prefix, Title, Suffix, Academic Initials. |
| NOTE_UPDATE_INST_UTC_DTTM | DATETIME (UTC) | The last time this note was received through Care Everywhere. The value of Received Assessment and Plan Existence Days (I DXC 17000) defines how long notes with this item set exist before they are deleted. Scheduled task Remove HNO Records (E1J 88032) deletes notes and all of their references that have not been received within the amount of days defined by Received Assessment and Plan Existence Days (I DXC 17000)  Received Assessment and Plan Existence Days (I DXC 17000) defaults to 30 days if not set. |
| ROUT_RECPNT_COMMUNICATION_ID | NUMERIC (18,0) | This is a Communication Management (LCA) record that contains information about recipients that users selected for routing in the clinical note editor. |
| EXTERNAL_SOURCE_IDENT | VARCHAR (192) | If this note is associated with information in an outside system, the ID of that information can be stored here. |
| DENTAL_NOTE_SECTION_KEY | VARCHAR (4000) |  |
| EXTERNAL_PROBLEM_IDENT | VARCHAR (174) | The reference ID for the external problem linked to the note. |
| OUTREACH_CSN_ID | NUMERIC (18,0) | The unique contact serial number of the outreach for the letter. |
| TRANSLATION_IDENTIFIER | VARCHAR (192) | Stores the unique identifier to link back to the source information that the note is a translation for. This should only be set on Translation (Item HNO 50 = 61) type HNO records. The format of the identifier is intended to capture the INI and ID of the source record, along with the requested language to be translated in. |
| TRANSLATION_LANGUAGE_ID | NUMERIC (18,0) | The unique identifier (.1 item) for the Epic Languages record associated with a translation HNO record. Should only be set for Translation (Item HNO 50 = 61) type notes. |
| TRANSLATION_SOURCE_LANGUAGE_ID | NUMERIC (18,0) | Stores the language (E4N record) of the source text for this translation HNO record. Should only be set for Translation (Item HNO 50 = 61) type notes. |
| PURGE_TIME_STAMP_UTC_DTTM | DATETIME (UTC) | The instant to use when determining if the HNO is old enough that it should be purged. |
| NOT_RESEARCH_RELATED_YN | VARCHAR (1) |  |
| PRIVATE_YN | VARCHAR (1) |  |
| T9N_DRAFT_SAME_CHRS | INTEGER | This item stores the number of unchanged characters between the generated translation and the translation accepted by the translator. This is calculated by performing the Largest Common Subsequence algorithm on the AI generated translation and the translation accepted by the translator, and then storing the number of unchanged characters. |
| T9N_LANG_DRAFT_LEN | INTEGER | This item stores the length of the generated translation. This data is used in tandem with the unchanged character count (I HNO 276) to calculate a percent of the draft edited. |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | NOTE_ID | ABN_NOTES | ABN_NOTE_ID | Unknown | No | No |  |
| 1 | NOTE_ID | ABN_NOTE_INFO | NOTE_ID | No | No | No |  |
| 1 | NOTE_ID | CODING_CLA_NOTES | NOTE_ID | Unknown | No | No |  |
| 1 | NOTE_ID | FA_NOTES_QUERY | NOTE_ID | No | No | No |  |
| 1 | NOTE_ID | FIN_ASST_LETTER | NOTE_ID | No | No | No |  |
| 1 | NOTE_ID | FIN_ASST_NOTE | NOTE_ID | No | No | No |  |
| 1 | NOTE_ID | HNO_CVG_REQUEST | NOTE_ID | Unknown | No | No |  |
| 1 | NOTE_ID | HNO_INFO | NOTE_ID | No | No | No |  |
| 1 | NOTE_ID | HNO_MYC_LET_INFO | NOTE_ID | No | No | No |  |
| 1 | NOTE_ID | HSP_ACCT_LETTERS | NOTE_ID | Unknown | No | No |  |
| 1 | NOTE_ID | HSP_ACCT_NOTES | NOTE_ID | Unknown | No | No |  |
| 1 | NOTE_ID | LETTER_EXTERNAL_INFO | NOTE_ID | No | No | No |  |
| 1 | NOTE_ID | NOTES_ACCT | NOTE_ID | Unknown | No | No |  |
| 1 | NOTE_ID | NOTES_LAB | NOTE_ID | Unknown | No | No |  |
| 1 | NOTE_ID | NOTES_MC_CLM | NOTE_ID | Unknown | Unknown | No |  |
| 1 | NOTE_ID | NOTES_MC_PBA | NOTE_ID | No | No | No |  |
| 1 | NOTE_ID | NOTES_MC_SER | NOTE_ID | Unknown | Unknown | No |  |
| 1 | NOTE_ID | NOTE_PARENT_NOTE | NOTE_ID | No | No | No |  |
| 1 | NOTE_ID | PATIENT_FYI_FLAGS | NOTE_ID | Unknown | No | No |  |
| 1 | NOTE_ID | REG_HX_NOTES | NOTE_ID | Unknown | No | No |  |
| 1 | NOTE_ID | SAVED_LETTER_HNO | NOTE_ID | Unknown | No | No |  |
| 1 | NOTE_ID | V_EHI_PBA_NOTES_MC_PBA | NOTE_ID | Unknown | Unknown | No |  |
| 1 | NOTE_ID | V_NOTE_CHARACTERISTICS | NOTE_ID | Unknown | Unknown | No |  |
| 1 | NOTE_ID | V_NOTE_SHARE_W_PAT_INFO | NOTE_ID | Unknown | Unknown | No |  |
| 1 | NOTE_ID | V_NOTE_VIEW_INFO | NOTE_ID | Unknown | Unknown | No |  |
| 2 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 2 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 2 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 3 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |

_(384 total; showing first 30)_
