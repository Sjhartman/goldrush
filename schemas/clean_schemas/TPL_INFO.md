# TPL_INFO

**COLUMN NAME CORRECTIONS -- use these exact names, no others:**
- `display_name` -- NOT plan_display_name, NOT treatment_plan_display_name
- `eff_end_date` -- NOT plan_eff_end_date
- `plan_status_c` -- decoded via JOIN to ZC_PLAN_STATUS on plan_status_c; alias decoded value as plan_status_name
- `dc_reason_c` -- decoded via JOIN to ZC_DC_REASON on dc_reason_c; alias decoded value as dc_reason_name
- `trt_goal_c` -- decoded via JOIN to ZC_TRT_GOAL on trt_goal_c; alias decoded value as trt_goal_name
- `line_of_treatment_c` -- no ZC_ decode table available; expose code directly

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=TPL_INFO

## Description

This table contains basic information about a treatment plan or a pathway, such as the plan/pathway name, the user who created the plan/pathway, when it was created, which protocol it was created from, the starting cycle number or step, etc.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | TPL |
| Release Version | SPRING 2008 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| TREATMENT_PLAN_ID | NUMERIC (18,0) | The treatment plan ID. |
| CM_PHY_OWNER_ID | VARCHAR (25) | ID of the physical deployment owner for this row.  Physical owners will be where the data is hosted, either on the cross-over server or the owner deployment. |
| CM_LOG_OWNER_ID | VARCHAR (25) | ID of the logical deployment owner for this row.  Logical owners show the deployment where the row was created but doesn't represent if the row is a part of version skew. |
| TREATMENT_PLAN_NAME | VARCHAR (200) | The name of the treatment plan in this row. |
| PLAN_STATUS_C | INTEGER |  |
| PLAN_REC_TYP_C | INTEGER |  |
| PLAN_START_DATE | DATETIME | The start date in external format of the treatment plan in this row.  For treatment plans this is the date of the first cycle within the plan. |
| ZERO_BASED_YN | VARCHAR (1) |  |
| PROTOCOL_ID | NUMERIC (18,0) | The ID of the protocol that generated the treatment plan in this row. |
| PROTOCOL_DAT | VARCHAR (50) | The contact date (DAT) of the protocol that generated the treatment plan in this row. |
| CREATED_USER_ID | VARCHAR (18) | The user ID of the person who created the treatment plan in this row. |
| CREATED_ON_TM | DATETIME (Attached) | The date/time in external format that the treatment plan in this row was created. |
| PLAN_VERIF_DATE_TM | DATETIME (Local) | The date/time in external format when the treatment plan in this row was last verified. |
| PLAN_VERIF_USER_ID | VARCHAR (18) | The user ID of the person who last verified the treatment plan in this row. |
| DC_REASON_C | VARCHAR (66) |  |
| DISPLAY_NAME | VARCHAR (500) | The treatment plan display name entered by the user. |
| FIRST_CYCLE_NUM | INTEGER | The cycle number of the first cycle in the treatment plan. |
| START_CYCLE_NUM | INTEGER | The cycle number of the cycle marked as the 'start cycle' in the treatment plan. |
| PAT_ID | VARCHAR (18) | The unique ID of the patient who is associated with this treatment plan or pathway. |
| PATHWAY_DISC_RESN_C | INTEGER |  |
| REV_TYPE_C | INTEGER |  |
| REV_NEXT_DUE | VARCHAR (64) | The contact date (DAT) or treatment number when review reminders begin to display to users. |
| REV_EXPIRES | VARCHAR (64) | The contact date (DAT) or treatment number after which this plan will be considered unreviewed. |
| TRT_GOAL_C | INTEGER |  |
| TPL_PROVIDER_ID | VARCHAR (18) | The provider who is managing this treatment plan. |
| PLAN_VERSION | INTEGER | Stores the lowest Version in which the plan was edited. This data is used to determine what features will be enabled for the plan. |
| REFERRAL_ID | NUMERIC (18,0) | Stores the ID of a referral which is used for prior authorization. |
| WAS_PATH_SUGGSTD_YN | VARCHAR (1) |  |
| PATH_SUG_ALT_CSN_ID | NUMERIC (18,0) | The unique contact serial number for the alert contact that corresponds to the advisory that suggested the pathway. This number is unique across all alert contacts in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). This column is only populated for pathways that were suggested by advisories; other rows have a value of null. |
| DEVIATION_USER_ID | VARCHAR (18) | The user who signed off on the treatment plan deviation |
| DEVIATION_DTTM | DATETIME (UTC) | The instant when the treatment plan was given a signoff for deviation |
| DEVIATION_REASON_C | INTEGER |  |
| DEVIATION_COMMENT | VARCHAR (4000) | The comment to give more information about the deviation reason.  This only extracts the first 4000 characters. |
| LAST_DEVIATION_DTTM | DATETIME (UTC) | Stores the instant when the plan last deviated from the protocol |
| DEVIATION_REQUESTOR_ID | VARCHAR (18) | Stores the user who marked the plan as needing approval for deviation |
| NEXT_PLANNED_DATE | DATETIME | Next planned treatment date for a plan. |
| INFUSION_DEPT_ID | NUMERIC (18,0) | Stores the treatment department. |
| PROTOCOL_CONTACT_DATE_REAL | FLOAT | The contact date real of the protocol that generated the treatment plan in this row.  The contact date real is a unique, internal contact date in decimal format. The integer portion of the number indicates the date of the contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| HOLD_INSTANT_UTC_DTTM | DATETIME (UTC) | The UTC instant when this plan was put on hold, if it is on hold. |
| HOLD_USER_ID | VARCHAR (18) | The user who put this plan on hold, if it is on hold. |
| HOLD_REASON_C | INTEGER |  |
| HOLD_COMMENT | VARCHAR (254) | The comment entered when this plan was put on hold. |
| PROGRAM_NUMBER | INTEGER | This item contains the program number for a treatment plan |
| REGIMEN_NUMBER | INTEGER | This item contains the regimen number for a treatment plan |
| LINE_OF_TREATMENT_C | INTEGER |  |
| PROTOCOL_SUGGESTION_SOURCE_C | INTEGER |  |
| PROTOCOL_LINK_CSN | NUMERIC (18,0) | For a treatment plan created from a linked protocol (PTP) record, this column stores the contact serial number (CSN) of the PTP contact linking the clinical protocol contact to a billing protocol contact. |
| CREATION_STATE_C | INTEGER |  |
| STUDY_CURRENT_VERSION_IDENT | VARCHAR (100) | The current study version identifier of the treatment plan. |
| PRIOR_AUTH_PRIMARY_COVERAGE_ID | NUMERIC (18,0) | This item stores the primary coverage ID that is used to generate the Referral in the treatment or therapy plan. |
| BMT_AMEND_USER_ID | VARCHAR (18) | the user who amended the plan which resulted in the creation of a new treatment plan. |
| BMT_PLAN_AMEND_INST_DTTM | DATETIME (UTC) | The instant that the plan was amended. |
| REFERRAL_STATUS_CHNG_UTC_DTTM | DATETIME (UTC) | This item stores the most recent instant when the treatment plan referral status changed due to changes made to the treatment plan. |
| DISCON_COMMENT | VARCHAR (100) | It stores the discontinue comments entered by the user. |
| DISCON_INSTANT_UTC_DTTM | DATETIME (UTC) | This item stores the discontinue plan instant. |
| DISCON_PLAN_USER_ID | VARCHAR (18) | This item store the user who discontinued the plan. |
| LAST_USER_ACTION_UTC_DTTM | DATETIME (UTC) | Stores the last instant that a user interacted directly with the plan. This item will not be updated when the plan is updated by an action outside the plan or by a background process. |
| RECONCILIATION_EVENT_ID | VARCHAR (18) | This item contains the ID of the event used to track reconciliation actions for this plan |
| NEEDS_RECONCILIATION_YN | VARCHAR (1) |  |
| NEXT_UNAUTH_TREATMENT_DAY_ID | NUMERIC (18,0) | This item stores the treatment day ID of the next unauthorized day in the treatment plan. |
| INSTANT_OF_UPDATE_DTTM | DATETIME (Local) | Instant when record was updated |
| RECORD_STATUS_C | INTEGER |  |
| IS_PLAN_DELETED_YN | 10120 |  |
| PATH_PRIM_HSP_PAT_ENC_CSN_ID | NUMERIC (18,0) | The primary hospital encounter for a pathway-type treatment plan. Hospital outpatient visits are excluded. If multiple encounters are linked to steps on the pathway, the first non-HOV hospital encounter is used. |
| FUTURE_PLAN_DATES_FIXED_YN | VARCHAR (1) |  |
| AUTO_DISCONTINUE_ENABLE_YN | VARCHAR (1) |  |
| AUTO_DISCONTINUE_INACTIVE_DATE | DATETIME | The date at which this plan is considered inactive for the purposes of automatic discontinuation. |
| FLEXIBLE_START_DATE_PRIORITY_C | INTEGER |  |
| FLEXIBLE_START_DATE_TOL_DAYS | INTEGER | This item stores the tolerance (in days) associated with the priority in I TPL 55 at the time of that item being set that a plan utilizing flexible start dates should be scheduled within. |
| FLEX_START_DT_ORDER_PRIORITY_C | INTEGER |  |
| TREATMENT_START_DATE | DATETIME | The date of the first treatment cycle in a treatment plan. |
| REFERRING_PROV_ID | VARCHAR (18) | Referring provider for the plan. |
| AUTO_DC_NO_REMAIN_TREAT_DATE | DATETIME | The date when the plan will automatically be discontinued due to running out of treatments. |
| EFF_END_DATE | DATETIME | The effective end date for a treatment plan. If a plan is still active this will be the date the last cycle ends and if it is discontinued it will be the date of the last started treatment day. |
| MED_ACCESS_REFERRAL_ID | NUMERIC (18,0) | Stores the ID of the current Medication Access referral. |
| PLAN_NOTE_ID | VARCHAR (254) | The unique ID of the note record that contains the notes for a treatment or therapy plan. |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | TREATMENT_PLAN_ID | DENT_TREATMENT | TREATMENT_ID | No | No | No |  |
| 1 | TREATMENT_PLAN_ID | TPL_HSB_EPT_LINK | TREATMENT_PLAN_ID | Unknown | No | No |  |
| 2 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 2 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 2 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 3 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 5 | PLAN_STATUS_C | ZC_PLAN_STATUS | PLAN_STATUS_C | No | No | No |  |
| 6 | PLAN_REC_TYP_C | ZC_PLAN_REC_TYP | PLAN_REC_TYP_C | No | No | No |  |
| 9 | PROTOCOL_ID | CL_PRL_SS | PROTOCOL_ID | No | No | No |  |
| 11 | CREATED_USER_ID | CLARITY_EMP | USER_ID | Unknown | No | No |  |
| 11 | CREATED_USER_ID | CLARITY_EMP_2 | USER_ID | Unknown | No | No |  |
| 11 | CREATED_USER_ID | CLARITY_EMP_3 | USER_ID | Unknown | No | No |  |
| 11 | CREATED_USER_ID | CLARITY_EMP_4 | USER_ID | No | No | No |  |
| 11 | CREATED_USER_ID | CLARITY_EMP_DEMO | USER_ID | No | No | No |  |
| 11 | CREATED_USER_ID | EMP_BASIC_INFO | USER_ID | No | No | No |  |
| 11 | CREATED_USER_ID | EMP_DOC_SETTINGS | USER_NUMBER_ID | No | No | No |  |
| 11 | CREATED_USER_ID | F_RX_USER | USER_ID | Unknown | Unknown | No |  |
| 11 | CREATED_USER_ID | IB_MESSAGE_SETTINGS | USER_ID | No | No | No |  |
| 11 | CREATED_USER_ID | LOGIN_INFO | USER_NUMBER_ID | No | No | No |  |
| 11 | CREATED_USER_ID | QC_RESULTS_REVIEW | USER_NUMBER_ID | No | No | No |  |
| 11 | CREATED_USER_ID | USER_SIDEBAR_RPT | USER_NUMBER_ID | Unknown | No | No |  |
| 11 | CREATED_USER_ID | V_CUBE_D_USER | USER_ID | Unknown | Unknown | No |  |
| 11 | CREATED_USER_ID | V_CUBE_RX_USER | USER_ID | Unknown | Unknown | No |  |
| 14 | PLAN_VERIF_USER_ID | CLARITY_EMP | USER_ID | Unknown | No | No |  |
| 14 | PLAN_VERIF_USER_ID | CLARITY_EMP_2 | USER_ID | Unknown | No | No |  |
| 14 | PLAN_VERIF_USER_ID | CLARITY_EMP_3 | USER_ID | Unknown | No | No |  |
| 14 | PLAN_VERIF_USER_ID | CLARITY_EMP_4 | USER_ID | No | No | No |  |
| 14 | PLAN_VERIF_USER_ID | CLARITY_EMP_DEMO | USER_ID | No | No | No |  |

_(403 total; showing first 30)_
