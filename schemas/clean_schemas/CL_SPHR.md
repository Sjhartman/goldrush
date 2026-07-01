# CL_SPHR

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=CL_SPHR

## Description

The CL_SPHR stores basic information about the SmartPhrase master file (HH1).

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
| CM_PHY_OWNER_ID | VARCHAR (25) | Stores the physical owner of this record. |
| CM_LOG_OWNER_ID | VARCHAR (25) | Logical owner of the record. |
| SMARTPHRASE_NAME | VARCHAR (91) | The name of the SmartPhrase record. |
| RECORD_STATUS_C | INTEGER |  |
| MNEMONIC | VARCHAR (91) | Stores the mnemonic for the SmartPhrase that is used to invoke dot-phrase. |
| FACILITY_LEVEL_YN | VARCHAR (1) |  |
| INST_OF_NA_EDIT_TM | DATETIME (Local) | Stores the instant of edit for no-add items. |
| NOADD_ITEMS_EDITED | VARCHAR (254) | Stores the numbers of all no-add items changed. |
| SMARTPHRASE_TYPE_C | INTEGER |  |
| ACCESS_LOGGING_YN | VARCHAR (1) |  |
| ORIG_FILENAME | VARCHAR (254) | This item stores the file name of where the SmartPhrase came from. |
| FILENAME_HASH | VARCHAR (91) | Contains hash value for originating filename. |
| AFF_FAC_LEV_YN | VARCHAR (1) |  |
| OUT_FAC_LEV_YN | VARCHAR (1) |  |
| PLAIN_TEXT_YN | VARCHAR (1) |  |
| IMPORT_SOURCE_MNEM | VARCHAR (91) | Stores the mnemonic of the SmartPhrase this was sourced from. |
| IMPORT_INITIAL_USER_ID | VARCHAR (18) | Stores the ID of the user who initially created this SmartPhrase as part of a user SmartTool import. |
| IMPORT_INACTIVE_YN *(deprecated)* | VARCHAR (1) |  |
| STPHRASE_INACTIVE_C | INTEGER |  |
| IMPORT_SOURCE_OID | VARCHAR (20) | Stores the OID of the organization that the SmartPhrase was originally exported from. |
| IMPORT_SOURCE_SETTING | VARCHAR (20) | Stores the identifier of the source record at the organization that the SmartPhrase was exported from. |
| LAST_USER_IMPORT_VERSION | INTEGER | Stores the identifier of the source record version at the organization that the SmartPhrase was exported from. |
| LAST_USER_IMPORT_INST_UTC_DTTM | DATETIME (UTC) | Stores the instant that the source record was last imported into this SmartPhrase. |
| RECONCILED_AFTER_IMPORT_YN | VARCHAR (1) |  |
| RECONCILED_AFT_IMPORT_USER_ID | VARCHAR (18) | Stores the user who last reconciled the SmartPhrase after the last time it was imported. |
| RECONC_AFT_IMP_INST_UTC_DTTM | DATETIME (UTC) | Stores the UTC instant the SmartPhrase was most recently reconciled after the last import. |
| LAST_USER_EXPORT_VERSION | INTEGER | Stores the counter representing the last version of the SmartPhrase used for an export. |
| LAST_USER_EXPORT_VERS_CHECKSUM | VARCHAR (250) | Stores the checksum of the last version of the SmartPhrase used for an export. |
| IMPORT_INACTIVE_REASON_C | INTEGER | Surrogate key used to uniquely identify rows in this (and only this) table on Cogito Cloud only, do not assume the surrogate key in this table will correspond to the surrogate key in another table |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 2 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 2 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 3 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 5 | RECORD_STATUS_C | ZC_RECORD_STATUS | RECORD_STATUS_C | No | No | No |  |
| 18 | IMPORT_INITIAL_USER_ID | CLARITY_EMP | USER_ID | Unknown | No | No |  |
| 18 | IMPORT_INITIAL_USER_ID | CLARITY_EMP_2 | USER_ID | Unknown | No | No |  |
| 18 | IMPORT_INITIAL_USER_ID | CLARITY_EMP_3 | USER_ID | Unknown | No | No |  |
| 18 | IMPORT_INITIAL_USER_ID | CLARITY_EMP_4 | USER_ID | No | No | No |  |
| 18 | IMPORT_INITIAL_USER_ID | CLARITY_EMP_DEMO | USER_ID | No | No | No |  |
| 18 | IMPORT_INITIAL_USER_ID | EMP_BASIC_INFO | USER_ID | No | No | No |  |
| 18 | IMPORT_INITIAL_USER_ID | EMP_DOC_SETTINGS | USER_NUMBER_ID | No | No | No |  |
| 18 | IMPORT_INITIAL_USER_ID | F_RX_USER | USER_ID | Unknown | Unknown | No |  |
| 18 | IMPORT_INITIAL_USER_ID | IB_MESSAGE_SETTINGS | USER_ID | No | No | No |  |
| 18 | IMPORT_INITIAL_USER_ID | LOGIN_INFO | USER_NUMBER_ID | No | No | No |  |
| 18 | IMPORT_INITIAL_USER_ID | QC_RESULTS_REVIEW | USER_NUMBER_ID | No | No | No |  |
| 18 | IMPORT_INITIAL_USER_ID | USER_SIDEBAR_RPT | USER_NUMBER_ID | Unknown | No | No |  |
| 18 | IMPORT_INITIAL_USER_ID | V_CUBE_D_USER | USER_ID | Unknown | Unknown | No |  |
| 18 | IMPORT_INITIAL_USER_ID | V_CUBE_RX_USER | USER_ID | Unknown | Unknown | No |  |
| 20 | STPHRASE_INACTIVE_C | ZC_STPHRASE_INACTIVE | STPHRASE_INACTIVE_C | No | No | No |  |
| 26 | RECONCILED_AFT_IMPORT_USER_ID | CLARITY_EMP | USER_ID | Unknown | No | No |  |
| 26 | RECONCILED_AFT_IMPORT_USER_ID | CLARITY_EMP_2 | USER_ID | Unknown | No | No |  |
| 26 | RECONCILED_AFT_IMPORT_USER_ID | CLARITY_EMP_3 | USER_ID | Unknown | No | No |  |
| 26 | RECONCILED_AFT_IMPORT_USER_ID | CLARITY_EMP_4 | USER_ID | No | No | No |  |
| 26 | RECONCILED_AFT_IMPORT_USER_ID | CLARITY_EMP_DEMO | USER_ID | No | No | No |  |
| 26 | RECONCILED_AFT_IMPORT_USER_ID | EMP_BASIC_INFO | USER_ID | No | No | No |  |
| 26 | RECONCILED_AFT_IMPORT_USER_ID | EMP_DOC_SETTINGS | USER_NUMBER_ID | No | No | No |  |
| 26 | RECONCILED_AFT_IMPORT_USER_ID | F_RX_USER | USER_ID | Unknown | Unknown | No |  |

_(37 total; showing first 30)_
