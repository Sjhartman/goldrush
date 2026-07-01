# ZC_MC_PAT_STATUS

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=ZC_MC_PAT_STATUS

## Description

This table contains the category items for the discharge disposition/patient status.

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
| PAT_STATUS_C | VARCHAR (66) |  |
| NAME | VARCHAR (254) |  |
| TITLE | VARCHAR (254) |  |
| ABBR | VARCHAR (254) |  |
| INTERNAL_ID | VARCHAR (66) |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | PAT_STATUS_C | ZC_ER_PAT_STS_HA | ER_PAT_STS_HA_C | No | No | No |  |
