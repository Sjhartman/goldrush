# ZC_ALRTS_OVR_RSN

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=ZC_ALRTS_OVR_RSN

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
| ALRTS_OVR_RSN_C | INTEGER |  |
| NAME | VARCHAR (254) |  |
| TITLE | VARCHAR (254) |  |
| ABBR | VARCHAR (254) |  |
| INTERNAL_ID | INTEGER |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ALRTS_OVR_RSN_C | ZC_ALRT_SP_OVR_RSN | ALRT_SP_OVR_RSN_C | No | No | No |  |
