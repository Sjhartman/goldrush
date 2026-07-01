# HSP_ACCT_MULT_DRGS

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=HSP_ACCT_MULT_DRGS

## Description

This table contains multiple diagnosis related group information for hospital accounts.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | HAR |
| Release Version | MU2 - EPIC 2002 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| HSP_ACCOUNT_ID | NUMERIC (18,0) | The hospital account ID with associated Single Billing Office information. |
| LINE | No | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| DRG_ID_TYPE_ID | NUMERIC (18,0) | From the list of diagnosis-related group (DRG) filed to the hospital account, the unique ID of DRG code set for this row. |
| DRG_ID | VARCHAR (18) | This column extracts the internal IDs of DRG codes entered in the Multiple DRG grid of Hospital Billing - Coding for each Hospital Account. |
| DRG_MPI_CODE | No | This column extracts the Master Patient Index (MPI) IDs of diagnosis-related group (DRG) codes entered in the Multiple DRG grid of Hospital Billing - Coding for each Hospital Account.  The MPI IDs shown here will be the IDs that correspond to the DRG MPI Type extracted in the DRG_ID_TYPE_ID column. |
| DRG_REIMBURSEMENT | NUMERIC (12,2) | From the list of diagnosis-related groups (DRGs) filed to the hospital account, the expected reimbursement amount for the DRG in this row. |
| DRG_MDC_VALUE | VARCHAR (40) | From the list of diagnosis-related group (DRG) filed to the hospital account, the Major Diagnostic Category value for the DRG in this row. |
| DRG_WEIGHT | NUMERIC (9,4) | From the list of DRGs filed to the hospital account, the weight for the DRG in this row. |
| DRG_PS | INTEGER |  |
| DRG_ROM | INTEGER |  |
| DRG_SHORT_LOS | VARCHAR (40) | The unique identifier for the treatment plan record. |
| DRG_LONG_LOS | VARCHAR (40) | From the list of diagnosis-related group (DRG) filed to the hospital account, the long length of stay for the DRG in this row. |
| DRG_AMLOS | VARCHAR (40) | From the list of DRGs filed to the hospital account, the arithmetic mean length of stay for the DRG in this row. |
| DRG_GMLOS | VARCHAR (40) | From the list of diagnosis-related group (DRG) filed to the hospital account, the geometric mean length of stay for the DRG in this row. |
| CM_PHY_OWNER_ID | VARCHAR (25) | ID of the physical deployment owner for this record.  Physical owners will be where the data is hosted, either on the cross-over server or the owner deployment. |
| CM_LOG_OWNER_ID | VARCHAR (25) | ID of the logical deployment owner for this record.  Logical owners show the deployment where the record was created but doesn't represent if the record is a part of version skew. |
| DRG_CST_OTLR_THRSH | NUMERIC (12,2) | The diagnosis-related group (DRG) cost outlier threshold for the hospital account. |
| DRG_DAY_OTLR_THRSH | NUMERIC (18,2) | The diagnosis-related group (DRG) day outlier threshold for the hospital account. |
| DRG_NRM_PT_RMB_AMT | NUMERIC (12,2) | The normal patient reimbursal amount for diagnosis-related group (DRG) on the hospital account. |
| DRG_TG_FED_BLND_RT | NUMERIC (12,2) | The target fed blended rate for DRG on the hospital account. |
| DRG_COND_CODE | NUMERIC (18,0) | The diagnosis-related group (DRG) condition code on the hospital account. |
| DRG_FORMULA | NUMERIC (18,0) | The diagnosis-related group (DRG) formula information on the hospital account. |
| DRG_LOS | INTEGER | The diagnosis-related group (DRG) LOS for the hospital account. |
| DRG_PAT_STATUS | VARCHAR (254) | The patient status for the diagnosis-related group (DRG) on the hospital account. |
| DRG_ISP_SHR_AJ_AMT | NUMERIC (18,2) | The dispensed share adjustment amount for the diagnosis-related group (DRG) on the hospital account. |
| DRG_INDIR_MED_AMT | NUMERIC (18,2) | The indirect medicated monetary amount for the diagnosis-related group (DRG) on the hospital account. |
| DRG_CAPITAL_AMT | NUMERIC (18,2) | The capital monetary amount for the DRG on the hospital account. |
| DRG_OTLR_RMB_AMT | NUMERIC (18,2) | The outlier reimbursement monetary amount for the diagnosis-related group (DRG) on the hospital account. |
| DRG_CHG_CLM_AMT | NUMERIC (18,2) | The total diagnosis-related group (DRG) charges on claim for this DRG on this hospital account. |
| DRG_OUTLIER_TYPE | INTEGER | The outlier type for the diagnosis-related group (DRG) on the hospital account. |
| DRG_OUTLIER_DAYS | INTEGER | The number of outlier days for the diagnosis-related group (DRG) on the hospital account. |
| DRG_OTLR_CST_AMT | NUMERIC (18,2) | The monetary outlier cost for the diagnosis-related group (DRG) on the hospital account. |
| DRG_OUTLIER_REIMB | NUMERIC (18,2) | The outlier reimbursement for the diagnosis-related group (DRG) on the hospital account. |
| DRG_CMT | VARCHAR (1000) | The comment associated with the diagnosis-related group (DRG) on the hospital account. |
| DRG_QLFR_C | INTEGER |  |
| DRG_BILLING_FLAG_YN | VARCHAR (1) |  |
| DRG_ECCS | NUMERIC (18,2) | The ECCS (episode clinical complexity score) associated with the DRG. |
| DELIM_COND_CODES | VARCHAR (254) | DRG condition codes delimited by ~ in text form |
| DRG_IS_CMI_EXCLUD_YN | VARCHAR (1) | Surrogate key used to uniquely identify rows in this (and only this) table on Cogito Cloud only, do not assume the surrogate key in this table will correspond to the surrogate key in another table |

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

_(49 total; showing first 30)_
