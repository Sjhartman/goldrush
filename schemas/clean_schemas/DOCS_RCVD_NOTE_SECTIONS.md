# DOCS_RCVD_NOTE_SECTIONS

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=DOCS_RCVD_NOTE_SECTIONS

## Description

Stores note section data received.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | DXR |
| Release Version | Rel May 2022 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| DOCUMENT_ID | NUMERIC (22,0) | The unique identifier (.1 item) for the document record. |
| CONTACT_DATE_REAL | FLOAT | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| LINE | INTEGER | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| CONTACT_DATE | DATETIME | The date of this contact in calendar format. |
| NOTE_SECTION_IDENTIFIER | VARCHAR (64) | Stores unique identifier for the note section we received |
| NOTE_SECTION_TYPE | VARCHAR (20) | Stores LOINC code for the section type |
| NOTE_SECTION_NOTE_ID | VARCHAR (254) | HNO ID where the note text is saved |
| CONTACT_SERIAL_NUM | NUMERIC (22,0) | The contact serial number (CSN) of the contact. |
| NOTE_SECTION_LENGTH | INTEGER | This item stores total number of characters in the note section. |
| HUMAN_REVIEWED_YN | VARCHAR (1) |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | DOCUMENT_ID | DOCS_RCVD | DOCUMENT_ID | Unknown | No | No |  |
| 1 | DOCUMENT_ID | DOCS_RCVD_FMK_INFO | DOCUMENT_ID | No | No | No |  |
| 1 | DOCUMENT_ID | V_EHI_DXR_LINKED_PATS | DOCUMENT_ID | Unknown | Unknown | No |  |
| 1 | DOCUMENT_ID | DISPENSE_QUERY_INFO | DOCUMENT_ID | No | No | No |  |
| 2 | CONTACT_DATE_REAL | CONTACT_DATE_REAL |  |  |  |  |  |
| 1 | DOCUMENT_ID | DOCS_RCVD_DETAILS | DOCUMENT_ID | Unknown | No | No |  |
| 2 | CONTACT_DATE_REAL | CONTACT_DATE_REAL |  |  |  |  |  |
| 1 | DOCUMENT_ID | DOCS_RCVD_DETAILS_2 | DOCUMENT_ID | No | No | No |  |
| 2 | CONTACT_DATE_REAL | CONTACT_DATE_REAL |  |  |  |  |  |
| 1 | DOCUMENT_ID | DOCS_RCVD_DETAILS_3 | DOCUMENT_ID | No | No | No |  |
| 2 | CONTACT_DATE_REAL | CONTACT_DATE_REAL |  |  |  |  |  |
| 1 | DOCUMENT_ID | DOCS_RCVD_SFM_QUERY_INFO | DOCUMENT_ID | No | No | No |  |
| 2 | CONTACT_DATE_REAL | CONTACT_DATE_REAL |  |  |  |  |  |
| 1 | DOCUMENT_ID | MEDCOM_RCVD_DETAILS | DOCUMENT_ID | No | No | No |  |
| 2 | CONTACT_DATE_REAL | CONTACT_DATE_REAL |  |  |  |  |  |
| 7 | NOTE_SECTION_NOTE_ID | ABN_NOTES | ABN_NOTE_ID | Unknown | No | No |  |
| 7 | NOTE_SECTION_NOTE_ID | ABN_NOTE_INFO | NOTE_ID | No | No | No |  |
| 7 | NOTE_SECTION_NOTE_ID | CODING_CLA_NOTES | NOTE_ID | Unknown | No | No |  |
| 7 | NOTE_SECTION_NOTE_ID | FA_NOTES_QUERY | NOTE_ID | No | No | No |  |
| 7 | NOTE_SECTION_NOTE_ID | FIN_ASST_LETTER | NOTE_ID | No | No | No |  |
| 7 | NOTE_SECTION_NOTE_ID | FIN_ASST_NOTE | NOTE_ID | No | No | No |  |
| 7 | NOTE_SECTION_NOTE_ID | HNO_CVG_REQUEST | NOTE_ID | Unknown | No | No |  |
| 7 | NOTE_SECTION_NOTE_ID | HNO_INFO | NOTE_ID | No | No | No |  |
| 7 | NOTE_SECTION_NOTE_ID | HNO_INFO_2 | NOTE_ID | No | No | No |  |
| 7 | NOTE_SECTION_NOTE_ID | HNO_MYC_LET_INFO | NOTE_ID | No | No | No |  |
| 7 | NOTE_SECTION_NOTE_ID | HSP_ACCT_LETTERS | NOTE_ID | Unknown | No | No |  |
| 7 | NOTE_SECTION_NOTE_ID | HSP_ACCT_NOTES | NOTE_ID | Unknown | No | No |  |
| 7 | NOTE_SECTION_NOTE_ID | LETTER_EXTERNAL_INFO | NOTE_ID | No | No | No |  |
| 7 | NOTE_SECTION_NOTE_ID | NOTES_ACCT | NOTE_ID | Unknown | No | No |  |
| 7 | NOTE_SECTION_NOTE_ID | NOTES_LAB | NOTE_ID | Unknown | No | No |  |

_(41 total; showing first 30)_
