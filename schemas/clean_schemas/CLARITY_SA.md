# CLARITY_SA

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=CLARITY_SA

## Description

The CLARITY_SA table contains information about your service areas. The records included in this table are facility profile records that are designated as facility, service area or payor business segment. That is, Type of Location, has a value of 1, 4 or 11.

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
| SERV_AREA_ID | NUMERIC (18,0) | The unique ID number assigned to the service area record. |
| SERV_AREA_NAME | VARCHAR (200) | The name of the service area. |
| SERV_AREA_ABBR | VARCHAR (25) | The abbreviation of the service area name. |
| SERV_AREA_TYPE | VARCHAR (35) |  |
| SERV_AREA_GROUP | INTEGER |  |
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
| BILLING_SYSTEM_C | INTEGER |  |
| ID_TYPE | NUMERIC (18,0) | The master person index ID Type assigned to the service area. If the service area is not assigned an ID Type, then the ID Type of the facility (EAF 1) will be shown. |
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
| PPL_AREA_YN | VARCHAR (1) |  |
| CLNT_ACCT_TYPE_C | INTEGER |  |
| CLNT_FEE_SCHEDUL_ID | NUMERIC (18,0) | The unique ID of the default fee schedule used by the lab billing client account that is associated with this service area.  . |
| CLNT_STM_FORM_ID | VARCHAR (18) | The unique ID of the default client statement form that is associated with this service area. |
| CLNT_SBWO_AMT | NUMERIC (12,2) | Used to store client small balance amount. |
| CLNT_SBWO_CODE_ID | NUMERIC (18,0) | The unique ID of the procedure used to store the client small balance write-off code that is associated with this service area. |
| HB_CEWQ_SELECTIVE_C | INTEGER |  |
| REMIT_WQPR_EN_YN *(deprecated)* | VARCHAR (1) |  |
| ERR_FRC_CEWQ_YN *(deprecated)* | VARCHAR (1) |  |
| ERR_OVRD_CEWQ_YN *(deprecated)* | VARCHAR (1) |  |
| EPSDT_VALUE_DFLT_C | INTEGER |  |
| CONTACT_PERSON_ID | VARCHAR (18) | Stores the administrative contact person for claims for this service area. |
| SA_PRODUCT_MODE_C | VARCHAR (66) |  |
| DEF_VENCONTRACT_ID | NUMERIC (18,0) | The default vendor contract to use. |
| SMS_EML_FRM | VARCHAR (192) | This column is the source email address for the emails to SMS gateway provider. These emails are converted to text messages (SMS) at the gateway provider. In most cases, this address is used for authentication at the gateway provider and must match the set up at the gateway. |
| SMS_EML_TO | VARCHAR (192) | This column is the target email address for the emails to gateway provider. These emails are converted to text messages (SMS) at the gateway provider. |
| SMS_SETUP_ETX_ID | VARCHAR (18) | The ID of the SmartText that contains the format of the email to the SMS gateway provider in the format dictated by the gateway provider. The email message sent to the gateway provider is converted into an SMS by the gateway. This text will usually contain the authentication details for the SMS gateway. |
| RCV_MSGS_C | INTEGER |  |
| DELIVERY_MECH_C | INTEGER |  |
| APPT_REM_RULE_ID | VARCHAR (18) | The unique ID of the patient rule to control the conditions to be met before sending an quick reminder to a patient. |
| SMS_REM_MSG_ETX_ID | VARCHAR (18) | The unique ID of the SmartText used to generate the message for quick reminders sent via SMS. |
| APPT_REM_EML_FRM | VARCHAR (192) | This column is the source email address for the quick reminders sent to patients via an email. |
| EML_REM_SUBJ_ETX_ID | VARCHAR (18) | The unique ID of the SmartText used to generate the subject for quick reminders sent to patients via email. |
| EML_REM_MSG_ETX_ID | VARCHAR (18) | The unique ID of the SmartText used to generate the body for quick reminders sent to patients via email. |
| ANSI_835_TRN03 | VARCHAR (254) | Unique identifier for the organization sending the ANSI 835 file. |
| LICENSE_TYPE_C | INTEGER |  |
| HSD_PROFILE_ID | NUMERIC (18,0) | The Hospital Billing System Definition Profile record associated with this service area.  If no profile is specified for this service area, the ID of the profile assigned to the service area that this service area inherits null values from will be used.  If no alternate service area is specified, and a flag is set on the service area to default to the facility level profile, then the facility level profile ID will be used. |
| SMS_OVRRD_ID | NUMERIC (18,0) | The ID of the extension record that overrides the standard delivery mechanism to send text messages out of the system. The standard mechanism is to use an email-to-SMS interface to communicate with a gateway provider. |
| CONTACT_NAME | VARCHAR (254) | Name of the contact person at the associated payor organization. |
| CMS_PLAN_ID | VARCHAR (254) | CMS Plan ID sent on outbound ANSI 835 files. |
| SEC_COMM_TYPE_C | INTEGER |  |
| SEC_COMM_NUM | VARCHAR (254) | Secondary communication number |
| EXTERNAL_NAME | VARCHAR (254) | The name of the record that appears in billing correspondences such as statements and letters. |
| HB_CUST_SVC_PHNUM | VARCHAR (30) | Phone number to contact for Hospital Billing related inquiries for this facility or service area. |
| PB_CUST_SVC_PHNUM | VARCHAR (30) | Phone number to contact for Professional Billing related inquiries for this facility or service area. |
| ABN_SEARCH_CONT_YN | VARCHAR (1) |  |
| AUTO_CREATE_ABNS_YN | VARCHAR (1) |  |
| AUTO_REGEN_ABNS_YN | VARCHAR (1) |  |
| PR_LEEWAY_UP_DOL | NUMERIC (18,2) | Minimum increase of the estimated price in dollars that would trigger a regeneration. |
| PR_LEEWAY_UP_PCT | NUMERIC (18,2) | Minimum increase of the estimated price in percentage of the original estimate that would trigger a regeneration. |
| PR_LEEWAY_DOWN_DOL | NUMERIC (18,2) | Minimum decrease of the estimated price in dollars that would trigger a regeneration. |
| PR_LEEWAY_DOWN_PCT | NUMERIC (18,2) | Minimum decrease of the estimated price in percentage of the original estimate that would trigger a regeneration. |
| REGEN_IF_DEP_CHAN_C | VARCHAR (66) |  |
| RA_SMARTTEXT_ID | VARCHAR (18) | Contains the SmartText format used by RA reports. |
| PB_CEV_EDIT_YN | VARCHAR (1) |  |
| HB_CEV_EDIT_YN | VARCHAR (1) |  |
| LTG_DEFAULT_MIN_DAYS | INTEGER | Stores the default minimum number of days allowed between appointment scheduling and the appointment date for the goal. |
| LTG_DEFAULT_MAX_DAYS | INTEGER | Stores the default maximum number of days allowed between appointment scheduling and the appointment date for the goal. |
| LICENSE_GROUP_C | INTEGER |  |
| LATE_CANCEL_HOURS | INTEGER | The number of hours before the start time of an appointment that a patient can cancel before it is considered a late cancellation. |
| HB_CUBE_ACCESS_YN | VARCHAR (1) |  |
| PB_CUBE_ACCESS_YN | VARCHAR (1) |  |
| REG_TYPE_AIF_ID | NUMERIC (18,0) | This item holds the mapping table for department register type (1.2.246.537.5.40150) to controller register type (1.2.246.537.5.40172). |
| OSA_VALID_LENGTH | INTEGER | This item holds the length of time an outsourced service event authorization query result remains valid for. By default, the query will remain valid for 10 minutes. |
| DEMAND_MET_DAYS_BEFORE | INTEGER | The maximum number of days an appointment can be scheduled before the requested date to be considered as having met the request. If null, appointments scheduled at any time before the requested date will meet the request. |
| DEMAND_MET_DAYS_AFTER | INTEGER | The maximum number of days an appointment can be scheduled after the requested date to be considered as having met the request. If null, appointments scheduled at any time after the requested date will meet the request. |
| MYC_ENC_EXCL_DATE | DATETIME | If set, MyChart will not examine encounters in this service area that ended before this date when calculating activation rate metric values.  This value will be overridden by the analagous department column, CLARITY_DEP_MYC.MYC_ENC_EXCL_DATE if the encounter's department has a value.   To specify dates for service areas, contact your MyChart TS and reference SLG 3876732. |
| PB_GOLIVE_DT | DATETIME | This column holds the true production go-live date for Resolute PB to enable more accurate reporting. |
| BILL_SYS_SUBTYPE_C | INTEGER |  |
| ALLOW_REFER_TO_YN | VARCHAR (1) |  |
| ALT_HSD_SERV_AREA_ID | NUMERIC (18,0) | Indicates whether the system should obtain a profile value from the profile record of an alternate service area if the profile value is null for the given EAF record. |
| USE_FAC_HSD_DFLT_YN | VARCHAR (1) |  |
| SA_HSD_PROFILE_ID | NUMERIC (18,0) | The Hospital Billing System Definition Profile record associated with this service area. Unlike the column CLARITY_SA.HSD_PROFILE_ID, this column will not check the alternative service area, or default to the facility level profile. Instead, this column will simply pulling directly from item HSD 41000. |
| IS_BUSINESS_SEGMENT_YN | VARCHAR (1) |  |
| NEWBORN_PAT_CLASS_C | VARCHAR (66) |  |
| DFLT_DELAY_DT_RSN_C | INTEGER |  |
| REPORTING_SERV_AREA_ID | NUMERIC (18,0) | The service area responsible for reporting Springboard data gathered in this service area. If this item is blank, it is assumed that the service area is responsible for reporting its own data.  This item should only be used in rare situations, such as when two service areas merge, but the organization has not combined the service area records. |
| EPS_PRESC_COST_CENTER_POS_ID | NUMERIC (18,0) | The e-prescribing cost center organization to be used for reimbursement for this service area. This must point to a facility (EAF) record with a valid ODS code for e-prescribing reimbursement with the NHS Business Service Authority (BSA). This item is only relevant for configuration in the United Kingdom, specifically for organizations that integrate with the NHS Electronic Prescription Service (EPS). |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | SERV_AREA_ID | ANALYTICS_SYSTEM_SETTINGS | FACILITY_ID | No | No | No |  |
| 1 | SERV_AREA_ID | ARPB_SA_SETTINGS | FACILITY_ID | No | No | No |  |
| 1 | SERV_AREA_ID | CLARITY_LOC | LOC_ID | Unknown | No | No |  |
| 1 | SERV_AREA_ID | CLARITY_LOC_2 | LOC_ID | Unknown | No | No |  |
| 1 | SERV_AREA_ID | CLARITY_POS | POS_ID | No | No | No |  |
| 1 | SERV_AREA_ID | CLARITY_POS_2 | POS_ID | No | No | No |  |
| 1 | SERV_AREA_ID | CL_LOC_HIERARCHY | LOC_ID | Unknown | No | No |  |
| 1 | SERV_AREA_ID | CV_PCI_D2B_SETTINGS | FACILITY_ID | No | No | No |  |
| 1 | SERV_AREA_ID | EAF_CLM_ALTADR_INF | FACILITY_ID | No | No | No |  |
| 1 | SERV_AREA_ID | EAF_CLM_RMT_SETUP | FACILITY_ID | No | No | No |  |
| 1 | SERV_AREA_ID | EAF_EXP_APPT_LOG | FACILITY_ID | No | No | No |  |
| 1 | SERV_AREA_ID | EAF_SEARCH_TERMS | FACILITY_ID | No | No | No |  |
| 1 | SERV_AREA_ID | ESCALATION_THRESH_SGL | FACILITY_ID | No | No | No |  |
| 1 | SERV_AREA_ID | FAC_CONNECT | FACILITY_ID | No | No | No |  |
| 1 | SERV_AREA_ID | FAC_DIRECT_ADDR | FACILITY_ID | Unknown | No | No |  |
| 1 | SERV_AREA_ID | HH_FAC_INFO | FACILITY_ID | No | No | No |  |
| 1 | SERV_AREA_ID | MC_FACILITY_GL_SEGMENTS | FACILITY_ID | No | No | No |  |
| 1 | SERV_AREA_ID | MYC_INFO | FACILITY_ID | No | No | No |  |
| 1 | SERV_AREA_ID | OR_LOC | LOC_ID | Unknown | No | No |  |
| 1 | SERV_AREA_ID | PDMD_FILE_CONFIG | FACILITY_ID | No | No | No |  |
| 1 | SERV_AREA_ID | RX_LOC | LOC_ID | Unknown | No | No |  |
| 1 | SERV_AREA_ID | SD_FILTER_CONFIG_SETTING | FACILITY_ID | Yes | No | No |  |
| 1 | SERV_AREA_ID | SERVICE_PROV | FACILITY_ID | No | No | No |  |
| 1 | SERV_AREA_ID | SMS_SETTINGS_SNGL | FACILITY_ID | No | No | No |  |
| 1 | SERV_AREA_ID | SYS_RSH_RPT_GRP_OVRIDE | FACILITY_ID | No | No | No |  |
| 1 | SERV_AREA_ID | V_CMS_MU_LOC | LOC_ID | Unknown | Unknown | No |  |
| 1 | SERV_AREA_ID | V_CUBE_D_LOCATION | LOCATION_ID | Unknown | Unknown | No |  |
| 1 | SERV_AREA_ID | V_CUBE_D_SERVICE_AREA | SERVICE_AREA_ID | Unknown | Unknown | No |  |
| 1 | SERV_AREA_ID | V_OR_LOC_STRUCTURE | OR_LOC_ID | Unknown | Unknown | No |  |
| 5 | SERV_AREA_GROUP | ZC_SERV_AREA_GROUP | SERV_AREA_GROUP | No | No | No |  |

_(200 total; showing first 30)_
