# CLARITY_LWS

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=CLARITY_LWS

## Description

The CLARITY_LWS table contains basic information about workstations used in your system.

**Primary table** in this group (101 cols). Overflow siblings joined on shared key: CLARITY_LWS_2 (100 cols), CLARITY_LWS_3 (41 cols), CLARITY_LWS_4 (13 cols). Prefer this table for most queries.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | LWS |
| Release Version | SUMMER 2004 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| WORKSTATION_ID | VARCHAR (18) | This is the unique internal ID of the workstation. |
| WORKSTATION_NAME | VARCHAR (254) | This is the internal workstation name. |
| ROOM_IDENTIFIER | VARCHAR (254) | This is a free-text Room identification for the workstation |
| PRIM_DEPARTMENT_ID | NUMERIC (18,0) | This is the unique ID of the primary department for this workstation. |
| SCREEN_NAME | VARCHAR (254) | This is the screen name of the workstation. |
| WORKSTN_IDENTIFIER | VARCHAR (254) | This is the alphanumeric workstation identifier |
| WORKSTATION_TYPE_C | INTEGER |  |
| CM_LOG_OWNER_ID | VARCHAR (25) | This is the ID of the logical deployment owner for this record.  Logical owners show the deployment where the record was created but don't represent if the record is a part of version skew. |
| CM_PHY_OWNER_ID | VARCHAR (25) | This is the ID of the physical deployment owner for this record.  Physical owners will be where the data is hosted, either on the cross-over server or the owner deployment. |
| POOL_HIP_ID | NUMERIC (18,0) | When the workstation type is set to Pool, this workstation record is used to define a pool of users which can be set as a destination for orders in order transmittal.  Enter the pool that you wish to define for the workstation record. If this item is blank, then no pool  messages will be sent. |
| LOCAL_PRINTER_ID *(deprecated)* | VARCHAR (18) | *** Deprecated *** In table CLARITY_LWS, the column LOCAL_PRINTER_ID (LWS/35) has been deprecated.  The deprecated column's content/data is no longer available since it is no longer populated in Chronicles.  If this workstation has a local printer, this will be the local printer's workstation id number .  When a user of this workstation specifies "Print local copy," the local copy will be printed on this device. |
| PRI_ORD_TRNS_GP_ID | VARCHAR (254) | This is the default Order Transmittal Group which this workstation is assigned to. |
| ALLOWD_OVERRIDE_YN | VARCHAR (254) |  |
| OVERRIDE_DISP_NAME | VARCHAR (254) | This is the name that users see in the list of allowed override workstations if the workstation is allowed as override. |
| IS_WKSTN_DOWN_YN | VARCHAR (254) |  |
| DOWN_ON_DATE | DATETIME | This is the date the workstation went down. |
| ALT_WORKSTATION_ID | VARCHAR (18) | This is the workstation id that should intercept and process this device's messages or data if this workstation becomes unavailable. |
| REBUILD_FILES_YN *(deprecated)* | VARCHAR (254) |  |
| ORDER_PRNT_LN_NUM | INTEGER | This is the order print line number. |
| INTERFACE_ROUTG_ID | NUMERIC (18,0) | This is the type of interface that should be used when this destination is chosen. |
| CLIENT_ENABLED_YN | VARCHAR (254) |  |
| CLIENT_MAX_CACHE | INTEGER | This is the number of client events the workstation or event server should cache (store in local memory) before sending the event monitoring data to the server.  A blank entry signifies one transmission packet. |
| CACHE_LICENCE_TMOT | INTEGER | This is the number of seconds the workstation can sit idle at the login screen before a timeout occurs and the workstation's license is removed. |
| SERVER_ENABLED_YN | VARCHAR (254) |  |
| SERVER_MAX_CACHE | INTEGER | This is the number of client events the workstation or event server should cache (store in local memory) before sending the event monitoring data to the server.  A blank entry signifies one transmission packet. |
| WKSTATION_GROUP_C | VARCHAR (66) |  |
| WS_EXAM_ROOOM_YN | VARCHAR (254) |  |
| ENABLE_DIS_MGMT_YN *(deprecated)* | VARCHAR (254) |  |
| MODEM_CONNECT_TO_C | INTEGER |  |
| LOCAL_CALL_PREFIX | INTEGER | This is the local dialing prefix. |
| LONG_DISTANCE_PRFX | INTEGER | This the the long distance dialing prefix. |
| MODEM_RECORD_ID_C *(deprecated)* | VARCHAR (254) | In table CLARITY_LWS, the column MODEM_RECORD_ID_C (LWS/2030) has been deprecated.   The deprecated column's content/data is no longer available since it is no longer extracted to Clarity. |
| IS_LOCALBALLM_YN | VARCHAR (254) |  |
| IS_CARD_READER_YN | VARCHAR (254) |  |
| CARD_RDR_PORT_C | INTEGER |  |
| CARD_RDR_BAUD_C | INTEGER |  |
| CARD_RDR_DATA_BITS | INTEGER | This is the number of data bits for the card reader. |
| CARD_RDR_STOP_BITS | INTEGER | This is the number of stop bits for the card reader. |
| CARD_RDR_PARITY | INTEGER |  |
| CARD_RDR_PROGID | VARCHAR (254) | This is the programmatic ID of the card reader. |
| SP_FILE_LIMIT | INTEGER | This is the SmartPhrase file load limit |
| WKSTN_SETTINGS_ID | NUMERIC (18,0) | This is the workstation settings record used by this workstation. |
| LOGIN_CONTROL_C | VARCHAR (254) |  |
| BED_ID | VARCHAR (18) | This is the unique ID of the bed to which this workstation is linked. |
| EDMAP_USER_LOCATN | VARCHAR (254) | This is the ED map user location. |
| DEFAULT_LBL_PTR_ID | VARCHAR (18) | This is the default label printer ID for this workstation. |
| ED_LOGIN_MODE_C | INTEGER |  |
| ED_LOGIN_VIEW_ID | VARCHAR (18) | This indicates what view record to display when the LOGIN_CONTROL_C is set to Emergency Department Login and ED_LOGIN_MODE_C is Trackboard. |
| RIS_PRE_LOGIN_ID | NUMERIC (18,0) | This is the RIS Pre-Login MWL. |
| DEFAULT_WS_USER_ID | VARCHAR (18) | This is the default workstation user ID. |
| PACS_LINK_PP_ID *(deprecated)* | NUMERIC (18,0) | Deprecated, do not use. |
| ORD_OVRRDE_REVLD_C | INTEGER |  |
| RIS_PRE_LOGIN_SO_ID | NUMERIC (18,0) | Defines the Schedule Orders report definition for the imaging tech's pre-login screen. |
| KIOSK_USER_ID | VARCHAR (18) | The unique ID of the user record associated with a Kiosk workstation record. This column is frequently used to link to the CLARITY_EMP table. |
| KIOSK_PARNT_LWS_ID | VARCHAR (18) | The unique ID of the parent workstation associated with a Kiosk workstation record. This column is frequently used to link to the CLARITY_LWS table. |
| DEPARTMENT_ID | NUMERIC (18,0) | The department in which the workstation is located. |
| KIOSK_COMPUTER_NAME | VARCHAR (254) | This is dynamically set by a running kiosk to the current computer name of the machine the kiosk associated with this LWS record is running on. |
| KI_SIGN_IN_YN *(deprecated)* | VARCHAR (1) |  |
| KIOSK_ED_DEP_ID | NUMERIC (18,0) | Emergency Department to use in arriving patients. |
| KI_ED_NEW_PAT_YN | VARCHAR (1) |  |
| KIOSK_STATUS_CTRL_C | INTEGER |  |
| KI_TYPE_C | INTEGER |  |
| KIOSK_GROUP_TYPE_C | INTEGER |  |
| CHS_RLTNSHP_PTNS_C | INTEGER |  |
| CHK_IN_WIN_LEN_BEF | INTEGER | check in time window len before appt time |
| CHK_IN_TIM_WIN_AFT | INTEGER | Check in time window length after appt time |
| MYCHART_ACCESS_R_ID | VARCHAR (18) | If rule is true, the patient can not use my chart. |
| DAYS_TO_ASK_SIGN_UP | INTEGER | How oftern to ask patient for my chart sign up from kiosk |
| PAGE_TIME_OUT_VALUE | INTEGER | Page timeout value in seconds |
| ALLOW_PRINT_DOC_YN | VARCHAR (1) |  |
| ALLOW_PAT_COPAY_YN | VARCHAR (1) |  |
| REQUIRE_COPAY_YN | VARCHAR (1) |  |
| CAPTURE_CC_SIGN_YN | VARCHAR (1) |  |
| NUMBER_PMTS_DISP *(deprecated)* | INTEGER | This item has been deprecated in the Epic 2012 release. There is no replacement for this column because the functionality controlled by this configuration item no longer exists and is no longer relevant. Previously, this column contained the number of payments to display to a patient when viewing their account detail. |
| ALLOW_ACCT_DRILL_YN | VARCHAR (1) |  |
| ALLOW_BAL_PMT_YN | VARCHAR (1) |  |
| COPAY_POSTING_C | INTEGER |  |
| REQ_PT_IDENT_C | INTEGER |  |
| ALLW_DNTFCTN_CRD_YN | VARCHAR (1) |  |
| FINAL_NARROW_C | INTEGER |  |
| REG_CARD_SEC_C | INTEGER |  |
| IDENT_FILTER_C | INTEGER |  |
| DYS_BTWN_DMGRPHC_VR | INTEGER | Number of days to elapse between requests for demographic verification. |
| VERIFY_DEMOG_YN | VARCHAR (1) |  |
| MSPQ_FAILED_C | INTEGER |  |
| KI_INSURANCE_SCA_YN | VARCHAR (1) |  |
| DYS_BTWN_NSRNC_VRFC | INTEGER | Specifies the number of days to elapse between subsequent requests for insurance verification. |
| DYS_BTWN_MRGNCY_CNT | INTEGER | The number of days that elapses between subsequent requests for verification of the patient contact information. |
| KI_INSUR_FAIL_ACT_C | INTEGER |  |
| VRFY_MRGNCY_CNTC_YN | VARCHAR (1) |  |
| VERIFY_INSURANCE_YN | VARCHAR (1) |  |
| KI_NUM_EMER_CONTACT | INTEGER | Number of patient contacts to show at the kiosk |
| VERIFY_EC_AD_FMT_YN | VARCHAR (1) |  |
| VERIFY_ADDR_FMT_YN | VARCHAR (1) |  |
| BAD_ADDR_FMT_ACT_C | INTEGER |  |
| LOG_EVENTS_YN | VARCHAR (1) |  |
| KI_HH_ASK_MYCHAR_YN | VARCHAR (1) |  |
| KIOSK_ASK_QUEST_YN | VARCHAR (1) |  |
| KIOSK_CO_PMTTYPES_C | INTEGER |  |
| KI_ALLOW_PRT_AVS_YN | VARCHAR (1) | Surrogate key used to uniquely identify rows in this (and only this) table on Cogito Cloud only, do not assume the surrogate key in this table will correspond to the surrogate key in another table |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| B-TREE INDEX | EIX_CLARITY_LWS_NAME | WORKSTATION_NAME | 1 | Yes | Yes |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | WORKSTATION_ID | CLARITY_LWS_2 | WORKSTATION_ID | No | No | No |  |
| 1 | WORKSTATION_ID | CLARITY_LWS_3 | WORK_STATION_2_ID | No | No | No |  |
| 1 | WORKSTATION_ID | CLARITY_LWS_4 | WORKSTATION_ID | No | No | No |  |
| 1 | WORKSTATION_ID | WS_DEFINITION | WORKSTATION_ID | No | No | No |  |
| 4 | PRIM_DEPARTMENT_ID | BH_DEP | DEPARTMENT_ID | No | No | No |  |
| 4 | PRIM_DEPARTMENT_ID | CLARITY_DEP | DEPARTMENT_ID | No | No | No |  |
| 4 | PRIM_DEPARTMENT_ID | CLARITY_DEP_2 | DEPARTMENT_ID | No | No | No |  |
| 4 | PRIM_DEPARTMENT_ID | CLARITY_DEP_3 | DEPARTMENT_ID | No | No | No |  |
| 4 | PRIM_DEPARTMENT_ID | CLARITY_DEP_4 | DEPARTMENT_ID | No | No | No |  |
| 4 | PRIM_DEPARTMENT_ID | CLARITY_DEP_5 | DEPARTMENT_ID | No | No | No |  |
| 4 | PRIM_DEPARTMENT_ID | CLARITY_DEP_MYC | DEPARTMENT_ID | No | No | No |  |
| 4 | PRIM_DEPARTMENT_ID | DEPT_QUEUE_MSG_SETTINGS | DEPARTMENT_ID | No | No | No |  |
| 4 | PRIM_DEPARTMENT_ID | DEPT_VERIFIED_INFO | DEPARTMENT_ID | No | No | No |  |
| 4 | PRIM_DEPARTMENT_ID | DEP_BATCH_LTR_GEN | DEPARTMENT_ID | No | No | No |  |
| 4 | PRIM_DEPARTMENT_ID | DEP_CE_SETTINGS | DEPARTMENT_ID | No | No | No |  |
| 4 | PRIM_DEPARTMENT_ID | DP_HIDE_SENSITIVE_CONFIG | DEPARTMENT_ID | No | No | No |  |
| 4 | PRIM_DEPARTMENT_ID | ED_ALRT_DFLT | DEPARTMENT_ID | No | No | No |  |
| 4 | PRIM_DEPARTMENT_ID | ED_DEP_SETTINGS | DEP_ID | No | No | No |  |
| 4 | PRIM_DEPARTMENT_ID | EXT_CAL_DEPT_CONFIG | DEPARTMENT_ID | No | No | No |  |
| 4 | PRIM_DEPARTMENT_ID | VISIT_MODE_CONFIG_DEP | DEPARTMENT_ID | No | No | No |  |
| 4 | PRIM_DEPARTMENT_ID | V_CUBE_D_DEPARTMENT | DEPARTMENT_ID | Unknown | Unknown | No |  |
| 4 | PRIM_DEPARTMENT_ID | V_CUBE_D_DEP_LOC | DEPARTMENT_ID | Unknown | Unknown | No |  |
| 7 | WORKSTATION_TYPE_C | ZC_WKSTATION_TYPE | WKSTATION_TYPE_C | No | No | No |  |
| 8 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 8 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 8 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 9 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 9 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 9 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 10 | POOL_HIP_ID | CLARITY_HIP | REGISTRY_ID | Unknown | No | No |  |

_(142 total; showing first 30)_
