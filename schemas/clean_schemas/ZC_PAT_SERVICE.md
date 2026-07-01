# ZC_PAT_SERVICE

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=ZC_PAT_SERVICE

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
| HOSP_SERV_C | VARCHAR (66) |  |
| NAME | VARCHAR (254) |  |
| TITLE | VARCHAR (254) |  |
| ABBR | VARCHAR (254) |  |
| INTERNAL_ID | VARCHAR (66) |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | HOSP_SERV_C | ZC_PRIM_SVC_HA | PRIM_SVC_HA_C | No | No | No |  |
| 1 | HOSP_SERV_C | ZC_SCNDRY_SVC_HA | SCNDRY_SVC_HA_C | No | No | No |  |
| 5 | INTERNAL_ID | ZC_PAT_SERVICE | HOSP_SERV_C | No | No | No |  |
| 5 | INTERNAL_ID | ZC_PRIM_SVC_HA | PRIM_SVC_HA_C | No | No | No |  |
| 5 | INTERNAL_ID | ZC_SCNDRY_SVC_HA | SCNDRY_SVC_HA_C | No | No | No |  |
