# OR_CASE_ADDL_CODES

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=OR_CASE_ADDL_CODES

## Description

This table stores the additional codes for the case.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | ORC |
| Release Version | Rel 2015 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| CASE_ID | VARCHAR (18) | The unique identifier for the case request record. |
| LINE | INTEGER | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| OR_CASE_ADDL_CODE_ID | NUMERIC (18,0) | This item stores the additional codes for the case. |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | CASE_ID | OR_CASE | OR_CASE_ID | Unknown | No | No |  |
| 1 | CASE_ID | OR_CASE_2 | CASE_ID | Unknown | No | No |  |
| 1 | CASE_ID | OR_CASE_3 | CASE_ID | Unknown | No | No |  |
| 1 | CASE_ID | OR_CASE_4 | OR_CASE_ID | No | No | No |  |
| 1 | CASE_ID | OR_CASE_VIRTUAL | OR_CASE_ID | No | No | No |  |
| 1 | CASE_ID | V_OR_CASE_ORR | CASE_ID | Unknown | Unknown | No |  |
| 3 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 4 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 4 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 4 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 5 | OR_CASE_ADDL_CODE_ID | CLARITY_EAP | PROC_ID | No | No | No |  |
| 5 | OR_CASE_ADDL_CODE_ID | CLARITY_EAP_2 | PROC_ID | No | No | No |  |
| 5 | OR_CASE_ADDL_CODE_ID | CLARITY_EAP_3 | PROC_ID | No | No | No |  |
| 5 | OR_CASE_ADDL_CODE_ID | CLARITY_EAP_4 | PROC_ID | No | No | No |  |
| 5 | OR_CASE_ADDL_CODE_ID | CLARITY_EAP_5 | PROC_ID | No | No | No |  |
| 5 | OR_CASE_ADDL_CODE_ID | CLARITY_EAP_IMM | PROC_ID | Unknown | No | No |  |
| 5 | OR_CASE_ADDL_CODE_ID | PROC_CONSENT_CONFIG | PROC_ID | No | No | No |  |
| 5 | OR_CASE_ADDL_CODE_ID | PROC_UM | PROC_ID | No | No | No |  |
| 5 | OR_CASE_ADDL_CODE_ID | V_CUBE_D_PROCEDURE | PROCEDURE_ID | Unknown | Unknown | No |  |
