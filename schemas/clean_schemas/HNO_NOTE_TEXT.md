# HNO_NOTE_TEXT

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=HNO_NOTE_TEXT

## Description

The HNO_NOTE_TEXT table contains the note text on I HNO 41 or I HNO 40. The text in HNO 40 or 41 is first converted to plain text. The formatting information in RTF note text or HTML note text is removed. The plain text is then broken up into lines of 1950 characters or less. If Chart Sync is enabled, note records with note type 24-Chart Sync Patient Summary Report, 25-Chart Sync Admission Summary Report are excluded from the table. Note records with a note type of 40-Charge Homing Guarantor Inquiry are not included as they may cause extract issues and serve no reporting purpose.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | HNO |
| Release Version | SPRING 2008 |
| May contain EHI? | No |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| NOTE_ID | VARCHAR (254) | The unique ID of the note record. |
| CONTACT_DATE_REAL | No | A unique, internal contact date in decimal format. The integer portion of the number indicates the date of the contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| LINE | INTEGER | The line number for the note text associated with this contact.  The note text is first converted to plain text, then broken into lines of 1950 characters or less.  Words and line breaks are not split across different lines. This LINE column indicates the line number of the processed text. |
| NOTE_CSN_ID | NUMERIC (18,0) | The unique contact serial number for this contact. This number is unique across all note contacts in your system. If you use IntraConnect this is the Unique Contact Identifier (UCI). |
| CONTACT_DATE | DATETIME | The date of this contact in calendar format. |
| CM_CT_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this contact. This is only populated if you use IntraConnect. |
| CHRON_ITEM_NUM | INTEGER | Indicates the item number, either 40 or 41, that the note text is from. If the note format (on item HNO 53, if blank it looks at item HNO 52) is 2-Rich Text, the note text is obtained from item 41; if the note format is 1-Plain Text, 3-HTML,4-Epic HTML, or 5-EpicML, the note text is obtained from item 40; if the note format is blank, the note text is obtained from item 41 first, and if blank obtained from item 40. |
| NOTE_TEXT | VARCHAR (2000) | The text of the note.   The note text is first converted to plain text, then broken into lines of 1950 characters or less. Words and line breaks are not split across different lines. |
| IS_ARCHIVED_YN | No | Indicates whether or not the note text is archived. During ETL process, the value on this column is updated by the TEXT_ARCHIVED_YN column on the HNO_UPDATE_CT table. |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| B-TREE INDEX | EIX_HNO_NOTE_TEXT_ID | NOTE_ID | 1 | Yes | Yes |  |

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
| 4 | NOTE_CSN_ID | ABN_FOLLOW_UP | NOTE_CSN_ID | No | No | No |  |
| 4 | NOTE_CSN_ID | NOTES_TRANS_IB | NOTE_CSN_ID | Unknown | No | No |  |
| 4 | NOTE_CSN_ID | NOTE_ENC_INFO | CONTACT_SERIAL_NUM | No | No | No |  |
| 4 | NOTE_CSN_ID | NOTE_ENC_INFO_2 | NOTE_CSN_ID | No | No | No |  |

_(33 total; showing first 30)_
