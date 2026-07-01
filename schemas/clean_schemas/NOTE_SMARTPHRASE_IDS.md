# NOTE_SMARTPHRASE_IDS

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=NOTE_SMARTPHRASE_IDS

## Description

This table stores the SmartPhrase IDs used by the notes.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | HNO |
| Release Version | Rel 2015 |
| May contain EHI? | No |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| NOTE_CSN_ID | NUMERIC (18,0) | The contact serial number (CSN) of the contact. |
| LINE | INTEGER | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| NOTE_ID | VARCHAR (254) | The unique identifier (.1 item) for the note record. |
| CONTACT_DATE_REAL | FLOAT | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| CONTACT_DATE | DATETIME | The date of this contact in calendar format. |
| SMARTPHRASES_ID | NUMERIC (18,0) | This item stores the SmartPhrase IDs used in the note. |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| B-TREE INDEX | EIX_NOTE_SMAR446698915_CONTACT | NOTE_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_NOTE_SMAR446698915_CONTACT | CONTACT_DATE_REAL | 2 | Yes | Yes |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | NOTE_CSN_ID | ABN_FOLLOW_UP | NOTE_CSN_ID | No | No | No |  |
| 1 | NOTE_CSN_ID | NOTES_TRANS_IB | NOTE_CSN_ID | Unknown | No | No |  |
| 1 | NOTE_CSN_ID | NOTE_ENC_INFO | CONTACT_SERIAL_NUM | No | No | No |  |
| 1 | NOTE_CSN_ID | NOTE_ENC_INFO_2 | NOTE_CSN_ID | No | No | No |  |
| 3 | NOTE_ID | ABN_NOTES | ABN_NOTE_ID | Unknown | No | No |  |
| 3 | NOTE_ID | ABN_NOTE_INFO | NOTE_ID | No | No | No |  |
| 3 | NOTE_ID | CODING_CLA_NOTES | NOTE_ID | Unknown | No | No |  |
| 3 | NOTE_ID | FA_NOTES_QUERY | NOTE_ID | No | No | No |  |
| 3 | NOTE_ID | FIN_ASST_LETTER | NOTE_ID | No | No | No |  |
| 3 | NOTE_ID | FIN_ASST_NOTE | NOTE_ID | No | No | No |  |
| 3 | NOTE_ID | HNO_CVG_REQUEST | NOTE_ID | Unknown | No | No |  |
| 3 | NOTE_ID | HNO_INFO | NOTE_ID | No | No | No |  |
| 3 | NOTE_ID | HNO_INFO_2 | NOTE_ID | No | No | No |  |
| 3 | NOTE_ID | HNO_MYC_LET_INFO | NOTE_ID | No | No | No |  |
| 3 | NOTE_ID | HSP_ACCT_LETTERS | NOTE_ID | Unknown | No | No |  |
| 3 | NOTE_ID | HSP_ACCT_NOTES | NOTE_ID | Unknown | No | No |  |
| 3 | NOTE_ID | LETTER_EXTERNAL_INFO | NOTE_ID | No | No | No |  |
| 3 | NOTE_ID | NOTES_ACCT | NOTE_ID | Unknown | No | No |  |
| 3 | NOTE_ID | NOTES_LAB | NOTE_ID | Unknown | No | No |  |
| 3 | NOTE_ID | NOTES_MC_CLM | NOTE_ID | Unknown | Unknown | No |  |
| 3 | NOTE_ID | NOTES_MC_PBA | NOTE_ID | No | No | No |  |
| 3 | NOTE_ID | NOTES_MC_SER | NOTE_ID | Unknown | Unknown | No |  |
| 3 | NOTE_ID | NOTE_PARENT_NOTE | NOTE_ID | No | No | No |  |
| 3 | NOTE_ID | PATIENT_FYI_FLAGS | NOTE_ID | Unknown | No | No |  |
| 3 | NOTE_ID | REG_HX_NOTES | NOTE_ID | Unknown | No | No |  |
| 3 | NOTE_ID | SAVED_LETTER_HNO | NOTE_ID | Unknown | No | No |  |
| 3 | NOTE_ID | V_EHI_PBA_NOTES_MC_PBA | NOTE_ID | Unknown | Unknown | No |  |
| 3 | NOTE_ID | V_NOTE_CHARACTERISTICS | NOTE_ID | Unknown | Unknown | No |  |
| 3 | NOTE_ID | V_NOTE_SHARE_W_PAT_INFO | NOTE_ID | Unknown | Unknown | No |  |
| 3 | NOTE_ID | V_NOTE_VIEW_INFO | NOTE_ID | Unknown | Unknown | No |  |

_(31 total; showing first 30)_
