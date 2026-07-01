# EPISODE_DEF

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=EPISODE_DEF

## Description

This table contains information about Episode Definition records.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | HBD |
| Release Version | Rel 2014 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| EPISODE_DEF_ID | NUMERIC (18,0) | The unique identifier for the block type record. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| EPISODE_TYPE_C | INTEGER |  |
| BASE_PWY_PER_TYPE_C | INTEGER |  |
| PWY_PER_TYPE_NAME | VARCHAR (128) | This column displays the name of the administrative pathway period type. |
| RTT_STATUS_MAP_ID | NUMERIC (18,0) | This column displays the source administrative pathway period definition record (HBD) whose mapping table is to be used for this definition record. |
| EPISODE_DEF_NAME | VARCHAR (254) | This column displays the name of the episode / block definition record. |
| DFLT_TARGET_SET_ID | VARCHAR (18) | Default set of targets to add to administrative pathway period (HSB) record when creating one with a type of this HBD. |
| MEASUREMENT_TYPE_C | INTEGER |  |
| REQ_DOSE_MODIFICATION_RSN_YN | VARCHAR (1) |  |
| DEFAULT_PROPAGATION_TARGET_C | INTEGER |  |
| PROC_SAME_CAT_PROPAGATE_YN | VARCHAR (1) |  |
| AUTO_SELECT_RELATED_DAYS_YN | VARCHAR (1) |  |
| MAX_DEFER_DAYS_WITHOUT_UNSIGN | INTEGER | Specifies the number of days a treatment day can be deferred without requiring re-signing in a treatment plan of this episode type. |
| SUPPRESS_KEEP_SIGNED_OPTION_YN | VARCHAR (1) |  |
| UNSIGN_PLAN_ON_MAX_DEFERRAL_YN | VARCHAR (1) |  |
| PACKAGE_START_PX_ID | NUMERIC (18,0) | Administrative package code used when the admin pathway is created. |
| PLAN_HOLD_REASON_REQ_C | INTEGER |  |
| PLAN_HOLD_COMMENT_REQ_C | INTEGER |  |
| PLAN_HOLD_RELEASE_REASON_REQ_C | INTEGER |  |
| PLAN_HOLD_RELEASE_CMT_REQ_C | INTEGER |  |
| PLAN_HOLD_ACTION_ON_MED_C | INTEGER |  |
| PLAN_SCHEDULING_WINDOW_COUNT | INTEGER | Stores the numeric amount for the scheduling window. |
| PLAN_SCHEDULING_WINDOW_UNIT_C | INTEGER |  |
| PAS_PWY_TYPE_C | INTEGER |  |
| ELEMENT_LABEL_C | INTEGER |  |
| CCM_EPISODE_TYPE_C | INTEGER |  |
| USE_EXP_DATE_FOR_NEXT_DUE_YN | VARCHAR (1) |  |
| REQ_DT_MATCH_TO_RELINK_APPT_YN | VARCHAR (1) |  |
| NON_REPORTABLE_YN | VARCHAR (1) |  |
| RFL_BEFORE_PLAN_ACTIVATION_YN | VARCHAR (1) |  |
| THP_CRT_NEW_ORD_REORD_COMP_YN | VARCHAR (1) |  |
| AUTO_DC_ENABLE_YN | VARCHAR (1) |  |
| AUTO_DC_INACTIVITY_THRESHOLD | INTEGER | The number of days of inactivity that must elapse before plans of this episode type are considered inactive. |
| RFL_ALWAYS_CREATE_YN | VARCHAR (1) |  |
| PWY_REPORTING_TYPE_C | INTEGER |  |
| TRIGGER_ADJUST_DUE_TIMES_YN | VARCHAR (1) |  |
| ALLOW_AUTO_DC_NO_REMAIN_TRT_YN | VARCHAR (1) |  |
| HBD_OUTREACH_ATMPT_REQ_NUM | INTEGER | Contains the number of Outreach Attempts required for tasks (LTKs) attached to episodes of this type to display quickbuttons in Start Outreach.  ? This item will be used by a task if I LTR 26400 is left blank. |
| HBD_CNT_OUTREACH_FROM_C | INTEGER |  |
| HBD_CNT_OUTREACH_BY_C | INTEGER |  |
| WAL_USE_HSB_START_YN | VARCHAR (1) |  |
| EPISODE_PROG_CAT_C | INTEGER |  |
| ALLOW_STUDY_PROTOCOLS_YN | VARCHAR (1) |  |
| MAX_DAYS_MULTIDAY_INTERVAL | INTEGER | The maximum number of days between treatments in the multi-day interval for therapy plan orders. |
| ALLOW_SIGN_CYCLES_YN | VARCHAR (1) |  |
| CAN_USE_FLEX_START_DT_C | INTEGER |  |
| ALLOW_CUSTOM_FREQUENCY_C | INTEGER |  |
| THP_ALLOW_RLS_ORD_NON_TREAT_YN | VARCHAR (1) | Surrogate key used to uniquely identify rows in this (and only this) table on Cogito Cloud only, do not assume the surrogate key in this table will correspond to the surrogate key in another table |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 2 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 2 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 3 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 4 | EPISODE_TYPE_C | ZC_HOME_CARE_TYPE | HOME_CARE_TYPE_C | No | No | No |  |
| 5 | BASE_PWY_PER_TYPE_C | ZC_BASE_PWY_PER_TYPE | BASE_PWY_PER_TYPE_C | No | No | No |  |
| 7 | RTT_STATUS_MAP_ID | EPISODE_DEF | EPISODE_DEF_ID | No | No | No |  |
| 9 | DFLT_TARGET_SET_ID | TASK_INFO | RECORD_ID | No | No | No |  |
| 10 | MEASUREMENT_TYPE_C | ZC_MEASUREMENT_TYPE | MEASUREMENT_TYPE_C | No | No | No |  |
| 12 | DEFAULT_PROPAGATION_TARGET_C | ZC_DFLT_PRPG_TGT | DFLT_PRPG_TGT_C | No | No | No |  |
| 18 | PACKAGE_START_PX_ID | CLARITY_EAP | PROC_ID | No | No | No |  |
| 18 | PACKAGE_START_PX_ID | CLARITY_EAP_2 | PROC_ID | No | No | No |  |
| 18 | PACKAGE_START_PX_ID | CLARITY_EAP_3 | PROC_ID | No | No | No |  |
| 18 | PACKAGE_START_PX_ID | CLARITY_EAP_4 | PROC_ID | No | No | No |  |
| 18 | PACKAGE_START_PX_ID | CLARITY_EAP_5 | PROC_ID | No | No | No |  |
| 18 | PACKAGE_START_PX_ID | CLARITY_EAP_IMM | PROC_ID | Unknown | No | No |  |
| 18 | PACKAGE_START_PX_ID | PROC_CONSENT_CONFIG | PROC_ID | No | No | No |  |
| 18 | PACKAGE_START_PX_ID | PROC_UM | PROC_ID | No | No | No |  |
| 18 | PACKAGE_START_PX_ID | V_CUBE_D_PROCEDURE | PROCEDURE_ID | Unknown | Unknown | No |  |
| 19 | PLAN_HOLD_REASON_REQ_C | ZC_QF_DATA_REQ | QF_DATA_REQ_C | No | No | No |  |
| 20 | PLAN_HOLD_COMMENT_REQ_C | ZC_QF_DATA_REQ | QF_DATA_REQ_C | No | No | No |  |
| 21 | PLAN_HOLD_RELEASE_REASON_REQ_C | ZC_QF_DATA_REQ | QF_DATA_REQ_C | No | No | No |  |
| 22 | PLAN_HOLD_RELEASE_CMT_REQ_C | ZC_QF_DATA_REQ | QF_DATA_REQ_C | No | No | No |  |
| 23 | PLAN_HOLD_ACTION_ON_MED_C | ZC_PLAN_HLD_ACTION_ON_MED | PLAN_HOLD_ACTION_ON_MED_C | No | No | No |  |
| 25 | PLAN_SCHEDULING_WINDOW_UNIT_C | ZC_PLAN_SCHEDULING_WINDOW | PLAN_SCHEDULING_WINDOW_C | No | No | No |  |
| 26 | PAS_PWY_TYPE_C | ZC_PAS_PWY_TYPE | PAS_PWY_TYPE_C | No | No | No |  |
| 27 | ELEMENT_LABEL_C | ZC_ELEMENT_LABEL | ELEMENT_LABEL_C | No | No | No |  |
| 28 | CCM_EPISODE_TYPE_C | ZC_CCM_EPISODE_TYPE | CCM_EPISODE_TYPE_C | No | No | No |  |

_(36 total; showing first 30)_
