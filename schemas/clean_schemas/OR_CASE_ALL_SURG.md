# OR_CASE_ALL_SURG

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=OR_CASE_ALL_SURG

## Description

The OR_CASE_ALL_SURG table contains OR management system case surgeons.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | ORC |
| Release Version | MU1 - MAY 2001 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| OR_CASE_ID | VARCHAR (18) | The unique ID of the case record. |
| LINE | No | The number of the lines of the surgeon within the case. |
| SURG_ID | VARCHAR (18) | The unique ID of the surgeon within the case. |
| ROLE_C | INTEGER |  |
| SERVICE_C | VARCHAR (66) |  |
| CASE_BEGIN | INTEGER | The start time for the surgeon within the case. |
| CAE_END | INTEGER | The end time for the surgeon within the case. |
| TOTAL_LENGTH | INTEGER | The total number of minutes the surgeon is needed within the case. |
| PANEL | INTEGER | The procedure panel within which this surgeon is performing a procedure. This is a numeric value between 1 and 5. |
| CM_PHY_OWNER_ID | VARCHAR (25) | ID of the physical deployment owner for this record.  Physical owners will be where the data is hosted, either on the cross-over server or the owner deployment. |
| CM_LOG_OWNER_ID | VARCHAR (25) | ID of the logical deployment owner for this record.  Logical owners show the deployment where the record was created but doesn't represent if the record is a part of version skew. |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| B-TREE INDEX | EIX_OR_CASE_ALL_SURG_ROC | ROLE_C | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_OR_CASE_ALL_SURG_SEC | SERVICE_C | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_OR_CASE_ALL_SURG_SUID | SURG_ID | 1 | Yes | Yes |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | OR_CASE_ID | OR_CASE | OR_CASE_ID | Unknown | No | No |  |
| 1 | OR_CASE_ID | OR_CASE_2 | CASE_ID | Unknown | No | No |  |
| 1 | OR_CASE_ID | OR_CASE_3 | CASE_ID | Unknown | No | No |  |
| 1 | OR_CASE_ID | OR_CASE_4 | OR_CASE_ID | No | No | No |  |
| 1 | OR_CASE_ID | OR_CASE_VIRTUAL | OR_CASE_ID | No | No | No |  |
| 1 | OR_CASE_ID | V_OR_CASE_ORR | CASE_ID | Unknown | Unknown | No |  |
| 3 | SURG_ID | CLARITY_SER | PROV_ID | Unknown | No | No |  |
| 3 | SURG_ID | CLARITY_SER_2 | PROV_ID | Unknown | No | No |  |
| 3 | SURG_ID | CLARITY_SER_3 | PROV_ID | Unknown | No | No |  |
| 3 | SURG_ID | CLARITY_SER_4 | PROV_ID | No | No | No |  |
| 3 | SURG_ID | CLARITY_SER_MYC | PROV_ID | Unknown | No | No |  |
| 3 | SURG_ID | D_PROV_PRIMARY_HIERARCHY | PROV_ID | Unknown | Unknown | No |  |
| 3 | SURG_ID | ED_SER_SETTINGS | PROV_ID | Unknown | No | No |  |
| 3 | SURG_ID | EXT_CAL_PROV_CONFIG | PROV_ID | No | No | No |  |
| 3 | SURG_ID | OR_SER_EQUIPMENT | PROV_ID | Unknown | No | No |  |
| 3 | SURG_ID | OR_SER_ROOM | PROV_ID | Unknown | No | No |  |
| 3 | SURG_ID | PROV_BATCH_LTR_GEN | PROV_ID | Unknown | No | No |  |
| 3 | SURG_ID | PROV_GROUP | PROV_ID | No | No | No |  |
| 3 | SURG_ID | V_CUBE_D_PROVIDER | PROVIDER_ID | Unknown | Unknown | No |  |
| 4 | ROLE_C | ZC_OR_PANEL_ROLE | ROLE_C | No | No | No |  |
| 5 | SERVICE_C | ZC_OR_SERVICE | SERVICE_C | No | No | No |  |
| 10 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 10 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 10 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 11 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 11 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 11 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
