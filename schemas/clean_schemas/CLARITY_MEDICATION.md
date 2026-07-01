# CLARITY_MEDICATION

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=CLARITY_MEDICATION

## Description

The CLARITY_MEDICATION table contains high-level information from all the medications for use in your facility.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | ERX |
| Release Version | EPIC 2000 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| MEDICATION_ID | NUMERIC (18,0) | The unique ID of the medication record. |
| NAME | VARCHAR (255) | The name of the medication. |
| THERA_CLASS_C | INTEGER |  |
| PHARM_CLASS_C | INTEGER |  |
| PHARM_SUBCLASS_C | INTEGER |  |
| SIMPLE_GENERIC_C | VARCHAR (66) |  |
| COST | VARCHAR (254) | The cost of the drug, in accordance with the scheme chosen by your facility. |
| GENERIC_NAME | VARCHAR (200) | The first line of the generic, non-proprietary name for this medication. |
| GPI | VARCHAR (192) | The Generic Product Identifier for the medication:  first line of Item ERX 210. |
| STRENGTH | VARCHAR (254) | The strength of this NDC version of the drug, for example, ?10%, ? or ?50 mg/ml.? |
| FORM *(deprecated)* | VARCHAR (50) |  |
| ROUTE *(deprecated)* | VARCHAR (50) |  |
| CONTROLLED_MED_YN | VARCHAR (1) |  |
| DEA_CLASS_CODE_C | INTEGER |  |
| RECORD_STATE *(deprecated)* | VARCHAR (50) |  |
| CM_PHY_OWNER_ID | VARCHAR (25) | ID of the physical deployment owner for this record.  Physical owners will be where the data is hosted, either on the cross-over server or the owner deployment. |
| CM_LOG_OWNER_ID | VARCHAR (25) | ID of the logical deployment owner for this record.  Logical owners show the deployment where the record was created but doesn't represent if the record is a part of version skew. |
| INVESTIGATL_MED_YN | VARCHAR (1) |  |
| DAY_SUP_ENABLE_YN | VARCHAR (1) |  |
| EQUIP_STATUS_YN | VARCHAR (1) |  |
| MED_IS_CONFIGURED_C | INTEGER | Surrogate key used to uniquely identify rows in this (and only this) table on Cogito Cloud only, do not assume the surrogate key in this table will correspond to the surrogate key in another table |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| B-TREE INDEX | EIX_CLARITY_MED_GPI_MED | GPI | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_CLARITY_MED_GPI_MED | MEDICATION_ID | 2 | Yes | Yes |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | MEDICATION_ID | MED_ADS_INFO | MEDICATION_ID | No | No | No |  |
| 1 | MEDICATION_ID | RX_MED_FIVE | MEDICATION_ID | No | No | No |  |
| 1 | MEDICATION_ID | RX_MED_FOUR | MEDICATION_ID | No | No | No |  |
| 1 | MEDICATION_ID | RX_MED_ONE | MEDICATION_ID | No | No | No |  |
| 1 | MEDICATION_ID | RX_MED_THREE | MEDICATION_ID | No | No | No |  |
| 1 | MEDICATION_ID | RX_MED_TWO | MEDICATION_ID | No | No | No |  |
| 1 | MEDICATION_ID | V_CUBE_D_MEDICATION | MEDICATION_ID | Unknown | Unknown | No |  |
| 3 | THERA_CLASS_C | ZC_THERA_CLASS | THERA_CLASS_C | No | No | No |  |
| 4 | PHARM_CLASS_C | ZC_PHARM_CLASS | PHARM_CLASS_C | No | No | No |  |
| 5 | PHARM_SUBCLASS_C | ZC_PHARM_SUBCLASS | PHARM_SUBCLASS_C | No | No | No |  |
| 6 | SIMPLE_GENERIC_C | ZC_SIMPLE_GENERIC | SIMPLE_GENERIC_C | No | No | No |  |
| 14 | DEA_CLASS_CODE_C | ZC_DEA_CLASS_CODE | DEA_CLASS_CODE_C | No | No | No |  |
| 16 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 16 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 16 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 17 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 17 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 17 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 21 | MED_IS_CONFIGURED_C | ZC_MED_IS_CONFIGURED | MED_IS_CONFIGURED_C | No | No | No |  |
