# ORDER_MED_2

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=ORDER_MED_2

## Description

This table enables you to report on medications ordered in EpicCare or Ambulatory Pharmacy (Prescriptions). This table should be used with ORDER_MED.

**Overflow table** for ORDER_MED (139 cols). Contains additional columns for the same records — join on the shared primary key column.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | ORD |
| Release Version | SPRING 2008 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| ORDER_ID | NUMERIC (18,0) | The unique ID of the order record associated with this medication order. This is an internal unique identifier for order records in this table and cannot be used to link to CLARITY_MEDICATION. |
| CM_PHY_OWNER_ID | VARCHAR (25) | ID of the physical deployment owner for this record. Physical owners will be where the data is hosted, either on the cross-over server or the owner deployment. |
| CM_LOG_OWNER_ID | VARCHAR (25) | ID of the logical deployment owner for this record. Logical owners show the deployment where the record was created but doesn't represent if the record is a part of version skew. |
| TXT_AUTHPROV_NAME | VARCHAR (192) | In ambulatory pharmacy, a prescription order could be authorized by a non-EpicCare provider. There is no provider record for this provider. This is used to store the non-EpicCare provider's name. |
| TXT_AUTHPROV_DEA | VARCHAR (192) | In ambulatory pharmacy, a prescription order could be authorized by a non-EpicCare provider. There is no provider record for this provider. This is used to store the non-EpicCare provider's Dynamic Epic Advisory Database (DEA) number. |
| TXT_AUTHPROV_PHONE | VARCHAR (254) | In ambulatory pharmacy, a prescription order could be authorized by a non-EpicCare provider. There is no provider record for this provider. This is used to store the non-EpicCare provider's phone number. |
| TXT_AUTHPROV_FAX | VARCHAR (254) | In ambulatory pharmacy, a prescription order could be authorized by a non-EpicCare provider. There is no provider record for this provider. This is used to store the non-EpicCare provider's fax number. |
| TXT_AUTHPROV_STREET | VARCHAR (254) | In ambulatory pharmacy, a prescription order could be authorized by a non-EpicCare provider. There is no provider record for this provider. This is used to store the non-EpicCare provider's street address information. |
| TXT_AUTHPROV_CITY | VARCHAR (254) | In ambulatory pharmacy, a prescription order could be authorized by a non-EpicCare provider. There is no provider record for this provider. This is used to store the non-EpicCare provider's city. |
| TXT_AUTHPROV_STAT_C | VARCHAR (66) |  |
| TXT_AUTHPROV_ZIP | VARCHAR (254) | In ambulatory pharmacy, a prescription order could be authorized by a non-EpicCare provider. There is no provider record for this provider. This is used to store the non-EpicCare provider's zip code. |
| RX_NUM_RAW_PHARMACY *(deprecated)* | VARCHAR (192) | The column is deprecated and does not extract any data. Instead of using this column, use recent values of Clarity columns RX_NUM_UNFMTTED_HX and DISPENSE_PHR_ID in Clarity table ORDER_DISP_INFO to get the current unformatted prescription number and dispensing pharmacy. |
| RX_NUM_FORMATTED | VARCHAR (184) | The formatted prescription number for the order. |
| RX_COMMENTS | VARCHAR (1000) | In an ambulatory pharmacy, the person who enters the prescription into the system can add additional comments to the prescription. The comments are not part of the order and are used for pharmacy internal communication only. The comments do not affect the patient instructions, nor the dispense information. |
| RX_WRITTEN_DATE | DATETIME | Store the prescription written date, which is the date the prescription was entered into the system through EpicCare, or the date the prescription was written to the paper prescription. |
| COSIGNER_MSG_ID *(deprecated)* | VARCHAR (18) | This column is no longer used.  Refer to tables ORDER_SIGNED_MED and ORDER_SIGNED_PROC for cosign information.  The deprecated column's content/data is no longer available since it is no longer populated in Chronicles. |
| MED_DISCONT_ENC *(deprecated)* | NUMERIC (18,2) |  |
| EFQ_OVRD_DAY_TYPE | NUMERIC (18,0) | Specifies what the numeric values in the frequency override days columns represent. If it is 1 then the listed days are relative days. If it is 2 then the listed days are weekdays. Any other value has no meaning. |
| EFQ_OVRD_CYCL_LEN | NUMERIC (18,0) | If there is a frequency override specified, this item will contain the length of a relative specified type cycle. For all other specified types this value will be ignored (and should be empty). |
| CHART_CORRECTION_ID | NUMERIC (18,0) | For chart corrections, links the order to a Chart Correction Audit (CCA) record. |
| PARENT_CE_ORDER_ID | NUMERIC (18,0) | When a cross-encounter order is released, this item stores the ID of the parent order. |
| TPL_WT_SRC_C | INTEGER |  |
| OVERRIDE_LINKED_C | INTEGER |  |
| CONDITIONAL_C | INTEGER |  |
| COND_STATUS_C | INTEGER |  |
| PENDED_PREV_SIG *(deprecated)* | VARCHAR (450) |  |
| INITIATED_TIME | DATETIME (Local) | Stores the instant when an inpatient conditional order was initiated. |
| INITIATING_USER_ID | VARCHAR (18) | Stores the user ID for the user who initiated an inpatient conditional order. |
| PEND_REF_REAS_COMM | No | Extracts the comment attached to the pend refusal reason (I ORD 7706) |
| IS_SAVED_ORDER_YN | VARCHAR (1) |  |
| SOURCE_OF_PRI_INS_C | INTEGER |  |
| PRIORITIZED_INST_TM | DATETIME (Local) | The time and date that is used as the prioritized date. |
| ORDER_QUESN_LIST | VARCHAR (1024) | The order specific questions that are listed in the order composer for the order. |
| EXT_PHARM_MED_NAME | VARCHAR (254) | Medication display name received from an external pharmacy. |
| SIG_BEFOREEDIT *(deprecated)* | VARCHAR (450) |  |
| ORD_OSQ_ID | NUMERIC (18,0) | The unique ID of the Orderable OSQ that this order was created from. |
| ORD_OSQ_DATE | VARCHAR (254) | The date corresponding to the version of the parent Orderable OSQ used to place this order. |
| ORD_OSQ_OV_CTX | VARCHAR (254) | A descriptor that can be used to identify the override record used for the parent Orderable OSQ. |
| ORD_OSQ_ORDER_SRC_C | INTEGER |  |
| PEND_MED_ACTIVE_YN | VARCHAR (1) |  |
| PEND_PREV_ORD_ID | VARCHAR (254) | The previous order ID for the pending medication. This item is NOT networked to orders. |
| RX_DEFERRED_YN *(deprecated)* | VARCHAR (1) |  |
| TXT_AUTHPROV_NPI | VARCHAR (254) | If the authorizing provider for a medication is not currently an Epic provider (no SER record for this provider), free text provider items are used to save information about this provider. This item stores the National Provider ID (NPI) of the provider. |
| TXT_AUTHPROV_ST_ID *(deprecated)* | VARCHAR (508) | In table ORDER_MED_2, the column TXT_AUTHPROV_ST_ID (ORD/1107) has been deprecated.  This column has been replaced by column TXT_AUTHPROV_OTH_ID (ORD/1107) in table TXT_AUTHPR_OTH_IDS.  To look up the deprecated columns' value after the Clarity Compass upgrade, join column TXT_AUTHPR_OTH_IDS.TXT_AUTHPROV_OTH_ID to table ORDER_MED_2 column TXT_AUTHPROV_ST_ID. |
| ORD_TRANS_METHOD_C | INTEGER |  |
| PROFILE_ONLY_RX_YN | VARCHAR (1) |  |
| DISP_QTY_REM | NUMERIC (18,2) | Stores the remaining authorized quantity (in Written Dispense Quantity unit) that the pharmacist can dispense. It is used in Ambulatory Pharmacy to calculate the Refills Remaining. |
| FREQ_UNSCHEDULED_C | INTEGER |  |
| DURATION | INTEGER | Duration for this medication. |
| FREQUENCY *(deprecated)* | VARCHAR (254) |  |
| INTERVENTION | VARCHAR (254) | Intervention for this medication. |
| SUMM_UPDATE_DTTM | DATETIME (Local) | Instant that the summary sentence was generated for a signed order. |
| NEEDS_TRANSMITTAL_C | INTEGER |  |
| LAST_SUSPEND_DTTM | DATETIME (Local) | Instant this medication was last suspended. |
| COMM_ORD_STATUS_C | INTEGER |  |
| NEEDS_CHARGE_DROP_C | INTEGER |  |
| ORD_TRANSMTL_COM_YN | VARCHAR (1) |  |
| SS_PRL_ORD_SRC_C | INTEGER |  |
| CROSS_ENC_ORD_C | INTEGER |  |
| SIGN_ACTION_PEND_C | INTEGER |  |
| ORIG_MED_ID | NUMERIC (18,0) | Original prescription column; contains the medication order medication ID. |
| ORIG_STRENGTH | VARCHAR (254) | Original prescription column; contains the medication order strength. |
| ORIG_ROUTE_C | INTEGER |  |
| ORIG_MED_SOURCE_C | INTEGER |  |
| ORIG_DIS_DISP_QTY | NUMERIC (18,4) | Original prescription column; contains the medication order discrete dispense quantity. |
| ORIG_DISP_UNIT_C | INTEGER |  |
| ORIG_START_DATE | DATETIME | Original prescription column; contains the medication order start date. |
| ORIG_END_DATE | DATETIME | Original prescription column; contains the medication order end date. |
| ORIG_DAW_YN | VARCHAR (1) |  |
| PENDDC_STATUS_C | INTEGER |  |
| MED_DISC_REFILLS | INTEGER | Saves the discrete medication refills information for the order. |
| BACK_DATED_YN | VARCHAR (1) |  |
| RX_CLINICALLY_RV_YN | VARCHAR (1) |  |
| PRIORITIZED_UTC_DTTM | DATETIME (UTC) | Stores the prioritized instant for the result in UTC |
| MEDICATION_PLL_IDENT | VARCHAR (50) | Stores the PLL-ID of a prescription in Norway, to track the Treatment group the prescription belongs to. |

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
| 1 | ORDER_ID | ORDER_MED_3 | ORDER_ID | Unknown | No | No |  |
| 1 | ORDER_ID | ORDER_MED_4 | ORDER_ID | Unknown | No | No |  |
| 1 | ORDER_ID | ORDER_MED_5 | ORDER_ID | Unknown | No | No |  |
| 1 | ORDER_ID | ORDER_MED_6 | ORDER_MED_ID | Unknown | No | No |  |
| 1 | ORDER_ID | ORDER_MED_7 | ORDER_ID | No | No | No |  |

_(203 total; showing first 30)_
