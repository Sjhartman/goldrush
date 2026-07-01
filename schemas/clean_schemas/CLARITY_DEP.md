# CLARITY_DEP

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=CLARITY_DEP

## Description

The CLARITY_DEP table contains high-level information about departments.

**Primary table** in this group (110 cols). Overflow siblings joined on shared key: CLARITY_DEP_2 (100 cols), CLARITY_DEP_3 (100 cols), CLARITY_DEP_4 (100 cols), CLARITY_DEP_5 (17 cols). Prefer this table for most queries.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | DEP |
| Release Version | EPIC 2000 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| DEPARTMENT_ID | NUMERIC (18,0) | The unique ID number assigned to the department record. |
| DEPARTMENT_NAME | VARCHAR (254) | The name of the department. |
| DEPT_ABBREVIATION | VARCHAR (20) | The abbreviation of the department name. |
| SPECIALTY | VARCHAR (50) |  |
| REV_LOC_ID | NUMERIC (18,0) | The unique ID of the revenue location to which the department is linked. |
| DEP_GROUP | INTEGER |  |
| GL_PREFIX | VARCHAR (128) | The code that the General Ledger report uses to sort the departments if you use Department as a sorting category in your facility. |
| RPT_GRP_ONE | VARCHAR (80) | You can specify groupers for enterprise reporting, SQL, or report generator reporting. This is one of the free-text report groupers. |
| RPT_GRP_TWO | VARCHAR (80) | You can specify groupers for enterprise reporting, SQL, or report generator reporting. This is one of the free-text report groupers. |
| RPT_GRP_THREE | VARCHAR (80) | You can specify groupers for enterprise reporting, SQL, or report generator reporting. This is one of the free-text report groupers. |
| RPT_GRP_FOUR | VARCHAR (80) | You can specify groupers for enterprise reporting, SQL, or report generator reporting. This is one of the free-text report groupers. |
| RPT_GRP_FIVE | VARCHAR (80) | You can specify groupers for enterprise reporting, SQL, or report generator reporting. This is one of the free-text report groupers. |
| RPT_GRP_SIX | VARCHAR (66) |  |
| RPT_GRP_SEVEN | VARCHAR (66) |  |
| RPT_GRP_EIGHT | VARCHAR (66) |  |
| RPT_GRP_NINE | VARCHAR (66) |  |
| RPT_GRP_TEN | VARCHAR (66) |  |
| ADT_PARENT_ID | NUMERIC (18,0) | The unique ID of the location that serves as the parent in your facility?s ADT organizational structure. |
| SERV_AREA_ID | No | The unique ID of the service area in which this department is located. This is the service area for the department, calculated by the function EPIC_DEPTOSA; this function is needed because the service area is linked to the location record and not to the department record directly. |
| SPECIALTY_DEP_C | VARCHAR (66) |  |
| LICENSED_BEDS | INTEGER | The current number of licensed beds for this department. |
| MASTER_POOL_ID | VARCHAR (18) | The ID of the master radiology pool for this department. |
| MASTER_POOL_NAME *(deprecated)* | VARCHAR (254) | This column is deprecated and does not extract any data. This column should not be used as it can get out of sync if the name of the pool (PLS) record is changed. Use CLARITY_DEP.MASTER_POOL_ID to link to SCHED_POOL_INFO.POOL_ID and use SCHED_POOL_INFO.POOL_NAME instead. |
| COVERING_POOL_ID | VARCHAR (18) | The ID of the covering pool for this department. |
| COVERING_POOL_NAME *(deprecated)* | VARCHAR (30) | This column is deprecated and does not extract any data. This column should not be used as it can get out of sync if the name of the pool (PLS) record is changed. Use CLARITY_DEP.COVERING_POOL_ID to link to SCHED_POOL_INFO.POOL_ID and use SCHED_POOL_INFO.POOL_NAME instead. |
| FLASH_CARD_PRT_ROU | VARCHAR (255) | The routine used to print flash cards in this department. |
| NUM_FLASH_CARDS | INTEGER | The number of flash cards to print in this department. |
| CTRL_SHEET_ROU | VARCHAR (255) | The routine used to print control sheets in this department. |
| NUM_CONTROL_SHEETS | INTEGER | The number of control sheets to print in this department. |
| ADT_UNIT_TYPE_C | INTEGER |  |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| RPT_GRP_ELEVEN_C | VARCHAR (66) |  |
| RPT_GRP_TWELVE_C | VARCHAR (66) |  |
| RPT_GRP_THIRTEEN_C | VARCHAR (66) |  |
| RPT_GRP_FOURTEEN_C | VARCHAR (66) |  |
| RPT_GRP_FIFTEEN_C | VARCHAR (66) |  |
| RPT_GRP_SIXTEEN_C | VARCHAR (66) |  |
| RPT_GRP_SEVNTEEN_C | VARCHAR (66) |  |
| RPT_GRP_EIGHTEEN_C | VARCHAR (66) |  |
| RPT_GRP_NINETEEN_C | VARCHAR (66) |  |
| RPT_GRP_TWENTY_C | VARCHAR (66) |  |
| DFLT_PHARMACY_ID | NUMERIC (18,0) | The ID of the pharmacy linked to the department record. |
| CENTER_C | VARCHAR (254) |  |
| RECORD_STATUS | INTEGER |  |
| OUTPAT_DUP_INT_STR | VARCHAR (254) | Indicate the lookback time for duplicate checking. This item stores the string value of the duplicate interval (in days). This value is converted into hours and populated into item-17210 Outpatient Duplicate Interval. To specify an interval in DAYS, you can enter a positive number. To specify an interval in HOURS, you can enter it in terms of days. (e.g., to specify 6 hours, enter .25) To specify the interval in weeks, you can enter a number/fraction followed by the letter W. (e.g., to specify 3 weeks, type 3W or 3.0W). The value is converted to equivalent days and displayed to the user. Note: Large interval values may cause the system to slow down considerably. Please consult your system Technical Services Representative before setting large values in this field. When a procedure is ordered, a check is made to see if that procedure had been previously ordered within the duplicate interval. If found, the user is asked whether to continue placing the order. The order in which duplicate interval is looked up is -  Procedure -> Procedure Category -> Department -> Misc. configuration If the interval value in the Misc. Configuration level is used and if the interval is empty or equal to zero, the system will check duplicates against orders placed in the same session; if the interval is -1, the duplicate check will be disabled |
| INPAT_DUP_INT_STR | VARCHAR (254) | Indicate the lookback time for duplicate checking. This item stores the string value of the duplicate interval (in days). This value is converted into hours and populated into item-17220 Inpatient Duplicate Interval. To specify an interval in DAYS, you can enter a positive number. To specify an interval in HOURS, you can enter it in terms of days. (e.g., to specify 6 hours, enter .25) To specify the interval in weeks, you can enter a number/fraction followed by the letter W. (e.g., to specify 3 weeks, type 3W or 3.0W). The value is converted to equivalent days and displayed to the user. Note: Large interval values may cause the system to slow down considerably. Please consult your system Technical Services Representative before setting large values in this field. When a procedure is ordered, a check is made to see if that procedure had been previously ordered within the duplicate interval. If found, the user is asked whether to continue placing the order. The order in which duplicate interval is looked up is -Procedure -> Procedure Category -> Department -> Misc. configuration If the interval value in the Misc. Configuration level is used and if the interval is empty or equal to zero, the system will check duplicates against orders placed in the same session; if the interval is -1, the duplicate check will be disabled. |
| RX_LOGON_PHR_ID | NUMERIC (18,0) | When the user logs on to this department, this will be treated as the pharmacy the user logged into. This will be used as default pharmacy when you start some Pharmacy activities, such as Cart Fill, Triggered Fill. |
| RX_CHARGE_ADMIN_YN | VARCHAR (254) |  |
| MAR_LABEL_PRNTR_ID | VARCHAR (18) | The printer ID for MAR label. |
| ALLOW_AUTO_FUT_YN | VARCHAR (1) |  |
| DEF_COE_ORD_MOD_C | INTEGER |  |
| ORD_MOD_OP_CAP | VARCHAR (254) | Specify the caption to display for outpatient mode here. The default caption for outpatient mode is "After visit". |
| ORD_MOD_IP_CAP | VARCHAR (254) | Specify the caption to display for inpatient mode here. The default caption for inpatient mode is "During visit". |
| IP_MED_PREF_ID | NUMERIC (18,0) | The facility preference list provides an additional preference list layer between the user's preference list and the full database. It allows the user to search for medications and procedures on a smaller subset of the full database if they do not find any matches on their personal list. |
| MR_HSB_LINK_USER | VARCHAR (18) | The user record to be used to record in the audit trail when a contact is auto-linked to (or unlinked from) an episode. |
| COST_CENTER_ID | NUMERIC (18,0) | This column holds the internal cost center identifier associated with a given department. Please note to get the external cost center identifier you will need to link to CL_COST_CNTR. |
| REQ_ADM_HAR_MCH_YN | VARCHAR (1) |  |
| USE_HAR_REC_YN | VARCHAR (1) |  |
| HAR_DEF_ACT_TYPE_C | INTEGER |  |
| COPAY_WAIVE_C | INTEGER |  |
| IGNOR_DSP_PATXFR_YN | VARCHAR (1) |  |
| PROMPT_REDIR_YN | VARCHAR (1) |  |
| PROMPT_DYS_CHK_C | INTEGER | This item stores the number of days ahead that the system should prompt for confirmation |
| PROMPT_MSG_TEXT_C | VARCHAR (254) | This item stores a configurable prompt to use in the encounter redirection pop-up. The default prompt if no value is entered here is "Will this visit be charted separately from the admission? Selecting [No] will attach it to the admission." |
| NEAREST_PROC_TIME | INTEGER | Nearest unit of time for scheduling procedure orders |
| NEAREST_PROC_TIME_C | INTEGER |  |
| DEP_ED_TYPE_C | INTEGER |  |
| SCHD_INTRP_AUTO_YN | VARCHAR (1) |  |
| RPT_GRP_TWENTYONE | VARCHAR (254) | Users can specify groupers for enterprise reporting, SQL, or report generator reporting. This is one of the free-text report groupers. |
| RPT_GRP_TWENTYTWO | VARCHAR (254) | Users can specify groupers for enterprise reporting, SQL, or report generator reporting. This is one of the free-text report groupers. |
| RPT_GRP_TWENTYTHREE | VARCHAR (254) | Users can specify groupers for enterprise reporting, SQL, or report generator reporting. This is one of the free-text report groupers. |
| RPT_GRP_TWENTYFOUR | VARCHAR (254) | Users can specify groupers for enterprise reporting, SQL, or report generator reporting. This is one of the free-text report groupers. |
| RPT_GRP_TWENTYFIVE | VARCHAR (254) | Users can specify groupers for enterprise reporting, SQL, or report generator reporting. This is one of the free-text report groupers. |
| RPT_GRP_TWENTYSIX | VARCHAR (254) | Users can specify groupers for enterprise reporting, SQL, or report generator reporting. This is one of the free-text report groupers. |
| RPT_GRP_TWENTYSEVEN | VARCHAR (254) | Users can specify groupers for enterprise reporting, SQL, or report generator reporting. This is one of the free-text report groupers. |
| RPT_GRP_TWENTYEIGHT | VARCHAR (254) | Users can specify groupers for enterprise reporting, SQL, or report generator reporting. This is one of the free-text report groupers. |
| RPT_GRP_TWENTYNINE | VARCHAR (254) | Users can specify groupers for enterprise reporting, SQL, or report generator reporting. This is one of the free-text report groupers. |
| RPT_GRP_THIRTY | VARCHAR (254) | Users can specify groupers for enterprise reporting, SQL, or report generator reporting. This is one of the free-text report groupers. |
| RPT_GRP_THIRTYONE_C | VARCHAR (66) |  |
| RPT_GRP_THIRTYTWO_C | VARCHAR (66) |  |
| RPT_GRP_TRTYTHREE_C | VARCHAR (66) |  |
| RPT_GRP_TRTYFOUR_C | VARCHAR (66) |  |
| RPT_GRP_TRTYFIVE_C | VARCHAR (66) |  |
| RPT_GRP_THIRTYSIX_C | VARCHAR (66) |  |
| RPT_GRP_TRTYSEVEN_C | VARCHAR (66) |  |
| RPT_GRP_TRTYEIGHT_C | VARCHAR (66) |  |
| RPT_GRP_TRTYNINE_C | VARCHAR (66) |  |
| RPT_GRP_FOURTY_C | VARCHAR (66) |  |
| REVERIFY_ORDERS_YN | VARCHAR (1) |  |
| PPL_DEPT_YN | VARCHAR (1) |  |
| EXTERNAL_NAME | VARCHAR (254) | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| PHONE_NUMBER | VARCHAR (254) | The phone number of the department. This is often used in patient correspondence such as reminder letters. |
| OR_UNIT_TYPE_C | INTEGER |  |
| BED_COLUMN_INFO_ID | NUMERIC (18,0) | The unique ID of the extension which returns the room info. |
| IS_PERIOP_DEP_YN | VARCHAR (1) |  |
| TX_PLAN_REL_CATS_ID | NUMERIC (18,0) | The unique ID of the extension that determines which categories are currently allowed to release. |
| FACILITY_C | VARCHAR (66) |  |
| INPATIENT_DEPT_YN | VARCHAR (1) |  |
| CARE_AREA_C | INTEGER |  |
| RESTRICTED_DEPT_YN | VARCHAR (1) |  |
| PHYSICAL_LOC_C | INTEGER |  |
| LAG_TIME | INTEGER | The number of minutes to keep between appointments for a given patient within the same department. The lag time runs from the end of one appointment to the beginning of the next. |
| AUTO_PROMPT_CNTR_YN | VARCHAR (1) |  |
| CLM_ALT_NAME | VARCHAR (254) | The department level claim alternate address name that you want to be printed on claims. This name could appear in Box 33 on paper CMS, FL1 on UB, BA0-18 on NSF and 2010AB-NM1-03 on ANSI claim forms. |
| CLM_ALT_CITY | VARCHAR (66) | The department level claim alternate address city that you want to be printed on claims. |
| CLM_ALT_STATE_C | VARCHAR (66) |  |
| CLM_ALT_ZIP | VARCHAR (10) | The department level claim alternate address zip that you want to be printed on claims. |
| CLM_ALT_PHONE | VARCHAR (30) | The department level claim alternate phone number that you want to be printed on claims. |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| B-TREE INDEX | EIX_CLARITY_DEP_SPEC_C | SPECIALTY_DEP_C | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_CLARITY_DEP__REV_DEP | REV_LOC_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_CLARITY_DEP__REV_DEP | DEPARTMENT_ID | 2 | Yes | Yes |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | DEPARTMENT_ID | BH_DEP | DEPARTMENT_ID | No | No | No |  |
| 1 | DEPARTMENT_ID | CLARITY_DEP_2 | DEPARTMENT_ID | No | No | No |  |
| 1 | DEPARTMENT_ID | CLARITY_DEP_3 | DEPARTMENT_ID | No | No | No |  |
| 1 | DEPARTMENT_ID | CLARITY_DEP_4 | DEPARTMENT_ID | No | No | No |  |
| 1 | DEPARTMENT_ID | CLARITY_DEP_5 | DEPARTMENT_ID | No | No | No |  |
| 1 | DEPARTMENT_ID | CLARITY_DEP_MYC | DEPARTMENT_ID | No | No | No |  |
| 1 | DEPARTMENT_ID | DEPT_QUEUE_MSG_SETTINGS | DEPARTMENT_ID | No | No | No |  |
| 1 | DEPARTMENT_ID | DEPT_VERIFIED_INFO | DEPARTMENT_ID | No | No | No |  |
| 1 | DEPARTMENT_ID | DEP_BATCH_LTR_GEN | DEPARTMENT_ID | No | No | No |  |
| 1 | DEPARTMENT_ID | DEP_CE_SETTINGS | DEPARTMENT_ID | No | No | No |  |
| 1 | DEPARTMENT_ID | DP_HIDE_SENSITIVE_CONFIG | DEPARTMENT_ID | No | No | No |  |
| 1 | DEPARTMENT_ID | ED_ALRT_DFLT | DEPARTMENT_ID | No | No | No |  |
| 1 | DEPARTMENT_ID | ED_DEP_SETTINGS | DEP_ID | No | No | No |  |
| 1 | DEPARTMENT_ID | EXT_CAL_DEPT_CONFIG | DEPARTMENT_ID | No | No | No |  |
| 1 | DEPARTMENT_ID | VISIT_MODE_CONFIG_DEP | DEPARTMENT_ID | No | No | No |  |
| 1 | DEPARTMENT_ID | V_CUBE_D_DEPARTMENT | DEPARTMENT_ID | Unknown | Unknown | No |  |
| 1 | DEPARTMENT_ID | V_CUBE_D_DEP_LOC | DEPARTMENT_ID | Unknown | Unknown | No |  |
| 5 | REV_LOC_ID | ANALYTICS_SYSTEM_SETTINGS | FACILITY_ID | No | No | No |  |
| 5 | REV_LOC_ID | ARPB_SA_SETTINGS | FACILITY_ID | No | No | No |  |
| 5 | REV_LOC_ID | CLARITY_LOC | LOC_ID | Unknown | No | No |  |
| 5 | REV_LOC_ID | CLARITY_LOC_2 | LOC_ID | Unknown | No | No |  |
| 5 | REV_LOC_ID | CLARITY_POS | POS_ID | No | No | No |  |
| 5 | REV_LOC_ID | CLARITY_POS_2 | POS_ID | No | No | No |  |
| 5 | REV_LOC_ID | CLARITY_SA | SERV_AREA_ID | Unknown | No | No |  |
| 5 | REV_LOC_ID | CL_LOC_HIERARCHY | LOC_ID | Unknown | No | No |  |
| 5 | REV_LOC_ID | CV_PCI_D2B_SETTINGS | FACILITY_ID | No | No | No |  |
| 5 | REV_LOC_ID | EAF_CLM_ALTADR_INF | FACILITY_ID | No | No | No |  |
| 5 | REV_LOC_ID | EAF_CLM_RMT_SETUP | FACILITY_ID | No | No | No |  |
| 5 | REV_LOC_ID | EAF_EXP_APPT_LOG | FACILITY_ID | No | No | No |  |
| 5 | REV_LOC_ID | EAF_SEARCH_TERMS | FACILITY_ID | No | No | No |  |

_(220 total; showing first 30)_
