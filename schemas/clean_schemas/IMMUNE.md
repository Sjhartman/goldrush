# IMMUNE

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=IMMUNE

## Description

The IMMUNE table contains data for immunizations ordered through clinical system. May also contain information on immunizations as reported by patient, but not ordered/administered via clinical system;  Fields in this table are noadd- single items in database. If an immunization record is edited/changed, that record will be re-extracted and reflect the updated values.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | LPL |
| Release Version | EPIC 2000 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| IMMUNE_ID | NUMERIC (18,0) | The unique ID of the immunization record in your system production system. |
| PAT_ID | VARCHAR (18) | The unique ID assigned to the patient record. This ID may be encrypted if you have elected to use enterprise reporting?s encryption utility. |
| IMMUNZATN_ID | NUMERIC (18,0) | The ID of the immunization record that corresponds to the type of immunization given to this patient. |
| IMMUNE_DATE | DATETIME | The date the immunization was administered in calendar format. |
| DOSE | VARCHAR (80) | The immunization dosage. |
| ROUTE_C | INTEGER |  |
| SITE_C | INTEGER |  |
| MFG_C | INTEGER |  |
| LOT | VARCHAR (200) | The lot number of the vaccine. |
| EXP_DATE | DATETIME | The date the immunization is next due, if in a series. This is manually established by the user, and not automatically calculated like an HM or advisory. |
| GIVEN_BY_USER_ID | VARCHAR (18) | The unique ID of the system user who administered the immunization. This ID may be encrypted. |
| ENTRY_USER_ID | VARCHAR (18) | The unique ID of the system user who ordered the immunization. This ID may be encrypted.  NOTE: If an immunization record is edited/updated, this will show the most recent change user ID. |
| ENTRY_DATE | DATETIME | The date the immunization was recorded in the patient?s chart in calendar format. NOTE: If an immunization record is edited/updated, this will show the most recent change date. |
| STATUS *(deprecated)* | VARCHAR (30) |  |
| UPDATE_DATE | No | *** Deprecated *** This column is not reliably populated, row update tracking should be used instead. ****** The extract date and time of the record for this table. |
| CM_PHY_OWNER_ID | VARCHAR (25) | ID of the physical deployment owner for this record.  Physical owners will be where the data is hosted, either on the cross-over server or the owner deployment. |
| CM_LOG_OWNER_ID | VARCHAR (25) | ID of the logical deployment owner for this record.  Logical owners show the deployment where the record was created but doesn't represent if the record is a part of version skew. |
| EXPIRATION_DATE | DATETIME | Date upon which this immunization expires |
| EXTERNAL_ADMIN_C | INTEGER |  |
| VIS_DATE_TEXT | VARCHAR (254) | The date on the vaccine information statement. Note that this is a free text field in the application, so data will not be in standard datetime format. |
| DEFER_REASON_C | INTEGER |  |
| MED_ADMIN_COMMENT | VARCHAR (1000) | Free text comment regarding the administration of this immunization |
| PHYSICAL_SITE | VARCHAR (254) | Item that stores the physical location where the immunization was administered like some specific hospital |
| IMM_PRODUCT | VARCHAR (254) | Item which stores the product of the immunization. Products are usually related to the lot number. |
| IMMUNIZATION_TIME | DATETIME (Local) | Column that stores the time when a given immunization was administered. |
| NDC_NUM_ID | VARCHAR (18) | Store the NDC number ID associated with the administration |
| DOCUMENT_DCS_ID | VARCHAR (18) | Document ID for the immunization. This is the information stored when the e-sign information is selected. |
| ORDER_ID | NUMERIC (18,0) | Order ID for immunization ordered. |
| IMM_ANSWER_ID | VARCHAR (18) | Stores answers for immunization questions. |
| IMMNZTN_STATUS_C | INTEGER |  |
| IMM_MAR_ADMIN_LINE | INTEGER | The line number in the linked order record's immunization link item (I ORD 11270) which references this immunization record ID. |
| IMM_CHARGE_REC_ID | VARCHAR (254) | This column contains the UCL (Universal Charge Line) record ID for the immunization charge. |
| IMM_CSN | NUMERIC (18,0) | This column contains the CSN (contact serial number) for the immunization. |
| EXTERNAL_ID | VARCHAR (192) | This column contains the immunization's external ID, which is populated by the interface.  The external ID is the external system's identifier for the immunization. |
| EXTERNAL_SYSTEM | VARCHAR (254) | This column contains the name or ID of the third party system that the immunization data came from.  This item is only populated by custom import specifications. |
| INSTANT_OF_ENT_DTTM | DATETIME (Local) | This column contains the last instant of update of the immunization problem list (LPL) record. |
| ENCOUNTER_DEPT_ID | NUMERIC (18,0) | This column contains the unique ID of the encounter department for the immunization.  This item is only populated by custom import specifications. |
| REC_ARCHIVED_YN | No | Indicates whether the Immunization record is archived at the record level. |
| IMM_HISTORIC_ADM_YN | VARCHAR (1) |  |
| IMMNZTN_DUALSIGN_ID | VARCHAR (18) | The user who performed the second user verification on the immunization. |
| IMM_DUALSIGNINSTANT_DTTM | DATETIME (Local) | The instant at which this immunization was verified by the second user. |
| IMMNZTN_DOSE_AMOUNT | NUMERIC (18,4) | Immunization dose amount. |
| IMMNZTN_DOSE_UNIT_C | INTEGER |  |
| IMM_DEL_REASON_C | VARCHAR (66) |  |
| IMM_SCANNED_BARCODE | VARCHAR (254) | The raw data captured during immunization barcode scanning. |
| ENTRY_DTTM | DATETIME (Local) | Contains the date and time that the immunization administration data was last updated. If the exact time is not known, a date may be contained in ENTRY_DATE instead. |
| IMM_STORAGE_UNIT_ID | NUMERIC (18,0) | Immunziation Storage Unit. |
| IMM_PRODUCT_C | INTEGER |  |
| IMM_DEFER_DUR_C | INTEGER |  |
| IMM_REG_STATUS_C | INTEGER |  |
| IMM_LST_REGINST_UTC_DTTM | DATETIME (UTC) | Last instant in which the overall registry status from an Immunization Registry was updated for a vaccine administration problem list  (LPL)record. |
| IMM_INV_CLASS_C | INTEGER |  |
| IMM_MAR_ADM_INPATIENT_DATA_ID | VARCHAR (18) | Link to the INP record that may hold the administrations data. |
| IMM_LOT_NUM_ID | NUMERIC (18,0) | This item stores the record ID of the lot(LOT) used for immunization administration. |
| IMM_EDIT_SOURCE_C | INTEGER |  |
| ORIGINAL_IMM_EDIT_SOURCE_C | INTEGER | Surrogate key used to uniquely identify rows in this (and only this) table on Cogito Cloud only, do not assume the surrogate key in this table will correspond to the surrogate key in another table |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| BITMAP INDEX | EIX_IMMUNE_DEFERRAL_REASON | DEFER_REASON_C | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_IMMUNE_DOCUMENT | DOCUMENT_DCS_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_IMMUNE_ENTRY_DATE | ENTRY_DATE | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_IMMUNE_ENTRY_USER | ENTRY_USER_ID | 1 | Yes | Yes |  |
| BITMAP INDEX | EIX_IMMUNE_EXTERNAL_ADMIN | EXTERNAL_ADMIN_C | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_IMMUNE_GIVEN_BY | GIVEN_BY_USER_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_IMMUNE_LIM_ID | IMMUNZATN_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_IMMUNE_LOT | LOT | 1 | Yes | Yes |  |
| BITMAP INDEX | EIX_IMMUNE_MFG | MFG_C | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_IMMUNE_NDC | NDC_NUM_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_IMMUNE_ORDER | ORDER_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_IMMUNE_PAID | PAT_ID | 1 | Yes | Yes |  |
| BITMAP INDEX | EIX_IMMUNE_ROUTE | ROUTE_C | 1 | Yes | Yes |  |
| BITMAP INDEX | EIX_IMMUNE_SITE | SITE_C | 1 | Yes | Yes |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | IMMUNE_ID | ADVERSE_EVENT_INFO | ADVERSE_EVENT_ID | No | No | No |  |
| 1 | IMMUNE_ID | ALLERGY | ALLERGY_ID | Unknown | No | No |  |
| 1 | IMMUNE_ID | COMPLICATIONS | PROBLEM_LIST_ID | No | No | No |  |
| 1 | IMMUNE_ID | HH_PBLST_INFO | PROBLEM_LIST_ID | Unknown | No | No |  |
| 1 | IMMUNE_ID | PL_SYSTEMS | PROBLEM_LIST_ID | Unknown | No | No |  |
| 1 | IMMUNE_ID | PROBLEM_LIST | PROBLEM_LIST_ID | Unknown | No | No |  |
| 1 | IMMUNE_ID | PROBLEM_LIST_ALL | PROBLEM_LIST_ID | No | No | No |  |
| 1 | IMMUNE_ID | PROB_TXP_MODIFIERS | PROBLEM_LIST_ID | Unknown | No | No |  |
| 1 | IMMUNE_ID | V_IMMUNIZATION_ADMINS | IMMUNE_ID | Unknown | Unknown | No |  |
| 2 | PAT_ID | ANTICOAG_SELF_REGULATING | PAT_ID | No | No | No |  |
| 2 | PAT_ID | CARE_COORDINATION | PAT_ID | Unknown | No | No |  |
| 2 | PAT_ID | CLAIMS_DERIVE_PAT_FLAGS | PAT_ID | No | No | No |  |
| 2 | PAT_ID | COMMUNITY_RESRC_REVIEWED | PAT_ID | No | No | No |  |
| 2 | PAT_ID | D_PAT_GEOGRAPHIC_CLASS | PAT_ID | Unknown | Unknown | No |  |
| 2 | PAT_ID | EPT_MEM_INFO | PAT_ID | No | No | No |  |
| 2 | PAT_ID | EXT_DATA_LAST_DONE | PAT_ID | No | No | No |  |
| 2 | PAT_ID | F_IBD_ADULT_FORM_PAT | PAT_ID | Unknown | Unknown | No |  |
| 2 | PAT_ID | HH_PAT_INFO | PAT_ID | Unknown | No | No |  |
| 2 | PAT_ID | HM_STATUS_UPD | PAT_ID | No | No | No |  |
| 2 | PAT_ID | IMMNZTN_LAST_REVIEW | PAT_ID | No | No | No |  |
| 2 | PAT_ID | PATIENT | PAT_ID | No | No | No |  |
| 2 | PAT_ID | PATIENT_2 | PAT_ID | No | No | No |  |
| 2 | PAT_ID | PATIENT_3 | PAT_ID | No | No | No |  |
| 2 | PAT_ID | PATIENT_4 | PAT_ID | No | No | No |  |
| 2 | PAT_ID | PATIENT_5 | PAT_ID | No | No | No |  |
| 2 | PAT_ID | PATIENT_6 | PAT_ID | No | No | No |  |
| 2 | PAT_ID | PATIENT_CONF_ADDR | PAT_ID | No | No | No |  |
| 2 | PAT_ID | PATIENT_MISC_COMMENTS | PAT_ID | No | No | No |  |
| 2 | PAT_ID | PATIENT_MYC | PAT_ID | Unknown | No | No |  |
| 2 | PAT_ID | PATIENT_OPT | PAT_ID | No | No | No |  |

_(338 total; showing first 30)_
