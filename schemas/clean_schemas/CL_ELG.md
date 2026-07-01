# CL_ELG

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=CL_ELG

## Description

This table contains information on allergens.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | ELG |
| Release Version | MU4 - EPIC 2002 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| ALLERGEN_ID | NUMERIC (18,0) | The ID of the allergen record. |
| ALLERGEN_NAME | VARCHAR (200) | The name of the allergen record. |
| RECORD_STATE_NAME | VARCHAR (50) |  |
| EDIT_NAME | VARCHAR (254) | The edit name of the allergen. This may also be used for the generic name of the allergen. |
| ALLERGEN_TYPE_C | INTEGER |  |
| INTRACTN_FWD_ID | NUMERIC (18,0) | This column contains the unique identifier for the "active" allergen record associated with a deleted allergen record. |
| MED_INTRCT_LINK | VARCHAR (40) | The medication interaction link |
| CM_PHY_OWNER_ID | VARCHAR (25) | ID of the physical deployment owner for this record.  Physical owners will be where the data is hosted, either on the cross-over server or the owner deployment. |
| CM_LOG_OWNER_ID | VARCHAR (25) | ID of the logical deployment owner for this record.  Logical owners show the deployment where the record was created but doesn't represent if the record is a part of version skew. |
| POTENTIAL_INACT_YN | VARCHAR (1) |  |
| IMPORTED_ALG_NAME | VARCHAR (254) | The name of the allergen as imported from the med load. |
| PROTECT_NAME_YN | VARCHAR (1) |  |
| COMMON_YN | VARCHAR (1) |  |
| SORT_PRIORITY | INTEGER | The higher the priority value the ealier its position in a sorted list. |
| LAST_IMP_UPD_I_DTTM | DATETIME (Local) | The instant of the last import update. |
| REPLACE_ALLERGEN_ID | NUMERIC (18,0) | Use this allergen record for interaction checking purposes rather than using the record itself. |
| VEN_IMPORT_STATUS_C | INTEGER |  |
| VEN_REPL_ALRGY_ID | NUMERIC (18,0) | This item stores a replacement for this allergen as defined by the medication data vendor. |
| PROTECT_IS_COMMON_YN | VARCHAR (1) |  |
| RECORD_STATE_C | INTEGER |  |
| ALRGY_ABSENCE_YN | VARCHAR (1) |  |
| USER_DEFINED_YN | VARCHAR (1) | Surrogate key used to uniquely identify rows in this (and only this) table on Cogito Cloud only, do not assume the surrogate key in this table will correspond to the surrogate key in another table |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 5 | ALLERGEN_TYPE_C | ZC_ALLERGEN_TYPE | ALLERGEN_TYPE_C | No | No | No |  |
| 6 | INTRACTN_FWD_ID | CL_ELG | ALLERGEN_ID | No | No | No |  |
| 8 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 8 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 8 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 9 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 9 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 9 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 16 | REPLACE_ALLERGEN_ID | CL_ELG | ALLERGEN_ID | No | No | No |  |
| 17 | VEN_IMPORT_STATUS_C | ZC_ELG_IMPORT_STAT | ELG_IMPORT_STATUS_C | No | No | No |  |
| 18 | VEN_REPL_ALRGY_ID | CL_ELG | ALLERGEN_ID | No | No | No |  |
| 20 | RECORD_STATE_C | ZC_DEL_STATUS | DEL_STATUS_C | No | No | No |  |
| 20 | RECORD_STATE_C | ZC_EDG_REC_STAT | EDG_REC_STAT_C | No | No | No |  |
| 20 | RECORD_STATE_C | ZC_ERS_REC_STAT | RECORD_STATUS_C | No | No | No |  |
| 20 | RECORD_STATE_C | ZC_HCD_REC_STATE | HCD_REC_STATE_C | No | No | No |  |
| 20 | RECORD_STATE_C | ZC_HFL_RECORD_STAT | HFL_RECORD_STAT_C | No | No | No |  |
| 20 | RECORD_STATE_C | ZC_IMM_REC_STATUS | IMM_REC_STATUS_C | No | No | No |  |
| 20 | RECORD_STATE_C | ZC_LLB_STATUS | LLB_STATUS_C | No | No | No |  |
| 20 | RECORD_STATE_C | ZC_LMA_RECORD_STAT | LMA_RECORD_STAT_C | No | No | No |  |
| 20 | RECORD_STATE_C | ZC_MEM_REC_STATUS | MEM_REC_STATUS_C | No | No | No |  |
| 20 | RECORD_STATE_C | ZC_OR_REC_STATUS | OR_REC_STATUS_C | No | No | No |  |
| 20 | RECORD_STATE_C | ZC_PBA_REC_STAT | PBA_REC_STAT_C | No | No | No |  |
| 20 | RECORD_STATE_C | ZC_PROV_REC_STATE | PROV_REC_STATE_C | No | No | No |  |
| 20 | RECORD_STATE_C | ZC_RECORD_STATE_2 | RECORD_STATE_2_C | No | No | No |  |
| 20 | RECORD_STATE_C | ZC_RECORD_STATE_3 | RECORD_STATE_3_C | No | No | No |  |
| 20 | RECORD_STATE_C | ZC_RECORD_STATE_4 | RECORD_STATE_4_C | No | No | No |  |
| 20 | RECORD_STATE_C | ZC_RECORD_STATE_6 | RECORD_STATE_6_C | No | No | No |  |
| 20 | RECORD_STATE_C | ZC_RECORD_STATE_7 | RECORD_STATE_7_C | No | No | No |  |
| 20 | RECORD_STATE_C | ZC_RECORD_STAT_EPM | RECORD_STAT_EPM_C | No | No | No |  |
| 20 | RECORD_STATE_C | ZC_RECORD_STAT_EPP | RECORD_STAT_EPP_C | No | No | No |  |

_(33 total; showing first 30)_
