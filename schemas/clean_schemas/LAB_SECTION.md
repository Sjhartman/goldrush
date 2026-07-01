# LAB_SECTION

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=LAB_SECTION

## Description

This table contains information about your lab sections. These are LDF records where the record type (item LDF 27) is set to section (7). It only contains information from the newest contact.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | LDF |
| Release Version | SPRING 2006 |
| May contain EHI? | No |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| SECTION_ID | VARCHAR (18) | The unique ID of the lab section. |
| LDF_TYPE_C | INTEGER |  |
| LAB_ID | VARCHAR (18) | The unique ID of the lab this section is part of. |
| SECTION_NAME | VARCHAR (254) | The name of the lab section. |
| SECTION_ABBR | VARCHAR (254) | The abbreviation of the lab section name. |
| SECTION_STATUS_C | INTEGER |  |
| OTSTND_LIST_REFRESH | INTEGER | Outstanding list refresh interval (in seconds). |
| LLB_LAB_ID | NUMERIC (18,0) | The unique ID of the resulting agency for this lab section. This links a lab section to a resulting agency, and vice versa. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| CM_CT_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this contact. This is only populated if you use IntraConnect. |
| LAB_DATE | DATETIME | The date of this contact in calendar format. |
| CRIT_PUSH_PRELIM_RULE_ID | VARCHAR (18) | Prelim verification rule to qualify a result as needing critical result follow-up and push notification. |
| CRIT_PUSH_PRELIM_UNCALL_YN | VARCHAR (1) |  |
| CRIT_PUSH_PRELIM_DISABLE_YN | VARCHAR (1) |  |
| CRIT_PUSH_FINAL_RULE_ID | VARCHAR (18) | Final verification rule to qualify a result as needing critical result follow-up and push notification. |
| CRIT_PUSH_FINAL_UNCALL_YN | VARCHAR (1) |  |
| CRIT_PUSH_FINAL_DISABLE_YN | VARCHAR (1) |  |
| CRIT_SUPPRESS_CREAT_OL_ROW_YN | VARCHAR (1) | Surrogate key used to uniquely identify rows in this (and only this) table on Cogito Cloud only, do not assume the surrogate key in this table will correspond to the surrogate key in another table |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | SECTION_ID | AP_CASE_TYPES | LAB_ID | Unknown | No | No |  |
| 1 | SECTION_ID | LAB_AP_LAB_SETUP | LAB_ID | Unknown | No | No |  |
| 1 | SECTION_ID | LAB_INFO | LAB_ID | Unknown | No | No |  |
| 1 | SECTION_ID | LAB_PROFILE | LAB_ID | Unknown | No | No |  |
| 1 | SECTION_ID | LDF_REQ_SETUP | LAB_ID | Unknown | No | No |  |
| 1 | SECTION_ID | WORKBENCH_PROFILE | WORKBENCH_ID | Unknown | No | No |  |
| 2 | LDF_TYPE_C | ZC_LDF_TYPE | LDF_TYPE_C | No | No | No |  |
| 3 | LAB_ID | AP_CASE_TYPES | LAB_ID | Unknown | No | No |  |
| 3 | LAB_ID | LAB_AP_LAB_SETUP | LAB_ID | Unknown | No | No |  |
| 3 | LAB_ID | LAB_INFO | LAB_ID | Unknown | No | No |  |
| 3 | LAB_ID | LAB_PROFILE | LAB_ID | Unknown | No | No |  |
| 3 | LAB_ID | LAB_SECTION | SECTION_ID | Unknown | No | No |  |
| 3 | LAB_ID | LDF_REQ_SETUP | LAB_ID | Unknown | No | No |  |
| 3 | LAB_ID | WORKBENCH_PROFILE | WORKBENCH_ID | Unknown | No | No |  |
| 6 | SECTION_STATUS_C | ZC_LDF_STATUS | LDF_STATUS_C | No | No | No |  |
| 8 | LLB_LAB_ID | CLARITY_LLB | RESULTING_LAB_ID | Unknown | No | No |  |
| 9 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 9 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 9 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 10 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 10 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 10 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 11 | CM_CT_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 11 | CM_CT_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 11 | CM_CT_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 13 | CRIT_PUSH_PRELIM_RULE_ID | CLARITY_CER | RULE_ID | No | No | No |  |
| 13 | CRIT_PUSH_PRELIM_RULE_ID | CL_CHRG_EDIT_RULE | RULE_ID | No | No | No |  |
| 16 | CRIT_PUSH_FINAL_RULE_ID | CLARITY_CER | RULE_ID | No | No | No |  |
| 16 | CRIT_PUSH_FINAL_RULE_ID | CL_CHRG_EDIT_RULE | RULE_ID | No | No | No |  |
