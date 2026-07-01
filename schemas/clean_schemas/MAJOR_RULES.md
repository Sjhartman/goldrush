# MAJOR_RULES

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=MAJOR_RULES

## Description

This table contains the list of rule records that contribute to the acuity scoring systems.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | HDA |
| Release Version | Summer 2009 |
| May contain EHI? | No |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| ACUITY_SYSTEM_ID | NUMERIC (18,0) | The unique identifier (.1 item) for the acuity system record. |
| LINE | No | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| MAJOR_RULES_ID | VARCHAR (18) | This column stores the list of rule records that contribute to the acuity scoring system. |
| LINKED_RULE_TYPE_C | INTEGER |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ACUITY_SYSTEM_ID | ACUITY_CONFIG | ACUITY_SYSTEM_ID | No | No | No |  |
| 1 | ACUITY_SYSTEM_ID | DISEASE_RISK_MODEL | ACUITY_SYSTEM_ID | No | No | No |  |
| 1 | ACUITY_SYSTEM_ID | PM_TRANSFER_CONFIG | ACUITY_SYSTEM_ID | No | No | No |  |
| 3 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 4 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 4 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 4 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 5 | MAJOR_RULES_ID | CLARITY_CER | RULE_ID | No | No | No |  |
| 5 | MAJOR_RULES_ID | CL_CHRG_EDIT_RULE | RULE_ID | No | No | No |  |
| 6 | LINKED_RULE_TYPE_C | ZC_LINKED_RULE_TYPE | LINKED_RULE_TYPE_C | No | No | No |  |
