# CLARITY_EPP_2

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=CLARITY_EPP_2

## Description

The CLARITY_EPP_2 table contains additional information about your benefit plan records.

**Overflow table** for CLARITY_EPP (114 cols). Contains additional columns for the same records — join on the shared primary key column.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | EPP |
| Release Version | Summer 2009 |
| May contain EHI? | No |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| BENEFIT_PLAN_ID | NUMERIC (18,0) | The unique identifier (.1 item) for the benefit plan record. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| USE_ACCEL_SP_YN *(deprecated)* | VARCHAR (1) |  |
| DFLT_DRG_TYPE_ID | NUMERIC (18,0) | The default DRG Type (MPI ID) used for billing by the benefit plan. |
| BDRG_TYP_REF_DT_C | INTEGER |  |
| MIXTURE_DISP_FEE | NUMERIC (18,3) | The default mixture dispensing fee when calculating the plan price for prescription. |
| RPT_GRP_ELEVEN_C | VARCHAR (66) |  |
| RPT_GRP_TWELVE_C | VARCHAR (66) |  |
| RPT_GRP_THIRTEEN_C | VARCHAR (66) |  |
| RPT_GRP_FOURTEEN_C | VARCHAR (66) |  |
| RPT_GRP_FIFTEEN_C | VARCHAR (66) |  |
| RPT_GRP_SIXTEEN_C | VARCHAR (66) |  |
| RPT_GRP_SEVENTEEN_C | VARCHAR (66) |  |
| RPT_GRP_EIGHTEEN_C | VARCHAR (66) |  |
| RPT_GRP_NINETEEN_C | VARCHAR (66) |  |
| RPT_GRP_TWENTY_C | VARCHAR (66) |  |
| BIN_NUM | VARCHAR (30) | The Bank Information Number (BIN) used during prescription adjudication.  If blank at the plan level, the payor level BIN is used. |
| NON_PRIMARY_BIN_NUM | VARCHAR (30) | The Bank Information Number (BIN) used during prescription adjudication for non-primary coverages. Leave this field blank if the same BIN is used regardless of whether the coverage is primary or secondary.  If no non-primary BIN is specified, the BIN will be used for non-primary coverages. If blank at the plan level, the payor level BINs are used. |
| PROCESSOR_CNTRL_NUM | VARCHAR (10) | The Processor Control Number (PCN) used during prescription adjudication.  If blank at the plan level the payor level PCN is used. |
| NON_PRIMARY_PCN | VARCHAR (30) | The Processor Control Number (PCN) used during prescription adjudication for non-primary coverages. Leave this field blank if the same PCN is used regardless of whether the coverage is primary or secondary.  If no non-primary PCN is specified, the PCN will be used for non-primary coverages. If blank at the plan level, the payor level PCNs are used. |
| PAYOR_SHEET_PP_ID | NUMERIC (18,0) | Extension to select what payor sheet to use during prescription adjudication. If the extension does not return a value, the transaction table will be used to find the payor sheet.  The plan level payor sheet extension is always checked first, then the plan level table, then the payor level payor sheet extension, and then the payor level table. |
| SUP_PART_FILLS_YN | VARCHAR (1) |  |
| ALT_PROCCD_BY_PLAN | VARCHAR (254) | Alternate identifier for Procedure code in the Procedure master file |
| PROD_TYPE_C | VARCHAR (66) |  |
| RPT_GRP_TWENTYONE | VARCHAR (80) | You have the ability to specify groupers for enterprise reporting, SQL, or report generator reporting. There are free text groupers and category groupers. If you elect to use these groupers, please contact your enterprise reporting representative for assistance. This is one of the free text report groupers. There are more report grouper columns in the CLARITY_EPP table and the CLARITY_EPP_OT table. |
| RPT_GRP_TWENTYTWO | VARCHAR (80) | You have the ability to specify groupers for enterprise reporting, SQL, or report generator reporting. There are free text groupers and category groupers. If you elect to use these groupers, please contact your enterprise reporting representative for assistance. This is one of the free text report groupers. There are more report grouper columns in the CLARITY_EPP table and the CLARITY_EPP_OT table. |
| RPT_GRP_TWENTYTHREE | VARCHAR (80) | You have the ability to specify groupers for enterprise reporting, SQL, or report generator reporting. There are free text groupers and category groupers. If you elect to use these groupers, please contact your enterprise reporting representative for assistance. This is one of the free text report groupers. There are more report grouper columns in the CLARITY_EPP table and the CLARITY_EPP_OT table. |
| RPT_GRP_TWENTYFOUR | VARCHAR (80) | You have the ability to specify groupers for enterprise reporting, SQL, or report generator reporting. There are free text groupers and category groupers. If you elect to use these groupers, please contact your enterprise reporting representative for assistance. This is one of the free text report groupers. There are more report grouper columns in the CLARITY_EPP table and the CLARITY_EPP_OT table. |
| RPT_GRP_TWENTYFIVE | VARCHAR (80) | You have the ability to specify groupers for enterprise reporting, SQL, or report generator reporting. There are free text groupers and category groupers. If you elect to use these groupers, please contact your enterprise reporting representative for assistance. This is one of the free text report groupers. There are more report grouper columns in the CLARITY_EPP table and the CLARITY_EPP_OT table. |
| RPT_GRP_TWENTYSIX_C | VARCHAR (66) |  |
| RPT_GRP_TWNTYSVN_C | VARCHAR (66) |  |
| RPT_GRP_TWNTYEGHT_C | VARCHAR (66) |  |
| RPT_GRP_TWNTYNINE_C | VARCHAR (66) |  |
| RPT_GRP_THIRTY_C | VARCHAR (66) |  |
| RPT_GRP_THRTYONE_C | VARCHAR (66) |  |
| RPT_GRP_THRTYTWO_C | VARCHAR (66) |  |
| RPT_GRP_THRTYTHRE_C | VARCHAR (66) |  |
| RPT_GRP_THRTYFOUR_C | VARCHAR (66) |  |
| RPT_GRP_THRTYFIVE_C | VARCHAR (66) |  |
| RPT_GRP_THRTYSIX_C | VARCHAR (66) |  |
| RPT_GRP_THRTYSVN_C | VARCHAR (66) |  |
| RPT_GRP_THRTYEGHT_C | VARCHAR (66) |  |
| RPT_GRP_THRTYNINE_C | VARCHAR (66) |  |
| RPT_GRP_FORTY_C | VARCHAR (66) |  |
| INC_BAD_DEBT_YN | VARCHAR (1) |  |
| CAP_RR_TOLERANCE | NUMERIC (18,2) | Rate tolerance to be used when an incoming capitation reconciliation is done against a coverage with this plan. |
| MC_CVG_CLASS_C | VARCHAR (66) |  |
| TIER_BEN_PLAN_YN | VARCHAR (1) |  |
| PLAN_DESC_URL | VARCHAR (254) | URL of the page to display when the plan hyperlink is clicked by an employee during online enrollment. |
| PRE_AUTH_PHONE_NUM | VARCHAR (40) | The phone number for the authorization contact at this plan. |
| CLAIM_MAX_FILE_DAYS | INTEGER | Plan specific limit on the number of days from the date of service by which claims must be filed. |
| PMT_TYPOLOGY_C | INTEGER |  |
| CHK_XOVERREMIT_YN | VARCHAR (1) |  |
| CASE_INS_WO_CODE_ID | NUMERIC (18,0) | The insurance write-off procedure used to write off case charges to zero balance in case rate insurance payment posting. |
| CASE_DB_ADJ_CODE_ID | NUMERIC (18,0) | The insurance debit adjustment procedure used to offset the overpaid portion of an insurance payment. |
| ALLOW_PCP_ADDING_C | INTEGER |  |
| CMPR_MEM_ID_5010_YN | VARCHAR (1) |  |
| ALLOW_PCP_EDITING_C | INTEGER |  |
| SURCHARGE_GROUP_C | INTEGER |  |
| PLAN_APPEAL_WINDOW | INTEGER | The number of days a plan allows for appeal of denials or underpayments. |
| ALLOW_RX_DEF_YN | VARCHAR (1) |  |
| SEC_PLAN_WINDOW | INTEGER | The number of days a plan allows for initial filing of secondary claim |
| UDS_TYPE_C | INTEGER |  |
| ALT_CLM_COUNTRY_C | VARCHAR (66) |  |
| ALT_ID | VARCHAR (192) | Alternate ID of the plan |
| USE_ELCT_VERIF_YN | VARCHAR (1) |  |
| CONTRACT_NUM | VARCHAR (30) | This column contains the Medicare Advantage contract number, which identifies the benefit plan represented by this plan record to CMS. |
| PBP_NUM | VARCHAR (30) | This column contains the unique identification number for the Plan Benefit Package, which is a set of benefits for a defined Medicare Advantage or prescription drug plan service area. |
| PART_D_RX_GRP | VARCHAR (30) | This column stores the plan's group identifier for its members. |
| PLAN_ORIGIN_CODE_C | INTEGER |  |
| ALWAYS_WO_PYR_YN | VARCHAR (1) |  |
| PAT_FRIENDLY_PLAN_NAME | VARCHAR (254) | Stores the name of the plan in a patient-friendly, correctly formatted way (not in all caps) |
| RX_SND_ZERO_CLAIM_YN | VARCHAR (1) |  |
| UDS_CVG_CLASS_C | INTEGER |  |
| RYN_WHT_MED_INSURANCE_C | INTEGER |  |
| PAYS_SIA_YN *(deprecated)* | VARCHAR (1) |  |
| RX_PA_ORGANIZATION_ID | NUMERIC (18,0) | This item specifies which Prior Authorization Payer record (DXO master file) represents the same payer associated with this plan record (EPP master file) for adjudication. |
| SOFTWARE_VENDOR_ID | VARCHAR (254) | The software vendor ID for the plan for prescription adjudication. The plan-level software vendor ID will override the payer-level software vendor ID (in EPM 7240). |
| RFLS_ARE_UM_YN | VARCHAR (1) |  |
| RIDER_TYPE_C | INTEGER |  |
| PART_D_CREDITABLE_YN | VARCHAR (1) |  |
| CONTRACT_ID | NUMERIC (18,0) | The unique ID of the pricing contract you have set up with the benefit plan. |
| EFF_FROM_DATE | DATETIME | The date the benefit plan is effective from. Registration system definition settings may be configured to screen out plans during coverage creation based on this date (I EAF 63613). For all other applications, this date is for reporting use only. |
| EFF_TO_DATE | DATETIME | The date the benefit plan is effective to. Registration system definition settings may be configured to screen out plans during coverage creation based on this date (I EAF 63613). For all other applications, this date is for reporting use only. |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | BENEFIT_PLAN_ID | CLARITY_EPP | BENEFIT_PLAN_ID | No | No | No |  |
| 1 | BENEFIT_PLAN_ID | CLARITY_EPP_3 | BENEFIT_PLAN_ID | No | No | No |  |
| 1 | BENEFIT_PLAN_ID | CLARITY_EPP_CERTIF | BENEFIT_PLAN_ID | No | No | No |  |
| 1 | BENEFIT_PLAN_ID | DENT_PLAN_BENEFITS_FLAGS | BENEFIT_PLAN_ID | No | No | No |  |
| 1 | BENEFIT_PLAN_ID | V_CUBE_D_BENEFIT_PLAN | BENEFIT_PLAN_ID | Unknown | Unknown | No |  |
| 2 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 2 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 2 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 3 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 5 | DFLT_DRG_TYPE_ID | IDENTITY_ID_TYPE | ID_TYPE | No | No | No |  |
| 5 | DFLT_DRG_TYPE_ID | V_ZZLOV_DRG_TYPES | DRG_ID_TYPE_ID | Unknown | Unknown | No |  |
| 6 | BDRG_TYP_REF_DT_C | ZC_BDRG_TYP_REF_DT | BDRG_TYP_REF_DT_C | No | No | No |  |
| 8 | RPT_GRP_ELEVEN_C | ZC_EPP_RPT_GRP_11 | RPT_GRP_ELEVEN_C | No | No | No |  |
| 9 | RPT_GRP_TWELVE_C | ZC_EPP_RPT_GRP_12 | RPT_GRP_TWELVE_C | No | No | No |  |
| 10 | RPT_GRP_THIRTEEN_C | ZC_EPP_RPT_GRP_13 | RPT_GRP_THIRTEEN_C | No | No | No |  |
| 11 | RPT_GRP_FOURTEEN_C | ZC_EPP_RPT_GRP_14 | RPT_GRP_FOURTEEN_C | No | No | No |  |
| 12 | RPT_GRP_FIFTEEN_C | ZC_EPP_RPT_GRP_15 | RPT_GRP_FIFTEEN_C | No | No | No |  |
| 13 | RPT_GRP_SIXTEEN_C | ZC_EPP_RPT_GRP_16 | RPT_GRP_SIXTEEN_C | No | No | No |  |
| 13 | RPT_GRP_SIXTEEN_C | ZC_ESOP_PLAN_NAME | ESOP_PLAN_NAME_C | No | No | No |  |
| 14 | RPT_GRP_SEVENTEEN_C | ZC_EPP_RPT_GRP_17 | RPT_GRP_SEVENTEEN_C | No | No | No |  |
| 14 | RPT_GRP_SEVENTEEN_C | ZC_ESOP_PLAN_TYPE | ESOP_PLAN_TYPE_C | No | No | No |  |
| 15 | RPT_GRP_EIGHTEEN_C | ZC_EPP_RPT_GRP_18 | RPT_GRP_EIGHTEEN_C | No | No | No |  |
| 16 | RPT_GRP_NINETEEN_C | ZC_EPP_RPT_GRP_19 | RPT_GRP_NINETEEN_C | No | No | No |  |
| 17 | RPT_GRP_TWENTY_C | ZC_EPP_RPT_GRP_20 | RPT_GRP_TWENTY_C | No | No | No |  |
| 22 | PAYOR_SHEET_PP_ID | CLARITY_LPP | LPP_ID | Unknown | No | No |  |
| 25 | PROD_TYPE_C | ZC_PROD_TYPE | PROD_TYPE_C | No | No | No |  |
| 31 | RPT_GRP_TWENTYSIX_C | ZC_RPT_GRP_TWENTYS | RPT_GRP_TWENTYS_C | No | No | No |  |
| 32 | RPT_GRP_TWNTYSVN_C | ZC_RPT_GRP_TWNTYSV | RPT_GRP_TWNTYSV_C | No | No | No |  |

_(78 total; showing first 30)_
