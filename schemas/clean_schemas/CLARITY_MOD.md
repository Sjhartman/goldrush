# CLARITY_MOD

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=CLARITY_MOD

## Description

This table contains masterfile information on billing modifiers.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | FULL |
| Load Frequency | WEEKLY - FULL |
| Chronicles INI | MOD |
| Release Version | MU3 - EPIC 2002 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| MODIFIER_ID | VARCHAR (20) | The unique id of the modifier record |
| MODIFIER_NAME | VARCHAR (150) | The name of the modifier record. |
| EXTERNAL_ID | VARCHAR (25) | The external id of the modifier record. |
| PRICE_CHANGE_PCT | NUMERIC (12,2) | The percentage change the modifier has on a charge. |
| RVU_CHANGE_PCT | NUMERIC (12,2) | The percentage change the modifier has on an RVU value for a charge. |
| IS_NONPRICE_MOD_YN | VARCHAR (1) |  |
| IS_REPEATABLE_YN | VARCHAR (1) |  |
| AP_PRICE_CHG_PCT *(deprecated)* | NUMERIC (12,2) |  |
| SUPPRESS_CHOICE_C | INTEGER |  |
| CM_PHY_OWNER_ID | VARCHAR (25) | ID of the physical deployment owner for this record.  Physical owners will be where the data is hosted, either on the cross-over server or the owner deployment. |
| CM_LOG_OWNER_ID | VARCHAR (25) | ID of the logical deployment owner for this record.  Logical owners show the deployment where the record was created but doesn't represent if the record is a part of version skew. |
| IS_PHRM_MODIFIER_YN | VARCHAR (1) |  |
| AP_MOD_PRICING_C *(deprecated)* | INTEGER |  |
| PRIORITY | INTEGER | The priority of this modifier. |
| RECORD_STATUS_C | INTEGER |  |
| TYPE_OF_SERVICE_C | INTEGER |  |
| RVU_PRICING_MOD_YN | VARCHAR (1) |  |
| NL_SURCHARGE_CODE | VARCHAR (15) | Indicates whether a percentage change modifier is a Dutch surcharge and, if so, which surcharge code it represents. |
| NL_SURCHARGE_SPEC_C | VARCHAR (66) |  |
| NL_WDS_SERV_AREA_ID | NUMERIC (18,0) | For an internal ODV (WDS) modifier, this column gives the service area from which this modifier represents a request. |
| NL_REHAB_CODE | VARCHAR (30) | The Dutch rehab module that this modifier represents. |
| MOD_EFF_FROM_DATE | DATETIME | Date this modifier is effective from. |
| MOD_EFF_TO_DATE | DATETIME | Date this modifier is effective to. |
| MOD_UM_SERVICES_YN | VARCHAR (1) | Surrogate key used to uniquely identify rows in this (and only this) table on Cogito Cloud only, do not assume the surrogate key in this table will correspond to the surrogate key in another table |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 9 | SUPPRESS_CHOICE_C | ZC_SUPPRESS_CHOICE | SUPPRESS_CHOICE_C | No | No | No |  |
| 10 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 10 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 10 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 11 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 11 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 11 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 15 | RECORD_STATUS_C | ZC_DEL_STATUS | DEL_STATUS_C | No | No | No |  |
| 15 | RECORD_STATUS_C | ZC_EDG_REC_STAT | EDG_REC_STAT_C | No | No | No |  |
| 15 | RECORD_STATUS_C | ZC_ERS_REC_STAT | RECORD_STATUS_C | No | No | No |  |
| 15 | RECORD_STATUS_C | ZC_HCD_REC_STATE | HCD_REC_STATE_C | No | No | No |  |
| 15 | RECORD_STATUS_C | ZC_HFL_RECORD_STAT | HFL_RECORD_STAT_C | No | No | No |  |
| 15 | RECORD_STATUS_C | ZC_IMM_REC_STATUS | IMM_REC_STATUS_C | No | No | No |  |
| 15 | RECORD_STATUS_C | ZC_LLB_STATUS | LLB_STATUS_C | No | No | No |  |
| 15 | RECORD_STATUS_C | ZC_LMA_RECORD_STAT | LMA_RECORD_STAT_C | No | No | No |  |
| 15 | RECORD_STATUS_C | ZC_MEM_REC_STATUS | MEM_REC_STATUS_C | No | No | No |  |
| 15 | RECORD_STATUS_C | ZC_OR_REC_STATUS | OR_REC_STATUS_C | No | No | No |  |
| 15 | RECORD_STATUS_C | ZC_PBA_REC_STAT | PBA_REC_STAT_C | No | No | No |  |
| 15 | RECORD_STATUS_C | ZC_PROV_REC_STATE | PROV_REC_STATE_C | No | No | No |  |
| 15 | RECORD_STATUS_C | ZC_RECORD_STATE_2 | RECORD_STATE_2_C | No | No | No |  |
| 15 | RECORD_STATUS_C | ZC_RECORD_STATE_3 | RECORD_STATE_3_C | No | No | No |  |
| 15 | RECORD_STATUS_C | ZC_RECORD_STATE_4 | RECORD_STATE_4_C | No | No | No |  |
| 15 | RECORD_STATUS_C | ZC_RECORD_STATE_6 | RECORD_STATE_6_C | No | No | No |  |
| 15 | RECORD_STATUS_C | ZC_RECORD_STATE_7 | RECORD_STATE_7_C | No | No | No |  |
| 15 | RECORD_STATUS_C | ZC_RECORD_STAT_EPM | RECORD_STAT_EPM_C | No | No | No |  |
| 15 | RECORD_STATUS_C | ZC_RECORD_STAT_EPP | RECORD_STAT_EPP_C | No | No | No |  |
| 15 | RECORD_STATUS_C | ZC_RECORD_STAT_ETX | RECORD_STAT_ETX_C | No | No | No |  |
| 15 | RECORD_STATUS_C | ZC_RECORD_STAT_HRV | RECORD_STAT_HRV_C | No | No | No |  |
| 15 | RECORD_STATUS_C | ZC_RECORD_STAT_RMC | RECORD_STAT_RMC_C | No | No | No |  |
| 16 | TYPE_OF_SERVICE_C | ZC_EAP_TYPE_OF_SER | EAP_TYPE_OF_SER_C | No | No | No |  |

_(67 total; showing first 30)_
