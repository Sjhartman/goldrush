# RX_MED_TWO

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=RX_MED_TWO

## Description

This table contains medications' information.

**Primary table** in this group (103 cols). Overflow siblings joined on shared key: RX_MED_FOUR (41 cols), RX_MED_ONE (100 cols), RX_MED_THREE (100 cols). Prefer this table for most queries.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | ERX |
| Release Version | EPIC 2002 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| MEDICATION_ID | NUMERIC (18,0) | The unique ID for this medication record. |
| MEDICATION_NAME | VARCHAR (255) | The name of this medication record. |
| RECORD_STATE_NAME | VARCHAR (255) |  |
| TEMP_NAME_EDIT | VARCHAR (255) | The temporary name of this medication record. |
| PROPTRY_STATUS_C | INTEGER |  |
| BRAND_NAME_CODE_C | INTEGER |  |
| NAME_SOURCE_C | INTEGER |  |
| CHK_INGRED_NAME *(deprecated)* | VARCHAR (255) |  |
| MEDISPAN_DDI | VARCHAR (192) | The Drug Descriptor Identifier for this medication record. |
| PHARM_SUBCLASS_C | INTEGER |  |
| SMPLE_GEN_NAM_C *(deprecated)* | NUMERIC (18,0) |  |
| COST | VARCHAR (255) | The cost of this medication. |
| DEA_CLASS_CODE_C | INTEGER |  |
| DEA_CLASS_CODE_NAM | VARCHAR (255) |  |
| CONTROLLED_NAME | VARCHAR (255) |  |
| STRENGTH | VARCHAR (255) | The strength of the NDC version of this medication. |
| FORM_C | INTEGER |  |
| ADMIN_ROUTE_C | INTEGER |  |
| RX_TEMPLT_TYP_NAME | VARCHAR (255) |  |
| NDC_INACTIVATED_DT *(deprecated)* | DATETIME | The date the vendor listed this medication as inactive.  This item is no longer used. |
| MDDB_RECORD_KEY *(deprecated)* | VARCHAR (192) | In table RX_MED_TWO, the column MDDB_RECORD_KEY (ERX 510) has been deprecated. The deprecated column's content/data is no longer available since it is no longer populated in Chronicles. |
| DPC_DRG_DRG_INTRCT *(deprecated)* | VARCHAR (255) | In table RX_MED_TWO, the column DPC_DRG_DRG_INTRCT (ERX 520) has been deprecated. The deprecated column's content/data is no longer available since it is no longer populated in Chronicles. |
| APC_ALLERGY_CHECK *(deprecated)* | VARCHAR (255) | In table RX_MED_TWO, the column APC_ALLERGY_CHECK (ERX 530) has been deprecated. The deprecated column's content/data is no longer available since it is no longer populated in Chronicles. |
| PPC_PAT_CONS_MSG *(deprecated)* | VARCHAR (255) | In table RX_MED_TWO, the column PPC_PAT_CONS_MSG (ERX 540) has been deprecated. The deprecated column's content/data is no longer available since it is no longer populated in Chronicles. |
| PANEL_NAME | VARCHAR (255) |  |
| PNL_SUP_ALT_CHK_NM | VARCHAR (255) |  |
| ORDER_DISPLAY_NAME | VARCHAR (255) | The default display name that will be used for this medication in the preference list display in order entry. |
| DISCRETE_DOSE | VARCHAR (91) | The default dose for this medication. |
| DISCRETE_STR_UNITS | VARCHAR (255) | The discrete strength units of this medication. |
| DEFAULT_FREQ_ID | VARCHAR (18) | The default frequency for this medication. |
| SHORT_NAME | VARCHAR (192) | The short name for this medication. |
| MODIFIED_NAME | VARCHAR (255) | The name used as part of the display name hierarchy for medication names in gui system. |
| FILTER_TYPE_C | INTEGER |  |
| USE_ALTER_NAME | VARCHAR (255) |  |
| RX_NAME_ORDER_ID | NUMERIC (18,0) | The ID of the programming point that gets the order name at ordering time. |
| FILE_RX_NAME_PP_ID | NUMERIC (18,0) | The ID of the programming point that gets the order name at order filing time. |
| RX_NAME_VERIFY_ID *(deprecated)* | NUMERIC (18,0) | *** Deprecated *** In table RX_MED_TWO, the column RX_NAME_VERIFY_ID (ERX 3010) has been deprecated.  The deprecated column's content/data is no longer available since it is no longer populated in Chronicles.  The ID of the programming point that gets the order name at order verification time. |
| RX_NAME_REPORT_ID | NUMERIC (18,0) | The ID of the programming point that gets the order name at order MAR and report time. |
| INCLUDE_STRNGTH_YN | VARCHAR (1) |  |
| PX_GROUPER_ID | NUMERIC (18,0) | The procedure code ID for the medications grouper procedure. |
| CART_GROUP_C | INTEGER |  |
| MED_UNIT_C | INTEGER |  |
| MED_RND_FACTOR | NUMERIC (14,4) | The medication rounding factor. |
| MED_RND_METHOD_NM | VARCHAR (255) |  |
| DISPENSE_UNIT_C | INTEGER |  |
| DISP_RND_FACTOR | NUMERIC (14,4) | The dispense rounding factor. |
| DISP_RND_METHOD_NM | VARCHAR (255) |  |
| ADMIN_UNIT_C | INTEGER |  |
| ADMIN_RND_FACTOR | NUMERIC (14,4) | The administration rounding factor. |
| ADMIN_RND_METH_NM | VARCHAR (255) |  |
| CM_PHY_OWNER_ID | VARCHAR (25) | ID of the physical deployment owner for this record.  Physical owners will be where the data is hosted, either on the cross-over server or the owner deployment. |
| CM_LOG_OWNER_ID | VARCHAR (25) | ID of the logical deployment owner for this record.  Logical owners show the deployment where the record was created but doesn't represent if the record is a part of version skew. |
| RX_MAIN_CUSTAMT_YN | VARCHAR (1) |  |
| PADDED_DOSE | VARCHAR (254) | Stores the dose strength of the medication padded with leading spaces so that medications of the same short name will sort alphabetically from lowest to highest dose. |
| IMS_PP_ID *(deprecated)* | NUMERIC (18,0) | This column is deprecated and does not extract any data. There is no replacement column. This PP refers to the logic that should be used for Intelligent Medication Selection for this drug. |
| IMS_ENABLED_YN *(deprecated)* | VARCHAR (1) |  |
| STRENGTH_UNIT_C | INTEGER |  |
| SPECIAL_MED_TYPE_C | INTEGER |  |
| OP_DEFAULT_FREQ_ID | VARCHAR (18) | Outpatient default frequency.  Only used if discrete sigs is enabled. |
| OP_ADMIN_INST_ID | VARCHAR (18) | Outpatient SmartText instructions.  Only used if discrete sigs is enabled. |
| OP_SHORT_INST | VARCHAR (254) | Outpatient short instructions.  Only used if discrete sigs is enabled. |
| OP_ORDER_HELP_ID | VARCHAR (18) | Outpatient SmartText order help. Only used if discrete sigs is enabled. |
| OP_SHORT_ORDER_HEL | VARCHAR (254) | Outpatient short order help.  Only used if discrete sigs is enabled. |
| AMB_NAME_ORD_PP_ID | NUMERIC (18,0) | The during Order Entry programming point that is used to construct the ambulatory medication order display name. |
| AMB_AFTORD_PP_ID | NUMERIC (18,0) | The after ordering programming point that is used to construct the ambulatory medication order display name. |
| AMB_INCLU_STR_YN | VARCHAR (1) |  |
| AMB_NAME_MIXSTR_YN | VARCHAR (1) |  |
| AMB_INCLU_FORM_YN | VARCHAR (1) |  |
| AMB_NAME_SUFFIX | VARCHAR (254) | The text that can be appended to the ambulatory medication order display name. |
| DEFAULT_LONG_TER_YN | VARCHAR (1) |  |
| CALC_RATE_FRM_VD_YN | VARCHAR (1) |  |
| AMB_DFLT_WEIGHT_C | INTEGER |  |
| DEFAULT_WEIGHT_C | INTEGER |  |
| CA_FED_REG_CD_C | INTEGER |  |
| BLANK_DOSE_SCAN_YN | VARCHAR (1) |  |
| IP_MAR_FLO_EXPIRY | INTEGER | Number of minutes for which flowsheet data is valid. |
| STD_DOSE_DEVIATION | NUMERIC (10,4) | This is the maximum percentage by which an ordered dose can differ from the standard dose it will be changed to. If the ordered dose differs from the closest standard dose by more than this amount it will not be changed to a standard dose.  For example, if this is set to 50 percent, and a dose of 100 mg is ordered, it could be rounded to a standard dose of 60 mg or 150 mg, but not to a standard dose of 40 mg or 160 mg.  If this is left blank, the percent specified in system definitions (Medication, Allergy, Imm, etc. > Dosing, Rate Calculation > Dosing Calculations 2) will be used.  If the field in system definitions is also left blank, all ordered doses will be rounded to the closest standard doses, regardless of percent deviation.  If 0 is entered in this field, no attempt to standardize the dose will be made if the ordered dose falls outside of a range.  NOTE: If an ordered dose falls within a set of bounds it will be changed to the standard dose or to reflect the rounding factor regardless of deviation percentage. |
| PROTECT_DEL_YN | VARCHAR (1) |  |
| MATCH_ACROSS_CON_YN | VARCHAR (1) |  |
| RX_SETTINGS_MED_ID | NUMERIC (18,0) | This item points to an ERX record to use for various configuration settings. |
| PROXY_MED_FOR_DC_ID | NUMERIC (18,0) | The medication linked here will be used as a proxy med for dose checking. |
| RX_TPN_OVERFILL_AMT | NUMERIC (18,2) | Stores the amount in mLs for pharmacy-added overfill. This item does not account for manufacturer-added overfill. |
| OP_IMS_PREF_PROD_ID | NUMERIC (18,0) | Indicates the medication strength to try to use in Intelligent Medication Selection for outpatient prescriptions. |
| AMB_MAX_DOSE | NUMERIC (18,4) | The maximum dose for outpatient orders. |
| AMB_MAX_DOSE_UNIT_C | INTEGER |  |
| AMB_MIN_DOSE | NUMERIC (18,4) | The minimum dose for outpatient orders. |
| AMB_MIN_DOSE_UNIT_C | INTEGER |  |
| AMB_ALL_OVR_DOSE_YN | VARCHAR (1) |  |
| MAX_DOSE | NUMERIC (18,4) | The maximum dose for inpatient orders. |
| MAX_DOSE_UNIT_C | INTEGER |  |
| MIN_DOSE | NUMERIC (18,4) | The minimum dose for inpatient orders. |
| MIN_DOSE_UNIT_C | INTEGER |  |
| ALLOW_OR_DOSE_LI_YN | VARCHAR (1) |  |
| HIDE_FRM_OP_IMS_YN | VARCHAR (1) |  |
| COMP_AND_RPKG_C | INTEGER |  |
| RX_INCFAT_DEXCON_YN *(deprecated)* | VARCHAR (1) |  |
| RECIPE_SMART_TXT_ID | VARCHAR (18) | The SmartText (ETX) ID that contains the recipe information to be used when building the compound or repackaging the medication. |
| RECIPE_ETX_LABEL_ID | VARCHAR (18) | Stores a link to the SmartText record containing the label to be printed from the Compounding and Repackaging Activity. |
| RECIPE_PKG_INFO_ID *(deprecated)* | VARCHAR (18) | This column is deprecated. This was single response but needed to be related group. This can now be found in the ERX_CNR_NDC_INFO table.  The NDC record which contains package information for this compounding or repackaging record. The data is stored in the NDC as follows:   Item 510 Package Size: The base amount for the recipe  Item 515 Units of Measure: The units for the base amount   Item 530 Package Description: The package   Among valid NDC formats are the following:              9999-9999-99              99999-999-99              99999-9999-9 |
| SHELF_LIFE | INTEGER | The shelf life in days. This column stores the maximum expiration date of any compounded or repackaged medications built using this Drug Compounding Record. Expiration date will be determined by using this number of days from the date created or the earliest expiring ingredient, whichever comes sooner. |
| MAR_OFFSCHED_MINS | INTEGER | From the MAR, administrations documented against a due time and more than this number of minutes away from the due time will cause the off schedule alert to be displayed.  If null, the system will behave as before and the off schedule alert will not display if the user is documenting against due time even if the user changes the documented time. |
| LAST_RESORT_DISP_ID | NUMERIC (18,0) | Identifies which dispensable medication is the choice of last resort in orderable to dispensable mapping records. |
| AMB_INC_SG_NAME_YN | VARCHAR (1) |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | MEDICATION_ID | CLARITY_MEDICATION | MEDICATION_ID | Unknown | No | No |  |
| 1 | MEDICATION_ID | MED_ADS_INFO | MEDICATION_ID | No | No | No |  |
| 1 | MEDICATION_ID | RX_MED_FIVE | MEDICATION_ID | No | No | No |  |
| 1 | MEDICATION_ID | RX_MED_FOUR | MEDICATION_ID | No | No | No |  |
| 1 | MEDICATION_ID | RX_MED_ONE | MEDICATION_ID | No | No | No |  |
| 1 | MEDICATION_ID | RX_MED_THREE | MEDICATION_ID | No | No | No |  |
| 1 | MEDICATION_ID | V_CUBE_D_MEDICATION | MEDICATION_ID | Unknown | Unknown | No |  |
| 5 | PROPTRY_STATUS_C | ZC_PROPTRY_STATUS | PROPTRY_STATUS_C | No | No | No |  |
| 6 | BRAND_NAME_CODE_C | ZC_BRAND_NAME_CODE | BRAND_NAME_CODE_C | No | No | No |  |
| 7 | NAME_SOURCE_C | ZC_NAME_SRC_CODE | NAME_SOURCE_C | No | No | No |  |
| 10 | PHARM_SUBCLASS_C | ZC_PHARM_SUBCLASS | PHARM_SUBCLASS_C | No | No | No |  |
| 13 | DEA_CLASS_CODE_C | ZC_DEA_CLASS_CODE | DEA_CLASS_CODE_C | No | No | No |  |
| 17 | FORM_C | ZC_FORM | FORM_C | No | No | No |  |
| 18 | ADMIN_ROUTE_C | ZC_ADMIN_ROUTE | MED_ROUTE_C | No | No | No |  |
| 18 | ADMIN_ROUTE_C | ZC_DISPENSE_ROUTE | DISPENSE_ROUTE_C | No | No | No |  |
| 30 | DEFAULT_FREQ_ID | FREQ_INCL_OR_EXCL_DEPS | FREQ_ID | No | No | No |  |
| 30 | DEFAULT_FREQ_ID | FREQ_INCL_OR_EXCL_FACS | FREQ_ID | No | No | No |  |
| 30 | DEFAULT_FREQ_ID | FREQ_INCL_OR_EXCL_LEDS | FREQ_ID | No | No | No |  |
| 30 | DEFAULT_FREQ_ID | IP_FREQUENCY | FREQ_ID | No | No | No |  |
| 33 | FILTER_TYPE_C | ZC_FILTER_TYPE | FILTER_TYPE_C | No | No | No |  |
| 35 | RX_NAME_ORDER_ID | CLARITY_LPP | LPP_ID | Unknown | No | No |  |
| 36 | FILE_RX_NAME_PP_ID | CLARITY_LPP | LPP_ID | Unknown | No | No |  |
| 38 | RX_NAME_REPORT_ID | CLARITY_LPP | LPP_ID | Unknown | No | No |  |
| 40 | PX_GROUPER_ID | CLARITY_EAP | PROC_ID | No | No | No |  |
| 40 | PX_GROUPER_ID | CLARITY_EAP_2 | PROC_ID | No | No | No |  |
| 40 | PX_GROUPER_ID | CLARITY_EAP_3 | PROC_ID | No | No | No |  |
| 40 | PX_GROUPER_ID | CLARITY_EAP_4 | PROC_ID | No | No | No |  |
| 40 | PX_GROUPER_ID | CLARITY_EAP_5 | PROC_ID | No | No | No |  |
| 40 | PX_GROUPER_ID | CLARITY_EAP_IMM | PROC_ID | Unknown | No | No |  |
| 40 | PX_GROUPER_ID | PROC_CONSENT_CONFIG | PROC_ID | No | No | No |  |

_(94 total; showing first 30)_
