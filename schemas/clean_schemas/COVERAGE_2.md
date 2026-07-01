# COVERAGE_2

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=COVERAGE_2

## Description

The COVERAGE_2 table contains high-level information on both managed care and indemnity coverage records in your system.

**Overflow table** for COVERAGE (116 cols). Contains additional columns for the same records — join on the shared primary key column.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | CVG |
| Release Version | Summer 2009 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| CVG_ID | NUMERIC (18,0) | The unique identifier for the coverage record. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| STATUS_C | INTEGER |  |
| RETRO_QUEUE_FLAG | VARCHAR (254) | The retroadjudication queue flag for the coverage. Indicates if the coverage should be queued for retroadjudication from self-pay to insurance. 1 if the coverage is newly created and the only coverage on its account. |
| COPAY_INFO | VARCHAR (254) | Notes regarding copay information for this coverage. |
| IS_DEDUCT_MET_C | INTEGER |  |
| IS_ASGN_CVG_C | INTEGER |  |
| SIG_ON_FILE_DATE | DATETIME | The date when the signature was filed. |
| SIG_ON_FILE_LOC | VARCHAR (254) | The location at which the signature was filed. |
| MEDIGAP_AUTH_YN | VARCHAR (1) |  |
| TPL_RESOURCE_CODE | VARCHAR (254) | This column lists the Third Party Liability resource code for a specific plan. This code is either returned in the real-time eligibility response or found on the patient's insurance card. |
| THIRD_PARTY_LIAB_YN | VARCHAR (1) |  |
| BENEFIT_CODE | VARCHAR (254) | The benefit code for this coverage. This can contain any facility-specific benefit code. |
| SUBSCR_EMPLOYER_FAX | VARCHAR (254) | The fax number of the coverage subscriber's employer. |
| EMPLOYEE_ID_NUM | VARCHAR (254) | The coverage subscriber's employee ID number. |
| SUBSCR_OCCUPATION | VARCHAR (254) | The coverage subscriber's occupation. |
| SUBSC_RETIRE_DT | DATETIME | The date when the coverage subscriber retired. |
| SUBSC_SPS_RETIRE_DT | DATETIME | The date when the coverage subscriber's spouse retired. |
| SCHEDULED_DISCON_DT | DATETIME | The date when the coverage is scheduled to be discontinued. |
| SCHEDULED_ACTV_DT | DATETIME | The date when the coverage is scheduled to be activated. |
| VERIFY_PROMPT_YN | VARCHAR (1) |  |
| YR_ALLOW_DOL_TOT | VARCHAR (254) | The yearly dollar limit for payments against this coverage's payor. |
| YR_ALLOW_DOL_USE | VARCHAR (254) | The year-to-date payments made against the coverage's payor. |
| ORG_FOR_CLM_SUBMIT | VARCHAR (254) | The title or name of the organization to which submitted claims under this coverage will be sent. |
| FINANCIAL_CLASS_C | VARCHAR (66) |  |
| COVERAGE_FAX | VARCHAR (254) | The fax number for this coverage. |
| FREE_TXT_PLAN_NAME | VARCHAR (254) | The free-text plan name for this coverage. |
| FREE_TXT_PAYOR_NAME | VARCHAR (254) | The free-text payor name for this coverage. |
| CVG_CPY_SRC_ID | NUMERIC (18,0) | The ID of the coverage from which this coverage was copied. |
| PLAN_FREE_TEXT | VARCHAR (254) | The format of the coverage's free-text plan. |
| TEFRA_PAT_YN | VARCHAR (1) |  |
| ADMISSION_SRC_C | INTEGER |  |
| ENROLL_CODE_FBC | VARCHAR (254) | The Federal Employment Program enrollment code. |
| GRP_NUMBER | VARCHAR (254) | The group number for the coverage. |
| HMO_SITE_NUM | VARCHAR (254) | The site number for the coverage's HMO. |
| HMO_SITE_PHONE | VARCHAR (254) | The phone number for the coverage's HMO. |
| ALT_SUBSCR_BILL_NAM | VARCHAR (254) | The alternate billing name for the coverage subscriber. |
| COPAY_AMOUNT | VARCHAR (254) | The copay amount for the coverage. |
| CHAMPUS_SUBSCR_STAT | VARCHAR (254) | The CHAMPUS/Tricare subscriber status. |
| CHAMP_SPON_STATUS_C | VARCHAR (66) |  |
| SERVICE_BRANCH | VARCHAR (254) | The military service branch for a CHAMPUS/Tricare coverage subscriber. |
| CHAMP_SPON_BRANCH_C | VARCHAR (66) |  |
| CHAMP_SPON_GRADE_C | VARCHAR (66) |  |
| MCARE_OTHER_INS_CO | VARCHAR (254) | An additional insurance company providing coverage for a Medicare patient. |
| MCARE_REC_DIS_YN | VARCHAR (1) |  |
| DIS_CVD_BY_EMP_YN | VARCHAR (1) |  |
| MCARE_100_EMP_YN | VARCHAR (1) |  |
| MCARE_AUTO_YN | VARCHAR (1) |  |
| MCARE_LIAB_YN | VARCHAR (1) |  |
| MCARE_WK_COMP_YN | VARCHAR (1) |  |
| MCARE_NON_AUTO_YN | VARCHAR (1) |  |
| MCARE_BLACK_LUNG_YN | VARCHAR (1) |  |
| MCARE_VA_YN | VARCHAR (1) |  |
| MCARE_PARENT_EMP_YN | VARCHAR (1) |  |
| MCARE_CVD_GD_YN | VARCHAR (1) |  |
| MCARE_GD_EMP_100_YN | VARCHAR (1) |  |
| IS_MCARE_VET_ADMN_C | VARCHAR (66) |  |
| MCARE_EMPLOYED_YN | VARCHAR (1) |  |
| MCARE_ENRL_HMO_YN | VARCHAR (1) |  |
| MCARE_CVD_EGHP_YN | VARCHAR (1) |  |
| MCARE_EMP_20_YN | VARCHAR (1) |  |
| MCARE_REN_DIAL_YN | VARCHAR (1) |  |
| IS_MCARE_RENAL_DI_C | VARCHAR (66) |  |
| MCARE_1ST_18MO_YN | VARCHAR (1) |  |
| MCARE_HOME_DIAL_YN | VARCHAR (1) |  |
| MCARE_SELF_EPO_YN | VARCHAR (1) |  |
| MCARE_DISABLE_YN | VARCHAR (1) |  |
| MCARE_SPSE_RET_YN | VARCHAR (1) |  |
| MCARE_SPOUSE_RET_DT | DATETIME | The date when a Medicare patient's spouse retired. |
| MCARE_EMPR_INS_YN | VARCHAR (1) |  |
| MCARE_RETIRE_YN | VARCHAR (1) |  |
| MCARE_RETIRE_DATE | DATETIME | The date when a Medicare patient retired. |
| MCARE_FAM_EMPY_YN | VARCHAR (1) |  |
| MCARE_OTHR_CVG_YN | VARCHAR (1) |  |
| MCARE_SPC_EMP_YN | VARCHAR (1) |  |
| MCARE_CVG_FRM_SP_YN | VARCHAR (1) |  |
| VERIF_EVS_YN | VARCHAR (1) |  |
| EVS_VERIF_DATE | DATETIME | The date when eligibility was verified with Eligibility Verification Systems (EVS). |
| PAYOR_NAME | VARCHAR (254) | The coverage payor's name. |
| PAYOR_CITY | VARCHAR (254) | The coverage payor's city. |
| SUBSCRIBER_BNK_ID | VARCHAR (18) | Banking details of the subscriber. |
| EXT_CVG_SRC_ORGANIZATION_ID | NUMERIC (18,0) | The Organization (DXO) that provided the information for this coverage. |
| EXT_CVG_FHIR_IDENT | VARCHAR (255) | The FHIR Id of a coverage record on an external system that was used to  create this coverage. |
| EXT_CVG_OID | VARCHAR (254) | The OID of a coverage record on an external system that was used to create  this coverage. |
| EXT_PAYER_NAME | VARCHAR (254) | Payer name received for a coverage from an external payer system. |
| EXT_PLAN_NAME | VARCHAR (254) | Plan name received for a coverage from an external payer system. |
| EXT_PLAN_LOGO_FHIR_IDENT | VARCHAR (184) | Plan logo binary FHIR ID received for a coverage from an external payer system. |
| EXT_REFERENCE_PAYER_C | INTEGER |  |
| EXT_REFERENCE_FIN_CLASS_C | INTEGER |  |
| EXT_PAYER_LOB_TYPE_C | INTEGER |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | CVG_ID | COVERAGE | COVERAGE_ID | Unknown | No | No |  |
| 1 | CVG_ID | COVERAGE_3 | CVG_ID | Unknown | No | No |  |
| 1 | CVG_ID | COVERAGE_4 | CVG_ID | Unknown | No | No |  |
| 1 | CVG_ID | COVERAGE_5 | CVG_ID | No | No | No |  |
| 1 | CVG_ID | COVERAGE_6 | COVERAGE_ID | No | No | No |  |
| 1 | CVG_ID | COVERAGE_MISC_COMMENTS | COVERAGE_ID | No | No | No |  |
| 1 | CVG_ID | CVG_AP_CLAIMS | COVERAGE_ID | Unknown | No | No |  |
| 1 | CVG_ID | V_EHI_COVERAGE_SUBS | COVERAGE_ID | Unknown | Unknown | No |  |
| 2 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 2 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 2 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 3 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 4 | STATUS_C | ZC_DEL_STATUS | DEL_STATUS_C | No | No | No |  |
| 4 | STATUS_C | ZC_EDG_REC_STAT | EDG_REC_STAT_C | No | No | No |  |
| 4 | STATUS_C | ZC_ERS_REC_STAT | RECORD_STATUS_C | No | No | No |  |
| 4 | STATUS_C | ZC_HCD_REC_STATE | HCD_REC_STATE_C | No | No | No |  |
| 4 | STATUS_C | ZC_HFL_RECORD_STAT | HFL_RECORD_STAT_C | No | No | No |  |
| 4 | STATUS_C | ZC_IMM_REC_STATUS | IMM_REC_STATUS_C | No | No | No |  |
| 4 | STATUS_C | ZC_LLB_STATUS | LLB_STATUS_C | No | No | No |  |
| 4 | STATUS_C | ZC_LMA_RECORD_STAT | LMA_RECORD_STAT_C | No | No | No |  |
| 4 | STATUS_C | ZC_MEM_REC_STATUS | MEM_REC_STATUS_C | No | No | No |  |
| 4 | STATUS_C | ZC_OR_REC_STATUS | OR_REC_STATUS_C | No | No | No |  |
| 4 | STATUS_C | ZC_PBA_REC_STAT | PBA_REC_STAT_C | No | No | No |  |
| 4 | STATUS_C | ZC_PROV_REC_STATE | PROV_REC_STATE_C | No | No | No |  |
| 4 | STATUS_C | ZC_RECORD_STATE_2 | RECORD_STATE_2_C | No | No | No |  |
| 4 | STATUS_C | ZC_RECORD_STATE_3 | RECORD_STATE_3_C | No | No | No |  |
| 4 | STATUS_C | ZC_RECORD_STATE_4 | RECORD_STATE_4_C | No | No | No |  |
| 4 | STATUS_C | ZC_RECORD_STATE_6 | RECORD_STATE_6_C | No | No | No |  |

_(67 total; showing first 30)_
