# CL_CHRG_EDIT_RULE

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=CL_CHRG_EDIT_RULE

## Description

This table contains rule information.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | CER |
| Release Version | MU1 - EPIC 2002 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| RULE_ID | VARCHAR (18) | The unique ID of the rule. |
| RULE_NAME | VARCHAR (254) | The name of the rule. |
| CM_PHY_OWNER_ID | VARCHAR (25) | ID of the physical deployment owner for this record.  Physical owners will be where the data is hosted, either on the cross-over server or the owner deployment. |
| CM_LOG_OWNER_ID | VARCHAR (25) | ID of the logical deployment owner for this record.  Logical owners show the deployment where the record was created but doesn't represent if the record is a part of version skew. |
| DISPLAY_NAME | VARCHAR (250) | This is the display name to use for the rule when it is used as a column in patient lists and as a heading in reports. |
| RPT_DISPLAY_PP_ID | NUMERIC (18,0) | This is the programming point which gets an array of data to show in the report for a given rule in an acuity system. |
| RULE_DESCRIP_STRING | VARCHAR (1000) | This string is used by the standard rule display programming point to determine what explanation to show for the rule. The strings @#@ will be replaced by the appropriate property values (e.g., "@1@" becomes the first property), and @S@ becomes the rule score). |
| PERF_MEASURE_C | INTEGER |  |
| RULE_RETURN_TYPE_C | INTEGER |  |
| NETWORKED_INI | VARCHAR (254) | Database which the return value of this rule is linked to. This may not be applicable for all rules. |
| NETWORKED_ITEM | VARCHAR (254) | Item which this rule's return value is networked to. For example, if this rule returns a category value, this would be the item which defines that category list. |
| OVRIDE_STATUS_C | INTEGER |  |
| OVRIDE_CONTEXT | VARCHAR (62) | The rule override context. |
| OVRIDE_PARENT_ID | VARCHAR (18) | The rule override record's parent record ID. |
| OVRIDE_INSTANT_TM | DATETIME (Local) | The instant when the rule override record was last compiled. |
| OVERRIDABLE_YN | VARCHAR (1) |  |
| RULE_ACTIVITY | VARCHAR (192) | This column stores the activity that should be launched for this rule. |
| RULE_PATLIST_COL_ID | NUMERIC (18,0) | This column stores the PAF ID which would be displayed in the patient list activity for this rule. |
| EFF_DATE | DATETIME | The date a rule becomes effective. |
| DESCRIPTION | VARCHAR (4000) | A general description of the rule. |
| DEPEND_FINAL_YN *(deprecated)* | VARCHAR (1) |  |
| RULE_CONTEXT_ID | NUMERIC (18,0) | The type of the rule. |
| EXT_CDI_PRIORITY_COMPONENT | VARCHAR (184) | This holds the identifier for a CDI priority component from a third-party prioritization application that this rule looks up. |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | RULE_ID | CLARITY_CER | RULE_ID | No | No | No |  |
| 3 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 4 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 4 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 4 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 6 | RPT_DISPLAY_PP_ID | CLARITY_LPP | LPP_ID | Unknown | No | No |  |
| 8 | PERF_MEASURE_C | ZC_PERF_MEASURE | PERF_MEASURE_C | No | No | No |  |
| 9 | RULE_RETURN_TYPE_C | ZC_RULE_RETURN_TYP | RULE_RETURN_TYP_C | No | No | No |  |
| 12 | OVRIDE_STATUS_C | ZC_OVERRDE_STATUS | OVERRDE_STATUS_C | No | No | No |  |
| 14 | OVRIDE_PARENT_ID | CLARITY_CER | RULE_ID | No | No | No |  |
| 14 | OVRIDE_PARENT_ID | CL_CHRG_EDIT_RULE | RULE_ID | No | No | No |  |
| 18 | RULE_PATLIST_COL_ID | REPORT_COLUMN_INFO | COLUMN_ID | No | No | No |  |
