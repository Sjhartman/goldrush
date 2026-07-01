# CONCEPT_MAPPED

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=CONCEPT_MAPPED

## Description

The CONCEPT_MAPPED table stores the Concept Identifier of the SNOMED concept or SmartData Identifier (SDI) of the SmartData element referenced by mappings as well as the type of mapping associated with each concept-to-entity link. The mapped entities are given in the EXTERNAL_CNCPT_MAP table.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | EXM |
| Release Version | Summer 2009 |
| May contain EHI? | No |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| MAPPING_ID | NUMERIC (18,0) | The unique identifier (.1 item) for the mapping record. |
| LINE | No | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| MAPPING_TYPE_C | INTEGER |  |
| CONCEPT_ID | VARCHAR (192) | The Concept Identifier of the SNOMED concept or SmartData Identifier (SDI) of the SmartData element referenced by the current row's mapping. |
| MAPPING_DEFINITION | VARCHAR (254) | Stores the meaning of the map between the Chronicles entity and the concept in in EDG-410. Is automatically populated by the diagnosis import. |
| PREF_LEX_MAP_YN | VARCHAR (1) | Surrogate key used to uniquely identify rows in this (and only this) table on Cogito Cloud only, do not assume the surrogate key in this table will correspond to the surrogate key in another table |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | MAPPING_ID | EXTERNAL_CNCPT_MAP | MAPPING_ID | No | No | No |  |
| 3 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 4 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 4 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 4 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 5 | MAPPING_TYPE_C | ZC_MAPPING_TYPE | MAPPING_TYPE_C | No | No | No |  |
