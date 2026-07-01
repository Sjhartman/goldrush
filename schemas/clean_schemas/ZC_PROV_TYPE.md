# ZC_PROV_TYPE

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=ZC_PROV_TYPE

## Description

This table will be deprecated in a future release. You should use ZC_NOTE_SER when reporting on this category list.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | FULL |
| Load Frequency | INCREMENTAL |
| Chronicles INI | N/A |
| Release Version | MU4 - EPIC 2002 |
| May contain EHI? | No |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| PROV_TYPE_C | VARCHAR (66) |  |
| NAME | VARCHAR (254) |  |
| TITLE | VARCHAR (254) |  |
| ABBR | VARCHAR (254) |  |
| INTERNAL_ID | VARCHAR (66) |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | PROV_TYPE_C | ZC_NOTE_SER | SERVICE_TYPE_C | No | No | No |  |
