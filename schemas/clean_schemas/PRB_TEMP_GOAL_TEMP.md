# PRB_TEMP_GOAL_TEMP

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=PRB_TEMP_GOAL_TEMP

## Description

This table stores the goal templates associated with the problem template.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | FULL |
| Load Frequency | WEEKLY - FULL |
| Chronicles INI | LTP |
| Release Version | SPRING 2007 |
| May contain EHI? | No |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| TEMPLATE_PROBLEM_ID | NUMERIC (18,0) | This is the problem template ID. |
| CONTACT_DATE_REAL | No | This is a numeric representation of the date of this encounter in your system. The integer portion of the number specifies the date of the encounter. The digits after the decimal point indicate multiple visits on one day. |
| LINE | No | This is the line number for a multiple response item. |
| CONTACT_DATE | DATETIME | This is the chronicles contact date. |
| CM_PHY_OWNER_ID | VARCHAR (25) | ID of the physical deployment owner for this record. Physical owners will be where the data is hosted, either on the cross-over server or the owner deployment. |
| CM_LOG_OWNER_ID | VARCHAR (25) | ID of the logical deployment owner for this record. Logical owners show the deployment where the record was created but doesn't represent if the record is a part of version skew. |
| CM_CT_OWNER_ID | VARCHAR (25) | This is the deployment that owns the this contact. |
| GOAL_TEMPLATE_ID | NUMERIC (18,0) | This column stores the goal templates associated with the problem template. |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | TEMPLATE_PROBLEM_ID | PRB_TEMP_INFO | TEMPLATE_PROBLEM_ID | Unknown | No | No |  |
| 1 | TEMPLATE_PROBLEM_ID | PRB_TEMP_EDIT_INFO | TEMPLATE_PROBLEM_ID | Unknown | No | No |  |
| 2 | CONTACT_DATE_REAL | CONTACT_DATE_REAL |  |  |  |  |  |
| 5 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 5 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 5 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 6 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 6 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 6 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 7 | CM_CT_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 7 | CM_CT_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 7 | CM_CT_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 8 | GOAL_TEMPLATE_ID | GOAL_TEMPLATES | GOAL_TEMPLATE_ID | No | No | No |  |
