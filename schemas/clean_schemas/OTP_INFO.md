# OTP_INFO

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=OTP_INFO

## Description

This table stores basic information about a treatment plan order, such as its status, display name, which medication or procedure it represents, etc.

**Primary table** in this group (100 cols). Overflow siblings joined on shared key: OTP_INFO_1 (63 cols), OTP_INFO_2 (69 cols), OTP_INFO_3 (100 cols), OTP_INFO_4 (43 cols), OTP_INFO_5 (10 cols). Prefer this table for most queries.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | OTP |
| Release Version | SPRING 2008 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| OTP_ID | NUMERIC (18,0) | The unique identifier for the patient order template record. |
| CM_PHY_OWNER_ID | VARCHAR (25) | ID of the physical deployment owner for this record.  Physical owners will be where the data is hosted, either on the cross-over server or the owner deployment. |
| CM_LOG_OWNER_ID | VARCHAR (25) | ID of the logical deployment owner for this record.  Logical owners show the deployment where the record was created but doesn't represent if the record is a part of version skew. |
| ORDER_TYPE_C | INTEGER |  |
| PROC_ID | NUMERIC (18,0) | The unique ID of the procedure linked to the order template in this row. |
| ORDER_DESC | VARCHAR (254) | The description of the order linked to the order template in this row. |
| DISPLAY_NAME | VARCHAR (500) | The display name of the order template in this row. |
| PRESEL_DISPLAY_NAME | VARCHAR (254) | The pre-selection display name for the order template in this row. |
| ORDER_CLASS_C | VARCHAR (66) |  |
| RESULTING_AGENCY_ID | NUMERIC (18,0) | The resulting agency ID of the order template in this row. |
| OTP_STATUS_C | INTEGER |  |
| PRIORITY_C | INTEGER |  |
| PREAUTH_PROV_ID | VARCHAR (18) | The provider ID of the person who signed the order template in this row; or, for a dual-sign medication order, the provider ID of the person who gave the second signature. |
| OTP_PREAUTH_INST | DATETIME (Local) | The date/time in external format when the order template in this row was signed. |
| DUAL_SIGN_PROV_ID | VARCHAR (18) | The provider ID of the first person who signed the order template in this row. |
| DUAL_SIGN_INST | DATETIME (Local) | The date/time in external format when the first signature was given for the order template in this row. |
| ORDERING_QUANTITY | NUMERIC (18,0) | The ordering quantity of the order template in this row. |
| DX_FOLLOW_UP_C | INTEGER |  |
| CHECK_OUT_COMMENT | VARCHAR (508) | The check-out comments for the order template in this row. |
| SPECIMEN_TYPE_C | INTEGER |  |
| SPECIMEN_SOURCE_C | INTEGER |  |
| ORD_SIGN_CONTEXT_C | INTEGER |  |
| ORD_SIGN_WKS_ID | VARCHAR (18) | The workstation at which the order template in this row was signed. |
| ORD_SIGN_RESULT_C | INTEGER |  |
| ORD_SIGN_DEVICE_C | INTEGER |  |
| DUAL_SIGN_CONTEXT_C | INTEGER |  |
| DUAL_SIGN_WKS_ID | VARCHAR (18) | The workstation of the first signing of the order template in this row. |
| DUAL_SIGN_RESULT_C | INTEGER |  |
| DUAL_SIGN_DEVICE_C | INTEGER |  |
| ORDER_ID | NUMERIC (18,0) | The unique identifier of the order record linked to the order template in this row. |
| STANDING_ORDER_C | INTEGER |  |
| STANDING_EXP_DATE | VARCHAR (100) | The standing expiration date of the order template in this row. |
| FUT_EXPECT_COMP_DT | VARCHAR (100) | The future expected completion date of the order template in this row. |
| FUT_APPROX_DT_YN | VARCHAR (1) |  |
| STAND_INTERVAL | VARCHAR (100) | The standing interval for the order template in this row. |
| DISCRETE_INTERVAL_C | VARCHAR (66) |  |
| STAND_OCCUR | NUMERIC (18,0) | The standing occurrences for the order template in this row. |
| STAND_ORIG_OCCUR | NUMERIC (18,0) | The original number of standing occurrences for the order template in this row. |
| PERFORMING_DEPT_ID | NUMERIC (18,0) | The performing department for the order template in this row. |
| REFG_PROV_ID | VARCHAR (18) | The ID of the referring provider for the order template in this row. |
| SER_ADDRESSID | VARCHAR (254) | Stores the referring provider address ID for referral orders. The format is provider external ID - Address line number. For example, if provider external ID = 123 and Address line = 4, the value would be 123-4. If the referring provider has no address, this will store the provider external ID only. |
| REFD_TO_PROV_ID | VARCHAR (18) | The referred-to provider for the order template in this row. |
| REFD_TO_FACILITY_ID | NUMERIC (18,0) | The referred-to facility for the order template in this row. |
| REFD_TO_SPECLTY_C | VARCHAR (66) |  |
| DEPT_REF_TO_ID | NUMERIC (18,0) | The referred-to department for the order template in this row. |
| DEPT_SPEC_REF_TO_C | VARCHAR (66) |  |
| RFL_PRIORITY_C | VARCHAR (66) |  |
| RFL_TYPE_C | VARCHAR (66) |  |
| RSN_FOR_RFL_C | VARCHAR (66) |  |
| RFL_NUM_VIS | NUMERIC (18,0) | The referral number of visits for the order template in this row. |
| RFL_EXPIRE_DT | VARCHAR (100) | The referral expiration date for the order template in this row. |
| PRN_COMMENT | VARCHAR (450) | The user-entered comments for why the PRN medication should be administered. |
| MED_ID | NUMERIC (18,0) | The ID of the linked medication for the order template in this row. |
| MED_CONTACT_DAT | NUMERIC (18,0) | The contact date of the linked medication for the order template in this row. |
| MED_ROUTE_C | INTEGER |  |
| MED_QUANTITY | VARCHAR (50) | The quantity of the linked medication for the order template in this row. |
| MED_REFILLS | VARCHAR (50) | The refill information for the linked medication for the order template in this row. |
| MED_DIRECTIONS *(deprecated)* | VARCHAR (450) |  |
| MED_DIRECTN_LONG | VARCHAR (1000) | The long version of the instructions for the medication linked to the order template in this row. |
| MED_START_DATE | VARCHAR (100) | The start date of the medication linked to the order template in this row. |
| START_TIME | DATETIME (Local) | The start time of the medication linked to the order template in this row. |
| MED_END_TIME | DATETIME (Local) | The end time of the medication linked to the order template in this row. |
| MED_END_DATE | VARCHAR (100) | The end date of the medication linked to the order template in this row. |
| DISP_AS_WRITTEN_YN | VARCHAR (1) |  |
| MED_DFL_DSCR_FRQ_YN | VARCHAR (1) |  |
| MED_DFL_DSCR_DOS_YN | VARCHAR (1) |  |
| MED_NF_CODE_C | INTEGER |  |
| MED_COMMENTS | VARCHAR (300) | The medication comments for the medication linked to the order template in this row. |
| MED_NUM_OF_DOSES | NUMERIC (18,0) | The number of doses for the medication linked to the order template in this row. |
| MED_TYPE_C | INTEGER |  |
| MODIFIED_MIXTURE_YN | VARCHAR (1) |  |
| MED_INFUSION_TYPE_C | INTEGER |  |
| MED_INFUSION_RATE | VARCHAR (100) | The infusion rate for the medication linked to the order template in this row. |
| MED_RATE_UNIT_C | INTEGER |  |
| MED_INFUSE_DURATION | VARCHAR (100) | The duration for the medication linked to the order template in this row. |
| MED_DURATION_UNIT_C | INTEGER |  |
| TPN_SITE_C | INTEGER |  |
| MED_VOLUME | VARCHAR (100) | The volume of the medication linked to the order template in this row. |
| MED_VOLUME_UNIT_C | INTEGER |  |
| CALCULATE_VOLUME_YN | VARCHAR (1) |  |
| MIXTURE_CONC_C | INTEGER |  |
| DISCRETE_FREQ_ID | VARCHAR (18) | The discrete frequency for the medication linked to the order template in this row. |
| DISCRETE_DOSE_MIN | VARCHAR (254) | The minimum discrete dose for a medication whose dose was entered as a range, or the discrete dose amount for a medication whose dose was not entered as a range. |
| DISC_DOSE_UNIT *(deprecated)* | VARCHAR (254) |  |
| DOSE_UNIT_C | INTEGER |  |
| ORDER_TIME_PRIOR_C | VARCHAR (18) |  |
| ENC_CSN | NUMERIC (18,0) | The contact serial number (CSN) of the encounter linked to the order template in this row. |
| ENC_ASN | NUMERIC (18,0) | The appointment serial number (ASN) of the appointment linked to the order template in this row. |
| ORDER_FREQ | VARCHAR (100) | The frequency of the medication being ordered in this order template. |
| OTP_TPL_ID | NUMERIC (18,0) | The ID of the treatment plan that contains this order template. |
| OTP_TRG_ID | NUMERIC (18,0) | The ID of the treatment day that contains this order template. |
| DISCRETE_DOSE_MAX | VARCHAR (254) | The maximum discrete dose for a medication whose dose was entered as a range. |
| MAX_DOSE | NUMERIC (19,4) | This column stores the suggested maximum dose amount for the patient order template record. |
| MAX_DOSE_UNIT_C | INTEGER |  |
| USR_SEL_IMS_YN | VARCHAR (1) |  |
| OVRD_IMS_PROD_ID | NUMERIC (18,0) | If the user has indicated that a specific product should be used for this order; that product will be stored here. |
| INDICATION_COMMENTS | VARCHAR (300) | User's comments for the corresponding Indications of Use (stored in OTP_INDICATIONS table) |
| MED_DISP_QTY | NUMERIC (19,4) | This item stores the medication dispense quantity when discrete dispense is enabled. |
| MED_DISP_UNIT_C | INTEGER |  |
| MAX_BSA | NUMERIC (18,5) | The maximum Body Surface Area (BSA) for an order, if the selected BSA is greater than this BSA than the selected BSA will be capped at this value. |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | OTP_ID | ADT_PAT_ORDER_TEMPLATE | OTP_ID | No | No | No |  |
| 1 | OTP_ID | CL_OTP_FST_LST_SCH | OTP_ID | Unknown | No | No |  |
| 1 | OTP_ID | OTP_DOSE_PARAMS | OTP_ID | Unknown | No | No |  |
| 1 | OTP_ID | OTP_INFO_1 | OTP_ID | Unknown | No | No |  |
| 1 | OTP_ID | OTP_INFO_2 | OTP_ID | Unknown | No | No |  |
| 1 | OTP_ID | OTP_INFO_3 | OTP_ID | Unknown | No | No |  |
| 1 | OTP_ID | OTP_INFO_4 | OTP_ID | Unknown | No | No |  |
| 1 | OTP_ID | OTP_INFO_5 | OTP_ID | No | No | No |  |
| 1 | OTP_ID | OTP_ROUTING | OTP_ID | Unknown | No | No |  |
| 2 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 2 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 2 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 3 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 4 | ORDER_TYPE_C | ZC_DFLT_ORDER_TYPE | DFLT_ORDER_TYPE_C | No | No | No |  |
| 4 | ORDER_TYPE_C | ZC_EDP_ORDER_TYPE | ORDER_TYPE_C | No | No | No |  |
| 4 | ORDER_TYPE_C | ZC_ORDER_TYPE | ORDER_TYPE_C | No | No | No |  |
| 5 | PROC_ID | CLARITY_EAP | PROC_ID | No | No | No |  |
| 5 | PROC_ID | CLARITY_EAP_2 | PROC_ID | No | No | No |  |
| 5 | PROC_ID | CLARITY_EAP_3 | PROC_ID | No | No | No |  |
| 5 | PROC_ID | CLARITY_EAP_4 | PROC_ID | No | No | No |  |
| 5 | PROC_ID | CLARITY_EAP_5 | PROC_ID | No | No | No |  |
| 5 | PROC_ID | CLARITY_EAP_IMM | PROC_ID | Unknown | No | No |  |
| 5 | PROC_ID | PROC_CONSENT_CONFIG | PROC_ID | No | No | No |  |
| 5 | PROC_ID | PROC_UM | PROC_ID | No | No | No |  |
| 5 | PROC_ID | V_CUBE_D_PROCEDURE | PROCEDURE_ID | Unknown | Unknown | No |  |
| 9 | ORDER_CLASS_C | ZC_LLB_ORDER_CLASS | LLB_ORDER_CLASS_C | No | No | No |  |
| 9 | ORDER_CLASS_C | ZC_ORDER_CLASS | ORDER_CLASS_C | No | No | No |  |
| 9 | ORDER_CLASS_C | ZC_PANEL_INP_CLASS | PANEL_INP_CLASS_C | No | No | No |  |

_(532 total; showing first 30)_
