# CLARITY_SER

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=CLARITY_SER

## Description

The CLARITY_SER table contains high-level information about your provider records. These records may be caregivers, resources, classes, devices, and modalities.

**Primary table** in this group (127 cols). Overflow siblings joined on shared key: CLARITY_SER_2 (100 cols), CLARITY_SER_3 (46 cols), CLARITY_SER_4 (13 cols). Prefer this table for most queries.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | SER |
| Release Version | EPIC 2000 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| PROV_ID | VARCHAR (18) | The unique ID assigned to the provider record. This ID can be encrypted. |
| PROV_NAME | VARCHAR (200) | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| PROV_TYPE | VARCHAR (66) |  |
| PROV_ABBR | VARCHAR (254) | An abbreviation of the provider's name. This item can be hidden in a public view of the CLARITY_SER table. |
| GL_PREFIX | VARCHAR (128) | The code that billing system?s general ledger report uses to identify transactions associated with a provider if you use provider as an identifying category in your facility. |
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
| IS_RESIDENT | VARCHAR (3) |  |
| USER_ID | No | The unique ID of the user record that is assigned to this provider, found using item 17500 in the user record. This column is frequently used to link to the CLARITY_EMP table. |
| EPIC_PROV_ID | VARCHAR (18) | The unique ID assigned to the provider record. This ID may be hidden in a public view of this table. |
| REFERRAL_SRCE_TYPE | VARCHAR (66) |  |
| IS_VERIFIED_YN | VARCHAR (1) |  |
| SER_REF_SRCE_ID | VARCHAR (18) | The unique ID of the referral source record that is associated with this provider. |
| UPIN | VARCHAR (30) | The Unique Physician Identification Number (UPIN) for the provider. |
| SSN | VARCHAR (192) | The provider's social security number. |
| EMP_STATUS | VARCHAR (40) | The employment status for this provider. |
| STAFF_RESOURCE | VARCHAR (20) |  |
| CLINICIAN_TITLE | VARCHAR (66) |  |
| EXTERNAL_NAME | VARCHAR (80) | The external name of the provider record. |
| ACTIVE_STATUS | VARCHAR (20) |  |
| REFERRAL_SOURCE_TYPE | VARCHAR (66) |  |
| RECORD_TYPE | INTEGER |  |
| BILL_PROV_YN | VARCHAR (1) |  |
| BILL_UNDER_PROV_ID | VARCHAR (18) | The default provider to bill under if not a billing provider. |
| SUP_PROV_ID | VARCHAR (18) | The link to the supervisor's provider record. |
| COUNTY_C | VARCHAR (66) |  |
| COUNTRY_C | VARCHAR (66) |  |
| OFFICE_PHONE_NUM | VARCHAR (50) | The office phone number for the provider. |
| OFFICE_FAX_NUM | VARCHAR (25) | The office fax number for the provider. |
| EMAIL | VARCHAR (254) | The provider's e-mail address. |
| DEA_NUMBER | VARCHAR (30) | The provider's DEA number for prescribing controlled medications. |
| SEX | VARCHAR (66) |  |
| BIRTH_DATE | DATETIME | The date the provider was born. |
| MEDICARE_PROV_ID | VARCHAR (12) | The Medicare ID number for this provider. |
| MEDICAID_PROV_ID | VARCHAR (12) | The Medicaid ID number for this provider. |
| IS_PRIV_REVOKED | VARCHAR (1) |  |
| NURSE_EMP_ID | VARCHAR (18) | The unique ID of the user record that is associated with the provider's nurse. This is frequently used to link to the CLARITY_EMP table. |
| EPICCARE_PROV_YN | VARCHAR (1) |  |
| MEDS_AUTH_PROV_YN | VARCHAR (1) |  |
| ORDS_AUTH_PROV_YN | VARCHAR (1) |  |
| TRANS_INTF_USER_YN | VARCHAR (1) |  |
| PEER_REV_LAST_DATE | DATETIME | The date this provider last went through peer review. |
| TAKING_NEW_PAT_YN | VARCHAR (1) |  |
| TAKING_WALKINS_YN | VARCHAR (1) |  |
| LAST_RECOMMENDED_DATE | DATETIME | The date of last recommendation. |
| BASE_COST | NUMERIC (12,2) | The base cost for the surgeon/staff/resource in OR management system. |
| SURG_REC_POOL_YN | VARCHAR (1) |  |
| INSTRUMENT_TYPE_C | VARCHAR (66) |  |
| EQUIP_SERVICE_DATE | DATETIME | The next service date of equipment, if specified in surgical equipment admin. |
| EQUIP_LASTSVC_DATE | DATETIME | The last date that the equipment was serviced. |
| CLM_POS_REQD_YN | VARCHAR (1) |  |
| DEFAULT_POS_CLM_YN | VARCHAR (1) |  |
| MODALITY_TYPE_C | INTEGER |  |
| MODALITY_YN | VARCHAR (1) | Indicates whether the provider or resource is a modality. |
| SUPERV_POOL_ID *(deprecated)* | VARCHAR (18) | *** Deprecated *** In table CLARITY_SER, the column SUPERV_POOL_ID (SER/52020) has been deprecated. The deprecated column's content/data is no longer available since it is no longer populated in Chronicles.   The supervising pool ID for a resident. |
| SUPERV_POOL_NAME *(deprecated)* | VARCHAR (254) | *** Deprecated *** In table CLARITY_SER, the column SUPERV_POOL_NAME (SER/52020) has been deprecated. The deprecated column's content/data is no longer available since it is no longer populated in Chronicles.   The supervising pool name for a resident. |
| FLASH_CARD_PRT_ROU | VARCHAR (255) | The routine for printing flash cards. |
| CTRL_SHEET_PRT_ROU | VARCHAR (255) | The routine for printing control sheets. |
| PIN_ID | VARCHAR (18) | The unique ID of the Provider Insurance Filing Information record that is associated with this provider. |
| PROV_ATTR_ID | VARCHAR (18) | The unique ID of the provider attribute record that is associated with this provider. |
| ATTND_PRIM_PAGER | VARCHAR (50) | The primary pager number of the provider. |
| OO_OFFICE_FROM_DTE | DATETIME | The date from which the provider is out of the office. |
| OO_OFFICE_TO_DTE | DATETIME | The date until which the provider will be out of the office. |
| DEF_DEPARTMENT_ID | NUMERIC (18,0) | The ID of the chart tracking deficiency department for the provider. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
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
| HOSPITALIST_YN | VARCHAR (254) |  |
| DEF_DIVISION_C | VARCHAR (66) |  |
| DEF_PROVIDER_YN | VARCHAR (254) |  |
| PROV_REC_STATE_C | INTEGER |  |
| PROV_START_DATE | DATETIME | The employment start date for this provider. |
| PRACTICE_NAME_C | INTEGER |  |
| SURG_SCHED_OUT_YN | VARCHAR (1) |  |
| SURG_EQP_SVCDAT_YN | VARCHAR (1) |  |
| SURG_COST_TBL_ID | NUMERIC (18,0) | Stores the cost table ID (OCT) for the surgical staff/resource. |
| TEAM_LEADER_ID | VARCHAR (18) | This column contains the provider ID (SER dot one) of the provider's team leader. |
| TEAM_C | INTEGER |  |
| SUP_PROV_YN | VARCHAR (1) |  |
| EMPLOYED_CRNA_YN | VARCHAR (1) |  |
| IS_INTERPRETER_YN | VARCHAR (1) |  |
| DOCTORS_DEGREE | VARCHAR (254) | The degrees, such as M.D., held by this provider. |
| REVENUE_DEPT_ID | NUMERIC (18,0) | This is the default department for which revenue generated by this provider should be associated. Currently, this field is only used for determining the correct service area in which to create an HPF encounter when ADT triggers encounter creation. |
| ENC_PROV_YN | VARCHAR (1) |  |
| PHARMACIST_YN | VARCHAR (1) |  |
| LAB_FAX_NUMBER | VARCHAR (254) | Stores a fax number that will be used to route paper result reports from the Lab. |
| PROV_PHOTO | VARCHAR (508) | Path to the provider photo to use in the Welcome kiosk. |
| USE_DEPT_VT_LIM_YN *(deprecated)* | VARCHAR (1) |  |
| VERIFYING_PERSON_ID | VARCHAR (18) | User ID of the person verifying the SER record. |
| OR_VLD_DT_OFST | INTEGER | Release offset - How many months into the future this resource can be scheduled in OpTime. |
| OR_CHARGE_CODE_ID | NUMERIC (18,0) | The unique ID of the charge code associated with this equipment resource. |
| DIRECTORY_INFO | VARCHAR (254) | Contains extended information for display in a facility directory in the Welcome kiosk. |
| DBC_EXT_POS_ID | NUMERIC (18,0) | The unique ID of the EAF record that represents the external place of service for the provider. It is only for providers deemed external by the internal/external flag (I SER 190). |
| RES_POOL_TYPE_C | INTEGER |  |
| EDI_CLM_ACTIVE_YN | VARCHAR (1) |  |
| PROV_CLM_PROC_STA_C | INTEGER |  |
| PAYEE_NUM_DEFAULT | VARCHAR (254) | The payee code which should appear by default in box 33 of Medicaid Claims using standard form 182 (Illinois Medicaid). |
| SER_CLM_ID | VARCHAR (254) | The unique ID of the provider for custom claims. |
| MCD_PROF_CD_C | INTEGER |  |
| OP_ORD_PROV_YN | VARCHAR (1) |  |
| IS_SUP_PROV_REQ_C | INTEGER |  |
| PROVIDER_TYPE_C | VARCHAR (66) |  |
| EPRESCRIBING_YN | VARCHAR (1) |  |
| EP_FLAG_YN *(deprecated)* | VARCHAR (1) |  |
| SEX_C | VARCHAR (66) |  |
| ACTIVE_STATUS_C | INTEGER |  |
| REFERRAL_SOURCE_TYPE_C | VARCHAR (66) |  |
| STAFF_RESOURCE_C | INTEGER |  |
| REFERRAL_SRCE_TYPE_C | 45 | Surrogate key used to uniquely identify rows in this (and only this) table on Cogito Cloud only, do not assume the surrogate key in this table will correspond to the surrogate key in another table |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| B-TREE INDEX | EIX_CLARITY_SER_EPPRID | EPIC_PROV_ID | 1 | Yes | Yes |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | PROV_ID | CLARITY_SER_2 | PROV_ID | Unknown | No | No |  |
| 1 | PROV_ID | CLARITY_SER_3 | PROV_ID | Unknown | No | No |  |
| 1 | PROV_ID | CLARITY_SER_4 | PROV_ID | No | No | No |  |
| 1 | PROV_ID | CLARITY_SER_MYC | PROV_ID | Unknown | No | No |  |
| 1 | PROV_ID | D_PROV_PRIMARY_HIERARCHY | PROV_ID | Unknown | Unknown | No |  |
| 1 | PROV_ID | ED_SER_SETTINGS | PROV_ID | Unknown | No | No |  |
| 1 | PROV_ID | EXT_CAL_PROV_CONFIG | PROV_ID | No | No | No |  |
| 1 | PROV_ID | OR_SER_EQUIPMENT | PROV_ID | Unknown | No | No |  |
| 1 | PROV_ID | OR_SER_ROOM | PROV_ID | Unknown | No | No |  |
| 1 | PROV_ID | PROV_BATCH_LTR_GEN | PROV_ID | Unknown | No | No |  |
| 1 | PROV_ID | PROV_GROUP | PROV_ID | No | No | No |  |
| 1 | PROV_ID | V_CUBE_D_PROVIDER | PROVIDER_ID | Unknown | Unknown | No |  |
| 11 | RPT_GRP_SIX | ZC_SER_RPT_GRP_6 | RPT_GRP_SIX | No | No | No |  |
| 12 | RPT_GRP_SEVEN | ZC_SER_RPT_GRP_7 | RPT_GRP_SEVEN | No | No | No |  |
| 13 | RPT_GRP_EIGHT | ZC_SER_RPT_GRP_8 | RPT_GRP_EIGHT | No | No | No |  |
| 14 | RPT_GRP_NINE | ZC_SER_RPT_GRP_9 | RPT_GRP_NINE | No | No | No |  |
| 15 | RPT_GRP_TEN | ZC_SER_RPT_GRP_10 | RPT_GRP_TEN | No | No | No |  |
| 17 | USER_ID | CLARITY_EMP | USER_ID | Unknown | No | No |  |
| 17 | USER_ID | CLARITY_EMP_2 | USER_ID | Unknown | No | No |  |
| 17 | USER_ID | CLARITY_EMP_3 | USER_ID | Unknown | No | No |  |
| 17 | USER_ID | CLARITY_EMP_4 | USER_ID | No | No | No |  |
| 17 | USER_ID | CLARITY_EMP_DEMO | USER_ID | No | No | No |  |
| 17 | USER_ID | EMP_BASIC_INFO | USER_ID | No | No | No |  |
| 17 | USER_ID | EMP_DOC_SETTINGS | USER_NUMBER_ID | No | No | No |  |
| 17 | USER_ID | F_RX_USER | USER_ID | Unknown | Unknown | No |  |
| 17 | USER_ID | IB_MESSAGE_SETTINGS | USER_ID | No | No | No |  |
| 17 | USER_ID | LOGIN_INFO | USER_NUMBER_ID | No | No | No |  |
| 17 | USER_ID | QC_RESULTS_REVIEW | USER_NUMBER_ID | No | No | No |  |
| 17 | USER_ID | USER_SIDEBAR_RPT | USER_NUMBER_ID | Unknown | No | No |  |
| 17 | USER_ID | V_CUBE_D_USER | USER_ID | Unknown | Unknown | No |  |

_(244 total; showing first 30)_
