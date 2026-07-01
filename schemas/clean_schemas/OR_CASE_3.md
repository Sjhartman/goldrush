# OR_CASE_3

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=OR_CASE_3

## Description

The OR_CASE_3 table enables you to report on surgical and procedural case data. This table has the same basic structure as OR_CASE and OR_CASE_2, but was created as a second table to prevent OR_CASE and OR_CASE_2 from getting any larger.

**Overflow table** for OR_CASE (134 cols). Contains additional columns for the same records — join on the shared primary key column.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | ORC |
| Release Version | Rel May 2024 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| CASE_ID | VARCHAR (18) | The unique identifier (.1 item) for the case request record. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| SETUP_TIME_MOD_YN | VARCHAR (1) |  |
| DFLT_SETUP_MINS | INTEGER | This item stores the setup time defaulted by the system. |
| DFLT_CLEANUP_MINS | INTEGER | This item stores the clean up time defaulted by the system. |
| DFLT_PREP_MINS | INTEGER | This item stores the patient prep time defaulted by the system. |
| DFLT_WRAPUP_MINS | INTEGER | This item stores the wrap-up time defaulted by the system. |
| CLEANUP_TIME_MOD_YN | VARCHAR (1) |  |
| WRAPUP_TIME_MOD_YN | VARCHAR (1) |  |
| CASE_LEN_MOD_YN | VARCHAR (1) |  |
| LEN_MOD_USER_ID | VARCHAR (18) | This item tracks the last user to modify a length of a procedure or panel such that a length doesn't use the defaulted length. |
| PAN1_PAN_DLFT_SNG_TYP_C | INTEGER |  |
| PAN1_PAN_DLFT_MLT_TYP_C | INTEGER |  |
| PAN1_PAN_DLFT_PAN_TYP_C | INTEGER |  |
| PAN2_PAN_DLFT_SNG_TYP_C | INTEGER |  |
| PAN2_PAN_DLFT_MLT_TYP_C | INTEGER |  |
| PAN2_PAN_DLFT_PAN_TYP_C | INTEGER |  |
| PAN3_PAN_DLFT_SNG_TYP_C | INTEGER |  |
| PAN3_PAN_DLFT_MLT_TYP_C | INTEGER |  |
| PAN3_PAN_DLFT_PAN_TYP_C | INTEGER |  |
| PAN4_PAN_DLFT_SNG_TYP_C | INTEGER |  |
| PAN4_PAN_DLFT_MLT_TYP_C | INTEGER |  |
| PAN4_PAN_DLFT_PAN_TYP_C | INTEGER |  |
| PAN5_PAN_DLFT_SNG_TYP_C | INTEGER |  |
| PAN5_PAN_DLFT_MLT_TYP_C | INTEGER |  |
| PAN5_PAN_DLFT_PAN_TYP_C | INTEGER |  |
| PAN1_REQ_PROC_MINS | INTEGER | This item holds the requested total number of minutes for all the procedures in a panel. |
| PAN2_REQ_PROC_MINS | INTEGER | This item holds the requested total number of minutes for all the procedures in a panel. |
| PAN3_REQ_PROC_MINS | INTEGER | This item holds the requested total number of minutes for all the procedures in a panel. |
| PAN4_REQ_PROC_MINS | INTEGER | This item holds the requested total number of minutes for all the procedures in a panel. |
| PAN5_REQ_PROC_MINS | INTEGER | This item holds the requested total number of minutes for all the procedures in a panel. |
| PAN1_REQ_PROC_CMTS | VARCHAR (500) | This item holds the comments regarding the requested total procedure length in minutes. |
| PAN2_REQ_PROC_CMTS | VARCHAR (500) | This item holds the comments regarding the requested total procedure length in minutes. |
| PAN3_REQ_PROC_CMTS | VARCHAR (500) | This item holds the comments regarding the requested total procedure length in minutes. |
| PAN4_REQ_PROC_CMTS | VARCHAR (500) | This item holds the comments regarding the requested total procedure length in minutes. |
| PAN5_REQ_PROC_CMTS | VARCHAR (500) | This item holds the comments regarding the requested total procedure length in minutes. |
| PAN1_REQ_PROC_ACT_C | INTEGER |  |
| PAN2_REQ_PROC_ACT_C | INTEGER |  |
| PAN3_REQ_PROC_ACT_C | INTEGER |  |
| PAN4_REQ_PROC_ACT_C | INTEGER |  |
| PAN5_REQ_PROC_ACT_C | INTEGER |  |
| PAN1_PANEL_CONFIDENCE_C | INTEGER |  |
| PAN2_PANEL_CONFIDENCE_C | INTEGER |  |
| PAN3_PANEL_CONFIDENCE_C | INTEGER |  |
| PAN4_PANEL_CONFIDENCE_C | INTEGER |  |
| PAN5_PANEL_CONFIDENCE_C | INTEGER |  |
| PAT_CONF_CASE_YN | VARCHAR (1) |  |
| CASE_CONF_UTC_DTTM | DATETIME (UTC) | The most recent instant of a patient's case confirmation. Part of the patient case confirmation workflow. Updated each time the patient confirms and reset to null when case is rescheduled to different date or OR location. |
| CASE_CONF_PAT_ID | VARCHAR (18) | The patient ID of the patient if they texted to confirm their own case. |
| CONF_PAT_RELATIONSHIP_ID | NUMERIC (18,0) | The Guardian (RLA networked ID) that confirmed the patient's case through text. |
| CASE_CONF_USER_ID | VARCHAR (18) | The employee ID (EMP networked) that confirmed the patient's case. |
| PAN1_TOTAL_PROC_MIN | INTEGER | The total number of minutes required for all of the procedures on this panel. |
| PAN1_DFLT_PROC_MINS | INTEGER | The total number of minutes required for all of the procedures on this panel as calculated by the system using procedure length estimates, preference cards, and procedure records. |
| PAN1_PROC_MIN_MOD_YN | VARCHAR (1) |  |
| PAN1_PROC_START | INTEGER | The time at which this panel's procedures should begin. This is measured in minutes relative to the beginning of the case. |
| PAN1_PRC_STRT_MOD_YN | VARCHAR (1) |  |
| PAN1_REQ_MINS_USER_ID | VARCHAR (18) | The id of the user who requested a total procedure length for this panel in minutes. |
| PAN2_TOTAL_PROC_MIN | INTEGER | The total number of minutes required for all of the procedures on this panel. |
| PAN2_DFLT_PROC_MINS | INTEGER | The total number of minutes required for all of the procedures on this panel as calculated by the system using procedure length estimates, preference cards, and procedure records. |
| PAN2_PROC_MIN_MOD_YN | VARCHAR (1) |  |
| PAN2_PROC_START | INTEGER | The time at which this panel's procedures should begin. This is measured in minutes relative to the beginning of the case. |
| PAN2_PRC_STRT_MOD_YN | VARCHAR (1) |  |
| PAN2_REQ_MINS_USER_ID | VARCHAR (18) | The id of the user who requested a total procedure length for this panel in minutes. |
| PAN3_TOTAL_PROC_MIN | INTEGER | The total number of minutes required for all of the procedures on this panel. |
| PAN3_DFLT_PROC_MINS | INTEGER | The total number of minutes required for all of the procedures on this panel as calculated by the system using procedure length estimates, preference cards, and procedure records. |
| PAN3_PROC_MIN_MOD_YN | VARCHAR (1) |  |
| PAN3_PROC_START | INTEGER | The time at which this panel's procedures should begin. This is measured in minutes relative to the beginning of the case. |
| PAN3_PRC_STRT_MOD_YN | VARCHAR (1) |  |
| PAN3_REQ_MINS_USER_ID | VARCHAR (18) | The id of the user who requested a total procedure length for this panel in minutes. |
| PAN4_TOTAL_PROC_MIN | INTEGER | The total number of minutes required for all of the procedures on this panel. |
| PAN4_DFLT_PROC_MINS | INTEGER | The total number of minutes required for all of the procedures on this panel as calculated by the system using procedure length estimates, preference cards, and procedure records. |
| PAN4_PROC_MIN_MOD_YN | VARCHAR (1) |  |
| PAN4_PROC_START | INTEGER | The time at which this panel's procedures should begin. This is measured in minutes relative to the beginning of the case. |
| PAN4_PRC_STRT_MOD_YN | VARCHAR (1) |  |
| PAN4_REQ_MINS_USER_ID | VARCHAR (18) | The id of the user who requested a total procedure length for this panel in minutes. |
| PAN5_TOTAL_PROC_MIN | INTEGER | The total number of minutes required for all of the procedures on this panel. |
| PAN5_DFLT_PROC_MINS | INTEGER | The total number of minutes required for all of the procedures on this panel as calculated by the system using procedure length estimates, preference cards, and procedure records. |
| PAN5_PROC_MIN_MOD_YN | VARCHAR (1) |  |
| PAN5_PROC_START | INTEGER | The time at which this panel's procedures should begin. This is measured in minutes relative to the beginning of the case. |
| PAN5_PRC_STRT_MOD_YN | VARCHAR (1) |  |
| PAN5_REQ_MINS_USER_ID | VARCHAR (18) | The id of the user who requested a total procedure length for this panel in minutes. |
| EMERG_APPROVAL_INST_UTC_DTTM | DATETIME (UTC) | This item stores an instant intended to be used to record the time at which an emergency case has been approved to be scheduled. |
| CASE_CONF_MYPT_ID | VARCHAR (18) | The MyChart user (WPR networked ID) that confirmed the patient's case through text. |
| DATE_IS_SUGGESTED_YN | VARCHAR (1) |  |
| CLINICAL_PRIORITY_C | INTEGER |  |
| INSTR_PICKING_STATUS_C | INTEGER |  |
| CS_CASE_ELIGIBLE_YN | VARCHAR (1) |  |
| CS_CASE_OPT_OUT_YN | VARCHAR (1) |  |
| CS_CASE_DAYS_SOONER | INTEGER | The number of days sooner a case is scheduled after being suggested. |
| START_AT_OR_AFTER_OVERRIDE_TM | DATETIME (Local) | Case should be scheduled on or after this time. |
| START_AT_OR_BEFORE_OVERRIDE_TM | DATETIME (Local) | Case should be scheduled on or after this time. |
| SCHEDULING_REVIEWED_YN | VARCHAR (1) |  |
| SCHEDULE_SOURCE_MKTPL_YN | VARCHAR (1) |  |
| HAS_SAME_ORD_PROC_YN | VARCHAR (1) |  |
| PROC_BUTTON_SHOWN_YN | VARCHAR (1) |  |
| PROC_BUTTON_USED_YN | VARCHAR (1) |  |
| HIDE_PAT_PRC_INSTR_YN | VARCHAR (1) |  |
| AUTH_PROV_ADDR | VARCHAR (120) | Stores the address ID for the authorizing provider for the case. |
| PAT_REQUEST_CANCEL_YN | VARCHAR (1) |  |
| CASE_REQUEST_CANCEL_UTC_DTTM | DATETIME (UTC) | The most recent instant of a patient's request to cancel a case. Part of the patient case confirmation workflow. Updated each time the patient confirms and reset to null when the case is rescheduled to different date or OR location. |
| CASE_REQUEST_CANCEL_PAT_ID | VARCHAR (18) | The patient who requested to cancel the case. |
| REQ_CANCEL_PAT_RELATIONSHIP_ID | NUMERIC (18,0) | The guardian who requested to cancel the case. |
| CS_CASE_PDS_ELIGIBLE_YN | VARCHAR (1) |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | CASE_ID | OR_CASE | OR_CASE_ID | Unknown | No | No |  |
| 1 | CASE_ID | OR_CASE_2 | CASE_ID | Unknown | No | No |  |
| 1 | CASE_ID | OR_CASE_4 | OR_CASE_ID | No | No | No |  |
| 1 | CASE_ID | OR_CASE_VIRTUAL | OR_CASE_ID | No | No | No |  |
| 1 | CASE_ID | V_OR_CASE_ORR | CASE_ID | Unknown | Unknown | No |  |
| 2 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 2 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 2 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 3 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 12 | LEN_MOD_USER_ID | CLARITY_EMP | USER_ID | Unknown | No | No |  |
| 12 | LEN_MOD_USER_ID | CLARITY_EMP_2 | USER_ID | Unknown | No | No |  |
| 12 | LEN_MOD_USER_ID | CLARITY_EMP_3 | USER_ID | Unknown | No | No |  |
| 12 | LEN_MOD_USER_ID | CLARITY_EMP_4 | USER_ID | No | No | No |  |
| 12 | LEN_MOD_USER_ID | CLARITY_EMP_DEMO | USER_ID | No | No | No |  |
| 12 | LEN_MOD_USER_ID | EMP_BASIC_INFO | USER_ID | No | No | No |  |
| 12 | LEN_MOD_USER_ID | EMP_DOC_SETTINGS | USER_NUMBER_ID | No | No | No |  |
| 12 | LEN_MOD_USER_ID | F_RX_USER | USER_ID | Unknown | Unknown | No |  |
| 12 | LEN_MOD_USER_ID | IB_MESSAGE_SETTINGS | USER_ID | No | No | No |  |
| 12 | LEN_MOD_USER_ID | LOGIN_INFO | USER_NUMBER_ID | No | No | No |  |
| 12 | LEN_MOD_USER_ID | QC_RESULTS_REVIEW | USER_NUMBER_ID | No | No | No |  |
| 12 | LEN_MOD_USER_ID | USER_SIDEBAR_RPT | USER_NUMBER_ID | Unknown | No | No |  |
| 12 | LEN_MOD_USER_ID | V_CUBE_D_USER | USER_ID | Unknown | Unknown | No |  |
| 12 | LEN_MOD_USER_ID | V_CUBE_RX_USER | USER_ID | Unknown | Unknown | No |  |
| 13 | PAN1_PAN_DLFT_SNG_TYP_C | ZC_PAN_DLFT_SNG_TYP | PAN_DLFT_SNG_TYP_C | No | No | No |  |
| 14 | PAN1_PAN_DLFT_MLT_TYP_C | ZC_PAN_DLFT_MLT_TYP | PAN_DLFT_MLT_TYP_C | No | No | No |  |
| 15 | PAN1_PAN_DLFT_PAN_TYP_C | ZC_PAN_DLFT_PAN_TYP | PAN_DLFT_PAN_TYP_C | No | No | No |  |
| 16 | PAN2_PAN_DLFT_SNG_TYP_C | ZC_PAN_DLFT_SNG_TYP | PAN_DLFT_SNG_TYP_C | No | No | No |  |
| 17 | PAN2_PAN_DLFT_MLT_TYP_C | ZC_PAN_DLFT_MLT_TYP | PAN_DLFT_MLT_TYP_C | No | No | No |  |

_(207 total; showing first 30)_
