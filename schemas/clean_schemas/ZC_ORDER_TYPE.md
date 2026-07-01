# ZC_ORDER_TYPE

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=ZC_ORDER_TYPE

## Description

This table contains information for the order type category list.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | FULL |
| Load Frequency | INCREMENTAL |
| Chronicles INI | N/A |
| Release Version | EPIC 2000 |
| May contain EHI? | No |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| ORDER_TYPE_C | INTEGER |  |
| NAME | VARCHAR (254) |  |
| TITLE | VARCHAR (254) |  |
| ABBR | VARCHAR (254) |  |
| INTERNAL_ID | INTEGER |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ORDER_TYPE_C | ZC_DFLT_ORDER_TYPE | DFLT_ORDER_TYPE_C | No | No | No |  |
| 1 | ORDER_TYPE_C | ZC_EDP_ORDER_TYPE | ORDER_TYPE_C | No | No | No |  |
