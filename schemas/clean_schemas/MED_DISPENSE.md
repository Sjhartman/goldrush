# MED_DISPENSE

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=MED_DISPENSE

## Description

This table contains information about a patient's med dispense history from a third-party interface. This information can be helpful for reviewing whether a patient is getting their prescriptions filled at the correct intervals.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | DXR |
| Release Version | Rel 2012 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| DOCUMENT_ID | NUMERIC (22,0) | This item stores the Received Document record ID. |
| CONTACT_DATE_REAL | FLOAT | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| LINE | INTEGER | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| CONTACT_DATE | DATETIME | The date of this contact in calendar format. |
| EXT_DRUG_DESP | VARCHAR (400) | This column stores the drug description in free text. |
| EXT_MED_REF_ID | VARCHAR (174) | This column stores a reference identifier associated with each medication dispense. |
| EXT_DRUD_ID_STR | VARCHAR (254) | This column stores the identifier of the drug. |
| EXT_MED_ERX_ID | NUMERIC (18,0) | This column stores the matching medication ID for this drug. |
| EXT_MED_SMP_GEN_C *(deprecated)* | VARCHAR (66) |  |
| EXT_DRUG_CODE_SYS | VARCHAR (254) | This column stores the coding system used for the drug identifier. |
| EXT_DRUG_DISP_INST_DTTM | DATETIME (Local) | This column stores the dispense instant. |
| EXT_DRUG_DISP_AMT | INTEGER | This column stores the actual dispense amount of the drug. |
| EXT_DRUG_DISP_UNIT | VARCHAR (254) | This column stores the drug dispense unit ID. |
| EXT_DRUG_UNIT_TXT | VARCHAR (254) | This column stores the free text name of the dispense unit. |
| EXT_DRUG_DOSE_FORM | VARCHAR (254) | This column stores the drug dosage form when dispensed. |
| EXT_DRUG_RX_NUM | VARCHAR (254) | This column stores the prescription number of the dispense. |
| EXT_DRUG_DSPPROV_ID | NUMERIC (18,0) | This column stores the dispensing provider ID. |
| EXT_DRUG_PROV_NAME | VARCHAR (254) | The dispensing provider name for the external dispense. |
| EXT_DRUG_UNIT_STR | VARCHAR (254) | This column stores the actual unit strength. |
| EXT_DRUG_PHAR_PHON | VARCHAR (254) | The pharmacy phone (or other contact) number associated with the external dispense. |
| EXT_MED_STATUS_YN *(deprecated)* | VARCHAR (1) |  |
| EXT_MED_DAY_SUPPLY | INTEGER | This column stores the number of days the dispense is written for. |
| EXT_MED_ORDPROV_ID | VARCHAR (18) | The unique identifier of the ordering provider for this medication. This column is frequently used to link to the CLARITY_SER table. |
| EXT_MED_ORD_PROVNAM | VARCHAR (254) | The name of the ordering provider for this medication. |
| EXT_MED_ENT_ORG_NAM | VARCHAR (254) | This column stores the entering organization name of the dispense data. |
| EXT_MED_ORD_ID | NUMERIC (18,0) | This column stores the linked order ID for the corresponding order record in Epic, if one exists. |
| EXT_MED_DISP_UNT_C | INTEGER |  |
| EXT_MED_DAW_YN | VARCHAR (1) |  |
| EXT_MED_REFILLS | VARCHAR (20) | This stores the original refills for an external dispense. |
| EXT_MED_REF_REMAIN | VARCHAR (20) | This stores the refills remaining for an external dispense. |
| EXT_MED_QUAN_REMAIN | INTEGER | This stores the remaining quantity for an external dispense. |
| EXT_MED_QUAN_REM_C | INTEGER |  |
| EXT_MED_DUP_MASTER *(deprecated)* | VARCHAR (174) | *** Deprecated *** In table MED_DISPENSE the column EXT_MED_DUP_MASTER (DXR/16220) has been deprecated.  The deprecated column's content/data is no longer available since it is no longer populated in Chronicles. |
| EXT_MED_MSG_TYPE_C | INTEGER |  |
| EXT_MED_PRI_AUTH | VARCHAR (100) | This stores the prior authorization number for an external dispense. |
| EXT_MED_DOSE | VARCHAR (254) | Stores the discrete dose value for a dispense. |
| EXT_MED_DOSE_UNIT_C | INTEGER |  |
| EXT_MED_FREQ_ID | VARCHAR (18) | The unique ID of the frequency type for the external dispense. |
| EXT_MED_ROUTE_C | INTEGER |  |
| EXT_MED_HIST_C | INTEGER |  |
| WRITTEN_DATE | DATETIME | This item holds the written date for a dispense. |
| EXT_MED_SRC_DXR_CSN | NUMERIC (22,0) | This item stores the contact serial number (CSN) for the Document Received record that contains the external dispense information. |
| DISP_FILTER_RSN_C | INTEGER |  |
| EXT_MED_FILL_STAT_C | INTEGER |  |
| EXT_MED_FILL_REF_NUM | VARCHAR (35) | The external reference number identifying this dispense. |
| EXT_MED_FILL_NOTE | VARCHAR (254) | The note from the external system about this fill. |
| EXT_MED_MIXTURE_FORM_C | INTEGER |  |
| EXT_MED_WAS_SUBSTITUTED_YN | VARCHAR (1) |  |
| EXT_MED_IS_CANCELLATON_YN | VARCHAR (1) |  |
| EXT_DISPENSE_CANCELLATN_IDENT | VARCHAR (174) | The dispense reference ID (EXT_MED_REF_ID) cancelled by this dispense line. |
| EXT_MED_CONCLUDED_YN | VARCHAR (1) |  |
| EXT_MED_MAX_DLY_DOSE | VARCHAR (254) | Stores the maximum daily dose value for a dispense |
| EXT_MED_MAX_DLY_DOSE_QTYUNIT_C | INTEGER |  |
| EXT_MED_PRN_CMT | VARCHAR (450) | Stores the PRN comment for a PRN dispense |
| EXT_DRUG_DSPPROV_ZIP | VARCHAR (24) | This item stores the postal code of the pharmacy or provider that dispensed the medication. This item is only populated in Cosmos host environments. |
| EXT_MED_LINK | VARCHAR (174) | Linked medication order on the 12000 super item for this dispense. |
| EXT_DRUG_DISP_INST_UTC_DTTM | DATETIME (UTC) | This column stores the dispense instant in UTC. Assumes system local time if dispense does not have timezone. |
| MED_SINGLE_SRC_ORG_ID | NUMERIC (18,0) | This column stores the external organization that reported this dispense to organization, in the case where the dispense was reported by exactly 1 source organization. It is only populated on the deduplicated data DXR in Cosmos host environments. |
| DISP_BULK_STAT_C | INTEGER |  |
| DISP_BULK_INCL_DATE | DATETIME | The date to compare to the change tracking window when loading flat files in bulk via DINE. If the date is within the window, but the data element is missing from the load, then the data element is invalidated. |
| EXT_DRUG_SOLD_DATE | DATETIME | This item stores the sold date of an external dispense. |
| EXT_MED_DISPENSER | VARCHAR (254) | The name of the individual that completed the dispense. |
| EXT_MED_TREATMENT_IDENT | VARCHAR (174) | Identifier for the treatment that this dispense is associated with. |
| EXT_MED_FILL_TYPE | VARCHAR (254) | The type of dispense that was completed. |
| EXT_MED_SPLY_UNIT_QF_TM_UNIT_C | INTEGER |  |
| EXT_MED_SPLY | INTEGER | The amount of the dispense supply period. |
| EXT_MED_ROUTE | VARCHAR (254) | The free-text route for the dispense. |
| EXT_MED_CYCLE_REPEAT_DAYS | INTEGER | The number of days before a cyclical dosing instruction should be repeated. |
| EXT_MED_DISPENSER_REF | VARCHAR (254) | The user or organization that dispensed the medication. This is a reference to an ID in I DXR 9000. |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | DOCUMENT_ID | DOCS_RCVD | DOCUMENT_ID | Unknown | No | No |  |
| 1 | DOCUMENT_ID | DOCS_RCVD_FMK_INFO | DOCUMENT_ID | No | No | No |  |
| 1 | DOCUMENT_ID | V_EHI_DXR_LINKED_PATS | DOCUMENT_ID | Unknown | Unknown | No |  |
| 1 | DOCUMENT_ID | DISPENSE_QUERY_INFO | DOCUMENT_ID | No | No | No |  |
| 2 | CONTACT_DATE_REAL | CONTACT_DATE_REAL |  |  |  |  |  |
| 1 | DOCUMENT_ID | DOCS_RCVD_DETAILS | DOCUMENT_ID | Unknown | No | No |  |
| 2 | CONTACT_DATE_REAL | CONTACT_DATE_REAL |  |  |  |  |  |
| 1 | DOCUMENT_ID | DOCS_RCVD_DETAILS_2 | DOCUMENT_ID | No | No | No |  |
| 2 | CONTACT_DATE_REAL | CONTACT_DATE_REAL |  |  |  |  |  |
| 1 | DOCUMENT_ID | DOCS_RCVD_DETAILS_3 | DOCUMENT_ID | No | No | No |  |
| 2 | CONTACT_DATE_REAL | CONTACT_DATE_REAL |  |  |  |  |  |
| 1 | DOCUMENT_ID | DOCS_RCVD_SFM_QUERY_INFO | DOCUMENT_ID | No | No | No |  |
| 2 | CONTACT_DATE_REAL | CONTACT_DATE_REAL |  |  |  |  |  |
| 1 | DOCUMENT_ID | MEDCOM_RCVD_DETAILS | DOCUMENT_ID | No | No | No |  |
| 2 | CONTACT_DATE_REAL | CONTACT_DATE_REAL |  |  |  |  |  |
| 8 | EXT_MED_ERX_ID | CLARITY_MEDICATION | MEDICATION_ID | Unknown | No | No |  |
| 8 | EXT_MED_ERX_ID | MED_ADS_INFO | MEDICATION_ID | No | No | No |  |
| 8 | EXT_MED_ERX_ID | RX_MED_FIVE | MEDICATION_ID | No | No | No |  |
| 8 | EXT_MED_ERX_ID | RX_MED_FOUR | MEDICATION_ID | No | No | No |  |
| 8 | EXT_MED_ERX_ID | RX_MED_ONE | MEDICATION_ID | No | No | No |  |
| 8 | EXT_MED_ERX_ID | RX_MED_THREE | MEDICATION_ID | No | No | No |  |
| 8 | EXT_MED_ERX_ID | RX_MED_TWO | MEDICATION_ID | No | No | No |  |
| 8 | EXT_MED_ERX_ID | V_CUBE_D_MEDICATION | MEDICATION_ID | Unknown | Unknown | No |  |
| 17 | EXT_DRUG_DSPPROV_ID | RX_PHARMACY_SETTINGS | PHARMACY_ID | No | No | No |  |
| 17 | EXT_DRUG_DSPPROV_ID | RX_PHR | PHARMACY_ID | No | No | No |  |
| 17 | EXT_DRUG_DSPPROV_ID | RX_PHR_2 | PHARMACY_ID | No | No | No |  |
| 17 | EXT_DRUG_DSPPROV_ID | RX_PHR_3 | PHARMACY_ID | No | No | No |  |
| 17 | EXT_DRUG_DSPPROV_ID | RX_PHR_CENTRAL_FILL | PHARMACY_ID | No | No | No |  |
| 23 | EXT_MED_ORDPROV_ID | CLARITY_SER | PROV_ID | Unknown | No | No |  |
| 23 | EXT_MED_ORDPROV_ID | CLARITY_SER_2 | PROV_ID | Unknown | No | No |  |

_(134 total; showing first 30)_
