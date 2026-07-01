# OR_OTA

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=OR_OTA

## Description

The OR_OTA table contains information about the release of blocks in the OR Scheduling system.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | OTA |
| Release Version | SPRING 2006 |
| May contain EHI? | No |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| RECORD_ID | NUMERIC (18,0) | Template audit record (OTA) ID. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CONTACT_NUM *(deprecated)* | INTEGER | Contact number of the current contact.  Deprecated this column because OTA records don't have contacts, |
| CONTACT_DATE *(deprecated)* | DATETIME | Contact date of the current contact.  Deprecated this column because OTA records don't have contacts. Use MOD_INST instead. |
| MOD_TYPE_C | VARCHAR (66) |  |
| REL_DAYS_IN_ADVANC | INTEGER | Stores the number of days before the scheduled automatic release that the block change/release happened. |
| SER_RECORD_ID | VARCHAR (18) | The ID of the SER record whose template was modified. |
| TEMPLATE_BEGIN_DT *(deprecated)* | DATETIME | This column is deprecated and does not extract any data. The template begin date and begin time have been combined into one column. Use OR_OTA__BLOCK_START_INST  instead. |
| TEMPLATE_END_DT *(deprecated)* | DATETIME | This column is deprecated and does not extract any data. The template end date and end time have been combined into one column. Use OR_OTA__BLOCK_END_INST  instead. |
| MOD_INST | DATETIME (Local) | The instant the template was modified. |
| MOD_USER_ID | VARCHAR (18) | The ID of the user who modified the template. |
| TEMPLATE_BEGIN_TM *(deprecated)* | DATETIME | This column is deprecated and does not extract any data. The template begin date and begin time have been combined into one column. Use OR_OTA__BLOCK_START_INST  instead. |
| TEMPLATE_END_TM *(deprecated)* | DATETIME | This column is deprecated and does not extract any data. The template end date and end time have been combined into one column. Use OR_OTA__BLOCK_END_INST  instead. |
| FROM_BLOCK_TYPE_C | INTEGER |  |
| FROM_BLOCK_ID | VARCHAR (254) | The block ID before the release/change happened on the block. This column is frequently linked to the table OR_BLOCKNAMES. Columns OR_OTA.FROM_BLOCK_TYPE_C and OR_OTA.FROM_BLOCK_ID both need to be linked to table OR_BLOCKNAMES to retrieve the correct block name information. |
| TO_BLOCK_TYPE_C | INTEGER |  |
| TO_BLOCK_ID | VARCHAR (254) | The block ID after the release/change happened to the block. This column is frequently linked to the table OR_BLOCKNAMES. Columns OR_OTA.TO_BLOCK_TYPE_C and OR_OTA.TO_BLOCK_ID both need to be linked to table OR_BLOCKNAMES to retrieve the correct block name information. |
| BLOCK_START_INST | DATETIME (Local) | The start instant of the block that was released/changed. |
| BLOCK_END_INST | DATETIME (Local) | The end instant of the block that was released/changed. |
| TEMPLATE_DT | DATETIME | The template date that was modified. |
| RELEASE_REASON_C | INTEGER |  |
| RELEASE_COMMENTS | VARCHAR (254) | The block release comments. |
| FROM_BLK_ID | NUMERIC (18,0) | The unique identifier (.1 item) for the block record that released the time. This column can be linked with BLOCK.BLOCK_ID for more block information. |
| TO_BLK_ID | NUMERIC (18,0) | The unique identifier (.1 item) for the block record that received the released time. This column can be linked with BLOCK.BLOCK_ID for more block information. |
| UNAVAILABLE_RSN_C | INTEGER |  |
| REQUEST_RANGE_C | INTEGER |  |
| REQUEST_DECLINED_YN | VARCHAR (1) |  |
| REQUEST_DECLINED_COMMENTS | VARCHAR (1000) | The comments about the declined request. |
| REQUEST_DECLINED_BY_USER_ID | VARCHAR (18) | The user that declined the request to release. |
| UNDERUTIL_NOTIF_READ_YN | VARCHAR (1) |  |
| OR_MN_WAVE_C | INTEGER |  |
| OR_MN_NEXT_INST_UTC_DTTM | DATETIME (UTC) | This item stores the instant that the next OR Marketplace Notification should be sent for the release. |
| TEMPLATE_MOD_OUTDATED_YN | VARCHAR (1) | Surrogate key used to uniquely identify rows in this (and only this) table on Cogito Cloud only, do not assume the surrogate key in this table will correspond to the surrogate key in another table |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | RECORD_ID | V_OR_OTA_METRICS | AUDIT_ID | Unknown | Unknown | No |  |
| 2 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 2 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 2 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 3 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 6 | MOD_TYPE_C | ZC_MOD_TYPE | MOD_TYPE_C | No | No | No |  |
| 8 | SER_RECORD_ID | CLARITY_SER | PROV_ID | Unknown | No | No |  |
| 8 | SER_RECORD_ID | CLARITY_SER_2 | PROV_ID | Unknown | No | No |  |
| 8 | SER_RECORD_ID | CLARITY_SER_3 | PROV_ID | Unknown | No | No |  |
| 8 | SER_RECORD_ID | CLARITY_SER_4 | PROV_ID | No | No | No |  |
| 8 | SER_RECORD_ID | CLARITY_SER_MYC | PROV_ID | Unknown | No | No |  |
| 8 | SER_RECORD_ID | D_PROV_PRIMARY_HIERARCHY | PROV_ID | Unknown | Unknown | No |  |
| 8 | SER_RECORD_ID | ED_SER_SETTINGS | PROV_ID | Unknown | No | No |  |
| 8 | SER_RECORD_ID | EXT_CAL_PROV_CONFIG | PROV_ID | No | No | No |  |
| 8 | SER_RECORD_ID | OR_SER_EQUIPMENT | PROV_ID | Unknown | No | No |  |
| 8 | SER_RECORD_ID | OR_SER_ROOM | PROV_ID | Unknown | No | No |  |
| 8 | SER_RECORD_ID | PROV_BATCH_LTR_GEN | PROV_ID | Unknown | No | No |  |
| 8 | SER_RECORD_ID | PROV_GROUP | PROV_ID | No | No | No |  |
| 8 | SER_RECORD_ID | V_CUBE_D_PROVIDER | PROVIDER_ID | Unknown | Unknown | No |  |
| 12 | MOD_USER_ID | CLARITY_EMP | USER_ID | Unknown | No | No |  |
| 12 | MOD_USER_ID | CLARITY_EMP_2 | USER_ID | Unknown | No | No |  |
| 12 | MOD_USER_ID | CLARITY_EMP_3 | USER_ID | Unknown | No | No |  |
| 12 | MOD_USER_ID | CLARITY_EMP_4 | USER_ID | No | No | No |  |
| 12 | MOD_USER_ID | CLARITY_EMP_DEMO | USER_ID | No | No | No |  |
| 12 | MOD_USER_ID | EMP_BASIC_INFO | USER_ID | No | No | No |  |
| 12 | MOD_USER_ID | EMP_DOC_SETTINGS | USER_NUMBER_ID | No | No | No |  |
| 12 | MOD_USER_ID | F_RX_USER | USER_ID | Unknown | Unknown | No |  |
| 12 | MOD_USER_ID | IB_MESSAGE_SETTINGS | USER_ID | No | No | No |  |

_(58 total; showing first 30)_
