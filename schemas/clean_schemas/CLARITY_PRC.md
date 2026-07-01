# CLARITY_PRC

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=CLARITY_PRC

## Description

The CLARITY_PRC table contains one record for each visit type, panel, agent, and visit type modifier in your system.

**Primary table** in this group (101 cols). Overflow siblings joined on shared key: CLARITY_PRC_2 (34 cols). Prefer this table for most queries.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | PRC |
| Release Version | EPIC 2000 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| PRC_ID | VARCHAR (18) | The unique ID of the visit type record. |
| PRC_NAME | VARCHAR (200) | The name of the visit type. |
| PRC_ABBR | VARCHAR (60) | The abbreviation of the visit type, for example, OV. |
| RECORD_TYPE *(deprecated)* | VARCHAR (30) |  |
| PROC_CAT *(deprecated)* | VARCHAR (60) |  |
| OVRD_BILL_NO_TYPE *(deprecated)* | VARCHAR (30) |  |
| CHART_PULL *(deprecated)* | VARCHAR (30) |  |
| XRAY_PULL *(deprecated)* | VARCHAR (30) |  |
| SAME_DAY_PULL *(deprecated)* | VARCHAR (30) |  |
| EXTERNAL_NAME | VARCHAR (200) | The visit type name on reports and letters sent to patients. |
| STATUS *(deprecated)* | VARCHAR (10) |  |
| DEFAULT_LENGTH | INTEGER | The default appointment length for this visit type in minutes. |
| DEFAULT_COPAY_CAT *(deprecated)* | VARCHAR (254) |  |
| IN_OUT_PAT *(deprecated)* | VARCHAR (10) |  |
| CPT_PROC_ID | NUMERIC (18,0) | The unique ID of the CPT? procedure code that is associated with the visit type. |
| BENEFIT_GROUP *(deprecated)* | VARCHAR (40) |  |
| ANC_PROC_LENGTH | INTEGER | The total time for which a patient would be scheduled for an appointment using this visit type, if using scheduling pools, in minutes. |
| DUPLICATE_WITHIN | INTEGER | The total time in seconds that must elapse before scheduling the visit type again without it being considered a duplicate.  The following should always be true:  DUPLICATE_WITHIN = 3600 * DUPLICATE_HOURS + 86400 * DUPLICATE_DAYS. |
| DUPLICATE_DAYS | INTEGER | The time in days which must elapse before scheduling the visit type again without it being considered a duplicate.  NOTE: This value is the days portion only of the total.  It must be added with the hours portion to be complete. |
| DUPLICATE_HOURS | INTEGER | The time in hours which must elapse before scheduling the visit type again without it being considered a duplicate.  NOTE: This value is the hours portion only of the total.  It must be added with the days portion to be complete. |
| AUTOSCHEDULE_ALGO *(deprecated)* | VARCHAR (10) |  |
| VISIT_GROUP_NUM *(deprecated)* | INTEGER |  |
| VISIT_GROUP *(deprecated)* | VARCHAR (50) |  |
| RPT_GRP_ONE | VARCHAR (80) | You can specify groupers for enterprise reporting, SQL, or report generator reporting. This is one of the free-text report groupers. |
| RPT_GRP_TWO | VARCHAR (80) | You can specify groupers for enterprise reporting, SQL, or report generator reporting. This is one of the free-text report groupers. |
| RPT_GRP_THREE | VARCHAR (80) | You can specify groupers for enterprise reporting, SQL, or report generator reporting. This is one of the free-text report groupers. |
| RPT_GRP_FOUR | VARCHAR (80) | You can specify groupers for enterprise reporting, SQL, or report generator reporting. This is one of the free-text report groupers. |
| RPT_GRP_FIVE | VARCHAR (80) | You can specify groupers for enterprise reporting, SQL, or report generator reporting. This is one of the free-text report groupers. |
| RPT_GRP_SIX_C | VARCHAR (66) |  |
| RPT_GRP_SEVEN_C | VARCHAR (66) |  |
| RPT_GRP_EIGHT_C | VARCHAR (66) |  |
| RPT_GRP_NINE_C | VARCHAR (66) |  |
| RPT_GRP_TEN_C | VARCHAR (66) |  |
| NUM_FLASH_CARDS | INTEGER | The number of flash cards to print for appointments made with this visit type. |
| NUM_CONTROL_SHEETS | INTEGER | The number of control sheets to print for appointments of this visit type. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| RPT_GRP_ELEVEN_C | VARCHAR (66) |  |
| RPT_GRP_TWELVE_C | VARCHAR (66) |  |
| RPT_GRP_THIRTEEN_C | VARCHAR (66) |  |
| RPT_GRP_FOURTEEN_C | VARCHAR (66) |  |
| RPT_GRP_FIFTEEN_C | VARCHAR (66) |  |
| RPT_GRP_SIXTEEN_C | VARCHAR (66) |  |
| RPT_GRP_SEVENTEEN_C | VARCHAR (66) |  |
| RPT_GRP_EIGHTEEN_C | VARCHAR (66) |  |
| RPT_GRP_NINETEEN_C | VARCHAR (66) |  |
| RPT_GRP_TWENTY_C | VARCHAR (66) |  |
| INTRP_TYPE_NEEDED_C | INTEGER |  |
| SAME_PROV_ALL_YN | VARCHAR (1) |  |
| USE_IP_INSTR_YN | VARCHAR (1) |  |
| USE_INSTR_OF_PRC_ID | VARCHAR (18) | If set, the instructions from the selected visit type will be used for this visit type. |
| IS_ADVANCED_YN | VARCHAR (1) |  |
| PREREQ_FROM_PRC_ID | VARCHAR (18) | Use prereq settings from another visit type |
| RECALL_FROM_PRC_ID | VARCHAR (18) | Use recall settings from another visit type |
| BLOCK_OVERRULE_C | INTEGER |  |
| DEFAULT_BLOCKS_YN | VARCHAR (1) |  |
| BLOCK_OVR_FIRST_C | INTEGER |  |
| ORD_GENERATED_YN | VARCHAR (1) |  |
| ORDER_ALL_YN | VARCHAR (1) |  |
| USE_DEFAULT_PROC_YN | VARCHAR (1) |  |
| PRC_REC_TYPE_C | INTEGER |  |
| AUTOSCHED_ALG_C | INTEGER |  |
| VTMOD_SCHED_C | INTEGER |  |
| VTMOD_MAX_AGE_DAYS | INTEGER | The maximum age the visit type modifier applies to, in days. |
| VTMOD_MIN_AGE_DAYS | INTEGER | The minimum age the visit type modifier applies to, in days. |
| VTMOD_SEX_C | INTEGER |  |
| VTMOD_MIN_AGE_NUM | INTEGER | The minimum age the visit type modifier applies to. |
| VTM_MIN_AGE_UNIT_C | INTEGER |  |
| VTMOD_MAX_AGE_NUM | INTEGER | The maximum age the visit type modifier applies to. |
| VTM_MAX_AGE_UNIT_C | INTEGER |  |
| VTMOD_PRC_ID | VARCHAR (18) | The unique ID associated with the visit type record using this visit type modifier. This column is frequently used to link to the CLARITY_PRC table. |
| VTMOD_PROV_ID | VARCHAR (18) | The unique ID associated with the provider record using this visit type modifier. This column is frequently used to link to the CLARITY_SER table. |
| VTMOD_DEPT_ID | NUMERIC (18,0) | The unique ID associated with the department record using this visit type modifier. This column is frequently used to link to the CLARITY_DEP table. |
| VTMOD_LENGTH_VAL | INTEGER | The length in minutes that the appointment will be modified by. |
| VTMOD_LEN_ADJ_C | INTEGER |  |
| VTMOD_REPL_SCH_C | INTEGER |  |
| VTMOD_USE_SCH_IP_YN | VARCHAR (1) |  |
| VTMOD_REPL_PAT_C | INTEGER |  |
| RFL_GRP_C | VARCHAR (66) |  |
| RECORD_STATUS_C | INTEGER |  |
| SCHED_OTHER_SPEC_C | INTEGER |  |
| REQUIRE_IPOP_YN | VARCHAR (1) |  |
| ARRIVAL_REASON | VARCHAR (254) | The reason for asking a patient to arrive early. |
| ARRIVAL_OFFSET_MINUTES | INTEGER | Default offset for arrival time for appointments of this type. |
| FILTER_RESTR_PROV_YN | VARCHAR (1) |  |
| ALLOW_OVERLAP_C | INTEGER |  |
| GROUP_SESSION_C | INTEGER |  |
| PANEL_VISIT_RELATIONSHIP_C | INTEGER |  |
| APPT_DELAY_DEFAULT_MINUTES | INTEGER | Default number of minutes from now to schedule this visit type. |
| PAT_PREP_TIME | INTEGER | Number of minutes before the appointment allotted to the patient for preparation. |
| PAT_RECOVERY_TIME | INTEGER | Number of minutes after the appointment allotted to the patient for recovery. |
| AGENT_CONFLICT_TYPE_C | INTEGER |  |
| DTREE_FORM_ID | VARCHAR (18) | The decision tree that will come up during Appointment Entry after a visit type is entered. |
| DEFAULT_FASTING_DURATION | INTEGER | The default fasting duration in hours. If an appointment with this visit type is linked to a procedure that has a fasting duration, whichever duration is longer will be used. |
| BREAKS_FAST_YN | VARCHAR (1) |  |
| USE_SMARTTEXT_PAT_INSTR_YN | VARCHAR (1) |  |
| HIDE_FROM_PAT_YN | VARCHAR (1) |  |
| ALLOW_CHANGE_HIDDEN_STATUS_YN | VARCHAR (1) |  |
| PROV_NAME_DISPLAY_C | INTEGER |  |
| HIDE_VISIT_TIME_YN | VARCHAR (1) | Surrogate key used to uniquely identify rows in this (and only this) table on Cogito Cloud only, do not assume the surrogate key in this table will correspond to the surrogate key in another table |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| B-TREE INDEX | EIX_CLARITY_PRC_CPPRID | CPT_PROC_ID | 1 | Yes | Yes |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | PRC_ID | CLARITY_PRC_2 | PRC_ID | No | No | No |  |
| 1 | PRC_ID | CLARITY_PRC_MYC | VISIT_TYPE_ID | No | No | No |  |
| 15 | CPT_PROC_ID | CLARITY_EAP | PROC_ID | No | No | No |  |
| 15 | CPT_PROC_ID | CLARITY_EAP_2 | PROC_ID | No | No | No |  |
| 15 | CPT_PROC_ID | CLARITY_EAP_3 | PROC_ID | No | No | No |  |
| 15 | CPT_PROC_ID | CLARITY_EAP_4 | PROC_ID | No | No | No |  |
| 15 | CPT_PROC_ID | CLARITY_EAP_5 | PROC_ID | No | No | No |  |
| 15 | CPT_PROC_ID | CLARITY_EAP_IMM | PROC_ID | Unknown | No | No |  |
| 15 | CPT_PROC_ID | PROC_CONSENT_CONFIG | PROC_ID | No | No | No |  |
| 15 | CPT_PROC_ID | PROC_UM | PROC_ID | No | No | No |  |
| 15 | CPT_PROC_ID | V_CUBE_D_PROCEDURE | PROCEDURE_ID | Unknown | Unknown | No |  |
| 29 | RPT_GRP_SIX_C | ZC_PRC_RPT_GRP_6 | RPT_GRP_SIX_C | No | No | No |  |
| 30 | RPT_GRP_SEVEN_C | ZC_PRC_RPT_GRP_7 | RPT_GRP_SEVEN_C | No | No | No |  |
| 31 | RPT_GRP_EIGHT_C | ZC_PRC_RPT_GRP_8 | RPT_GRP_EIGHT_C | No | No | No |  |
| 32 | RPT_GRP_NINE_C | ZC_PRC_RPT_GRP_9 | RPT_GRP_NINE_C | No | No | No |  |
| 33 | RPT_GRP_TEN_C | ZC_PRC_RPT_GRP_10 | RPT_GRP_TEN_C | No | No | No |  |
| 36 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 36 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 36 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 37 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 37 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 37 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 38 | RPT_GRP_ELEVEN_C | ZC_PRC_RPT_GRP_11 | RPT_GRP_ELEVEN_C | No | No | No |  |
| 39 | RPT_GRP_TWELVE_C | ZC_PRC_RPT_GRP_12 | RPT_GRP_TWELVE_C | No | No | No |  |
| 40 | RPT_GRP_THIRTEEN_C | ZC_PRC_RPT_GRP_13 | RPT_GRP_THIRTEEN_C | No | No | No |  |
| 41 | RPT_GRP_FOURTEEN_C | ZC_PRC_RPT_GRP_14 | RPT_GRP_FOURTEEN_C | No | No | No |  |
| 42 | RPT_GRP_FIFTEEN_C | ZC_PRC_RPT_GRP_15 | RPT_GRP_FIFTEEN_C | No | No | No |  |
| 43 | RPT_GRP_SIXTEEN_C | ZC_PRC_RPT_GRP_16 | RPT_GRP_SIXTEEN_C | No | No | No |  |
| 44 | RPT_GRP_SEVENTEEN_C | ZC_PRC_RPT_GRP_17 | RPT_GRP_SEVENTEEN_C | No | No | No |  |
| 45 | RPT_GRP_EIGHTEEN_C | ZC_PRC_RPT_GRP_18 | RPT_GRP_EIGHTEEN_C | No | No | No |  |

_(120 total; showing first 30)_
