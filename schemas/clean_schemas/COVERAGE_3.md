# COVERAGE_3

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=COVERAGE_3

## Description

The COVERAGE_3 table contains high-level information on both managed care and indemnity coverage records in your system.

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
| PAYOR_STATE_C | VARCHAR (66) |  |
| PAYOR_ZIP | VARCHAR (254) | The ZIP code of the coverage payer. |
| PAYOR_PHONE | VARCHAR (254) | The phone number of the coverage payer. |
| PAYOR_CLAIM_OFC_NUM | VARCHAR (254) | The claim office number of the coverage payer. |
| REF_PROV_NAME_ID | VARCHAR (18) | The name of the Health Maintenance Organization's referring physician. |
| REF_PROV_CITY | VARCHAR (254) | The city of the Health Maintenance Organization's referring physician. |
| REF_PROV_STATE_C | VARCHAR (66) |  |
| REF_PROV_ZIP | VARCHAR (254) | The ZIP code of the Health Maintenance Organization's referring physician. |
| AUTH_NUM | VARCHAR (254) | The authorization number for this coverage. |
| AUTHORIZATION_DTTM | 2255 | The authorization date and time for this coverage. |
| AUTH_PERSON | VARCHAR (254) | The name of the person who authorized services for this coverage. |
| VERIF_DATETIME | 2260 | The date and time when authorization was obtained. |
| MED_ASSIST_CARD | VARCHAR (254) | The medical assistance card number. |
| MED_ASSIST_CODE_C | VARCHAR (66) |  |
| MED_ASSIST_STATUS | VARCHAR (254) | The medical assistance status. |
| MED_ASSIST_COV_CODE | VARCHAR (254) | The medical assistance coverage code. |
| IS_CVG_VA_PROG_YN | VARCHAR (66) |  |
| INSTANT_OF_UPD_DTTM *(deprecated)* | DATETIME (Local) | Date and time of the last coverage update. |
| IS_MC_PROGRAM_YN | VARCHAR (1) |  |
| MC_PRIM_PROV | VARCHAR (254) | The primary provider for a managed care coverage. |
| MC_AUTH_NUM | VARCHAR (254) | The authorization number for a managed care coverage. |
| MC_AUTH_PHONE_NUM | VARCHAR (254) | The authorization phone number for a managed care coverage. |
| TYPE_OF_COVERAGE_C | VARCHAR (66) |  |
| ALSO_HAS_MCARE_YN | VARCHAR (1) |  |
| MAJOR_MEDICAL_C | VARCHAR (66) |  |
| MCAID_GRP_NO_SUF_C | VARCHAR (66) |  |
| CHAMPUS_RANK | VARCHAR (254) | The CHAMPUS/Tricare rank. |
| CHAMPUS_GRADE | VARCHAR (254) | The CHAMPUS/Tricare grade. |
| BC_BS_CNTRCT_ACCT_C | VARCHAR (66) |  |
| MAC_PROV_PHONE_NUM | VARCHAR (254) | The phone number for the primary provider. |
| MAC_AUTH_CNCT_PRSN | VARCHAR (254) | The person who provided authorization information for this visit. |
| MAC_COMMENT | VARCHAR (254) | Comments regarding authorization or denial. |
| MAC_PMP_AUTH_C | VARCHAR (66) |  |
| MCARE_RR_SUB_NO_P_C | INTEGER |  |
| RECIPROCITY_NO | VARCHAR (254) | The reciprocity number for this coverage. |
| MAC_AUTH_ENT_PRSN | VARCHAR (254) | The person who entered the authorization number for this managed care coverage. |
| THERAPY_TYPE_C | INTEGER |  |
| THERAPY_PLAN_DATE | DATETIME | The date when the therapy plan was established. |
| THERAPY_START_DT | DATETIME | The date when the therapy started. |
| LAST_MENSTRUAL_DATE | VARCHAR (254) | The patient's last menstrual date. |
| AUTH_VALID_FROM_DT | DATETIME | The date when the authorization became valid. |
| AUTH_VALID_TO_DATE | DATETIME | The date when the authorization became invalid. |
| COMMERCIAL_AUTH_NUM | VARCHAR (254) | The commercial authorization number. |
| COMM_AUTH_PRSN | VARCHAR (254) | The person who authorized the commercial coverage. |
| MC_COBRA_STATUS_YN | VARCHAR (1) |  |
| MC_COBRA_DATE | DATETIME | The date when a managed care coverage received Consolidated Omnibus Budget Reconciliation Act status. |
| PB_ACCT_CREATED_YN | VARCHAR (1) |  |
| ALTR_CVG_ATTN | VARCHAR (254) | The alternate name of the organization to which claims submitted under this coverage can be sent. |
| ALTR_CITY | VARCHAR (254) | The alternate city to which claims under this coverage can be sent. |
| ALTR_STATE_C | VARCHAR (66) |  |
| ENROLL_REASON_REG_C | INTEGER |  |
| HRA_ID *(deprecated)* | NUMERIC (18,0) | *** Deprecated *** In table COVERAGE_3, the column HRA_ID (CVG/8010) has been deprecated.  The deprecated column's content/data is no longer available since it is no longer populated in Chronicles.   The Health Reimbursement Account ID that the coverage is attached to. |
| SUBS_SUBDIV_CODE_C | INTEGER |  |
| EXT_UPD_TYPE_C | INTEGER |  |
| EXT_UPDATE_COMMENT | VARCHAR (300) | This item stores the comment that accompanies the external update request. |
| ENROLL_RECV_DATE | DATETIME | The enrollment received date for this coverage. |
| PRIOR_LIS_DATE | DATETIME | The most recent LIS period date. |
| ALT_TRANSPLANT_PAYER_OPT_C | INTEGER |  |
| PB_PAID_THROUGH_DATE | DATETIME | The date at which the coverage's premium has been fully paid through. |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | CVG_ID | COVERAGE | COVERAGE_ID | Unknown | No | No |  |
| 1 | CVG_ID | COVERAGE_2 | CVG_ID | Unknown | No | No |  |
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
| 4 | PAYOR_STATE_C | ZC_ALT_INVOICE_STA | ALT_INVOICE_STA_C | No | No | No |  |
| 4 | PAYOR_STATE_C | ZC_LLB_STATE | LLB_STATE_C | No | No | No |  |
| 4 | PAYOR_STATE_C | ZC_REFG_PROV_STATE | REFG_PROV_STATE_C | No | No | No |  |
| 4 | PAYOR_STATE_C | ZC_STATE | STATE_C | No | No | No |  |
| 4 | PAYOR_STATE_C | ZC_STATE_HISTORY | STATE_HISTORY_C | No | No | No |  |
| 4 | PAYOR_STATE_C | ZC_SUBSCR_EEP_STE | SUBSCR_EEP_STE_C | No | No | No |  |
| 4 | PAYOR_STATE_C | ZC_TAX_STATE | TAX_STATE_C | No | No | No |  |
| 8 | REF_PROV_NAME_ID | REFERRAL_SOURCE | REFERRING_PROV_ID | No | No | No |  |
| 10 | REF_PROV_STATE_C | ZC_ALT_INVOICE_STA | ALT_INVOICE_STA_C | No | No | No |  |
| 10 | REF_PROV_STATE_C | ZC_LLB_STATE | LLB_STATE_C | No | No | No |  |
| 10 | REF_PROV_STATE_C | ZC_REFG_PROV_STATE | REFG_PROV_STATE_C | No | No | No |  |
| 10 | REF_PROV_STATE_C | ZC_STATE | STATE_C | No | No | No |  |
| 10 | REF_PROV_STATE_C | ZC_STATE_HISTORY | STATE_HISTORY_C | No | No | No |  |
| 10 | REF_PROV_STATE_C | ZC_SUBSCR_EEP_STE | SUBSCR_EEP_STE_C | No | No | No |  |
| 10 | REF_PROV_STATE_C | ZC_TAX_STATE | TAX_STATE_C | No | No | No |  |
| 17 | MED_ASSIST_CODE_C | ZC_MED_ASSIST_CODE | MED_ASSIST_CODE_C | No | No | No |  |

_(49 total; showing first 30)_
