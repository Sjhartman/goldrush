# PROB_GOALS

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=PROB_GOALS

## Description

This table contains data on the discrete goal (IGO) records associated with each problem.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | LPB |
| Release Version | EPIC 2002 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| PROBLEM_ID | VARCHAR (18) | The unique ID for the care integrator problem. |
| LINE | No | The line count for the item. |
| GOAL_ID | VARCHAR (18) | The unique ID for the goal associated with this problem. |
| CM_PHY_OWNER_ID | VARCHAR (25) | ID of the physical deployment owner for this record.  Physical owners will be where the data is hosted, either on the cross-over server or the owner deployment. |
| CM_LOG_OWNER_ID | VARCHAR (25) | ID of the logical deployment owner for this record.  Logical owners show the deployment where the record was created but doesn't represent if the record is a part of version skew. |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | PROBLEM_ID | HH_PROB_INFO | PROBLEM_ID | Unknown | No | No |  |
| 1 | PROBLEM_ID | PROBLEM | PROBLEM_ID | Unknown | No | No |  |
| 3 | GOAL_ID | GOAL | GOAL_ID | Unknown | No | No |  |
| 3 | GOAL_ID | PT_GOALS_INFO | GOAL_ID | Unknown | No | No |  |
| 4 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 4 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 4 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 5 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 5 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 5 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
