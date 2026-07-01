# CLARITY_EAP_2

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=CLARITY_EAP_2

## Description

The CLARITY_EAP_2 table contains basic information about the procedure records in your system. This includes both A/R and clinical procedures. This is a continuation of Clarity table CLARITY_EAP.

**Overflow table** for CLARITY_EAP (149 cols). Contains additional columns for the same records — join on the shared primary key column.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | EAP |
| Release Version | Summer 2009 |
| May contain EHI? | No |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| PROC_ID | NUMERIC (18,0) | The unique ID of each procedure record in your system. This is not the CPT code or other procedure code. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| SCREENING_PROC_YN | VARCHAR (1) |  |
| ABN_SPANISH_NAME | VARCHAR (254) | The Spanish language description of the procedure used on the Spanish ABN form. |
| QTY_PER_BILL_CODE | NUMERIC (18,3) | Stores the quantity of a medication equivalent to one billing quantity of this procedure record's billing code. |
| QTY_PER_BC_UNITS_C | INTEGER |  |
| BILL_QTY_RND_FCTR | NUMERIC (18,3) | Stores the rounding factor used to calculate the billing quantity for the billing code represented by a procedure record. |
| HIDE_IN_RSLT_REV_YN | VARCHAR (1) |  |
| SERVICE_TIME_YN | VARCHAR (1) |  |
| USE_IP_ALT_YN | VARCHAR (1) |  |
| IP_DEF_ALT_ID | NUMERIC (18,0) | Displays the alternative procedure to use if the order is placed in an Inpatient setting. |
| DUP_ACROSS_ENC_YN | VARCHAR (1) |  |
| DUP_ENTIRE_ADM_YN | VARCHAR (1) |  |
| DUP_SEARCH_TIME | INTEGER | The time interval that is used to search for possible duplicates for this procedure starting from the time the new order is placed. |
| DUP_MATCH_TIME | INTEGER | The time interval that is used when comparing two specific scheduled times to determine whether they are close enough together to be considered a match. |
| USE_EXPIRING_YN | VARCHAR (1) |  |
| REV_ONLY_ONCE_YN | VARCHAR (1) |  |
| PAL_TAB_ADV_ACT_ID | NUMERIC (18,0) | The advantage activity that determines the tab style used for this procedure. This controls how the sub tabs appear in the Procedures tab in the reading palette. |
| CAPTION_OVERRIDE | VARCHAR (30) | Caption that is displayed on the tab for this procedure in the dynamic palette. |
| VESSEL_LOCATION_C | INTEGER |  |
| PROC_EXP_DATE | VARCHAR (254) | Stores the procedure expiration date. |
| OUTPAT_DFLT_PRI_C | INTEGER |  |
| REFUND_YN | VARCHAR (1) |  |
| SUM_FINDING_TGT_ID | NUMERIC (18,0) | Text generation template to use for this orderable procedure in Study Review's Summary Statement control. |
| PRODUCT_LINE | VARCHAR (254) | Product line for this procedure. |
| SPECIAL_PRICING | VARCHAR (254) | Special pricing for this procedure. |
| PROTOCOL_GROUPER_C | INTEGER |  |
| SCHED_GROUPER_C | INTEGER |  |
| TRANSPLANT_TYPE_C | INTEGER |  |
| ADJUSTMENT_CAT_C | INTEGER |  |
| UNIT_AFT_ST_DATE_C | INTEGER |  |
| UNIT_BEF_END_DATE_C | INTEGER |  |
| DEF_POS_TYPE_C | INTEGER |  |
| RX_GROUPER_YN | VARCHAR (1) |  |
| PRI_PHYS_SIG_REQ_YN | VARCHAR (1) |  |
| PRIOR_STAT_CONFIG_C | INTEGER |  |
| DFLT_ORDER_CLASS_C | VARCHAR (66) |  |
| NORMAL_DROP_YN | VARCHAR (1) |  |
| REF_DROP_YN | VARCHAR (1) |  |
| FUTURE_DROP_YN | VARCHAR (1) |  |
| DISABLE_BREAS_DE_YN | VARCHAR (1) |  |
| REQ_BD_AT_STATUS_C | INTEGER |  |
| LATERALITY_C | INTEGER |  |
| ALLOWANCE_YN | VARCHAR (1) |  |
| RESULT_RPT_TYPE_C | INTEGER |  |
| END_CONT_DATE | DATETIME | The latest contact date in datetime format. |
| END_CONT_DATE_REAL | FLOAT | The latest contact date in decimal format. |
| DIAGNOSTIC_PROC_YN | VARCHAR (1) |  |
| BIOPSY_PROC_YN | VARCHAR (1) |  |
| TECH_ACCESSIBLE_YN | VARCHAR (1) |  |
| ASMT_REQ_STATUS_C | INTEGER |  |
| MAM_BX_GUIDANCE_C | INTEGER |  |
| RATE_CENTER_ID | NUMERIC (18,0) | Used as the default Rate Center for a charge if it has this EAP. |
| ALL_HIST_COMP_YN | VARCHAR (1) |  |
| DEFAULT_LNC_ID | NUMERIC (18,0) | The unique ID of the LOINC (LNC) record that will be used if no complex mapping of LOINC codes has been done, or if there is no match in the complex mapping table. |
| REPEAT_UNIT_C | INTEGER |  |
| TRANSPLANT_DONOR_YN | VARCHAR (1) |  |
| DEFAULT_SMARTSET_ID | NUMERIC (18,0) | Stores a list of OTLs to be used in procedure documentation (ProcDoc). |
| ANTICOAG_EPISODE_NAME | VARCHAR (192) | The name given to an anticoagulation episode created from this procedure. |
| ANTICOAG_LINK_PROB_YN | VARCHAR (1) |  |
| ANTICOAG_CREATE_PROB_YN | VARCHAR (1) |  |
| ANTICOAG_SEND_ENROLL_MSG_YN | VARCHAR (1) |  |
| ANTICOAG_SEND_INR_RMNDR_YN | VARCHAR (1) |  |
| ANTICOAG_AUTH_PROV_BEHAV_C | INTEGER |  |
| ANTICOAG_AUTH_PROV_ROLE_C | INTEGER |  |
| NEW_OR_EST_C | INTEGER |  |
| MYC_GEN_SCH_TKT_YN *(deprecated)* | VARCHAR (1) |  |
| SCRFORM_TEMPLATE_ID | NUMERIC (18,0) | The navigator template that will be used to create screening forms for the procedure. |
| MYC_TKT_SCH_NAME | VARCHAR (128) | Holds what the patient will see on the scheduling ticket list associated with this procedure. |
| DENTAL_PROC_TYPE_C | INTEGER |  |
| INSTANT_OF_UPDATE_DTTM | DATETIME (Local) | The instant when the procedure record was last locked or unlocked before this row was extracted. Changes to the instant of update do not trigger a Clarity extract, so values in this column may not represent the current value in Chronicles. |
| NOTE_TEMPLATE_ID *(deprecated)* | VARCHAR (18) | *** Deprecated *** In table CLARITY_EAP_2, the column NOTE_TEMPLATE_ID (EAP/52009) has been deprecated. The deprecated column's content/data is no longer available since it is no longer populated in Chronicles.  The note writer template to be used for the procedure. |
| RPT_GRP_SIX_C *(deprecated)* | VARCHAR (66) |  |
| RPT_GRP_SEVEN_C *(deprecated)* | VARCHAR (66) |  |
| RPT_GRP_EIGHT_C *(deprecated)* | VARCHAR (66) |  |
| RPT_GRP_NINE_C *(deprecated)* | VARCHAR (66) |  |
| RPT_GRP_TEN_C *(deprecated)* | VARCHAR (66) |  |
| RPT_GRP_ELEVEN_C *(deprecated)* | VARCHAR (66) |  |
| RPT_GRP_TWELVE_C *(deprecated)* | VARCHAR (66) |  |
| RPT_GRP_THIRTEEN_C *(deprecated)* | VARCHAR (66) |  |
| RPT_GRP_FOURTEEN_C *(deprecated)* | VARCHAR (66) |  |
| RPT_GRP_FIFTEEN_C *(deprecated)* | VARCHAR (66) |  |
| RPT_GRP_SIXTEEN_C *(deprecated)* | VARCHAR (66) |  |
| RPT_GRP_SEVENTEEN_C *(deprecated)* | VARCHAR (66) |  |
| RPT_GRP_EIGHTEEN_C *(deprecated)* | VARCHAR (66) |  |
| RPT_GRP_NINETEEN_C *(deprecated)* | VARCHAR (66) |  |
| RPT_GRP_TWENTY_C *(deprecated)* | VARCHAR (66) |  |
| SCHED_DUR | INTEGER | This stores the default scheduling appointment length (in minutes) for the procedure when ordered. |
| SCHED_DUR_IS_CALC_YN | VARCHAR (1) |  |
| SCHED_DUR_BUFFER | INTEGER | Default amount of time (in minutes) that should be added to the order's scheduling duration if it is automatically calculated. |
| SCHED_IS_INFSN_VS_YN | VARCHAR (1) |  |
| SCHED_TOL_BEF | INTEGER | Stores the number of days before the expected date that the procedure can be scheduled within. |
| SCHED_TOL_AFTR | INTEGER | Stores the number of days after the expected date that the procedure can be scheduled within. |
| SCHED_TOL_NO_RESTR_BEF_YN | VARCHAR (1) |  |
| SCHED_TOL_NO_RESTR_AFTR_YN | VARCHAR (1) |  |
| TIME_BEF_ORD_END_DATE | INTEGER | The length of time before the end date that orders for this procedure will be flagged as expiring. Units of time can be specified as Hours, Days, or Weeks. |
| TIME_AFT_ORD_ST_DATE | INTEGER | The length of time after the start date that orders for this procedure should be reviewed. Units of time can be specified as Hours, Days, or Weeks. |
| SCRN_PROC_TYPES_C | INTEGER |  |
| ENABLE_ORDER_UP_YN | VARCHAR (1) |  |
| REQ_RSLT_LET_YN | VARCHAR (1) |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | PROC_ID | CLARITY_EAP | PROC_ID | No | No | No |  |
| 1 | PROC_ID | CLARITY_EAP_3 | PROC_ID | No | No | No |  |
| 1 | PROC_ID | CLARITY_EAP_4 | PROC_ID | No | No | No |  |
| 1 | PROC_ID | CLARITY_EAP_5 | PROC_ID | No | No | No |  |
| 1 | PROC_ID | CLARITY_EAP_IMM | PROC_ID | Unknown | No | No |  |
| 1 | PROC_ID | PROC_CONSENT_CONFIG | PROC_ID | No | No | No |  |
| 1 | PROC_ID | PROC_UM | PROC_ID | No | No | No |  |
| 1 | PROC_ID | V_CUBE_D_PROCEDURE | PROCEDURE_ID | Unknown | Unknown | No |  |
| 2 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 2 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 2 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 3 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 7 | QTY_PER_BC_UNITS_C | ZC_MED_UNIT | DISP_QTYUNIT_C | No | No | No |  |
| 12 | IP_DEF_ALT_ID | ALTERNATIVES | ALTERNATIVE_ID | Unknown | No | No |  |
| 19 | PAL_TAB_ADV_ACT_ID | ADV_ACTIVITY_DATA | ADV_ACTIVITY_ID | No | No | No |  |
| 21 | VESSEL_LOCATION_C | ZC_VESSEL_LOCATION | VESSEL_LOCATION_C | No | No | No |  |
| 23 | OUTPAT_DFLT_PRI_C | ZC_ORDER_PRIORITY | ORDER_PRIORITY_C | No | No | No |  |
| 28 | PROTOCOL_GROUPER_C | ZC_PROTCL_GROUPER | PROTCL_GROUPER_C | No | No | No |  |
| 29 | SCHED_GROUPER_C | ZC_SCHEDULING_GROU | SCHEDULING_GROU_C | No | No | No |  |
| 30 | TRANSPLANT_TYPE_C | ZC_TXP_COMMITTEE_T | TXP_COMMITTEE_T_C | No | No | No |  |
| 30 | TRANSPLANT_TYPE_C | ZC_TX_CLASS | TX_CLASS_C | Unknown | Unknown | Yes |  |
| 31 | ADJUSTMENT_CAT_C | ZC_ADJUSTMENT_CAT | ADJUSTMENT_CAT_C | No | No | No |  |
| 32 | UNIT_AFT_ST_DATE_C | ZC_TIME_PERIOD | TIME_PERIOD_C | No | No | No |  |
| 33 | UNIT_BEF_END_DATE_C | ZC_TIME_PERIOD | TIME_PERIOD_C | No | No | No |  |
| 34 | DEF_POS_TYPE_C | ZC_POS_TYPE | POS_TYPE_C | No | No | No |  |
| 37 | PRIOR_STAT_CONFIG_C | ZC_PRIOR_STAT_CONF | PRIOR_STAT_CONF_C | No | No | No |  |
| 38 | DFLT_ORDER_CLASS_C | ZC_LLB_ORDER_CLASS | LLB_ORDER_CLASS_C | No | No | No |  |
| 38 | DFLT_ORDER_CLASS_C | ZC_ORDER_CLASS | ORDER_CLASS_C | No | No | No |  |

_(47 total; showing first 30)_
