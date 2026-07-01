# OR_PROC_CPT_ID

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=OR_PROC_CPT_ID

## Description

The OR_PROC_CPT_ID table contains OR management system procedure CPT codes.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | FULL |
| Load Frequency | WEEKLY - FULL |
| Chronicles INI | ORP |
| Release Version | MU1 - MAY 2001 |
| May contain EHI? | No |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| OR_PROC_ID | VARCHAR (254) | The unique internal ID of the surgical procedure. |
| LINE | No | The total number of lines of CPT? code information associated with this procedure. |
| CPT_ID | NUMERIC (18,0) | The unique internal ID of the CPT? code record. |
| REAL_CPT_CODE | VARCHAR (184) | The real CPT? code for the procedure. |
| CM_PHY_OWNER_ID | VARCHAR (25) | ID of the physical deployment owner for this record.  Physical owners will be where the data is hosted, either on the cross-over server or the owner deployment. |
| CM_LOG_OWNER_ID | VARCHAR (25) | ID of the logical deployment owner for this record.  Logical owners show the deployment where the record was created but doesn't represent if the record is a part of version skew. |
| IS_DEFAULT_CODE_YN | VARCHAR (1) |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | OR_PROC_ID | OR_PROC | OR_PROC_ID | Unknown | No | No |  |
| 1 | OR_PROC_ID | OR_PROC_2 | OR_PROC_ID | No | No | No |  |
| 1 | OR_PROC_ID | OR_PROC_CONSENT_CONFIG | PROC_ID | No | No | No |  |
| 3 | CPT_ID | CLARITY_EAP | PROC_ID | No | No | No |  |
| 3 | CPT_ID | CLARITY_EAP_2 | PROC_ID | No | No | No |  |
| 3 | CPT_ID | CLARITY_EAP_3 | PROC_ID | No | No | No |  |
| 3 | CPT_ID | CLARITY_EAP_4 | PROC_ID | No | No | No |  |
| 3 | CPT_ID | CLARITY_EAP_5 | PROC_ID | No | No | No |  |
| 3 | CPT_ID | CLARITY_EAP_IMM | PROC_ID | Unknown | No | No |  |
| 3 | CPT_ID | PROC_CONSENT_CONFIG | PROC_ID | No | No | No |  |
| 3 | CPT_ID | PROC_UM | PROC_ID | No | No | No |  |
| 3 | CPT_ID | V_CUBE_D_PROCEDURE | PROCEDURE_ID | Unknown | Unknown | No |  |
| 5 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 5 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 5 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 6 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 6 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 6 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
