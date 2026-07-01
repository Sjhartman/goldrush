# AP_CASE_TYPES

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=AP_CASE_TYPES

## Description

Use this table to report on anatomic pathology settings configured at the case type level. Refer to table LAB_AP_LAB_SETUP if you're looking for the equivalent items set at the lab level.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | LDF |
| Release Version | Summer 2009 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| LAB_ID | VARCHAR (18) | The unique ID of the case type defaults associated with a case type definition. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| ID_PIECE_FORMAT_C | INTEGER |  |
| DELIM_PREC_SLD | VARCHAR (10) | Delimiter to separate blocks from slides. |
| DELIM_PREC_SPEC | VARCHAR (10) | Delimiter to separate cases from specimens. |
| AP_WORKLIST_TYPE_C | INTEGER |  |
| CASE_TYPE_NAME | VARCHAR (254) | The name of the case type. |
| AP_USE_HISTOLOGY_YN | VARCHAR (1) |  |
| CASE_EXPECTED_LEN | INTEGER | The expected length that a case of this type will be performed in. |
| CASE_EXPECTED_LEN_C | INTEGER |  |
| TYPE_CASE_C | INTEGER |  |
| AP_REL_RPT_SET_ID | NUMERIC (18,0) | Report setting used when looking up related orders for anatomic pathology. |
| AP_USE_IN_BASKET_YN | VARCHAR (1) |  |
| REPORT_NAME | VARCHAR (254) | The report name to use in the header of the result report generated for anatomic pathology cases of a certain case type. |
| AP_QA_RPT_SET_ID | NUMERIC (18,0) | Report setting used when looking up possible quality assurance correlation orders for anatomic pathology. |
| MED_CYTO_WORKFLOW_C | INTEGER |  |
| AP_CHRG_REVIEW_YN *(deprecated)* | VARCHAR (1) |  |
| SKIP_ON_SOURCE_YN | VARCHAR (1) |  |
| ALLOW_MANUAL_NUM_C | INTEGER |  |
| AP_CHRG_REVIEW_C | INTEGER |  |
| BELONGS_TO_LAB_ID | VARCHAR (18) | The unique ID of the lab record this case type belongs to. This column is frequently used to link to the LAB_PROFILE table. |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | LAB_ID | LAB_AP_LAB_SETUP | LAB_ID | Unknown | No | No |  |
| 1 | LAB_ID | LAB_INFO | LAB_ID | Unknown | No | No |  |
| 1 | LAB_ID | LAB_PROFILE | LAB_ID | Unknown | No | No |  |
| 1 | LAB_ID | LAB_SECTION | SECTION_ID | Unknown | No | No |  |
| 1 | LAB_ID | LDF_REQ_SETUP | LAB_ID | Unknown | No | No |  |
| 1 | LAB_ID | WORKBENCH_PROFILE | WORKBENCH_ID | Unknown | No | No |  |
| 2 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 2 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 2 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 3 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 4 | ID_PIECE_FORMAT_C | ZC_ID_PIECE_FORMAT | ID_PIECE_FORMAT_C | No | No | No |  |
| 7 | AP_WORKLIST_TYPE_C | ZC_AP_WORKLIST_TYP | AP_WORKLIST_TYP_C | No | No | No |  |
| 11 | CASE_EXPECTED_LEN_C | ZC_DFLT_UNIT | DFLT_UNIT_C | No | No | No |  |
| 12 | TYPE_CASE_C | ZC_TYPE_CASE | TYPE_CASE_C | No | No | No |  |
| 13 | AP_REL_RPT_SET_ID | REPORT_INFO | REPORT_INFO_ID | No | No | No |  |
| 13 | AP_REL_RPT_SET_ID | V_REPORT_SETTINGS_FACT | REPORT_INFO_ID | Unknown | Unknown | No |  |
| 16 | AP_QA_RPT_SET_ID | REPORT_INFO | REPORT_INFO_ID | No | No | No |  |
| 16 | AP_QA_RPT_SET_ID | V_REPORT_SETTINGS_FACT | REPORT_INFO_ID | Unknown | Unknown | No |  |
| 17 | MED_CYTO_WORKFLOW_C | ZC_MED_CYTO_WORKFL | MED_CYTO_WORKFL_C | No | No | No |  |
| 20 | ALLOW_MANUAL_NUM_C | ZC_ALLOW_CASE_NUM | ALLOW_CASE_NUM_C | No | No | No |  |
| 21 | AP_CHRG_REVIEW_C | ZC_AP_CHRG_REVIEW | AP_CHRG_REVIEW_C | No | No | No |  |
| 22 | BELONGS_TO_LAB_ID | AP_CASE_TYPES | LAB_ID | Unknown | No | No |  |
| 22 | BELONGS_TO_LAB_ID | LAB_AP_LAB_SETUP | LAB_ID | Unknown | No | No |  |
| 22 | BELONGS_TO_LAB_ID | LAB_INFO | LAB_ID | Unknown | No | No |  |
| 22 | BELONGS_TO_LAB_ID | LAB_PROFILE | LAB_ID | Unknown | No | No |  |
| 22 | BELONGS_TO_LAB_ID | LAB_SECTION | SECTION_ID | Unknown | No | No |  |
| 22 | BELONGS_TO_LAB_ID | LDF_REQ_SETUP | LAB_ID | Unknown | No | No |  |
| 22 | BELONGS_TO_LAB_ID | WORKBENCH_PROFILE | WORKBENCH_ID | Unknown | No | No |  |
