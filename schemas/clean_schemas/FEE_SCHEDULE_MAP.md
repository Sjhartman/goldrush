# FEE_SCHEDULE_MAP

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=FEE_SCHEDULE_MAP

## Description

The FEE_SCHEDULE_MAP table contains basic information about the fee schedule map that is used to select a fee schedule and conversion factor table per geographic area.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | FSM |
| Release Version | Rel 2015 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| FEE_SCHEDULE_MAP_ID | NUMERIC (18,0) | The unique identifier for the fee schedule map record. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| FEE_SCHEDULE_MAP_NAME | VARCHAR (200) | The name for the fee schedule map record. |
| RECORD_STATUS_C | INTEGER |  |
| EXTERNAL_IDENTIFIER | VARCHAR (30) | An external system identifier. |
| RECORD_CREATION_DT | DATETIME | Stores the date the record was created. |
| INSTANT_OF_UPDATE_DTTM | DATETIME (Local) | The instant when the fee schedule map record was last locked or unlocked before this row was extracted. Changes to the instant of update do not trigger a Clarity extract, so values in this column may not represent the current value in Chronicles. |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 2 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 2 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 3 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 5 | RECORD_STATUS_C | ZC_RECORD_STATUS_2 | RECORD_STATUS_2_C | No | No | No |  |
| 5 | RECORD_STATUS_C | ZC_RECORD_STS | RECORD_STS_C | No | No | No |  |
