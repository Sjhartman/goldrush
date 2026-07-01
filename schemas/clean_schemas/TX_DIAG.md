# TX_DIAG

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=TX_DIAG

## Description

This table contains information about the diagnoses associated with transactions. Since one transaction may be associated with multiple diagnoses, each row in this table represents one diagnosis and is identified by the transaction ID and line number. The first six diagnosis IDs associated with a transaction are recorded in the CLARITY_TDL table in the columns DX_ ONE_ID through DX_ SIX_ID. This table allows you to easily identify transactions with a specific diagnosis code or range of diagnosis codes. The data for this table is extracted using a KB_SQL query.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | ETR |
| Release Version | EPIC 2000 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| TX_ID | NUMERIC (18,0) | The unique accounts receivable transaction record ID. |
| LINE | No | Line number to identify each row of diagnosis data associated with an individual transaction. Line 1 identifies the primary diagnosis of the charge. |
| POST_DATE | DATETIME | The post date of the charge transaction |
| SERV_AREA_ID | NUMERIC (18,0) | The ID of the service area associated with the transaction identified by TX_ID. |
| DX_ID | NUMERIC (18,0) | The diagnosis associated with the charge transaction.  This diagnosis is from the primary codeset. |
| ICD9_CODE *(deprecated)* | VARCHAR (20) | *** Deprecated *** In table TX_DIAG, the column ICD9_CODE (EDG 2000) has been deprecated. Link to the CLARITY_EDG table using TX_DIAG.DX_ID column. Refer to the Diagnosis and ICD Procedure Updates section of https://galaxy.epic.com/redirect.aspx?documentid=1577542 to determine the correct column to use. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The physical owner deployment of this record, , used in Community Model record sharing. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The logical owner deployment of this record, used in Community Model record sharing. |
| DX_QUALIFIER_C | VARCHAR (66) |  |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| B-TREE INDEX | EIX_TX_DIAG_DX_ID | DX_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_TX_DIAG_PODA | POST_DATE | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_TX_DIAG_SEARID | SERV_AREA_ID | 1 | Yes | Yes |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | TX_ID | AP_CLAIM_PROC | TX_ID | Unknown | No | No |  |
| 1 | TX_ID | AP_CLAIM_PROC_2 | TX_ID | Unknown | No | No |  |
| 1 | TX_ID | AP_CLAIM_PROC_3 | TX_ID | Unknown | No | No |  |
| 1 | TX_ID | AP_CLAIM_PROC_4 | TX_ID | Unknown | No | No |  |
| 1 | TX_ID | AP_CLAIM_PROC_5 | TX_ID | No | No | No |  |
| 1 | TX_ID | AP_CLAIM_REAL_TM_INTERF | TX_ID | Unknown | No | No |  |
| 1 | TX_ID | AP_CLM_RX_DTL | TX_ID | No | No | No |  |
| 1 | TX_ID | AP_CLM_RX_DTL_2 | TX_ID | No | No | No |  |
| 1 | TX_ID | ARPB_FILING_ORDER | TX_ID | Unknown | No | No |  |
| 1 | TX_ID | ARPB_TRANSACTIONS | TX_ID | Unknown | No | No |  |
| 1 | TX_ID | ARPB_TRANSACTIONS2 | TX_ID | Unknown | No | No |  |
| 1 | TX_ID | ARPB_TRANSACTIONS3 | TX_ID | No | No | No |  |
| 1 | TX_ID | ARPB_TRANSACTIONS4 | TX_ID | No | No | No |  |
| 1 | TX_ID | ARPB_TX_CH_GEN_ITM | TX_ID | Unknown | No | No |  |
| 1 | TX_ID | ARPB_TX_COLL_RATIO | TX_ID | No | No | No |  |
| 1 | TX_ID | ARPB_TX_COST | TX_ID | No | No | No |  |
| 1 | TX_ID | ARPB_TX_DENTAL | TX_ID | Unknown | No | No |  |
| 1 | TX_ID | ARPB_TX_E_PMT | TX_ID | No | No | No |  |
| 1 | TX_ID | ARPB_TX_FIN_ASST | TX_ID | Unknown | No | No |  |
| 1 | TX_ID | ARPB_TX_MODERATE | TX_ID | No | No | No |  |
| 1 | TX_ID | ARPB_TX_REFUND | TX_ID | Unknown | No | No |  |
| 1 | TX_ID | ARPB_TX_SST | TX_ID | Unknown | No | No |  |
| 1 | TX_ID | ARPB_TX_TEST_INFO | TX_ID | Unknown | No | No |  |
| 1 | TX_ID | ARPB_TX_VOID | TX_ID | Unknown | No | No |  |
| 1 | TX_ID | CLAIM_STMNT_DATE | TX_ID | Unknown | No | No |  |
| 1 | TX_ID | F_ARPB_CUBE_ETR_INDEX | TRANSACTION_ID | Unknown | Unknown | No |  |
| 1 | TX_ID | REFLAB_TRANSACTION | TX_ID | Unknown | No | No |  |
| 1 | TX_ID | TX_ANES_INFO | TX_ID | Unknown | No | No |  |
| 1 | TX_ID | V_ARPB_PAYMENTS | TX_ID | Unknown | Unknown | No |  |
| 1 | TX_ID | V_CUBE_D_PB_TRANSACTION | TRANSACTION_ID | Unknown | Unknown | No |  |

_(77 total; showing first 30)_
