# OR_SER_SURG_SRVC

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=OR_SER_SURG_SRVC

## Description

The OR_SER_SURG_SRVC table contains OR management system surgical services.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | FULL |
| Load Frequency | WEEKLY - FULL |
| Chronicles INI | SER |
| Release Version | MU1 - MAY 2001 |
| May contain EHI? | No |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| PROV_ID | VARCHAR (18) | The unique ID for the surgical staff/resource record. |
| LINE | No | The total number of lines of surgical service information. |
| SERVICE_C | VARCHAR (66) |  |
| ALLOW_ALL_SERV_YN | VARCHAR (1) |  |
| LOC_ID | NUMERIC (18,0) | The unique ID of the authorized location for the staff/resource. |
| ALLOW_ALL_PROC_YN | VARCHAR (1) |  |
| CM_PHY_OWNER_ID | VARCHAR (25) | ID of the physical deployment owner for this record.  Physical owners will be where the data is hosted, either on the cross-over server or the owner deployment. |
| CM_LOG_OWNER_ID | VARCHAR (25) | ID of the logical deployment owner for this record.  Logical owners show the deployment where the record was created but doesn't represent if the record is a part of version skew. |
| CM_ACTV_DPLY_ID | No | The deployment ID of the deployment the PROV_ID comes from. |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| B-TREE INDEX | EIX_OR_SER_SURG_SRVC_LOID | LOC_ID | 1 | Yes | Yes |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | PROV_ID | CLARITY_SER | PROV_ID | Unknown | No | No |  |
| 1 | PROV_ID | CLARITY_SER_2 | PROV_ID | Unknown | No | No |  |
| 1 | PROV_ID | CLARITY_SER_3 | PROV_ID | Unknown | No | No |  |
| 1 | PROV_ID | CLARITY_SER_4 | PROV_ID | No | No | No |  |
| 1 | PROV_ID | CLARITY_SER_MYC | PROV_ID | Unknown | No | No |  |
| 1 | PROV_ID | D_PROV_PRIMARY_HIERARCHY | PROV_ID | Unknown | Unknown | No |  |
| 1 | PROV_ID | ED_SER_SETTINGS | PROV_ID | Unknown | No | No |  |
| 1 | PROV_ID | EXT_CAL_PROV_CONFIG | PROV_ID | No | No | No |  |
| 1 | PROV_ID | OR_SER_EQUIPMENT | PROV_ID | Unknown | No | No |  |
| 1 | PROV_ID | OR_SER_ROOM | PROV_ID | Unknown | No | No |  |
| 1 | PROV_ID | PROV_BATCH_LTR_GEN | PROV_ID | Unknown | No | No |  |
| 1 | PROV_ID | PROV_GROUP | PROV_ID | No | No | No |  |
| 1 | PROV_ID | V_CUBE_D_PROVIDER | PROVIDER_ID | Unknown | Unknown | No |  |
| 3 | SERVICE_C | ZC_OR_SERVICE | SERVICE_C | No | No | No |  |
| 5 | LOC_ID | ANALYTICS_SYSTEM_SETTINGS | FACILITY_ID | No | No | No |  |
| 5 | LOC_ID | ARPB_SA_SETTINGS | FACILITY_ID | No | No | No |  |
| 5 | LOC_ID | CLARITY_LOC | LOC_ID | Unknown | No | No |  |
| 5 | LOC_ID | CLARITY_LOC_2 | LOC_ID | Unknown | No | No |  |
| 5 | LOC_ID | CLARITY_POS | POS_ID | No | No | No |  |
| 5 | LOC_ID | CLARITY_POS_2 | POS_ID | No | No | No |  |
| 5 | LOC_ID | CLARITY_SA | SERV_AREA_ID | Unknown | No | No |  |
| 5 | LOC_ID | CL_LOC_HIERARCHY | LOC_ID | Unknown | No | No |  |
| 5 | LOC_ID | CV_PCI_D2B_SETTINGS | FACILITY_ID | No | No | No |  |
| 5 | LOC_ID | EAF_CLM_ALTADR_INF | FACILITY_ID | No | No | No |  |
| 5 | LOC_ID | EAF_CLM_RMT_SETUP | FACILITY_ID | No | No | No |  |
| 5 | LOC_ID | EAF_EXP_APPT_LOG | FACILITY_ID | No | No | No |  |
| 5 | LOC_ID | EAF_SEARCH_TERMS | FACILITY_ID | No | No | No |  |
| 5 | LOC_ID | ESCALATION_THRESH_SGL | FACILITY_ID | No | No | No |  |
| 5 | LOC_ID | FAC_CONNECT | FACILITY_ID | No | No | No |  |
| 5 | LOC_ID | FAC_DIRECT_ADDR | FACILITY_ID | Unknown | No | No |  |

_(50 total; showing first 30)_
