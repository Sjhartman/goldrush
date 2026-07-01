# ORDER_METRICS

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=ORDER_METRICS

## Description

This table is designed to extract the information necessary to determine where and how orders are being placed in the system. It can also give an indication of what percentage of orders are being placed in the system where the ordering provider is the same as the ordering user. It also details what type of orders and if the orders were modified and/or reordered. Included orders are parent orders; not pended; not created from an interface; not created by an Instant Order OurPractice Advisory action; not a cabinet override; not a historical order; not a bulk dispense order; not created by referral; not external; and either have a procedure associated or do not have an appointment request system status.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | ORD |
| Release Version | Summer 2009 |
| May contain EHI? | No |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| ORDER_ID | NUMERIC (18,0) | The unique order ID. |
| AUTH_PROV_ID | VARCHAR (18) | The ID of the order's authorizing provider. |
| ORDERING_PROV_ID | VARCHAR (18) | The ID of the order's ordering provider. |
| ORDERING_USER_ID | No | The EMP ID (.1) of the user who signed or signed and held the order. |
| CPOE_YN | No | Indicates whether the ordering provider is the same as the ordering user. |
| LGQ_ORDERSET_ID *(deprecated)* | NUMERIC (18,0) | The ID, if any, of the Order Set used to place the order. This will only populate for Order Sets from the LGQ INI. NOTE: LGQ Order Sets were retired in '08, so this column is deprecated. |
| USER_OVERRIDE_YN | No | Indicates whether there was a user override for this order template at the time of the order. |
| REORDERED_YN | No | Indicates whether this order is a reorder of an existing order. |
| MODIFIED_YN | No | Indicates whether this order is the modification of an existing order. |
| ORDER_MODE | VARCHAR (254) | The order mode specified when placing the order. |
| ORD_VRB_MSGSENT_YN | VARCHAR (1) | Indicates whether a verbal message was sent for the order. |
| ORD_COS_MSGSENT_YN | VARCHAR (1) | Indicates whether a cosign message was sent for the order. |
| DISCONTINUE_MODE | VARCHAR (254) | The order mode specified when discontinuing the order. |
| DSC_VRB_MSGSENT_YN | VARCHAR (1) | If the order has been discontinued, indicates whether a verbal message was sent when discontinuing the order. |
| DSC_COS_MSGSENT_YN | VARCHAR (1) | If the order has been discontinued, indicates whether a cosign message was sent when discontinuing the order. |
| ORDER_SOURCE_C | INTEGER |  |
| PRL_ORDERSET_ID | NUMERIC (18,0) | The ID, if any, of the Order Set used to place the order. This will only populate for Order Sets from the PRL INI. |
| FIRST_VERIFY_CDR | No | This is the CONTACT_DATE_REAL of the first Verify contact for the order (the first contact in ORDER_DISP_INFO with ORD_CNTCT_TYPE_C=4). This contact will be created when the order is autoverified from Order Entry or verified from Verify Orders. The contact date real is a unique, internal contact date in decimal format. The integer portion of the number indicates the date of the contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| FIRST_DISPENSE_CDR | No | This is the CONTACT_DATE_REAL of the first Dispense contact for the order (the first contact in ORDER_DISP_INFO with ORD_CNTCT_TYPE_C=5). This contact will be created when the order is dispensed by Willow. The contact date real is a unique, internal contact date in decimal format. The integer portion of the number indicates the date of the contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| ORD_WORKSTATION_ID | VARCHAR (18) | The unique ID associated with the ordering workstation record on which this order was first signed. For most orders, this is ORD 80, but for sign+held orders, this comes from ORD 34430. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| ORDER_DTTM | DATETIME (Local) | The date and time the order was created. |
| ACKNOWLEDGE_DTTM | DATETIME (Local) | The date and time the order was first acknowledged. |
| SESSION_KEY | VARCHAR (254) | The session key of this order. When a group of orders are signed simultaneously, they share a session key value. |
| CSGN_TURNAROUND_SEC *(deprecated)* | INTEGER | In table ORDER_METRICS, the column CSGN_TURNAROUND_SEC (ORD/34869) has been deprecated.   This column's data was not trustworthy, since it did not account for situations where an order required multiple signatures (e.g. a verbal order placed by a user who additionally required cosignature).  To determine the amount of time from order signing to cosigning or verbal signature for a medication order, join ORDER_MED.ORDER_MED_ID to ORDER_SIGNED_MED.ORDER_MED_ID and compare the time in ORDER_SIGNED_MED.CSGN_SIGNED_TIME (for cosigns - ORD/34855) or ORDER_SIGNED_MED.VERB_SIGNED_TIME (for verbal signature - ORD/34825) to the time in ORDER_MED.ORDER_INST (ORD/31). Alternately, join ORDER_METRICS.ORDER_ID to ORDER_SIGNED_MED.ORDER_MED_ID and compare against ORDER_METRICS.ORDER_DTTM.  For a procedure order, do the same but change "MED" to "PROC" for all table and column names. |
| ORDER_DESC | VARCHAR (254) | The description of the order. This information is found in the Order field of clinical systems Order Detail window. |
| DISPLAY_NAME | VARCHAR (510) | The name of the medication as it appears on the medication record itself. |
| ORDER_STATUS_C | INTEGER |  |
| PAT_ID | VARCHAR (18) | The unique ID of the patient record for this line. This column is frequently used to link to the PATIENT table. |
| PAT_ENC_CSN_ID | 8 | The unique contact serial number for the patient contact associated with this order. This number is unique across patients and encounters in your system. If you use IntraConnect this is the Unique Contact Identifier (UCI). |
| ACTIVE_ORDER_C | INTEGER |  |
| ORDER_TYPE_C | INTEGER |  |
| ORIGINAL_SESSIONKEY | VARCHAR (20) | The original session in which this order was created.  (In a few cases, this may be earlier than the ORD-455 sessionkey if you pend an order set, then add an order to it after unpending.)  Used by discontinue logic for locating all related orders, even if they are not all signed at the same time. |
| MU_CPOE_YN | No | *** Deprecated *** The deprecated table's content/data is no longer populated in Chronicles and is no longer available.   Indicates whether this order meets the criteria for CPOE as defined in Meaningful Use Stage 1.  The exact criteria that are used depend on the Meaningful Use CPOE criteria setting in System Definitions (I LSD 20030): If the selected setting is 1-Providers Check/Ordering Mode, an order meets the CPOE criteria if either of the following is true: - The ordering provider (for outpatent orders, the authorizing provider) is the same as the entering user; or - The ordering mode used when placing the order is included in the Order Modes to Include setting in System Definitions (I LSD 20010). If the selected setting is 2-Entering Provider Licence, an order meets the CPOE criteria if either of the following is true: - The entering user has the Meaningful Use CPOE User? flag set to Yes (I EMP 17930); or - The entering user has the Meaningful Use CPOE User? flag left blank, and the entering provider's license is included in the License Types to Include setting in System Definitions (I LSD 20000).  Note that the Objective Measures in Chronicles logic used for determining whether orders meet Meaningful Use CPOE criteria (both Stage 1 and Stage 2) is slightly different from what is described above, and so the value in this column can only be used reliably for checking an order's CPOE status for Stage 1 Meaningful Use in Clarity. |
| PAT_LOC_ID | NUMERIC (18,0) | The unique ID of the department that the patient was in at the time this order was signed. This column is frequently used to link to the CLARITY_DEP table. |
| DEST_DEPT_OVRIDE_YN | VARCHAR (1) |  |
| ORIG_AUTH_PROV_ID | VARCHAR (18) | This will hold the SER ID of the authorizing provider at the time the order was signed or sign & held. |
| ORIG_ORD_PROV_ID | VARCHAR (18) | This will hold the SER ID of the ordering provider at the time the order was signed or sign & held. |
| CANC_DEPT_OVRIDE_YN | VARCHAR (1) |  |
| PREFERENCE_LIST_TYPE_C | VARCHAR (66) |  |
| DISCON_LOC_DTTM | DATETIME (Local) | The instant the order was discontinued or canceled in the system's local timezone |
| SPECIMEN_RECV_DATE | DATETIME | The date the specimen for this order was received |
| FIRST_FINAL_LOC_DTTM | DATETIME (Local) | The instant final results were first made available on the chart. This is the result contact instant (ORD-1970) from the first contact where the procedure result status (ORD-115) is 3-Final result. |
| PARENT_CE_ORDER_ID | NUMERIC (18,0) | When a cross-encounter order is released, this item stores the ID of the parent order. |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| B-TREE INDEX | EIX_ORDER_METRICS_ORDER_DTTM | ORDER_DTTM | 1 | Yes | Yes |  |

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

_(399 total; showing first 30)_
