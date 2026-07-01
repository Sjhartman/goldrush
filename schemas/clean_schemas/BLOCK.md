# BLOCK

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=BLOCK

## Description

This table contains information about scheduling blocks.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | BLK |
| Release Version | Rel 2018 |
| May contain EHI? | No |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| BLOCK_ID | NUMERIC (18,0) | The unique identifier (.1 item) for the block record. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| BLOCK_NAME | VARCHAR (200) | Block name as found in the source record name. |
| BLOCK_TYPE_C | INTEGER |  |
| PROVIDER_ID | VARCHAR (18) | The unique ID of the provider associated with the block. |
| SURGEON_GROUP_ID | VARCHAR (18) | The unique ID of the surgeon group associated with the block. |
| SURGICAL_SERVICE_C | VARCHAR (66) |  |
| RECORD_STATUS_C | INTEGER |  |
| RECORD_CREATION_DATE | DATETIME | The date the record was created. |
| INSTANT_OF_UPDATE_DTTM *(deprecated)* | DATETIME (Local) | *** Deprecated *** I BLK 95000 was discontinued since this item is no longer used. This item's value was updated whenever a BLK record was locked, even if a change was made to the BLK record or not. This item was previously used to flag BLK records that needed Clarity updates, but this has been replaced with E4A records. ****** The date and time the block was last updated. |
| RESPONSIBLE_PROV_ID | VARCHAR (18) | Stores the responsible provider for a block. |
| SOURCE_BLOCK_ID | NUMERIC (18,0) | Contains the block ID of the source block for the modifier block. For example: A surgeon modifier block for a general block will contain the record ID of the general block in this item. |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 2 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 2 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 3 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 5 | BLOCK_TYPE_C | ZC_OR_BLOCK | BLOCK_TYPE_C | No | No | No |  |
| 6 | PROVIDER_ID | CLARITY_SER | PROV_ID | Unknown | No | No |  |
| 6 | PROVIDER_ID | CLARITY_SER_2 | PROV_ID | Unknown | No | No |  |
| 6 | PROVIDER_ID | CLARITY_SER_3 | PROV_ID | Unknown | No | No |  |
| 6 | PROVIDER_ID | CLARITY_SER_4 | PROV_ID | No | No | No |  |
| 6 | PROVIDER_ID | CLARITY_SER_MYC | PROV_ID | Unknown | No | No |  |
| 6 | PROVIDER_ID | D_PROV_PRIMARY_HIERARCHY | PROV_ID | Unknown | Unknown | No |  |
| 6 | PROVIDER_ID | ED_SER_SETTINGS | PROV_ID | Unknown | No | No |  |
| 6 | PROVIDER_ID | EXT_CAL_PROV_CONFIG | PROV_ID | No | No | No |  |
| 6 | PROVIDER_ID | OR_SER_EQUIPMENT | PROV_ID | Unknown | No | No |  |
| 6 | PROVIDER_ID | OR_SER_ROOM | PROV_ID | Unknown | No | No |  |
| 6 | PROVIDER_ID | PROV_BATCH_LTR_GEN | PROV_ID | Unknown | No | No |  |
| 6 | PROVIDER_ID | PROV_GROUP | PROV_ID | No | No | No |  |
| 6 | PROVIDER_ID | V_CUBE_D_PROVIDER | PROVIDER_ID | Unknown | Unknown | No |  |
| 7 | SURGEON_GROUP_ID | OR_GRP | GROUP_ID | Unknown | No | No |  |
| 8 | SURGICAL_SERVICE_C | ZC_OR_SERVICE | SERVICE_C | No | No | No |  |
| 9 | RECORD_STATUS_C | ZC_RECORD_STATUS_2 | RECORD_STATUS_2_C | No | No | No |  |
| 9 | RECORD_STATUS_C | ZC_RECORD_STS | RECORD_STS_C | No | No | No |  |
| 12 | RESPONSIBLE_PROV_ID | CLARITY_SER | PROV_ID | Unknown | No | No |  |
| 12 | RESPONSIBLE_PROV_ID | CLARITY_SER_2 | PROV_ID | Unknown | No | No |  |
| 12 | RESPONSIBLE_PROV_ID | CLARITY_SER_3 | PROV_ID | Unknown | No | No |  |
| 12 | RESPONSIBLE_PROV_ID | CLARITY_SER_4 | PROV_ID | No | No | No |  |
| 12 | RESPONSIBLE_PROV_ID | CLARITY_SER_MYC | PROV_ID | Unknown | No | No |  |
| 12 | RESPONSIBLE_PROV_ID | D_PROV_PRIMARY_HIERARCHY | PROV_ID | Unknown | Unknown | No |  |

_(38 total; showing first 30)_
