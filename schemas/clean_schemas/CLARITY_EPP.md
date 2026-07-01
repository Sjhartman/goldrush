# CLARITY_EPP

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=CLARITY_EPP

## Description

The CLARITY_EPP table contains basic information about your benefit plans.

**Primary table** in this group (114 cols). Overflow siblings joined on shared key: CLARITY_EPP_2 (86 cols), CLARITY_EPP_3 (28 cols). Prefer this table for most queries.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | EPP |
| Release Version | EPIC 2000 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| BENEFIT_PLAN_ID | NUMERIC (18,0) | The unique ID assigned to the benefit plan record in the system. |
| BENEFIT_PLAN_NAME | VARCHAR (100) | The name of the benefit plan record. |
| PRODUCT_TYPE *(deprecated)* | VARCHAR (254) |  |
| RPT_GRP_ONE | VARCHAR (80) | You have the ability to specify groupers for enterprise reporting, SQL, or report generator reporting. There are free text groupers and category groupers. If you elect to use these groupers, please contact your enterprise reporting representative for assistance. This is one of the free text report groupers. There are more report grouper columns in the CLARITY_EPP_2 table. |
| RPT_GRP_TWO | VARCHAR (80) | You have the ability to specify groupers for enterprise reporting, SQL, or report generator reporting. There are free text groupers and category groupers. If you elect to use these groupers, please contact your enterprise reporting representative for assistance. This is one of the free text report groupers. There are more report grouper columns in the CLARITY_EPP_2 table. |
| RPT_GRP_THREE | VARCHAR (80) | You have the ability to specify groupers for enterprise reporting, SQL, or report generator reporting. There are free text groupers and category groupers. If you elect to use these groupers, please contact your enterprise reporting representative for assistance. This is one of the free text report groupers. There are more report grouper columns in the CLARITY_EPP_2 table. |
| RPT_GRP_FOUR | VARCHAR (80) | You have the ability to specify groupers for enterprise reporting, SQL, or report generator reporting. There are free text groupers and category groupers. If you elect to use these groupers, please contact your enterprise reporting representative for assistance. This is one of the free text report groupers. There are more report grouper columns in the CLARITY_EPP_2 table. |
| RPT_GRP_FIVE | VARCHAR (80) | You have the ability to specify groupers for enterprise reporting, SQL, or report generator reporting. There are free text groupers and category groupers. If you elect to use these groupers, please contact your enterprise reporting representative for assistance. This is one of the free text report groupers. There are more report grouper columns in the CLARITY_EPP_2 table. |
| RPT_GRP_SIX | VARCHAR (66) |  |
| RPT_GRP_SEVEN | VARCHAR (66) |  |
| RPT_GRP_EIGHT | VARCHAR (66) |  |
| RPT_GRP_NINE | VARCHAR (66) |  |
| RPT_GRP_TEN | VARCHAR (66) |  |
| BEN_BKT_OPT_C | INTEGER |  |
| IN_OUT_NET_D_C | INTEGER |  |
| PB_GL_SEG | VARCHAR (100) | The G/L segment value for this benefit plan for premium billing G/L transactions. |
| AP_CLM_GL_SEG | VARCHAR (12) | The G/L segment value for this benefit plan for AP claims G/L transactions. |
| CAP_AP_GL_SEG | VARCHAR (12) | The G/L segment value for this benefit plan for capitation AP G/L transactions. |
| CAP_RR_GL_SEG | VARCHAR (12) | The G/L segment value for this benefit plan for capitation receipt and reconciliation G/L transactions. |
| LIFEMAX_LIMIT_IN | NUMERIC (12,2) | The lifetime maximum buckets limit for in-plan buckets. |
| LIFEMAX_LIMIT_OUT | NUMERIC (12,2) | The lifetime maximum buckets limit for out-of-plan buckets. |
| LIFEMAX_LIMIT_ALL | NUMERIC (12,2) | The lifetime maximum buckets limit for total accumulation. |
| LIFEMAX_DOLLAR_IN | NUMERIC (12,2) | The lifetime maximum buckets dollar amount threshold for in-plan buckets. |
| LIFEMAX_DOLLAR_OUT | NUMERIC (12,2) | The lifetime maximum buckets dollar amount threshold for out-of-plan buckets. |
| LIFEMAX_DOLLAR_ALL | NUMERIC (12,2) | The lifetime maximum buckets dollar amount threshold for total accumulation of buckets. |
| LIFEMAX_PER_IN | NUMERIC (12,2) | The lifetime maximum buckets percentage of total threshold for in-plan buckets. |
| LIFEMAX_PER_OUT | NUMERIC (12,2) | The lifetime maximum buckets percentage of total threshold for out-of-plan buckets. |
| LIFEMAX_PER_ALL | NUMERIC (12,2) | The lifetime maximum buckets percentage of total threshold for total accumulation of buckets. |
| PLAN_TYPE_C | INTEGER |  |
| CVG_TYPE_C | INTEGER |  |
| PLAN_BILL_TYPE_C *(deprecated)* | INTEGER |  |
| IS_DED_TO_MOOP_C *(deprecated)* | INTEGER |  |
| ALL_ENC_TO_MOOP_C *(deprecated)* | INTEGER |  |
| CARRYOVER_CLASS_C | INTEGER |  |
| PB_SAVINGS_PRCNTG | NUMERIC (7,2) | This is the percentage amount multiplied against premium payments in determining the amount by which benefit buckets should accumulate. |
| PPO_ADDRESS | VARCHAR (255) | The mailing address in this field will be used to create reprice cover sheet for this plan. |
| PPO_CITY | VARCHAR (40) | The city entered here will be used to create reprice cover sheet for this plan. |
| PPO_STATE_C | VARCHAR (66) |  |
| PPO_ZIP_CODE | VARCHAR (50) | The ZIP Code entered here will be used to create reprice cover sheet for this plan. |
| PPO_PHONE_NUMBER | VARCHAR (50) | The phone number entered here will be used to create reprice cover sheet for this plan. |
| PAYOR_ID | NUMERIC (18,0) | The unique ID of the payor associated with this benefit plan. |
| BP_ADDR_LINE1 | VARCHAR (80) | The street address of the benefit plan, line 1. |
| BP_ADDR_LINE2 | VARCHAR (80) | The street address of the benefit plan, line 2. |
| BP_CITY | VARCHAR (50) | The city of the benefit plan. |
| BP_STATE_C | VARCHAR (66) |  |
| BP_ZIP | VARCHAR (50) | The zip code of the benefit plan. |
| BP_PHONE | VARCHAR (50) | The phone number of the benefit plan. |
| SHORT_NAME | VARCHAR (254) | The short name of the benefit plan |
| CM_PHY_OWNER_ID | VARCHAR (25) | ID of the physical deployment owner for this record.  Physical owners will be where the data is hosted, either on the cross-over server or the owner deployment. |
| CM_LOG_OWNER_ID | VARCHAR (25) | ID of the logical deployment owner for this record.  Logical owners show the deployment where the record was created but doesn't represent if the record is a part of version skew. |
| RECORD_STAT_EPP_C | INTEGER |  |
| IS_GEN_EOB_YN | VARCHAR (254) |  |
| BP_FAX | VARCHAR (50) | The fax number of the benefit plan. |
| MSP_TYPE_C | INTEGER |  |
| ALT_CLM_CITY | VARCHAR (50) | The alternate mailing city for this plan.  The address can be used to send claims to an alternate address.  The alternate claim address is found in the EPP_ALT_CLM_ADDR table. |
| ALT_CLM_STATE_C | VARCHAR (66) |  |
| ALT_CLM_ZIP_CODE | VARCHAR (50) | The alternate mailing zip code for this plan.  The address can be used to send claims to an alternate plan address.  The alternate claim address is found in the EPP_ALT_CLM_ADDR table. |
| OVERRIDE_PAYOR_YN | NUMERIC (18,0) |  |
| BP_COUNTY_C | VARCHAR (66) |  |
| BP_COUNTRY_C | VARCHAR (66) |  |
| BP_HOUSE_NUMBER | VARCHAR (20) | The house number of the benefit plan. |
| BP_DISTRICT_C | INTEGER |  |
| CARRIER_ID | VARCHAR (18) | The unique ID of the carrier |
| ALLOW_PCP_EDITIN_YN *(deprecated)* | VARCHAR (1) |  |
| DEFAULT_COPAY | NUMERIC (18,2) | Indicates the default copay. |
| ALT_ID_RC_BY_PLN | VARCHAR (254) | Alternate Plan Identifier for Revenue Code |
| EPP_PLAN_GENERIC_YN | VARCHAR (1) |  |
| PLAN_NAME_OPT_YN | VARCHAR (1) |  |
| CLAIM_MAIL_CODE_C | INTEGER |  |
| PLAN_CODE_ON_PAPER | VARCHAR (254) | Text for plan code to be printed on paper claims. |
| PLAN_CODE_ON_ELEC | VARCHAR (254) | Text for plan code printed on electronic claims. |
| PAYOR_ORG_ID | VARCHAR (254) | Plan's payor organization ID.  Used to populate L2010BB/NM1-09 (Professional), L2010BC/NM1-09 (Institutional), or L2330B/NM1-09 (ANSI 837) fields. |
| MEDIGAP_NUM | VARCHAR (254) | Plan's Medigap Number.  Used to populate L2010BB/NM1-09 and L2330B/NM1-09 fields on ANSI 837 format. |
| MEDIGAP_PLAN_YN | VARCHAR (1) |  |
| XOVER_APP_C | VARCHAR (66) |  |
| SAVE_FULL_GP_RES_YN | VARCHAR (1) |  |
| APC_GRP_DISP_PP_ID | NUMERIC (18,0) | This item holds the extension that displays an alternate view of the APC Grouper messages for a claim. |
| ANES_PRICING_ID | NUMERIC (18,0) | Anesthesia Pricing ID for this plan. |
| SHOW_ASA_CODE_YN | VARCHAR (1) |  |
| ANES_UN_MIN_YN | VARCHAR (1) |  |
| ANES_P_MODS_YN | VARCHAR (1) |  |
| VOIDS_DMD_RPRT_YN | VARCHAR (1) |  |
| PAPER_CLAIM_YN | VARCHAR (1) |  |
| CLM_FIN_CL_C | VARCHAR (66) |  |
| ALT_CLM_PHONE | VARCHAR (15) | Stores alternate claim phone number |
| EXCLD_PB_FO_YN | VARCHAR (1) |  |
| CLAIM_DEF_PLAN_ID | NUMERIC (18,0) | Default claim definition record to use for claims to this plan. |
| OK_RESUB_ZERO_YN | VARCHAR (1) |  |
| OK_SUBMT_ZERO_IN_YN | VARCHAR (1) |  |
| PAID_DEMAND_CLM_YN | VARCHAR (1) |  |
| CLM_GRP_PTER_ID | NUMERIC (18,0) | Claim grouping pointer for this benefit plan. |
| RESUB_ZERO_CMG_ID | VARCHAR (200) | The component group ID that must be used in order to resubmit charges with a zero dollar balance. |
| SUBMIT_ZERO_INS_ID | VARCHAR (200) | The component group ID that must be used in order to submit charges with a zero dollar balance on insurance claims. |
| DMD_ZERO_CMG_ID | VARCHAR (200) | The component group ID that must be used in order to submit charges with a zero dollar balance on a demand claim. |
| PAPER_CRD_YN *(deprecated)* | VARCHAR (1) |  |
| ELCT_CRD_YN *(deprecated)* | VARCHAR (1) |  |
| PRNT_TAXO_YN | VARCHAR (1) |  |
| PROD_PRT_B_CLM_YN | VARCHAR (1) |  |
| SUPP_PMT_PAYOR_ID | NUMERIC (18,0) | Payor ID for Medicare for supplemental payment (IME) claims |
| SUPP_PMT_PLAN_ID | NUMERIC (18,0) | Plan ID for Medicare for supplemental payment (IME) claims |
| MAX_SVC_LINES_CMS | NUMERIC (18,0) | Stores the maximum number of service lines on a claim for this benefit plan on a CMS claim. |
| ADJ_GRPR_SEC_CLM_C | INTEGER |  |
| ADJUSTMENT_CODE | VARCHAR (254) | Remittance code to be associated with capitation adjustments that should be treated as payments in electronic secondary claims logic. |
| DEFAULT_CHG_TBL_ID | VARCHAR (18) | Plan level default charge table ID to use during prescription medication charge calculations. |
| CHG_TBL_LPP_ID | NUMERIC (18,0) | Plan level charge table selection extension to use during prescription medication charge calculations |
| ADJUD_CHARGE_VIA_C | INTEGER |  |
| COVERED_PERCENTAGE | NUMERIC (18,10) | Indicates the percentage of the price that the payor is responsible for if Specified Percentage is selected in the Adjudicate Charge Via item. The remaining balance will be charged to the patient. |
| ADJUD_PP_ID | NUMERIC (18,0) | The extension that determines how much the payor will pay and how much the patient will pay for the order. |
| COPY_IME_LINES_YN | VARCHAR (1) |  |
| USE_IN_SHARED_CV_YN | VARCHAR (1) |  |
| ADMSN_BILL_YN | VARCHAR (1) |  |
| INTERF_CVGCREATE_ID | NUMERIC (18,0) | This item specifies a second interface items table, to be used when creating a coverage from an incoming message (rather than updating an existing coverage). |
| PREVENT_DUP_CVG_C | INTEGER | Surrogate key used to uniquely identify rows in this (and only this) table on Cogito Cloud only, do not assume the surrogate key in this table will correspond to the surrogate key in another table |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | BENEFIT_PLAN_ID | CLARITY_EPP_2 | BENEFIT_PLAN_ID | No | No | No |  |
| 1 | BENEFIT_PLAN_ID | CLARITY_EPP_3 | BENEFIT_PLAN_ID | No | No | No |  |
| 1 | BENEFIT_PLAN_ID | CLARITY_EPP_CERTIF | BENEFIT_PLAN_ID | No | No | No |  |
| 1 | BENEFIT_PLAN_ID | DENT_PLAN_BENEFITS_FLAGS | BENEFIT_PLAN_ID | No | No | No |  |
| 1 | BENEFIT_PLAN_ID | V_CUBE_D_BENEFIT_PLAN | BENEFIT_PLAN_ID | Unknown | Unknown | No |  |
| 9 | RPT_GRP_SIX | ZC_EPP_RPT_GRP_6 | RPT_GRP_SIX | No | No | No |  |
| 10 | RPT_GRP_SEVEN | ZC_EPP_RPT_GRP_7 | RPT_GRP_SEVEN | No | No | No |  |
| 11 | RPT_GRP_EIGHT | ZC_EPP_RPT_GRP_8 | RPT_GRP_EIGHT | No | No | No |  |
| 12 | RPT_GRP_NINE | ZC_EPP_RPT_GRP_9 | RPT_GRP_NINE | No | No | No |  |
| 13 | RPT_GRP_TEN | ZC_EPP_RPT_GRP_10 | RPT_GRP_TEN | No | No | No |  |
| 14 | BEN_BKT_OPT_C | ZC_BEN_BKT_OPT | BEN_BKT_OPT_C | No | No | No |  |
| 15 | IN_OUT_NET_D_C | ZC_IN_OUT_NET_D | IN_OUT_NET_D_C | No | No | No |  |
| 29 | PLAN_TYPE_C | ZC_PLAN_TYPE | PLAN_TYPE_C | No | No | No |  |
| 30 | CVG_TYPE_C | ZC_CVG_TYPE | CVG_TYPE_C | No | No | No |  |
| 34 | CARRYOVER_CLASS_C | ZC_CARRYOVER_CLASS | CARRYOVER_CLASS_C | No | No | No |  |
| 34 | CARRYOVER_CLASS_C | ZC_CARRYOVER_CLA_2 | CARRYOVER_CLA_2_C | No | No | No |  |
| 38 | PPO_STATE_C | ZC_ALT_INVOICE_STA | ALT_INVOICE_STA_C | No | No | No |  |
| 38 | PPO_STATE_C | ZC_LLB_STATE | LLB_STATE_C | No | No | No |  |
| 38 | PPO_STATE_C | ZC_REFG_PROV_STATE | REFG_PROV_STATE_C | No | No | No |  |
| 38 | PPO_STATE_C | ZC_STATE | STATE_C | No | No | No |  |
| 38 | PPO_STATE_C | ZC_STATE_HISTORY | STATE_HISTORY_C | No | No | No |  |
| 38 | PPO_STATE_C | ZC_SUBSCR_EEP_STE | SUBSCR_EEP_STE_C | No | No | No |  |
| 38 | PPO_STATE_C | ZC_TAX_STATE | TAX_STATE_C | No | No | No |  |
| 41 | PAYOR_ID | CLARITY_EPM | PAYOR_ID | No | No | No |  |
| 41 | PAYOR_ID | CLARITY_EPM_2 | PAYOR_ID | No | No | No |  |
| 41 | PAYOR_ID | CLARITY_EPM_3 | PAYOR_ID | No | No | No |  |
| 41 | PAYOR_ID | DENT_PAYER_BENEFITS_FLAGS | PAYOR_ID | No | No | No |  |
| 41 | PAYOR_ID | EPM_CLM_FILING_INF | PAYOR_ID | No | No | No |  |
| 41 | PAYOR_ID | EPM_CLM_FRM_OPTION | PAYOR_ID | No | No | No |  |
| 41 | PAYOR_ID | EPM_CLM_PRNT_OPTN | PAYOR_ID | No | No | No |  |

_(122 total; showing first 30)_
