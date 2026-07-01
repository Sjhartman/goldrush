# HNO_INFO

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=HNO_INFO

## Description

This table contains common information from General Use Notes items. This table focuses on time-insensitive, once-per-record data while other HNO tables (e.g., NOTES_ACCT, CODING_CLA_NOTES) contain the data for different note types.

**Primary table** in this group (102 cols). Overflow siblings joined on shared key: HNO_INFO_2 (53 cols). Prefer this table for most queries.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | HNO |
| Release Version | SPRING 2008 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| NOTE_ID | VARCHAR (254) | The unique ID of the note record. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| DELETED_CAT_C | INTEGER |  |
| NOTE_TYPE_NOADD_C | VARCHAR (66) |  |
| NOTE_FORMAT_NOADD_C | VARCHAR (66) |  |
| DICT_IDENTIFIER | VARCHAR (254) | Contains the dictation identifier. |
| PAT_ID | VARCHAR (18) | The unique ID of the patient who is associated to this note.  This column is frequently used to link to the PATIENT table. |
| PAT_ENC_CSN_ID | NUMERIC (18,0) | The unique contact serial number for the patient encounter to which the note is attached. This number is unique across all patient encounters in your system. If you use IntraConnect this is the Unique Contact Identifier (UCI). |
| ENTRY_USER_ID | VARCHAR (18) | The unique ID of the user who created this note. This column is frequently used to link to the CLARITY_EMP table. |
| ENTRY_DATETIME | 524 | The date and time when the note was created, either manually by a staff member or automatically by system. If the date is null, the default value is 01/01/1900; If the time is null, the default value is 00:00. |
| NOTE_DESC | VARCHAR (254) | This is a free text description of the note. |
| PATMSG_PAT_ID | VARCHAR (18) | The unique ID of the patient for whom this message will be displayed. |
| PATMSG_EXP_DT | DATETIME | The date when this message will expire. |
| PATMSG_PRIORITY_C | VARCHAR (66) |  |
| PATMSG_LED_USER_ID | VARCHAR (18) | The unique ID of the user who made the most recent edit to this message. |
| PATMSG_LED_DT | DATETIME | The date when the most recent edit to this message was made. |
| PATMSG_DISPLAY | VARCHAR (508) | The HTML representation of this message. |
| NOTE_LET_PRNT_DTTM | DATETIME (Local) | The letter print instant. |
| NOTE_SOURCE_C | INTEGER |  |
| DEPT_MSG_TYPE_C | INTEGER |  |
| DEPT_MSG_DEPT_ID | NUMERIC (18,0) | The department that this message was logged in. |
| DEPT_MSG_STATUS_C | INTEGER |  |
| INPATIENT_DATA_ID *(deprecated)* | VARCHAR (18) |  |
| IP_NOTE_TYPE_C | VARCHAR (66) |  |
| ORIGINAL_HP_ID | VARCHAR (254) | For View-Only H&P notes only - original note record identifier |
| ORIG_HP_DATE_REAL | NUMERIC (18,2) | For View-Only H&P notes only - original note record contact |
| SOURCE_HP_ID | VARCHAR (254) | For Interval H&P only - ID of H&P Note being modified by interval note |
| SOURCE_HP_DATE_REAL | NUMERIC (18,2) | For Interval H&P only - contact of H&P Note being modified by interval note |
| ACCEPT_DATE | DATETIME | Contains the Date the transcription message was accepted. |
| LET_PRNT_MTHD_C | INTEGER |  |
| TRNSCRTN_MVD_DT | DATETIME | The date the transcription was moved to Progress Notes. |
| DEPT_SPECIALTY_C | VARCHAR (66) |  |
| ECG_REV_INST_DTTM | DATETIME (Local) | The date and time when the Electrocardiogram (ECG/EKG) or Spirometry was reviewed. |
| ECG_TECHNICIAN_ID | VARCHAR (254) | The Electrocardiogram/Spirometry Technician |
| SENSITIVITY_STAT_C | VARCHAR (66) |  |
| SAVED_IN_NW_YN | VARCHAR (1) |  |
| DOWNTIME_ID | VARCHAR (192) | A downtime generated identifier. |
| ADDENDUM_PARENT_CSN *(deprecated)* | NUMERIC (18,0) | *** Deprecated *** In table HNO_INFO, the column Addendum_parent (HNO/121) has been deprecated.  The deprecated column's content/data is no longer available since it is no longer populated in Chronicles.  Contains the contact serial number (CSN) of the parent document. |
| SCANNED_DOC_INFO | VARCHAR (254) | Stores the patient ID, DAT and filename associated with a scanned document. This is only for documents coming from the transcription interface. |
| ECG_REPORT_TYPE | VARCHAR (254) | Stores whether the test was an ECG or spirometric test. |
| ECG_REVIEWED_BY | VARCHAR (254) | Stores the technician who reviewed the ECG or spirometry test. |
| PAT_LINK_ID | VARCHAR (18) | Virtual item that will check all HNO items linked to EPT and return the first EPT ID it finds. The items are checked in the following order: 505, 38970, 21001, 600 (which gives us an order, then we look at ord 210), 1605, 1643, 1640. |
| AUTO_GENERATED_YN | VARCHAR (1) |  |
| ACCT_NOTES_EXTRA_ID | NUMERIC (18,0) | This item would be used to link with HAR record to store the claim image and error messages. |
| CLAIM_TEST_INS_DTTM | DATETIME (UTC) | The UTC instance when the error information was stored. |
| LETTER_SUMMARY | VARCHAR (512) | The summary of the letter. |
| REC_ARCHIVED_YN | No | Indicates whether the Note record is archived at the record level. |
| INTF_TRANS_C | INTEGER |  |
| TX_IB_FOLDER_C | NUMERIC (38,0) |  |
| CREATE_INSTANT_DTTM | DATETIME (UTC) | The note's create instant. |
| NOTEWRITER_TEMPLATE | VARCHAR (150) | The NoteWriter template of the note. |
| UNSIGNED_YN | VARCHAR (1) |  |
| DELETE_INSTANT_DTTM | DATETIME (UTC) | The instant when the note is deleted. |
| DELETE_USER_ID | VARCHAR (18) | User who deleted the note |
| FASTNOTE_YN | VARCHAR (1) |  |
| FROM_AUTOSAVE_YN | VARCHAR (1) |  |
| COSIGNED_NOTE_LINK | NUMERIC (18,0) | Contains a contact serial number (CSN) that points to the resident's note being cosigned. Cosigning Note Link (I HNO 34158) is a link for the opposite direction. |
| DATE_OF_SERVIC_DTTM | DATETIME (UTC) | The note's date of service. |
| SIGNED_NOTE_ID | VARCHAR (254) | This item points to the ID of the signed note that this note is addending/editing/cosigning. |
| LST_FILED_INST_DTTM | DATETIME (UTC) | The instant the note was last edited. |
| UPDATE_DATE | No | The date and time when this row was created or last updated in Clarity. |
| NOTE_MOVE_SOURCE_ID | VARCHAR (254) | Populated on a note move with the source note ID. |
| CURRENT_AUTHOR_ID | VARCHAR (18) | This item stores the current author of the note for indexing purposes. |
| NUM_LETTER_PARTS | INTEGER | Number of parts in the letter. |
| LETTER_TYPE_C | VARCHAR (66) |  |
| VISIT_NUM | VARCHAR (254) | Professional billing visit number attached to this note. |
| SCANNED_NOTE_YN | VARCHAR (1) |  |
| CRT_INST_LOCAL_DTTM | DATETIME (Local) | This is a virtual item that gets the create instant (I HNO 17105), in local time format. |
| DEL_INST_LOCAL_DTTM | DATETIME (Local) | This is a virtual item that gets the delete instant, HNO-34150, in local time format. |
| NOTE_PURPOSE_C *(deprecated)* | INTEGER |  |
| RTE_TRIGGER_USER_ID | VARCHAR (18) | End user who triggered the Eligibility query. |
| RTE_TRIGRD_PAT_ID | VARCHAR (18) | The patient that the query was sent for. |
| RTE_REVIEW_VER_ID *(deprecated)* | NUMERIC (18,0) | *** Deprecated *** In table HNO_INFO, the column RTE_REVIEW_VER_ID (I HNO 16350) has been deprecated. The deprecated column's content/data is no longer available since it is no longer populated in Chronicles. |
| AMB_NOTE_YN | VARCHAR (1) |  |
| IB_RESP_USER_ID | VARCHAR (18) | This item stores the user responsible for the associated In Basket message, if any. |
| IB_RESP_POOL_ID | NUMERIC (18,0) | This item stores the pool responsible for the associated In Basket message, if any. |
| PREV_NOTE_TYPE_C | VARCHAR (66) |  |
| PREV_DOC_TYPE_C | VARCHAR (66) |  |
| A_COPY_YN | VARCHAR (1) |  |
| EXT_INTERF_ID | NUMERIC (18,0) | Holds the interface specification (AIP ID) that created the note record.  This column is only populated if the note was created by an interface, such as transcriptions. |
| PRIORITY_YN | VARCHAR (1) |  |
| ACTIVE_FROM_DT | DATETIME | The date on which the note becomes active. |
| ACTIVE_TO_DT | DATETIME | The date after which the note becomes inactive. |
| NOTE_ATTESTED_YN | VARCHAR (1) |  |
| NURS_NOTE_AUTH_NAM | VARCHAR (250) | The name of the note's author. Populated from an EPT nursing note during conversion to HNO. |
| MMTA_USED_YN | VARCHAR (1) |  |
| ADDR_VERIF_ACCT_ID | NUMERIC (18,0) | The ID of the account that an Address Verification query was sent for. |
| NOT_FOR_PRINTING_YN | VARCHAR (1) |  |
| TREAT_SUM_RLS_TO_MYC_YN | VARCHAR (1) |  |
| TREAT_SUM_RLS_TO_MYC_CSN | NUMERIC (18,0) | Stores the CSN of the Treatment Summary (HNO) that is released to MyChart. If you use IntraConnect, this column stores the Unique Contact Identifier (UCI). |
| IS_POC_NOTE_YN | VARCHAR (1) |  |
| NOTE_SHARED_W_PAT_YN | VARCHAR (1) |  |
| COMMENT_USER_ID | VARCHAR (18) | The unique ID of the last user to edit the internal comment in either the Continued Care and Services Coordination or Payer Communication workflows. |
| COMMENT_EDIT_INST_DTTM | DATETIME (UTC) | Instant the comment was last edited in either the Continued Care and Services Coordination or Payer Communication workflows. In UTC. |
| LETTER_TEMPLATE_SMARTTEXT_ID | VARCHAR (18) | For HNO records with a note type (NOTE_TYPE_NOADD_C) of 3-Letter, this column stores the ID of the SmartText (ETX) which was used to build a letter from the Communication Management navigator section or the Letters activity.  For HNO records with a note type of 84-Treatment Summary, this column stores the ID of the Treatment Summary template SmartText that was used to generate the summary. |
| CONVERSATION_MSG_ID | VARCHAR (18) | The record for the message that was also filed as a note. The text filed in the message and the quicknote will be the same and displaying one of these to the end user should be sufficient. |
| BOOK_CONFRM_PROV_ID | VARCHAR (18) | The provider that a booking confirmation was booked with. |
| BOOK_CONFRM_LOC_ID | NUMERIC (18,0) | The location that a booking confirmation was booked with. |
| BOOK_CONFRM_TXT | VARCHAR (254) | Some free text about the location that a booking confirmation was booked with. |
| WORKING_COPY_YN | VARCHAR (1) | Surrogate key used to uniquely identify rows in this (and only this) table on Cogito Cloud only, do not assume the surrogate key in this table will correspond to the surrogate key in another table |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| B-TREE INDEX | EIX_HNO_INFO__CSN_ID | PAT_ENC_CSN_ID | 1 | Yes | Yes |  |

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
| 1 | NOTE_ID | HNO_INFO_2 | NOTE_ID | No | No | No |  |
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

_(631 total; showing first 30)_
