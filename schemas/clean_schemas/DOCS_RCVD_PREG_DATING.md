# DOCS_RCVD_PREG_DATING

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=DOCS_RCVD_PREG_DATING

## Description

This table contains Pregnancy Dating information received from other organizations.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | DXR |
| Release Version | Rel November 2022 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| DOCUMENT_ID | NUMERIC (22,0) | The unique identifier (.1 item) for the document record. |
| CONTACT_DATE_REAL | FLOAT | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| LINE | INTEGER | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| CONTACT_DATE | DATETIME | The date of this contact in calendar format. |
| EVENT_IDENTIFIER | VARCHAR (174) | Unique identifier for the dating event |
| OB_DT_EDD_DATE | DATETIME | Estimated date of delivery documented for the dating event |
| OB_DT_WORKING_EDD_YN | VARCHAR (1) |  |
| OB_DT_EVENT_C | INTEGER |  |
| OB_DT_EVENT_FREE_TEXT | VARCHAR (254) | String basis that was used to determine the estimated date of delivery. |
| OB_DT_EVENT_DATE | DATETIME | The date of the basis event |
| OB_DT_DTEPREC_C | INTEGER |  |
| OB_DT_GA | INTEGER | The gestational age that was determined on the date of the event. |
| OB_DT_DAYS_TO_EDD | INTEGER | The number of days from the date of the event to the EDD. |
| OB_DT_BC_YN | VARCHAR (1) |  |
| OB_DT_CYCLE_LENGTH | INTEGER | The length of a patient's menstrual cycle. Associated with the estimated date of conception (EDC) basis. |
| OB_DT_LUTEAL_LENGTH | INTEGER | The luteal length of a patient's menstrual cycle. Associated with the estimated date of conception (EDC) basis. |
| OB_DT_COMMENT | VARCHAR (254) | Free text comment for the dating event. |
| OB_DT_CHECKSUM | INTEGER | Checksum of the data associated with this row. |
| OB_DT_SOURCE_DOCUMENT_CSN_ID | NUMERIC (22,0) | CSN of the source DXR record |

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
| 8 | OB_DT_EVENT_C | ZC_OB_DT_EVENT | OB_DT_EVENT_C | No | No | No |  |
| 11 | OB_DT_DTEPREC_C | ZC_OB_DT_DTEPREC | OB_DT_DTEPREC_C | No | No | No |  |
