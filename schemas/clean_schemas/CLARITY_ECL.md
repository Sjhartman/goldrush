# CLARITY_ECL

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=CLARITY_ECL

## Description

This table contains information about security classes in the system.

**Primary table** in this group (110 cols). Overflow siblings joined on shared key: CLARITY_ECL_2 (72 cols). Prefer this table for most queries.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | FULL |
| Load Frequency | WEEKLY - FULL |
| Chronicles INI | ECL |
| Release Version | EPIC 2002 |
| May contain EHI? | No |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| ECL_ID | VARCHAR (18) | The unique ID (.1 item) of the security class record. |
| CLASSIFCTN_NAME | VARCHAR (80) | The name of the security class. |
| ECL_RECORD_STAT_C | INTEGER |  |
| CAD_INI_MENU | VARCHAR (40) | The initial menu specified for scheduling system. |
| SEC_STRING *(deprecated)* | VARCHAR (254) | The security string for the classification record. As of the Spring 2007 release, this item is now only extracted as <null> in order to avoid string truncation warnings and errors. |
| ENTRY_ACC_YN | VARCHAR (1) |  |
| VIEW_ACC_YN | VARCHAR (1) |  |
| OVRBK_ACC_YN | VARCHAR (1) |  |
| SUP_OVRBK_ACC_YN | VARCHAR (1) |  |
| OVRIDE_ACC_YN | VARCHAR (1) |  |
| OVRULE_ACC_YN | VARCHAR (1) |  |
| CHKIN_ACC_YN | VARCHAR (1) |  |
| CANC_ACC_YN | VARCHAR (1) |  |
| CHG_APPT_ACC_YN | VARCHAR (1) |  |
| TEMPLT_ACC_YN | VARCHAR (1) |  |
| GATEWAY_ACC_YN | VARCHAR (1) |  |
| TMPT_EXCP_ACC_YN | VARCHAR (1) |  |
| POS_CVG_ACC_YN *(deprecated)* | VARCHAR (1) |  |
| EOD_ACC_YN | VARCHAR (1) |  |
| SYS_UTIL_ACC_YN | VARCHAR (1) |  |
| USER_FUNC_ACC_YN | VARCHAR (1) |  |
| FORMS_ACC_YN | VARCHAR (1) |  |
| STAT_RPT_ACCT_YN | VARCHAR (1) |  |
| ED_PT_REC_YN | VARCHAR (1) |  |
| PTRN_BLD_YN | VARCHAR (1) |  |
| RPT_CAD_YN | VARCHAR (1) |  |
| WINGS_YN | VARCHAR (1) |  |
| FUNKEYS_YN | VARCHAR (1) |  |
| OVRD_CONF_DEP_YN | VARCHAR (1) |  |
| HOLD_ACC_YN | VARCHAR (1) |  |
| OVRD_HOLD_YN | VARCHAR (1) |  |
| BLK_OVR_ACC_YN | VARCHAR (1) |  |
| SES_LIM_OVR_ACC_YN | VARCHAR (1) |  |
| VIEW_TAKS_YN | VARCHAR (1) |  |
| EDIT_TASKS_YN | VARCHAR (1) |  |
| COMPLETE_TASKS_YN | VARCHAR (1) |  |
| SCHORD_ACC_YN | VARCHAR (1) |  |
| OPN_PT_REC_YN | VARCHAR (1) |  |
| OPN_STAFF_REC_YN | VARCHAR (1) |  |
| OPN_PRCD_REC_YN | VARCHAR (1) |  |
| OPN_DEPT_REC_YN | VARCHAR (1) |  |
| OPN_NEW_GRP_YN | VARCHAR (1) |  |
| CLASS_MENUS | VARCHAR (40) | The menus for classes. |
| MAIN_MNU_C | INTEGER |  |
| RPT_MNU_C | INTEGER |  |
| FRM_LST_MNU_C | INTEGER |  |
| STAT_MNU_C | INTEGER |  |
| TEMPLT_MNU_C | INTEGER |  |
| UTIL_MNU_C | INTEGER |  |
| USER_SEC_MNU_C | INTEGER |  |
| CAD_MGMT_MNU_C | INTEGER |  |
| OTH_SYS_MNU_C | INTEGER |  |
| BATCH_SCH_C | INTEGER |  |
| POS_MCS_MNU_C | INTEGER |  |
| OPR_MNU_C | INTEGER |  |
| CHT_TRK_MNU_C | INTEGER |  |
| REG_MNU_C | INTEGER |  |
| CREATE_PUB_RPT_YN | VARCHAR (1) |  |
| GUI_SLOT_ACC_YN | VARCHAR (1) |  |
| GUI_BLK_ACC_YN | VARCHAR (1) |  |
| GUI_PTFLG_ACC_YN | VARCHAR (1) |  |
| GUI_APPT_NOTF_YN | VARCHAR (1) |  |
| SCHD_TMPLT_MNU_C | INTEGER |  |
| CT_SEC_STRING *(deprecated)* | VARCHAR (40) | The Chart Tracking security string for the classification. |
| LAST_USER_ID *(deprecated)* | VARCHAR (18) | The ID of the last editor of the security classification. This column is now deprecated since the item is not filled in when the security classification is edited. |
| AR_INIT_MENU | VARCHAR (40) | The initial AR menu for the Resolute Professional Billing security class. |
| SEC_CLS_NAME | VARCHAR (255) | The on-screen edit class name. |
| CM_PHY_OWNER_ID | VARCHAR (25) | ID of the physical deployment owner for this record.  Physical owners will be where the data is hosted, either on the cross-over server or the owner deployment. |
| CM_LOG_OWNER_ID | VARCHAR (25) | ID of the logical deployment owner for this record.  Logical owners show the deployment where the record was created but doesn't represent if the record is a part of version skew. |
| LINK_APPT_ACC_YN | VARCHAR (1) |  |
| INTERP_REP_ACC_YN | VARCHAR (1) |  |
| WHICH_SYSTEM_C | INTEGER |  |
| DESK_FUTURE_YN | VARCHAR (1) |  |
| DESK_PAST_YN | VARCHAR (1) |  |
| OVERLAP_APPTS_YN | VARCHAR (1) |  |
| OVERLAP_CASES_YN | VARCHAR (1) |  |
| LINK_APPT_ORD_YN | VARCHAR (1) |  |
| EDIT_APPT_MSGS_YN | VARCHAR (1) |  |
| CANCEL_CHECKIN_YN | VARCHAR (1) |  |
| EDIT_EOD_STATUS_YN | VARCHAR (1) |  |
| CANCEL_SIGN_IN_YN | VARCHAR (1) |  |
| OVRIDE_REST_REC_YN | VARCHAR (1) |  |
| EDIT_APT_STS_ACC_YN | VARCHAR (1) |  |
| EDIT_TEMP_SDA_YN | VARCHAR (1) |  |
| CANCEL_TASKS_YN | VARCHAR (1) |  |
| REMOVEORD_ACC_YN | VARCHAR (1) |  |
| TEMP_BLD_YN | VARCHAR (1) |  |
| PROV_MSG_EDIT_YN | VARCHAR (1) |  |
| PAT_DISMISS_ACCS_YN | VARCHAR (1) |  |
| OVR_POOL_USE_ACC_YN | VARCHAR (1) |  |
| RECALL_REC_ACC_C | INTEGER |  |
| RECALL_LINKING_YN | VARCHAR (1) |  |
| PREREQ_LINK_C | INTEGER |  |
| PREREQ_VERIFY_YN | VARCHAR (1) |  |
| PREREQ_DELETE_YN | VARCHAR (1) |  |
| PREREQ_OVERRULE_YN | VARCHAR (1) |  |
| PREREQ_UNDO_STAT_YN | VARCHAR (1) |  |
| PREREQ_VERIFY_AP_YN | VARCHAR (1) |  |
| SUBGRP_EDIT_ACSS_C | INTEGER |  |
| CONFIG_SEC_CLASS_ID | VARCHAR (18) | The unique ID of the default profile for this security class. |
| OR_REPORT_ACCS_C | INTEGER |  |
| UNBLOCKED_ACCESS_C | INTEGER |  |
| USE_BLOCK_RESTR_YN | VARCHAR (1) |  |
| CASE_TRACK_SEC_YN | VARCHAR (1) |  |
| CASE_ENTRY_WORKFLOW *(deprecated)* | VARCHAR (192) | *** Deprecated ***  In table CLARITY_ECL, the column CASE_ENTRY_WORKFLOW (ECL/10101) has been deprecated. The deprecated column's data is no longer available since it is no longer populated in Chronicles. |
| CASE_ENTRY_TABS | VARCHAR (192) | The menu that lists which activity tabs should appear in record case entry. |
| LOG_ENTRY_WORKFLOW *(deprecated)* | VARCHAR (192) | *** Deprecated *** In table CLARITY_ECL, the column LOG_ENTRY_WORKFLOW (ECL/10106) has been deprecated. The deprecated column's content/data is no longer available since it is no longer populated in Chronicles.  This item stores the E2U record for the log entry menu. |
| LOG_ENTRY_TABS *(deprecated)* | VARCHAR (192) | *** Deprecated *** In table CLARITY_ECL, the column LOG_ENTRY_TABS (ECL/10107) has been deprecated. The deprecated column's content/data is no longer available since it is no longer populated in Chronicles.  The menu that lists which activity tabs should appear in record log entry. |
| LOG_SCRIPT_PREF_ID | VARCHAR (18) | This item stores the unique ID of the log script preference list. |
| CROSS_DEPL_QUERY_YN | VARCHAR (1) |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ECL_ID | CLARITY_ECL_2 | ECL_ID | Unknown | No | No |  |
| 1 | ECL_ID | ZC_DFLT_SEC_CLASS | DFLT_SEC_CLASS_C | Unknown | Unknown | No |  |
| 1 | ECL_ID | ZC_EW_USER_CLS | EW_USER_CLS_C | Unknown | Unknown | No |  |
| 3 | ECL_RECORD_STAT_C | ZC_ECL_RECORD_STAT | ECL_RECORD_STAT_C | No | No | No |  |
| 44 | MAIN_MNU_C | ZC_ECL_MENU | MAIN_MNU_C | No | No | No |  |
| 45 | RPT_MNU_C | ZC_ECL_MENU | MAIN_MNU_C | No | No | No |  |
| 46 | FRM_LST_MNU_C | ZC_ECL_MENU | MAIN_MNU_C | No | No | No |  |
| 47 | STAT_MNU_C | ZC_ECL_MENU | MAIN_MNU_C | No | No | No |  |
| 48 | TEMPLT_MNU_C | ZC_ECL_MENU | MAIN_MNU_C | No | No | No |  |
| 49 | UTIL_MNU_C | ZC_ECL_MENU | MAIN_MNU_C | No | No | No |  |
| 50 | USER_SEC_MNU_C | ZC_ECL_MENU | MAIN_MNU_C | No | No | No |  |
| 51 | CAD_MGMT_MNU_C | ZC_ECL_MENU | MAIN_MNU_C | No | No | No |  |
| 52 | OTH_SYS_MNU_C | ZC_ECL_MENU | MAIN_MNU_C | No | No | No |  |
| 53 | BATCH_SCH_C | ZC_ECL_MENU | MAIN_MNU_C | No | No | No |  |
| 54 | POS_MCS_MNU_C | ZC_ECL_MENU | MAIN_MNU_C | No | No | No |  |
| 55 | OPR_MNU_C | ZC_ECL_MENU | MAIN_MNU_C | No | No | No |  |
| 56 | CHT_TRK_MNU_C | ZC_ECL_MENU | MAIN_MNU_C | No | No | No |  |
| 57 | REG_MNU_C | ZC_REG_MNU | REG_MNU_C | No | No | No |  |
| 63 | SCHD_TMPLT_MNU_C | ZC_ECL_MENU | MAIN_MNU_C | No | No | No |  |
| 68 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 68 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 68 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 69 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 69 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 69 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 72 | WHICH_SYSTEM_C | ZC_WHICH_SYSTEM | WHICH_SYSTEM_C | No | No | No |  |
| 91 | RECALL_REC_ACC_C | ZC_RECALL_REC_ACC | RECALL_REC_ACC_C | No | No | No |  |
| 93 | PREREQ_LINK_C | ZC_PREREQ_LINK | PREREQ_LINK_C | No | No | No |  |
| 99 | SUBGRP_EDIT_ACSS_C | ZC_SUBGRP_EDIT_ACS | SUBGRP_EDIT_ACS_C | No | No | No |  |
| 100 | CONFIG_SEC_CLASS_ID | INSULIN_INSTR_PROF_DFLTS | PROFILE_ID | No | No | No |  |

_(33 total; showing first 30)_
