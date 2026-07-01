# OR_IMP

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=OR_IMP

## Description

The OR_IMP table contains implant information.

**Primary table** in this group (101 cols). Overflow siblings joined on shared key: OR_IMP_2 (101 cols), OR_IMP_3 (40 cols). Prefer this table for most queries.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | IMP |
| Release Version | MU6 - MAY 2001 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| IMPLANT_ID | VARCHAR (18) | The unique ID of the implant record. |
| IMPLANT_NAME | VARCHAR (254) | The name of the implant record. |
| PO_NUMBER | VARCHAR (254) | The purchase order number of the implant record. |
| ABBREVIATION | VARCHAR (254) | The abbreviation of the implant record. |
| IMPLANT_TYPE_C | VARCHAR (66) |  |
| MANUFACTURER_C | VARCHAR (66) |  |
| STATUS_C | INTEGER |  |
| SMDA_YN | VARCHAR (1) |  |
| ACTIVE_YN | VARCHAR (1) |  |
| VENDOR_DISTRIB_C | VARCHAR (66) |  |
| MODEL_NUMBER | VARCHAR (254) | The model number of the implant. |
| SERIAL_NUMBER | VARCHAR (254) | The serial number of the implant. |
| LOT_NUMBER | VARCHAR (254) | The lot number of the implant. |
| SITE_ID | NUMERIC (18,0) | The unique ID of the location for the implant. |
| COST | NUMERIC (12,2) | The cost of the implant. |
| EXPIRATION_DATE | DATETIME | The expiration date of the implant. |
| RECEIVED_DATE | DATETIME | The date the implant was received. |
| RECPT_NOTIFY_DATE | DATETIME | The date the manufacturer was notified of implant receipt. |
| RETURNED_DATE | DATETIME | The date that the implant was returned. |
| RETURN_NOTIF_DATE | DATETIME | The date the manufacturer was notified of implant return. |
| DESTROYED_DATE | DATETIME | The date the implant was destroyed. |
| DESTROYED_NOT_DAT | DATETIME | The date the manufacturer was notified of implant destruction. |
| RECALLED_DATE | DATETIME | The date the implant was recalled. |
| RECALLED_NOT_DATE | DATETIME | The date the manufacturer was notified of implant recall. |
| PAT_EXPIRY_DATE | DATETIME | The date the patient with the implant expired. |
| PAT_EXP_NOTIF_DATE | DATETIME | The date the manufacturer was notified of the patient's expiration. |
| MULTIPLE_USE_YN *(deprecated)* | VARCHAR (1) |  |
| LABELS_PRNTED_YN | VARCHAR (1) |  |
| INVENTORY_ITEM_ID | VARCHAR (18) | The unique ID of the supply linked to the implant record. |
| CHARGE_CODE | VARCHAR (254) | The charge code that corresponds to the implant. |
| CHARGE_PER_UNIT | NUMERIC (12,2) | The charge per unit of the implant. |
| PACEMAKER_RATE | NUMERIC (12,2) | The pacemaker rate of the implant. |
| IMPLANT_AREA_C | INTEGER |  |
| COST_PER_UNIT | NUMERIC (12,2) | The cost per unit of the implant. |
| PASS_THROUGH_CODE | VARCHAR (254) | The pass through code used for billing. |
| CHARGE_CODE_EAP_ID | NUMERIC (18,0) | The unique ID of the charge code associated with the implant record. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this Chronicles record. This is populated only if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this Chronicles record was extracted. This is populated only if you use IntraConnect. |
| IMPLANT_SIZE | VARCHAR (254) | The size of the implant. |
| PREALLOC_REC_TYPE_C | INTEGER |  |
| TISSUE_TYPE_C | INTEGER |  |
| PREP_START_DTTM | DATETIME (Attached) | The date and time when the tissue preparation was started. |
| PREP_END_DTTM | DATETIME (Attached) | The date and time when the tissue preparation was ended. |
| PREP_STAFF_ID | VARCHAR (18) | The unique ID of the staff who prepared the tissue. This column is frequently used to link to the CLARITY_SER table. |
| PREP_SOLN_LOTNUM *(deprecated)* | VARCHAR (192) |  |
| IMPLANT_TEMP | NUMERIC (18,2) | Temperature at implantation of tissue, in degrees Fahrenheit. |
| TISSUE_ICE_C | INTEGER |  |
| TISSUE_RECV_DTTM | DATETIME (Attached) | The date and time the tissue was received. |
| IMP_RECV_STAFF_ID | VARCHAR (18) | The unique ID of the user who receives the tissue. This column is frequently used to link to the CLARITY_EMP table. |
| TISSUE_STORAGE_TEMP | NUMERIC (18,2) | Temperature of tissue for storage, in degrees Fahrenheit. |
| TISSUE_DONOR_ID | VARCHAR (192) | The unique ID of the source donor of the tissue. |
| INFECTED_DATE | DATETIME | The date the tissue was infected. |
| SURG_NOTIFIED_DATE | DATETIME | The date the surgeon was notified about the infection. |
| TISSUE_YN | VARCHAR (1) |  |
| MARKUP_PERCENT | NUMERIC (18,2) | The override markup percentage used to calculate a charge per unit for this implant record. |
| CHARGEABLE_YN | VARCHAR (1) |  |
| PREP_SOLN_EXP_DT *(deprecated)* | DATETIME |  |
| PAT_ID | VARCHAR (18) | The unique ID of the patient record for this implant. This column is frequently used to link to the PATIENT table. |
| IMPLANT_LAT_C | INTEGER |  |
| IMP_OUTOFSRVC_DATE | DATETIME | The date the implant was marked out of service. |
| PACE_INITIAL_YN | VARCHAR (1) |  |
| PACE_POCKET_LOC_C | INTEGER |  |
| TEMP_PACE_YN | VARCHAR (1) |  |
| PACE_PREVENTION_C | INTEGER |  |
| TEMP_PACE_CHAMBER_C | INTEGER |  |
| RECORD_STATUS_C | INTEGER |  |
| CLINICAL_TRIAL_YN | VARCHAR (1) |  |
| PACKAGE_INTEGRITY_C | INTEGER |  |
| RET_TO_MANUF_YN | VARCHAR (1) |  |
| MANUF_NUM | VARCHAR (192) | The manufacturer number of the supply linked to the implant record. |
| SUP_CAT_NUM | VARCHAR (192) | The supplier catalog number of the supply linked to the implant record. |
| PREP_INSTR_SOURCE_C | INTEGER |  |
| STATIC_UDI | VARCHAR (192) | The static piece of the unique device identifier, obtained from the implant barcode.  This is the Global Trade Item Number (GTIN) for General Specifications (GS1) barcodes and the combination of the labeler identification code and the catalog number for Health Industry Bar Code (HIBC) barcodes. |
| STATIC_UDI_TYPE_C | INTEGER |  |
| EXTRACT_FLAG_DTTM | DATETIME (UTC) | The timestamp when the implant was last modified. This is used to determine whether the implant should be included in an extract for an external implant tracking system. The value is populated by system and cannot be overwritten by the user manually. |
| TISSUE_AUTOLOGOU_YN | VARCHAR (1) |  |
| EXPLANT_DISPOSITN_C | INTEGER |  |
| SKIN_SUBSTITUTE_YN | VARCHAR (1) |  |
| SKIN_SUB_USAGE_C | INTEGER |  |
| SKIN_SUB_AREA_USED | NUMERIC (18,1) | Document the area of the skin substitute used. |
| SKIN_SUB_AREA_WASTE | NUMERIC (18,1) | Document the area of the skin substitute wasted. |
| TISSUE_STORAG_ENV_C | INTEGER |  |
| TISSUE_STORAG_LOC_C | INTEGER |  |
| TISSUE_INSPC_RSLT_C | INTEGER |  |
| RADIOACTIVE_C | INTEGER |  |
| REPLACE_EXISTING_C | INTEGER |  |
| TISSUE_TRCK_BARCODE | VARCHAR (254) | This unique ID of the barcode used in third party tissue tracking systems. |
| RECD_IN_OR_DTTM | DATETIME (UTC) | This item is used to document the time an implant was received in the OR. |
| TISSUE_BANK_C | INTEGER |  |
| TISSUE_STG_END_DTTM | DATETIME (Attached) | This item is used to document the time a tissue was removed from storage prior to surgery. |
| SKIN_SUB_ORIG_LEN | NUMERIC (18,2) | This item is used to document the original length of the skin substitute. |
| SKIN_SUB_ORIG_WDTH | NUMERIC (18,2) | This item is used to document the original width of the skin substitute. |
| SKIN_SUB_TOTAL_AREA | NUMERIC (18,2) | This item is used to document the total area of the skin substitute. |
| SKIN_SUB_FRCN_USD_C | INTEGER |  |
| TISSUE_EXPANDER_VOLUME | NUMERIC (18,2) | The volume (mL) the tissue expander was inflated. |
| REMOVE_BY_DATE | DATETIME | Date implant needs to be removed from patient. |
| IMPLANT_VOLUME | NUMERIC (18,2) | This documents the volume of the implant. |
| IMP_VOLUME_UNIT_C | INTEGER |  |
| SUPPLY_TYPE_C | VARCHAR (66) |  |
| EXPLANT_WARRANTY_COMPLETION_DT | DATETIME | This item stores the explant warranty completion date. |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| B-TREE INDEX | EIX_OR_IMP_ACYN | ACTIVE_YN | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_OR_IMP_CHCO | CHARGE_CODE | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_OR_IMP_CHCOEAID | CHARGE_CODE_EAP_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_OR_IMP_IMARC | IMPLANT_AREA_C | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_OR_IMP_IMTYC | IMPLANT_TYPE_C | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_OR_IMP_INITID | INVENTORY_ITEM_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_OR_IMP_LAPRYN | LABELS_PRNTED_YN | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_OR_IMP_LONU | LOT_NUMBER | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_OR_IMP_MAC | MANUFACTURER_C | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_OR_IMP_MONU | MODEL_NUMBER | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_OR_IMP_MUUSYN | MULTIPLE_USE_YN | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_OR_IMP_SENU | SERIAL_NUMBER | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_OR_IMP_SIID | SITE_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_OR_IMP_SMYN | SMDA_YN | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_OR_IMP_STC | STATUS_C | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_OR_IMP_VEDIC | VENDOR_DISTRIB_C | 1 | Yes | Yes |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | IMPLANT_ID | IMP_STENT_DIMENSIONS | IMPLANT_ID | No | No | No |  |
| 1 | IMPLANT_ID | OR_IMP_2 | IMPLANT_ID | Unknown | No | No |  |
| 1 | IMPLANT_ID | OR_IMP_3 | IMPLANT_ID | No | No | No |  |
| 1 | IMPLANT_ID | OR_IMP_SKNSUB | IMPLANT_ID | No | No | No |  |
| 1 | IMPLANT_ID | UK_CRM_LEAD_PLACMNT | IMPLANT_ID | No | No | No |  |
| 1 | IMPLANT_ID | V_CUBE_D_IMPLANT | IMPLANT_ID | Unknown | Unknown | No |  |
| 5 | IMPLANT_TYPE_C | ZC_OR_IMPLANT_TYPE | IMPLANT_TYPE_C | No | No | No |  |
| 6 | MANUFACTURER_C | ZC_OR_MANUFACTURER | MANUFACTURER_C | No | No | No |  |
| 7 | STATUS_C | ZC_OR_IMP_STATUS | STATUS_C | No | No | No |  |
| 10 | VENDOR_DISTRIB_C | ZC_OR_SUPPLIER | SUPPLIER_C | No | No | No |  |
| 14 | SITE_ID | ANALYTICS_SYSTEM_SETTINGS | FACILITY_ID | No | No | No |  |
| 14 | SITE_ID | ARPB_SA_SETTINGS | FACILITY_ID | No | No | No |  |
| 14 | SITE_ID | CLARITY_LOC | LOC_ID | Unknown | No | No |  |
| 14 | SITE_ID | CLARITY_LOC_2 | LOC_ID | Unknown | No | No |  |
| 14 | SITE_ID | CLARITY_POS | POS_ID | No | No | No |  |
| 14 | SITE_ID | CLARITY_POS_2 | POS_ID | No | No | No |  |
| 14 | SITE_ID | CLARITY_SA | SERV_AREA_ID | Unknown | No | No |  |
| 14 | SITE_ID | CL_LOC_HIERARCHY | LOC_ID | Unknown | No | No |  |
| 14 | SITE_ID | CV_PCI_D2B_SETTINGS | FACILITY_ID | No | No | No |  |
| 14 | SITE_ID | EAF_CLM_ALTADR_INF | FACILITY_ID | No | No | No |  |
| 14 | SITE_ID | EAF_CLM_RMT_SETUP | FACILITY_ID | No | No | No |  |
| 14 | SITE_ID | EAF_EXP_APPT_LOG | FACILITY_ID | No | No | No |  |
| 14 | SITE_ID | EAF_SEARCH_TERMS | FACILITY_ID | No | No | No |  |
| 14 | SITE_ID | ESCALATION_THRESH_SGL | FACILITY_ID | No | No | No |  |
| 14 | SITE_ID | FAC_CONNECT | FACILITY_ID | No | No | No |  |
| 14 | SITE_ID | FAC_DIRECT_ADDR | FACILITY_ID | Unknown | No | No |  |
| 14 | SITE_ID | HH_FAC_INFO | FACILITY_ID | No | No | No |  |
| 14 | SITE_ID | MC_FACILITY_GL_SEGMENTS | FACILITY_ID | No | No | No |  |
| 14 | SITE_ID | MYC_INFO | FACILITY_ID | No | No | No |  |
| 14 | SITE_ID | OR_LOC | LOC_ID | Unknown | No | No |  |

_(160 total; showing first 30)_
