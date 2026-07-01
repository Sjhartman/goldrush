# ZC_ORD_BLOB_TYPE

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=ZC_ORD_BLOB_TYPE

## Description

Category table

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | FULL |
| Load Frequency | INCREMENTAL |
| Chronicles INI | N/A |
| Release Version | MU5 - EPIC 2002 |
| May contain EHI? | No |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| ORD_BLOB_TYPE_C | INTEGER |  |
| NAME | VARCHAR (254) |  |
| TITLE | VARCHAR (254) |  |
| ABBR | VARCHAR (254) |  |
| INTERNAL_ID | INTEGER |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ORD_BLOB_TYPE_C | ZC_OBJECT_BLOB_TYPE | OBJECT_BLOB_TYPE_C | No | No | No |  |
