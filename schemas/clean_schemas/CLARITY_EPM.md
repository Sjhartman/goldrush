# CLARITY_EPM

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=CLARITY_EPM

## Description

The CLARITY_EPM table contains information about payer records.

**Primary table** in this group (101 cols). Overflow siblings joined on shared key: CLARITY_EPM_2 (54 cols), CLARITY_EPM_3 (11 cols). Prefer this table for most queries.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | EPM |
| Release Version | EPIC 2000 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| PAYOR_ID | NUMERIC (18,0) | The unique ID assigned to the payor. |
| PAYOR_NAME | VARCHAR (80) | The name of the payor. |
| FINANCIAL_CLASS | VARCHAR (66) |  |
| PRODUCT_TYPE *(deprecated)* | VARCHAR (66) |  |
| GL_PREFIX | VARCHAR (128) | The code that the General Ledger report uses to identify transactions as belonging to a payor if you use payor as an identifying category in your facility. |
| RPT_GRP_ONE | VARCHAR (254) | You have the ability to specify groupers for enterprise reporting, SQL, or report generator reporting. There are five free text groupers and five category groupers. If you elect to use these groupers, please contact your enterprise reporting representative for assistance. This is the first free text report grouper. |
| RPT_GRP_TWO | VARCHAR (254) | You have the ability to specify groupers for enterprise reporting, SQL, or report generator reporting. There are five free text groupers and five category groupers. If you elect to use these groupers, please contact your enterprise reporting representative for assistance. This is the second free text report grouper. |
| RPT_GRP_THREE | VARCHAR (254) | You have the ability to specify groupers for enterprise reporting, SQL, or report generator reporting. There are five free text groupers and five category groupers. If you elect to use these groupers, please contact your enterprise reporting representative for assistance. This is the third free text report grouper. |
| RPT_GRP_FOUR | VARCHAR (254) | You have the ability to specify groupers for enterprise reporting, SQL, or report generator reporting. There are five free text groupers and five category groupers. If you elect to use these groupers, please contact your enterprise reporting representative for assistance. This is the fourth free text report grouper. |
| RPT_GRP_FIVE | VARCHAR (254) | You have the ability to specify groupers for enterprise reporting, SQL, or report generator reporting. There are five free text groupers and five category groupers. If you elect to use these groupers, please contact your enterprise reporting representative for assistance. This is the fifth free text report grouper. |
| RPT_GRP_SIX | VARCHAR (66) |  |
| RPT_GRP_SEVEN | VARCHAR (66) |  |
| RPT_GRP_EIGHT | VARCHAR (66) |  |
| RPT_GRP_NINE | VARCHAR (66) |  |
| RPT_GRP_TEN | VARCHAR (66) |  |
| REPRICED_HCFA_FRM | VARCHAR (18) | Indicates the manage care system Repriced Paper HCFA form to submit to the payor. |
| REPRICED_UB_FRM | VARCHAR (18) | Indicates the manage care system Repriced Paper UB form to submit to the payor. |
| BEN_BKT_OPT_C | INTEGER |  |
| EPM_ALT_IDFR | VARCHAR (254) | This item is the alternate identifier used by this payor to identify if an alternate procedure code should be used. |
| DFLT_DRG_TYPE_ID | NUMERIC (18,0) | The default DRG Type (MPI ID) used for billing by the payor. |
| LL_PMT_POST_YN *(deprecated)* | VARCHAR (1) |  |
| ADDR_LINE_1 | VARCHAR (255) | The first line of the payor's street address. |
| ADDR_LINE_2 | VARCHAR (255) | The second line of the payor's street address. |
| CITY | VARCHAR (255) | The city in which the payor is located. |
| STATE_C | VARCHAR (66) |  |
| COUNTY_C | VARCHAR (66) |  |
| ZIP_CODE | VARCHAR (50) | The ZIP Code in which the payor is located. |
| PHONE | VARCHAR (50) | The phone number for the payor. |
| SHORT_NAME | VARCHAR (254) | The short name of the payor. |
| CM_PHY_OWNER_ID | VARCHAR (25) | ID of the physical deployment owner for this record.  Physical owners will be where the data is hosted, either on the cross-over server or the owner deployment. |
| CM_LOG_OWNER_ID | VARCHAR (25) | ID of the logical deployment owner for this record.  Logical owners show the deployment where the record was created but doesn't represent if the record is a part of version skew. |
| FAX | VARCHAR (50) | The fax number for the payor. |
| MSP_TYPE_C | INTEGER |  |
| RECORD_STAT_EPM_C | INTEGER |  |
| COUNTRY_C | VARCHAR (66) |  |
| HOUSE_NUMBER | VARCHAR (20) | The payor's house number. |
| DISTRICT_C | INTEGER |  |
| MANAGED_PAYOR_YN | VARCHAR (1) |  |
| SHOW_ASA_CODE_YN | VARCHAR (1) |  |
| ANES_UN_MIN_YN | VARCHAR (1) |  |
| ANES_P_MODS_YN | VARCHAR (1) |  |
| OK_RESUB_ZERO_YN | VARCHAR (1) |  |
| OK_SUBMT_ZERO_IN_YN | VARCHAR (1) |  |
| PAID_DEMAND_CLM_YN | VARCHAR (1) |  |
| CLM_GP_PTER_ID | NUMERIC (18,0) | The unique ID of the default claim grouping pointer for this payor. |
| RESUB_ZERO_CMG_ID | VARCHAR (200) | The Component Group ID to allow zero dollar Claims to be resubmitted. |
| SUBMIT_ZERO_INS_ID | VARCHAR (200) | The Component Group ID to allow zero dollar Insurance Balance Claims to be submitted. |
| DMD_ZERO_CMG_ID | VARCHAR (200) | The Component Group ID to allow zero dollar Insurance Balance Demand Claims to be submitted. |
| DAYS_TO_REFILE | INTEGER | The number of days that must pass after a claim is accepted before it is automatically resubmitted to the payor. |
| PAPER_CRD_YN *(deprecated)* | VARCHAR (1) |  |
| ELCT_CRD_YN *(deprecated)* | VARCHAR (1) |  |
| CMS_SPLIT_COMP_ID | VARCHAR (200) | The component ID to determine which charges should not be split by billing provider. |
| PRNT_TAXO_YN | VARCHAR (1) |  |
| ALT_CLM_CITY | VARCHAR (254) | The city for the alternate claim address. |
| ALT_CLM_STATE_C | VARCHAR (66) |  |
| ALT_CLM_ZIP | VARCHAR (50) | The ZIP code for the alternate claim address. |
| ALT_CLM_PHONE | VARCHAR (15) | Stores alternate address phone number |
| PROD_PRT_B_CLM_YN | VARCHAR (1) |  |
| SUPP_PMT_PAYOR_ID | NUMERIC (18,0) | Payor ID for Medicare for supplemental payment (IME) claims |
| SUPP_PMT_PLAN_ID | NUMERIC (18,0) | Plan ID for Medicare for supplemental payment (IME) claims |
| MAX_SVC_LINES_HCFA | NUMERIC (18,0) | Stores the maximum number of service lines on a claim for this payor on a CMS claim. |
| ADJ_GRPR_SEC_CLM_C | INTEGER |  |
| ADJUSTMENT_CODE | VARCHAR (254) | Adjustment code for ANSI secondary claims |
| USE_CL_STATUS_YN | VARCHAR (1) |  |
| OUTGOING_PROFILE_ID | NUMERIC (18,0) | The unique ID of the interface profile used by this payor for claim status request messages. |
| PAYOR_INT_EXT_C | VARCHAR (66) |  |
| SUPER_PAYOR_YN | VARCHAR (1) |  |
| COPY_IME_LINES_YN | VARCHAR (1) |  |
| PYR_ID_FOR_FAC | VARCHAR (254) | Every payor has an identification code for every place that it receives claims from.  If this payor has set up a facility identification code that needs to be present on claims, then the identification code will be entered here. |
| CLAIM_MAIL_CODE_C | INTEGER |  |
| PLAN_NAME_OPT_YN | VARCHAR (1) |  |
| CLAIM_MAX_FILE_DAYS | NUMERIC (18,0) | If this Payor has set a limit on the number of days from the date of service by which claims must be filed, enter the number of days allowed here. Entering a number here will not prevent late claims from being submitted, but it will allow the application to determine when Payor-specific exception codes should be sent and adds the flexibility to define edit checks that will place late claims into an error run during claims processing.  The number entered here can be overridden for specific plans by entering a different value in the Benefit Plan master file. |
| SAVE_FULL_GP_RES_YN | VARCHAR (1) |  |
| APC_GRP_DISP_PP_ID | NUMERIC (18,0) | This item holds the programming point that displays an alternate view of the APC Grouper messages for a claim. |
| OHCI_IDENTIFIER_C | VARCHAR (66) |  |
| HB_EOB_DRV_PP_YN | VARCHAR (1) |  |
| HB_REFUND_DB_ADJ_ID | NUMERIC (18,0) | The unique ID of the default refund debit adjustment code. |
| HB_APC_GRPR_SYS_C | VARCHAR (66) |  |
| HB_DEF_XR_SRC_C | VARCHAR (66) |  |
| RAP_PMT_PRCNT_ID *(deprecated)* | NUMERIC (18,0) |  |
| HB_RECUR_DEF_CTYP_C | INTEGER |  |
| HB_RECUR_DEF_DAYS | VARCHAR (254) | The days within a cycle period on which discharge of any open accounts with guarantor accounts not defined in the EPM_HB_RECUR_CYCLE table will occur. |
| INTERIM_BILLING_YN | VARCHAR (1) |  |
| INTERIM_BILL_CYCLE | NUMERIC (18,0) | When processing interim bills in the background, this value will determine the number of days between interim bills. |
| CMLT_BILLED_YN | VARCHAR (1) |  |
| COMB_BKTS_IF_SCN_YN | VARCHAR (1) |  |
| ADMSN_BILL_YN | VARCHAR (1) |  |
| INTERF_CVGCREATE_ID | NUMERIC (18,0) | This item specifies a second interface items table, to be used when creating a coverage from an incoming message (rather than updating an existing coverage). |
| PREVENT_DUP_CVG_C | INTEGER |  |
| BIN_NUM | VARCHAR (30) | The Bank Information Number (BIN) used during prescription adjudication.   This can be overridden at the plan level but if nothing is specified at the plan level, the payor level BIN is used. |
| PAYOR_SHEET_PP_ID | NUMERIC (18,0) | Extension to select what payor sheet to use during Rx adjudication. If the extension does not return a value, the transaction table will be used to find the payor sheet.  The plan level payor sheet extension is always checked first, then the plan level table, then the payor level payor sheet extension, and then the payor level table. |
| USE_ACCEL_SP_YN *(deprecated)* | VARCHAR (1) |  |
| SUP_PART_FILLS_YN | VARCHAR (1) |  |
| PROCESSOR_CNTRL_NUM | VARCHAR (10) | The Processor Control Number (PCN) used during prescription adjudication.   This can be overridden at the plan level but if nothing is specified at the plan level, the payor level PCNs are used. |
| BDRG_TYP_REF_DT_C | INTEGER |  |
| SOFTWARE_VENDOR_ID | VARCHAR (254) | The software vendor ID given by the payor for prescription adjudication. |
| NON_PRIMARY_BIN_NUM | VARCHAR (30) | The Bank Information Number (BIN) used during prescription adjudication for non primary coverages. Leave this field blank if the same BIN is used regardless of whether the coverage is primary or secondary.   If no non-primary BIN is specified, the BIN will be used for non-primary coverages. This can be overridden at the plan level, but if nothing is specified at the plan level, then the payor level BINs are used. |
| NON_PRIMARY_PCN | VARCHAR (30) | The Processor Control Number (PCN) used during prescription adjudication for non-primary coverages. Leave this field blank if the same PCN is used regardless of whether the coverage is primary or secondary.  If no non-primary PCN is specified, the PCN will be used for non-primary coverages. This can be overridden at the plan level, but if nothing is specified at the plan level, then the payor level PCNs are used. |
| INFOSCAN_TIER | NUMERIC (18,0) | This field identifies if this payor's plans are two-tier plans, three-tier plans or they have no tier information. |
| SURCHARGE_GROUP_C | INTEGER | Surrogate key used to uniquely identify rows in this (and only this) table on Cogito Cloud only, do not assume the surrogate key in this table will correspond to the surrogate key in another table |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | PAYOR_ID | CLARITY_EPM_2 | PAYOR_ID | No | No | No |  |
| 1 | PAYOR_ID | CLARITY_EPM_3 | PAYOR_ID | No | No | No |  |
| 1 | PAYOR_ID | DENT_PAYER_BENEFITS_FLAGS | PAYOR_ID | No | No | No |  |
| 1 | PAYOR_ID | EPM_CLM_FILING_INF | PAYOR_ID | No | No | No |  |
| 1 | PAYOR_ID | EPM_CLM_FRM_OPTION | PAYOR_ID | No | No | No |  |
| 1 | PAYOR_ID | EPM_CLM_PRNT_OPTN | PAYOR_ID | No | No | No |  |
| 1 | PAYOR_ID | EPM_TAP_PAYOR_INFO | PAYOR_ID | No | No | No |  |
| 1 | PAYOR_ID | V_CUBE_D_PAYOR | PAYOR_ID | Unknown | Unknown | No |  |
| 3 | FINANCIAL_CLASS | CLARITY_FC | FINANCIAL_CLASS | No | No | No |  |
| 3 | FINANCIAL_CLASS | ZC_ACTN_FIN_CLASS | ACTION_FIN_CLASS | No | No | No |  |
| 3 | FINANCIAL_CLASS | ZC_CUR_FIN_CLASS | CUR_FIN_CLASS | No | No | No |  |
| 3 | FINANCIAL_CLASS | ZC_FC_MEDICAID | FC_MEDICAID_C | No | No | No |  |
| 3 | FINANCIAL_CLASS | ZC_FINANCIAL_CLASS | FINANCIAL_CLASS | No | No | No |  |
| 3 | FINANCIAL_CLASS | ZC_FIN_CLASS | FIN_CLASS_C | No | No | No |  |
| 3 | FINANCIAL_CLASS | ZC_ORIG_FIN_CLASS | ORIGINAL_FIN_CLASS | No | No | No |  |
| 11 | RPT_GRP_SIX | ZC_EPM_RPT_GRP_6 | RPT_GRP_SIX | No | No | No |  |
| 12 | RPT_GRP_SEVEN | ZC_EPM_RPT_GRP_7 | RPT_GRP_SEVEN | No | No | No |  |
| 13 | RPT_GRP_EIGHT | ZC_EPM_RPT_GRP_8 | RPT_GRP_EIGHT | No | No | No |  |
| 14 | RPT_GRP_NINE | ZC_EPM_RPT_GRP_9 | RPT_GRP_NINE | No | No | No |  |
| 15 | RPT_GRP_TEN | ZC_EPM_RPT_GRP_10 | RPT_GRP_TEN | No | No | No |  |
| 16 | REPRICED_HCFA_FRM | PAPER_FORM | PAPER_FORM_ID | No | No | No |  |
| 17 | REPRICED_UB_FRM | PAPER_FORM | PAPER_FORM_ID | No | No | No |  |
| 18 | BEN_BKT_OPT_C | ZC_BEN_BKT_OPT | BEN_BKT_OPT_C | No | No | No |  |
| 20 | DFLT_DRG_TYPE_ID | IDENTITY_ID_TYPE | ID_TYPE | No | No | No |  |
| 20 | DFLT_DRG_TYPE_ID | V_ZZLOV_DRG_TYPES | DRG_ID_TYPE_ID | Unknown | Unknown | No |  |
| 25 | STATE_C | ZC_ALT_INVOICE_STA | ALT_INVOICE_STA_C | No | No | No |  |
| 25 | STATE_C | ZC_LLB_STATE | LLB_STATE_C | No | No | No |  |
| 25 | STATE_C | ZC_REFG_PROV_STATE | REFG_PROV_STATE_C | No | No | No |  |
| 25 | STATE_C | ZC_STATE | STATE_C | No | No | No |  |
| 25 | STATE_C | ZC_STATE_HISTORY | STATE_HISTORY_C | No | No | No |  |

_(120 total; showing first 30)_
