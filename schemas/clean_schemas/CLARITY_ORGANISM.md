# CLARITY_ORGANISM

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=CLARITY_ORGANISM

## Description

The CLARITY_ORGANISM table contains basic information about the organisms used in clinical systems.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | FULL |
| Load Frequency | WEEKLY - FULL |
| Chronicles INI | LLO |
| Release Version | EPIC 2000 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| ORGANISM_ID | NUMERIC (18,0) | The unique ID of the organism record. |
| NAME | VARCHAR (254) | The name of the organism. |
| ABBREVIATION | VARCHAR (20) | The abbreviation of the organism?s name. |
| REC_STATE | VARCHAR (254) |  |
| CM_PHY_OWNER_ID | VARCHAR (25) | ID of the physical deployment owner for this record.  Physical owners will be where the data is hosted, either on the cross-over server or the owner deployment. |
| CM_LOG_OWNER_ID | VARCHAR (25) | ID of the logical deployment owner for this record.  Logical owners show the deployment where the record was created but doesn't represent if the record is a part of version skew. |
| RECORD_TYPE_C | INTEGER |  |
| RECORD_STATUS_C | INTEGER |  |
| ORGANISM_TYPE_C | INTEGER |  |
| ORGANISM_GROUP_C | INTEGER |  |
| GENUS_C | INTEGER |  |
| SPECIES_C | INTEGER |  |
| SEROTYPE_C | INTEGER |  |
| BIOTYPE_C | INTEGER |  |
| PHAGE_TYPE_C | INTEGER |  |
| RESULT_CHECKING_ID | NUMERIC (18,0) | Stores a link to the result checking record for this organism. |
| EXTERNAL_NAME | VARCHAR (254) | The external name for the organism. This can be mixed case, which is friendlier for reports. |
| MDRO_THRESHOLD | INTEGER | This column stores the minimum number of antibiotics/antibiotic classes that must match the given interpretations for the multidrug-resistant organism definition to apply. |
| MDRO_UPPER_THRESHOLD | INTEGER | This column stores the maximum number of antibiotics/antibiotic classes that are allowed to match the given interpretations for the multidrug-resistant organism definition to apply. |
| MDRO_ANY_ORGANISM_YN | VARCHAR (1) |  |
| RECORD_STATE_C | INTEGER | Surrogate key used to uniquely identify rows in this (and only this) table on Cogito Cloud only, do not assume the surrogate key in this table will correspond to the surrogate key in another table |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 5 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 5 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 5 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 6 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 6 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 6 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 7 | RECORD_TYPE_C | ZC_ORG_RECORD_TYPE | ORG_RECORD_TYPE_C | No | No | No |  |
| 8 | RECORD_STATUS_C | ZC_ORG_REC_STATUS | ORG_REC_STATUS_C | No | No | No |  |
| 9 | ORGANISM_TYPE_C | ZC_ORGANISM_TYPE | ORGANISM_TYPE_C | No | No | No |  |
| 10 | ORGANISM_GROUP_C | ZC_MICRO_GROUP | MICRO_GROUP_C | No | No | No |  |
| 11 | GENUS_C | ZC_MICRO_GENUS | MICRO_GENUS_C | No | No | No |  |
| 12 | SPECIES_C | ZC_MICRO_SPECIES | MICRO_SPECIES_C | No | No | No |  |
| 13 | SEROTYPE_C | ZC_SEROTYPE | SEROTYPE_C | No | No | No |  |
| 14 | BIOTYPE_C | ZC_BIOTYPE | BIOTYPE_C | No | No | No |  |
| 15 | PHAGE_TYPE_C | ZC_PHAGE_TYPE | PHAGE_TYPE_C | No | No | No |  |
| 16 | RESULT_CHECKING_ID | LAB_TRE_NOADD | RECORD_ID | Unknown | No | No |  |
| 21 | RECORD_STATE_C | ZC_DEL_STATUS | DEL_STATUS_C | No | No | No |  |
| 21 | RECORD_STATE_C | ZC_EDG_REC_STAT | EDG_REC_STAT_C | No | No | No |  |
| 21 | RECORD_STATE_C | ZC_ERS_REC_STAT | RECORD_STATUS_C | No | No | No |  |
| 21 | RECORD_STATE_C | ZC_HCD_REC_STATE | HCD_REC_STATE_C | No | No | No |  |
| 21 | RECORD_STATE_C | ZC_HFL_RECORD_STAT | HFL_RECORD_STAT_C | No | No | No |  |
| 21 | RECORD_STATE_C | ZC_IMM_REC_STATUS | IMM_REC_STATUS_C | No | No | No |  |
| 21 | RECORD_STATE_C | ZC_LLB_STATUS | LLB_STATUS_C | No | No | No |  |
| 21 | RECORD_STATE_C | ZC_LMA_RECORD_STAT | LMA_RECORD_STAT_C | No | No | No |  |
| 21 | RECORD_STATE_C | ZC_MEM_REC_STATUS | MEM_REC_STATUS_C | No | No | No |  |
| 21 | RECORD_STATE_C | ZC_OR_REC_STATUS | OR_REC_STATUS_C | No | No | No |  |
| 21 | RECORD_STATE_C | ZC_PBA_REC_STAT | PBA_REC_STAT_C | No | No | No |  |
| 21 | RECORD_STATE_C | ZC_PROV_REC_STATE | PROV_REC_STATE_C | No | No | No |  |
| 21 | RECORD_STATE_C | ZC_RECORD_STATE_2 | RECORD_STATE_2_C | No | No | No |  |
| 21 | RECORD_STATE_C | ZC_RECORD_STATE_3 | RECORD_STATE_3_C | No | No | No |  |

_(38 total; showing first 30)_
