# IMM_ADMIN

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=IMM_ADMIN

## Description

The IMM_ADMIN table contains information about the immunization administered. The rows included in this table are items from DXR (Document) masterfile which include information on type of immunization, administration date, administered dose, administration route, administration site, immunization manufacturer, immunization lot number, administered by, visit date, deferral reason, administration notes, administration location, administration status, administered amount, administered unit, contact serial number of the DXR record that owns the immunization instance and a unique reference identifier to identify a specific instance of an immunization.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | DXR |
| Release Version | Rel 2014 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| DOCUMENT_ID | NUMERIC (22,0) | The unique identifier for the document record. |
| CONTACT_DATE_REAL | FLOAT | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| LINE | INTEGER | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| CONTACT_DATE | DATETIME | The date of this contact in calendar format. |
| IMM_TYPE_ID | NUMERIC (18,0) | External immunization type ID. |
| IMM_TYPE_FREE_TEXT | VARCHAR (254) | The immunization type information for the administered immunization as free text. |
| IMM_DATE | DATETIME | The immunization administration date. |
| IMM_DOSE | VARCHAR (254) | The dose of immunization administered. |
| IMM_ROUTE_C | INTEGER |  |
| IMM_ROUTE_FREE_TXT | VARCHAR (254) | The immunization route information for the administered immunization as free text. |
| IMM_SITE_C | INTEGER |  |
| IMM_SITE_FREE_TXT | VARCHAR (254) | The immunization site information for the administered immunization as free text. |
| IMM_MANUFACTURER_C | INTEGER |  |
| IMM_MANUF_FREE_TEXT | VARCHAR (254) | The immunization manufacturer information for the administered immunization as free text. |
| IMM_LOT_NUMBER | VARCHAR (254) | The immunization administered lot number. |
| IMM_GIVEN_BY_ID | VARCHAR (18) | The immunization administering user ID. This column is frequently used to link to the table CLARITY_EMP. |
| IMM_GIVEN_BY_FT | VARCHAR (254) | The immunization given by information for the administered immunization as free text. |
| IMM_VIS_PUB_DATE | DATETIME | The immunization visit date presented to patient for the administered immunization. |
| IMM_VIS_DATE | VARCHAR (254) | The immunization visit date for the administered immunization. |
| IMM_DEF_RSN_FREE_TX | VARCHAR (254) | The immunization administration deferral reason as free text. |
| IMM_DEF_REASON_C | INTEGER |  |
| IMM_NOTES_RAW_DATA | VARCHAR (300) | Free text immunization notes from the immunization administration. |
| IMM_NOTES | VARCHAR (300) | The immunization administration notes. |
| IMM_LOCATION | VARCHAR (254) | The immunization administration location. |
| IMM_STATUS_C | INTEGER |  |
| IMM_DOSE_AMOUNT | NUMERIC (18,4) | Immunization dose amount. |
| IMM_DOSE_UNIT_C | INTEGER |  |
| IMM_SRC_DXR_CSN | NUMERIC (22,0) | The contact serial number of the received document record that owns the instance of this immunization. |
| IMM_REFERENCE_ID | VARCHAR (174) | This item stores a unique reference identifier to identify a specific instance of an immunization. |
| IMM_SCHED_ID_FT | VARCHAR (254) | Immunization schedule ID used for the administered vaccination. |
| IMM_SCHED_NAME_FT | VARCHAR (254) | Immunization schedule name used for the administered vaccination. |
| IMM_SCHED_CODING_FT | VARCHAR (254) | Immunization schedule coding system used for the administered vaccination. |
| IMM_SCHED_VALID_YN | VARCHAR (1) |  |
| IMM_VALID_RSN_C | INTEGER |  |
| IMM_VALID_RSN_FT | VARCHAR (254) | Description of why the given administration is valid or invalid based on its immunization schedule. |
| IMM_EXT_PRC_REF_ID | VARCHAR (174) | This column stores the external procedure unique reference ID from which this immunization is derived. |
| IMM_LST_UPD_INST_DTTM | DATETIME (UTC) | Stores the last update instant of the immunization in UTC. |
| IMMNZTN_SRC_APPL_C | INTEGER |  |
| IMMNZTN_SRC_WPR_ID | VARCHAR (18) | Stores the WPR ID of the MyChart user who edited the immunization for the contact. |
| IMM_EVENT_IDENT | VARCHAR (150) | This item stores the ID of the event that is associated with an immunization. In cases where there are multiple encounters that link to an immunization, the earliest encounter is represented here. |
| IMM_CHKSUM_VER | VARCHAR (12) | Store which version of the checksum was used to calculate I DXR 4021-Immunization Checksum |
| IMM_ATC_CLASS_C | INTEGER |  |
| IMM_VNR | VARCHAR (18) | Stores the VNR (Nordic product number) of the immunization. |
| IMM_STUDY_IDENT | VARCHAR (254) | Stores the ID of the investigational study associated with this immunization, if one exists. |
| IMM_ORDINAL_NUM | INTEGER | Stores the ordinal number of a vaccine delivered over multiple administrations. |
| IMM_FUNDING_SOURCE_C | INTEGER |  |
| IMM_VFC_ELIGIBILITY_STATUS_C | INTEGER |  |
| IMM_TYPE_OF_CHANGE_C | INTEGER |  |
| IMM_AUTORECON_YN | VARCHAR (1) |  |
| IMM_DUP_INT_IMM_ID | NUMERIC (18,0) | Link to an internal immunization |
| IMM_DEFER_DUR_C | INTEGER |  |
| IMM_PRODUCT_C | INTEGER |  |
| IMM_PRODUCT_FT | VARCHAR (254) | The vaccine administration brand name for the vaccine administration in the received document. |
| IMM_EXT_ADMIN_C | INTEGER |  |
| IMM_FILTER_RSN_C | INTEGER |  |
| IMM_DOSE_UNIT | VARCHAR (254) | This item stores the dose units associated with the immunization. |
| IMM_EXTERNAL_YN | VARCHAR (1) |  |
| IMM_RSN_FOR_VAC_C | INTEGER |  |
| IMM_IS_HI_MATCH_YN | VARCHAR (1) |  |
| IMM_EXTERNAL_IDENTIFIER | VARCHAR (192) | External ID of the immunization record. |
| IMM_SRC_ORG_ID | NUMERIC (18,0) | This item stores the source organizations for immunizations with single sources. |
| IMM_GENERATED_SERIAL_NUM | INTEGER | This item stores the serial number that is generated when receiving the document. |
| IMM_HIST_ADMIN_YN | VARCHAR (1) |  |
| IMM_RECORDED_BY_ADMIN_YN | VARCHAR (1) |  |
| IMM_BULK_STAT_C | INTEGER |  |
| IMM_BULK_INCL_DATE | DATETIME | The date to compare to the change tracking window when loading flat files in bulk via DINE. If the date is within the window, but the data element is missing from the load, then the data element is invalidated. |
| IMM_STATUS_CODE_C | INTEGER |  |
| IMM_ADMIN_EXPIRATION_DATE | DATETIME | This item contains the expiration date sent with an immunization in a C-CDA document. It is used to indicate whether the administered immunization should be considered valid or not. |

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
| 5 | IMM_TYPE_ID | CLARITY_IMMUNZATN | IMMUNZATN_ID | Unknown | No | No |  |
| 9 | IMM_ROUTE_C | ZC_ROUTE | ROUTE_C | No | No | No |  |
| 11 | IMM_SITE_C | ZC_SITE | SITE_C | No | No | No |  |
| 13 | IMM_MANUFACTURER_C | ZC_MFG | MFG_C | No | No | No |  |
| 16 | IMM_GIVEN_BY_ID | CLARITY_EMP | USER_ID | Unknown | No | No |  |
| 16 | IMM_GIVEN_BY_ID | CLARITY_EMP_2 | USER_ID | Unknown | No | No |  |
| 16 | IMM_GIVEN_BY_ID | CLARITY_EMP_3 | USER_ID | Unknown | No | No |  |
| 16 | IMM_GIVEN_BY_ID | CLARITY_EMP_4 | USER_ID | No | No | No |  |
| 16 | IMM_GIVEN_BY_ID | CLARITY_EMP_DEMO | USER_ID | No | No | No |  |
| 16 | IMM_GIVEN_BY_ID | EMP_BASIC_INFO | USER_ID | No | No | No |  |
| 16 | IMM_GIVEN_BY_ID | EMP_DOC_SETTINGS | USER_NUMBER_ID | No | No | No |  |
| 16 | IMM_GIVEN_BY_ID | F_RX_USER | USER_ID | Unknown | Unknown | No |  |
| 16 | IMM_GIVEN_BY_ID | IB_MESSAGE_SETTINGS | USER_ID | No | No | No |  |
| 16 | IMM_GIVEN_BY_ID | LOGIN_INFO | USER_NUMBER_ID | No | No | No |  |
| 16 | IMM_GIVEN_BY_ID | QC_RESULTS_REVIEW | USER_NUMBER_ID | No | No | No |  |

_(70 total; showing first 30)_
