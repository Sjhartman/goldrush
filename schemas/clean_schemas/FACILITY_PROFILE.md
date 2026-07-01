# FACILITY_PROFILE

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=FACILITY_PROFILE

## Description

This table contains basic information about your facility record. It only contains information from the newest contact.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | FULL |
| Load Frequency | WEEKLY - FULL |
| Chronicles INI | LDF |
| Release Version | SPRING 2008 |
| May contain EHI? | No |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| LAB_ID | VARCHAR (18) | The unique ID of the facility. This will always be 1. |
| CONTACT_DATE_REAL | No | A unique, internal contact date in decimal format. The integer portion of the number indicates the date of the contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| LAB_DATE | DATETIME | The date of this contact in calendar format. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| CM_CT_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this contact. This is only populated if you use IntraConnect. |
| SPEC_REC_BEHAVIOR_C | INTEGER |  |
| SPEC_RECV_BEH_EX_C | INTEGER |  |
| DFLT_TEST_ID | VARCHAR (18) | The unique ID of the test to use during accessioning if there is no EAP-OVT link. |
| DFLT_TEST_METHOD_ID | VARCHAR (18) | The unique ID of the method to use as the default test method. |
| DFLT_QC_PRI_C | VARCHAR (66) |  |
| DFLT_PACKNG_LIST_ID | VARCHAR (18) | The unique ID of the default packing list. |
| DFLT_COLL_LIST_ID *(deprecated)* | VARCHAR (18) | *** Deprecated *** In table FACILITY_PROFILE, the column DFLT_COLL_LIST_ID (LDF/51311) has been deprecated. The deprecated column's content/data is no longer available since it is no longer populated in Chronicles. |
| ADDON_RPT_SET_ID | NUMERIC (18,0) | The unique ID of the report setting used when looking up available orders for add-ons. |
| ACCESS_REPORT_ID *(deprecated)* | VARCHAR (18) | In table FACILITY_PROFILE, the column ACCESS_REPORT_ID (LDF/51810) has been deprecated. The deprecated column's content/data is no longer available since it is no longer populated in Chronicles. |
| COLL_TRNSFR_RPT_ID *(deprecated)* | VARCHAR (18) | *** Deprecated *** In table FACILITY_PROFILE, the column COLL_TRNSFR_RPT_ID (LDF/51811) has been deprecated. The deprecated column's content/data is no longer available since it is no longer populated in Chronicles. |
| LLB_LAB_ID | NUMERIC (18,0) | The unique ID of the resulting agency. This links the facility to resulting agency, and vice versa. |
| DFLT_OUT_SECT_CODE *(deprecated)* | VARCHAR (254) | In table FACILTY_PROFILE, the column DFLT_OUT_SECT_CODE (LDF/51825) has been deprecated. The deprecated column's content/data is no longer available since it is no longer populated in Chronicles. |
| DFLT_OUTRCH_LAB_ID *(deprecated)* | VARCHAR (18) | *** Deprecated *** This item has been discontinued.  The unique ID of the default destination lab to be used if the resulting agency selected by a provider or over the web does not already have a corresponding laboratory. |
| DFLT_HLD_TO_APPLY_C | INTEGER |  |
| DISPLAY_WARN_MSG_YN | VARCHAR (1) |  |
| IS_USER_AUTH_YN | VARCHAR (1) |  |
| SUSCEPT_RULES_ID | NUMERIC (18,0) | The unique ID of the tree node containing susceptibility rules. |
| SPEC_ID_LENGTH *(deprecated)* | INTEGER | *** Deprecated *** In table FACILITY_PROFILE, the column SPEC_ID_LENGTH (LDF/3130) has been deprecated. The deprecated column's content/data is no longer available since it is no longer populated in Chronicles. |
| LABEL_REPRINT_YN | VARCHAR (1) |  |
| DFLT_FAX_DEVICE_ID | NUMERIC (18,0) | The unique ID of the default fax device. This is used for faxing reports in cases where the recipient's fax device cannot be found. |
| DFLT_PRNT_DEVICE_ID | NUMERIC (18,0) | The unique ID of the default printing device. This is used for printing reports in cases where the recipient's device cannot be found. |
| DFLT_BLOCK_TYPE_ID *(deprecated)* | VARCHAR (18) | In table FACILITY_PROFILE, the column DFLT_BLOCK_TYPE_ID (LDF/51365) has been deprecated. The deprecated column's content/data is no longer available since it is no longer populated in Chronicles.  The unique ID of the container type that will be used to create blocks when a block creation task is not explicitly specified for a group of slides. |
| QC_SECTION_CODE | VARCHAR (254) | The default section code for QC specimens for the facility. |
| ACTION_ON_WARN_C | INTEGER |  |
| ACTION_ON_REJECT_C | INTEGER |  |
| BKG_JOB_USER_ID | VARCHAR (18) | This specifies the background job user used in background jobs. |
| REQ_BATCH_TYPE_ID | VARCHAR (18) | This specifies the batch type to use for requistion batches created in Express Requisition Entry. |
| REQ_BATCH_GEN_PP_ID | NUMERIC (18,0) | This specifies the programming point used to generate the batch ID for Express Requisition Entry batches. |
| RES_RPT_SETNG_PP_ID | NUMERIC (18,0) | The programming point used in result reporting to determine the settings to use to process the report. |
| AB_INTERP_SENS_C | INTEGER |  |
| QC_PRECISION_OVRIDE | NUMERIC (2,0) | The number of additional digits of precision to use for QC results |
| RES_RPT_STOR_TYPE_C | INTEGER |  |
| RES_RPT_FILE_PP_ID | NUMERIC (18,0) | Programming point to determine settings when generating files for result reports. |
| RES_RPT_STORE_PATH *(deprecated)* | VARCHAR (254) | *** Deprecated *** In table FACILITY_PROFILE, the column RES_RPT_STORE_PATH (LDF-51372) has been deprecated. The deprecated column's content/data is no longer available since it is no longer populated in Chronicles. |
| RES_RPT_VIEW_APP | VARCHAR (254) | Application to use when viewing external result report files. |
| BATCH_SEC_CD_LENGTH | NUMERIC (18,0) | Defines an upper-bound length limit for the section code when generating Batch (OVB) record IDs. |
| PRV_RSLT_USR_VRFY_C | INTEGER |  |
| NO_REL_UNSOL_QC_YN | VARCHAR (1) |  |
| TAT_BASIS_C | INTEGER |  |
| REGISTER_CC_FAX_YN | VARCHAR (1) |  |
| CHARGE_INPUT_LPP_ID | NUMERIC (18,0) | The unique ID of the programming point which is used to override charge input information before the charge is created. |
| RES_UPD_CORR_RSN_C | INTEGER |  |
| CANCEL_BEHAVIOR_C | INTEGER |  |
| CANCEL_REASON_C | VARCHAR (66) |  |
| CANCEL_RULE_ID | VARCHAR (18) | A rule to be evaluated that can block auto-canceling on a per-order basis. |
| SCI_NOTATN_FMT_C | INTEGER |  |
| AP_RES_TRANS_FMT_C | INTEGER |  |
| SEARCH_BY_OVSID_YN | VARCHAR (1) |  |
| CANCEL_HIGH_PRI_YN | VARCHAR (1) |  |
| TRACE_SHUTOFF_DT | DATETIME | The date that document tracing will automatically turn off. If not set, then tracing is already off. |
| RECALC_DISP_DT_YN | VARCHAR (1) |  |
| PRNT_BLANK_LABEL_YN | VARCHAR (1) |  |
| ASGN_USR_DF_EXT_ID | NUMERIC (18,0) | The unique ID of the extension which defines the default assigned user if the follow-up type does not define a type-specific extension. |
| USE_AUTO_REG_YN | No | *** Deprecated *** The auto-registration functionality is now renamed as Use Hospital Account. This column has been replaced by column USE_HOSP_ACCT_YN to avoid confusion with column title.  Stores whether or not auto registration should be used. |
| AUTO_DISPOSE_YN | VARCHAR (1) |  |
| AP_CHRG_REVIEW_YN *(deprecated)* | VARCHAR (1) |  |
| PRNT_COVER_SHEET_C | INTEGER |  |
| USE_CHG_BUNDLER_YN | VARCHAR (1) |  |
| GLOBAL_COUNTER_LEN | INTEGER | The length of the global counter piece in case number setup for this facility. |
| ALLOW_MANUAL_NUM_C | INTEGER |  |
| GENRT_ADDON_ID_YN | VARCHAR (1) |  |
| FAILED_FAX_MSG_YN | VARCHAR (1) |  |
| CANCEL_TIME_INTER | INTEGER | The value, in minutes, representing the time interval the system uses to identify duplicates to be canceled. |
| DFLT_CALC_METHOD_ID | VARCHAR (18) | Links an LDF record to a MAC record to setup a default calculated component method. |
| SEARCH_BY_OVCID_YN | VARCHAR (1) |  |
| USE_HOSP_ACCT_YN | VARCHAR (1) |  |
| AP_CHRG_REVIEW_C | INTEGER |  |
| USE_BILL_ENC_C | INTEGER |  |
| TURNOFF_SMARTTEXT_YN | VARCHAR (1) |  |
| SPEC_HDR_SMRTTXT_ID | VARCHAR (18) | This item stores the default SmartText that should be used for the specimen-level header content for AP Quick Results in the Outstanding List. |
| AUTO_CPT_PB_C | INTEGER |  |
| CRIT_PUSH_PRELIM_RULE_ID | VARCHAR (18) | Prelim verification rule to qualify a result as needing critical result follow-up and push notification. |
| CRIT_PUSH_PRELIM_UNCALL_YN | VARCHAR (1) |  |
| CRIT_PUSH_PRELIM_DISABLE_YN | VARCHAR (1) |  |
| CRIT_PUSH_FINAL_RULE_ID | VARCHAR (18) | Final verification rule to qualify a result as needing critical result follow-up and push notification. |
| CRIT_PUSH_FINAL_UNCALL_YN | VARCHAR (1) |  |
| CRIT_PUSH_FINAL_DISABLE_YN | VARCHAR (1) |  |
| CRIT_SUPPRESS_CREAT_OL_ROW_YN | VARCHAR (1) |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | LAB_ID | AP_CASE_TYPES | LAB_ID | Unknown | No | No |  |
| 1 | LAB_ID | LAB_AP_LAB_SETUP | LAB_ID | Unknown | No | No |  |
| 1 | LAB_ID | LAB_INFO | LAB_ID | Unknown | No | No |  |
| 1 | LAB_ID | LAB_PROFILE | LAB_ID | Unknown | No | No |  |
| 1 | LAB_ID | LAB_SECTION | SECTION_ID | Unknown | No | No |  |
| 1 | LAB_ID | LDF_REQ_SETUP | LAB_ID | Unknown | No | No |  |
| 1 | LAB_ID | WORKBENCH_PROFILE | WORKBENCH_ID | Unknown | No | No |  |
| 4 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 4 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 4 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 5 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 5 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 5 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 6 | CM_CT_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 6 | CM_CT_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 6 | CM_CT_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 7 | SPEC_REC_BEHAVIOR_C | ZC_SPEC_REC_BEHAVI | SPEC_REC_BEHAVI_C | No | No | No |  |
| 8 | SPEC_RECV_BEH_EX_C | ZC_SPEC_RECV_BEH_E | SPEC_RECV_BEH_E_C | No | No | No |  |
| 9 | DFLT_TEST_ID | PROTOCOL_DB_MAIN | PROTOCOL_ID | Unknown | No | No |  |
| 9 | DFLT_TEST_ID | TEST_MSTR_DB_MAIN | TEST_ID | Unknown | No | No |  |
| 9 | DFLT_TEST_ID | ZC_QC_TEST_CAT_ID | QC_TEST_CAT_ID_C | Unknown | Unknown | No |  |
| 10 | DFLT_TEST_METHOD_ID | METHOD_DB_MAIN | METHOD_ID | Unknown | No | No |  |
| 10 | DFLT_TEST_METHOD_ID | METHOD_INFO | METHOD_ID | Unknown | No | No |  |
| 11 | DFLT_QC_PRI_C | ZC_SPEC_TEST_PRI | SPEC_TEST_PRI_C | No | No | No |  |
| 12 | DFLT_PACKNG_LIST_ID | BAT_MSTR_DB_MAIN | BATCH_TYPE_ID | Unknown | No | No |  |
| 12 | DFLT_PACKNG_LIST_ID | BAT_MSTR_OVERTIME | BATCH_TYPE_ID | Unknown | No | No |  |
| 14 | ADDON_RPT_SET_ID | REPORT_INFO | REPORT_INFO_ID | No | No | No |  |
| 14 | ADDON_RPT_SET_ID | V_REPORT_SETTINGS_FACT | REPORT_INFO_ID | Unknown | Unknown | No |  |
| 17 | LLB_LAB_ID | CLARITY_LLB | RESULTING_LAB_ID | Unknown | No | No |  |
| 20 | DFLT_HLD_TO_APPLY_C | ZC_HLD_TO_APPLY | HLD_TO_APPLY_C | No | No | No |  |

_(82 total; showing first 30)_
