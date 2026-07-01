# V_CUBE_D_PROVIDER

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=V_CUBE_D_PROVIDER

## Description

This view contains data from the CLARITY_SER table, optimized for use in SSAS Cubes.

## Metadata

| Property | Value |
| --- | --- |
| Type | View |
| Release Version | Rel 2012 |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| PROVIDER_ID | VARCHAR (18) | The unique ID assigned to the provider record. This ID can be encrypted. |
| PROVIDER_NAME | VARCHAR (200) | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| PROVIDER_DISPLAY_NAME | No | The name of the service provider concatenated with the provider ID. The format is "PROVIDER_NAME [PROVIDER_ID]". |
| PROVIDER_TYPE | CCA |  |
| STAFF_RESOURCE | VARCHAR (20) |  |
| PRIMARY_SPECIALTY | VARCHAR (254) |  |
| IS_RESIDENT_YN | VARCHAR (3) |  |
| CLINICIAN_TITLE | VARCHAR (66) |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | PROVIDER_ID | CLARITY_SER | PROV_ID | Unknown | Unknown | No |  |
| 1 | PROVIDER_ID | CLARITY_SER_2 | PROV_ID | Unknown | Unknown | No |  |
| 1 | PROVIDER_ID | CLARITY_SER_3 | PROV_ID | Unknown | Unknown | No |  |
| 1 | PROVIDER_ID | CLARITY_SER_4 | PROV_ID | No | Unknown | No |  |
| 1 | PROVIDER_ID | CLARITY_SER_MYC | PROV_ID | Unknown | Unknown | No |  |
| 1 | PROVIDER_ID | D_PROV_PRIMARY_HIERARCHY | PROV_ID | Unknown | Unknown | No |  |
| 1 | PROVIDER_ID | ED_SER_SETTINGS | PROV_ID | Unknown | Unknown | No |  |
| 1 | PROVIDER_ID | EXT_CAL_PROV_CONFIG | PROV_ID | No | Unknown | No |  |
| 1 | PROVIDER_ID | OR_SER_EQUIPMENT | PROV_ID | Unknown | Unknown | No |  |
| 1 | PROVIDER_ID | OR_SER_ROOM | PROV_ID | Unknown | Unknown | No |  |
| 1 | PROVIDER_ID | PROV_BATCH_LTR_GEN | PROV_ID | Unknown | Unknown | No |  |
| 1 | PROVIDER_ID | PROV_GROUP | PROV_ID | No | Unknown | No |  |
