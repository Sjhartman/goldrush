# CAREPLAN_TEMPLATE

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=CAREPLAN_TEMPLATE

## Description

Contains information about Healthy Planet Care Plan templates.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | LCP |
| Release Version | Rel May 2019 |
| May contain EHI? | No |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| CAREPLAN_ID | VARCHAR (18) | This column stores the unique identifier for a care plan record. |
| LINE | INTEGER | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| CAREPLAN_TEMPLATE_ID | NUMERIC (18,0) | Stores the care plan template (LCE) ID that was used to generate the patient's care plan (LCP). |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | CAREPLAN_ID | CAREPLAN_ENROLLMENT_INFO | CAREPLAN_ID | No | No | No |  |
| 1 | CAREPLAN_ID | CAREPLAN_INFO | CARE_INTG_ID | No | No | No |  |
| 1 | CAREPLAN_ID | CAREPLAN_PT_TASK_INFO | CAREPLAN_ID | No | No | No |  |
| 1 | CAREPLAN_ID | V_EHI_LCP_EPISODE_FILTER | CAREPLAN_ID | Unknown | Unknown | No |  |
| 3 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 4 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 4 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 4 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 5 | CAREPLAN_TEMPLATE_ID | CAREPLAN_TEMP_INFO | TEMPLATE_ID | No | No | No |  |
