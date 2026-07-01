# ZC_RECORD_STS

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=ZC_RECORD_STS

## Description

Contains a list of record statuses used for order event actions.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | FULL |
| Load Frequency | INCREMENTAL |
| Chronicles INI | N/A |
| Release Version | Summer 2009 |
| May contain EHI? | No |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| RECORD_STS_C | 5 |  |
| NAME | 5 |  |
| TITLE | 5 |  |
| ABBR | 5 |  |
| INTERNAL_ID | 5 |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | RECORD_STS_C | ZC_RECORD_STATUS_2 | RECORD_STATUS_2_C | No | No | No |  |
