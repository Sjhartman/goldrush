# ZC_TX_CURRENT_STAG

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=ZC_TX_CURRENT_STAG

## Description

Category table for transplant stage

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | FULL |
| Load Frequency | INCREMENTAL |
| Chronicles INI | N/A |
| Release Version | SPRING 2007 |
| May contain EHI? | No |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| TX_CURRENT_STAG_C | 30105 |  |
| NAME | 30105 |  |
| TITLE | 30105 |  |
| ABBR | 30105 |  |
| INTERNAL_ID | 30105 |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | TX_CURRENT_STAG_C | ZC_TX_STAT | TX_STAT_C | No | No | No |  |
