# MYC_PAT_NOTE_VIEW

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=MYC_PAT_NOTE_VIEW

## Description

This table contains information about the patient that viewed this note and when the viewing was done.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | HNO |
| Release Version | SUMMER 2004 |
| May contain EHI? | No |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| NOTE_ID | VARCHAR (254) | The unique ID of the note. |
| CONTACT_DATE_REAL | No | A unique, internal contact date in decimal format. The integer portion of the number indicates the date of the contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| LINE | No | The line count of the patient view audit trail. |
| PAT_ID | VARCHAR (18) | The unique ID of the patient that viewed this note. |
| PATIENT_VIEW_TIME | DATETIME (Local) | The date/time when the patient viewed this note. |
| CM_CT_OWNER_ID | VARCHAR (25) | ID of the deployment owner for this contact. |
| CM_PHY_OWNER_ID | VARCHAR (25) | Record's physical owner. |
| CM_LOG_OWNER_ID | VARCHAR (25) | Record's logical owner. |
| MYC_VIEWER_WPR_ID | VARCHAR (18) | Stores the WPR of the person who viewed the note |

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
| 4 | PAT_ID | ANTICOAG_SELF_REGULATING | PAT_ID | No | No | No |  |
| 4 | PAT_ID | CARE_COORDINATION | PAT_ID | Unknown | No | No |  |
| 4 | PAT_ID | CLAIMS_DERIVE_PAT_FLAGS | PAT_ID | No | No | No |  |
| 4 | PAT_ID | COMMUNITY_RESRC_REVIEWED | PAT_ID | No | No | No |  |

_(72 total; showing first 30)_
