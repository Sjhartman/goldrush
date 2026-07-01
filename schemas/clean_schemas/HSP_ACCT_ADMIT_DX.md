# HSP_ACCT_ADMIT_DX

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=HSP_ACCT_ADMIT_DX

## Description

This table contains hospital account admit diagnoses from the Hospital Accounts Receivable (HAR) master file.

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
| HSP_ACCOUNT_ID | NUMERIC (18,0) | This column stores the unique identifier for the hospital account. |
| LINE | No | This column stores the line number in the results of a query. As multiple admission diagnoses can be stored in one hospital account, each diagnosis will have a unique line number. |
| ADMIT_DX_ID | NUMERIC (18,0) | This column stores the unique identifier for admission diagnosis stored in the hospital account. |
| ADMIT_DX_TEXT | VARCHAR (508) | A text description of an admission diagnosis stored in the hospital account. |
| CM_PHY_OWNER_ID | VARCHAR (25) | ID of the physical deployment owner for this record.  Physical owners will be where the data is hosted, either on the cross-over server or the owner deployment. |
| CM_LOG_OWNER_ID | VARCHAR (25) | ID of the logical deployment owner for this record.  Logical owners show the deployment where the record was created but doesn't represent if the record is a part of version skew. |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| B-TREE INDEX | EIX_HSP_ACCT_ADMIT_DX_DXACCT | ADMIT_DX_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_HSP_ACCT_ADMIT_DX_DXACCT | HSP_ACCOUNT_ID | 2 | Yes | Yes |  |

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

_(46 total; showing first 30)_
