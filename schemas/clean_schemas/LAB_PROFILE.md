# LAB_PROFILE

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=LAB_PROFILE

## Description

This table contains basic information about your labs. These are LDF records where the record type (item LDF 27) is set to department (6). It only contains information from the newest contact.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | FULL |
| Load Frequency | WEEKLY - FULL |
| Chronicles INI | LDF |
| Release Version | FALL 2004 |
| May contain EHI? | No |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| LAB_ID | VARCHAR (18) | The unique ID of the lab. |
| LAB_NAME | VARCHAR (254) | The name of the lab. |
| LAB_ABBR | VARCHAR (254) | The abbreviation of the lab name. |
| LDF_TYPE_C | INTEGER |  |
| LAB_STATUS_C | INTEGER |  |
| LAB_LINK_DEP_ID | NUMERIC (18,0) | The unique ID of the department for this lab. This item is used to associate the lab hierarchy with the main hierarchy setup in the department. |
| LAB_LLB_ID | NUMERIC (18,0) | The unique ID of the resulting agency for this lab. This links a lab to a resulting agency, and vice versa. |
| EXTERNAL_LAB_YN | VARCHAR (1) |  |
| INTERFACED_LAB_YN | VARCHAR (1) |  |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| CM_CT_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this contact. This is only populated if you use IntraConnect. |
| LAB_DATE | DATETIME | The date of this contact in calendar format. |
| EXTERNAL_LAB_URL | VARCHAR (254) | This URL provides a link to more information about this laboratory. |
| IS_USER_AUTH_YN | VARCHAR (1) |  |
| DEF_HLD_TO_APPLY_C | INTEGER |  |
| DISPLAY_WARN_MSG_YN | VARCHAR (1) |  |
| SUSCEPT_RULES_ID | NUMERIC (18,0) | The unique ID of the tree node containing susceptibility rules. |
| SPEC_TRACK_ENABL_YN *(deprecated)* | VARCHAR (1) |  |
| PRV_RSLT_USR_VRFY_C | INTEGER |  |
| NO_REL_UNSOL_QC_YN | VARCHAR (1) |  |
| RES_BY_EXT_LAB_YN | VARCHAR (1) |  |
| TAT_BASIS_C | INTEGER |  |
| RES_UPD_CORR_RSN_C | INTEGER |  |
| INTERF_ID_TYPE_ID | NUMERIC (18,0) | The unique ID of the MPI ID type to use in this lab for interfaces. |
| RECALC_DISP_DT_YN | VARCHAR (1) |  |
| AUTO_DISPOSE_YN | VARCHAR (1) |  |
| HOLD_INHERIT_C | INTEGER |  |
| AP_CHRG_REVIEW_YN *(deprecated)* | VARCHAR (1) |  |
| AP_CHRG_REVIEW_C | INTEGER |  |
| AUTO_CPT_PB_C | INTEGER |  |
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
| 1 | LAB_ID | AP_CASE_TYPES | LAB_ID | Unknown | No | No |  |
| 1 | LAB_ID | LAB_AP_LAB_SETUP | LAB_ID | Unknown | No | No |  |
| 1 | LAB_ID | LAB_INFO | LAB_ID | Unknown | No | No |  |
| 1 | LAB_ID | LAB_SECTION | SECTION_ID | Unknown | No | No |  |
| 1 | LAB_ID | LDF_REQ_SETUP | LAB_ID | Unknown | No | No |  |
| 1 | LAB_ID | WORKBENCH_PROFILE | WORKBENCH_ID | Unknown | No | No |  |
| 4 | LDF_TYPE_C | ZC_LDF_TYPE | LDF_TYPE_C | No | No | No |  |
| 5 | LAB_STATUS_C | ZC_LDF_STATUS | LDF_STATUS_C | No | No | No |  |
| 6 | LAB_LINK_DEP_ID | BH_DEP | DEPARTMENT_ID | No | No | No |  |
| 6 | LAB_LINK_DEP_ID | CLARITY_DEP | DEPARTMENT_ID | No | No | No |  |
| 6 | LAB_LINK_DEP_ID | CLARITY_DEP_2 | DEPARTMENT_ID | No | No | No |  |
| 6 | LAB_LINK_DEP_ID | CLARITY_DEP_3 | DEPARTMENT_ID | No | No | No |  |
| 6 | LAB_LINK_DEP_ID | CLARITY_DEP_4 | DEPARTMENT_ID | No | No | No |  |
| 6 | LAB_LINK_DEP_ID | CLARITY_DEP_5 | DEPARTMENT_ID | No | No | No |  |
| 6 | LAB_LINK_DEP_ID | CLARITY_DEP_MYC | DEPARTMENT_ID | No | No | No |  |
| 6 | LAB_LINK_DEP_ID | DEPT_QUEUE_MSG_SETTINGS | DEPARTMENT_ID | No | No | No |  |
| 6 | LAB_LINK_DEP_ID | DEPT_VERIFIED_INFO | DEPARTMENT_ID | No | No | No |  |
| 6 | LAB_LINK_DEP_ID | DEP_BATCH_LTR_GEN | DEPARTMENT_ID | No | No | No |  |
| 6 | LAB_LINK_DEP_ID | DEP_CE_SETTINGS | DEPARTMENT_ID | No | No | No |  |
| 6 | LAB_LINK_DEP_ID | DP_HIDE_SENSITIVE_CONFIG | DEPARTMENT_ID | No | No | No |  |
| 6 | LAB_LINK_DEP_ID | ED_ALRT_DFLT | DEPARTMENT_ID | No | No | No |  |
| 6 | LAB_LINK_DEP_ID | ED_DEP_SETTINGS | DEP_ID | No | No | No |  |
| 6 | LAB_LINK_DEP_ID | EXT_CAL_DEPT_CONFIG | DEPARTMENT_ID | No | No | No |  |
| 6 | LAB_LINK_DEP_ID | VISIT_MODE_CONFIG_DEP | DEPARTMENT_ID | No | No | No |  |
| 6 | LAB_LINK_DEP_ID | V_CUBE_D_DEPARTMENT | DEPARTMENT_ID | Unknown | Unknown | No |  |
| 6 | LAB_LINK_DEP_ID | V_CUBE_D_DEP_LOC | DEPARTMENT_ID | Unknown | Unknown | No |  |
| 7 | LAB_LLB_ID | CLARITY_LLB | RESULTING_LAB_ID | Unknown | No | No |  |
| 10 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 10 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 10 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |

_(50 total; showing first 30)_
