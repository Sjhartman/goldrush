# CLARITY_EAP_3

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=CLARITY_EAP_3

## Description

The CLARITY_EAP_3 table contains basic information about the procedure records in your system. This includes both A/R and clinical procedures. This is a continuation of Clarity table CLARITY_EAP.

**Overflow table** for CLARITY_EAP (149 cols). Contains additional columns for the same records — join on the shared primary key column.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | EAP |
| Release Version | Rel 2015 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| PROC_ID | NUMERIC (18,0) | The unique ID number for a procedure record. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| CONTRAST_REQ_C | INTEGER |  |
| PAT_FRIENDLY_DESC | VARCHAR (500) | The patient-friendly description to be used on the outgoing EOBs |
| TOMOSYNTHESIS_PROC_YN | VARCHAR (1) |  |
| PROC_SUBTYPE_C | INTEGER |  |
| CLINICALLY_ACTIVE_YN | VARCHAR (1) |  |
| MYC_GEN_SCH_TKT_C | INTEGER |  |
| DENTAL_MATERIAL_C | INTEGER |  |
| MYC_NO_ACCT_TKT_YN | VARCHAR (1) |  |
| PT_FRIENDLY_NAME | VARCHAR (4000) | The patient friendly procedure name for use in MyChart. |
| RECUR_AUTORLS_LIMIT_OPTION_C | INTEGER |  |
| RECUR_AUTORLS_SCHEDULING_LIMIT | INTEGER | The number of appointments that the patient can schedule if the procedure is set to auto-release an order to the patient for scheduling in MyChart. |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | PROC_ID | CLARITY_EAP | PROC_ID | No | No | No |  |
| 1 | PROC_ID | CLARITY_EAP_2 | PROC_ID | No | No | No |  |
| 1 | PROC_ID | CLARITY_EAP_4 | PROC_ID | No | No | No |  |
| 1 | PROC_ID | CLARITY_EAP_5 | PROC_ID | No | No | No |  |
| 1 | PROC_ID | CLARITY_EAP_IMM | PROC_ID | Unknown | No | No |  |
| 1 | PROC_ID | PROC_CONSENT_CONFIG | PROC_ID | No | No | No |  |
| 1 | PROC_ID | PROC_UM | PROC_ID | No | No | No |  |
| 1 | PROC_ID | V_CUBE_D_PROCEDURE | PROCEDURE_ID | Unknown | Unknown | No |  |
| 2 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 2 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 2 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 3 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 4 | CONTRAST_REQ_C | ZC_CONTRAST_REQ | CONTRAST_REQ_C | No | No | No |  |
| 7 | PROC_SUBTYPE_C | ZC_PROCEDURE_SUBTYPE | PROCEDURE_SUBTYPE_C | No | No | No |  |
| 9 | MYC_GEN_SCH_TKT_C | ZC_MYC_GEN_SCH_TKT | MYC_GEN_SCH_TKT_C | No | No | No |  |
| 10 | DENTAL_MATERIAL_C | ZC_DENTAL_MATERIAL | DENTAL_MATERIAL_C | No | No | No |  |
| 13 | RECUR_AUTORLS_LIMIT_OPTION_C | ZC_PAT_SCHED_LIMIT_OPTION | PAT_SCHED_LIMIT_OPTION_C | No | No | No |  |
