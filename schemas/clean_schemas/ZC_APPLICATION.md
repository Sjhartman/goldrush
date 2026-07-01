# ZC_APPLICATION

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=ZC_APPLICATION

## Description

This table contains the category information contained in E0B 10015.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | FULL |
| Load Frequency | INCREMENTAL |
| Chronicles INI | N/A |
| Release Version | MU6 - EPIC 2002 |
| May contain EHI? | No |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| APPLICATION_C | INTEGER |  |
| NAME | VARCHAR (254) |  |
| TITLE | VARCHAR (254) |  |
| ABBR | VARCHAR (254) |  |
| INTERNAL_ID | INTEGER |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | APPLICATION_C | ZC_ACTIVE_APPS | ACTIVE_APPS_C | No | No | No |  |
