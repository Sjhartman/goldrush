# ZC_SPEC_SOURCE

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=ZC_SPEC_SOURCE

## Description

This table contains the category information for specimen sources.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | FULL |
| Load Frequency | INCREMENTAL |
| Chronicles INI | N/A |
| Release Version | FALL 2004 |
| May contain EHI? | No |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| SPEC_SOURCE_C | INTEGER |  |
| NAME | VARCHAR (254) |  |
| TITLE | VARCHAR (254) |  |
| ABBR | VARCHAR (254) |  |
| INTERNAL_ID | INTEGER |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | SPEC_SOURCE_C | ZC_SPECIMEN_SOURCE | SPECIMEN_SOURCE_C | No | No | No |  |
| 1 | SPEC_SOURCE_C | ZC_SPECIMEN_SRC_2 | SPECIMEN_SRC_2_C | No | No | No |  |
