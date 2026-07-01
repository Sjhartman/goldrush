# ORDER_DISP_MEDS

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=ORDER_DISP_MEDS

## Description

This table contains information about the dispensed medications for orders.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | ORD |
| Release Version | EPIC 2002 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| ORDER_MED_ID | NUMERIC (18,0) | The unique ID of the order to which these component actions belong. |
| CONTACT_DATE_REAL | No | A unique, internal contact date in decimal format. The integer portion of the number indicates the date of the contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| LINE | No | The line number for the information associated with this record. Multiple pieces of information can often be associated with this record. |
| CONTACT_DATE | DATETIME | The date of this contact in calendar format. |
| DISP_MED_ID | NUMERIC (18,0) | The unique ID of the medication that is related to this component action (the medication that was dispensed, verified or returned). |
| DISP_QTY | NUMERIC (26,4) | The quantity of the dispensed medication. |
| DISP_QTYUNIT_C | INTEGER |  |
| DISP_NDC_CSN | VARCHAR (254) | The NDC CSN of the dispensed medication. |
| PACKAGES | NUMERIC (12,2) | The dispensed packages. |
| SEPARATE_CHG_YN | VARCHAR (1) |  |
| OVR_COMP_COST | NUMERIC (13,3) | The override cost of the component. |
| CHARGE_METHOD_C | VARCHAR (66) |  |
| OVR_COMP_CHARGE | NUMERIC (13,3) | The override charge of the component. |
| DISP_CTYPE_C | INTEGER |  |
| DISP_LOTNUM | VARCHAR (50) | The lot number for a component associated with the dispense. For a mixture, this is the lot number for an individual component of the mixture. For the mixture level lot number, see I ORD 47535. |
| DISP_EXP_DT | DATETIME | The expiration date of the component. |
| COMP_CHARGE *(deprecated)* | NUMERIC (13,3) | Discontinued:  This column extracts a null value, as this item is instead extracted by ORDER_MED_CHARGE.  The charge for the component. |
| BILLING_CODE *(deprecated)* | VARCHAR (50) | Discontinued:  This column extracts a null value, as this item is instead extracted by ORDER_MED_CHARGE.  The billing code associated with the component. |
| BILLING_CODE_QT *(deprecated)* | NUMERIC (12,2) | Discontinued:  This column extracts a null value, as this item is instead extracted by ORDER_MED_CHARGE.  The quantity of billing codes associated with the component. |
| CHG_AMOUNT_USED *(deprecated)* | NUMERIC (13,3) | Discontinued:  This column extracts a null value, as this item is instead extracted by ORDER_MED_CHARGE.  The rounded dispense quantity which will be sent to Billing system. |
| CHG_AMTUNIT_C *(deprecated)* | INTEGER |  |
| COMP_COST *(deprecated)* | NUMERIC (13,3) | Discontinued:  This column extracts a null value, as this item is instead extracted by ORDER_MED_CHARGE.  The cost that is used to calculate the charge  if the medication is charged by component. |
| CM_CT_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this contact. This is only populated if you use IntraConnect. |
| RX_OVERFILL_QTY | NUMERIC (18,2) | Stores the pharmacy-added overfilled dispense amount for a single dose |
| RX_INTENDED_QTY | NUMERIC (13,3) | The intended dispense amount for partial fills in Ambulatory Rx. |
| RX_INTEND_QTYUNT_C | INTEGER |  |
| PRODUCT_SCANNED_YN | VARCHAR (1) |  |
| PRODUCT_SCAN_TYPE_C | INTEGER |  |
| WASTECHG_FAIL_RSN_C | INTEGER |  |
| RX_QTY_DISP_UNIT *(deprecated)* | NUMERIC (18,2) |  |
| RX_PICK_METHOD_C | INTEGER |  |
| RX_VER_COMP_ING_LINE | INTEGER | For administration contact, stores the corresponding component line number of the verify contact. |
| ING_WASTE_REASON_C | INTEGER |  |
| RX_USR_WSTQTY | NUMERIC (18,2) | This item stores the numeric part of the waste quanity and unit entered by the user. |
| RX_USR_WSTQTY_UNT_C | INTEGER |  |
| REPACKAGE_CNR_ID | NUMERIC (18,0) | Stores the CNR ID if the component on this line is a repackaged CNR. |
| RX_APPLY_MFR_OVERFILL_YN | VARCHAR (1) |  |
| RX_MFR_OVERFILL_VOLUME | NUMERIC (18,4) | Holds the manufacturer overfill volume per ingredient. |
| COMPOUND_RECORD_ID | NUMERIC (18,0) | This item stores the compounding record associated with the component. |
| RX_WASTE_COMMENT | VARCHAR (500) | This item stores the comment that the user entered when documenting waste. |
| CNR_USG_STATUS_C | INTEGER |  |
| RX_IS_COMPON_EXCL_ADJUD_YN | VARCHAR (1) |  |
| RX_IS_COMPON_FILT_ADJU_C | INTEGER |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ORDER_MED_ID | ADT_ORDERS_ERRORS | ORDER_ID | No | No | No |  |
| 1 | ORDER_MED_ID | ADT_ORDER_INFORMATION | ORDER_ID | No | No | No |  |
| 1 | ORDER_MED_ID | APPT_REQUEST | REQUEST_ID | No | No | No |  |
| 1 | ORDER_MED_ID | CL_ORD_FST_LST_SCH | ORDER_ID | No | No | No |  |
| 1 | ORDER_MED_ID | DENT_ORD_NOADD | ORDER_ID | No | No | No |  |
| 1 | ORDER_MED_ID | DUPMED_DISMISS_HH_INFO | ORDER_ID | No | No | No |  |
| 1 | ORDER_MED_ID | ENDOSCOPY_METRICS | ORDER_ID | Unknown | No | No |  |
| 1 | ORDER_MED_ID | EXTERNAL_ORDER_INFO | ORDER_ID | No | No | No |  |
| 1 | ORDER_MED_ID | F_IMG_STUDY | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_MED_ID | F_IP_HSP_SUM_ORDER | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_MED_ID | F_LAB_ORDERS | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_MED_ID | F_MU_OBJ_EH_PLACED_ORDER | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_MED_ID | F_MU_OBJ_EH_RESULTD_ORDER | ORDER_PROC_ID | Unknown | Unknown | No |  |
| 1 | ORDER_MED_ID | F_ONC_PRIOR_AUTH_ORDERS | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_MED_ID | F_OPIOID_ORDERS | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_MED_ID | F_RX_ORDER | ORDER_MED_ID | Unknown | Unknown | No |  |
| 1 | ORDER_MED_ID | HH_MED_ORD_IN_POC_DETAIL | ORDER_MED_ID | No | No | No |  |
| 1 | ORDER_MED_ID | HV_ORDER_PROC | ORDER_PROC_ID | Unknown | No | No |  |
| 1 | ORDER_MED_ID | MED_DETAILS_EXT_ORD | ORDER_ID | No | No | No |  |
| 1 | ORDER_MED_ID | MERCHANDISE_ORDER_INFO | ORDER_ID | Yes | No | No |  |
| 1 | ORDER_MED_ID | MU_EH_QRDA_I_ORDER | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_MED_ID | ORDERS | ORDER_ID | No | No | No |  |
| 1 | ORDER_MED_ID | ORDER_AUTH_INFO | ORDER_ID | No | No | No |  |
| 1 | ORDER_MED_ID | ORDER_MED | ORDER_MED_ID | Unknown | No | No |  |
| 1 | ORDER_MED_ID | ORDER_MEDINFO | ORDER_MED_ID | Unknown | No | No |  |
| 1 | ORDER_MED_ID | ORDER_MED_2 | ORDER_ID | Unknown | No | No |  |
| 1 | ORDER_MED_ID | ORDER_MED_3 | ORDER_ID | Unknown | No | No |  |
| 1 | ORDER_MED_ID | ORDER_MED_4 | ORDER_ID | Unknown | No | No |  |
| 1 | ORDER_MED_ID | ORDER_MED_5 | ORDER_ID | Unknown | No | No |  |
| 1 | ORDER_MED_ID | ORDER_MED_6 | ORDER_MED_ID | Unknown | No | No |  |

_(133 total; showing first 30)_
