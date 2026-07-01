# EXTERNAL_CNCPT_MAP

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=EXTERNAL_CNCPT_MAP

## Description

The EXTERNAL_CNCPT_MAP table stores information about mappings as well as the entities (record/category/item) they reference. The SNOMED concepts or SmartData elements referenced by mappings are stored in the CONCEPT_MAPPED table.

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
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| RECORD_STATUS_C | INTEGER |  |
| CUSTOM_MAPPING_YN | VARCHAR (1) |  |
| ENTITY_INI | VARCHAR (254) | The three letter abbreviation of the entity master file linked to the concepts defined for the current mapping. |
| ENTITY_ITEM | NUMERIC (18,1) | The item number of the entity item linked to the concepts defined for the current mapping. |
| ENTITY_VALUE_NUM | NUMERIC (18,1) | The entity value linked to the concepts defined for the current mapping. This value is often a record ID. ENTITY_VALUE_NUM is only populated if the linked value is a number. |
| ENTITY_VALUE_STR | VARCHAR (254) | The entity value linked to the concepts defined for the current mapping.  This value is often a record ID. ENTITY_VALUE_STR is only populated if the linked value is a string. |
| ENTITY_SEC_VALUE | VARCHAR (253) | Stores concept mappings for item values for specific records. |
| MAPPED_VALUE_NAME | VARCHAR (254) | Holds the name of the Epic entity being mapped via EXM. This item can correspond to the name of a masterfile, record, item, category value, or secondary value (such as a flowsheet value). |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 2 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 2 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 3 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 4 | RECORD_STATUS_C | ZC_RECORD_STATUS | RECORD_STATUS_C | No | No | No |  |
