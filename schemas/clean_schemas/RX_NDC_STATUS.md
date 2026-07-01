# RX_NDC_STATUS

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=RX_NDC_STATUS

## Description

This table contains the medication related to NDC for each contact.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | NDC |
| Release Version | MU4 - EPIC 2002 |
| May contain EHI? | No |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| NDC_ID | VARCHAR (18) | The unique ID for the NDC (National Drug Code). |
| CONTACT_DATE_REAL | No | A unique, internal contact date in decimal format. The integer portion of the number indicates the date of the contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| CONTACT_DATE | DATETIME | The date of this contact in calendar format. |
| LINE | No | This column is deprecated. Table RX_NDC_STATUS extracts OVERTIME_SINGLE table of NDC, it should not have a LINE column. This column actually extracts CONTACT_NUMBER of NDC. Use CONTACT_NUMBER column for contact number instead of this column. |
| CNCT_STAT_NAME | VARCHAR (255) |  |
| CNCT_STAT_CHG_TIME | DATETIME (Local) | The instant the particular contact's status was changed |
| MEDICATION_ID | NUMERIC (18,0) | This is a link to the medication (ERX) record this NDC code represents. |
| CNCT_SERIAL_NUM | VARCHAR (254) | The contact serial number for the NDC line. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this Chronicles record. This is populated only if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this Chronicles record was extracted. This is populated only if you use IntraConnect. |
| IMP_STATUS_C | INTEGER |  |
| OUT_OF_MARKET_DATE | DATETIME | For G-Standaard, it is to save the date when the product is out of market. For Medispan, it may be set to the current date/time or NDCs that are inactivated so we know when that happened. For FDB, it is to save the obsolete date for inactivated NDCs. |
| CM_CT_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this contact. This is only populated if you use IntraConnect. |
| CONTACT_NUMBER | INTEGER |  |
| CONTACT_STATUS_C | INTEGER |  |
| IS_BRAND_NDC_YN | VARCHAR (1) |  |
| FINLAND_STATUS_C | INTEGER |  |
| VENDOR_LINKED_MEDICATION_ID | NUMERIC (18,0) | This is a link to the medication (ERX) record this NDC code was assigned during the latest medication load. |
| MED_ID_DIFF_REV_YN | VARCHAR (1) |  |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| B-TREE INDEX | EIX_RX_NDC_STATUS_CSN | CNCT_SERIAL_NUM | 1 | Yes | Yes |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | NDC_ID | RX_NDC | NDC_ID | No | No | No |  |
| 1 | NDC_ID | RX_NDC_2 | NDC_ID | No | No | No |  |
| 1 | NDC_ID | RX_NDC_ADS_INFO | NDC_ID | No | No | No |  |
| 7 | MEDICATION_ID | CLARITY_MEDICATION | MEDICATION_ID | Unknown | No | No |  |
| 7 | MEDICATION_ID | MED_ADS_INFO | MEDICATION_ID | No | No | No |  |
| 7 | MEDICATION_ID | RX_MED_FIVE | MEDICATION_ID | No | No | No |  |
| 7 | MEDICATION_ID | RX_MED_FOUR | MEDICATION_ID | No | No | No |  |
| 7 | MEDICATION_ID | RX_MED_ONE | MEDICATION_ID | No | No | No |  |
| 7 | MEDICATION_ID | RX_MED_THREE | MEDICATION_ID | No | No | No |  |
| 7 | MEDICATION_ID | RX_MED_TWO | MEDICATION_ID | No | No | No |  |
| 7 | MEDICATION_ID | V_CUBE_D_MEDICATION | MEDICATION_ID | Unknown | Unknown | No |  |
| 9 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 9 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 9 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 10 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 10 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 10 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 11 | IMP_STATUS_C | ZC_IMP_STATUS | IMP_STATUS_C | No | No | No |  |
| 13 | CM_CT_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 13 | CM_CT_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 13 | CM_CT_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 15 | CONTACT_STATUS_C | ZC_DEL_STATUS | DEL_STATUS_C | No | No | No |  |
| 15 | CONTACT_STATUS_C | ZC_EDG_REC_STAT | EDG_REC_STAT_C | No | No | No |  |
| 15 | CONTACT_STATUS_C | ZC_ERS_REC_STAT | RECORD_STATUS_C | No | No | No |  |
| 15 | CONTACT_STATUS_C | ZC_HCD_REC_STATE | HCD_REC_STATE_C | No | No | No |  |
| 15 | CONTACT_STATUS_C | ZC_HFL_RECORD_STAT | HFL_RECORD_STAT_C | No | No | No |  |
| 15 | CONTACT_STATUS_C | ZC_IMM_REC_STATUS | IMM_REC_STATUS_C | No | No | No |  |
| 15 | CONTACT_STATUS_C | ZC_LLB_STATUS | LLB_STATUS_C | No | No | No |  |
| 15 | CONTACT_STATUS_C | ZC_LMA_RECORD_STAT | LMA_RECORD_STAT_C | No | No | No |  |
| 15 | CONTACT_STATUS_C | ZC_MEM_REC_STATUS | MEM_REC_STATUS_C | No | No | No |  |

_(52 total; showing first 30)_
