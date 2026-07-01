# ZC_MSG_CALLER_REL

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=ZC_MSG_CALLER_REL

## Description

The ZC_MSG_CALLER_REL table contains the name, title, abbreviation, and internal ID of the category for the relationship between the caller and the patient.

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
| MSG_CALLER_REL_C | 19350 |  |
| NAME | 19350 |  |
| TITLE | 19350 |  |
| ABBR | 19350 |  |
| INTERNAL_ID | 19350 |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | MSG_CALLER_REL_C | ZC_RELATION | RELATION_C | No | No | No |  |
