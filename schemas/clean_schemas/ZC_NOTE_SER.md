# ZC_NOTE_SER

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=ZC_NOTE_SER

## Description

This table contains information about the provider type category.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | FULL |
| Load Frequency | INCREMENTAL |
| Chronicles INI | N/A |
| Release Version | EPIC 2002 |
| May contain EHI? | No |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| SERVICE_TYPE_C | CCA |  |
| NAME | CCA |  |
| TITLE | CCA |  |
| ABBR | CCA |  |
| INTERNAL_ID | CCA |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | SERVICE_TYPE_C | ZC_PROV_TYPE | PROV_TYPE_C | No | No | No |  |
