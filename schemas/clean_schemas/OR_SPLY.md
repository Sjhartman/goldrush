# OR_SPLY

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=OR_SPLY

## Description

The OR_SPLY table contains inventory item records.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | SUP |
| Release Version | MU1 - MAY 2001 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| SUPPLY_ID | VARCHAR (18) | The internal ID of the inventory item. |
| SUPPLY_NAME | VARCHAR (254) | The name of the inventory item. |
| ACTIVE_YN | VARCHAR (1) |  |
| ABBR | VARCHAR (254) | The abbreviation of the inventory item. |
| CHARGE_CODE *(deprecated)* | VARCHAR (254) | This column is deprecated and does not extract any new data. It has been replaced with a more appropriate data structure. Use OR_SPLY_OVTM.CHARGE_CODE_FT_OT instead. |
| CHARGE_PER_UNIT *(deprecated)* | NUMERIC (12,2) | This column is deprecated and does not extract any new data. It has been replaced with a more appropriate data structure. Use OR_SPLY_OVTM.OVERRIDE_CHARGE_OT  instead. |
| COST_PER_UNIT *(deprecated)* | NUMERIC (12,2) | This column is deprecated and does not extract any new data. It has been replaced with a more appropriate data structure. Use OR_SPLY_OVTM.COST_PER_UNIT_OT instead. |
| NAME *(deprecated)* | VARCHAR (30) |  |
| TEMP_RECORD_YN | VARCHAR (1) |  |
| TYPE_OF_ITEM_C | VARCHAR (66) |  |
| REUSABLE_YN | VARCHAR (1) |  |
| PACK_YN | VARCHAR (1) |  |
| STOCK_ITEM_C | VARCHAR (66) |  |
| LEAD_TIME_DAYS | INTEGER | The number of days it takes to get the supply/drug from the supplier. |
| LAST_SUPPLIER_C | VARCHAR (66) |  |
| LAST_SUPPLIER_NUM | VARCHAR (192) | The catalog number associated with the most recent supplier. |
| LAST_PURCHS_PRICE | NUMERIC (12,2) | The most recent price paid for the item. |
| REC_CREATE_DATE | DATETIME | The date that the supply/drug record was created. |
| REC_CREATE_USER_ID | VARCHAR (18) | The internal ID of the user who created the supply/drug record. |
| PRIMARY_EXT_ID | VARCHAR (254) | The primary external ID for this supply/drug. |
| ITEM_DESC *(deprecated)* | VARCHAR (254) | This columm is being deprecated in this table. Please use the table OR_SPLY_DESC for free text item desciptions related to the supply or drug. |
| COMMENTS *(deprecated)* | VARCHAR (254) | This columm is being deprecated in this table. Please use the table OR_SPLY_COMMENTS for free text item desciptions related to the supply or drug. |
| SMDA_ITEM_YN | VARCHAR (1) |  |
| IMAGE_FILE | VARCHAR (254) | The file name of the image associated with the supply/drug. |
| CHARGEABLE_YN *(deprecated)* | VARCHAR (1) |  |
| LATEX_PRODUCT_YN | VARCHAR (1) |  |
| PASS_THROUGH_CODE | VARCHAR (254) | The pass through code used for billing. |
| IMPLANT_TYPE_C | VARCHAR (66) |  |
| ONLY_IN_PACK_YN | VARCHAR (1) |  |
| CONSIGNMENT_ITM_YN | VARCHAR (1) |  |
| CHARGE_CODE_EAP_ID *(deprecated)* | NUMERIC (18,0) | This column is deprecated and does not extract any new data. It has been replaced with a more appropriate data structure. Use OR_SPLY_OVTM.CHRG_COD_EAP_OT_ID instead. |
| MARKUP_PERCENTAGE *(deprecated)* | NUMERIC (12,2) | This column is deprecated and does not extract any new data. It has been replaced with a more appropriate data structure. Use OR_SPLY_OVTM.OVRIDE_MKUP_PCT_OT instead. |
| CM_PHY_OWNER_ID | VARCHAR (25) | ID of the physical deployment owner for this record.  Physical owners will be where the data is hosted, either on the cross-over server or the owner deployment. |
| CM_LOG_OWNER_ID | VARCHAR (25) | ID of the logical deployment owner for this record.  Logical owners show the deployment where the record was created but do not represent if the record is a part of version skew. |
| ORDERING_RATIO | NUMERIC (18,2) | Contains the ordering ratio for the supply/drug. |
| ORDER_PACK_TYPE_C | VARCHAR (66) |  |
| SURGERY_ID | VARCHAR (18) | The case/log ID to which this temporary supply is linked. |
| BILLING_NAME | VARCHAR (254) | The billing name for the supply record. |
| SUPPLY_OR_DRUG_C | INTEGER |  |
| LDA_TYPE_ID | VARCHAR (18) | The type of line/drain/airway that the supply is assigned to. |
| TAXABLE_YN | VARCHAR (1) |  |
| TRACKED_EXTERNAL_YN | VARCHAR (1) |  |
| IMPLANT_CLASS_GROUPER_C | INTEGER |  |
| IS_ACTIVE_MM_C | INTEGER |  |
| CLIN_IND_LQL_ID | VARCHAR (18) | Stores the order-specific question (LQL ID) that will store the clinical indcation for this implant. |
| RECORD_STATUS_C | INTEGER |  |
| IS_ELIGIBLE_HC_EXPENSE_YN | VARCHAR (1) |  |
| IS_ELIGIBLE_HC_EXPNSE_SIGIS_YN | VARCHAR (1) |  |
| NDC_ID | VARCHAR (18) | A linkage to the NDC record for this product, if it is a medication. |
| SUPPLY_CONTRACT_STATUS_C | INTEGER | Surrogate key used to uniquely identify rows in this (and only this) table on Cogito Cloud only, do not assume the surrogate key in this table will correspond to the surrogate key in another table |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| B-TREE INDEX | EIX_OR_SPLY_ACYN | ACTIVE_YN | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_OR_SPLY_CHYN | CHARGEABLE_YN | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_OR_SPLY_PAYN | PACK_YN | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_OR_SPLY_PREXID | PRIMARY_EXT_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_OR_SPLY_RECRUSID | REC_CREATE_USER_ID | 1 | Yes | Yes |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | SUPPLY_ID | V_CUBE_D_SUPPLY | SUPPLY_ID | Unknown | Unknown | No |  |
| 10 | TYPE_OF_ITEM_C | ZC_OR_TYPE_OF_ITEM | TYPE_OF_ITEM_C | No | No | No |  |
| 13 | STOCK_ITEM_C | ZC_OR_STOCK_ITEM | STOCK_ITEM_C | No | No | No |  |
| 15 | LAST_SUPPLIER_C | ZC_OR_SUPPLIER | SUPPLIER_C | No | No | No |  |
| 19 | REC_CREATE_USER_ID | CLARITY_EMP | USER_ID | Unknown | No | No |  |
| 19 | REC_CREATE_USER_ID | CLARITY_EMP_2 | USER_ID | Unknown | No | No |  |
| 19 | REC_CREATE_USER_ID | CLARITY_EMP_3 | USER_ID | Unknown | No | No |  |
| 19 | REC_CREATE_USER_ID | CLARITY_EMP_4 | USER_ID | No | No | No |  |
| 19 | REC_CREATE_USER_ID | CLARITY_EMP_DEMO | USER_ID | No | No | No |  |
| 19 | REC_CREATE_USER_ID | EMP_BASIC_INFO | USER_ID | No | No | No |  |
| 19 | REC_CREATE_USER_ID | EMP_DOC_SETTINGS | USER_NUMBER_ID | No | No | No |  |
| 19 | REC_CREATE_USER_ID | F_RX_USER | USER_ID | Unknown | Unknown | No |  |
| 19 | REC_CREATE_USER_ID | IB_MESSAGE_SETTINGS | USER_ID | No | No | No |  |
| 19 | REC_CREATE_USER_ID | LOGIN_INFO | USER_NUMBER_ID | No | No | No |  |
| 19 | REC_CREATE_USER_ID | QC_RESULTS_REVIEW | USER_NUMBER_ID | No | No | No |  |
| 19 | REC_CREATE_USER_ID | USER_SIDEBAR_RPT | USER_NUMBER_ID | Unknown | No | No |  |
| 19 | REC_CREATE_USER_ID | V_CUBE_D_USER | USER_ID | Unknown | Unknown | No |  |
| 19 | REC_CREATE_USER_ID | V_CUBE_RX_USER | USER_ID | Unknown | Unknown | No |  |
| 28 | IMPLANT_TYPE_C | ZC_OR_IMPLANT_TYPE | IMPLANT_TYPE_C | No | No | No |  |
| 33 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 33 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 33 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 34 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 34 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 34 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 36 | ORDER_PACK_TYPE_C | ZC_OR_UNIT_ISSUE | UNIT_ISSUE_C | No | No | No |  |
| 37 | SURGERY_ID | OR_CASE | OR_CASE_ID | Unknown | No | No |  |
| 37 | SURGERY_ID | OR_CASE_2 | CASE_ID | Unknown | No | No |  |
| 37 | SURGERY_ID | OR_CASE_3 | CASE_ID | Unknown | No | No |  |
| 37 | SURGERY_ID | OR_CASE_4 | OR_CASE_ID | No | No | No |  |

_(65 total; showing first 30)_
