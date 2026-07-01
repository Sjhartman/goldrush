# SPHR_PLAIN_TEXT

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=SPHR_PLAIN_TEXT

## Description

The SPHR_PLAIN_TEXT table contains information about SmartPhrase text in plain text format from the SmartPhrase master file (HH1).

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | HH1 |
| Release Version | SPRING 2006 |
| May contain EHI? | No |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| SMARTPHRASE_ID | NUMERIC (18,0) | The ID of the SmartPhrase record. |
| LINE | No |  |
| CONTACT_DATE | DATETIME | Stores the contact date for the record. |
| CM_CT_OWNER_ID | VARCHAR (25) |  |
| PLAIN_TEXT | VARCHAR (550) | Stores the plain text version of SmartPhrase text. |
| CONTACT_DATE_REAL | No | This is a numeric representation of the date of this encounter in your system. The integer portion of the number specifies the date of the encounter. The digits after the decimal point indicate multiple visits on one day. |
| CM_PHY_OWNER_ID | VARCHAR (25) | Stores the physical owner of this record. |
| CM_LOG_OWNER_ID | VARCHAR (25) | Stores the logical owner of the record. |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | SMARTPHRASE_ID | CL_SPHR | SMARTPHRASE_ID | No | No | No |  |
| 1 | SMARTPHRASE_ID | CL_SPHR_OVRTM | SMARTPHRASE_ID | No | No | No |  |
| 6 | CONTACT_DATE_REAL | CONTACT_DATE_REAL |  |  |  |  |  |
| 4 | CM_CT_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 4 | CM_CT_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 4 | CM_CT_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 7 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 7 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 7 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 8 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 8 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 8 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
