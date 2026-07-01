# ACCESS_LOG_MNEM

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=ACCESS_LOG_MNEM

## Description

The ACCESS_LOG_MNEM table contains the detailed information of each mnemonic that should be recorded.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | FULL |
| Load Frequency | INCREMENTAL |
| Chronicles INI | E1M |
| Release Version | MU13 - MAY 2001 |
| May contain EHI? | No |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| DATA_MNEMONIC_ID | VARCHAR (15) | The mnemonic of the data users want to record, i.e. the indices of the info array. |
| DATA_DESC | VARCHAR (60) | The detailed description of the data that this mnemonic denotes. |
| DATA_INDEXED_C | INTEGER |  |
| DATA_INI_ITEM | VARCHAR (12) | The INI and item for the data recorded with this Data Mnemonic. |
| VALUES_PER_EVNT_C | INTEGER |  |
| CM_PHY_OWNER_ID | VARCHAR (25) | ID of the physical deployment owner for this record.  Physical owners will be where the data is hosted, either on the cross-over server or the owner deployment. |
| CM_LOG_OWNER_ID | No | ID of the logical deployment owner for this record.  Logical owners show the deployment where the record was created but doesn't represent if the record is a part of version skew. |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 3 | DATA_INDEXED_C | ZC_CNT_METRIC_EVNT | CNT_METRIC_EVNT_C | No | No | No |  |
| 3 | DATA_INDEXED_C | ZC_CONVERTED | CONVERTED_C | No | No | No |  |
| 3 | DATA_INDEXED_C | ZC_DATA_INDEXED | DATA_INDEXED_C | No | No | No |  |
| 3 | DATA_INDEXED_C | ZC_OP_MIXED_DEFAUL | OP_MIXED_DEFAUL_C | No | No | No |  |
| 3 | DATA_INDEXED_C | ZC_YES_NO | YES_NO_C | No | No | No |  |
| 5 | VALUES_PER_EVNT_C | ZC_VALUES_PER_EVNT | VALUES_PER_EVNT_C | No | No | No |  |
| 6 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 6 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 6 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 7 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 7 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 7 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
