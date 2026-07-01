# CLARITY_FC

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=CLARITY_FC

## Description

Financial Class is actually a category list (HCT 50000) in your system; however, it is used so frequently in Accounts Receivable reports that we made it easier to locate by naming the table CLARITY_FC, similar to a structural master file. You can also use ZC_FINANCIAL_CLASS to report on this information.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | FULL |
| Load Frequency | INCREMENTAL |
| Chronicles INI | N/A |
| Release Version | EPIC 2000 |
| May contain EHI? | No |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| FINANCIAL_CLASS | VARCHAR (66) |  |
| FINANCIAL_CLASS_NAME | VARCHAR (254) |  |
| FIN_CLASS_TITLE | VARCHAR (254) |  |
| FINANCIAL_CLASS_ABBR | VARCHAR (15) |  |
| INTERNAL_ID | VARCHAR (66) |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | FINANCIAL_CLASS | ZC_ACTN_FIN_CLASS | ACTION_FIN_CLASS | No | No | No |  |
| 1 | FINANCIAL_CLASS | ZC_CUR_FIN_CLASS | CUR_FIN_CLASS | No | No | No |  |
| 1 | FINANCIAL_CLASS | ZC_FC_MEDICAID | FC_MEDICAID_C | No | No | No |  |
| 1 | FINANCIAL_CLASS | ZC_FINANCIAL_CLASS | FINANCIAL_CLASS | No | No | No |  |
| 1 | FINANCIAL_CLASS | ZC_FIN_CLASS | FIN_CLASS_C | No | No | No |  |
| 1 | FINANCIAL_CLASS | ZC_ORIG_FIN_CLASS | ORIGINAL_FIN_CLASS | No | No | No |  |
