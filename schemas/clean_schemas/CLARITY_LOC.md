# CLARITY_LOC

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=CLARITY_LOC

## Description

This table contains information about your location records. These include revenue locations and patients' primary clinics/locations. The records included in this table are Facility Profile (EAF) records that are designated as facility, service area, and location records. That is, Type of Location (I EAF 27) has a value of 1, 2, or 4.

**Primary table** in this group (100 cols). Overflow siblings joined on shared key: CLARITY_LOC_2 (74 cols). Prefer this table for most queries.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | EAF |
| Release Version | EPIC 2000 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| LOC_ID | NUMERIC (18,0) | The unique ID number assigned to the location record. |
| LOC_NAME | VARCHAR (200) | The name of the revenue location. |
| LOCATION_GROUP | INTEGER |  |
| DEFAULT_DEPT_ID | NUMERIC (18,0) | The ID of the default department associated with this location. |
| POS_TYPE | VARCHAR (66) |  |
| LOCATION_ABBR | VARCHAR (25) | The abbreviated name of the location. |
| LOC_IS_OUTSIDE | VARCHAR (10) |  |
| GL_PREFIX | VARCHAR (128) | The code that billing system?s General Ledger report uses to identify transactions belonging to a revenue location. |
| RPT_GRP_ONE | VARCHAR (80) | You can specify groupers for enterprise reporting, SQL, or report generator reporting. This is one of the free-text report groupers. |
| RPT_GRP_TWO | VARCHAR (80) | You can specify groupers for enterprise reporting, SQL, or report generator reporting. This is one of the free-text report groupers. |
| RPT_GRP_THREE | VARCHAR (80) | You can specify groupers for enterprise reporting, SQL, or report generator reporting. This is one of the free-text report groupers. |
| RPT_GRP_FOUR | VARCHAR (80) | You can specify groupers for enterprise reporting, SQL, or report generator reporting. This is one of the free-text report groupers. |
| RPT_GRP_FIVE | VARCHAR (80) | You can specify groupers for enterprise reporting, SQL, or report generator reporting. This is one of the free-text report groupers. |
| RPT_GRP_SIX | VARCHAR (66) |  |
| RPT_GRP_SEVEN | VARCHAR (66) |  |
| RPT_GRP_EIGHT | VARCHAR (66) |  |
| RPT_GRP_NINE | VARCHAR (66) |  |
| RPT_GRP_TEN | VARCHAR (66) |  |
| SERV_AREA_ID | NUMERIC (18,0) | The unique ID for the service area to which this location is assigned. |
| BEN_BKT_OPT_C | INTEGER |  |
| ID_TYPE | NUMERIC (18,0) | The master person index ID Type assigned to this location. If the location has no ID Type, then the ID Type of the parent service area will be shown. If the service area has no ID type assigned either, then the ID Type of the facility (EAF 1) will be shown. |
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
| RECORD_STATUS | INTEGER |  |
| MED_PREF_LIST_ID | NUMERIC (18,0) | This column holds the medication preference list ID associated with this location. |
| ORDERS_PREF_LIST_ID | NUMERIC (18,0) | This column holds the orders preference list ID associated with this location. |
| DFLT_PREFLST_EPD_ID | NUMERIC (18,0) | The unique ID of the default Editor-based preference list that should be used in this location. |
| DFLT_PREFLST_LPF_ID | VARCHAR (25) | The unique ID of the default Composer-based preference list that should be used in this location. |
| DISC_INT_ENAB_YN | VARCHAR (1) |  |
| MANUAL_FREE_TXT_YN | VARCHAR (1) |  |
| THERAPY_UP_POOL_ID *(deprecated)* | NUMERIC (18,0) | *** Deprecated ***  In table CLARITY_LOC, the column THERAPY_UP_POOL_ID (EAF/27230) has been deprecated. The deprecated column's content/data is no longer available since it is no longer populated in Chronicles.  The In Basket pool to which therapy upcode messages should be sent. |
| CRCL_FORMULA_PPT_ID | NUMERIC (18,0) | The unique ID of the extension to be used for calculating the Creatinine Clearance (CrCl) value for patients. This extension will be used for all calculations and reports that rely on CrCl lab results in the current hospital. |
| FLT_PREF_LIST_ID | NUMERIC (18,0) | Flowsheet template preference list used by this facility. |
| CC_DEP_SEL_PPT_ID | NUMERIC (18,0) | The unique ID of the programming point to select departments for charges in this location. |
| CC_ASSN_DEF_CC_ID | NUMERIC (18,0) | The unique ID of the default cost center for this location. |
| DEF_MESSAGE_TYPE_C | INTEGER |  |
| ED_SA_CREATE_HAR_YN | VARCHAR (1) |  |
| ED_SA_DFLT_PATCLS_C | VARCHAR (66) |  |
| CONV_APPT_TO_HOV_YN | VARCHAR (1) |  |
| CONV_APPTS_HOV_ID | NUMERIC (18,0) | This column holds converted appointments' HOV IDs. |
| DFLT_ED_HOSP_AREA_C | INTEGER |  |
| CS_DATE_RANGE_LIMIT | INTEGER | This column holds the maximum time range, in hours, for the census snapshot report. |
| NEWBORN_UNKN_SSN_C | INTEGER |  |
| FAX_NUM | VARCHAR (80) | This is the fax number corresponding to the location, service area, or facility record. |
| USING_EMR_YN | VARCHAR (1) |  |
| INTERNAL_LAB_ID | NUMERIC (18,0) | If this location has an internal lab, this column will contain the ID of the lab record. Order completion can be configured so that this lab has priority and will always be the first lab considered when determining where to send an order. |
| CHILD_ORDER_DEPT_ID | NUMERIC (18,0) | The unique ID of the Department into which future and standing discharge orders in this revenue location are released. |
| POS_CODE | VARCHAR (25) | Code for Place of Service. |
| OR_LOC_TYPE_C | INTEGER |  |
| PRC_STP_END_EVT_C | INTEGER |  |
| SHARE_PERIDATA_I_YN | VARCHAR (1) |  |
| FILT_IMP_OFF_PCK_YN | VARCHAR (1) |  |
| FILT_CDP_OFF_PCK_YN | VARCHAR (1) |  |
| CASE_SETUP_EVENT_C | VARCHAR (66) |  |
| CASE_CLEANUP_EVNT_C | VARCHAR (66) |  |
| CS_SETUP_END_EVT_C | VARCHAR (66) |  |
| CASE_CLNP_END_EVT_C | VARCHAR (66) |  |
| PRC_CLNUP_END_EVT_C | INTEGER |  |
| PROC_END_TIM_EVT_C | INTEGER |  |
| INVENTORY_LOC_YN | VARCHAR (1) |  |
| SETUP_EVENT_C | INTEGER |  |
| CLEANUP_EVENT_C | INTEGER |  |
| OR_NORMAL_START_TM | DATETIME (Local) | Stores the normal start time for the OR. |
| OR_NORMAL_END_TM | DATETIME (Local) | Stores the normal end time for the OR. |
| PROC_LENGTH_EVENT_C | INTEGER |  |
| SURG_START_EVENT_C | VARCHAR (66) |  |
| SURG_END_EVENT_C | VARCHAR (66) |  |
| EPT_PRIVACY_FLAG_C | INTEGER |  |
| ADT_LOCATION_TYPE_C | VARCHAR (66) |  |
| ADT_PARENT_ID | NUMERIC (18,0) | The parent for this hospital area. |
| DAILY_BCB_TABLE_ID | NUMERIC (18,0) | The ID of the Bed Charge Billing Procedure Table (BCB)  that is used to determine daily bed charges. |
| HOURLY_BCB_TABLE_ID | NUMERIC (18,0) | The ID of the Bed Charge Billing Procedure Table (BCB)  that is used to determine hourly bed charges. |
| DAYS_FOR_INCOMP_MSG | INTEGER | This item stores the number of days an encounter is left open until the supervisor receives an incomplete chart message. |
| FACILITY_TRNSCRTN | VARCHAR (254) | The name of the transcriptionist for this location. |
| FAC_LET_TRNSCRTN | VARCHAR (254) | The name of the letter transcriptionist for this location. |
| TRNSCRTN_POOL_C | VARCHAR (66) |  |
| LT_TRNSCRTN_POOL_C | VARCHAR (66) |  |
| EMERG_PHONE | VARCHAR (30) | Stores the hotline/emergency phone number for the location. |
| PERSIS_FUTURE_YN | VARCHAR (1) |  |
| CMS_CERT_NUM | VARCHAR (254) | The CMS Certification Number (CCN). |
| CALC_CMS_CERT_NUM *(deprecated)* | VARCHAR (254) |  |
| GEO_LOCALITY_ID | NUMERIC (18,0) | The locale is based on the actual geographic location of this facility, and is used in determining adjusted prices. |
| DISP_CVG_FAST_RE_YN | VARCHAR (1) |  |
| ECP_SERVER_NAME *(deprecated)* | VARCHAR (50) | *** Deprecated *** In table CLARITY_LOC,  the column ECP_SERVER_NAME (EAF 12900) has been deprecated. The deprecated column's content/data is no longer available since it is no longer populated in Chronicles. ECP Server overrides are no longer supported. |
| POS_TYPE_C | INTEGER |  |
| HOSP_PARENT_LOC_ID | NUMERIC (18,0) | Parent Location is the location that the amount on a charge is allotted to. |
| FACILITY_ID | No | Facility ID is the CID of the facility level within an IntraConnect neighborhood. The local Facility ID in an environment (including non-IC environments) is always 1; this column performs the standard Clarity CID translation. |
| DEF_RC_ID | NUMERIC (18,0) | Used as the Rate Center if no lines in the Cost Center Assignment table match |
| HRA_BAL_NEGATIVE_YN *(deprecated)* | VARCHAR (1) |  |
| AUR_ENABLED_YN *(deprecated)* | VARCHAR (1) |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | LOC_ID | ANALYTICS_SYSTEM_SETTINGS | FACILITY_ID | No | No | No |  |
| 1 | LOC_ID | ARPB_SA_SETTINGS | FACILITY_ID | No | No | No |  |
| 1 | LOC_ID | CLARITY_LOC_2 | LOC_ID | Unknown | No | No |  |
| 1 | LOC_ID | CLARITY_POS | POS_ID | No | No | No |  |
| 1 | LOC_ID | CLARITY_POS_2 | POS_ID | No | No | No |  |
| 1 | LOC_ID | CLARITY_SA | SERV_AREA_ID | Unknown | No | No |  |
| 1 | LOC_ID | CL_LOC_HIERARCHY | LOC_ID | Unknown | No | No |  |
| 1 | LOC_ID | CV_PCI_D2B_SETTINGS | FACILITY_ID | No | No | No |  |
| 1 | LOC_ID | EAF_CLM_ALTADR_INF | FACILITY_ID | No | No | No |  |
| 1 | LOC_ID | EAF_CLM_RMT_SETUP | FACILITY_ID | No | No | No |  |
| 1 | LOC_ID | EAF_EXP_APPT_LOG | FACILITY_ID | No | No | No |  |
| 1 | LOC_ID | EAF_SEARCH_TERMS | FACILITY_ID | No | No | No |  |
| 1 | LOC_ID | ESCALATION_THRESH_SGL | FACILITY_ID | No | No | No |  |
| 1 | LOC_ID | FAC_CONNECT | FACILITY_ID | No | No | No |  |
| 1 | LOC_ID | FAC_DIRECT_ADDR | FACILITY_ID | Unknown | No | No |  |
| 1 | LOC_ID | HH_FAC_INFO | FACILITY_ID | No | No | No |  |
| 1 | LOC_ID | MC_FACILITY_GL_SEGMENTS | FACILITY_ID | No | No | No |  |
| 1 | LOC_ID | MYC_INFO | FACILITY_ID | No | No | No |  |
| 1 | LOC_ID | OR_LOC | LOC_ID | Unknown | No | No |  |
| 1 | LOC_ID | PDMD_FILE_CONFIG | FACILITY_ID | No | No | No |  |
| 1 | LOC_ID | RX_LOC | LOC_ID | Unknown | No | No |  |
| 1 | LOC_ID | SD_FILTER_CONFIG_SETTING | FACILITY_ID | Yes | No | No |  |
| 1 | LOC_ID | SERVICE_PROV | FACILITY_ID | No | No | No |  |
| 1 | LOC_ID | SMS_SETTINGS_SNGL | FACILITY_ID | No | No | No |  |
| 1 | LOC_ID | SYS_RSH_RPT_GRP_OVRIDE | FACILITY_ID | No | No | No |  |
| 1 | LOC_ID | V_CMS_MU_LOC | LOC_ID | Unknown | Unknown | No |  |
| 1 | LOC_ID | V_CUBE_D_LOCATION | LOCATION_ID | Unknown | Unknown | No |  |
| 1 | LOC_ID | V_CUBE_D_SERVICE_AREA | SERVICE_AREA_ID | Unknown | Unknown | No |  |
| 1 | LOC_ID | V_OR_LOC_STRUCTURE | OR_LOC_ID | Unknown | Unknown | No |  |
| 3 | LOCATION_GROUP | ZC_LOCATION_GROUP | LOCATION_GROUP | No | No | No |  |

_(300 total; showing first 30)_
