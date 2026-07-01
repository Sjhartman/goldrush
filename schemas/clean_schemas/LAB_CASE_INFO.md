# LAB_CASE_INFO

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=LAB_CASE_INFO

## Description

Lab Anatomic Pathology case information.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | REQ |
| Release Version | Summer 2009 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| REQUISITION_ID | NUMERIC (18,0) | The unique identifier for the case record. |
| LINE | No | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this Chronicles record. This is populated only if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this Chronicles record was extracted. This is populated only if you use IntraConnect. |
| CASE_TYPE_ID | VARCHAR (18) | The case type for the given case number. |
| CASE_NUM | VARCHAR (254) | Case number with type and compiled number generation |
| AP_CASE_STATUS_C | INTEGER |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | REQUISITION_ID | EXT_ID_BUNDLE_MAP_DB_MAIN | MAPPING_ID | No | No | No |  |
| 1 | REQUISITION_ID | ID_BUNDLE_DEMOG_DB_MAIN | DEMOG_ID | No | No | No |  |
| 1 | REQUISITION_ID | LAB_CASE_DB_MAIN | CASE_ID | Unknown | No | No |  |
| 1 | REQUISITION_ID | REQ_ALL_MAIN | REQUISITION_ID | No | No | No |  |
| 1 | REQUISITION_ID | REQ_DB_MAIN | REQUISITION_ID | Unknown | No | No |  |
| 3 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 4 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 4 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 4 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 5 | CASE_TYPE_ID | AP_CASE_TYPES | LAB_ID | Unknown | No | No |  |
| 5 | CASE_TYPE_ID | LAB_AP_LAB_SETUP | LAB_ID | Unknown | No | No |  |
| 5 | CASE_TYPE_ID | LAB_INFO | LAB_ID | Unknown | No | No |  |
| 5 | CASE_TYPE_ID | LAB_PROFILE | LAB_ID | Unknown | No | No |  |
| 5 | CASE_TYPE_ID | LAB_SECTION | SECTION_ID | Unknown | No | No |  |
| 5 | CASE_TYPE_ID | LDF_REQ_SETUP | LAB_ID | Unknown | No | No |  |
| 5 | CASE_TYPE_ID | WORKBENCH_PROFILE | WORKBENCH_ID | Unknown | No | No |  |
| 7 | AP_CASE_STATUS_C | ZC_AP_CASE_STATUS | AP_CASE_STATUS_C | No | No | No |  |
