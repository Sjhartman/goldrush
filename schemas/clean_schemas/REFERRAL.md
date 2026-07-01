# REFERRAL

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=REFERRAL

## Description

The REFERRAL table is the primary table for referral information stored in system.

**Primary table** in this group (112 cols). Overflow siblings joined on shared key: REFERRAL_2 (100 cols), REFERRAL_3 (52 cols), REFERRAL_4 (87 cols), REFERRAL_5 (99 cols), REFERRAL_6 (11 cols). Prefer this table for most queries.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | RFL |
| Release Version | EPIC 2000 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| REFERRAL_ID | NUMERIC (18,0) | The unique ID of the referral in database. This is the primary key for the REFERRAL table. |
| EXTERNAL_ID_NUM | VARCHAR (30) | The external identification number used on the referral. |
| PAT_ID | VARCHAR (18) | The ID of the patient associated with the referral. |
| PCP_PROV_ID | VARCHAR (18) | The unique ID of the patient's primary care provider at the time the referral was created. |
| ENTRY_DATE | DATETIME | The date the referral was entered. |
| RFL_STATUS_C | INTEGER |  |
| REFERRING_PROV_ID | VARCHAR (18) | The unique ID of the referral source (REF) record of the provider who made the referral. This column is frequently used to link to the REFERRAL_SOURCE table. The actual provider (SER) ID can be found in column REF_PROVIDER_ID of table REFERRAL_SOURCE. |
| VENDOR_ID | VARCHAR (18) | The ID number of the vendor associated with the referral. |
| REFERRAL_PROV_ID | VARCHAR (18) | The unique ID of the provider (SER) being referred to. This column is frequently used to link to the CLARITY_SER table. |
| PROV_SPEC_C | VARCHAR (66) |  |
| RFL_TYPE_C | VARCHAR (66) |  |
| RSN_FOR_RFL_C | VARCHAR (66) |  |
| RFL_CLASS_C | VARCHAR (66) |  |
| AUTH_VIS_PERIOD | INTEGER | The number of authorized visits in each visit period. |
| AUTH_PERIOD_TYPE_C | INTEGER |  |
| AUTH_NUM_PERIODS | INTEGER | The number of periods authorized for this referral. |
| AUTH_NUM_OF_VISITS | NUMERIC (10,2) | The number of visits authorized for this referral. |
| ADMISSION_DATE | DATETIME | The admission date associated with the referral. |
| DISCHARGE_DATE | DATETIME | The discharge date associated with the referral. |
| ESTIMATED_DAYS | INTEGER | The authorized length of stay if the patient is being admitted. |
| OVERRIDE_DAYS *(deprecated)* | INTEGER | The actual length of stay.  This column is deprecated as "Length of Stay" has been renamed as "Bed Days". The data can now be found in I RFL 2074. |
| START_DATE | DATETIME | The start date of the referral. |
| EXP_DATE | DATETIME | The expiration date of the referral. |
| PEND_TO | VARCHAR (40) | The person or pool to whom an In Basket message should be sent about this referral. |
| PEND_RSN_C | INTEGER |  |
| DENY_RSN_C | INTEGER |  |
| SERV_AREA_ID | NUMERIC (18,0) | The ID number of the service area associated with the referral. |
| COVERAGE_ID | NUMERIC (18,0) | The unique ID of the coverage associated with the referral. |
| NUM_PROC | NUMERIC (18,0) | The number of procedures associated with the referral. |
| SVC_DATE_REAL | No | If available, this column is populated by the authorized start date (I RFL 85). If not, it is populated by the expiration date on the referral (I RFL 90). If neither of these are available, the column will be empty. The date in this column is based on days since December 31, 1840. |
| CARRIER_ID | No | The ID number of the carrier associated with the referral. |
| PAYOR_ID | No | The ID number of the payor associated with the referral. |
| PLAN_ID | No | The ID number of the plan associated with the referral. |
| SERV_DATE | No | This column is populated by the authorized start date (I RFL 85) if available. If not, it is populated by the expiration date on the referral (I RFL 90). If neither of these are available, the column will be empty. The date in this column is in MM/DD/YYYY format. |
| RETRO_FLAG_YN | VARCHAR (1) |  |
| IBNR | NUMERIC (12,2) | The "Incurred but not reported" amount associated with this referral. |
| AUTO_APPROVED_DATE | DATETIME | The date on which the referral was approved automatically by the system. |
| AUTH_RSN_C | VARCHAR (66) |  |
| REFD_BY_LOC_POS_ID | NUMERIC (18,0) | The ID number of the place of service the referral was referred from. |
| REFD_TO_LOC_POS_ID | NUMERIC (18,0) | The ID number of the place of service the referral was referred to. |
| REFD_TO_DEPT_ID | NUMERIC (18,0) | The ID number of the department the referral was referred to. |
| REFD_TO_SPEC_C | VARCHAR (66) |  |
| PRIORITY_C | VARCHAR (66) |  |
| TOTAL_PRICE | NUMERIC (12,2) | The total cost of the procedures authorized under the referral. |
| TOTAL_PAYABLE | NUMERIC (12,2) | The portion of the total price for which your facility is responsible. |
| PATIENT_AMOUNT | NUMERIC (12,2) | The total patient liability, under the parameters of the primary coverage used, for the procedures authorized under the referral. |
| EXPECT_TO_PAY | NUMERIC (12,2) | The total amount you expect your facility will pay for the procedures authorized under the referral. This amount entered by you overrides the total payable amount for the purpose of calculating IBNR. |
| IBNR_PAY_UNTIL_DT | DATETIME | The date up to which your facility will pay claims for the procedures approved on this referral. |
| CASE_RATE_YN | VARCHAR (1) |  |
| PRIM_LOC_ID | NUMERIC (18,0) | The unique ID of the member's primary location at the time the referral was entered. |
| MED_TYPE_C *(deprecated)* | INTEGER |  |
| ACUTE_AMOUNT | NUMERIC (12,2) | The amount of the confirmation if the confirmation is acute. |
| CHRONIC_AMOUNT | NUMERIC (12,2) | The amount of the confirmation if the confirmation is chronic. |
| PAT_AMOUNT | NUMERIC (12,2) | The amount of the confirmation if the confirmation is an acute medication that was suggested by the pharmacist or over-the-counter medication. |
| UPDATE_DATE | No | The instant of time when the referral was last updated. |
| RFL_LOB_ID | VARCHAR (18) | ID of the Line of Business (LOB) assigned to the referral. |
| ACTUAL_NUM_VISITS | NUMERIC (10,2) | The actual number of completed visits for this referral. |
| SCHED_NUM_VISITS | NUMERIC (10,2) | The number of visits scheduled for this referral. |
| REQUEST_NUM_VISITS | NUMERIC (10,2) | The number of visits requested for this referral. |
| GUIDELINE_DAYS | NUMERIC (8,2) | Guideline days for this referral. |
| OVRD_ADMIT_DATE | DATETIME | Override admit date for this referral. |
| OVRD_DISCHARGE_DT | DATETIME | Override discharge date for this referral. |
| DISP_VAL_C | INTEGER |  |
| DISP_RSN_C | INTEGER |  |
| DISP_EAF_ID | NUMERIC (18,0) | The unique id of the facility to which the referral was forwarded. |
| CM_PHY_OWNER_ID | VARCHAR (25) | ID of the physical deployment owner for this record.  Physical owners will be where the data is hosted, either on the cross-over server or the owner deployment. |
| CM_LOG_OWNER_ID | VARCHAR (25) | ID of the logical deployment owner for this record.  Logical owners show the deployment where the record was created, but don't represent the logical owner if the record is a part of the version skew. |
| REFD_BY_DEPT_ID | NUMERIC (18,0) | The ID number of the department the referral was referred by. |
| CLOSE_RSN_C | VARCHAR (66) |  |
| RECORD_STATUS_C | INTEGER |  |
| SCHED_STATUS_C | INTEGER |  |
| SCHED_BY_DATE | DATETIME | Indicates deadline to schedule a referral. |
| PREAUTH_REQ_C | INTEGER |  |
| NOT_COLLCTD_RSN_C | INTEGER |  |
| PREAUTH_DEFER_DT | DATETIME | Set by the user to indicate they don't want to see the record until that date on the preauthorization workqueue report. |
| PROCESSED_RSN_C | INTEGER |  |
| PREAUTH_CHG_EMP_ID | VARCHAR (18) | The unique ID of the user who last changed the preauthorization data. |
| PREAUTH_CHNGD_DTTM | DATETIME (Local) | Date/time stamp for last time the preauthorization data was changed. |
| AUTH_NUM | VARCHAR (254) | Authorization number. |
| PRE_CERT_NUM | VARCHAR (254) | Pre-certification number. |
| NON_PREF_PROV_RSN_C | INTEGER |  |
| EXT_REF_DATE | DATETIME | This is the external referring date. |
| EOW_ID | VARCHAR (18) | The unique EOW ID associated with the referral. |
| IB_STATUS_EXPLAN | VARCHAR (254) | The IB status explanation for the referral. |
| REQ_VIS_PER_PERIOD | INTEGER | The requested visits per period on the referral. |
| REQ_PERIOD_TYPE_C | INTEGER |  |
| REQ_NUM_OF_PERIODS | INTEGER | The requested number of periods on the referral. |
| REF_FROM_ECI_ID | VARCHAR (25) | Used by Chart Sync to determine the referring deployment, so that a "ping pong" message can be sent to them. |
| PREV_REF_FRM_ECI_ID | VARCHAR (25) | Used by Chart Sync to determine the previously referring deployment. |
| EOW_ON_ECI_ID | VARCHAR (25) | The unique ID of the deployment where the referral verification message should be generated. This is used for Cross Deployment messaging. |
| REF_TO_PROV_ADDR_ID | VARCHAR (254) | This stores the address ID of the referred to provider. The format is as follows: ProvID-AddressID. AddressID is the line number of the multiple response address items in the SER masterfile. To use this column, join to CLARITY_SER_ADDR on REFERRAL.REF_TO_PROV_ADDR_ID = CLARITY_SER_ADDR.ADDR_UNIQUE_ID. If you use IntraConnect, also join on REFERRAL.REFERRAL_PROV_ID = CLARITY_SER_ADDR.PROV_ID. |
| REF_TO_ECI_ID | VARCHAR (25) | Used by Chart Sync to determine the referred to deployment. |
| DECISION_DATE | DATETIME | Date on which the referral's current status was assigned. |
| NUM_CLMS_EXPECTED | INTEGER | Number of claims expected to be filed on this referral. |
| RFL_STATCHG_RSN_C | VARCHAR (66) |  |
| RFL_SENS_C | INTEGER |  |
| TOTAL_EST_DAYS | NUMERIC (18,2) | Total estimated days for the referral. |
| TOTAL_OVERRIDE_DAYS | NUMERIC (18,2) | The total number of override days on the referral. |
| TOTAL_CONVTD_DAYS | NUMERIC (18,2) | The total number of converted days on the referral. |
| AMT_CLMS_ADJUDICTD | NUMERIC (18,2) | The amount of claims adjudicated. |
| AMT_CLMS_PAID | NUMERIC (18,2) | The amount of claims paid. |
| ADJ_VENDOR_ID | VARCHAR (18) | The adjudication vendor. |
| ADJ_MEMBER_GROUP_ID | VARCHAR (18) | Adjudication member group. |
| ADJ_NET_STATUS_C | VARCHAR (66) |  |
| NO_CLAIMS_PAID | NUMERIC (18,2) | The number of claims paid on the claim. |
| CVG_REFRESH_DATE | DATETIME | Coverage refresh date. |
| ENTRY_SOURCE_C | INTEGER |  |
| IS_COPY | NUMERIC (18,0) |  |
| SUPPRESS_EXP_WAR_YN | VARCHAR (1) |  |
| ADJUD_SERV_AREA_ID | NUMERIC (18,0) | Service area used in referral pricing and adjudication. |
| PREV_REF_TO_ECI_ID | VARCHAR (25) | Used by Chart Sync to determine the previously referred to deployment, so that a ping pong message can be sent to them. |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| B-TREE INDEX | EIX_REFERRAL_ENTRY_DATE | ENTRY_DATE | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_REFERRAL_PAID | PAT_ID | 1 | Yes | Yes |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | REFERRAL_ID | EPA_INFO | REFERRAL_ID | No | No | No |  |
| 1 | REFERRAL_ID | EPA_INFO_2 | REFERRAL_ID | No | No | No |  |
| 1 | REFERRAL_ID | F_REFERRAL_PRICE | REFERRAL_ID | Unknown | Unknown | No |  |
| 1 | REFERRAL_ID | REFERRAL_2 | REFERRAL_ID | Unknown | No | No |  |
| 1 | REFERRAL_ID | REFERRAL_3 | REFERRAL_ID | Unknown | No | No |  |
| 1 | REFERRAL_ID | REFERRAL_4 | REFERRAL_ID | Unknown | No | No |  |
| 1 | REFERRAL_ID | REFERRAL_5 | REFERRAL_ID | No | No | No |  |
| 1 | REFERRAL_ID | REFERRAL_6 | REFERRAL_ID | No | No | No |  |
| 1 | REFERRAL_ID | RFL_GROUP_INFO | REFERRAL_ID | No | No | No |  |
| 1 | REFERRAL_ID | V_ECL_REFERRALS | REFERRAL_ID | Unknown | Unknown | No |  |
| 1 | REFERRAL_ID | V_EPA_DATA | REFERRAL_ID | Unknown | Unknown | No |  |
| 1 | REFERRAL_ID | V_HH_REFERRALS | REFERRAL_ID | Unknown | Unknown | No |  |
| 1 | REFERRAL_ID | V_REFERRAL_CYCLE_TIME | REFERRAL_ID | Unknown | Unknown | No |  |
| 1 | REFERRAL_ID | V_VIC_ACCESS_POLICY_TARGETS | REFERRAL_ID | Unknown | Unknown | No |  |
| 3 | PAT_ID | ANTICOAG_SELF_REGULATING | PAT_ID | No | No | No |  |
| 3 | PAT_ID | CARE_COORDINATION | PAT_ID | Unknown | No | No |  |
| 3 | PAT_ID | CLAIMS_DERIVE_PAT_FLAGS | PAT_ID | No | No | No |  |
| 3 | PAT_ID | COMMUNITY_RESRC_REVIEWED | PAT_ID | No | No | No |  |
| 3 | PAT_ID | D_PAT_GEOGRAPHIC_CLASS | PAT_ID | Unknown | Unknown | No |  |
| 3 | PAT_ID | EPT_MEM_INFO | PAT_ID | No | No | No |  |
| 3 | PAT_ID | EXT_DATA_LAST_DONE | PAT_ID | No | No | No |  |
| 3 | PAT_ID | F_IBD_ADULT_FORM_PAT | PAT_ID | Unknown | Unknown | No |  |
| 3 | PAT_ID | HH_PAT_INFO | PAT_ID | Unknown | No | No |  |
| 3 | PAT_ID | HM_STATUS_UPD | PAT_ID | No | No | No |  |
| 3 | PAT_ID | IMMNZTN_LAST_REVIEW | PAT_ID | No | No | No |  |
| 3 | PAT_ID | PATIENT | PAT_ID | No | No | No |  |
| 3 | PAT_ID | PATIENT_2 | PAT_ID | No | No | No |  |
| 3 | PAT_ID | PATIENT_3 | PAT_ID | No | No | No |  |
| 3 | PAT_ID | PATIENT_4 | PAT_ID | No | No | No |  |
| 3 | PAT_ID | PATIENT_5 | PAT_ID | No | No | No |  |

_(402 total; showing first 30)_
