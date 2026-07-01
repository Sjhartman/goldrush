# HSP_ACCT_CPT_CODES

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=HSP_ACCT_CPT_CODES

## Description

This table contains hospital account CPT(R) codes from the Hospital Accounts Receivable (HAR) master file.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | HAR |
| Release Version | MU1 - MAY 2001 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| HSP_ACCOUNT_ID | NUMERIC (18,0) | The ID number of a hospital account. |
| LINE | No | The line number in the results of a query. Since multiple CPT? codes can be stored in one hospital account, each CPT? code will have a unique line number. |
| CPT_CODE | VARCHAR (20) | A CPT? code stored in the hospital account. |
| CPT_CODE_DATE | DATETIME | A date associated with a CPT? code stored in the hospital account. |
| CPT_PERF_PROV_ID | VARCHAR (18) | The ID number of a performing provider associated with a CPT? code stored in the hospital account. |
| CPT_EVENT_NUMBER | INTEGER | The event number associated with a CPT? code stored in the hospital account. Event number are used to associate CPT? codes with procedure codes. |
| CPT_MODIFIERS | VARCHAR (25) | A modifier or modifiers associated with a CPT? code stored in the hospital account. |
| LMRP_CODE | VARCHAR (80) | A Local Medical Review Policy (LMRP) code associated with a CPT? code stored in the hospital account. |
| CPT_CODE_DESC | VARCHAR (1024) | The description of a CPT? code stored in the hospital account. |
| CM_PHY_OWNER_ID | VARCHAR (25) | ID of the physical deployment owner for this record.  Physical owners will be where the data is hosted, either on the cross-over server or the owner deployment. |
| CM_LOG_OWNER_ID | VARCHAR (25) | ID of the logical deployment owner for this record.  Logical owners show the deployment where the record was created but doesn't represent if the record is a part of version skew. |
| PX_APC_PMT_STS_IND | VARCHAR (254) | The indicator for the procedure APC payment status on the hospital account. |
| PX_CODE_AFF_DRG_YN | VARCHAR (254) |  |
| PX_APC_PMT_IND | NUMERIC (18,0) | The indicator for the procedure APC payment on the hospital account. |
| PX_APC_WEIGHT | NUMERIC (18,2) | The weight of the procedure APC on the hospital account. |
| PX_APC_FAC_RMB_AMT | NUMERIC (18,2) | The monetary reimbursement amount for the procedure Ambulatory Payment Classification (APC) FAC on the hospital account. |
| PX_OCE_EDIT_CODE | VARCHAR (254) | The procedure Outpatient Code Editor (OCE) edit code for the hospital account. |
| PX_APC_CODE | VARCHAR (254) | The procedure Ambulatory Payment Classification (APC) code for the hospital account. |
| PX_HCFA_PAYMT_AMT | NUMERIC (18,2) | The procedure Health Care Payment and Remittance Advice (HCFA) monetary payment amount for the hospital account. |
| PX_REIMB_TYPE | VARCHAR (254) | The procedure reimbursement type assigned to the hospital account. |
| PX_COPAY_AMT | NUMERIC (18,2) | The monetary copay amount for the procedure on the hospital account. |
| PX_PAY_RT_UNIT_AMT | NUMERIC (18,2) | The monetary procedure pay rate per unit on the hospital account. |
| PX_REV_CODE_ID | NUMERIC (18,0) | The unique ID of the revenue code. |
| CPT_EXCLD_RPT_YN | VARCHAR (1) |  |
| CPT_QUANTITY | INTEGER | Quantity of the CPT(R)/HCPCS code. Hospital accounts created prior to Epic 2014 have a null value in this column which implies a quantity of 1. |
| CPT_POS_TYPE_C | INTEGER | Surrogate key used to uniquely identify rows in this (and only this) table on Cogito Cloud only, do not assume the surrogate key in this table will correspond to the surrogate key in another table |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | HSP_ACCOUNT_ID | ARPB_VISITS | PB_VISIT_ID | No | No | No |  |
| 1 | HSP_ACCOUNT_ID | ARPB_VISIT_COST | PB_VISIT_ID | No | No | No |  |
| 1 | HSP_ACCOUNT_ID | F_ADT_HAR_CENSUS | HSP_ACCOUNT_ID | Unknown | Unknown | No |  |
| 1 | HSP_ACCOUNT_ID | F_ARHB_HAR_EOD | HSP_ACCOUNT_ID | Unknown | Unknown | No |  |
| 1 | HSP_ACCOUNT_ID | F_PDGM_METRICS | ACCT_ID | Unknown | Unknown | No |  |
| 1 | HSP_ACCOUNT_ID | HAR_ALL | ACCT_ID | No | No | No |  |
| 1 | HSP_ACCOUNT_ID | HAR_DBC_INFO | HSP_ACCOUNT_ID | No | No | No |  |
| 1 | HSP_ACCOUNT_ID | HSP_ACCOUNT | HSP_ACCOUNT_ID | Unknown | No | No |  |
| 1 | HSP_ACCOUNT_ID | HSP_ACCOUNT_2 | HSP_ACCOUNT_ID | Unknown | No | No |  |
| 1 | HSP_ACCOUNT_ID | HSP_ACCOUNT_3 | HSP_ACCOUNT_ID | Unknown | No | No |  |
| 1 | HSP_ACCOUNT_ID | HSP_ACCOUNT_4 | HSP_ACCOUNT_ID | Unknown | No | No |  |
| 1 | HSP_ACCOUNT_ID | HSP_ACCOUNT_5 | HSP_ACCOUNT_ID | No | No | No |  |
| 1 | HSP_ACCOUNT_ID | HSP_ACCT_APC | HSP_ACCOUNT_ID | Unknown | No | No |  |
| 1 | HSP_ACCOUNT_ID | HSP_ACCT_BILL_DRG | HSP_ACCOUNT_ID | Unknown | No | No |  |
| 1 | HSP_ACCOUNT_ID | HSP_ACCT_CLAIM_HAR | ACCT_ID | Unknown | No | No |  |
| 1 | HSP_ACCOUNT_ID | HSP_ACCT_CLAR_SWAP | HSP_ACCOUNT_ID | Unknown | No | No |  |
| 1 | HSP_ACCOUNT_ID | HSP_ACCT_CONS_SP_BAL | HSP_ACCOUNT_ID | No | No | No |  |
| 1 | HSP_ACCOUNT_ID | HSP_ACCT_COST | HSP_ACCOUNT_ID | No | No | No |  |
| 1 | HSP_ACCOUNT_ID | HSP_ACCT_EBC | HSP_ACCOUNT_ID | Unknown | No | No |  |
| 1 | HSP_ACCOUNT_ID | HSP_ACCT_EBC_2 | HSP_ACCOUNT_ID | Unknown | No | No |  |
| 1 | HSP_ACCOUNT_ID | HSP_ACCT_LAST_UPDATE | HSP_ACCOUNT_ID | Unknown | Unknown | No |  |
| 1 | HSP_ACCOUNT_ID | HSP_ACCT_PAT_MRN | HSP_ACCOUNT_ID | No | No | No |  |
| 1 | HSP_ACCOUNT_ID | HSP_ACCT_SBO | HSP_ACCOUNT_ID | Unknown | No | No |  |
| 1 | HSP_ACCOUNT_ID | HSP_ACCT_SEPSABILL | ACCT_ID | Unknown | No | No |  |
| 1 | HSP_ACCOUNT_ID | HSP_ACCT_SPLIT | HSP_ACCOUNT_ID | No | No | No |  |
| 1 | HSP_ACCOUNT_ID | HSP_ACCT_SP_DSCNT | ACCT_ID | Unknown | No | No |  |
| 1 | HSP_ACCOUNT_ID | HSP_CHARGE_HOMING | HSP_ACCOUNT_ID | No | No | No |  |
| 1 | HSP_ACCOUNT_ID | HSP_PAS_DK_KONTAKT | ACCT_ID | No | No | No |  |
| 1 | HSP_ACCOUNT_ID | HSP_PAS_EPSD_ENC | HSP_ACCOUNT_ID | Unknown | No | No |  |
| 1 | HSP_ACCOUNT_ID | V_ARHB_COLLECTION_RATIO | HSP_ACCOUNT_ID | Unknown | Unknown | No |  |

_(57 total; showing first 30)_
