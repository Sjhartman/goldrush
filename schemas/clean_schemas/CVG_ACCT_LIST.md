# CVG_ACCT_LIST

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=CVG_ACCT_LIST

## Description

This table contains the list of guarantor accounts associated with a coverage.

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
| CVG_ID | NUMERIC (18,0) | The unique ID of the coverage |
| LINE | No | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| CM_PHY_OWNER_ID | VARCHAR (25) | ID of the physical deployment owner for this record.  Physical owners will be where the data is hosted, either on the cross-over server or the owner deployment. |
| CM_LOG_OWNER_ID | VARCHAR (25) | ID of the logical deployment owner for this record.  Logical owners show the deployment where the record was created but doesn't represent if the record is a part of version skew. |
| ACCT_SHARING_CVG_ID | NUMERIC (18,0) | The ID of the account sharing coverage |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | CVG_ID | COVERAGE | COVERAGE_ID | Unknown | No | No |  |
| 1 | CVG_ID | COVERAGE_2 | CVG_ID | Unknown | No | No |  |
| 1 | CVG_ID | COVERAGE_3 | CVG_ID | Unknown | No | No |  |
| 1 | CVG_ID | COVERAGE_4 | CVG_ID | Unknown | No | No |  |
| 1 | CVG_ID | COVERAGE_5 | CVG_ID | No | No | No |  |
| 1 | CVG_ID | COVERAGE_6 | COVERAGE_ID | No | No | No |  |
| 1 | CVG_ID | COVERAGE_MISC_COMMENTS | COVERAGE_ID | No | No | No |  |
| 1 | CVG_ID | CVG_AP_CLAIMS | COVERAGE_ID | Unknown | No | No |  |
| 1 | CVG_ID | V_EHI_COVERAGE_SUBS | COVERAGE_ID | Unknown | Unknown | No |  |
| 3 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 4 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 4 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 4 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 5 | ACCT_SHARING_CVG_ID | ACCOUNT | ACCOUNT_ID | No | No | No |  |
| 5 | ACCT_SHARING_CVG_ID | ACCOUNT_2 | ACCT_ID | No | No | No |  |
| 5 | ACCT_SHARING_CVG_ID | ACCOUNT_3 | ACCOUNT_ID | No | No | No |  |
| 5 | ACCT_SHARING_CVG_ID | ACCOUNT_CONS_SP_SA_BILL | ACCT_ID | No | No | No |  |
| 5 | ACCT_SHARING_CVG_ID | CS_ACT_RECPULL | ACCOUNT_ID | No | No | No |  |
| 5 | ACCT_SHARING_CVG_ID | F_ARPB_CUBE_EAR_INDEX | GUARANTOR_ID | Unknown | Unknown | No |  |
| 5 | ACCT_SHARING_CVG_ID | GUAR_PMT_SCORE | ACCOUNT_ID | Unknown | Unknown | No |  |
| 5 | ACCT_SHARING_CVG_ID | GUAR_PMT_SCORE_REPL | ACCOUNT_ID | No | No | No |  |
| 5 | ACCT_SHARING_CVG_ID | V_CUBE_D_GUARANTOR | GUARANTOR_ID | Unknown | Unknown | No |  |
| 5 | ACCT_SHARING_CVG_ID | V_EHI_EAR_FILTER | ACCOUNT_ID | Unknown | Unknown | No |  |
| 5 | ACCT_SHARING_CVG_ID | V_ROI_REQUESTER_CREATION | ACCOUNT_ID | Unknown | Unknown | No |  |
