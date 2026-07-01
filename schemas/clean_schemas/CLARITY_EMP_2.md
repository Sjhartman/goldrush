# CLARITY_EMP_2

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=CLARITY_EMP_2

## Description

This table extends CLARITY_EMP, which contains high-level information about user records from the User master file.

**Overflow table** for CLARITY_EMP (174 cols). Contains additional columns for the same records — join on the shared primary key column.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | EMP |
| Release Version | Summer 2009 |
| May contain EHI? | No |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| USER_ID | VARCHAR (18) | The unique ID associated with the user record for this row. This column is frequently used to link to the CLARITY_EMP table. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| BTLR_CONFIG_C | INTEGER |  |
| BTLR_SORTING_C | INTEGER |  |
| OVR_DSB_FROM_ROL_YN | VARCHAR (1) |  |
| EW_PAT_SEL_PREF_C | INTEGER |  |
| WEB_PT_HEADER_DEF | VARCHAR (254) | Contains the user's patient header. |
| DFLT_MAIN_MENU | VARCHAR (254) | Contains the main menu that opens by default for the user. |
| DFLT_HOME_MENU | VARCHAR (254) | Contains the home menu that opens by default for the user. |
| DFLT_HOME_SUBMENU | VARCHAR (254) | Contains the home submenu that opens by default for the user. |
| WEB_INPAT_DISP_C_ID *(deprecated)* | VARCHAR (18) | *** Deprecated *** In table CLARITY_EMP_2, the column WEB_INPAT_DISP_C_ID (EMP/22700) has been deprecated.  The deprecated column's content/data is no longer available since it is no longer populated in Chronicles. |
| ENCOUNTER_TERM_C | INTEGER |  |
| DFLT_ENC_TAB_C | INTEGER |  |
| EVT_MON_PAT_PROF_ID *(deprecated)* | NUMERIC (18,0) | Contains the Event Monitor profile that is assigned to new patients by default. |
| EVT_MON_NEWPAT_YN *(deprecated)* | VARCHAR (1) |  |
| ED_WORK_LOG_YN *(deprecated)* | VARCHAR (1) |  |
| INTERCONNECT_ADM_YN | VARCHAR (1) |  |
| LAST_LOGIN_DEPT_ID | NUMERIC (18,0) | The column extracts the last department logged into by this user. |
| BCA_SEC_CL_ID | VARCHAR (18) | Security class to use for BCA web data entry. |
| OUTREACH_SUBMIT_ID | NUMERIC (18,0) | Specifies the submitter record associated with this user. This setting is required for the user to access OutReach. |
| OUTR_SKIP_MSG_YN | VARCHAR (1) |  |
| PROV_AT_LOGIN_OPT_C | INTEGER |  |
| USER_DICT_PATH | VARCHAR (254) | The filepath for the user's dictionary. |
| DFLT_SUP_PROV_ID | VARCHAR (18) | The default supervising provider used for EpicCare order entry. |
| DFLT_SUP_PROV_C | VARCHAR (66) |  |
| DFLT_SUP_PROV_DT | DATETIME | This date is used when defaulting of supervisor and type of supervision   during order entry in Epiccare.  If the default was not entered the   same day as the use, then the default items 17445, 17446 are considered   blank.  This forces user to enter new defaults each day. |
| LET_TMPLT_DFLT_TAB | INTEGER | Stores 1 if the Favorites tab or 2 if the All tab is the default tab in the letter templates section of the patient letters activity when this user opens the letters activity for a patient. |
| PREF_LIST_SET_DX_C | INTEGER |  |
| HAS_USER_PRF_LIS_YN | VARCHAR (1) |  |
| MC_CLM_AUTH_LIMIT | NUMERIC (18,2) | Maximum auhorized amount for the claims examiner. |
| MC_INIT_FACILITY_C | INTEGER |  |
| LOGIN_MSG_INST_DTTM | DATETIME (Local) | The last instant the user accepted the login message. |
| BOE_USER_NAME | VARCHAR (100) | The user's default user name used by Hyperspace to connect to BI applications. |
| MC_CLAIM_ADJ_LIMIT | NUMERIC (18,2) | Adjustment authorized amount for claim examiner. |
| DEF_DASHBOARD_ID | NUMERIC (18,0) | The default dashboard that should launch in the dashboard activity if no user override dashboard is defined.  This item is set by administrators only. |
| DEF_DB_USR_OVR_ID | NUMERIC (18,0) | This is the user override to the default dashboard to launch.  This item is set only by end-users who have Radar security class point 9 - May Set Default Dashboard. |
| CREATE_CONTRACT_YN | VARCHAR (1) |  |
| ACSS_GLC_CONFIG_ID | NUMERIC (18,0) | The Accessibility Config being used for the user in the Accessibility at a Glance component. This column can be used to link to the ACCESS_CONFIG table. |
| ACSS_GLC_YL | NUMERIC (18,2) | The number of days in the future with no open slots at which an indicator for a provider/department should turn from green to yellow in the Accessibility at a Glance component. |
| ACSS_GLC_RL | NUMERIC (18,2) | The number of days in the future with no open slots at which an indicator for a provider/department should turn from yellow to red in the Accessibility at a Glance component. |
| HKU_SEC_CLASS_ID | VARCHAR (18) | The Haiku security class for this user. |
| UNV_LAB_NUM_DAYS | INTEGER | The user's default selection for number of days to send an unviewed test result notification message. |
| MAX_SLIDES_PER_DAY | INTEGER | The maximum number of slides that a user may review in a single day. |
| LAST_DESKTOP_QUERY | VARCHAR (254) | It stores the last SQL query run using the Desktop SQL Report Viewer utility. |
| EVENT_POOL_YN | VARCHAR (1) |  |
| FLT_PROV_ID | VARCHAR (18) | The unique ID of the provider used to filter the lab results shown in the Results Release activity. Only orders for which this provider is the authorizing provider are displayed. |
| FLT_PRV_REL_RSLT_YN | VARCHAR (1) |  |
| APPROVAL_CAT_C | INTEGER |  |
| PRIM_MANAGER_ID | VARCHAR (18) | Item 20414 in the User master file will allow manual configuration of the primary manager of a user. It will store the user ID of the primary manager. It will be configured by administrators. |
| USE_CALC_MANAGER_YN | VARCHAR (1) |  |
| AUTHEN_CONFIG_ID *(deprecated)* | NUMERIC (18,0) | In table CLARITY_EMP_2, the column AUTHEN_CONFIG_ID (EMP/48) has been deprecated.  This column has been replaced by column AUTHEN_CONFIG_ID (EMP/48) in table EMP_BASIC_INFO.  To look up the deprecated column's value after the Clarity Compass upgrade, use the column AUTHEN_CONFIG_ID in table EMP_BASIC_INFO to get the AUTHEN_CONFIG_ID value. |
| MC_RFND_WRTOFF_LMT | NUMERIC (18,2) | Maximum refund write-off amount allowed. |
| CTO_SEC_CLASS_ID | VARCHAR (18) | The Canto security class for this user. |
| RV_SEC_CLASS_ID | VARCHAR (18) | The Record Viewer security class for the user. |
| TEMPLT_OWNER_PRIM_C | INTEGER |  |
| TEMPLT_DSPLY_TITLE | VARCHAR (100) | Display title for a template record in order to present template names to end users. |
| DFLT_LNK_TEMPLT_ID | VARCHAR (18) | The unique ID of the default linkable template (from the list of available linkable templates) a user should be provisioned as. |
| MR_ADMIN_VIEW_ONLY_C | INTEGER |  |
| PROMPT_LOGIN_RSN_YN | VARCHAR (1) |  |
| DIRECT_ADDRESS_PRIM | VARCHAR (254) | The current Direct address to share with other organizations in your directory export. |
| LOGIN_BLOCKED_INST_DTTM | DATETIME (Attached) | This item stores the Chronicles instant at which a user record has been blocked from logging in. |
| PRNT_SEC_CL_ID | VARCHAR (18) | Security class for Hyperspace Printing administration. |
| BEACON_SEC_PT_ID | VARCHAR (18) | Beacon default security class for the user. |
| THERAPY_SEC_PT_ID | VARCHAR (18) | Therapy Plan default security class for the user. |
| RW_CLASS_ID | VARCHAR (18) | This column contains the default Reporting Workbench security class for the user. |
| MC_DEF_SEC_LEVEL_ID | VARCHAR (18) | Tapestry security class |
| EW_USER_CLASS_ID | VARCHAR (18) | The unique ID (.1 item) of the Web Suite security class record. This column is frequently used to link to the CLARITY_ECL table. Should replace any references to the column CLARITY_EMP.ZC_EW_USER_CLS in software versions after Epic 2014. |
| MPI_SEC_CLS_ECL_ID | VARCHAR (18) | The unique ID (.1 item) of the default Identity security class record. This column is frequently used to link to the CLARITY_ECL table. |
| CT_DEF_CLS_ID | VARCHAR (18) | The unique ID (.1 item) of the default Chart Tracking security class record. This column is frequently used to link to the CLARITY_ECL table. |
| MR_DFLT_SEC_CLS_ID | VARCHAR (18) | Contains default EpicCare security class for user. |
| ADMIN_SEC_CL_ID | VARCHAR (18) | This is the default administrative security class assigned to this user, which can control access to the tree structure in the User Security activity. |
| DISABLE_SUB_INACT_YN | VARCHAR (1) |  |
| MU_CPOE_USER_YN | VARCHAR (1) |  |
| MC_RFND_OVERPAY_LMT | NUMERIC (18,2) | AP Claims maximum refund overpayment amount allowed. |
| PHOTO_FILE_PATH | VARCHAR (260) | Holds the path to the file where the user's photo is stored. |
| EMP_OVERRIDE_PT_C | VARCHAR (66) |  |
| NOTES_LST_REV_DT | DATETIME | The date an author's notes were last reviewed in Reporting Workbench to exclude them from future reports. |
| PN_LAST_LOGIN_DATE | DATETIME | Logs the last day that the user logged into a Push Notifications enabled app. If this item is null or the last time the user logged in was over 45 days ago, when a push notification is triggered, in addition to not sending a push notification an EOW record will not be created for this user. In addition, push notifications will not be sent if the user does not have security point 41 [Push Notifications] or an active EMP record. |
| PN_USER_ENABLED_YN | VARCHAR (1) |  |
| PN_SHOW_NEW_ONLY_YN | VARCHAR (1) |  |
| LDAP_PW_PROMPT_DATE | DATETIME | Date the user was last prompted to enter their LDAP password for use with BCA. |
| LDAP_PW_NEEDED_YN | VARCHAR (1) |  |
| RFL_DFLT_ECL_ID | VARCHAR (18) | The default referral security class when overrides are not specified by service area. |
| ANALYTICS_ECL_ID | VARCHAR (18) | The analytics default security class in the user record. This security class governs access to SlicerDicer, registry, BI integration, and predictive modeling functionality. |
| AUTHENTICATOR_ID | NUMERIC (18,0) | The mobile/physical authenticator associated with the user, networked to an E0G record. |
| ENROLLMENT_STATUS_YN | VARCHAR (1) |  |
| ALL_REG_ACCESS_YN | VARCHAR (1) |  |
| BMT_SEC_CLASS_ID | VARCHAR (18) | Stores a user's cell therapy security class. |
| CAMPAIGN_ECL_ID | VARCHAR (18) | The Campaigns security class for the user. |
| CTI_SEC_CLASS_ID | VARCHAR (18) | This is the Call Integration security class assigned to this user, which can control access functions where Epic interacts with the phone system. |
| GENETICS_SEC_CLASS_ID | VARCHAR (18) | Stores a user's Genetics security class. |
| PN_INAPP_SOUNDS_YN | VARCHAR (1) |  |
| PN_INAPP_VIBRATE_YN | VARCHAR (1) |  |
| OCC_HEALTH_SEC_ID | VARCHAR (18) | Stores a user's Occupational Health Security Class. |
| MAX_SLIDES_PER_HOUR_NUM | NUMERIC (18,2) | The maximum number of slides that a user may review in an hour. |
| NEPH_SEC_CLASS_ID | VARCHAR (18) | Stores a user's Beans security class. |
| COMM_ACSS_ONLY_YN | VARCHAR (1) |  |
| TWOFA_EMAIL_ADDRESS | VARCHAR (254) | Email address used for Two Factor Authentication in EpicCare Link. |
| TWOFA_PHONE | VARCHAR (254) | Phone number used for Two Factor Authentication in EpicCare Link. |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| B-TREE INDEX | EIX_CLARITY_EMP_2_BOE_USER | BOE_USER_NAME | 1 | Yes | Yes |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | USER_ID | CLARITY_EMP | USER_ID | Unknown | No | No |  |
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
| 2 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 2 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 2 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 3 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 4 | BTLR_CONFIG_C | ZC_BTLR_CONFIG | BTLR_CONFIG_C | No | No | No |  |
| 5 | BTLR_SORTING_C | ZC_BTLR_SORTING | BTLR_SORTING_C | No | No | No |  |
| 7 | EW_PAT_SEL_PREF_C | ZC_EW_PAT_SEL_PREF | EW_PAT_SEL_PREF_C | No | No | No |  |
| 13 | ENCOUNTER_TERM_C | ZC_ENCOUNTER_TERM | ENCOUNTER_TERM_C | No | No | No |  |
| 14 | DFLT_ENC_TAB_C | ZC_DFLT_ENC_TAB | DFLT_ENC_TAB_C | No | No | No |  |
| 19 | LAST_LOGIN_DEPT_ID | BH_DEP | DEPARTMENT_ID | No | No | No |  |
| 19 | LAST_LOGIN_DEPT_ID | CLARITY_DEP | DEPARTMENT_ID | No | No | No |  |
| 19 | LAST_LOGIN_DEPT_ID | CLARITY_DEP_2 | DEPARTMENT_ID | No | No | No |  |
| 19 | LAST_LOGIN_DEPT_ID | CLARITY_DEP_3 | DEPARTMENT_ID | No | No | No |  |
| 19 | LAST_LOGIN_DEPT_ID | CLARITY_DEP_4 | DEPARTMENT_ID | No | No | No |  |
| 19 | LAST_LOGIN_DEPT_ID | CLARITY_DEP_5 | DEPARTMENT_ID | No | No | No |  |

_(198 total; showing first 30)_
