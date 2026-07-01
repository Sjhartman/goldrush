# HSP_ACCT_DX_LIST

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=HSP_ACCT_DX_LIST

## Description

This table contains hospital account final diagnosis list information from the Hospital Accounts Receivable (HAR) master file.

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
| LINE | No | The line number in the results of a query. Since multiple final ICD diagnoses can be stored in one hospital account, each diagnosis will have a unique line number. The record associated with line 1 represents the principal final coded  diagnosis. |
| DX_ID | NUMERIC (18,0) | The system ID number of a final diagnosis code stored in the hospital account. |
| CM_PHY_OWNER_ID | VARCHAR (25) | ID of the physical deployment owner for this record.  Physical owners will be where the data is hosted, either on the cross-over server or the owner deployment. |
| CM_LOG_OWNER_ID | VARCHAR (25) | ID of the logical deployment owner for this record.  Logical owners show the deployment where the record was created but doesn't represent if the record is a part of version skew. |
| DX_POA_YNU *(deprecated)* | VARCHAR (254) |  |
| DX_AFFECTS_DRG_YN | VARCHAR (254) |  |
| DX_COMORBIDITY_YN | VARCHAR (254) |  |
| FINAL_DX_SOI_C | INTEGER |  |
| FINAL_DX_ROM_C | INTEGER |  |
| FINAL_DX_EXCLD_YN | VARCHAR (1) |  |
| FNL_DX_AFCT_SOI_YN | VARCHAR (1) |  |
| FNL_DX_AFCT_ROM_YN | VARCHAR (1) |  |
| FINAL_DX_POA_C | INTEGER |  |
| DX_COMORBIDITY_C | INTEGER |  |
| DX_HAC_YN | VARCHAR (1) |  |
| DX_TYPE_C | INTEGER |  |
| DX_START_DT | DATETIME | Specifies the start date of a diagnosis. |
| DX_END_DT | DATETIME | Specifies the end date of a diagnosis. |
| DX_PROBLEM_ID | NUMERIC (18,0) | Specifies the networked problem (LPL) ID for the related diagnosis. |
| DX_CHRONIC_FLAG_YN | VARCHAR (1) |  |
| DX_SUPP_ATC_CODE_C | INTEGER |  |
| DX_HSP_PROB_FLAG_YN | VARCHAR (1) |  |
| DX_OVERRIDDEN_DX_ID | NUMERIC (18,0) | This item stores the diagnosis that was on the problem at the time that it was associated. This overridden diagnosis is only populated if the diagnosis is overridden. |
| DX_DISPROVEN_YN | VARCHAR (1) |  |
| DK_CANCER_STATUS_C | INTEGER |  |
| DX_DOCUMENTING_USER_ID | VARCHAR (18) | Contains the user (EMP) ID of the user that documented the diagnosis |
| FNL_DX_QUALIFIER_C | VARCHAR (66) |  |
| TERM_DX_ID | NUMERIC (18,0) | This item stores the diagnosis term record (clinical diagnosis) that the diagnosis code record (billing diagnosis) is mapped from. This item may be null for old hospital accounts. |
| DX_COF_C | INTEGER |  |
| DX_COMPLEXITY_LVL | INTEGER | The diagnosis complexity level - the complexity weight assigned to the diagnosis in relation to the DRG. |
| COMPLEX_DX_C | INTEGER |  |
| DX_CLASS_C | INTEGER |  |
| CAUSE_DEATH_YN | VARCHAR (1) |  |
| DX_CLUSTER | VARCHAR (2) | This item stores the diagnosis cluster identifier. |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| B-TREE INDEX | EIX_HAR_DX_LIST_DX_ID | DX_ID | 1 | Yes | Yes |  |

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

_(93 total; showing first 30)_
