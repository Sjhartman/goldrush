# COVERAGE

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=COVERAGE

## Description

The COVERAGE table contains high-level information on both managed care and indemnity coverage records in your system.

**Primary table** in this group (116 cols). Overflow siblings joined on shared key: COVERAGE_2 (91 cols), COVERAGE_3 (62 cols), COVERAGE_4 (101 cols), COVERAGE_5 (20 cols), COVERAGE_6 (6 cols). Prefer this table for most queries.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | CVG |
| Release Version | EPIC 2000 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| COVERAGE_ID | NUMERIC (18,0) | The unique ID assigned to the coverage record. This ID may be encrypted if you have elected to use enterprise reporting?s encryption utility. |
| COVERAGE_TYPE_C | INTEGER |  |
| COVERAGE_STATUS_C *(deprecated)* | INTEGER |  |
| CARRIER_ID *(deprecated)* | VARCHAR (18) |  |
| PAYOR_ID | NUMERIC (18,0) | This column is only populated for indemnity coverages (COVERAGE_TYPE_C equal to 1). This column stores the unique identifier of the payor associated with the coverage record.  To look up the payor for managed care coverages (COVERAGE_TYPE_C equal to 2), join COVERAGE.COVERAGE_ID on V_COVERAGE_PAYOR_PLAN.COVERAGE_ID and filter on V_COVERAGE_PAYOR_PLAN.EFF_DATE and V_COVERAGE_PAYOR_PLAN.TERM_DATE to find the relevant PAYOR_ID. |
| PLAN_ID | NUMERIC (18,0) | This column is only populated for indemnity coverages (COVERAGE_TYPE_C equal to 1). This column stores the unique identifier of the benefit plan associated with the coverage record.  To look up the benefit plan for managed care coverages (COVERAGE_TYPE_C equal to 2), join COVERAGE.COVERAGE_ID on V_COVERAGE_PAYOR_PLAN.COVERAGE_ID and filter on V_COVERAGE_PAYOR_PLAN.EFF_DATE and V_COVERAGE_PAYOR_PLAN.TERM_DATE to find the relevant BENEFIT_PLAN_ID. |
| PLAN_GRP_ID | VARCHAR (35) | The ID of the employer group that determines the benefits in a managed care coverage. This item is NULL for indemnity coverages. |
| SUBSCR_NUM | VARCHAR (50) | The identification number assigned to the subscriber for the coverage. When the subscriber is also a member on the coverage, this is the same as the subscriber?s member number. This column may be hidden if you have elected to use enterprise reporting?s security utility. |
| ACCT_ID *(deprecated)* | NUMERIC (18,0) | This column is deprecated, and does not accurately represent the accounts on a coverage. The list of accounts on a coverage is stored in CVG-41, which is extracted to the CVG_ACCT_LIST table. |
| SUBSCR_NAME | VARCHAR (200) | The name of the subscriber for the coverage. This column may be hidden if you have elected to use enterprise reporting?s security utility. |
| COBRA_STATUS_YN | VARCHAR (1) |  |
| COBRA_DATE | DATETIME | The termination date for any COBRA arrangement. |
| LATE_ENROLL_YN | VARCHAR (1) |  |
| STUDENT_REVIEW_DT | DATETIME | The date on which you should review the status of any members on this coverage who are students. |
| EMPLOYMENT_DATE | DATETIME | The date on which the subscriber began working for the employer associated with the employer group. |
| APPLICATION_DATE | DATETIME | The date on which the subscriber applied for coverage. |
| EPIC_CVG_ID | NUMERIC (18,0) | The unique ID of the coverage record. This column may be hidden if you have elected to use enterprise reporting?s security utility. |
| PB_ACCT_ID | VARCHAR (18) | The unique ID of premium billing account associated with the coverage. |
| SUBSCR_BIRTHDATE | DATETIME | The date of birth for the subscriber on the coverage. |
| SUBSCR_SEX_C | VARCHAR (66) |  |
| SUBSCR_ADDR1 *(deprecated)* | VARCHAR (80) |  |
| SUBSCR_ADDR2 *(deprecated)* | VARCHAR (80) |  |
| SUBSCR_CITY | VARCHAR (50) | The city of the mailing address for the subscriber on the coverage. |
| SUBSCR_STATE_C | VARCHAR (66) |  |
| SUBSCR_COUNTRY_C | VARCHAR (66) |  |
| SUBSCR_ZIP | VARCHAR (50) | The postal code of the mailing address for the subscriber on the coverage. |
| SUBSCR_PHONE | VARCHAR (50) | The home phone number for the subscriber on the coverage. |
| SUBSCRIBER_FAX | VARCHAR (25) | The fax number for the subscriber on the coverage. |
| SUBSCR_WORK_PHONE | VARCHAR (50) | The work phone number for the subscriber on the coverage. |
| CVG_EFF_DT | DATETIME | The effective date of the coverage. |
| CVG_TERM_DT | DATETIME | The termination date of the coverage. |
| SUBSCR_COUNTY_C | VARCHAR (66) |  |
| CASEHEAD_NUMBER | VARCHAR (40) | The Medicaid ID number on the case head. |
| CASEHEAD_NAME | VARCHAR (40) | The Medicaid name on the case head. |
| DT_LAST_PRO_RATED *(deprecated)* | DATETIME | *** Deprecated *** The deprecated column's content/data is no longer available since it is no longer populated in Chronicles. |
| TNSFRD_COVERAGE_ID | NUMERIC (18,0) | The ID of the coverage from which this coverage is transferred from. |
| UPDATE_DATE | No | *** Deprecated *** This column should no longer be used to track updates to COVERAGE.  Change the "Track row updates?" setting to "Yes" in the Information Activity to enable capturing of row updates on COVERAGE using ESP_CR_ALTERED_ROWS.  ****** The extract date and time of the record for this table. |
| SUBSC_RACE_C | INTEGER |  |
| SUB_MARITAL_STS_C | INTEGER |  |
| IS_SUB_US_CITZN_YN | VARCHAR (1) |  |
| CVG_REG_STATUS_C | VARCHAR (66) |  |
| LAST_DATE_VERIFIED | DATETIME | The last date the coverage was verified. |
| NEXT_REVIEW_DATE | DATETIME | The date on which this coverage should next be verified. This is calculated every time the coverage is verified. |
| VERIFY_USER_ID | VARCHAR (18) | The ID of the user who performed the verification. |
| VERIFY_SOURCE_C | INTEGER |  |
| SUBSCR_EMPLOYER_ID | VARCHAR (254) | This is the unique ID of the employer of the patient subscribing to the coverage if EAF 6410 is set to 1. This is free text if EAF 6410 is set to 2. |
| GROUP_NAME | VARCHAR (254) | The name of the coverage group. |
| CVG_ADDR1 | VARCHAR (254) | The first line of the address of the coverage (administrative offices). |
| CVG_ADDR2 | VARCHAR (254) | The second line of the address of the coverage (administrative offices). |
| CVG_CITY | VARCHAR (40) | The city of the mailing address of the coverage (administrative offices). |
| STATE_C | VARCHAR (66) |  |
| CVG_ZIP | VARCHAR (50) | The zip code of the mailing address of the coverage (administrative offices). |
| CVG_PHONE1 | VARCHAR (50) | The primary phone number of the coverage (administrative offices). |
| SUBSCR_SSN | VARCHAR (192) | The SSN number of the subscriber on a coverage |
| SUBSCR_EEP_ADDR_1 | VARCHAR (80) | This column, although not deprecated, should no longer be used. Instead you should use the column SUBSCR_EMPR_ADDR (CVG 236) in table CVG_SUBSCR_EMPR_ADDR. The address can contain an unlimited number of lines. Previously you could only access the first two lines with the columns COVERAGE.SUBSCR_EEP_ADDR_1 and COVERAGE.SUBSCR_EEP_ADDR_2. The table CVG_SUBSCR_EMPR_ADDR allows you to get all lines of the coverage subscriber's employer address. We have chosen not to deprecate COVERAGE.SUBSCR_EEP_ADDR_1 and COVERAGE.SUBSCR_EEP_ADDR_2  because doing so would break any custom reports that use these columns. |
| SUBSCR_EEP_ADDR_2 | VARCHAR (80) | This column, although not deprecated, should no longer be used. Instead you should use the column SUBSCR_EMPR_ADDR (CVG 236) in table CVG_SUBSCR_EMPR_ADDR. The address can contain an unlimited number of lines. Previously you could only access the first two lines with the columns COVERAGE.SUBSCR_EEP_ADDR_1 and COVERAGE.SUBSCR_EEP_ADDR_2. The table CVG_SUBSCR_EMPR_ADDR allows you to get all lines of the coverage subscriber's employer address. We have chosen not to deprecate COVERAGE.SUBSCR_EEP_ADDR_1 and COVERAGE.SUBSCR_EEP_ADDR_2  because doing so would break any custom reports that use these columns. |
| SUBSCR_EEP_CITY | VARCHAR (50) | The City field of the subscriber's employer's address on the coverage. |
| SUBSCR_EEP_STE_C | VARCHAR (66) |  |
| SUBSCR_EEP_ZIP | VARCHAR (50) | The zip code of the subscriber's employer's address on a coverage |
| SUBSCR_EEP_PHONE | VARCHAR (50) | The phone number of the subscriber's employer on a coverage |
| SUBSCR_EMP_STAT_C | INTEGER |  |
| GROUP_NUM | VARCHAR (254) | The identification number assigned to this subscriber's employer/plan group by the payor.  This number will appear in box 11 of the HCFA claim form. |
| CLAIM_MAIL_CODE_C | INTEGER |  |
| CM_PHY_OWNER_ID | VARCHAR (25) | ID of the physical deployment owner for this record.  Physical owners will be where the data is hosted, either on the cross-over server or the owner deployment. |
| CM_LOG_OWNER_ID | VARCHAR (25) | ID of the logical deployment owner for this record.  Logical owners show the deployment where the record was created but doesn't represent if the record is a part of version skew. |
| WEB_APN_ID | VARCHAR (18) | The unique ID of the web application if the coverage is created based on a web application. |
| WC_EMPLOYER_ID | VARCHAR (254) | Workers' compensation employer at the time of injury. |
| WC_DATE_OF_INJURY | DATETIME | Workers Comp date of injury. This is the date the injury occurred on the job. This field is populated as the user sets up the WC account. |
| IS_SIG_ON_FILE_YN | VARCHAR (1) |  |
| ENROLL_REASON_C | INTEGER |  |
| CVG_TERM_REASON_C | INTEGER |  |
| SUBSCR_EMPR_ID_CMT | VARCHAR (254) | A free text comment that can be entered when the value that is considered to be "Other" is selected as the employer. This option is available only if your organization has chosen to link the subscriber employer to the Employer (EEP) master file in the Facility Profile. |
| PAT_REC_OF_SUBS_ID | VARCHAR (18) | If the subscriber is the same person as a patient, this item contains the patient ID. |
| ECD_TABLE_DEF_COPAY | NUMERIC (18,2) | Numeric default copay value. |
| COINSURANCE_OVR | NUMERIC (3,0) | Numeric Value for the coverage level coinsurance override. |
| SUBSCR_HOUSE_NUM | VARCHAR (254) | Subscriber House Number for non-US locales |
| MEDC_COVERED_LEFT | NUMERIC (18,0) | This is the number of Medicare Covered Days Remaining |
| MEDC_COINS_LEFT | NUMERIC (18,0) | This is the number of Medicare Coinsurance Days Remaining |
| MEDC_RESERVE_LEFT | NUMERIC (18,0) | This is the number of Medicare Reserved Days Remaining |
| CCS_PAT_ID | VARCHAR (254) | The patient's Comprehensive Community Services (CCS) ID. |
| CCS_DX | VARCHAR (254) | Stores the diagnosis that makes the patient eligible for Comprehensive Community Services (CCS) coverage. |
| CCS_CC_NAME | VARCHAR (254) | Stores the name of the Comprehensive Community Services (CCS) Case Coordinator. |
| CCS_COOR_PHONE | VARCHAR (254) | Stores the phone number for the Comprehensive Community Services (CCS) Case Coordinator. |
| CCS_COUNTY_PHONE | VARCHAR (254) | Stores the phone number for the Comprehensive Community Services (CCS) County Office. |
| CVG_COUNTY_C | VARCHAR (66) |  |
| CVG_COUNTRY_C | VARCHAR (66) |  |
| CVG_HOUSE_NUM | VARCHAR (20) | The house number of the mailing address of the coverage (administrative offices). |
| CVG_DISTRICT_C | INTEGER |  |
| SUBSCR_EEP_CNTY_C | VARCHAR (66) |  |
| SUBSCR_EEP_HOUSE_N | VARCHAR (20) | The house number of the subscriber's employer's address on a coverage |
| SUBSCR_EEP_DIST_C | INTEGER |  |
| SUBSCR_DISTRICT_C | INTEGER |  |
| EFF_HOSP_CVG_DT | DATETIME | The effective date of Medicare Part A. |
| EFF_PROV_CVG_DT | DATETIME | The effective date of Medicare Part B. |
| MEDICARE_CVG_TYPE_C | INTEGER |  |
| MEDICARE_SUBSCR_ID | VARCHAR (254) | The unique ID of the subscriber that will be used for supplemental claims. |
| RQG_REL_TO_SUB_C | INTEGER |  |
| Q4CO_BUCKETS_EXC_YN | VARCHAR (1) |  |
| MED_SEC_TYPE_C | VARCHAR (66) |  |
| CHDP_COUNTY_C | VARCHAR (66) |  |
| CHDP_AID_CODE | VARCHAR (254) | The Child Health and Disability Prevention Aid Code. |
| SUBSC_REL_TO_GUAR_C | INTEGER |  |
| SUBSCR_EMPR_CNTRY_C | VARCHAR (66) |  |
| CVG_CARD_ISSUE_DT | DATETIME | Stores the card issue date. |
| CVG_DEDUCTIBLE_YN | VARCHAR (1) |  |
| FIRST_SPEC_AID_CODE | VARCHAR (254) | First special aid code for the Treatment Authorization Request (TAR) for Medi-Cal. |
| SEC_SPEC_AID_CODE | VARCHAR (254) | Second special aid code for the Treatment Authorization Request (TAR) for Medi-Cal. |
| THRD_SPEC_AID_CODE | VARCHAR (254) | Third special aid code for the Treatment Authorization Request (TAR) for Medi-Cal. |
| EVC_NUM | VARCHAR (254) | Eligibility Verification Confirmation (EVC) that is used on the Treatment Authorization Request (TAR) for Medi-Cal. |
| COUNTY_CODE_C | INTEGER |  |
| CVG_VERIFICATION_ID | NUMERIC (18,0) | The verification record of the coverage |
| EXT_ROUTING_NUM_C | VARCHAR (66) |  |
| CONF_NAM_OF_ASSC_PT | VARCHAR (192) | This item contains the confidential name of the associated patient, if it exists. The name is used to determine the confidential nature of the subscriber. |
| OWN_BUS_SEG_EAF_ID | NUMERIC (18,0) | Owning service area/business segment, for use in business segmentation |
| SUBSCR_OR_SELF_MEM_PAT_ID | VARCHAR (18) | This item contains the subscriber patient Id of a coverage and will be used to associate patients with linked premium billing accounts for EHI. |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| B-TREE INDEX | EIX_COVERAGE_APNID | WEB_APN_ID | 1 | Yes | Yes |  |
| BITMAP INDEX | EIX_COVERAGE_TYPE_PLAN_GRP | COVERAGE_TYPE_C | 1 | Yes | Yes |  |
| BITMAP INDEX | EIX_COVERAGE_TYPE_PLAN_GRP | PLAN_GRP_ID | 2 | Yes | No |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | COVERAGE_ID | COVERAGE_2 | CVG_ID | Unknown | No | No |  |
| 1 | COVERAGE_ID | COVERAGE_3 | CVG_ID | Unknown | No | No |  |
| 1 | COVERAGE_ID | COVERAGE_4 | CVG_ID | Unknown | No | No |  |
| 1 | COVERAGE_ID | COVERAGE_5 | CVG_ID | No | No | No |  |
| 1 | COVERAGE_ID | COVERAGE_6 | COVERAGE_ID | No | No | No |  |
| 1 | COVERAGE_ID | COVERAGE_MISC_COMMENTS | COVERAGE_ID | No | No | No |  |
| 1 | COVERAGE_ID | CVG_AP_CLAIMS | COVERAGE_ID | Unknown | No | No |  |
| 1 | COVERAGE_ID | V_EHI_COVERAGE_SUBS | COVERAGE_ID | Unknown | Unknown | No |  |
| 2 | COVERAGE_TYPE_C | ZC_COVERAGE_TYPE | COVERAGE_TYPE_C | No | No | No |  |
| 5 | PAYOR_ID | CLARITY_EPM | PAYOR_ID | No | No | No |  |
| 5 | PAYOR_ID | CLARITY_EPM_2 | PAYOR_ID | No | No | No |  |
| 5 | PAYOR_ID | CLARITY_EPM_3 | PAYOR_ID | No | No | No |  |
| 5 | PAYOR_ID | DENT_PAYER_BENEFITS_FLAGS | PAYOR_ID | No | No | No |  |
| 5 | PAYOR_ID | EPM_CLM_FILING_INF | PAYOR_ID | No | No | No |  |
| 5 | PAYOR_ID | EPM_CLM_FRM_OPTION | PAYOR_ID | No | No | No |  |
| 5 | PAYOR_ID | EPM_CLM_PRNT_OPTN | PAYOR_ID | No | No | No |  |
| 5 | PAYOR_ID | EPM_TAP_PAYOR_INFO | PAYOR_ID | No | No | No |  |
| 5 | PAYOR_ID | V_CUBE_D_PAYOR | PAYOR_ID | Unknown | Unknown | No |  |
| 6 | PLAN_ID | CLARITY_EPP | BENEFIT_PLAN_ID | No | No | No |  |
| 6 | PLAN_ID | CLARITY_EPP_2 | BENEFIT_PLAN_ID | No | No | No |  |
| 6 | PLAN_ID | CLARITY_EPP_3 | BENEFIT_PLAN_ID | No | No | No |  |
| 6 | PLAN_ID | CLARITY_EPP_CERTIF | BENEFIT_PLAN_ID | No | No | No |  |
| 6 | PLAN_ID | DENT_PLAN_BENEFITS_FLAGS | BENEFIT_PLAN_ID | No | No | No |  |
| 6 | PLAN_ID | V_CUBE_D_BENEFIT_PLAN | BENEFIT_PLAN_ID | Unknown | Unknown | No |  |
| 7 | PLAN_GRP_ID | PLAN_GRP | PLAN_GRP_ID | No | No | No |  |
| 17 | EPIC_CVG_ID | COVERAGE | COVERAGE_ID | Unknown | No | No |  |
| 17 | EPIC_CVG_ID | COVERAGE_2 | CVG_ID | Unknown | No | No |  |
| 17 | EPIC_CVG_ID | COVERAGE_3 | CVG_ID | Unknown | No | No |  |
| 17 | EPIC_CVG_ID | COVERAGE_4 | CVG_ID | Unknown | No | No |  |
| 17 | EPIC_CVG_ID | COVERAGE_5 | CVG_ID | No | No | No |  |

_(238 total; showing first 30)_
