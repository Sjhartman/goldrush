# RX_NDC

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=RX_NDC

## Description

This table contains the National Drug Code (NDC) information.

**Primary table** in this group (101 cols). Overflow siblings joined on shared key: RX_NDC_2 (6 cols). Prefer this table for most queries.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | NDC |
| Release Version | MU4 - EPIC 2002 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| NDC_ID | VARCHAR (18) | The unique ID for the NDC (National Drug Code) |
| NDC_CODE | VARCHAR (255) | The external code for the National Drug Code (NDC). An NDC represents packages of medications. |
| NDC_FORMAT | INTEGER | The code format is used for the NDC. |
| RAW_11_DIGIT_NDC | VARCHAR (192) | 11-digit Raw NDC, without any format. |
| RAW_NDC_CODE | VARCHAR (40) | Raw NDC Code, it may not be 11-digit |
| MFG_LONG_NAME | VARCHAR (255) | The imported full manufacturer name |
| MFG_ABBR_NAME | VARCHAR (255) | The imported abbreviated manufacturer name |
| MFG_CODE | VARCHAR (255) | Manufacturer's code, the first piece of the NDC code. |
| PACKAGE_SIZE | NUMERIC (12,3) | The total size of the package in volume or number of units |
| MED_UNIT_C | INTEGER |  |
| PACKAGE_QUANTITY | INTEGER | The number of individual containers or units per package |
| PACKAGE_UNITS_NAME | VARCHAR (255) |  |
| PACK_DESC_C | INTEGER |  |
| GPPC_CODE | VARCHAR (255) | This GPPC code is used in the Medispan import |
| MULTI_DOSE_YN | VARCHAR (1) |  |
| KDC | VARCHAR (255) | It is Knowledge Base Drug Code, which Facts & Comparisons (Medi-span) assigns  to a drug product (by NDC) to indicate the interactions (both drug-drug and drug-allergy) known to that product. |
| KDC_FLAG_NAME | VARCHAR (255) |  |
| COST_ID_VAL | VARCHAR (255) | All NDCs which have the same Cost ID can have the same unit cost for billing. |
| IMP_EXT_UNIT_NAME | VARCHAR (255) |  |
| IP_DEF_COST | NUMERIC (13,3) | It is inpatient default cost used in charge calculation. |
| IP_DEF_COST_PU_YN | VARCHAR (1) |  |
| COST_LOCKED_YN | VARCHAR (1) |  |
| COST_UPDATE_TIME | DATETIME (Local) | The last updated instant. |
| IP_DEF_BILL_PU_YN | VARCHAR (1) |  |
| IP_DEF_RND_FACTOR | NUMERIC (18,3) | The next increment to round up to for billing purposes. |
| IP_DEF_CHM_TBL_ID | VARCHAR (18) | The charge method table to use when calculating a charge for this medication. |
| IP_WHEN_TO_CHG | VARCHAR (255) |  |
| CHARGE_METHOD_C | VARCHAR (66) |  |
| RX_PACKAGE_SUFFIX | VARCHAR (255) | The package order name suffix |
| SIMPLE_GENERIC_C | VARCHAR (66) |  |
| GCN_SEQNO | VARCHAR (254) | The Generic Code Number Sequence Number for this medication record. |
| INST_LAST_IMPORT | DATETIME (Local) | The instant that data was last imported. |
| CM_PHY_OWNER_ID | VARCHAR (25) | ID of the physical deployment owner for this record.  Physical owners will be where the data is hosted, either on the cross-over server or the owner deployment. |
| CM_LOG_OWNER_ID | VARCHAR (25) | ID of the logical deployment owner for this record.  Logical owners show the deployment where the record was created but doesn't represent if the record is a part of version skew. |
| PROTECT_PKGINFO_YN | VARCHAR (1) |  |
| ASSOCIATED_NDG | NUMERIC (18,0) | The NDG record (NDG .1) associated with this NDC. |
| CUSTOM_MODIFER *(deprecated)* | VARCHAR (255) |  |
| FDB_INACTREVIEW_YN | VARCHAR (1) |  |
| DFT_BILL_CODE | VARCHAR (254) | This is used to capture the billing code associated with this medication (e.g. J-Code). |
| QTY_PER_BILL_CODE | NUMERIC (12,3) | The number entered here will be the number of Billing Codes that are equal to one unit of the unit type entered in the "Units" field.  If  the "Units" field is blank, the Dispense Units will be used along with  this field. |
| BILL_CODE_UNITS_C | INTEGER |  |
| BILL_CODE_RND_FACT | NUMERIC (12,3) | Determines the rounding factor to use when calculating the number of  billing codes to charge for.  The amount will be rounded up to the next   interval of this rounding factor.  If this item is blank, a rounding  factor of 1 will be used. |
| BILLABLE_NDC_ID | VARCHAR (18) | The unique ID of the NDC record that will be sent to billing instead of the parent record. |
| LEGEND_INDICATOR_C | INTEGER |  |
| INNOVATOR_IND_YN | VARCHAR (1) |  |
| REPLACEMENT_NDC_ID | VARCHAR (18) | This column stores the ID of the NDC that is going to replace the current NDC. |
| IP_CHARGE_ADMIN_YN | VARCHAR (1) |  |
| FDB_IVM_COMP_CODE | VARCHAR (254) | This column stores the component code for the medication that is used in First Databank IV Compatibility checking. |
| RECORD_STATUS_C | INTEGER |  |
| BACK_COMP_MED_ID | NUMERIC (18,0) | If the medication vendor moves a NDC record from one ERX to another, this item can hold the medication that the NDC was associated with before the load occurred. This is used in some workflows so that the NDC can still be used to locate records based on the old NDC-ERX link (for example, finding orders for barcoded med admin.) |
| CUSTOM_MODIFIER_C | INTEGER |  |
| WASTAGE_ALLOWED_C | INTEGER |  |
| MULT_PAT_DOSE_YN | VARCHAR (1) |  |
| AGENT_DESC | VARCHAR (100) | This item stores the agent description for the package. The information is currently only provided by First Databank for the UAE. |
| AGENT_CODE | VARCHAR (30) | This stores the agent identifier for the package. This information is currently only provided by First Databank for the UAE. |
| COST_UPDATE_USER_ID | VARCHAR (18) | The unique ID of the user who updated the default cost for this NDC most  recently. |
| COST_UPD_SOURCE_C | VARCHAR (66) |  |
| COST_UPDATE_MARKUP | NUMERIC (18,1) | The markup percentage that was applied to the price in the Set NDC Costs activity, if applicable. |
| PRICE_FROM_OUT_NDC | VARCHAR (192) | This contains the outer NDC from which the price was copied into this inner NDC. This is populated only for customers with FDB US data. |
| AMINO_ACID_TYPE_C | INTEGER |  |
| MEDGUIDE_REQ_YN | VARCHAR (1) |  |
| MEDGUIDE_AVAIL_YN | VARCHAR (1) |  |
| KDC_FLAG_C | INTEGER |  |
| PACKAGE_UNITS_C | INTEGER |  |
| IMP_EXT_UNIT_C | INTEGER |  |
| IP_WHEN_TO_CHARGE_C | INTEGER |  |
| RX_LBL_PRT_RL_TYP_C | INTEGER |  |
| RX_NUM_PKGS_PER_LBL | NUMERIC (18,3) | If the label print quantity rule type is set to print one label per a given number of packages, this value determines the number of packages per label, which will be honored when calculating the number of fill labels to print for a fill. |
| REIMBURSEMENT_CODE_C | INTEGER |  |
| REIMBURSEMENT_CLAUSE_C | INTEGER |  |
| CAN_MATCH_EXT_YN | VARCHAR (1) |  |
| PRODUCT_TYPE_C | INTEGER |  |
| PACKAGE_UNIT_CODE | VARCHAR (10) | Code for the unit in which the package is dispensed to the patient. |
| REUSED_NDC_YN | VARCHAR (1) |  |
| PRIVATE_LABEL_YN | VARCHAR (1) |  |
| REPACKAGED_YN | VARCHAR (1) |  |
| FI_PKG_DATA_SRC_C | INTEGER |  |
| PRESCRIBING_CONDITION_CODE | VARCHAR (20) | This contains the prescribing condition code for the package. It is currently only populated for packages that are used in Finland. |
| PRESCRIBING_CONDITION_TEXT | VARCHAR (1000) | This contains the prescribing condition text for the package. It is currently only populated for packages that are used in Finland. |
| PACKAGE_SIZE_TEXT | VARCHAR (80) | This contains the free text package size information for the package. It is currently only populated for packages that are used in Finland. |
| INVENTORY_NDC_ID | VARCHAR (18) | This item contains the NDC in which inventory is tracked for this NDC. If set, inventory updates for this NDC will be made on the NDC stored in this item instead. |
| PACKAGE_UNIT_TEXT | VARCHAR (80) | This contains the free text package unit for the package. It is currently only populated for packages that are used in Finland. |
| SWISSMEDIC_CODE | VARCHAR (30) | The Swissmedic assortment code is a value assigned to a packaged product in Switzerland. It indicates the type of product. This value is set during the medication load when using HCI as the medication data vendor. |
| MAIN_PKG_NUM_YN | VARCHAR (1) |  |
| BE_PKG_DATA_SRC_C | INTEGER |  |
| DISPENSING_CODE | VARCHAR (20) | This contains the dispensing code for the package and is used to determine if the package can be prescribed with refills. It is currently only populated for packages that are used in Denmark. |
| SPECIFIC_GRAVITY | NUMERIC (18,4) | The specific gravity of the medication. Used to verify the amount of medication by weight.  If set for the package, this overrides the value at the medication level. |
| REIMBURSABLE_YN | VARCHAR (1) |  |
| BE_SAM_ID_KEY_CNK | VARCHAR (100) | This contains the Belgium SAM identifier version key for a CNK code. |
| INNER_PACKAGE_YN | VARCHAR (1) |  |
| SAMPLE_PACKAGE_YN | VARCHAR (1) |  |
| NORWAY_EXT_CON_TYPE_C | INTEGER |  |
| NOMA_APPLICATION_TYPE_C | INTEGER |  |
| BLACK_TRIANGLE_IND_C | INTEGER |  |
| FEST_PREPARATION_TYPE_C | INTEGER |  |
| SUBSTITUTION_GROUP_CODE | VARCHAR (50) | This contains the substitution group code associated with the package. |
| SUBSTITUTION_GROUP_CODE_DESC | VARCHAR (500) | This contains the description for the substitution group code. |
| SUBTITUTION_GROUP_REMARKS | VARCHAR (500) | This contains additional information regarding when the substitution can be done. |
| SUBSTITUTION_GROUP_FROM_DATE | DATETIME | This contains the start date when the substitution group is valid. |
| SUBSTITUTION_GROUP_TO_DATE | DATETIME | This contains the end date when the substitution group is valid. |
| NDC_GPI_CODE | VARCHAR (192) | This is the GPI associated with the NDC. |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | NDC_ID | RX_NDC_2 | NDC_ID | No | No | No |  |
| 1 | NDC_ID | RX_NDC_ADS_INFO | NDC_ID | No | No | No |  |
| 10 | MED_UNIT_C | ZC_MED_UNIT | DISP_QTYUNIT_C | No | No | No |  |
| 13 | PACK_DESC_C | ZC_PACK_DESC | PACK_DESC_C | No | No | No |  |
| 26 | IP_DEF_CHM_TBL_ID | RX_CHM | CHM_ID | Unknown | No | No |  |
| 28 | CHARGE_METHOD_C | ZC_CHARGE_METHOD | CHARGE_METHOD_C | No | No | No |  |
| 30 | SIMPLE_GENERIC_C | ZC_SIMPLE_GENERIC | SIMPLE_GENERIC_C | No | No | No |  |
| 33 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 33 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 33 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 34 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 34 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 34 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 36 | ASSOCIATED_NDG | RX_NDG | NDG_ID | Unknown | No | No |  |
| 36 | ASSOCIATED_NDG | RX_NDG_ADS_INFO | NDG_ID | Unknown | No | No |  |
| 41 | BILL_CODE_UNITS_C | ZC_MED_UNIT | DISP_QTYUNIT_C | No | No | No |  |
| 43 | BILLABLE_NDC_ID | RX_NDC | NDC_ID | No | No | No |  |
| 43 | BILLABLE_NDC_ID | RX_NDC_2 | NDC_ID | No | No | No |  |
| 43 | BILLABLE_NDC_ID | RX_NDC_ADS_INFO | NDC_ID | No | No | No |  |
| 44 | LEGEND_INDICATOR_C | ZC_LEGEND_INDCATOR | LEGEND_INDICATOR_C | No | No | No |  |
| 46 | REPLACEMENT_NDC_ID | RX_NDC | NDC_ID | No | No | No |  |
| 46 | REPLACEMENT_NDC_ID | RX_NDC_2 | NDC_ID | No | No | No |  |
| 46 | REPLACEMENT_NDC_ID | RX_NDC_ADS_INFO | NDC_ID | No | No | No |  |
| 49 | RECORD_STATUS_C | ZC_DEL_STATUS | DEL_STATUS_C | No | No | No |  |
| 49 | RECORD_STATUS_C | ZC_EDG_REC_STAT | EDG_REC_STAT_C | No | No | No |  |
| 49 | RECORD_STATUS_C | ZC_ERS_REC_STAT | RECORD_STATUS_C | No | No | No |  |
| 49 | RECORD_STATUS_C | ZC_HCD_REC_STATE | HCD_REC_STATE_C | No | No | No |  |
| 49 | RECORD_STATUS_C | ZC_HFL_RECORD_STAT | HFL_RECORD_STAT_C | No | No | No |  |
| 49 | RECORD_STATUS_C | ZC_IMM_REC_STATUS | IMM_REC_STATUS_C | No | No | No |  |
| 49 | RECORD_STATUS_C | ZC_LLB_STATUS | LLB_STATUS_C | No | No | No |  |

_(88 total; showing first 30)_
