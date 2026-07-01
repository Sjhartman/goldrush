# ZC_ALCOHOL_USE

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=ZC_ALCOHOL_USE

## Description

This is the table for I EPT 19220 category.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | FULL |
| Load Frequency | INCREMENTAL |
| Chronicles INI | N/A |
| Release Version | Rel 2012 |
| May contain EHI? | No |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| ALCOHOL_USE_C | INTEGER |  |
| NAME | VARCHAR (254) |  |
| TITLE | VARCHAR (254) |  |
| ABBR | VARCHAR (254) |  |
| INTERNAL_ID | INTEGER |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ALCOHOL_USE_C | ZC_OB_PREG_HX | OB_PREG_HX_C | No | No | No |  |
