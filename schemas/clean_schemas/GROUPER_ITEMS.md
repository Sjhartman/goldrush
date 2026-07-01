# GROUPER_ITEMS

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=GROUPER_ITEMS

## Description

The GROUPER_ITEMS table contains high-level information about your grouper records: description, context, grouper type and concept logic.

**Primary table** in this group (25 cols). Overflow siblings joined on shared key: GROUPER_ITEMS_2 (8 cols). Prefer this table for most queries.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | VCG |
| Release Version | SPRING 2005 |
| May contain EHI? | No |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| GROUPER_ID | VARCHAR (18) | Holds the grouper ID. |
| GROUPER_NAME | VARCHAR (254) | Holds the grouper name |
| DESCRIPTION | VARCHAR (3500) | Holds the description information. This column will automatically be truncated at 4000 characters. |
| CONTEXT_INI | VARCHAR (254) | Holds the context INI of the grouper record. |
| CONCEPT_LOGIC | VARCHAR (3000) | Holds the concept logic of the record. |
| CM_LOG_ONWER_ID | No | CM_LOG_OWNER_ID should be used instead of this column |
| CM_PHY_OWNER_ID | VARCHAR (25) | ID of the physical deployment owner for this record.  Physical owners will be where the data is hosted, either on the cross-over server or the owner deployment. |
| GROUPER_TYPE_C | INTEGER |  |
| CM_LOG_OWNER_ID | VARCHAR (25) | ID of the logical deployment owner for this record.  Logical owners show the deployment where the record was created but doesn't represent if the record is a part of version skew. |
| RLTD_TMPLT_RELS_YN | VARCHAR (1) |  |
| RECORD_STATUS_C | INTEGER |  |
| RESTR_TO_SNOMED_YN | VARCHAR (1) |  |
| EXCL_SPEC_TERM_YN *(deprecated)* | VARCHAR (1) |  |
| INC_MED_ROUTE_YN | VARCHAR (1) |  |
| CUI_LOGIC_TYPE_C | INTEGER |  |
| SLICERDICER_EXCL_YN | VARCHAR (1) |  |
| PROV_DISPLAY_NAME | VARCHAR (192) | A provider-friendly name for the grouper. |
| BASE_GROUPER_ID | VARCHAR (18) | The unique identifier (VCG-.1) of the base record to which the compiled record is linked. |
| COMPILED_CONTEXT | VARCHAR (3) | The context (master file) of the records contained in the compiled grouper. |
| EXTERNAL_ID_TYPE_C | INTEGER |  |
| EXTERNAL_GROUPER_ID | VARCHAR (180) | Stores the external ID of the grouper record. |
| COMPILE_ALL_CONTEXTS_YN | VARCHAR (1) |  |
| RECORD_TYPE_C | INTEGER |  |
| LAST_COMPILED_UTC_DTTM | DATETIME (UTC) | Stores the instant that the grouper last finished compiling. |
| FAM_HX_MAPPING_C | INTEGER |  |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| BITMAP INDEX | EIX_VCG_ITEMS_CONTEXT | CONTEXT_INI | 1 | Yes | Yes |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | GROUPER_ID | GROUPER_ITEMS_2 | GROUPER_ID | No | No | No |  |
| 7 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 7 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 7 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 8 | GROUPER_TYPE_C | ZC_GROUPER_TYPE | GROUPER_TYPE_C | No | No | No |  |
| 9 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 9 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 9 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 11 | RECORD_STATUS_C | ZC_RECORD_STATUS_2 | RECORD_STATUS_2_C | No | No | No |  |
| 11 | RECORD_STATUS_C | ZC_RECORD_STS | RECORD_STS_C | No | No | No |  |
| 15 | CUI_LOGIC_TYPE_C | ZC_CUI_LOGIC_TYPE | CUI_LOGIC_TYPE_C | No | No | No |  |
| 18 | BASE_GROUPER_ID | GROUPER_ITEMS | GROUPER_ID | No | No | No |  |
| 18 | BASE_GROUPER_ID | GROUPER_ITEMS_2 | GROUPER_ID | No | No | No |  |
| 20 | EXTERNAL_ID_TYPE_C | ZC_EXTERNAL_ID_TYPE | EXTERNAL_ID_TYPE_C | No | No | No |  |
| 23 | RECORD_TYPE_C | ZC_GROUPER_RECORD_TYPE | RECORD_TYPE_C | No | No | No |  |
| 25 | FAM_HX_MAPPING_C | ZC_MEDICAL_HX | MEDICAL_HX_C | No | No | No |  |
