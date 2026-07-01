# ORDER_DISP_INFO

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=ORDER_DISP_INFO

## Description

This table contains dispense information for orders.

**Primary table** in this group (101 cols). Overflow siblings joined on shared key: ORDER_DISP_INFO_2 (100 cols), ORDER_DISP_INFO_3 (95 cols). Prefer this table for most queries.

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
| ORDER_MED_ID | NUMERIC (18,0) | The unique ID of the order that these actions were taken on. |
| CONTACT_DATE_REAL | FLOAT | A unique, internal contact date in decimal format. The integer portion of the number indicates the date of the contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| CONTACT_DATE | DATETIME | The date of this contact in calendar format. |
| PHARMACY_USR_ID | VARCHAR (18) | The unique ID of the user who performed this pharmacy action. |
| ACTION_INSTANT | DATETIME (Local) | The instant of the pharmacy action. |
| SERVICE_DATE | DATETIME | The service date for the order action. |
| DISPENSE_PHR_ID | NUMERIC (18,0) | The unique ID of the pharmacy that is the dispense location of this order.    Different dispense pharmacies could be used for the first doses and other doses. The column FIRSTDOSE_PHR_ID in the table ORDER_DISP_INFO is used to save the dispense location for first doses. |
| INP_ADMIN_LINE_NO | NUMERIC (12,2) | For admin contacts, the matching MAR line number from the INP record for the patient's encounter. |
| INP_ADMIN_DISP_LNK | NUMERIC (12,2) | The inpatient administration dispense contact. |
| START_NUMBER | NUMERIC (12,2) | The starting dose or bag number. |
| DISPENSE_COUNT *(deprecated)* | NUMERIC (12,2) |  |
| CHG_BY_COMP_YN | VARCHAR (1) |  |
| GROUP_CHARGE | NUMERIC (13,3) | The group charge to be dropped for this order. |
| OVR_TOTAL_CHG *(deprecated)* | NUMERIC (13,3) |  |
| MIXTURE_CHARGE | NUMERIC (13,3) | The mixture charge defined at the medication level. |
| VERIFY_CONT_DAT | VARCHAR (255) | The contact date of the verify contact related to this contact in Chronicles DAT format. |
| RETURN_CNCT_DAT | VARCHAR (255) | The date of the dispense contact this return contact corresponds to in Chronicles DAT format. |
| DISP_VRFY_ID *(deprecated)* | VARCHAR (18) |  |
| DISP_VRFY_INST *(deprecated)* | DATETIME | *** Deprecated *** In table ORDER_DISP_INFO, the column DISP_VRFY_INST (ORD/48065) has been deprecated.   The deprecated column's content/data is no longer available since it is no longer populated in Chronicles. This information can be found in table ORDER_RXVER_TRACE in column RX_VERIFY_INSTANT (ORD/48016). |
| CHARGE_DRP_INST | DATETIME (Local) | The instant the charge was dropped. |
| DISPENSE_SIG *(deprecated)* | VARCHAR (255) | *** Deprecated *** In table ORDER_DISP_INFO, the column DISPENSE_SIG (ORD/48100) has been deprecated.   The deprecated column's content/data is no longer available since it is no longer populated in Chronicles. |
| REFILL_NUMBER *(deprecated)* | NUMERIC (12,2) |  |
| REFILLS_USED *(deprecated)* | NUMERIC (12,2) |  |
| ORD_CNTCT_TYPE_C | INTEGER |  |
| DISPENSE_CODE_C | INTEGER |  |
| DISP_STAT_NAME *(deprecated)* | VARCHAR (255) |  |
| DISP_INTERVAL | NUMERIC (15,5) | The interval in hours between each dispense |
| DISP_INT_INST | DATETIME (Local) | The instant this dispense was created for scheduling dispenses based on the dispense interval. |
| CART_GROUP_C *(deprecated)* | INTEGER |  |
| PAR_DOSES | INTEGER | PRN par level number of doses. |
| AUTO_RETURN_YN | VARCHAR (254) |  |
| DISP_VRFY_CART_ID | VARCHAR (18) | The unique ID of the user that verified the actual products prepared to satisfy a given dispense. |
| DISP_ONCE_YN | VARCHAR (254) |  |
| DISP_TYPE_C | INTEGER |  |
| DISP_UNIT_ID | NUMERIC (18,0) | The unique ID of the department this dispense was sent to.  Normally, this is the patient's department as of the action instant.  If the dispense was sent to another department (such as a surgical unit), that department is stored instead. |
| BULK_DISP_YN *(deprecated)* | VARCHAR (254) |  |
| DISP_MED_CNTCT_ID | No | The Contact Date Real of the dispense-related contact corresponding to this contact.  For Verify, Return, Admin, Credit, Waste, and Waste Credit contacts, this column will store the same data as CONTACT_DATE_REAL for this contact.  For Dispense contacts, this column will store the Contact Date Real of the most recent Verify contact, except if the medication/package dispensed was changed from what was verified.  In that case, this field will store the same data as CONTACT_DATE_REAL for this contact.  Use this field to link to ORDER_DISP_MEDS.CONTACT_DATE_REAL to correctly view data from ORDER_DISP_MEDS for each Verify, Return and Dispense contact. |
| CM_CT_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this contact. This is only populated if you use IntraConnect. |
| VERIFY_CONTDATREAL | FLOAT | The Contact Date Real of the most recent verify contact. |
| RETURN_CNCTDATREAL | FLOAT | The Contact Date Real of the  dispense contact that corresponds to this return contact. |
| ADMIN_DISPDATREAL | FLOAT | The Contact Date Real of the dispense contact that corresponds to this administration contact. |
| MED_CREDIT_TYPE_C | INTEGER |  |
| FIRSTDOSES_PHR_ID | NUMERIC (18,0) | The unique ID of the pharmacy that is dispensing the first dose.  Column DISPENSE_PHR_ID is used to save the dispense location for remaining doses. |
| MEDADMIN_STATUS_C | INTEGER |  |
| MED_VERIFY_TYPE_C | INTEGER |  |
| TRIGGER_FILL_YN | VARCHAR (254) |  |
| TRIGGER_CLEAR_INST | DATETIME (Local) | The instant when the order is removed from the triggered fill list of the pharmacy. |
| ORDER_CHARGE *(deprecated)* | NUMERIC (25,3) |  |
| ORDER_COST *(deprecated)* | NUMERIC (25,3) |  |
| DISP_VERIFY_INST | DATETIME (Local) | The instant when the actual products prepared to satisfy a given dispense were verified. |
| DISPENSE_REASON_C | INTEGER |  |
| CHARGE_SUPPRESS_C | INTEGER |  |
| RX_DISPENSE_CART_ID | NUMERIC (18,0) | The unique ID of the cart that will deliver this dispense contact. |
| RX_DELIVERY_DEST_ID | NUMERIC (18,0) | The unique ID of the patient location that is the destination of this dispense contact. |
| FILL_PHR_ID | NUMERIC (18,0) | The fill pharmacy for prescription being filled from Integrated pharmacy for each fill. A prescription could be filled multiple times and each fill will have a fill pharmacy saved.  A fill request is a contact on the order record recording information about the specific dispense of the order. |
| RX_NUM_UNFMTTED_HX | VARCHAR (254) | The history of the unformatted prescription numbers for the order (including the current active unformatted prescription number). |
| RX_NUM_FORMATTED_HX | VARCHAR (192) | The history of the formatted prescription numbers for the order (including the current active formatted prescription number). |
| FILL_AUTHPHRMCST_ID | VARCHAR (18) | When a prescription is filled in an integrated pharmacy, a fill contact is created in the order and all fill information is saved to this fill contact. A prescription can have multiple fills.  This item saves the pharmacist who will take responsibility of the fill when sending an adjudication message. |
| FILL_SERVICE_DATE | DATETIME | The date of service for a prescription fill.   The date of service can be entered by a user during the filling process. If no service date was entered by the user, then the date of service is the date of the first successful adjudication. If the prescription fill was not adjudicated, then the date of service is the date the fill was dispensed. |
| FILL_NUMBER | NUMERIC (18,0) | When a prescription is filled in an integrated pharmacy, a fill contact is created in the order and all fill information is saved to this fill contact. A prescription can have multiple fills.  The value is used in adjudication to indicate what fill we are adjudicating. The fill numbers are sequential with the first fill set to 0 and all refills numbered 1-99. |
| FILL_SUBM_CLR_C *(deprecated)* | INTEGER |  |
| FILL_SUPPLY_DAYS | NUMERIC (18,0) | When a prescription is filled in an integrated pharmacy, a fill contact is created in the order and all fill information is saved to this fill contact. A prescription can have multiple fills.  This is the number of days this fill will supply. For example, this fill dispensed enough to cover a 30-day supply. |
| FILL_DISP_QTY | NUMERIC (19,4) | When a prescription is filled in an integrated pharmacy, a fill contact is created in the order and all fill information is saved to this fill contact. A prescription can have multiple fills.  This is the actual amount the pharmacy is dispensing. This may be different from the intended quantity, which is what the prescriber intended the patient to receive. The two numbers may be different if the patient can only pay for a smaller days supply, or the pharmacy may only have a small amount of the medication left to dispense. |
| FILL_INT_SUP_DAYS | NUMERIC (18,0) | When a prescription is filled in an integrated pharmacy, a fill contact is created in the order and all fill information is saved to this fill contact. A prescription can have multiple fills.  If the fill is a partial fill, this is the number of days the supply that is dispensed will cover. For example, I have a partial fill of 15 tabs for a Daily medication. The intended days supply would be 15. |
| FILL_IS_PARTIAL_YN | VARCHAR (1) |  |
| FILL_SOURCE_C | INTEGER |  |
| FILL_TYPE_C | INTEGER |  |
| FILL_STATUS_C | INTEGER |  |
| FILL_PAT_LOC_C | INTEGER |  |
| FILL_PRIORAUTHTYP_C *(deprecated)* | INTEGER |  |
| FILL_PRIORAUTHNUM *(deprecated)* | NUMERIC (18,0) | When a prescription is filled in an integrated pharmacy, a fill contact is created in the order and all fill information is saved to this fill contact. A prescription can have multiple fills.  This item stores the prior authorization number that will be used when adjudicating the prescription. |
| FILL_DISP_QTYUNT_C | INTEGER |  |
| FILL_INT_QTY | NUMERIC (19,4) | When a prescription is filled in an integrated pharmacy, a fill contact is created in the order and all fill information is saved to this fill contact. A prescription can have multiple fills.  This is the amount the prescriber intended the patient to receive. In the case of a partial fill, the patient can only pay for a smaller supply or the pharmacy may only have a small amount of the medication left to dispense, and this actual dispense amount is saved in the dispense quantity. |
| FILL_INT_QTYUNT_C | INTEGER |  |
| CHG_STATUS_C | INTEGER |  |
| ACQUISITION_COST | NUMERIC (18,3) | When a prescription is filled in an integrated pharmacy, a fill contact is created in the order and all fill information is saved to this fill contact. A prescription can have multiple fills.  This item stores the acquisition cost of the medication that is being dispensed. |
| CASH_PRICE | NUMERIC (18,3) | The cash price for this order. |
| PLAN_PRICE *(deprecated)* | NUMERIC (18,3) | This column which is a single response is replaced with a column that is multiple response, RX_FILL_COVERAGES__PLAN_PRICE_FOR_CVG. This will allow a plan price to be calculated for each coverage.  When a prescription is filled in an integrated pharmacy, a fill contact is created in the order and all fill information is saved to this fill contact. A prescription can have multiple fills.  This item is the plan price for the fill.  This will be sent in to the payor during adjudication or used when billing charity or discount coverages. |
| FILL_REF_REQ_STAT_C *(deprecated)* | INTEGER |  |
| RX_TO_PHRM_USER_ID | VARCHAR (18) | This is the user that authorized the incoming prescription transfer (typically a pharmacist) when the user exists in the User (EMP) master file. |
| RX_TO_PHRM_USERNAM | VARCHAR (254) | This is the name of the user that authorized the incoming prescription transfer (typically a pharmacist) when the user does not exist in the User (EMP) master file. |
| RX_FRM_PHRM_USER_ID | VARCHAR (18) | This is the user that authorized the outgoing prescription transfer (typically a pharmacist) when the user exists in the User (EMP) master file. |
| RX_FRM_PHRM_USERNAM | VARCHAR (254) | This is the name of the user that authorized the outgoing prescription transfer (typically a pharmacist) when the user does not exist in the User (EMP) master file. |
| RX_FRM_PHRM_ID | NUMERIC (18,0) | This is the pharmacy from which the prescription was transferred when the pharmacy exists in the Pharmacy (PHR) master file. |
| RX_FRM_PHRM_NAM | VARCHAR (254) | This is the name of the pharmacy from which the prescription was transferred when the pharmacy does not exist in the Pharmacy (PHR) master file. |
| RX_FRM_PHRM_PHNUM | VARCHAR (254) | This is the phone number of the pharmacy from which the prescription was transferred when the pharmacy does not exist in the Pharmacy (PHR) master file. |
| RX_TO_PHRM_NAM | VARCHAR (254) | This is the name of the pharmacy to which the prescription was transferred when the pharmacy does not exist in the Pharmacy (PHR) master file. |
| RX_TO_PHRM_PHNUM | VARCHAR (254) | This is the phone number of the pharmacy to which the prescription was transferred when the pharmacy does not exist in the Pharmacy (PHR) master file. |
| RX_TRANSFER_COMMENT | VARCHAR (254) | These are the comments that are entered along with the prescription transfer. |
| PAT_PAY_AMOUNT | NUMERIC (18,3) | This is the expected payment amount for this order. This can be calculated by the system and optionally overridden by the user. If the patient pay amount was overridden, then the override amount is stored here. |
| RX_CHG_SUPPRESS_YN | VARCHAR (1) |  |
| RX_CHG_FORCED_YN | VARCHAR (1) |  |
| FILL_PKG_DISPQTY | NUMERIC (18,0) | The number of packages dispensed for this fill. |
| FILL_NDC_CSN | VARCHAR (12) | This column stores the package (NDC) contact serial number (CSN) for the dispensed medication. |
| DISP_WHOLE_PKG_YN | VARCHAR (1) |  |
| RX_REFIL_REQ_ORD_ID | NUMERIC (18,0) | The ID of the pending order associated with the refill request. |
| HAS_RX_FLAGS_YN | VARCHAR (1) |  |
| DAW_REASON_C | INTEGER |  |
| CASH_PAY_YN | VARCHAR (1) |  |
| ADJ_DEFERRED_YN | VARCHAR (1) | Surrogate key used to uniquely identify rows in this (and only this) table on Cogito Cloud only, do not assume the surrogate key in this table will correspond to the surrogate key in another table |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| B-TREE INDEX | EIX_ORD_DISP_INFO_ACT_INST | ACTION_INSTANT | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_ORD_DISP_INFO_TYPE_DATE | ORD_CNTCT_TYPE_C | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_ORD_DISP_INFO_TYPE_DATE | CONTACT_DATE | 2 | Yes | Yes |  |

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

_(274 total; showing first 30)_
