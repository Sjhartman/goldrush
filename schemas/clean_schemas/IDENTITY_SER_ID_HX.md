# IDENTITY_SER_ID_HX

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=IDENTITY_SER_ID_HX

## Description

The IDENTITY_SER_ID_HX table contains the system master person index ID History for your providers. Each provider may have multiple master person index IDs; therefore, a line number is used to identify each identification number for a provider. A row will only exist in this table if an ID is no longer valid for an SER record.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | FULL |
| Load Frequency | WEEKLY - FULL |
| Chronicles INI | SER |
| Release Version | EPIC 2002 |
| May contain EHI? | No |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| PROV_ID | VARCHAR (18) | The unique ID assigned to the provider record. This ID may be encrypted if you have elected to use enterprise reporting?s encryption utility. |
| LINE | No | The line number of the provider ID within the provider?s record. |
| ID_HX | VARCHAR (150) | The old master person index ID for the provider record. |
| ID_CHG_TIME | DATETIME (Attached) | The date the ID type was changed. |
| ID_TYPE_HX | NUMERIC (18,0) | The old master person index ID Type for the provider record. |
| ID_CHG_USER_ID | VARCHAR (18) | The user that made the change. |
| IDENTITY_NEW_ID | VARCHAR (150) | The ID that is now active for this ID Type. |
| OLD_PROV_ID | VARCHAR (50) | The provider's old system ID number. This ID no longer exists in either database. |
| FROM_DATE | DATETIME | The date the ID becomes active. |
| TO_DATE | DATETIME | The date the ID was made inactive. |
| CM_PHY_OWNER_ID | VARCHAR (25) | ID of the physical deployment owner for this record.  Physical owners will be where the data is hosted, either on the cross-over server or the owner deployment. |
| CM_LOG_OWNER_ID | VARCHAR (25) | ID of the logical deployment owner for this record.  Logical owners show the deployment where the record was created but doesn't represent if the record is a part of version skew. |
| MPI_AUDIT_TYPE_C | INTEGER |  |

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
| 5 | ID_TYPE_HX | IDENTITY_ID_TYPE | ID_TYPE | No | No | No |  |
| 5 | ID_TYPE_HX | V_ZZLOV_DRG_TYPES | DRG_ID_TYPE_ID | Unknown | Unknown | No |  |
| 6 | ID_CHG_USER_ID | CLARITY_EMP | USER_ID | Unknown | No | No |  |
| 6 | ID_CHG_USER_ID | CLARITY_EMP_2 | USER_ID | Unknown | No | No |  |
| 6 | ID_CHG_USER_ID | CLARITY_EMP_3 | USER_ID | Unknown | No | No |  |
| 6 | ID_CHG_USER_ID | CLARITY_EMP_4 | USER_ID | No | No | No |  |
| 6 | ID_CHG_USER_ID | CLARITY_EMP_DEMO | USER_ID | No | No | No |  |
| 6 | ID_CHG_USER_ID | EMP_BASIC_INFO | USER_ID | No | No | No |  |
| 6 | ID_CHG_USER_ID | EMP_DOC_SETTINGS | USER_NUMBER_ID | No | No | No |  |
| 6 | ID_CHG_USER_ID | F_RX_USER | USER_ID | Unknown | Unknown | No |  |
| 6 | ID_CHG_USER_ID | IB_MESSAGE_SETTINGS | USER_ID | No | No | No |  |
| 6 | ID_CHG_USER_ID | LOGIN_INFO | USER_NUMBER_ID | No | No | No |  |
| 6 | ID_CHG_USER_ID | QC_RESULTS_REVIEW | USER_NUMBER_ID | No | No | No |  |
| 6 | ID_CHG_USER_ID | USER_SIDEBAR_RPT | USER_NUMBER_ID | Unknown | No | No |  |
| 6 | ID_CHG_USER_ID | V_CUBE_D_USER | USER_ID | Unknown | Unknown | No |  |
| 6 | ID_CHG_USER_ID | V_CUBE_RX_USER | USER_ID | Unknown | Unknown | No |  |
| 11 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |

_(36 total; showing first 30)_
