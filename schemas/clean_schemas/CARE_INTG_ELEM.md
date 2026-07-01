# CARE_INTG_ELEM

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=CARE_INTG_ELEM

## Description

This table contains the problems associated with a Care Integrator record.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | LCP |
| Release Version | EPIC 2002 |
| May contain EHI? | No |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| CARE_INTG_ID | VARCHAR (18) | The unique ID for the care integrator record. |
| LINE | No | The line count for the item. |
| PROBLEM_ID | VARCHAR (18) | The unique ID for problems (LPB) associated with this care integrator record. |
| CM_PHY_OWNER_ID | VARCHAR (25) | ID of the physical deployment owner for this record.  Physical owners will be where the data is hosted, either on the cross-over server or the owner deployment. |
| CM_LOG_OWNER_ID | VARCHAR (25) | ID of the logical deployment owner for this record.  Logical owners show the deployment where the record was created but doesn't represent if the record is a part of version skew. |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | CARE_INTG_ID | CAREPLAN_ENROLLMENT_INFO | CAREPLAN_ID | No | No | No |  |
| 1 | CARE_INTG_ID | CAREPLAN_INFO | CARE_INTG_ID | No | No | No |  |
| 1 | CARE_INTG_ID | CAREPLAN_PT_TASK_INFO | CAREPLAN_ID | No | No | No |  |
| 1 | CARE_INTG_ID | V_EHI_LCP_EPISODE_FILTER | CAREPLAN_ID | Unknown | Unknown | No |  |
| 3 | PROBLEM_ID | HH_PROB_INFO | PROBLEM_ID | Unknown | No | No |  |
| 3 | PROBLEM_ID | PROBLEM | PROBLEM_ID | Unknown | No | No |  |
| 4 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 4 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 4 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 5 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 5 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 5 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
