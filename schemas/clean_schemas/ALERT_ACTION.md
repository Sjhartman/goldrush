# ALERT_ACTION

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=ALERT_ACTION

## Description

This table contains details on the actions seen or taken by the alert.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | ALT |
| Release Version | Rel November 2023 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| ALERT_ID | NUMERIC (18,0) | The unique identifier (.1 item) for the alert record. |
| CONTACT_DATE_REAL | FLOAT | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| LINE | INTEGER | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| CONTACT_DATE | DATETIME | The date of this contact in calendar format. |
| ACTION_TYPE_C | INTEGER |  |
| ACTION_IDENT | VARCHAR (91) | The ID of the action either shown or taken by the alert. The type of ID is stored in the ACTION_TYPE_C column. |
| ACTION_NAME | No | The name of the action either shown or taken by the alert at the time the action was extracted to clarity. |
| ACTION_PARENT_ROW | INTEGER | The line number of the row for the parent action within this same related group. |
| ACTION_OUTCOME_C | INTEGER |  |
| ALT_CSN_ID | NUMERIC (18,0) | The unique contact serial number (CSN) of the alert contact. |
| ACTION_FREQ_C | INTEGER |  |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| B-TREE INDEX | EIX_ALERT_ACTION | ACTION_TYPE_C | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_ALERT_ACTION | ACTION_IDENT | 2 | Yes | Yes |  |
| B-TREE INDEX | EIX_ALERT_ACTION | ALT_CSN_ID | 3 | Yes | Yes |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ALERT_ID | ALERT | ALT_ID | No | No | No |  |
| 1 | ALERT_ID | ALT_BPA_TRGR_ACT | ALERT_ID | Unknown | Unknown | No |  |
| 2 | CONTACT_DATE_REAL | CONTACT_DATE_REAL |  |  |  |  |  |
| 1 | ALERT_ID | ALT_DUPLICATE_LDA_INFO | ALERT_ID | No | No | No |  |
| 2 | CONTACT_DATE_REAL | CONTACT_DATE_REAL |  |  |  |  |  |
| 1 | ALERT_ID | SHIPMENT_ALT | ALERT_ID | No | No | No |  |
| 2 | CONTACT_DATE_REAL | CONTACT_DATE_REAL |  |  |  |  |  |
| 5 | ACTION_TYPE_C | ZC_DT_ACTION_TYPE | DT_ACTION_TYPE_C | No | Yes | No |  |
| 9 | ACTION_OUTCOME_C | ZC_DT_ACTION_OUTCOME | DT_ACTION_OUTCOME_C | No | Yes | No |  |
| 10 | ALT_CSN_ID | ALT_DRUG_AGE | ALT_CSN_ID | Unknown | Unknown | No |  |
| 10 | ALT_CSN_ID | ALT_DRUG_ALLERGY | ALT_CSN_ID | Unknown | Unknown | No |  |
| 10 | ALT_CSN_ID | ALT_DRUG_DFALC | ALT_CSN_ID | Unknown | Unknown | No |  |
| 10 | ALT_CSN_ID | ALT_DRUG_DISEASE | ALT_CSN_ID | Unknown | Unknown | No |  |
| 10 | ALT_CSN_ID | ALT_DRUG_DUPTHERPY | ALT_CSN_ID | Unknown | Unknown | No |  |
| 10 | ALT_CSN_ID | ALT_DRUG_IV | ALT_CSN_ID | Unknown | Unknown | No |  |
| 10 | ALT_CSN_ID | ALT_DRUG_LACTATION | ALT_CSN_ID | Unknown | Unknown | No |  |
| 10 | ALT_CSN_ID | ALT_DRUG_PREGNANCY | ALT_CSN_ID | Unknown | Unknown | No |  |
| 10 | ALT_CSN_ID | ALT_DRUG_TPN | ALT_CSN_ID | Unknown | Unknown | No |  |
| 10 | ALT_CSN_ID | ALT_HISTORY | ALT_CSN_ID | No | No | No |  |
| 10 | ALT_CSN_ID | ALT_HISTORY_2 | ALT_CSN_ID | No | No | No |  |
| 10 | ALT_CSN_ID | ALT_HISTORY_3 | ALT_CSN_ID | No | No | No |  |
| 10 | ALT_CSN_ID | F_IP_HSP_ALERT | ALERT_CSN_ID | Unknown | Unknown | No |  |
| 10 | ALT_CSN_ID | F_RX_OE_DRUG_WARNINGS | ALT_CSN_ID | Unknown | Unknown | No |  |
| 10 | ALT_CSN_ID | V_CUBE_F_ALERT | ALERT_CSN_ID | Unknown | Unknown | No |  |
| 10 | ALT_CSN_ID | V_DRUG_WARNINGS | ALT_CSN_ID | Unknown | Unknown | No |  |
| 11 | ACTION_FREQ_C | ZC_DT_ACTION_FREQ | DT_ACTION_FREQ_C | No | Yes | No |  |
