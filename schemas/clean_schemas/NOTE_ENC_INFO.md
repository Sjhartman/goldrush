# NOTE_ENC_INFO

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=NOTE_ENC_INFO

## Description

This table contains information from overtime single-response items about General Use Notes (HNO) records. Contact creation logic for clinical notes is as follows: 1. If a note doesn't exist, a new note is created. This represents the first contact on that note. 2. If a revision is filed by the incoming transcription interface, a new contact is created on the note being revised regardless of note status.

**Primary table** in this group (99 cols). Overflow siblings joined on shared key: NOTE_ENC_INFO_2 (20 cols). Prefer this table for most queries.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | HNO |
| Release Version | Rel 2010 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| NOTE_ID | VARCHAR (254) | The unique identifier for the note record. |
| CONTACT_SERIAL_NUM | NUMERIC (18,0) | The contact serial number (CSN) of the contact. |
| CONTACT_DATE_REAL | No | A unique, internal contact date in decimal format. The integer portion of the number indicates the date of the contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| LOGICAL_OWNER_ID *(deprecated)* | VARCHAR (25) |  |
| PHYSICAL_OWNER_ID *(deprecated)* | VARCHAR (25) |  |
| CM_CT_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this contact. This is only populated if you use IntraConnect. |
| EXTER_DOCUMENT_ID | VARCHAR (192) | This item stores the external document identifier assigned by the third party transcription system. |
| COSIGN_INSTANT_DTTM | DATETIME (UTC) | The instant when the note was cosigned. |
| COSIGNUSER_ID | VARCHAR (18) | The user who cosigned the note. |
| COSIGN_NOTE_LINK | NUMERIC (18,0) | A note contact serial number (CSN) that points to the attending's note that cosigned this one. |
| COSIGN_REQUIRED_C | INTEGER |  |
| AUTH_LNKED_PROV_ID | VARCHAR (18) | The author's linked provider record. |
| AUTHOR_SERVICE_C | VARCHAR (66) |  |
| ENTRY_INSTANT_DTTM | DATETIME (UTC) | UTC formatted instant of entry for a note. |
| UPD_AUTHOR_INS_DTTM | DATETIME (UTC) | UTC instant of update by a specific user. |
| SPEC_NOTE_TIME_DTTM | 34301 | The note's specified date paired with the specified time. |
| NOTE_FILE_TIME_DTTM | DATETIME (UTC) | UTC formatted instant of when a note is filed. |
| UCN_CONVERTED_C | INTEGER |  |
| AUTHOR_PRVD_TYPE_C | VARCHAR (66) |  |
| NOTE_STATUS_C | VARCHAR (66) |  |
| UPDATE_USER_ID | VARCHAR (18) | The id of the user who updated this contact of the note. |
| CONTACT_DATE | DATETIME | The date of this contact in calendar format. |
| TRN_DOC_AVAIL_STA_C | INTEGER |  |
| TRN_DOC_TYPE_C | VARCHAR (66) |  |
| SENSITIVE_STAT_C | VARCHAR (66) |  |
| AUTHOR_USER_ID | VARCHAR (18) | The unique ID associated with the user who is the author of the note. |
| NOTE_FORMAT_C | VARCHAR (66) |  |
| UPD_BY_AUTH_DTTM | DATETIME (Local) | The instant when the note is updated by the author. |
| LISTS_RESOLVED_YN | VARCHAR (1) |  |
| EXT_TRN_TYPE | VARCHAR (192) | Raw TXA2 values from incoming transcriptions. |
| DICT_PROV_ID | VARCHAR (18) | The unique ID of the provider who is the originator of the dictation. |
| TRAN_WORK_COPY_ID | VARCHAR (254) | Pointer to an HNO record containing text edited from a transcription message. This text should not be available until accepted as part of the transcription process. |
| ACTIVITY_DTTM | 1003 | The activity date and time of the partial dictation/transcription. |
| AUTH_STAT_C | INTEGER |  |
| CONTACT_NUM | VARCHAR (254) | Contact number for the record. |
| UPD_AUT_LOCAL_DTTM | DATETIME (Local) | Update by author instant in local format. |
| ENT_INST_LOCAL_DTTM | DATETIME (Local) | Note entry instant in local format. |
| SPEC_TIME_LOC_DTTM | 34302 | Note specified instant in local format. |
| NOT_FILETM_LOC_DTTM | DATETIME (Local) | Note file time in local format. |
| NOTE_SUMMARY *(deprecated)* | VARCHAR (255) |  |
| EDIT_USER_ID | VARCHAR (18) | The unique ID associated with the user record who edited the note for this particular contact. This is populated for notes with note type 76-Simple Med Note, 77-Medication History, etc. This column is frequently used to link to the CLARITY_EMP table. |
| TRACKING_ENABLED_YN *(deprecated)* | VARCHAR (1) |  |
| DOCUMENT_NAME | VARCHAR (254) | Contains the name of the multi-part document. |
| UMRG_SRC_MEDPROB_ID | NUMERIC (18,0) | The unique ID of the Med Problem List record. |
| ECG_COMMENTS | VARCHAR (254) | Comments about the Electrocardiogram (ECG/EKG). |
| ECG_EDITED_USER_ID | VARCHAR (254) | The person who edited the Electrocardiogram (ECG/EKG). |
| ECG_DIASTOLIC_BP | VARCHAR (254) | The diastolic blood pressure taken from the Electrocardiogram (ECG/EKG). |
| ECG_SYSTOLIC_BP | VARCHAR (254) | The systolic blood pressure taken from the Electrocardiogram (ECG/EKG). |
| ECG_HEARTRATE | VARCHAR (254) | The heartrate from the Electrocardiogram (ECG/EKG). |
| ECG_PR_INTERVAL | VARCHAR (254) | The interval from the beginning of the P wave to the beginning of the QRS wave on the Electrocardiogram (ECG/EKG). |
| ECG_PWAVEAXIS | VARCHAR (254) | The P wave axis on the Electrocardiogram (ECG/EKG). |
| ECG_QRS_DURATION | VARCHAR (254) | The duration of the QRS complex/wave on the Electrocardiogram (ECG/EKG). |
| ECG_QRS_WAVEAXIS | VARCHAR (254) | The QRS complex/wave axis on the Electrocardiogram (ECG/EKG). |
| ECG_QT_INTERVAL | VARCHAR (254) | The interval from the start of the QRS complex/wave to the end of the T wave on the Electrocardiogram (ECG/EKG). |
| ECG_QTC_INTERVAL | VARCHAR (254) | The corrected QT interval for the Electrocardiogram (ECG/EKG). |
| ECG_T_WAVEAXIS | VARCHAR (254) | The T wave axis for the Electrocardiogram (ECG/EKG). |
| SPIRO_BRON | VARCHAR (254) | Stores the type of bronchodilator given to the patient (ex: Albuterol). |
| CARE_PLAN_CSN_ID | NUMERIC (18,0) | Link to care plan contact.  Used to recreate historic versions of care plan. |
| PROGRESS_NOTE_ID | VARCHAR (254) | Progress note ID for the careplan goal note. |
| DEL_NOTE_USER_ID | VARCHAR (18) | The unique ID associated with the user record for this row.  For a note deleted by the IP Note Deletion utility, this item stores the last editing user of the note before it was deleted by the utility.  This column is frequently used to link to the CLARITY_EMP table. |
| DEL_NOTE_AUTHOR_ID | VARCHAR (18) | The unique ID associated with the user record for this row.  For a note deleted by the IP Note Deletion utility, this item stores the last author of the note before it was deleted by the utility.  This column is frequently used to link to the CLARITY_EMP table. |
| PRE_UCN_NOTE_TYPE_C *(deprecated)* | VARCHAR (66) |  |
| NOTE_MISFILE_CCA_ID | NUMERIC (18,0) | CCA id of the chart correction flag. |
| DOCUMENT_SOURCE_C | INTEGER |  |
| NOTE_CREATE_SRC_C | INTEGER |  |
| CNCT_NOTE_TYPE_C | VARCHAR (66) |  |
| DICTATION_DTTM | 1005 | The dictation date and time. |
| TRANSCRIPTION_DTTM | 1007 | The transcription date and time. |
| DICTATING_USER_ID | VARCHAR (18) | The unique ID associated with the user who dictated this transcription. |
| CHR_CNT_DTTM | DATETIME (Local) | Date and time that the transcription character count was recorded. |
| CHR_CNT_MET | FLOAT | The transcription character count metric, i.e. the number of characters found in this transcription. This column is only populated for transcriptions. |
| DICT_PRIORITY_C | INTEGER |  |
| TRNSCRTN_EDIT_DTTM | 1021 | This is the transcription edit date and time. |
| DOC_CHNG_REASON_C | VARCHAR (66) |  |
| TRNSCRTNIST_NAM | VARCHAR (254) | This is the name of the transcriptionist for this transcription. |
| CSGN_RECPNT_USER_ID | VARCHAR (18) | The unique ID associated with the user who is supposed to cosign the note. |
| DRAFT_STATUS_C | INTEGER |  |
| TREAT_SUMM_PAT_DTTM | DATETIME (UTC) | This column stores the UTC instant that a treatment summary note is given to the patient. |
| TREAT_SUMM_PROV_DTTM | DATETIME (UTC) | This column stores the UTC instant that a treatment summary note is given to the follow-up provider. |
| TREAT_SUMM_CPLT_DTTM | DATETIME (UTC) | This column saves the UTC instant that a treatment summary note is marked as complete. |
| PAT_ENC_CSN_ID | NUMERIC (18,0) | This column stores the patient encounter contact serial number (CSN) in which the note was edited. Used for persistent notes to determine in which encounter the note was edited. |
| END_OF_TREAT_DATE | DATETIME | This column saves the end of treatment date for a treatment summary. |
| UNMERGE_SRC_NOTE_ID | VARCHAR (254) | The source note ID before patient merge. |
| NOTE_LENGTH | INTEGER | This item stores the total number of characters of the note. |
| NOTE_SHARED_W_PAT_HX_YN | VARCHAR (1) |  |
| NOTE_TYPE_C | VARCHAR (66) |  |
| POC_NOTE_DISC_C | INTEGER |  |
| COSIGN_INST_LOCAL_DTTM | DATETIME (Local) | The instant in local time when the note was cosigned. |
| IS_PRECHARTED_YN | VARCHAR (1) |  |
| NOTE_LST_EDIT_SRC_C | INTEGER |  |
| LINK_DXR_CSN_ID | NUMERIC (22,0) | Link to the DXR contact that holds the NoteReader data for this note's contact. |
| KANTA_STMT_STAT_C | INTEGER |  |
| CLINICAL_NOTE_SUMMARY | VARCHAR (150) | This item stores a plain text summary of the note contents. |
| SUMMARY_REQUIREMENT_C | INTEGER |  |
| BLOCK_REASON_C | INTEGER |  |
| BLOCK_REASON_TXT | VARCHAR (508) | Stores a free text comment with additional information about why a note was blocked from the patient. |
| MOST_RECENT_CNCT_YN | VARCHAR (1) |  |
| NOTE_HOVER_BUBBLE_LENGTH | INTEGER | This item stores the total number of characters in hover bubbles within the note. |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| B-TREE INDEX | EIX_NOTE_ENC_INFO_ACTIVITY | ACTIVITY_DTTM | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_NOTE_ENC_INFO_CDR_TRN | CONTACT_DATE | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_NOTE_ENC_INFO_CDR_TRN | TRN_DOC_AVAIL_STA_C | 2 | Yes | Yes |  |
| B-TREE INDEX | EIX_NOTE_ENC_INFO_EXTER_DOC | EXTER_DOCUMENT_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_NOTE_ENC_INFO_EXTER_DOC | CONTACT_DATE_REAL | 2 | Yes | Yes |  |
| B-TREE INDEX | EIX_NOTE_ENC_INFO__ENTRY_DTTM | ENTRY_INSTANT_DTTM | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_NOTE_ENC_INFO__ID_DATE_REL | NOTE_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_NOTE_ENC_INFO__ID_DATE_REL | CONTACT_DATE_REAL | 2 | Yes | Yes |  |
| B-TREE INDEX | EIX_NOTE_ENC_I__CSN_UCN_DOC | CONTACT_SERIAL_NUM | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_NOTE_ENC_I__CSN_UCN_DOC | UCN_CONVERTED_C | 2 | Yes | Yes |  |
| B-TREE INDEX | EIX_NOTE_ENC_I__CSN_UCN_DOC | DOCUMENT_SOURCE_C | 3 | Yes | Yes |  |

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
| 2 | CONTACT_SERIAL_NUM | ABN_FOLLOW_UP | NOTE_CSN_ID | No | No | No |  |
| 2 | CONTACT_SERIAL_NUM | NOTES_TRANS_IB | NOTE_CSN_ID | Unknown | No | No |  |
| 2 | CONTACT_SERIAL_NUM | NOTE_ENC_INFO_2 | NOTE_CSN_ID | No | No | No |  |
| 6 | CM_CT_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |

_(400 total; showing first 30)_
