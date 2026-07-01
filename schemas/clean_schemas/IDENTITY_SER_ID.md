# IDENTITY_SER_ID

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=IDENTITY_SER_ID

## Description

The IDENTITY_SER_ID table contains the system master person index ID numbers for your providers. Each provider may have multiple master person index IDs; therefore, a line number is used to identify each identification number for a provider.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | SER |
| Release Version | EPIC 2002 |
| May contain EHI? | No |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| PROV_ID | VARCHAR (18) | The unique ID assigned to the provider record. This ID may be encrypted if you have elected to use enterprise reporting?s encryption utility. |
| LINE | No | The line number of the provider ID within the provider?s record. |
| IDENTITY_ID | VARCHAR (150) | The identification number associated with the provider. This ID may be encrypted. |
| IDENTITY_TYPE_ID | NUMERIC (18,0) | The system master person index ID type corresponding to this identification number for the provider. |
| CM_PHY_OWNER_ID | VARCHAR (25) | ID of the physical deployment owner for this record.  Physical owners will be where the data is hosted, either on the cross-over server or the owner deployment. |
| CM_LOG_OWNER_ID | VARCHAR (25) | ID of the logical deployment owner for this record.  Logical owners show the deployment where the record was created but doesn't represent if the record is a part of version skew. |
| MPI_ID_FROM_DATE | DATETIME | The effective from date for the MPI ID on the record. |
| MPI_ID_TO_DATE | DATETIME | The effective to date of the MPI ID on the record. |
| MPI_RET_CHK_PP_ID | NUMERIC (18,0) | MPI Retrieval Check Programming Point |
| MPI_RET_CHK_RULE_ID | VARCHAR (18) | MPI Retrieval check rule |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| B-TREE INDEX | EIX_IDENTITY_SER_ID_IDID | IDENTITY_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_IDENTITY_SER_ID_IDTYID | IDENTITY_TYPE_ID | 1 | Yes | Yes |  |

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
| 4 | IDENTITY_TYPE_ID | IDENTITY_ID_TYPE | ID_TYPE | No | No | No |  |
| 4 | IDENTITY_TYPE_ID | V_ZZLOV_DRG_TYPES | DRG_ID_TYPE_ID | Unknown | Unknown | No |  |
| 5 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 5 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 5 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 6 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 6 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 6 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 9 | MPI_RET_CHK_PP_ID | CLARITY_LPP | LPP_ID | Unknown | No | No |  |
| 10 | MPI_RET_CHK_RULE_ID | CLARITY_CER | RULE_ID | No | No | No |  |
| 10 | MPI_RET_CHK_RULE_ID | CL_CHRG_EDIT_RULE | RULE_ID | No | No | No |  |
