# ACCESS_LOG_METRIC

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=ACCESS_LOG_METRIC

## Description

The ACCESS_LOG_METRIC table contains the detailed information of the metrics defined in the E1M master file.

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
| METRIC_ID | NUMERIC (18,0) | The unique metric record ID (E1M .1). |
| METRIC_NAME | VARCHAR (200) | The name of the metric record. |
| CNT_METRIC_EVNT_C | INTEGER |  |
| NORM_FACTOR | NUMERIC (12,0) | The number used by the event counting routine to multiply by the recorded counts to get the actual event counts. |
| METRIC_DESC | VARCHAR (90) | The unique identifier for this metric. This item identifies events in the Access History and Event Count master files. |
| METRIC_TYPE_C | INTEGER |  |
| METRIC_GROUP_C | INTEGER |  |
| METRIC_ACTION_C | INTEGER | The action associated with this metric. |
| METRIC_LOG_TYPE_C *(deprecated)* | INTEGER |  |
| ACCESS_LOG_TYPE_C | INTEGER |  |
| METRIC_EVNT_TYP_C | INTEGER |  |
| METRIC_OVRMTRC_ID | NUMERIC (18,0) | The metric ID which is overridden by the current metric. |
| METRIC_STATUS_C | INTEGER |  |
| METRIC_WRKF_TYP_C | INTEGER |  |
| CM_PHY_OWNER_ID | VARCHAR (25) | ID of the physical deployment owner for this record.  Physical owners will be where the data is hosted, either on the cross-over server or the owner deployment. |
| CM_LOG_OWNER_ID | No | ID of the logical deployment owner for this record.  Logical owners show the deployment where the record was created but doesn't represent if the record is a part of version skew. |
| EVENT_ACTION_TYPE_C | INTEGER |  |
| EVENT_ACT_SUBTYPE_C | INTEGER |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | METRIC_ID | F_ACCESS_LOG_METRIC_NAME | METRIC_ID | Unknown | Unknown | No |  |
| 3 | CNT_METRIC_EVNT_C | ZC_CNT_METRIC_EVNT | CNT_METRIC_EVNT_C | No | No | No |  |
| 3 | CNT_METRIC_EVNT_C | ZC_CONVERTED | CONVERTED_C | No | No | No |  |
| 3 | CNT_METRIC_EVNT_C | ZC_DATA_INDEXED | DATA_INDEXED_C | No | No | No |  |
| 3 | CNT_METRIC_EVNT_C | ZC_OP_MIXED_DEFAUL | OP_MIXED_DEFAUL_C | No | No | No |  |
| 3 | CNT_METRIC_EVNT_C | ZC_YES_NO | YES_NO_C | No | No | No |  |
| 6 | METRIC_TYPE_C | ZC_METRIC_TYPE | METRIC_TYPE_C | No | No | No |  |
| 7 | METRIC_GROUP_C | ZC_METRIC_GROUP | METRIC_GROUP_C | No | No | No |  |
| 10 | ACCESS_LOG_TYPE_C | ZC_ACCESS_LOG_TYPE | ACCESS_LOG_TYPE_C | No | No | No |  |
| 11 | METRIC_EVNT_TYP_C | ZC_METRIC_EVNT_TYP | METRIC_EVNT_TYP_C | No | No | No |  |
| 12 | METRIC_OVRMTRC_ID | ACCESS_LOG_METRIC | METRIC_ID | Unknown | No | No |  |
| 12 | METRIC_OVRMTRC_ID | F_ACCESS_LOG_METRIC_NAME | METRIC_ID | Unknown | Unknown | No |  |
| 13 | METRIC_STATUS_C | ZC_METRIC_STATUS | METRIC_STATUS_C | No | No | No |  |
| 14 | METRIC_WRKF_TYP_C | ZC_METRIC_WRKF_TYP | METRIC_WRKF_TYP_C | No | No | No |  |
| 15 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 15 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 15 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 16 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 16 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 16 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 17 | EVENT_ACTION_TYPE_C | ZC_EVENT_ACTION_TYPE | EVENT_ACTION_TYPE_C | No | No | No |  |
| 18 | EVENT_ACT_SUBTYPE_C | ZC_EVENT_ACT_SUBTYPE | EVENT_ACT_SUBTYPE_C | No | No | No |  |
