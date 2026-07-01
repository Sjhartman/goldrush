# ORDER_DISP_INFO_2

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=ORDER_DISP_INFO_2

## Description

This table contains dispense information for orders.

**Overflow table** for ORDER_DISP_INFO (101 cols). Contains additional columns for the same records — join on the shared primary key column.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | ORD |
| Release Version | Summer 2009 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| ORDER_ID | NUMERIC (18,0) | The unique identifier (.1 item) for the order record. |
| CONTACT_DATE_REAL | No | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| CONTACT_DATE | DATETIME | The date of this contact in calendar format. |
| CM_CT_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this contact. This is only populated if you use IntraConnect. |
| TRACKED_DISP_INFO | VARCHAR (128) | Caret (^) delimited string with two pieces. The first piece indicates whether the associated dispense qualifies for a discounted price from the medication vendor or wholesaler. If the dispense qualifies for a discounted price, the value of the first piece is 1; otherwise it is 0. The second piece stores the inventory class of the balance record the associated dispense was deducted from. |
| RX_TO_PHRM_DEA | VARCHAR (20) | The transfer to pharmacy's Drug Enforcement Administration (DEA) number captured during a prescription transfer. A DEA number is assigned by the Drug Enforcement Administration to providers to allow them to write prescriptions for controlled substances. |
| RX_XFER_PHARMACY_ID | NUMERIC (18,0) | Stores the pharmacy that performed the prescription transfer. |
| RX_XFR_LAST_DISP_DT | DATETIME | Date the prescription was last dispensed from the previous non-integrated pharmacy captured during a prescription transfer. |
| RX_FROM_PHRM_DEA | VARCHAR (20) | The transfer from pharmacy's Drug Enforcement Administration (DEA) number captured during prescription transfer. A DEA number is assigned by the Drug Enforcement Administration to providers to allow them to write prescriptions for controlled substances. |
| RX_BILL_GUAR_ACC_ID | NUMERIC (18,0) | This item is used to contain the guarantor account ID to bill the remaining balance of the prescription if the patient will not be paying with cash. |
| RX_BILL_HOSP_ACC_ID | NUMERIC (18,0) | This item is used to contain the hospital account ID to bill the remaining balance of the prescription if the patient will not be paying with cash. |
| PAT_PAY_AMOUNT_CALC | NUMERIC (18,2) | When the prescription patient pay amount is overridden, this item is populated with the calculated patient pay amount. When the patient pay amount is not overridden, the calculated patient pay amount is stored in the patient pay amount (I ORD 47380). For cash prescriptions, the calculated patient pay amount is the cash price calculated by ambulatory pharmacy. For prescriptions using coverage, it's the patient pay amount determined by the processor. |
| PAT_PAY_AMT_REAS_C | INTEGER |  |
| FILL_PILL_CNTR_ID | NUMERIC (18,0) | The unique ID of the pill counter robot that filled the dispense. |
| DISPENSE_PRIORITY_C | INTEGER |  |
| WAS_FROM_RAR_APP_YN | VARCHAR (1) |  |
| RX_XFR_FRST_DISP_DT | DATETIME | The date the previous non-integrated pharmacy first dispensed the prescription to the patient. |
| FULLY_RETURNED_YN | VARCHAR (1) |  |
| RX_FRM_PHR_ADDR | VARCHAR (508) | A prescription can be transferred in from a non-integrated pharmacy that is not built in the system (a free-text pharmacy). That pharmacy's address can be entered during the transfer in and stored here. |
| RX_TO_PHR_ADDR | VARCHAR (508) | A prescription can be transferred out from an ambulatory pharmacy to a non-integrated pharmacy that is not built in the system (a free-text pharmacy). That pharmacy's address can be entered during the transfer out and stored here. |
| WASTE_DISP_YN | VARCHAR (1) |  |
| RX_RTRN_INV_LOC_ID | NUMERIC (18,0) | Specifies the return location (IVL) for a returned/wasted dispense |
| ACQ_COST_CALCULATED | NUMERIC (18,2) | The calculated acquisition cost if the user overrode the acquisition cost. If blank the acquisition cost (I ORD 47365) is the calculated acquisition cost. |
| ACQ_COST_REAS_C | INTEGER |  |
| ACQ_COST_OVR | NUMERIC (18,2) | The user specified value for the acquisition cost. |
| CASH_PRICE_CALC | NUMERIC (18,2) | The calculated cash price if the user overrode the cash price. If blank the cash price (I ORD 47370) is the calculated cash price. |
| CASH_PRICE_REAS_C | INTEGER |  |
| CASH_PRICE_OVR | NUMERIC (18,2) | The user specified value for the cash price. |
| PAT_PAY_AMT_OVR | NUMERIC (18,2) | The user specified value for the patient pay amount. |
| RX_ORIGIN_CODE_C | INTEGER |  |
| RX_XFER_FILL_XFR_YN | VARCHAR (1) |  |
| RX_XFER_QTY_XFER | NUMERIC (18,2) | This is the quantity that was transferred during a prescription transfer. |
| RX_XFR_QTY_UNIT_C | INTEGER |  |
| WAST_CHGDATREAL_DT | FLOAT | The Contact Date Real of the charge contact that corresponds to this waste contact. This contact can be an administration or dispense. |
| RET_WASTEDATREAL_DT | FLOAT | The Contact Date Real of the waste contact that corresponds to this waste return contact. |
| RX_WASTE_CHG_YN | VARCHAR (1) |  |
| NUM_DAYS_SUPPLY_YN | VARCHAR (1) |  |
| NUM_DAYS_TO_SUPPLY | INTEGER | If an order is dispensing number of days supply, this item stores the number of days that should be supplied by default. |
| NUM_DOSES_TO_SUPPLY | INTEGER | If an order is dispensing number of days supply, this item stores the number of doses that are accounted for in the number of days to dispense. |
| WAST_LINKDATREAL_DT | FLOAT | The Contact Date Real of the waste contact that corresponds to linked waste contact. This contact was auto generated by the contact indicated in the item. |
| COMP_FILL_YN | VARCHAR (1) |  |
| PART_FILL_CVG_SU_YN | VARCHAR (1) |  |
| PART_FILL_PARNT_DTE | NUMERIC (18,2) | For partial fills, the item holds the fill contact date in decimal format of the first partial fill. |
| RX_WASTE_STATUS_C | INTEGER |  |
| PAT_PAY_AMT_ESTIMAT | NUMERIC (18,2) | The patient pay amount estimated for the patient when requesting the fill. For example, this displays to the patient when requesting fills on the web with their credit card. If no estimate is shown to the patient, nothing will be stored. |
| PAT_PAY_AMT_POSTED | NUMERIC (18,2) | The total amount paid by the patient for this order. |
| PAT_PAY_AMT_APPRVD | NUMERIC (18,2) | The maximum allowed amount to charge the patient. This is used if an estimated price is shown to the patient while requesting the fill. For example, if an estimated price was shown to the patient this would initially be the estimated price plus a buffer. If blank, there is no maximum. |
| PRES_DISP_CUST_ID | VARCHAR (100) | This item contains the government issued ID of the customer picking up the corresponding prescription fill. |
| RX_FILL_DC_USER_ID | VARCHAR (18) | The unique ID of the user who filled a discontinued prescription. Normally this user is a pharmacist. |
| RX_XFER_LEG_CONV_YN | VARCHAR (1) |  |
| RX_INV_CNTRCT_TYP_C | INTEGER |  |
| RX_INV_CLASS_C | INTEGER |  |
| RX_CHARGE_STATUS_C | INTEGER |  |
| RX_ADM_OR_WAST_LNK_DISP_ORD_ID | NUMERIC (18,0) | This is the Order ID for one of the following contacts:     The dispense contact in ORD 48037, which is the contact the      administration is linked to.     The dispense contact in ORD 48062, which is the contact the waste is      documented against in dispense prep. |
| RX_CANCEL_INST_DTTM | DATETIME (Local) | This item contains the instant that a contact on an order was canceled. |
| RX_CANCEL_USER_ID | VARCHAR (18) | This item contains the user who canceled a contact on the order. |
| RX_WASTE_SOURCE_C | INTEGER |  |
| RX_DISP_WASTE_DAT | VARCHAR (184) | The linked dispense prep contact for waste |
| ADJUD_COMP_LINE | INTEGER | This corresponds to the line in the ORDER_MEDMIXINFO table of the component an adjudication contact is associated with. This is used when adjudicating each ingredient of an IMS Tab Mixture separately in Long Term Care. |
| LTC_ADJUDICATION_ORD_ID | NUMERIC (18,0) | Indicates the corresponding adjudication order ID in long term care. |
| LTC_ADJUDICATION_FLAG_C | INTEGER |  |
| SERVICE_DTTM | DATETIME (Local) | Service Date/Time If I ORD 48043 Service Time or I ORD 48025 Service Date is null, then this column will be null. If I ORD 48043 and I ORD 48025 both are not null, this item will combine the date portion of 48025 and time portion of 48025 to form a complete date. |
| RX_PATIENT_CLASS_C | VARCHAR (66) |  |
| RX_BILL_PAYMENT_ID | NUMERIC (18,0) | In table ORDER_DISP_INFO_2, the column RX_BILL_PAYMENT_ID (I ORD 47815) has been deprecated.  This column has been replaced by column RX_TAR_ID (I ORD 47816) in the table RX_ORDER_DISP_PAT_PMTS.  The deprecated column's data is no longer available because it is no longer populated in Chronicles. |
| RX_GEN_LOT_NUM | VARCHAR (100) | Stores the lot number generated by the system during release from the dispense queue. |
| ADMIN_CHG_DATREAL | FLOAT | This item stores the linked charge contact. Only One Step simple medication administration use this item to store the linked CHARGE contact. |
| APFS_MSG_SEQ_NUM | INTEGER | This item is used to indicate the proper sequencing of messages to and from Automated Prescription Filling Systems. When a new fill request is sent to a filling system, this number will be 1, and it will increment with each subsequent outgoing update message to the filling system for that particular fill. The intended purpose of this item is to provide a means for detection of cross-communication errors where the filling system is responding to messages containing data that may no longer be relevant. |
| RX_REFILL_REQ_MTHD_C | INTEGER |  |
| RX_REFILL_REQ_SER_ID | VARCHAR (18) | This item stores the recipient the refill authorization request was sent to. This item might be empty if the request was sent directly to a pool or a free text provider. |
| RX_REFILL_REQ_HIP_ID | NUMERIC (18,0) | This item stores the In Basket pool the refill authorization request was sent to. This item might be blank if a request was sent directly to a provider's In Basket or was sent outside the system (through Surescripts or by printing). |
| RX_NUM_LBLS_TO_PRNT | INTEGER | This item tracks the number of fill labels to print for a fill on order entry in Willow Ambulatory. Additional labels may have been reprinted outside of order entry; these reprints are not reflected in the value of this item. |
| RX_LBL_QTY_USR_SP_YN | VARCHAR (1) |  |
| PROD_EXP_DATE | DATETIME | This item tracks the expiration date of the product, which is the date on which the drug needs to be discarded due to spoilage. |
| RX_VRFY_PAT_CSN | NUMERIC (18,2) | This item stores the patient contact CSN that the verification applies to. |
| RX_ACTIVE_PHR_ID | NUMERIC (18,0) | The pharmacy that is currently processing this fill request. |
| RX_WRKFLW_REDIR_CSN | NUMERIC (18,0) | Stores the workflow redirection CSN for billing purposes (cost center routing). |
| CONTINUE_FILL_ON_DC_DTTM | DATETIME (UTC) | This item stores the most recent instant the continuation of the fill on a reordered prescription was approved. |
| FILL_DAY_SUP_THPY | INTEGER | This item stores the number of days that the patient will be taking the medication that was dispensed. |
| FILL_STATUS_INST_DTTM | DATETIME (UTC) | Contains the instant that this order moved to its current status. |
| RX_PART_FILL_PAT_CHARG | NUMERIC (18,3) | Stores the partial fill patient pay amount at the time of dispense, if the partial was reversed after it was dispensed for the rebilling on completion fill. |
| MULTIDOSE_ADMIN_C | INTEGER |  |
| RX_TRANSITION_OVRIDE_STAT_C | INTEGER |  |
| RX_TRANSITION_OVRIDE_RSN_C | INTEGER |  |
| RX_TRANSITION_OVRIDE_CMT | VARCHAR (508) | This item stores a free-text comment explaining why the medication transition was overridden on the fill-level. |
| RX_TRANSITION_OVRIDE_USR_ID | VARCHAR (18) | This item stores the user that overrode the medication transition on a fill-level. |
| RX_TRANSITION_OVRIDE_UTC_DTTM | DATETIME (UTC) | This item stores the Coordinated Universal Time (UTC) instant that the user overrode the medication transition. |
| DO_NOT_FLAG_INV_YN | VARCHAR (1) |  |
| ACCUM_OVER_C | INTEGER |  |
| ACCUM_OVER_USER_ID | VARCHAR (18) | User who overrides the accumulator to use for this fill. |
| CALC_ACCUM_C | INTEGER |  |
| RX_ADV_CAN_REASON_C | INTEGER |  |
| STOCK_LOC_OVR_ID | NUMERIC (18,0) | This column contains the inventory location used for the prescription fill.   This may be manually specified by the user during the prescription filling workflow. |
| RX_DISP_REJECT_RSN_C | INTEGER |  |
| OTH_PAY_COV_AMT | NUMERIC (18,2) | The total dollar amount of any payment from another source including coupons. |
| MEDSYNC_SYNCFILL_YN | VARCHAR (1) |  |
| PAT_PAY_CHA_APPROVE | NUMERIC (18,2) | When the Patient Charge Amount Changed flag is acknowledged by the user, this will store what Patient Charge (ORD 47380) amount they approved. It is used to make sure we don't re-add the flag unless the Patient Charge amount differs from this value. |
| CALC_WASTE_DATE_REAL | VARCHAR (184) | This column contains the charge contact that calculated waste is linked to. It is only populated for calculated waste order contacts. |
| REJECT_REDISPENSE_DATE_REAL | FLOAT | The linked dispense contact that was generated as a result of the initial dispense contact being rejected. |
| RX_ADS_DISP_COMBINED_DATE_REAL | FLOAT | When a previous ADS dispense is combined into a new ADS dispense, on the new ADS dispense this colulumn will store the contact date real of the previous ADS dispense. |
| RX_XFER_HUB_XFER_YN | VARCHAR (1) |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ORDER_ID | ADT_ORDERS_ERRORS | ORDER_ID | No | No | No |  |
| 1 | ORDER_ID | ADT_ORDER_INFORMATION | ORDER_ID | No | No | No |  |
| 1 | ORDER_ID | APPT_REQUEST | REQUEST_ID | No | No | No |  |
| 1 | ORDER_ID | CL_ORD_FST_LST_SCH | ORDER_ID | No | No | No |  |
| 1 | ORDER_ID | DENT_ORD_NOADD | ORDER_ID | No | No | No |  |
| 1 | ORDER_ID | DUPMED_DISMISS_HH_INFO | ORDER_ID | No | No | No |  |
| 1 | ORDER_ID | ENDOSCOPY_METRICS | ORDER_ID | Unknown | No | No |  |
| 1 | ORDER_ID | EXTERNAL_ORDER_INFO | ORDER_ID | No | No | No |  |
| 1 | ORDER_ID | F_IMG_STUDY | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_ID | F_IP_HSP_SUM_ORDER | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_ID | F_LAB_ORDERS | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_ID | F_MU_OBJ_EH_PLACED_ORDER | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_ID | F_MU_OBJ_EH_RESULTD_ORDER | ORDER_PROC_ID | Unknown | Unknown | No |  |
| 1 | ORDER_ID | F_ONC_PRIOR_AUTH_ORDERS | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_ID | F_OPIOID_ORDERS | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_ID | F_RX_ORDER | ORDER_MED_ID | Unknown | Unknown | No |  |
| 1 | ORDER_ID | HH_MED_ORD_IN_POC_DETAIL | ORDER_MED_ID | No | No | No |  |
| 1 | ORDER_ID | HV_ORDER_PROC | ORDER_PROC_ID | Unknown | No | No |  |
| 1 | ORDER_ID | MED_DETAILS_EXT_ORD | ORDER_ID | No | No | No |  |
| 1 | ORDER_ID | MERCHANDISE_ORDER_INFO | ORDER_ID | Yes | No | No |  |
| 1 | ORDER_ID | MU_EH_QRDA_I_ORDER | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_ID | ORDERS | ORDER_ID | No | No | No |  |
| 1 | ORDER_ID | ORDER_AUTH_INFO | ORDER_ID | No | No | No |  |
| 1 | ORDER_ID | ORDER_MED | ORDER_MED_ID | Unknown | No | No |  |
| 1 | ORDER_ID | ORDER_MEDINFO | ORDER_MED_ID | Unknown | No | No |  |
| 1 | ORDER_ID | ORDER_MED_2 | ORDER_ID | Unknown | No | No |  |
| 1 | ORDER_ID | ORDER_MED_3 | ORDER_ID | Unknown | No | No |  |
| 1 | ORDER_ID | ORDER_MED_4 | ORDER_ID | Unknown | No | No |  |
| 1 | ORDER_ID | ORDER_MED_5 | ORDER_ID | Unknown | No | No |  |
| 1 | ORDER_ID | ORDER_MED_6 | ORDER_MED_ID | Unknown | No | No |  |

_(620 total; showing first 30)_
