# OR_LNLG_IMPLANTS

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=OR_LNLG_IMPLANTS

## Description

This table contains the implants information for the surgical/invasive procedure log (ORL).

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | ORM |
| Release Version | SPRING 2006 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| RECORD_ID | VARCHAR (18) | The unique ID of the line record. |
| CM_PHY_OWNER_ID | VARCHAR (25) | Physical Owner - EMFI |
| CM_LOG_OWNER_ID | VARCHAR (25) | Logical Owner - EMFI Item |
| IMP_INV_TYPE_ID | VARCHAR (18) | The implant inventory ID (SUP). |
| IMP_NO_INV_ITEM_YN | VARCHAR (1) |  |
| IMPLANT_ID | VARCHAR (18) | The unique identifier for the implant record. |
| IMPLANT_ACTION_C | VARCHAR (66) |  |
| IMPLANT_NUM_USED | INTEGER | The number of implants used. |
| IMPLANT_AREA_C | INTEGER |  |
| IMPLANT_LATERAL_C | INTEGER |  |
| IMPLANT_RSN_WSTD_C | INTEGER |  |
| IMPLANT_CREATED_YN | VARCHAR (1) |  |
| IMP_TRAY_TYPE_C | VARCHAR (66) |  |
| IMP_TRAY_ID | NUMERIC (18,0) | This item is populated if the current implant row is an implant tray, and stores the tray id. |
| IMPLANT_FLASH_YN | VARCHAR (1) |  |
| FLSH_AUTCLVE_C | INTEGER |  |
| FLSH_LOAD | VARCHAR (254) | The load batch ID that this implant was flash sterilized in. |
| FLSH_RSN_C | INTEGER |  |
| FLSH_VER_BY_ID | VARCHAR (18) | The unique id of the staff member who was responsible for verifying that this implant was properly flash sterilized. |
| FLSH_RSLT_C | INTEGER |  |
| FLSH_PRE_RSN_C | INTEGER |  |
| IMPLANT_SCANNED_YN | VARCHAR (1) |  |
| IMPLANT_USAGE_C | INTEGER |  |
| IMPLANT_UNIT_CHARGE | NUMERIC (18,2) | The unit charge sent for the associated implant record. The charge is determined using the necessary settings from the procedural location and the relevant charge settings in place at the time the charges were triggered. Note that this value may differ from what is actually sent from the billing system. |
| IMPLANT_PICK_LIST_ID | VARCHAR (18) | Stores a link to the pick list that caused the implant ORM to be created. |
| IMPLANT_ADDED_VIA_EXPL_ADJ_YN | VARCHAR (1) |  |
| WAS_SWITCHED_YN | VARCHAR (1) |  |
| DATA_SCANNED_YN | VARCHAR (1) |  |
| EXT_IMPLANT_REF_IDENT | VARCHAR (174) | Stores the reference ID of the implant used to generate this data. |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| B-TREE INDEX | EIX_OR_LNLG_IMPLANT_IMPLANT_ID | IMPLANT_ID | 1 | Yes | Yes |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | RECORD_ID | OR_LNLG_ADV_EVENT | RECORD_ID | Unknown | No | No |  |
| 1 | RECORD_ID | OR_LNLG_ANEST_INFO | RECORD_ID | Unknown | No | No |  |
| 1 | RECORD_ID | OR_LNLG_ANES_COMPL | RECORD_ID | Unknown | No | No |  |
| 1 | RECORD_ID | OR_LNLG_ANES_EQUIP | RECORD_ID | Unknown | No | No |  |
| 1 | RECORD_ID | OR_LNLG_ANES_RESP | RECORD_ID | No | No | No |  |
| 1 | RECORD_ID | OR_LNLG_ANES_STAFF | RECORD_ID | Unknown | No | No |  |
| 1 | RECORD_ID | OR_LNLG_ARR_THERAP | RECORD_ID | Unknown | No | No |  |
| 1 | RECORD_ID | OR_LNLG_BLOOD_PROD | RECORD_ID | Unknown | No | No |  |
| 1 | RECORD_ID | OR_LNLG_CDP | RECORD_ID | Unknown | No | No |  |
| 1 | RECORD_ID | OR_LNLG_CHRGINFO | RECORD_ID | Unknown | No | No |  |
| 1 | RECORD_ID | OR_LNLG_COMPLICAT | RECORD_ID | Unknown | No | No |  |
| 1 | RECORD_ID | OR_LNLG_COUNTS | RECORD_ID | Unknown | No | No |  |
| 1 | RECORD_ID | OR_LNLG_DELAY | RECORD_ID | Unknown | No | No |  |
| 1 | RECORD_ID | OR_LNLG_DIAGNOSIS | RECORD_ID | Unknown | No | No |  |
| 1 | RECORD_ID | OR_LNLG_EQUIPMENT | RECORD_ID | Unknown | No | No |  |
| 1 | RECORD_ID | OR_LNLG_ESU | RECORD_ID | Unknown | No | No |  |
| 1 | RECORD_ID | OR_LNLG_GENERAL | RECORD_ID | Unknown | No | No |  |
| 1 | RECORD_ID | OR_LNLG_INSTRUMENT | RECORD_ID | Unknown | No | No |  |
| 1 | RECORD_ID | OR_LNLG_LASERS | RECORD_ID | Unknown | No | No |  |
| 1 | RECORD_ID | OR_LNLG_LASERS_2 | RECORD_ID | Unknown | No | No |  |
| 1 | RECORD_ID | OR_LNLG_LITHOTRIPSY_INFO | RECORD_ID | No | No | No |  |
| 1 | RECORD_ID | OR_LNLG_MEDS | RECORD_ID | Unknown | No | No |  |
| 1 | RECORD_ID | OR_LNLG_OTHEQP_TIME | RECORD_ID | No | No | No |  |
| 1 | RECORD_ID | OR_LNLG_OTH_EQUIP | RECORD_ID | Unknown | No | No |  |
| 1 | RECORD_ID | OR_LNLG_POSITION | RECORD_ID | Unknown | No | No |  |
| 1 | RECORD_ID | OR_LNLG_PREOP_APPT | RECORD_ID | Unknown | No | No |  |
| 1 | RECORD_ID | OR_LNLG_PREOP_PREP | RECORD_ID | Unknown | No | No |  |
| 1 | RECORD_ID | OR_LNLG_PRESUR_EVT | RECORD_ID | Unknown | No | No |  |
| 1 | RECORD_ID | OR_LNLG_PRE_SKIN | RECORD_ID | Unknown | No | No |  |
| 1 | RECORD_ID | OR_LNLG_PSTOP_APPT | RECORD_ID | Unknown | No | No |  |

_(79 total; showing first 30)_
