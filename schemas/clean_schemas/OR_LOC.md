# OR_LOC

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=OR_LOC

## Description

The OR_LOC table contains information about surgical, radiology, and invasive lab locations.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | EAF |
| Release Version | MU7 - MAY 2001 |
| May contain EHI? | No |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| LOC_ID | NUMERIC (18,0) | The unique ID of the location record. |
| DEP_ID | NUMERIC (18,0) | The unique ID of the scheduling department record. This column does not store the department linked to the OR Location. That information is stored in OR_LOC__OR_DEPARTMENT_ID. |
| TR_SKIP_SAT_YN | VARCHAR (1) |  |
| TR_SKIP_SUN_YN | VARCHAR (1) |  |
| EOD_OFFSET_DAYS | INTEGER | The offset in days after which OR management system End of Day will process cases. |
| CM_PHY_OWNER_ID | VARCHAR (25) | ID of the physical deployment owner for this record.  Physical owners will be where the data is hosted, either on the cross-over server or the owner deployment. |
| CM_LOG_OWNER_ID | VARCHAR (25) | ID of the logical deployment owner for this record.  Logical owners show the deployment where the record was created but doesn't represent if the record is a part of version skew. |
| LOCATION_TYPE_C | INTEGER |  |
| SUP_LKUP_TMP_CRT_YN | VARCHAR (1) |  |
| DEC_INV_BALANCE_YN | VARCHAR (1) |  |
| IMP_BC_DATA_MOD_ID | NUMERIC (18,0) | Specify the programming point which will be called after extracting the data out of the implant barcode. This programming point can be used to modify the data before sending it to Hyperspace. |
| IMP_BC_HIBC_SEC_C | INTEGER |  |
| NEW_PAT_ACTIVITY | VARCHAR (254) | Holds the descriptor of the E2N to launch when a new patient is created from within OpTime. |
| NEW_PAT_MENU | VARCHAR (254) | Holds the descriptor of the E2U to use as the activity toolbar when a new patient is created from within OpTime. |
| NEW_PAT_LPP_ID | NUMERIC (18,0) | Holds the programming point to fire when a new patient is created from within OpTime. |
| HOL_SAT_ACT_C | INTEGER |  |
| HOL_SUN_ACT_C | INTEGER |  |
| HOL_SAT_SKIP_YN | VARCHAR (1) |  |
| HOL_SUN_SKIP_YN | VARCHAR (1) |  |
| HSB_TYP_FOR_CASE_ID | NUMERIC (18,0) | This column will store the type of the patient episode that will be created for a case. |
| AUTO_CRT_HSB_YN | VARCHAR (1) |  |
| USE_STRUCTURE_FR_YN *(deprecated)* | VARCHAR (1) |  |
| IMP_NAME_SYNCH_C | INTEGER |  |
| DFLT_MARKUP_TBL_ID | NUMERIC (18,0) | The unique ID of the default Inventory Markup Table for this location.  This column is frequently used to link to the INV_MARKUP_TBL table. |
| OR_DEPARTMENT_ID | NUMERIC (18,0) | The unique ID of the linked OR department record. Use this department column as a link to the ADT facility structure. |
| ANESTH_ST_EVENT_C | VARCHAR (66) |  |
| ANESTH_END_EVENT_C | VARCHAR (66) |  |
| CASE_VIEW_ONLY_YN | VARCHAR (1) |  |
| IN_ROOM_EVENT_C | VARCHAR (66) |  |
| PAT_LOC_IN_ROOM_ID *(deprecated)* | NUMERIC (18,0) | In table OR_LOC, the column PAT_LOC_IN_ROOM_ID (EAF/53496) has been deprecated. The deprecated column's content/data is no longer available since it is no longer populated in Chronicles. |
| PAT_LOC_OUT_PACU_ID *(deprecated)* | NUMERIC (18,0) | In table OR_LOC, the column PAT_LOC_OUT_PACU_ID (EAF/53497) has been deprecated. The deprecated column's content/data is no longer available since it is no longer populated in Chronicles. |
| OUT_PREOP_EVENT_C | VARCHAR (66) |  |
| OUT_PHASEII_EVENT_C | VARCHAR (66) |  |
| SUB_PRSRV_INV_LO_YN | VARCHAR (1) |  |
| HOL_SCHED_WARN_C | INTEGER |  |
| IS_SYSTEM_DEFS_YN | No | Indicates whether the location record is the system definitions record. |
| RELEASE_TIME | DATETIME (Local) | The time of day in which block release settings using the day interval will release. |
| TR_SKIP_HOL_YN | VARCHAR (1) |  |
| DISABLE_NEW_HIER_YN | VARCHAR (1) |  |
| LOCATION_CLASSIFICATION_C | INTEGER |  |
| OUT_ROOM_TRACKING_EVENT_C | VARCHAR (66) |  |
| ORINVMGMT_GOLIVE_DATE | DATETIME | The date that the facility, or schedulable procedural location, will go live with the Procedural Supply Management module. |
| ORINVMGMT_LOC_YN | VARCHAR (1) | Surrogate key used to uniquely identify rows in this (and only this) table on Cogito Cloud only, do not assume the surrogate key in this table will correspond to the surrogate key in another table |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | LOC_ID | ANALYTICS_SYSTEM_SETTINGS | FACILITY_ID | No | No | No |  |
| 1 | LOC_ID | ARPB_SA_SETTINGS | FACILITY_ID | No | No | No |  |
| 1 | LOC_ID | CLARITY_LOC | LOC_ID | Unknown | No | No |  |
| 1 | LOC_ID | CLARITY_LOC_2 | LOC_ID | Unknown | No | No |  |
| 1 | LOC_ID | CLARITY_POS | POS_ID | No | No | No |  |
| 1 | LOC_ID | CLARITY_POS_2 | POS_ID | No | No | No |  |
| 1 | LOC_ID | CLARITY_SA | SERV_AREA_ID | Unknown | No | No |  |
| 1 | LOC_ID | CL_LOC_HIERARCHY | LOC_ID | Unknown | No | No |  |
| 1 | LOC_ID | CV_PCI_D2B_SETTINGS | FACILITY_ID | No | No | No |  |
| 1 | LOC_ID | EAF_CLM_ALTADR_INF | FACILITY_ID | No | No | No |  |
| 1 | LOC_ID | EAF_CLM_RMT_SETUP | FACILITY_ID | No | No | No |  |
| 1 | LOC_ID | EAF_EXP_APPT_LOG | FACILITY_ID | No | No | No |  |
| 1 | LOC_ID | EAF_SEARCH_TERMS | FACILITY_ID | No | No | No |  |
| 1 | LOC_ID | ESCALATION_THRESH_SGL | FACILITY_ID | No | No | No |  |
| 1 | LOC_ID | FAC_CONNECT | FACILITY_ID | No | No | No |  |
| 1 | LOC_ID | FAC_DIRECT_ADDR | FACILITY_ID | Unknown | No | No |  |
| 1 | LOC_ID | HH_FAC_INFO | FACILITY_ID | No | No | No |  |
| 1 | LOC_ID | MC_FACILITY_GL_SEGMENTS | FACILITY_ID | No | No | No |  |
| 1 | LOC_ID | MYC_INFO | FACILITY_ID | No | No | No |  |
| 1 | LOC_ID | PDMD_FILE_CONFIG | FACILITY_ID | No | No | No |  |
| 1 | LOC_ID | RX_LOC | LOC_ID | Unknown | No | No |  |
| 1 | LOC_ID | SD_FILTER_CONFIG_SETTING | FACILITY_ID | Yes | No | No |  |
| 1 | LOC_ID | SERVICE_PROV | FACILITY_ID | No | No | No |  |
| 1 | LOC_ID | SMS_SETTINGS_SNGL | FACILITY_ID | No | No | No |  |
| 1 | LOC_ID | SYS_RSH_RPT_GRP_OVRIDE | FACILITY_ID | No | No | No |  |
| 1 | LOC_ID | V_CMS_MU_LOC | LOC_ID | Unknown | Unknown | No |  |
| 1 | LOC_ID | V_CUBE_D_LOCATION | LOCATION_ID | Unknown | Unknown | No |  |
| 1 | LOC_ID | V_CUBE_D_SERVICE_AREA | SERVICE_AREA_ID | Unknown | Unknown | No |  |
| 1 | LOC_ID | V_OR_LOC_STRUCTURE | OR_LOC_ID | Unknown | Unknown | No |  |
| 2 | DEP_ID | BH_DEP | DEPARTMENT_ID | No | No | No |  |

_(89 total; showing first 30)_
