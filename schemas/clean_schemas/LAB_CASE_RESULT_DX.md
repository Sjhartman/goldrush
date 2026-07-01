# LAB_CASE_RESULT_DX

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=LAB_CASE_RESULT_DX

## Description

This table contains result diagnosis information for anatomic pathology cases.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | REQ |
| Release Version | Rel 2010 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| CASE_ID | NUMERIC (18,0) | The unique identifier for the case record. |
| LINE | INTEGER | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| RESULT_DX_ID | NUMERIC (18,0) | This item stores the result diagnoses of the case. |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | CASE_ID | EXT_ID_BUNDLE_MAP_DB_MAIN | MAPPING_ID | No | No | No |  |
| 1 | CASE_ID | ID_BUNDLE_DEMOG_DB_MAIN | DEMOG_ID | No | No | No |  |
| 1 | CASE_ID | LAB_CASE_DB_MAIN | CASE_ID | Unknown | No | No |  |
| 1 | CASE_ID | REQ_ALL_MAIN | REQUISITION_ID | No | No | No |  |
| 1 | CASE_ID | REQ_DB_MAIN | REQUISITION_ID | Unknown | No | No |  |
| 3 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 4 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 4 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 4 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 5 | RESULT_DX_ID | ADVERSE_EVENT_TERM_INFO | DX_ID | No | No | No |  |
| 5 | RESULT_DX_ID | CLARITY_EDG | DX_ID | Unknown | No | No |  |
| 5 | RESULT_DX_ID | EDG_DBC_INFO | DX_ID | No | No | No |  |
| 5 | RESULT_DX_ID | V_CUBE_D_DIAGNOSIS | DIAGNOSIS_ID | Unknown | Unknown | No |  |
