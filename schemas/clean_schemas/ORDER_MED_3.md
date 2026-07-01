# ORDER_MED_3

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=ORDER_MED_3

## Description

This table enables you to report on medications ordered. This table should be used with ORDER_MED.

**Overflow table** for ORDER_MED (139 cols). Contains additional columns for the same records — join on the shared primary key column.

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
| ORDER_ID | NUMERIC (18,0) | The unique identifier for the order record. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| ORIG_RX_DOSAGE | VARCHAR (254) | Original prescription column; contains the medication order dosage. |
| ORIG_RX_QUANTITY | VARCHAR (50) | Original prescription column; contains the medication order quantity. |
| ORIG_RX_REFILLS | VARCHAR (254) | Original prescription column; contains the medication refills. |
| ORIG_RX_DIRECTIONS | VARCHAR (1000) | Original prescription column; contains the medication directions. |
| ORIG_RX_PRE_PROV_ID | VARCHAR (18) | Original prescription column; contains the medication order prescriber ID. |
| ORIG_RX_COMMENTS | VARCHAR (450) | Original prescription column; contains the medication comments. |
| ORD_PATHWAY_GRP_ID | NUMERIC (18,0) | The unique ID of the orderable OSQ's Pathway group record that contains this record. |
| ORD_PATHWAY_GRP_CSN | NUMERIC (18,0) | The CSN of the contact of orderable OSQ's Pathway group record that contains this record. |
| VANCO_ADMIN_C | INTEGER |  |
| INSTANT_MET_DTTM | DATETIME (Local) | Stores the instant when the condition was marked as "met/satisfied" (ORD-1401) for an inpatient conditional order. |
| PRESCRIP_EXP_DATE | DATETIME | Contains the expiration date for the prescription. |
| PRESC_ORIGIN_CODE_C *(deprecated)* | INTEGER |  |
| PENDED_PREV_DISP | VARCHAR (50) | For a pended medication order, this holds the contents (if any) of the "Previous dispense" display item from the order composer. |
| ORD_AUC | NUMERIC (18,2) | Item to store the area under curve value for medications using this value in dose calculation. |
| ORD_SEL_TARGETAUC_C | INTEGER |  |
| ORIG_RX_PHRM_ID | NUMERIC (18,0) | Original prescription column; contains the pharmacy |
| ORD_PHASE_OF_CARE_C | INTEGER |  |
| ORIGINAL_MED_ID | NUMERIC (18,0) | The unique ID of the medication that determines the formulary status of the order at order entry. The formulary status of this medication at the time of ordering is found in the column ORDER_MED.NON_FORMULARY_YN. For Intelligent Medication Selection (IMS) cases, it will be the medication picked by the user before IMS changes the medication. This is only set for inpatient medication orders.  It is recommended to use the Clarity column ORDER_MEDINFO.DISPENSABLE_MED_ID when reporting on medication orders. Use ORIGINAL_MED_ID for reporting on the formulary status of medications chosen by ordering users. |
| AR_INTERFACE_STAT_C | INTEGER |  |
| INTERACT_COMMENT | VARCHAR (254) | Interaction override comment. |
| COPY_POINTER_ID | NUMERIC (18,0) | This object tracks order (ORD) record links created when using the inpatient or ambulatory order mover utilities to move an ORD record. This item is populated on the source ORD record and points to the target ORD record(s) created. |
| CONDITION_FLAG | INTEGER | This column contains the Condition Flag for an order. |
| WORKSTN_OVERRIDE_ID | VARCHAR (18) | This item stores the override workstation ID (LWS .1). |
| PRINT_LOCAL_COPY_YN | VARCHAR (1) |  |
| ORX_ID | NUMERIC (18,0) | This column contains the record ID from the Order Lookup Index (ORX).  The ORX contains records for all active medication records and procedure records. This may be populated if an order originates from an Order Panel. |
| SOFT_DEL_FLAG | VARCHAR (254) | Soft deletion flag for ORD records associated with order-based transcriptions, which were deleted by the transcription soft-deletion utility. |
| SELECTED_FOR_OPC_YN | VARCHAR (1) |  |
| MEDS_RESYME_REASO_C | INTEGER |  |
| MEDS_DC_REASON_C | INTEGER |  |
| IP_INCLUDE_NOW_C | INTEGER |  |
| IP_INCL_NOW_SCH_C | INTEGER |  |
| IP_NUM_BACKDATED | INTEGER | Number of back-dated doses eliminated for med orders |
| LAST_SCHED_DATE | DATETIME | The last scheduled date of the order. |
| COSIGN_REQUIRED | VARCHAR (5) | Cosign required flag for the order. |
| VERBAL_REQ_COSIGN | VARCHAR (5) | Flag to tell if it is a verbal order waiting for a cosign. |
| MEDS_ACTION_VERB_C | INTEGER |  |
| MED_SOURCE_C | INTEGER |  |
| CRCL_FORMULA_ID | NUMERIC (18,0) | The creatinine clearance  CrCl programming point that will be used for AUC calculations for order whose dose calculation programming point does not specify a CrCl programming point. |
| AFTER_ORDER_ID | NUMERIC (18,0) | This column contains the After Order ID for an order. |
| BEFORE_ORDER_ID | NUMERIC (18,0) | This column contains the Before Order ID for an order. |
| DIET_COMMENTS | VARCHAR (508) | This column contains the Diet Comments entered for an order. |
| END_DT_BEF_FILL_DT | DATETIME | Stores the order's end date before it was changed due to the order being (re)filled. This is needed so that if the fills are ever cancelled, we know what to set the end date back to. |
| ADJUST_SIG_YN | VARCHAR (1) |  |
| PREV_POC_C | INTEGER |  |
| ORDER_TIME | 29 | The date and time when the medication order was placed. |
| REC_ARCHIVED_YN | No | Indicates whether the Medication Order record is archived at the record level. |
| IS_HELD_ORDER_C | INTEGER |  |
| TXT_ORDPROV_NAME | VARCHAR (192) | The name of the ordering provider, for providers that do not yet exist in the Provider (SER) master file. |
| TXT_ORDPROV_DEA | VARCHAR (192) | The DEA number of the ordering provider, for providers that do not yet exist in the Provider (SER) master file. A DEA number is given to providers by the Drug Enforcement Administration and allows them to prescribe controlled substances. |
| TXT_ORDPROV_NPI | VARCHAR (192) | The National Provider Identifier (NPI) of the ordering provider, for providers that do not yet exist in the Provider (SER) master file. |
| TXT_ORDPROV_PHONE | VARCHAR (254) | The phone number of the ordering provider, for providers that do not yet exist in the Provider (SER) master file. |
| TXT_ORDPROV_FAX | VARCHAR (254) | The fax number of the ordering provider, for providers that do not yet exist in the Provider (SER) master file. |
| TXT_ORDPROV_STREET | VARCHAR (254) | The street address of the ordering provider, for providers that do not yet exist in the Provider (SER) master file. |
| TXT_ORDPROV_CITY | VARCHAR (254) | The city of the ordering provider, for providers that do not yet exist in the Provider (SER) master file. |
| TXT_ORDPROV_STATE_C | VARCHAR (66) |  |
| TXT_ORDPROV_ZIP | VARCHAR (254) | The zip code of the ordering provider, for providers that do not yet exist in the Provider (SER) master file. |
| RX_SERIAL_NUMBER | VARCHAR (256) | Stores the prescription serial number commonly found on triplicate prescription forms. Triplicate prescription forms are used for controlled substances and require multiple copies of the prescription form. |
| NOCHRG_EXT_RSLT_YN | VARCHAR (1) |  |
| WT_MAX_DOSE | NUMERIC (18,4) | This column returns the saved weight-based or body surface area (BSA)-based maximum dose for the order (ORD). |
| WT_MAX_DOSE_UNIT_C | INTEGER |  |
| MAX_DOSE_SOURCE_C | INTEGER |  |
| SRC_RX_MED_ID | NUMERIC (18,0) | The ID of the originally prescribed medication as returned by the pharmacy in a refill request. |
| SRC_RX_QUANTITY | VARCHAR (254) | The quantity of the originally prescribed medication as returned by the pharmacy in a refill request. |
| SRC_RX_DIS_DISP_QTY | NUMERIC (18,4) | The discrete dispense quantity of the originally prescribed medication as returned by the pharmacy in a refill request. |
| SRC_RX_DISP_UNIT_C | INTEGER |  |
| SRC_RX_REFILLS | VARCHAR (50) | The number of refills of the originally prescribed medication as returned by the pharmacy in a refill request. |
| SRC_RX_DIRECTIONS | VARCHAR (3500) | The directions (patient sig) of the originally prescribed medication as returned by the pharmacy in a refill request. |
| SRC_RX_START_DATE | DATETIME | The start date of the originally prescribed medication as returned by the pharmacy in a refill request. |
| SRC_RX_END_DATE | DATETIME | The end date of the originally prescribed medication as returned by the pharmacy in a refill request. |
| SRC_RX_DAW_YN | VARCHAR (1) |  |
| SRC_RX_PRES_PROV_ID | VARCHAR (18) | The ID of the prescribing provider of the originally prescribed medication as returned by the pharmacy in a refill request. |
| SRC_RX_COMMENTS | VARCHAR (450) | The comments associated with the originally prescribed medication as returned by the pharmacy in a refill request. |
| PAT_SIG_REPLY_C | INTEGER |  |
| SIG_REVIEW_USER_ID | VARCHAR (18) | Holds the user ID of the user who reviewed the patient sig for accuracy. The sig is the description of how a medication is supposed to be administered which includes the dose and frequency. |
| SIG_REVIEW_INS_DTTM | DATETIME (Local) | Holds the instant that the user took action on the patient sig in previous sig workflows. The sig is the description of how a medication is supposed to be administered which includes the dose and frequency. |
| SRC_RX_WRITTEN_DATE | DATETIME | The written date of the originally prescribed medication as returned by the pharmacy in a refill request. |
| DOSE_RND_ACK_RSN_C | INTEGER |  |
| SRC_RX_DESC | VARCHAR (254) | The description of the originally prescribed medication as returned by the pharmacy in a refill request. |
| EPRES_DEST_C | INTEGER |  |
| CTRL_MED_YN | VARCHAR (1) |  |
| RX_DIGITAL_SIG | VARCHAR (1000) | Pharmacy cryptographic signature of controlled med summary |
| RX_DIG_SIG_INS_DTTM | DATETIME (UTC) | Instant that pharmacy digitally signed the order. |
| DEA_NUM_MED_AUTH | VARCHAR (192) | The DEA number of the medication authorizing provider |
| OT_EPRES_FAILED_YN *(deprecated)* | VARCHAR (1) |  |

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
| 1 | ORDER_ID | ORDER_MED_4 | ORDER_ID | Unknown | No | No |  |
| 1 | ORDER_ID | ORDER_MED_5 | ORDER_ID | Unknown | No | No |  |
| 1 | ORDER_ID | ORDER_MED_6 | ORDER_MED_ID | Unknown | No | No |  |
| 1 | ORDER_ID | ORDER_MED_7 | ORDER_ID | No | No | No |  |

_(395 total; showing first 30)_
