# TRG_DEL_BLOCK_INFO

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=TRG_DEL_BLOCK_INFO

## Description

The information about the deleted order blocks (patient order templates) in the treatment day.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | TRG |
| Release Version | Rel 2010 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| REGIMEN_ID | NUMERIC (18,0) | The unique identifier for the patient order group record. |
| CONTACT_DATE_REAL | No | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| LINE | No | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| CONTACT_DT | DATETIME | The date of this contact in calendar format. |
| DELETED_BLOCK_ID | NUMERIC (18,0) | Stores the deleted order id. |
| DELETED_BLOCK_CAT_C | VARCHAR (66) |  |
| DEL_BLK_SRC_DAY_UID | VARCHAR (100) | Stores the unique ID of the day from which it was created. |
| DEL_ORD_SRC_AOG_ID | NUMERIC (18,0) | This column holds the order template (OTP) ID of the advanced order group order (if any) from which this deleted order was created. |
| DELETED_SOURCE_OTP_ID | NUMERIC (18,0) | Stores the block source (I TRG 110) for a deleted order. |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | REGIMEN_ID | DENTAL_VISIT_INFO | REGIMEN_ID | No | No | No |  |
| 1 | REGIMEN_ID | TRG_INFO | REGIMEN_ID | Unknown | No | No |  |
| 1 | REGIMEN_ID | V_EHI_TRG_FILTER | REGIMEN_ID | Unknown | Unknown | No |  |
| 1 | REGIMEN_ID | TRG_UPDATE_INFO | REGIMEN_ID | Unknown | No | No |  |
| 2 | CONTACT_DATE_REAL | CONTACT_DATE_REAL |  |  |  |  |  |
| 5 | DELETED_BLOCK_ID | ADT_PAT_ORDER_TEMPLATE | OTP_ID | No | No | No |  |
| 5 | DELETED_BLOCK_ID | CL_OTP_FST_LST_SCH | OTP_ID | Unknown | No | No |  |
| 5 | DELETED_BLOCK_ID | OTP_DOSE_PARAMS | OTP_ID | Unknown | No | No |  |
| 5 | DELETED_BLOCK_ID | OTP_INFO | OTP_ID | Unknown | No | No |  |
| 5 | DELETED_BLOCK_ID | OTP_INFO_1 | OTP_ID | Unknown | No | No |  |
| 5 | DELETED_BLOCK_ID | OTP_INFO_2 | OTP_ID | Unknown | No | No |  |
| 5 | DELETED_BLOCK_ID | OTP_INFO_3 | OTP_ID | Unknown | No | No |  |
| 5 | DELETED_BLOCK_ID | OTP_INFO_4 | OTP_ID | Unknown | No | No |  |
| 5 | DELETED_BLOCK_ID | OTP_INFO_5 | OTP_ID | No | No | No |  |
| 5 | DELETED_BLOCK_ID | OTP_ROUTING | OTP_ID | Unknown | No | No |  |
| 6 | DELETED_BLOCK_CAT_C | ZC_REGIMEN_CAT | REGIMEN_CAT_C | No | No | No |  |
| 8 | DEL_ORD_SRC_AOG_ID | ADT_PAT_ORDER_TEMPLATE | OTP_ID | No | No | No |  |
| 8 | DEL_ORD_SRC_AOG_ID | CL_OTP_FST_LST_SCH | OTP_ID | Unknown | No | No |  |
| 8 | DEL_ORD_SRC_AOG_ID | OTP_DOSE_PARAMS | OTP_ID | Unknown | No | No |  |
| 8 | DEL_ORD_SRC_AOG_ID | OTP_INFO | OTP_ID | Unknown | No | No |  |
| 8 | DEL_ORD_SRC_AOG_ID | OTP_INFO_1 | OTP_ID | Unknown | No | No |  |
| 8 | DEL_ORD_SRC_AOG_ID | OTP_INFO_2 | OTP_ID | Unknown | No | No |  |
| 8 | DEL_ORD_SRC_AOG_ID | OTP_INFO_3 | OTP_ID | Unknown | No | No |  |
| 8 | DEL_ORD_SRC_AOG_ID | OTP_INFO_4 | OTP_ID | Unknown | No | No |  |
| 8 | DEL_ORD_SRC_AOG_ID | OTP_INFO_5 | OTP_ID | No | No | No |  |
| 8 | DEL_ORD_SRC_AOG_ID | OTP_ROUTING | OTP_ID | Unknown | No | No |  |
| 9 | DELETED_SOURCE_OTP_ID | ADT_PAT_ORDER_TEMPLATE | OTP_ID | No | No | No |  |
| 9 | DELETED_SOURCE_OTP_ID | CL_OTP_FST_LST_SCH | OTP_ID | Unknown | No | No |  |
| 9 | DELETED_SOURCE_OTP_ID | OTP_DOSE_PARAMS | OTP_ID | Unknown | No | No |  |
| 9 | DELETED_SOURCE_OTP_ID | OTP_INFO | OTP_ID | Unknown | No | No |  |

_(36 total; showing first 30)_
