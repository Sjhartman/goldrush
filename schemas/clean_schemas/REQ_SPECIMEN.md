# REQ_SPECIMEN

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=REQ_SPECIMEN

## Description

This table contains the specimen IDs for specimens that are related to each requisition.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | REQ |
| Release Version | SPRING 2007 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| REQUISITION_ID | NUMERIC (18,0) | The unique identifier for the requisition record. |
| LINE | No | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| REQ_SPECIMEN_ID | VARCHAR (18) | Stores a list of specimens on this requisition. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this Chronicles record was extracted. This is populated only if you use IntraConnect. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this Chronicles record. This is populated only if you use IntraConnect. |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| B-TREE INDEX | EIX_REQ_SPECIMEN_ID | REQ_SPECIMEN_ID | 1 | Yes | Yes |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | REQUISITION_ID | EXT_ID_BUNDLE_MAP_DB_MAIN | MAPPING_ID | No | No | No |  |
| 1 | REQUISITION_ID | ID_BUNDLE_DEMOG_DB_MAIN | DEMOG_ID | No | No | No |  |
| 1 | REQUISITION_ID | LAB_CASE_DB_MAIN | CASE_ID | Unknown | No | No |  |
| 1 | REQUISITION_ID | REQ_ALL_MAIN | REQUISITION_ID | No | No | No |  |
| 1 | REQUISITION_ID | REQ_DB_MAIN | REQUISITION_ID | Unknown | No | No |  |
| 3 | REQ_SPECIMEN_ID | AP_SPECIMEN_DESC | SPECIMEN_ID | No | No | No |  |
| 3 | REQ_SPECIMEN_ID | EMBRYOLOGY_SPECIMEN | SPECIMEN_ID | No | No | No |  |
| 3 | REQ_SPECIMEN_ID | SPEC_DB_MAIN | SPECIMEN_ID | No | No | No |  |
| 4 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 4 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 4 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 5 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 5 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 5 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
