# OR_CASE_APPTS_PR

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=OR_CASE_APPTS_PR

## Description

The OR_CASE_APPTS_PR table contains OR management system case appointments.  This table contains pre-operation information.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | ORC |
| Release Version | MU6 - EPIC 2002 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| OR_CASE_ID | VARCHAR (18) | The unique ID of the case record. |
| APPT_TYPE | No | The type of appointment that needs to be scheduled for the patient before or after the surgery. This will be 1 for pre-op or 2 for post-op. |
| LINE | INTEGER | The number of the line of the pre-op and post-op appointment that need to be scheduled. |
| UNIQUE_ID | VARCHAR (184) | The unique ID of the appointment that has been scheduled. |
| APPT_PRC_ID | VARCHAR (18) | The unique ID of the visit type of the pre-op or post-op appointment that needs to be scheduled for the patient. |
| OR_PROC_ID | VARCHAR (254) | The unique ID of the related surgical procedure for which the appointment needs to be scheduled. |
| PROV_ID | VARCHAR (18) | The unique ID of the provider with whom the appointment should be scheduled. |
| DEPT_ID | NUMERIC (18,0) | The unique ID of the department in which the appointment is scheduled. |
| ASN | NUMERIC (18,0) | The unique appointment serial number associated with the appointment that is scheduled. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The deployment identifier of which the data is physically kept. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The deployment identifier of which the data is logically kept. |
| PXPASS_TASK_ID | NUMERIC (18,0) | This item stores the Procedure Pass (PxP) record this appointment was automatically linked from (if any). |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| B-TREE INDEX | EIX_OR_CASE_APPTS_PR_DEID | DEPT_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_OR_CASE_APPTS_PR_ORPRID | OR_PROC_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_OR_CASE_APPTS_PR_UNID | UNIQUE_ID | 1 | Yes | Yes |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | OR_CASE_ID | OR_CASE | OR_CASE_ID | Unknown | No | No |  |
| 1 | OR_CASE_ID | OR_CASE_2 | CASE_ID | Unknown | No | No |  |
| 1 | OR_CASE_ID | OR_CASE_3 | CASE_ID | Unknown | No | No |  |
| 1 | OR_CASE_ID | OR_CASE_4 | OR_CASE_ID | No | No | No |  |
| 1 | OR_CASE_ID | OR_CASE_VIRTUAL | OR_CASE_ID | No | No | No |  |
| 1 | OR_CASE_ID | V_OR_CASE_ORR | CASE_ID | Unknown | Unknown | No |  |
| 5 | APPT_PRC_ID | CLARITY_PRC | PRC_ID | No | No | No |  |
| 5 | APPT_PRC_ID | CLARITY_PRC_2 | PRC_ID | No | No | No |  |
| 5 | APPT_PRC_ID | CLARITY_PRC_MYC | VISIT_TYPE_ID | No | No | No |  |
| 6 | OR_PROC_ID | OR_PROC_2 | OR_PROC_ID | No | No | No |  |
| 6 | OR_PROC_ID | OR_PROC_CONSENT_CONFIG | PROC_ID | No | No | No |  |
| 7 | PROV_ID | CLARITY_SER | PROV_ID | Unknown | No | No |  |
| 7 | PROV_ID | CLARITY_SER_2 | PROV_ID | Unknown | No | No |  |
| 7 | PROV_ID | CLARITY_SER_3 | PROV_ID | Unknown | No | No |  |
| 7 | PROV_ID | CLARITY_SER_4 | PROV_ID | No | No | No |  |
| 7 | PROV_ID | CLARITY_SER_MYC | PROV_ID | Unknown | No | No |  |
| 7 | PROV_ID | D_PROV_PRIMARY_HIERARCHY | PROV_ID | Unknown | Unknown | No |  |
| 7 | PROV_ID | ED_SER_SETTINGS | PROV_ID | Unknown | No | No |  |
| 7 | PROV_ID | EXT_CAL_PROV_CONFIG | PROV_ID | No | No | No |  |
| 7 | PROV_ID | OR_SER_EQUIPMENT | PROV_ID | Unknown | No | No |  |
| 7 | PROV_ID | OR_SER_ROOM | PROV_ID | Unknown | No | No |  |
| 7 | PROV_ID | PROV_BATCH_LTR_GEN | PROV_ID | Unknown | No | No |  |
| 7 | PROV_ID | PROV_GROUP | PROV_ID | No | No | No |  |
| 7 | PROV_ID | V_CUBE_D_PROVIDER | PROVIDER_ID | Unknown | Unknown | No |  |
| 8 | DEPT_ID | BH_DEP | DEPARTMENT_ID | No | No | No |  |
| 8 | DEPT_ID | CLARITY_DEP | DEPARTMENT_ID | No | No | No |  |
| 8 | DEPT_ID | CLARITY_DEP_2 | DEPARTMENT_ID | No | No | No |  |
| 8 | DEPT_ID | CLARITY_DEP_3 | DEPARTMENT_ID | No | No | No |  |
| 8 | DEPT_ID | CLARITY_DEP_4 | DEPARTMENT_ID | No | No | No |  |
| 8 | DEPT_ID | CLARITY_DEP_5 | DEPARTMENT_ID | No | No | No |  |

_(169 total; showing first 30)_
