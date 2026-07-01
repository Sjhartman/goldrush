# CLARITY_DEP_2

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=CLARITY_DEP_2

## Description

This table extends CLARITY_DEP, which contains high-level information about departments from the Department master file.

**Overflow table** for CLARITY_DEP (110 cols). Contains additional columns for the same records — join on the shared primary key column.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | DEP |
| Release Version | Summer 2009 |
| May contain EHI? | No |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| DEPARTMENT_ID | NUMERIC (18,0) | The unique ID number assigned to the department record. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| ADDRESS_CITY | VARCHAR (254) | The city of the address for the department. |
| ADDRESS_STATE_C | VARCHAR (66) |  |
| ADDRESS_ZIP_CODE | VARCHAR (254) | The ZIP/postal code of the address for the department. |
| ADDRESS_COUNTY_C | VARCHAR (66) |  |
| ADDRESS_COUNTRY_C | VARCHAR (66) |  |
| ADDRESS_HOUSE_NUM | VARCHAR (254) | The house number of the address for the department. |
| ADDRESS_DISTRICT_C | INTEGER |  |
| EXPSCHED_ENABLED_YN | VARCHAR (1) |  |
| EXPSCHED_OFFSET | NUMERIC (18,0) | The release data offset override for express scheduling for the department. |
| ICU_DEPT_YN | VARCHAR (1) |  |
| SBO_CREATE_PB_HAR_C | INTEGER |  |
| ATTEND_EVNT_RULE_ID | VARCHAR (18) | The unique ID of the rule to determine the event triggered when assigning attending provider. |
| TT_DEF_EVNT_RULE_ID | VARCHAR (18) | The unique ID of the rule to determine the event triggered when assigning default treatment team. |
| RTLS_ARRV_EVNT_ID | VARCHAR (18) | The unique ID of the event that is recorded in a patient's events log when an attending provider arrives in the patient's room. This uses the real time location system (RTLS) to track the provider. |
| RTLS_DEPT_EVENT_ID | VARCHAR (18) | The unique ID of the event that is recorded in a patient's events log when an attending provider leaves the patient's room. This uses the real time location system (RTLS) to track the provider. |
| DEF_RTLS_ARRIVAL_ID | VARCHAR (18) | The unique ID of the event that is recorded in a patient's events log when a staff member arrives in the patient's room. This uses the real time location system (RTLS) to track the staff member. |
| DEF_RTLS_DEP_ID | VARCHAR (18) | The unique ID of the event that is recorded in a patient's events log when a staff member leaves the patient's room. This uses the real time location system (RTLS) to track the staff member. |
| ED_TB_USERSETTIN_YN *(deprecated)* | VARCHAR (1) |  |
| DUTCH_ICU_GROUP_C | INTEGER |  |
| FORCE_TBOT_YN | VARCHAR (1) |  |
| OVERDUE_RESULTS_ID | NUMERIC (18,0) | The unique ID of the Results Routing Scheme (LRS) used by this department to route Overdue Results messages to In Basket. |
| REL_CNT_NAME_PP_ID *(deprecated)* | NUMERIC (18,0) | In table CLARITY_DEP_2, the column REL_CNT_NAME_PP_ID (DEP/17120) has been deprecated. The deprecated column's content/data is no longer available since it is no longer populated in Chronicles.   This column stores the related name contact programming point.  It is used to define how related contacts coming from this department are named. |
| REL_CNT_DTL_PP_ID *(deprecated)* | NUMERIC (18,0) | In table CLARITY_DEP_2, the column REL_CNT_DTL_PP_ID (DEP/17125) has been deprecated. The deprecated column's content/data is no longer available since it is no longer populated in Chronicles.   This column stores the related contact details programming point.  It is used to define the details for related contacts for this department. |
| MED_PREF_LIST_ID | NUMERIC (18,0) | The unique ID of the medication Preference List (EPD) for the department. |
| ORDERS_PREF_LIST_ID | NUMERIC (18,0) | The unique ID of the Preference List (EPD) used by this department, including both medication and procedure orders. |
| DEPT_TRNSCR_EMPL_ID | VARCHAR (18) | The unique employee ID for the department transcriptionist. |
| DEPT_TRNSCR_POOL_C | VARCHAR (66) |  |
| DEP_LET_TRNS_EMP_ID | VARCHAR (18) | The unique employee ID for the department letter transcriptionist. |
| DEP_LET_TRNS_POOL_C | VARCHAR (66) |  |
| DISC_INT_ENAB_YN | VARCHAR (1) |  |
| MANUAL_FREE_YN | VARCHAR (1) |  |
| ALGLST_ATT_YN | VARCHAR (1) |  |
| ALGLST_PCP_YN | VARCHAR (1) |  |
| DEFAULT_MAR_FLOW_ID | VARCHAR (18) | The unique ID of the Flowsheet template that is used as the default MAR flowsheet template for this department. |
| EDU_ASSMT_TEMPLT_ID | NUMERIC (18,0) | The unique ID of the learning assessment template (ILA) record used by this department. |
| EDU_ASSMT_DISP_ID | NUMERIC (18,0) | The unique ID of the programming point record (LPP) used to display the Learning Assessment for this department record. |
| EDU_ASSMT_COPY_YN | VARCHAR (1) |  |
| NEAREST_MED_TIME | INTEGER | The number of time units used to round the scheduling medication orders and their associated activities. |
| NEAREST_MED_TIME_C | INTEGER |  |
| HOV_SHARED_LIST_ID | VARCHAR (18) | The unique ID of the shared list to be used to automatically add HOV patients on admission or a transfer to this department. On a transfer out or a discharge, the patient will be removed from this list. |
| MED_MSG_POOL_ID | NUMERIC (18,0) | The unique ID of the In Basket pool (HIP) which will receive medication messages for this department. |
| RX_TIMES_MSG_PL_ID | NUMERIC (18,0) | The unique ID of the In Basket pool (HIP) which is set to receive Rx Adjust Times Notification messages in the department record. |
| RX_MSG_TO_PROV_YN | VARCHAR (1) |  |
| RX_MARHOLD_NOTIF_YN | VARCHAR (1) |  |
| MAR_TIME_MATCH_DC | INTEGER | Number of hours past the discontinue time that the MAR will allow barcode matches on discontinued medication orders. |
| MAR_MATCH_DC_DUE_YN | VARCHAR (1) |  |
| UNVERIFIED_MED_P_ID | NUMERIC (18,0) | This column stores the HIP ID of the unverified medication administration notification pool associated with this department. |
| MAR_DSP_GROUPED_YN | VARCHAR (1) |  |
| MAR_LOOKAHEAD_GROUP | INTEGER | The number of hours the MAR activity will look ahead and display future medications. |
| MAR_LOOKBACK_GROUP | INTEGER | The number of hours that the MAR activity will look back and display discontinued medications. |
| MAR_SHIFT_HR_DISP | INTEGER | The number of hours to shift the display in the MAR activity. |
| DUAL_SIGNOFF_REQ_YN | VARCHAR (1) |  |
| MAR_DUAL_SIGN_RX_YN | VARCHAR (1) |  |
| MAR_TIME_LIMIT_PAST | INTEGER | This column stores how far in the past it is possible to record administrations on the MAR for patients in this DEP department. |
| MAR_TIME_LIMIT_FUT | INTEGER | This column stores how long in the future it is possible to consume due times on the MAR for patients in this DEP department. |
| MAR_TIME_DCMEDS | INTEGER | This column stores how long the MAR shows discontinued meds for patients in this department. |
| ONE_CLK_ADMIN_YN *(deprecated)* | VARCHAR (1) |  |
| MAR_SHIFT_PPT_ID | NUMERIC (18,0) | The unique ID of the programming point record (LPP) used to configure the times that appear in the MAR activity for users logged into this department. |
| DISAB_OVRIDE_LNK_YN | VARCHAR (1) |  |
| MAR_HAS_RX_INT_YN | VARCHAR (1) |  |
| HOV_SHLDC_LPP_ID | NUMERIC (18,0) | The unique ID of the extension record (LPP) used to determine whether an appointment should convert to a new HOV or redirect to a new encounter. |
| DFLT_RESUME_MED_C | INTEGER |  |
| ED_ARRIVAL_CONF_ID | VARCHAR (18) | The unique ID of the ED arrival confirmation record which is run when an expected patient is arrived. |
| ED_TEAM_WORDING | VARCHAR (254) | An alternate label for the word "Team" to be used in the sign-in activity. |
| ED_PAT_LIST_ID | NUMERIC (18,0) | The unique ID of the system patient list corresponding to this department. This is populated for Emergency or Labor & Delivery Departments. |
| MC_EXP_ID | NUMERIC (18,0) | The unique ID of the Care Area that will appear as the "Expected" area in the bottom panel of the ED Manager. If no Care Area is entered here, the Waiting  Room will expand to comprise the entire bottom panel. |
| SHOW_LANGUAGE_YN | VARCHAR (1) |  |
| IP_ALLOW_IVPUMP_YN | VARCHAR (1) |  |
| ED_EVENT_ARRIVAL_ID | VARCHAR (18) | The unique ID of the event that fires when a patient arrives in this ED. |
| ED_EVENT_ROOMED_ID | VARCHAR (18) | The unique ID of the event that fires when a patient is roomed in this ED. |
| ED_EVENT_TRANS_ID | VARCHAR (18) | The unique ID of the event that is fired when a patient is transferred within this ED. |
| ED_EVENT_TRAN_IN_ID | VARCHAR (18) | The unique ID of the event that fires when a patient is transferred into this ED from a different unit or ED. |
| ED_EVENT_DISMISS_ID | VARCHAR (18) | The unique ID of the event that fires when a patient is dismissed from this ED. |
| ED_EVENT_DISCH_ID | VARCHAR (18) | The unique ID of the event that fires when a patient is discharged from this ED. |
| ATTEND_ASGN_EVNT_ID | VARCHAR (18) | The unique ID of the event that will be recorded in the Patient Events Log when an attending provider is assigned to a patient's treatment team. |
| ATTEND_REMV_EVNT_ID | VARCHAR (18) | The unique ID of the event that will be recorded in the Patient Events Log when an attending provider is removed from a patient's treatment team. |
| TT_ASGN_EVNT_ID | VARCHAR (18) | The unique ID for the event that will be recorded in the patient events log when a staff member is assigned to a patient's treatment team. |
| TT_REMV_EVNT_ID | VARCHAR (18) | The unique ID for the event that will be recorded in the patient events log when a staff member is removed from a patient's treatment team. |
| DEP_EVENT_ID | VARCHAR (18) | This item holds the IEV record containing the events for this department. |
| ED_PCC_EVNT_DEF_ID | VARCHAR (18) | The unique ID of the event which is triggered when a patient class is changed in this department. Facility definition and workflow settings must be configured in order for this trigger to occur. |
| ED_CONTACT_RULE_ID | VARCHAR (18) | A rule to decide whether to display a warning message on ED arrival if there are existing preadmission contacts. |
| ED_CONTACT_TIME_HRS | INTEGER | The time frame to check against when showing an ED contact creation warning message. |
| ALLOW_EXPECTED_YN | VARCHAR (1) |  |
| MANAGER_WAIT2_ID | NUMERIC (18,0) | The care area that is the second waiting area in the ED Manager. This area is displayed on the left side, bottom panel of the ED Manager. |
| MANAGER_WAIT3_ID | NUMERIC (18,0) | The care area that is the third waiting area in the ED Manager. This area is displayed on the right side, bottom panel of the ED Manager. |
| IP_DATA_PURGE_DAYS *(deprecated)* | INTEGER | *** Deprecated *** In table CLARITY_DEP_2, the column IP_DATA_PURGE_DAYS (DEP/24450) has been deprecated. The deprecated column's content/data is no longer available since it is no longer populated in Chronicles. |
| PAT_VERIF_HCF_ID | VARCHAR (18) | The unique ID of the department override for the patient verification confirmation record. |
| ENC_VERIF_HCF_ID | VARCHAR (18) | The unique ID of the department override for the encounter verification confirmation record. |
| GUAR_VERIF_HCF_ID | VARCHAR (18) | The unique ID of the department override for the guarantor verification confirmation record. |
| HAR_VERIF_HCF_ID | VARCHAR (18) | The unique ID of the department override for the hospital account verification confirmation record. |
| CVG_VERIF_HCF_ID | VARCHAR (18) | The unique ID of the department override for the coverage verification confirmation record. |
| MEM_VERIF_HCF_ID | VARCHAR (18) | The unique ID of the department override for the coverage member verification confirmation record. |
| APPOINTMENT_PHONE | VARCHAR (20) | The appointment phone number for the department. |
| LOGO_FILENAME | VARCHAR (260) | The filename of the department's logo stored in a shared directory. |
| WKFLTRCK_ACTV_YN | VARCHAR (1) |  |
| LET_FRM_USER_DFLT_C | INTEGER |  |
| HAR_2_VERIF_HCF_ID | VARCHAR (18) | The unique ID of the department override for the second hospital account verification confirmation record. |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| BITMAP INDEX | EIX_ICU_DEPT_YN | ICU_DEPT_YN | 1 | Yes | Yes |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | DEPARTMENT_ID | BH_DEP | DEPARTMENT_ID | No | No | No |  |
| 1 | DEPARTMENT_ID | CLARITY_DEP | DEPARTMENT_ID | No | No | No |  |
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
| 2 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 2 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 2 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 3 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 5 | ADDRESS_STATE_C | ZC_ALT_INVOICE_STA | ALT_INVOICE_STA_C | No | No | No |  |
| 5 | ADDRESS_STATE_C | ZC_LLB_STATE | LLB_STATE_C | No | No | No |  |
| 5 | ADDRESS_STATE_C | ZC_REFG_PROV_STATE | REFG_PROV_STATE_C | No | No | No |  |
| 5 | ADDRESS_STATE_C | ZC_STATE | STATE_C | No | No | No |  |
| 5 | ADDRESS_STATE_C | ZC_STATE_HISTORY | STATE_HISTORY_C | No | No | No |  |
| 5 | ADDRESS_STATE_C | ZC_SUBSCR_EEP_STE | SUBSCR_EEP_STE_C | No | No | No |  |
| 5 | ADDRESS_STATE_C | ZC_TAX_STATE | TAX_STATE_C | No | No | No |  |

_(123 total; showing first 30)_
