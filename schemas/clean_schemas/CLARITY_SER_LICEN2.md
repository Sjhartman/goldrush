# CLARITY_SER_LICEN2

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=CLARITY_SER_LICEN2

## Description

The CLARITY_SER_LICEN2 table includes basic license information for providers.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | FULL |
| Load Frequency | WEEKLY - FULL |
| Chronicles INI | SER |
| Release Version | MU4 - MAY 2001 |
| May contain EHI? | No |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| PROV_ID | VARCHAR (18) | The unique ID of the provider. |
| LINE | No | The line count of the license for the provider. |
| LICENSE_TYPE | VARCHAR (40) | The practice for which this provider is licensed. |
| LICENSE_NUM | VARCHAR (40) | The license number for this provider. |
| LICENSE_EXP_DATE | DATETIME | The expiration date of the license for this provider. |
| CM_PHY_OWNER_ID | VARCHAR (25) | ID of the physical deployment owner for this record.  Physical owners will be where the data is hosted, either on the cross-over server or the owner deployment. |
| CM_LOG_OWNER_ID | VARCHAR (25) | ID of the logical deployment owner for this record.  Logical owners show the deployment where the record was created but doesn't represent if the record is a part of version skew. |
| LICENSE_STATE_C | VARCHAR (66) |  |

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
| 6 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 6 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 6 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 7 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 7 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 7 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 8 | LICENSE_STATE_C | ZC_ALT_INVOICE_STA | ALT_INVOICE_STA_C | No | No | No |  |
| 8 | LICENSE_STATE_C | ZC_LLB_STATE | LLB_STATE_C | No | No | No |  |
| 8 | LICENSE_STATE_C | ZC_REFG_PROV_STATE | REFG_PROV_STATE_C | No | No | No |  |
| 8 | LICENSE_STATE_C | ZC_STATE | STATE_C | No | No | No |  |
| 8 | LICENSE_STATE_C | ZC_STATE_HISTORY | STATE_HISTORY_C | No | No | No |  |
| 8 | LICENSE_STATE_C | ZC_SUBSCR_EEP_STE | SUBSCR_EEP_STE_C | No | No | No |  |
| 8 | LICENSE_STATE_C | ZC_TAX_STATE | TAX_STATE_C | No | No | No |  |
