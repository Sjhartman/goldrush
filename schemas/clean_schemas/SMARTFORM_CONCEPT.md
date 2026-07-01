# SMARTFORM_CONCEPT

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=SMARTFORM_CONCEPT

## Description

This table contains information about SmartData elements that are data bound on SmartForms.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | LQF |
| Release Version | SPRING 2007 |
| May contain EHI? | No |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| FORM_ID | VARCHAR (18) | The unique ID of the SmartForm. |
| CONTACT_DATE_REAL | No | This is a numeric representation of the date of this encounter in your system. The integer portion of the number specifies the date of the encounter. The digits after the decimal point indicate multiple visits on one day. |
| LINE | No | The line number of the over time related group items. |
| CONTACT_DATE | DATETIME | The contact date in external format. |
| CM_PHY_OWNER_ID | VARCHAR (25) | ID of the physical deployment owner for this record.  Physical owners will be where the data is hosted, either on the cross-over server or the owner deployment. |
| CM_LOG_OWNER_ID | VARCHAR (25) | ID of the logical deployment owner for this record.  Logical owners show the deployment where the record was created but doesn't represent if the record is a part of version skew. |
| CM_CT_OWNER_ID | VARCHAR (25) | Contact owner for the current SmartForm. |
| CONCEPT_ID | 40 | The SmartData Identifier (SDI) of the SmartData element used in this SmartForm. |
| CONCEPT_LIST_ID | VARCHAR (18) | This item stores the LQL records used in this SmartForm. |
| CONCEPT_CONTEXT_ID | NUMERIC (18,0) | The ID of the context in which this SmartData element is used. |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | FORM_ID | CL_QFORM | FORM_ID | No | No | No |  |
| 1 | FORM_ID | CL_QFORM1 | FORM_ID | Unknown | No | No |  |
| 1 | FORM_ID | DECISION_TREE_INFO | DTREE_ID | No | No | No |  |
| 1 | FORM_ID | QUESR_INSTRUCTIONS | FORM_ID | No | No | No |  |
| 1 | FORM_ID | CL_QFORM_OVTM | FORM_ID | No | No | No |  |
| 2 | CONTACT_DATE_REAL | CONTACT_DATE_REAL |  |  |  |  |  |
| 1 | FORM_ID | DTREE_INFO_OVTM | DTREE_ID | No | No | No |  |
| 2 | CONTACT_DATE_REAL | CONTACT_DATE_REAL |  |  |  |  |  |
| 1 | FORM_ID | UM_QUESTION_SET | FORM_ID | No | No | No |  |
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
| 9 | CONCEPT_LIST_ID | CL_QQUEST | QUEST_ID | No | No | No |  |
