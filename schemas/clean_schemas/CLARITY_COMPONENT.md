# CLARITY_COMPONENT

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=CLARITY_COMPONENT

## Description

The CLARITY_COMPONENT table contains basic information about the standard result components that can constitute your procedures. For example, the components of a lab panel are usually the tests performed on a single specimen.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | LRR |
| Release Version | EPIC 2000 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| COMPONENT_ID | NUMERIC (18,0) | The unique ID of the component record. |
| NAME | VARCHAR (75) | The name of the component. |
| ABBREVIATION | VARCHAR (40) | The abbreviated version of the component?s name. |
| EXTERNAL_NAME | VARCHAR (75) | The external name or alias of the result component name. |
| BASE_NAME | VARCHAR (75) | The name used by clinical system?s Best Practice Alerts to group related components. |
| CM_PHY_OWNER_ID | VARCHAR (25) | ID of the physical deployment owner for this record.  Physical owners will be where the data is hosted, either on the cross-over server or the owner deployment. |
| CM_LOG_OWNER_ID | VARCHAR (25) | ID of the logical deployment owner for this record.  Logical owners show the deployment where the record was created but doesn't represent if the record is a part of version skew. |
| COMPONENT_TYPE_C | INTEGER |  |
| LAB_DEFINITIONS_YN | VARCHAR (254) |  |
| LAB_DATA_TYPE_C | INTEGER |  |
| LAB_CAT_INI | VARCHAR (254) | If lab definitions and data type is category, the Chronicles' INI that hosts the category list. |
| LAB_CAT_ITEM | NUMERIC (14,2) | If lab definitions and data type is category, the Chronicles' item that hosts the category list. |
| LAB_CAT_DISPLY_C | INTEGER |  |
| LAB_CAT_DISCRIM | VARCHAR (254) | If lab definitions and data type is category, the discrimination code that limits the categories made available during lab result entry. This setting is discontinued and no longer affects end user workflows. |
| LAB_NUM_PRECISION | NUMERIC (12,0) | If lab definitions and data type is numeric, the number of decimal places to use. |
| LAB_TRUNCATE_YN | VARCHAR (254) |  |
| LAB_LTGT_DISBLD_YN | VARCHAR (254) |  |
| LAB_NUM_PRV_VALUES *(deprecated)* | NUMERIC (12,0) | Deprecated. Use the COMPONENT_LOOKBACK table in place of this column.. |
| LAB_DAYS_LOOKBACK *(deprecated)* | NUMERIC (12,0) | Deprecated. Use the COMPONENT_LOOKBACK table in place of this column. |
| LAB_ANTIBIOTIC_C | INTEGER |  |
| COMMON_NAME | VARCHAR (254) | The common name can be used to gather multiple components with different names that actually refer to the same thing, for example Na and Sodium. |
| LOINC_CODE | VARCHAR (254) | Free text LOINC code associated with a component. This field is for reference or lookup only, no Epic functionality is driven by this field. |
| RESULT_CHECKING_ID | NUMERIC (18,0) | Links to result checking setup (TRE) for this component. |
| ALLOW_DILUTION_YN | VARCHAR (1) |  |
| COMPONENT_SUBTYPE_C | INTEGER |  |
| RECORD_STATE_C | INTEGER |  |
| DEFAULT_LOW | VARCHAR (254) | If no result ranges are specified for an age range or resulting agency, this is the default value below which results are marked as low. |
| DEFAULT_HIGH | VARCHAR (254) | If no result ranges are specified for an age range or resulting agency, this is the default value above which results are marked as high. |
| DFLT_UNITS | VARCHAR (254) | If no units are specified for an age range or a resulting agency, this unit is used when printing result values. |
| DFLT_LOW_FEMALE | VARCHAR (254) | If no female-specific result ranges are specified for an age range or a resulting agency, this is the value below which the result entry will be marked as low for female patients. |
| DFLT_HIGH_FEMALE | VARCHAR (254) | If no female-specific result ranges are specified for an age range or a resulting agency, this is the value above which the result entry will be marked as high for female patients. |
| DISPLAY_YN | VARCHAR (1) |  |
| QC_NUM_PRECISION | NUMERIC (2,0) | The number of digits past the decimal point that should be stored for numeric results in QC tests. |
| ANTIBIOTIC_MED_ID | NUMERIC (18,0) | Link to a medication record. This is set only for antibiotic components. |
| LAB_SUBTYPE_C | INTEGER |  |
| LAB_OWC_USE_TYPE_C | INTEGER |  |
| CALCULATED_LRR_YN | VARCHAR (1) |  |
| DEFAULT_LNC_ID | NUMERIC (18,0) | The unique ID of the LOINC (LNC) record that will be used if no complex mapping of LOINC codes has been done, or if there is no match in the complex mapping table. |
| NHSN_CODE_ID | NUMERIC (18,0) | This is an Epic-released HLX record which corresponds to an NHSN-specific code associated with a drug susceptibility test (antibiotic) component. |
| ANTIBIO_COST_C | INTEGER |  |
| GRAPH_MIN | NUMERIC (18,2) | This item defines the minimum value that you expect this lab component to have. It is used by SlicerDicer to determine what the lower bound of the slider should be set to. This value is typically set using the SlicerDicer Lab Range Calculator. |
| GRAPH_MAX | NUMERIC (18,2) | This item defines the maximum value that you expect this lab component to have. It is used by SlicerDicer to determine what the upper bound of the slider should be set to. This value is typically set using the SlicerDicer Lab Range Calculator. |
| RECORD_TYPE_C | INTEGER |  |
| GROUP_TYPE_C | INTEGER |  |
| EXCHG_COMPONENT_YN | VARCHAR (1) |  |
| UNIT_CONCEPT_ID | NUMERIC (18,0) |  |
| STDRD_UNIT_TRG | VARCHAR (254) | Convert incoming Care Everywhere lab results to this unit |
| STDRD_RSLT_RNG_MIN | NUMERIC (18,2) | Post-standardization minimum reasonable value for this LRR |
| STDRD_RSLT_RNG_MAX | NUMERIC (18,2) | Post-standardization maximum reasonable value for this LRR |
| CANONICAL_CONCEPT_INTERNAL_ID | NUMERIC (18,0) | The unique ID of the canonical concept for the component. |
| COMP_RBC_ANTIGEN_C | INTEGER |  |
| COMP_PLATELET_ANTIGEN_C | INTEGER | Surrogate key used to uniquely identify rows in this (and only this) table on Cogito Cloud only, do not assume the surrogate key in this table will correspond to the surrogate key in another table |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 6 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 6 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 6 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 7 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 7 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 7 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 8 | COMPONENT_TYPE_C | ZC_COMPONENT_TYPE | COMPONENT_TYPE_C | No | No | No |  |
| 10 | LAB_DATA_TYPE_C | ZC_LAB_DATA_TYPE | LAB_DATA_TYPE_C | No | No | No |  |
| 13 | LAB_CAT_DISPLY_C | ZC_LAB_CAT_DISPLY | LAB_CAT_DISPLY_C | No | No | No |  |
| 20 | LAB_ANTIBIOTIC_C | ZC_ANTIBIOTIC | ANTIBIOTIC_C | No | No | No |  |
| 20 | LAB_ANTIBIOTIC_C | ZC_LAB_ANTIBIOTIC | LAB_ANTIBIOTIC_C | No | No | No |  |
| 23 | RESULT_CHECKING_ID | LAB_TRE_NOADD | RECORD_ID | Unknown | No | No |  |
| 25 | COMPONENT_SUBTYPE_C | ZC_COMPONENT_SUBTY | COMPONENT_SUBTYPE_C | No | No | No |  |
| 26 | RECORD_STATE_C | ZC_DEL_STATUS | DEL_STATUS_C | No | No | No |  |
| 26 | RECORD_STATE_C | ZC_EDG_REC_STAT | EDG_REC_STAT_C | No | No | No |  |
| 26 | RECORD_STATE_C | ZC_ERS_REC_STAT | RECORD_STATUS_C | No | No | No |  |
| 26 | RECORD_STATE_C | ZC_HCD_REC_STATE | HCD_REC_STATE_C | No | No | No |  |
| 26 | RECORD_STATE_C | ZC_HFL_RECORD_STAT | HFL_RECORD_STAT_C | No | No | No |  |
| 26 | RECORD_STATE_C | ZC_IMM_REC_STATUS | IMM_REC_STATUS_C | No | No | No |  |
| 26 | RECORD_STATE_C | ZC_LLB_STATUS | LLB_STATUS_C | No | No | No |  |
| 26 | RECORD_STATE_C | ZC_LMA_RECORD_STAT | LMA_RECORD_STAT_C | No | No | No |  |
| 26 | RECORD_STATE_C | ZC_MEM_REC_STATUS | MEM_REC_STATUS_C | No | No | No |  |
| 26 | RECORD_STATE_C | ZC_OR_REC_STATUS | OR_REC_STATUS_C | No | No | No |  |
| 26 | RECORD_STATE_C | ZC_PBA_REC_STAT | PBA_REC_STAT_C | No | No | No |  |
| 26 | RECORD_STATE_C | ZC_PROV_REC_STATE | PROV_REC_STATE_C | No | No | No |  |
| 26 | RECORD_STATE_C | ZC_RECORD_STATE_2 | RECORD_STATE_2_C | No | No | No |  |
| 26 | RECORD_STATE_C | ZC_RECORD_STATE_3 | RECORD_STATE_3_C | No | No | No |  |
| 26 | RECORD_STATE_C | ZC_RECORD_STATE_4 | RECORD_STATE_4_C | No | No | No |  |
| 26 | RECORD_STATE_C | ZC_RECORD_STATE_6 | RECORD_STATE_6_C | No | No | No |  |
| 26 | RECORD_STATE_C | ZC_RECORD_STATE_7 | RECORD_STATE_7_C | No | No | No |  |

_(54 total; showing first 30)_
