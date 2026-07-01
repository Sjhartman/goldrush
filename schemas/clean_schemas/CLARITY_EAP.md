# CLARITY_EAP

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=CLARITY_EAP

## Description

The CLARITY_EAP table contains basic information about the procedure records in your system. This does include both A/R and clinical procedures.

**Primary table** in this group (149 cols). Overflow siblings joined on shared key: CLARITY_EAP_2 (101 cols), CLARITY_EAP_3 (14 cols), CLARITY_EAP_4 (39 cols), CLARITY_EAP_5 (54 cols). Prefer this table for most queries.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | EAP |
| Release Version | EPIC 2000 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| PROC_ID | NUMERIC (18,0) | The unique ID of each procedure record in your system. This is not the CPT? code or other procedure code. |
| PROC_NAME | VARCHAR (189) | The name of each procedure. |
| PROC_CODE | VARCHAR (40) | The code for each procedure. |
| PROC_CAT | 200 | The category to which each procedure belongs, such as General Surgery or Internal Medicine. This column is deprecated due to the fact that it can become out of sync with the EDP information.  Use PROC_CAT_ID to link to EDP_PROC_CAT_INFO and use EDP_PROC_CAT_INFO__PROC_CAT_NAME instead. |
| PROC_TYPE *(deprecated)* | VARCHAR (20) |  |
| DEBIT_CREDIT *(deprecated)* | VARCHAR (20) |  |
| IS_BAD_DEBT_ACCT | VARCHAR (20) |  |
| ACCOUNT_INS *(deprecated)* | VARCHAR (20) |  |
| RPT_GRP_ONE | VARCHAR (80) | You have the ability to specify groupers for enterprise reporting, SQL, or report generator reporting. There are free text groupers and category groupers. If you elect to use these groupers, please contact your enterprise reporting representative for assistance. This is the first report grouper, with type free text. |
| RPT_GRP_TWO | VARCHAR (80) | You have the ability to specify groupers for enterprise reporting, SQL, or report generator reporting. There are free text groupers and category groupers. If you elect to use these groupers, please contact your enterprise reporting representative for assistance. This is the second report grouper, with type free text. |
| RPT_GRP_THREE | VARCHAR (80) | You have the ability to specify groupers for enterprise reporting, SQL, or report generator reporting. There are free text groupers and category groupers. If you elect to use these groupers, please contact your enterprise reporting representative for assistance. This is the third report grouper, with type free text. |
| RPT_GRP_FOUR | VARCHAR (80) | You have the ability to specify groupers for enterprise reporting, SQL, or report generator reporting. There are free text groupers and category groupers. If you elect to use these groupers, please contact your enterprise reporting representative for assistance. This is the fourth report grouper, with type free text. |
| RPT_GRP_FIVE | VARCHAR (80) | You have the ability to specify groupers for enterprise reporting, SQL, or report generator reporting. There are free text groupers and category groupers. If you elect to use these groupers, please contact your enterprise reporting representative for assistance. This is the fifth report grouper, with type free text. |
| RPT_GRP_SIX | VARCHAR (66) |  |
| RPT_GRP_SEVEN | VARCHAR (66) |  |
| RPT_GRP_EIGHT | VARCHAR (66) |  |
| RPT_GRP_NINE | VARCHAR (66) |  |
| RPT_GRP_TEN | VARCHAR (66) |  |
| GL_NUM_CREDIT | VARCHAR (100) | The default credit general ledger code for the procedure. |
| GL_NUM_DEBIT | VARCHAR (100) | The default debit general ledger code for the procedure. |
| IS_ACTIVE_YN | VARCHAR (1) |  |
| PANEL_C | INTEGER |  |
| PROC_COMMENT | VARCHAR (255) | The comment associated with the procedure. |
| IS_PRICE_OVRD_YN | VARCHAR (1) |  |
| EAP_TYPE_OF_SER_C | INTEGER |  |
| MODIFIER | VARCHAR (255) | The modifier or group of modifiers that billing system automatically applies to the procedure in charge entry. |
| IS_EC_INACTIVE_YN *(deprecated)* | VARCHAR (1) |  |
| UB_REV_CODE_ID | NUMERIC (18,0) | The Revenue Summary Code |
| COST_CNTR_ID | NUMERIC (18,0) | The unique ID of the hospital cost center associated with the procedure record. This is networked to the billing cost/rate centers masterfile. |
| CM_PHY_OWNER_ID | VARCHAR (25) | ID of the physical deployment owner for this record.  Physical owners will be where the data is hosted, either on the cross-over server or the owner deployment. |
| CM_LOG_OWNER_ID | VARCHAR (25) | ID of the logical deployment owner for this record.  Logical owners show the deployment where the record was created but doesn't represent if the record is a part of version skew. |
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
| PROC_GROUP_ID | VARCHAR (254) | The procedure cluster or group to which this procedure belongs. |
| OP_LOOKBACK_DAY | VARCHAR (254) | Indicate the lookback time for duplicate checking. This item stores the string value of the duplicate interval (in days). This value is converted into hours and populated into item-10105 Outpatient Duplicate Interval. To specify an interval in DAYS, you can enter a positive number.  To specify an interval in HOURS, you can enter it in terms of days. (e.g., to specify 6 hours, enter .25) To specify the interval in weeks, you can enter a number/fraction followed by the letter W. (e.g., to specify 3 weeks, type 3W or 3.0W). The value is converted to equivalent days and displayed to the user. Note: Large interval values may cause the system to slow down considerably. Please consult your system Technical Services Representative before setting large values in this field. When a procedure is ordered, a check is made to see if that procedure had been previously ordered within the duplicate interval. If found, the user is asked whether to continue placing the order. The order in which duplicate interval is looked up is -  Procedure -> Procedure Category -> Department -> Misc. configuration If the interval value in the Misc. Configuration level is used and if the interval is empty or equal to zero, the system will check duplicates against orders placed in the same session; if the interval is -1, the duplicate check will be disabled. |
| IP_LOOKBACK_DAY | VARCHAR (254) | Indicate the lookback time for duplicate checking. This item stores the string value of the duplicate interval (in days). This value is converted into hours and populated into item-10110 Inpatient Duplicate Interval. To specify an interval in DAYS, you can enter a positive number.  To specify an interval in HOURS, you can enter it in terms of days. (e.g., to specify 6 hours, enter .25) To specify the interval in weeks, you can enter a number/fraction followed by the letter W. (e.g., to specify 3 weeks, type 3W or 3.0W). The value is converted to equivalent days and displayed to the user. Note: Large interval values may cause the system to slow down considerably. Please consult your system Technical Services Representative before setting large values in this field.  When a procedure is ordered, a check is made to see if that procedure had been previously ordered within the duplicate interval. If found, the user is asked whether to continue placing the order. The order in which duplicate interval is looked up is -  Procedure -> Procedure Category -> Department -> Misc. configuration If the interval value in the Misc. Configuration level is used and if the interval is empty or equal to zero, the system will check duplicates against orders placed in the same session; if the interval is -1, the  duplicate check will be disabled. |
| CAT_OVERRIDE_ID *(deprecated)* | VARCHAR (254) | The procedure category database is used for defaults for several clinical system processes, including ASP, charge triggering, SmartText, overdue messages, and scheduling instructions.  These may require different organization from billing system-based procedure categories.  All clinical system processes will use these defaults, while billing system will ignore them. This column is deprecated due to the fact that it can become out of sync with the EDP information.  Use EC_OVRD_PROC_CAT_ID to link to EDP_PROC_CAT_INFO and use EDP_PROC_CAT_INFO__PROC_CAT_NAME instead. |
| SHOW_IN_MYC_YN | VARCHAR (1) |  |
| PT_FRIENDLY_NAME *(deprecated)* | VARCHAR (254) |  |
| SHOW_IN_MYC_C | INTEGER |  |
| CLM_PROC_TYPE_C | INTEGER |  |
| BILLING_CAT_C | VARCHAR (66) |  |
| RECORD_STATE_EAP_C | INTEGER |  |
| SELF_INS_C | INTEGER |  |
| DEBIT_OR_CREDIT_C | INTEGER |  |
| TYPE_C | VARCHAR (20) |  |
| ADMIN_PX_TYPE_C | INTEGER |  |
| ADMIN_PX_ERX_ID | NUMERIC (18,0) | ERX for configuring some of the "MAR" administration behaviors of this administrable procedure. |
| REL_PREF_CARD_ID | VARCHAR (254) | Specifies the corresponding preference card which holds the surgery-related configuration. |
| RIS_SIGN_AGAIN_R_YN | VARCHAR (1) |  |
| VENDOR_MEDIUM_DESC | VARCHAR (254) | Store vendor medium description of CPT codes |
| VENDOR_SHORT_DESC | VARCHAR (254) | Store vendor short description of CPT codes |
| PROC_DEFAULT_ORD_ID | NUMERIC (18,0) | This item holds the default orderable EAP |
| EXT_CROSS_REF_CODE | VARCHAR (20) | Stores the external cross reference code for the EAP record (used by Tapestry to store the UBC Revenue Code, as an override for the value stored in EAP 100) |
| PRINT_DESC_YN | VARCHAR (1) |  |
| IDE_NUMBER | VARCHAR (254) | Investigation Device Exemption Number  This number will appear in ANSI claim in the 2300 REF*LX segment.  To print this number on a paper claim, add Virtual Item 4319 to your paper form record.  If the IDE number is specified in the Claim Information Record (item CLM 28), then that number will appear on the claim instead. |
| DFLT_ADJ_DATE_C | INTEGER |  |
| REASON_CODE_ID | VARCHAR (18) | The unique ID of the default reason code to use if the action associated with this adjustment did not have a reason code given in payment posting. This reason code will be reported in the claim adjustment segment in secondary claims. |
| INST_OF_EDIT_TM | DATETIME (UTC) | Instant of edit/create. |
| DFLT_STAND_COUNT | INTEGER | The default standing order count for this procedure when it is placed as a standing order. Column IP_COUNT_TYPE_C gives the unit (days, hours, occurrences, etc). |
| IP_COUNT_TYPE_C | INTEGER |  |
| IS_PROC_USED | VARCHAR (1) | Indicates whether a procedure is used. A value of 1 indicates that the procedure is used. |
| SHORT_NAME | VARCHAR (254) | The short name for a procedure.  It is used in reports and displays where space is limited. |
| DFLT_PMT_SRC_C | VARCHAR (254) |  |
| SPRS_PNL_ALT_CHK_YN | VARCHAR (1) |  |
| REQ_DX_ASSOC_C | INTEGER |  |
| DFLT_SPEC_TYPE_C | INTEGER |  |
| DFLT_ORDER_TYPE_C | INTEGER |  |
| DFLT_RLSE_STAT_C | INTEGER |  |
| DFLT_EXPEC_DT | VARCHAR (254) | The default expected date for a procedure.  It is typically set in terms of days or weeks from the current date. |
| EXPEC_DT_APPROX_YN | VARCHAR (1) |  |
| DFLT_RLSE_TYPE_C | INTEGER |  |
| DFLT_RLSE_INTER_C | VARCHAR (66) |  |
| DFLT_RLSE_COUNT | INTEGER | The release count for a standing procedure.  It must be between 1 and 1000. |
| MAX_ORDERABLE | INTEGER | The maximum quantity that can be ordered for a procedure. |
| SHOW_ORD_DETAIL_C | INTEGER |  |
| USE_ALT_CHOICES_YN | VARCHAR (1) |  |
| DFLT_ALT_ID | NUMERIC (18,0) | The unique ID of the alternative to use for a procedure by default. |
| MAMMO_RELATED_YN | VARCHAR (1) |  |
| DFLT_SPEC_SRC_MAL_C | INTEGER |  |
| DFLT_SPEC_SRC_FEM_C | INTEGER |  |
| ORDER_DISPLAY_NAME | VARCHAR (254) | The default display name used for a procedure in the preference list display in order entry. |
| DFLT_INTER_ID | VARCHAR (18) | The unique ID of the default interval or frequency of occurrence for a standing order. |
| PROC_CAT_ID | VARCHAR (254) | The unique ID of the procedure category that is associated with this procedure. |
| EC_OVRD_PROC_CAT_ID | VARCHAR (254) | The unique ID of the procedure category that will be used as the default in Ambulatory EMR.  All Ambulatory EMR will use this procedure category as the default, while Resolute will ignore it. |
| SCHED_FOR_OUTPAT_YN | VARCHAR (1) |  |
| PROMPT_FOR_VT_YN | VARCHAR (1) |  |
| USE_VT_SPEC_REST_C | INTEGER |  |
| TEST_ID | VARCHAR (18) | The ID of the test that this procedure will create.  This is the test or test grouper used when an order linked to this procedure is accessioned in Lab. |
| USE_TIME_AVG_YN | VARCHAR (1) |  |
| MUST_START_AFTER_TM | DATETIME (Local) | Time before which this procedure cannot be scheduled. This can be used in the scenarios in which the procedure requires a particular resource, which is usually not available before a certain time of the day. |
| MUST_START_BEF_TM | DATETIME (Local) | Time after which this procedure cannot be scheduled. This can be used in the scenarios in which the procedure requires a particular resource, which is usually not available after certain time of the day. |
| SETUP_TIME | NUMERIC (18,0) | Setup time needed for this procedure. |
| CLEANUP_TIME | NUMERIC (18,0) | Cleanup time needed for this procedure |
| TIME_ALONE | NUMERIC (18,0) | Time required to perform this procedure when it is the only procedure in the case. This time is used only until the system has sufficient averaging data, or if you have decided to not use averaging for this procedure. |
| TIME_COMBINED | NUMERIC (18,0) | Time required to perform this procedure when there are other procedures being performed as well. This time is used only until the system has sufficient averaging data, or if you have decided to not use averaging for this procedure. |
| AVG_LEN_FOR_BILL | NUMERIC (18,0) | Stores average procedure length in minutes for billing purposes. Additional timing charges will be sent if the case takes more time than specified in this item. |
| USE_AVG_FROM_ID | NUMERIC (18,0) | The unique ID of the procedure with which this procedure shares the averaging data. This can be used to expedite the average build up and accuracy for similar procedures. |
| TYPE_OF_PROC_C | VARCHAR (66) |  |
| DFLT_WOUND_CLASS_C | INTEGER |  |
| DFLT_LAT_C | INTEGER |  |
| DFLT_OUTPAT_REGN_C | INTEGER |  |
| DFLT_PK_LST_GNRTD_C | INTEGER |  |
| LAP_YN | VARCHAR (1) |  |
| SURG_HIST_ID | NUMERIC (18,0) | Stores the EAP ID of the linked surgical history procedure which should be used to update surgical history when this procedure is documented as having been performed. |
| DFLT_ANESTH_TYPE_C | INTEGER |  |
| SERVICE_AREA_ID | NUMERIC (18,0) | The unique ID of the service area that is associated with this procedure. |
| NAME *(deprecated)* | VARCHAR (70) | In table CLARITY_EAP, the column NAME (EAP-90) has been deprecated. The deprecated column's content/data is no longer available since it is no longer populated in Chronicles.  The deprecated column's content/data is no longer available since it is no longer extracted to Clarity  Desc: The name for this procedure. |
| CHARGE_ENTRY_INSTR | VARCHAR (254) | Charge entry instructions for this procedure. |
| BILL_DESC | VARCHAR (254) | The description printed on the bill if different than the procedure name. |
| SPEC_PROC_TYPE_C | VARCHAR (66) |  |
| NUM_SURFACES_REQ | INTEGER | The number of surfaces the system requires a user to enter for this procedure in the Dental Information window in charge entry or account maintenance. |
| COMP_ANES_CONC_YN | VARCHAR (1) |  |
| ALLOW_PER_EXCL_YN | VARCHAR (1) |  |
| DX_REQ_YN | VARCHAR (1) |  |
| RECALL_ALLOWED_YN | VARCHAR (1) |  |
| DFLT_RECALL_MONTHS | INTEGER | The default number of months to follow up on this procedure. |
| DESC_ENTRY_YN | VARCHAR (1) |  |
| SYSTEM_GEN_YN | VARCHAR (1) |  |
| EFT_ADJ_YN | VARCHAR (1) |  |
| VIEW_PNL_DETAIL_YN | VARCHAR (1) |  |
| CE_RESTR_SEX_C | INTEGER |  |
| CE_RESTR_REF_YN | VARCHAR (1) |  |
| GL_DEBIT_TYPE_C | VARCHAR (66) |  |
| GL_CREDIT_TYPE_C | VARCHAR (66) |  |
| BILLING_SUMMARY | VARCHAR (254) | The billing summary code for this procedure. |
| STOP_QUANTITY_YN | VARCHAR (1) |  |
| VISIT_INDICATOR_C | INTEGER |  |
| GLFC_SVC_AREA_ID | NUMERIC (18,0) | The general ledger financial class service area ID for this procedure. |
| GLFC_DB_NUM | VARCHAR (254) | The general ledger financial class debit number for this procedure. |
| GLFC_CR_NUM | VARCHAR (254) | The general ledger financial class credit number for this procedure. |
| DISTRIBUTE_LVL_C *(deprecated)* | INTEGER |  |
| BLOOD_RELATED_C | INTEGER |  |
| FUTURE_PROC_EXP_DT | VARCHAR (254) | Expiration date for future orders. |
| STAND_PROC_EXP_DT | VARCHAR (254) | Standing expiration date for the procedure. |
| OUTPAT_DUP_INTER | INTEGER | The duplicate interval for outpatient in whole hours. |
| INPAT_DUP_INTER | INTEGER | The duplicate interval for inpatient in whole hours. |
| SMARTGROUP_ID | NUMERIC (18,0) | The unique ID of the order group that is associated with this procedure. |
| MODALITY_TYPE_C | INTEGER |  |
| EXT_AR_TYPE_C | INTEGER | Surrogate key used to uniquely identify rows in this (and only this) table on Cogito Cloud only, do not assume the surrogate key in this table will correspond to the surrogate key in another table |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | PROC_ID | CLARITY_EAP_2 | PROC_ID | No | No | No |  |
| 1 | PROC_ID | CLARITY_EAP_3 | PROC_ID | No | No | No |  |
| 1 | PROC_ID | CLARITY_EAP_4 | PROC_ID | No | No | No |  |
| 1 | PROC_ID | CLARITY_EAP_5 | PROC_ID | No | No | No |  |
| 1 | PROC_ID | CLARITY_EAP_IMM | PROC_ID | Unknown | No | No |  |
| 1 | PROC_ID | PROC_CONSENT_CONFIG | PROC_ID | No | No | No |  |
| 1 | PROC_ID | PROC_UM | PROC_ID | No | No | No |  |
| 1 | PROC_ID | V_CUBE_D_PROCEDURE | PROCEDURE_ID | Unknown | Unknown | No |  |
| 14 | RPT_GRP_SIX | ZC_EAP_RPT_GRP_6 | RPT_GRP_SIX | No | No | No |  |
| 15 | RPT_GRP_SEVEN | ZC_EAP_RPT_GRP_7 | RPT_GRP_SEVEN | No | No | No |  |
| 16 | RPT_GRP_EIGHT | ZC_EAP_RPT_GRP_8 | RPT_GRP_EIGHT | No | No | No |  |
| 17 | RPT_GRP_NINE | ZC_EAP_RPT_GRP_9 | RPT_GRP_NINE | No | No | No |  |
| 18 | RPT_GRP_TEN | ZC_EAP_RPT_GRP_10 | RPT_GRP_TEN | No | No | No |  |
| 22 | PANEL_C | ZC_PANEL | PANEL_C | No | No | No |  |
| 25 | EAP_TYPE_OF_SER_C | ZC_EAP_TYPE_OF_SER | EAP_TYPE_OF_SER_C | No | No | No |  |
| 25 | EAP_TYPE_OF_SER_C | ZC_TYPE_OF_SERVICE | TYPE_OF_SERVICE_C | No | No | No |  |
| 25 | EAP_TYPE_OF_SER_C | ZC_UBC_TYPE_OF_SER | UBC_TYPE_OF_SER_C | No | No | No |  |
| 28 | UB_REV_CODE_ID | CL_UB_REV_CODE | UB_REV_CODE_ID | No | No | No |  |
| 29 | COST_CNTR_ID | CL_COST_CNTR | COST_CNTR_ID | No | No | No |  |
| 30 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 30 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 30 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 31 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 31 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 31 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 32 | RPT_GRP_ELEVEN_C | ZC_EAP_RPT_GRP_11 | RPT_GRP_ELEVEN_C | No | No | No |  |
| 33 | RPT_GRP_TWELVE_C | ZC_EAP_RPT_GRP_12 | RPT_GRP_TWELVE_C | No | No | No |  |
| 34 | RPT_GRP_THIRTEEN_C | ZC_EAP_RPT_GRP_13 | RPT_GRP_THIRTEEN_C | No | No | No |  |
| 35 | RPT_GRP_FOURTEEN_C | ZC_EAP_RPT_GRP_14 | RPT_GRP_FOURTEEN_C | No | No | No |  |
| 36 | RPT_GRP_FIFTEEN_C | ZC_EAP_RPT_GRP_15 | RPT_GRP_FIFTEEN_C | No | No | No |  |

_(218 total; showing first 30)_
