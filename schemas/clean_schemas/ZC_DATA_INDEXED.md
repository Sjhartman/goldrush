# ZC_DATA_INDEXED

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=ZC_DATA_INDEXED

## Description

This table indicates whether event data should be indexed or not.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | FULL |
| Load Frequency | INCREMENTAL |
| Chronicles INI | N/A |
| Release Version | MU13 - MAY 2001 |
| May contain EHI? | No |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| DATA_INDEXED_C | INTEGER |  |
| NAME | VARCHAR (254) |  |
| TITLE | VARCHAR (254) |  |
| ABBR | VARCHAR (254) |  |
| INTERNAL_ID | INTEGER |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | DATA_INDEXED_C | ZC_CNT_METRIC_EVNT | CNT_METRIC_EVNT_C | No | No | No |  |
| 1 | DATA_INDEXED_C | ZC_CONVERTED | CONVERTED_C | No | No | No |  |
| 1 | DATA_INDEXED_C | ZC_OP_MIXED_DEFAUL | OP_MIXED_DEFAUL_C | No | No | No |  |
| 1 | DATA_INDEXED_C | ZC_YES_NO | YES_NO_C | No | No | No |  |
