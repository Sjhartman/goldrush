# CLARITY_EMP

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=CLARITY_EMP

## Description

This table contains high-level information about user records from the User master file.

**Primary table** in this group (174 cols). Overflow siblings joined on shared key: CLARITY_EMP_2 (100 cols), CLARITY_EMP_3 (33 cols), CLARITY_EMP_4 (22 cols). Prefer this table for most queries.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | EMP |
| Release Version | EPIC 2000 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| USER_ID | VARCHAR (18) | The unique ID assigned to the user record. This ID may be encrypted. |
| NAME | VARCHAR (160) | The name of the user record. This name may be hidden. |
| PROV_ID | VARCHAR (18) | The unique ID of the provider record that is linked to this user record if the user is a clinical system provider. This ID may be encrypted. |
| EPIC_EMP_ID | VARCHAR (18) | The unique ID assigned to the user record. This column will be omitted from public views of the CLARITY_EMP table.  NOTE: This will be the same as CLARITY_EMP.USER_ID unless encryption is turned on for your facility.  If encryption is enabled, this item too will be hidden from public view. |
| MC_DEPARTMENT_ID | NUMERIC (18,0) | The unique ID of the department.  This is the user's sign-on department if the user only has manage care system security. |
| CR_USER_NAME | VARCHAR (254) | The user name for criteria review software. |
| PB_DEF_CLS_NM *(deprecated)* | VARCHAR (40) | This column is deprecated. The column previously extracted the premium billing default security classification record name. In order to avoid data consistency issues, use PRM_BIL_DFLT_ECL_ID to link to CLARITY_ECL instead. |
| CONF_SEC_CLS_NM *(deprecated)* | VARCHAR (40) | This column is deprecated. The column previously extracted the confidentiality default security classification record name. In order to avoid data consistency issues, use CONF_DFLT_ECL_ID to link to CLARITY_ECL instead. |
| DFLT_SEC_CLASS_C | VARCHAR (18) | This is the user's billing system default security class. |
| EPR_SEC_CLASS_C | VARCHAR (18) | This is the user's enterprise registration system default security class. |
| MR_CLASS_C | VARCHAR (18) | In table CLARITY_EMP, the column MR_CLASS_C (EMP/17000) will be deprecated in the near future.  This column has been replaced by column MR_DFLT_SEC_CLS_ID (EMP/17000) in the table CLARITY_EMP_2.   To look up the soon-to-be-deprecated column's value, join column CLARITY_EMP.USER_ID to table CLARITY_EMP_2 column USER_ID and use the MR_DFLT_SEC_CLS_ID value.    The clinical system default security class category number for the user. |
| USER_CONFIG_ID | VARCHAR (18) | This is the user's profile for configuring clinical system. Information in this profile overrides the settings for profiles defined at other levels. |
| MC_DEF_SEC_LEVEL_C *(deprecated)* | VARCHAR (18) |  |
| RFL_DEF_CLS_C *(deprecated)* | VARCHAR (18) | *** Deprecated *** The column RFL_DEF_CLS_C (RFL) has been deprecated because the item definition for I EMP 19500 has been changed from a category updated item to a networked item.  This is the user's Referral default security class. |
| IB_SEC_CLASS_ID | VARCHAR (18) | This is the user's In Basket security class. |
| SHARED_SEC_CL_ID | VARCHAR (18) | The unique ID (.1 item) of the Shared security class record. This class controls access to certain provider-related functions, such as editing provider records "on the fly" across system applications and applies to both the Text and Hyperspace interfaces. This column is frequently used to link to the CLARITY_ECL table. |
| CUST_SVC_DEF_CLS | VARCHAR (18) | The unique ID (.1 item) of the Customer Relationship Management security class record. This column is frequently used to link to the CLARITY_ECL table. |
| DEL_STATUS_C | INTEGER |  |
| USER_NAME_EXT | VARCHAR (160) | The user's name for the user record. |
| USER_STATUS_C | INTEGER |  |
| ADDRESS | VARCHAR (254) | The user's street address. |
| CITY | VARCHAR (60) | The user's city/location. |
| STATE_PROVINCE | VARCHAR (50) | The user's state/province. |
| ZIP_CODE | VARCHAR (50) | The user's ZIP Code. |
| PHONE | VARCHAR (50) | The user's phone number. |
| LAST_PW_UPDATE | DATETIME | The date of the most recent user password change. |
| SQL_ECL_ID | VARCHAR (18) | The user's SQL security class ID. |
| ES_AUTH_ALLSA_YN | VARCHAR (1) |  |
| CAD0_OTH_DEP_C | No | This column is deprecated and does not extract any data. The item it previously extracted is no longer used. To determine the default scheduling security class, use the column CAD_OTH_DEP_ECL_ID. |
| CAD0_DEPARTMENT_ID *(deprecated)* | NUMERIC (18,0) |  |
| CAD1_OTH_DEP_C | No | This column is deprecated and does not extract any data. To determine the default scheduling security class, use the column CAD_OTH_DEP_ECL_ID. |
| CAD1_DEPARTMENT_ID | NUMERIC (18,0) | The scheduling system default logon department ID. |
| ES_DSKTP_ACSS_YN | VARCHAR (1) |  |
| ES_RPT_SEC_PNT_C | INTEGER |  |
| CT_DFLT_CLS_C | VARCHAR (18) | The column CT_DEF_CLS_ID from the CLARITY_EMP_2 table should be used instead of this column. This column will be deprecated in a future release.  The unique ID (.1 item) of the default Chart Tracking security class record. This column is frequently used to link to the CLARITY_ECL table. |
| CT_DSKTP_ACSS_YN *(deprecated)* | VARCHAR (1) |  |
| AR_DFLT_FACLTY_C | INTEGER |  |
| AR_DF_SERV_AREA_ID | NUMERIC (18,0) | The billing system default sign-on service area ID. |
| AR_DFLT_LOC_ID | NUMERIC (18,0) | The billing system default sign-on location ID. |
| AR_DEPARTMENT_ID | NUMERIC (18,0) | The billing system default sign-on department ID. |
| DFLT_ECL_ID | VARCHAR (18) | The user's default database security class ID. |
| MR_RESTR_ACCS_YN | VARCHAR (1) |  |
| ENBL_RSLT_REV_YN *(deprecated)* | VARCHAR (1) |  |
| PRF_LST_PX_C | INTEGER |  |
| PRF_LST_COMDX_C | INTEGER |  |
| PRF_LST_MEDS_C | INTEGER |  |
| PRF_LST_RFV_C | INTEGER |  |
| MPI_SEC_CLS_C | VARCHAR (18) | ***In table CLARITY_EMP, the column MPI_SEC_CLS_C will be deprecated in a future release.*** This column will be replaced by column MPI_SEC_CLS_ECL_ID in table CLARITY_EMP_2.  To look up the user's default Identity security class, join column MPI_SEC_CLS_ECL_ID in table CLARITY_EMP_2 to table CLARITY_ECL column ECL_ID. |
| MAIL_SYSTEM_C | INTEGER |  |
| LGIN_DEPARTMENT_ID | NUMERIC (18,0) | The ID of the default Hyperspace login department for this user. |
| EL_ACCS_C | INTEGER |  |
| EW_USER_CLS_C | VARCHAR (18) | In table CLARITY_EMP, the column EW_USER_CLS_C (EMP/22500) has been deprecated.  This column has been replaced by column EW_USER_CLASS_ID (EMP/22500) in the table CLARITY_EMP_2.  To look up the deprecated column's value (the ECL ID) after the Clarity Compass upgrade, use the column EW_USER_CLASS_ID in the table CLARITY_EMP_2. |
| CR_DFLT_ECL_ID | VARCHAR (18) | The unique ID (.1 item) of the default Clarity security class record. This column is frequently used to link to the CLARITY_ECL table. |
| APCLM_DEF_ECL_ID | VARCHAR (18) | The unique ID (.1 item) of the Accounts Payable Claims security class record. This column is frequently used to link to the CLARITY_ECL table. |
| CASE_DEF_ECL_ID | VARCHAR (18) | The unique ID (.1 item) of the Case Management security class record. This column is frequently used to link to the CLARITY_ECL table. |
| AP_DEF_ECL_ID | VARCHAR (18) | The unique ID (.1 item) of the Accounts Payable security class record. This column is frequently used to link to the CLARITY_ECL table. |
| CAPRR_DEF_ECL_ID | VARCHAR (18) | The unique ID (.1 item) of the Capitation Receipt and Reconciliation security class record. This column is frequently used to link to the CLARITY_ECL table. |
| CAPPAY_DEF_ECL_ID | VARCHAR (18) | The unique ID (.1 item) of the Capitation Payment security class record. This column is frequently used to link to the CLARITY_ECL table. |
| LAST_ACCS_DATETIME | DATETIME (Local) | The last date and time the user record was accessed. NOTE: Converted from an instant item to a human-readable date and time. |
| DFLT_LOC_YN | VARCHAR (1) |  |
| RESTR_ACCS_REV_YN *(deprecated)* | VARCHAR (1) |  |
| LAST_USER_ID *(deprecated)* | VARCHAR (18) | The ID of the last editor of the user record. This column is now deprecated since the item is not filled in when the user is edited. |
| MILLIMAN_USA_UNAME | VARCHAR (255) | The username for CareGuide QI software. |
| MR_LOGON_DEPT_ID | EMP | The user's login department. Depending on system configuration, this information can be retrieved from different places. If Cadence is licensed, the information is retrieved from Cadence Logon Department (I EMP 5115). Otherwise, the system first checks Last Login Department (I EMP 20670) if the user's primary role is configured to use their last login department as their default login department. If this item doesn't have a value, or if the user's last login department isn't their default login department, the system checks Hyperspace Login Department (I EMP 20660). If Hyperspace Login Department doesn't have a value, then the system checks MR Facility Department (I EMP 17330). |
| CAD_PRV_OTH_DPT_YN | VARCHAR (254) |  |
| CAD_GUI_BKDROP_YN *(deprecated)* | VARCHAR (254) |  |
| CAD_GUI_FRM_SZE_C | INTEGER |  |
| IS_DFLT_DEPT_YN | VARCHAR (254) |  |
| DISPLAY_ERR_RPT_C | VARCHAR (254) |  |
| IS_COLLECTOR_YN | VARCHAR (254) |  |
| USER_ALIAS | VARCHAR (254) | This is an alternative identification for this user. |
| CM_PHY_OWNER_ID | VARCHAR (25) | ID of the physical deployment owner for this record.  Physical owners will be where the data is hosted, either on the cross-over server or the owner deployment. |
| CM_LOG_OWNER_ID | VARCHAR (25) | ID of the logical deployment owner for this record.  Logical owners show the deployment where the record was created but doesn't represent if the record is a part of version skew. |
| SYSTEM_LOGIN | VARCHAR (254) | This is the user's Operating System login. |
| RPT_GRP_ONE | VARCHAR (254) | This is a general report grouper item. |
| RPT_GRP_TWO | VARCHAR (254) | This is a general report grouper item. |
| RPT_GRP_THREE | VARCHAR (254) | This is a general report grouper item. |
| LAB_DEFAULT_ECL_ID | VARCHAR (18) | The user's default laboratory security class. |
| LAB_WORKBENCH_YN | VARCHAR (254) |  |
| SUPERVISOR_YN *(deprecated)* | VARCHAR (1) |  |
| LICENSE_USRTYPE_C | INTEGER |  |
| EW_ACCS_C | INTEGER |  |
| EL_ACCS_PP_GRP_YN | VARCHAR (1) |  |
| EL_NOTFY_EMAIL_YN | VARCHAR (1) |  |
| EL_DAYS_BTN_EMAIL | INTEGER | This item only applies to AffiliateLink.   It specifies the minimum number of days the system should wait before sending the user another e-mail.  For instance if this is set to 7, the user will not get an e-mail from the batch job notification routine until 7 days have passed since the system sent the last e-mail.  Valid values for this item are from 1 to 30.  This item is only used if the system is configured to run the batch template EPICLINK - EMAIL NOTIFICATIONS FOR NEW ACCESSES (E1A 10020) or a copy of it. |
| EL_LAST_EMAIL_DT | DATETIME | This item only applies to AffiliateLink. It stores the date of the external email that was last sent to this user. |
| EL_GRP_NOTIFY_YN | VARCHAR (1) |  |
| EL_USR_AFFECT_YN | VARCHAR (1) |  |
| EL_TRMS_ACPT_INST | DATETIME (Local) | This item only applies to AffiliateLink/PlanLink. It stores the instant the user last accepted the terms and conditions.   The table CL_EMP_TERMS_AUDIT stores an audit trail of all past instances when the user accepted the terms. |
| EL_ACCS_PROG_PNT | VARCHAR (254) | This item applies only to AffiliateLink/PlanLink. It stores the programming point code that determines whether the user has access to a specific patient. |
| WEB_EXT_IDENTIFIER | VARCHAR (254) | This applies to the web applications (EpicWeb, AffiliateLink, PlanLink and OutReach).  It is used in Single Sign on (SSO) and stores the external identifier of this user in the other system. This value, if specified, should be unique across users. |
| ME_PORTAL_DEF_ID | VARCHAR (184) | The user's Radar portal definition ID that is used to name the corresponding XML on the web server.   Set programmatically when the user logs in to Radar for the first time. |
| ST_PASTE_C | INTEGER |  |
| ME_ADMIN_FLAG_YN | VARCHAR (1) |  |
| ME_ACCESS_C | INTEGER |  |
| FORCE_PWD_CHANGE_YN | VARCHAR (1) |  |
| OR_SYSTEM_CLASS_ID | VARCHAR (18) | The user's security class record (ECL) for OpTime security. |
| RX_SEC_CLASS_ID | VARCHAR (18) | The user's security class record (ECL) for Willow security. |
| OR_DEF_LOC_SECUR_ID | VARCHAR (18) | This is the OpTime Security of the user in their default Security Location. |
| INP_EMR_SEC_CLS_ID | VARCHAR (18) | The user's Inpatient security class that controls access to various Inpatient functionalities. |
| DFLT_ACCT_WQ_ID *(deprecated)* | NUMERIC (18,0) | Specifies the per user default account workqueue that an account will be loaded into when the LaunchEAR command is used over the Resolute Account Launch COM Interface. |
| SP_FAC_YN | VARCHAR (1) |  |
| SP_AFF_YN | VARCHAR (1) |  |
| SP_OUT_YN | VARCHAR (1) |  |
| HB_DFLT_LGN_DEP_ID | NUMERIC (18,0) | The unique ID for the hospital billing default text login department. This column is frequently used to link to the CLARITY_DEP table. |
| CDT_DFLT_ECL_ID | VARCHAR (18) | The unique ID (.1 item) of the Chart Deficiency Tracking security class record. This column is frequently used to link to the CLARITY_ECL table. |
| ROI_DFLT_ECL_ID | VARCHAR (18) | The unique ID (.1 item) of the default Release of Information security class record. This column is frequently used to link to the CLARITY_ECL table. |
| NTCM_DFLT_ECL_ID | VARCHAR (18) | The unique ID (.1 item) of the default Nurse Triage/Call Management security class record. This column is frequently used to link to the CLARITY_ECL table. |
| HH_DFLT_ECL_ID | VARCHAR (18) | The unique ID (.1 item) of the default Home Health security class record. This column is frequently used to link to the CLARITY_ECL table. |
| ER_DFLT_ECL_ID | VARCHAR (18) | The unique ID (.1 item) of the default ASAP security class record. This column is frequently used to link to the CLARITY_ECL table. |
| LAB_DFLT_TST_ECL_ID | VARCHAR (18) | The unique ID (.1 item) of the default Beaker Test-Level security class record that is used when a user attempts to take action on a test. This security class can be overridden by making use of workbench security. This column is frequently used to link to the CLARITY_ECL table. |
| PEAR_DFLT_ECL_ID | VARCHAR (18) | The unique ID (.1 item) of the default Procedural Application security class record. This column is frequently used to link to the CLARITY_ECL table. |
| OB_DFLT_ECL_ID | VARCHAR (18) | The unique ID (.1 item) of the default Stork security class record. This column is frequently used to link to the CLARITY_ECL table. |
| CHSYNC_DFLT_ECL_ID | VARCHAR (18) | The unique ID (.1 item) of the default Chart Sync security class record. This column is frequently used to link to the CLARITY_ECL table. |
| CDA_DFLT_ECL_ID | VARCHAR (18) | The unique ID (.1 item) of the Cross Deployment Access security class record. This column is frequently used to link to the CLARITY_ECL table. |
| CTM_DFLT_ECL_ID | VARCHAR (18) | The unique ID (.1 item) of the default Contract Management security class record. This column is frequently used to link to the CLARITY_ECL table. |
| CE_DFLT_ECL_ID | VARCHAR (18) | The unique ID (.1 item) of the default Care Everywhere security class record. This column is frequently used to link to the CLARITY_ECL table. |
| HNDHLD_DFLT_ECL_ID | VARCHAR (18) | The unique ID (.1 item) of the default Rover security class record. This column is frequently used to link to the CLARITY_ECL table. |
| PRM_BIL_DFLT_ECL_ID | VARCHAR (18) | The unique ID (.1 item) of the default Premium Billing security class record. Premium Billing is part of the health plan operations application. This column is frequently used to link to the CLARITY_ECL table. |
| CONF_DFLT_ECL_ID | VARCHAR (18) | The unique ID (.1 item) of the default Confidentiality security class record. This functionality is part of the Health Plan Operations application. This column is frequently used to link to the CLARITY_ECL table. |
| MR_INIT_PRAC_C | VARCHAR (66) |  |
| ADT_DFLT_ECL_ID | VARCHAR (18) | The unique ID (.1 item) of the default ADT security class record. This column is frequently used to link to the CLARITY_ECL table. |
| EDI_DFLT_ECL_ID | VARCHAR (18) | The unique ID (.1 item) of the default EDI security class record. This column is frequently used to link to the CLARITY_ECL table. |
| HB_DFLT_ECL_ID | VARCHAR (18) | The unique ID (.1 item) of the default Hospital Billing security class record. This column is frequently used to link to the CLARITY_ECL table. |
| RIS_DFLT_ECL_ID | VARCHAR (18) | The unique ID (.1 item) of the default Radiant security class record. This column is frequently used to link to the CLARITY_ECL table. |
| CARD_DFLT_ECL_ID | VARCHAR (18) | The unique ID (.1 item) of the default cardiology security class record. This column is frequently used to link to the CLARITY_ECL table. |
| EMFI_DFLT_ECL_ID | VARCHAR (18) | The unique ID (.1 item) of the default EMFI security class record. This column is frequently used to link to the CLARITY_ECL table. |
| DC_DFLT_ECL_ID | VARCHAR (18) | The unique ID (.1 item) of the default Data Courier security class record. This column is frequently used to link to the CLARITY_ECL table. |
| LOGIN_BLOCKED_C | INTEGER |  |
| EMP_RECORD_TYPE_C | INTEGER |  |
| LNK_SEC_TEMPLT_ID | VARCHAR (18) | The unique ID of the user record that is the linked template for this record. Linked templates populate data in a user record and when updates are made to a template the linked user records are updated also.  This column is frequently used to link to the CLARITY_EMP table. |
| LAB_BIL_DFLT_ECL_ID | VARCHAR (18) | The unique ID (.1 item) of the default Beaker Billing security class record. This column is frequently used to link to the CLARITY_ECL table. |
| LOGIN_BLOCKED_C_CMT | VARCHAR (254) |  |
| PPL_TYPE_C *(deprecated)* | INTEGER |  |
| CM_DFLT_SPT_USER_ID | VARCHAR (18) | The unique ID of the support staff user that will default as a recipient for support staff routing in the communication management module. |
| CM_DFLT_SPT_POOL_ID | NUMERIC (18,0) | The unique ID of the support pool (HIP record) that will default as a recipient for support staff routing in the communication management module. |
| CM_DFLT_SPT_FREETXT | VARCHAR (254) | The display name of the support staff user to whom the communication is routed when route to support staff is selected from communication management. This is a free text entry. |
| MR_ADMIN_VIEW_ONLY *(deprecated)* | INTEGER |  |
| SYS_OVERV_YN | VARCHAR (1) |  |
| FOCUS_DEPT_FIELD_YN | VARCHAR (1) |  |
| DFLT_SCHED_VIEW_C | INTEGER |  |
| OR_DEF_CASE_LOC_ID | NUMERIC (18,0) | The unique ID of the case request default OR location. |
| OR_DEF_CASE_SVC_C | VARCHAR (66) |  |
| OR_DEF_CASE_SRGN_ID | VARCHAR (18) | The unique ID of the case request default primary surgeon. |
| USR_LOG_OR_SCRPT_ID | VARCHAR (18) | The unique ID of the OR log script preference list. |
| RFL_REP_SECPT_C | INTEGER |  |
| LAB_LAST_DRAWTYPE_C | INTEGER |  |
| SHOW_UNREL_RES_YN | VARCHAR (1) |  |
| SHOW_ERR_RPT_C | INTEGER |  |
| PTSRCH_DEF_FAC_YN *(deprecated)* | VARCHAR (1) |  |
| IS_SUP_PROV_REQ_C | INTEGER |  |
| FAC_FILTER_TYPE_C | INTEGER |  |
| LAB_RESCREEN_FACTOR | NUMERIC (6,2) | This is the selection factor for determining rescreens. The factor is a percentage of slides to randomly select. |
| IGNORE_LIGHT_M_YN | VARCHAR (1) |  |
| HIM_REP_SEC_PT_C | INTEGER |  |
| HIM_ADMIN_ACCESS_YN | VARCHAR (1) |  |
| PREF_LIST_SET_ORX_C | INTEGER |  |
| DFLT_PROB_PRI_C | INTEGER |  |
| PROB_PRI_OFF_PREF_C | INTEGER |  |
| PROB_PRI_ON_PREF_C | INTEGER |  |
| PROB_LST_PREF_L_ID | NUMERIC (18,0) | The diagnosis preference list for the problem list. |
| USR_SORT_PROB_YN | VARCHAR (1) |  |
| LAST_PATIENT_LIST | VARCHAR (254) | The last patient list the user viewed. |
| IP_UNIQUE_ID | VARCHAR (192) | The user's initials or other documentation identifier. This is displayed instead of the user ID by default. This is set in User Security. Choose your user, select ?Inpatient EMR? from the list on the left, and enter your initials in the ?Inpatient documentation identifier:? field. |
| IPEMR_DEF_RESTR_YN | VARCHAR (1) |  |
| IP_DEF_RES_ACC_YN | VARCHAR (1) |  |
| IP_PATLST_DEFLST_ID | VARCHAR (18) | The default inpatient patient list to use for this employee. |
| PTSRCH_SHOW_LST_YN *(deprecated)* | VARCHAR (1) |  |
| DSB_FRM_SEC_ID | VARCHAR (18) | Dashboard Framework security class |
| EFF_FROM_DATE | DATETIME | Date account becomes active. This value behaves as a "start date" or an "effective from date." |
| EFF_TO_DATE | DATETIME | Date account ceases to be active. This value behaves as an "end date" or an "effective to date." |
| DEACTIVATE_DAYS | INTEGER | Days of inactivity after which to deactivate account. |
| CAD_OTH_DEP_ECL_ID | VARCHAR (18) | The unique ID (.1 item) of the Cadence security class record used for all other departments. This column is frequently used to link to the CLARITY_ECL table. |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| B-TREE INDEX | EIX_CLARITY_EMP_EPEMID | EPIC_EMP_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_CLARITY_EMP_PROV_ID | PROV_ID | 1 | Yes | Yes |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | USER_ID | CLARITY_EMP_2 | USER_ID | Unknown | No | No |  |
| 1 | USER_ID | CLARITY_EMP_3 | USER_ID | Unknown | No | No |  |
| 1 | USER_ID | CLARITY_EMP_4 | USER_ID | No | No | No |  |
| 1 | USER_ID | CLARITY_EMP_DEMO | USER_ID | No | No | No |  |
| 1 | USER_ID | EMP_BASIC_INFO | USER_ID | No | No | No |  |
| 1 | USER_ID | EMP_DOC_SETTINGS | USER_NUMBER_ID | No | No | No |  |
| 1 | USER_ID | F_RX_USER | USER_ID | Unknown | Unknown | No |  |
| 1 | USER_ID | IB_MESSAGE_SETTINGS | USER_ID | No | No | No |  |
| 1 | USER_ID | LOGIN_INFO | USER_NUMBER_ID | No | No | No |  |
| 1 | USER_ID | QC_RESULTS_REVIEW | USER_NUMBER_ID | No | No | No |  |
| 1 | USER_ID | USER_SIDEBAR_RPT | USER_NUMBER_ID | Unknown | No | No |  |
| 1 | USER_ID | V_CUBE_D_USER | USER_ID | Unknown | Unknown | No |  |
| 1 | USER_ID | V_CUBE_RX_USER | USER_ID | Unknown | Unknown | No |  |
| 3 | PROV_ID | CLARITY_SER | PROV_ID | Unknown | No | No |  |
| 3 | PROV_ID | CLARITY_SER_2 | PROV_ID | Unknown | No | No |  |
| 3 | PROV_ID | CLARITY_SER_3 | PROV_ID | Unknown | No | No |  |
| 3 | PROV_ID | CLARITY_SER_4 | PROV_ID | No | No | No |  |
| 3 | PROV_ID | CLARITY_SER_MYC | PROV_ID | Unknown | No | No |  |
| 3 | PROV_ID | D_PROV_PRIMARY_HIERARCHY | PROV_ID | Unknown | Unknown | No |  |
| 3 | PROV_ID | ED_SER_SETTINGS | PROV_ID | Unknown | No | No |  |
| 3 | PROV_ID | EXT_CAL_PROV_CONFIG | PROV_ID | No | No | No |  |
| 3 | PROV_ID | OR_SER_EQUIPMENT | PROV_ID | Unknown | No | No |  |
| 3 | PROV_ID | OR_SER_ROOM | PROV_ID | Unknown | No | No |  |
| 3 | PROV_ID | PROV_BATCH_LTR_GEN | PROV_ID | Unknown | No | No |  |
| 3 | PROV_ID | PROV_GROUP | PROV_ID | No | No | No |  |
| 3 | PROV_ID | V_CUBE_D_PROVIDER | PROVIDER_ID | Unknown | Unknown | No |  |
| 4 | EPIC_EMP_ID | CLARITY_EMP | USER_ID | Unknown | No | No |  |
| 4 | EPIC_EMP_ID | CLARITY_EMP_2 | USER_ID | Unknown | No | No |  |
| 4 | EPIC_EMP_ID | CLARITY_EMP_3 | USER_ID | Unknown | No | No |  |
| 4 | EPIC_EMP_ID | CLARITY_EMP_4 | USER_ID | No | No | No |  |

_(537 total; showing first 30)_
