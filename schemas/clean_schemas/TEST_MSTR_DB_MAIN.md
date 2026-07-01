# TEST_MSTR_DB_MAIN

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=TEST_MSTR_DB_MAIN

## Description

The TEST_MSTR_DB_MAIN table stores general settings for laboratory test records.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | FULL |
| Load Frequency | WEEKLY - FULL |
| Chronicles INI | OVT |
| Release Version | FALL 2004 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| TEST_ID | VARCHAR (18) | The unique ID of the test record. |
| TEST_NAME | VARCHAR (254) | The name of the test record. |
| TEST_ABBR | VARCHAR (254) | The abbreviation of the test record. |
| TEST_STATUS_C | INTEGER |  |
| TEST_SUSC_YN | VARCHAR (254) |  |
| TEST_NOADD_RTYPE_ID | VARCHAR (18) | The unique ID of the standard result type associated with each test. |
| TEST_NOADD_GW_RTYP | VARCHAR (18) | The unique ID of the general workcard result type associated with each test. |
| TEST_NOADD_OW_RTYP | VARCHAR (18) | The unique ID of the organism workcard result type associated with each test. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| USER_AUTH_YN | VARCHAR (1) |  |
| REPORT_NAME | VARCHAR (254) | The report name of the test record. |
| RPT_PER_100_CELL_YN | VARCHAR (1) |  |
| SCALE_FACTOR_WBCS | INTEGER | Scale factor for calculated WBCs. A default scale factor of 1000 will be assumed if this field is left blank. |
| DIFF_COUNT_CELL *(deprecated)* | INTEGER | Stores the number of cells counted after which an event will be triggered. If left empty then a default value of 100 will be used. The event is defined in OVT-51585. This column is being deprecated in 2014. The value will now be a part of OVT-51593 |
| RPT_ADIFF_ON_PRL_YN | VARCHAR (1) |  |
| RESULT_CHECKING_ID | NUMERIC (18,0) | Links to result checking setup for this test |
| PLACE_SETUP_BENC_YN | VARCHAR (1) |  |
| RES_ENTRY_SBENCH_YN | VARCHAR (1) |  |
| EXCL_SB_TSKS_CMP_YN | VARCHAR (1) |  |
| ALLOW_ADDL_TSK_YN | VARCHAR (1) |  |
| AUTO_VER_DIS_YN | VARCHAR (1) |  |
| AUTO_VER_MANL_YN | VARCHAR (1) |  |
| AUTO_VER_USER_ID | VARCHAR (18) | The unique ID of the user that is used when auto verifying results. |
| AUTO_VER_PR_RULE_ID | VARCHAR (18) | A rule to determine if a result should be auto-prelim verified. |
| AUTO_VER_FN_RULE_ID | VARCHAR (18) | A rule to determine if a result should be auto-final verified. |
| QC_AUTO_VER_DIS_YN | VARCHAR (1) |  |
| QC_AUTO_VER_MANL_YN | VARCHAR (1) |  |
| QC_AUTO_VER_USER_ID | VARCHAR (18) | The unique ID of the user that is used when auto verifying QC results. |
| QC_AUTO_VER_RULE_ID | VARCHAR (18) | A rule to determine if a QC result should be auto verified. |
| MAIN_PC_HEM_TITLE_C | INTEGER |  |
| TEST_REC_TYPE_C | INTEGER |  |
| AUTO_RES_START_C | INTEGER |  |
| PRVNT_EDIT_RESUL_YN | VARCHAR (1) |  |
| PRV_RSLT_USR_VRFY_C | INTEGER |  |
| AP_PROTOCOL_ID *(deprecated)* | VARCHAR (18) | In table TEST_MSTR_DB_MAIN, the column AP_PROTOCOL_ID (OVT/51001) has been deprecated.  This column has been replaced by column DFLT_PROTOCOL_ID (OVT/51002) in the table DFLT_PROTCL_SET.  To look up the deprecated column's value after the Clarity Compass upgrade, use the column DFLT_PROTOCOL_ID in table DFLT_PROTCL_SET to get the AP_PROTOCOL_ID value. |
| SCI_NOTATN_ORD_MAG | INTEGER | The minimum order of magnitude for displaying culture quantity in scientific notation for a test with a result type that includes a microbiology culture. |
| STAIN_BILL_DEF_YN | VARCHAR (1) |  |
| NOADD_STATUS_C | INTEGER |  |
| RECORD_DELETED_C | INTEGER |  |
| BILLABLE_PX_LPP_ID | NUMERIC (18,0) | The ID of the programming point for primary procedures. |
| DEFAULT_TEST_MAC_ID | VARCHAR (18) | The ID of the default Machine/Interface for this test. |
| ORG_WKCD_ACTION_ID | NUMERIC (18,0) | The ID of the initial workcard action to use when starting an organism workcard. |
| DISABLE_RRRECP_YN | VARCHAR (1) |  |
| TEST_RR_RULE_ID | VARCHAR (18) | Stores the rule which would be evaluated to determine if the test is to be reported or not. |
| DX_TO_USE_C | INTEGER |  |
| PREVENT_TEMPLATE_YN | VARCHAR (1) |  |
| ENT_REPLCTN_C | INTEGER |  |
| REPORT_AUTO_DIFF_YN | VARCHAR (1) |  |
| ALLOW_PART_AUTO_VER_YN | VARCHAR (1) |  |
| AUTO_VER_PR_COMP_RULE_ID | VARCHAR (18) | A rule to determine if a component should be auto prelim verified. |
| AUTO_VER_FN_COMP_RULE_ID | VARCHAR (18) | A rule to determine if a component should be auto final verified. |
| DISPLAY_NAME | 70 | Display name for the test. Extracts the report name if populated, otherwise the record name. |
| CRIT_PUSH_PRELIM_RULE_ID | VARCHAR (18) | Prelim verification rule to qualify a result as needing critical result follow-up and push notification. |
| CRIT_PUSH_PRELIM_UNCALL_YN | VARCHAR (1) |  |
| CRIT_PUSH_PRELIM_DISABLE_YN | VARCHAR (1) |  |
| CRIT_PUSH_FINAL_RULE_ID | VARCHAR (18) | Final verification rule to qualify a result as needing critical result follow-up and push notification. |
| CRIT_PUSH_FINAL_UNCALL_YN | VARCHAR (1) |  |
| CRIT_PUSH_FINAL_DISABLE_YN | VARCHAR (1) |  |
| RESULT_CHANGE_CMT_SUPPRESS_YN | VARCHAR (1) |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | TEST_ID | PROTOCOL_DB_MAIN | PROTOCOL_ID | Unknown | No | No |  |
| 1 | TEST_ID | ZC_QC_TEST_CAT_ID | QC_TEST_CAT_ID_C | Unknown | Unknown | No |  |
| 4 | TEST_STATUS_C | ZC_TEST_STATUS | TEST_STATUS_C | No | No | No |  |
| 6 | TEST_NOADD_RTYPE_ID | RTYPE_DB_MAIN | RESULT_TYPE_ID | Unknown | No | No |  |
| 6 | TEST_NOADD_RTYPE_ID | RTYPE_OT_MISC | RESULT_TYPE_ID | Unknown | No | No |  |
| 7 | TEST_NOADD_GW_RTYP | RTYPE_DB_MAIN | RESULT_TYPE_ID | Unknown | No | No |  |
| 7 | TEST_NOADD_GW_RTYP | RTYPE_OT_MISC | RESULT_TYPE_ID | Unknown | No | No |  |
| 8 | TEST_NOADD_OW_RTYP | RTYPE_DB_MAIN | RESULT_TYPE_ID | Unknown | No | No |  |
| 8 | TEST_NOADD_OW_RTYP | RTYPE_OT_MISC | RESULT_TYPE_ID | Unknown | No | No |  |
| 9 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 9 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 9 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 10 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 10 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 10 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 17 | RESULT_CHECKING_ID | LAB_TRE_NOADD | RECORD_ID | Unknown | No | No |  |
| 24 | AUTO_VER_USER_ID | CLARITY_EMP | USER_ID | Unknown | No | No |  |
| 24 | AUTO_VER_USER_ID | CLARITY_EMP_2 | USER_ID | Unknown | No | No |  |
| 24 | AUTO_VER_USER_ID | CLARITY_EMP_3 | USER_ID | Unknown | No | No |  |
| 24 | AUTO_VER_USER_ID | CLARITY_EMP_4 | USER_ID | No | No | No |  |
| 24 | AUTO_VER_USER_ID | CLARITY_EMP_DEMO | USER_ID | No | No | No |  |
| 24 | AUTO_VER_USER_ID | EMP_BASIC_INFO | USER_ID | No | No | No |  |
| 24 | AUTO_VER_USER_ID | EMP_DOC_SETTINGS | USER_NUMBER_ID | No | No | No |  |
| 24 | AUTO_VER_USER_ID | F_RX_USER | USER_ID | Unknown | Unknown | No |  |
| 24 | AUTO_VER_USER_ID | IB_MESSAGE_SETTINGS | USER_ID | No | No | No |  |
| 24 | AUTO_VER_USER_ID | LOGIN_INFO | USER_NUMBER_ID | No | No | No |  |
| 24 | AUTO_VER_USER_ID | QC_RESULTS_REVIEW | USER_NUMBER_ID | No | No | No |  |
| 24 | AUTO_VER_USER_ID | USER_SIDEBAR_RPT | USER_NUMBER_ID | Unknown | No | No |  |
| 24 | AUTO_VER_USER_ID | V_CUBE_D_USER | USER_ID | Unknown | Unknown | No |  |
| 24 | AUTO_VER_USER_ID | V_CUBE_RX_USER | USER_ID | Unknown | Unknown | No |  |

_(93 total; showing first 30)_
