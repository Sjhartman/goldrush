# OR_GRP_SURGEON

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=OR_GRP_SURGEON

## Description

The OR_GRP_SURGEON table contains OR management system surgeon groups.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | FULL |
| Load Frequency | WEEKLY - FULL |
| Chronicles INI | OGP |
| Release Version | MU1 - MAY 2001 |
| May contain EHI? | No |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| GROUP_ID | VARCHAR (18) | The unique ID of the surgeon group record. |
| LINE | No | The number of the line of the surgeon information within the group. |
| SURGEONS_ID | VARCHAR (18) | The unique ID of the surgeon in the group. |
| CM_PHY_OWNER_ID | VARCHAR (25) | ID of the physical deployment owner for this record.  Physical owners will be where the data is hosted, either on the cross-over server or the owner deployment. |
| CM_LOG_OWNER_ID | VARCHAR (25) | ID of the logical deployment owner for this record.  Logical owners show the deployment where the record was created but doesn't represent if the record is a part of version skew. |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| B-TREE INDEX | EIX_OR_GRP_SURGEON_SUID | SURGEONS_ID | 1 | Yes | Yes |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | GROUP_ID | OR_GRP | GROUP_ID | Unknown | No | No |  |
| 3 | SURGEONS_ID | CLARITY_SER | PROV_ID | Unknown | No | No |  |
| 3 | SURGEONS_ID | CLARITY_SER_2 | PROV_ID | Unknown | No | No |  |
| 3 | SURGEONS_ID | CLARITY_SER_3 | PROV_ID | Unknown | No | No |  |
| 3 | SURGEONS_ID | CLARITY_SER_4 | PROV_ID | No | No | No |  |
| 3 | SURGEONS_ID | CLARITY_SER_MYC | PROV_ID | Unknown | No | No |  |
| 3 | SURGEONS_ID | D_PROV_PRIMARY_HIERARCHY | PROV_ID | Unknown | Unknown | No |  |
| 3 | SURGEONS_ID | ED_SER_SETTINGS | PROV_ID | Unknown | No | No |  |
| 3 | SURGEONS_ID | EXT_CAL_PROV_CONFIG | PROV_ID | No | No | No |  |
| 3 | SURGEONS_ID | OR_SER_EQUIPMENT | PROV_ID | Unknown | No | No |  |
| 3 | SURGEONS_ID | OR_SER_ROOM | PROV_ID | Unknown | No | No |  |
| 3 | SURGEONS_ID | PROV_BATCH_LTR_GEN | PROV_ID | Unknown | No | No |  |
| 3 | SURGEONS_ID | PROV_GROUP | PROV_ID | No | No | No |  |
| 3 | SURGEONS_ID | V_CUBE_D_PROVIDER | PROVIDER_ID | Unknown | Unknown | No |  |
| 4 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 4 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 4 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 5 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 5 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 5 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
