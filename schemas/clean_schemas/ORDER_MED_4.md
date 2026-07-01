# ORDER_MED_4

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=ORDER_MED_4

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
| Release Version | Rel 2012 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| ORDER_ID | NUMERIC (18,0) | The unique identifier for the order record. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| E_PRES_PAT_NAME | VARCHAR (192) | This item holds the name of the patient this order is signed to. |
| E_PRES_PAT_ADDR | VARCHAR (192) | This item holds the address of the patient the order is signed to. |
| E_PRES_EARLIEST_DAT | DATETIME | This column stores the earliest date on which a prescription can be filled for a Schedule II controlled medication. The date must occur on or before the start date for the prescription. It can't be changed after the order is signed. |
| E_PRES_DEA_CODE_C | INTEGER |  |
| TWO_FACT_AUTH_DTTM | DATETIME (UTC) | Instant that two-factor authentication was completed for the order. |
| CTRL_SUM_SENT_ORDER | VARCHAR (508) | Holds the summary sentence order displayed during the controlled medication review. |
| CRYPT_STAT_C | INTEGER |  |
| CTRL_MED_SUM_CRYPT | VARCHAR (1000) | CRYPTOGRAPHIC SIGNATURE of CONTROLLED MED SUMMARY |
| EPCS_OTX_STATUS_C | INTEGER |  |
| E_PRES_PROV_SSN | VARCHAR (11) | The Social Security Number of the provider who signed the EPCS order, if they are using their SSN to sign orders. |
| OT_EPRES_FAILED_YN | VARCHAR (1) |  |
| ORDER_CONTEXT_ID | NUMERIC (18,0) | The unique identifier of the order context record associated with the order, which contains additional information about when the order is intended to be used. |
| PREV_ORD_CONTEXT_ID | NUMERIC (18,0) | The unique identifier of the order context record associated with the order, which contains additional information about when the order is intended to be used. |
| RX_RELATED_ORD_ID | NUMERIC (18,0) | Set this item to relate a non-clinical order to an existing clinical order. For example, non-clinical orders made via the Bulk Charge activity can be related to an exisiting clinical order by setting the Order ID of the clinical order in this item. The diagnosis and ordering provider information of the clinical order will be copied to the bulk charge order. |
| PARENT_ORDER_ID | NUMERIC (18,0) | The unique ID of the parent order record for Home Health (HH) orders.  An HH order is an order which represents documentation by a user whose scope of practice doesn't include editing prescription data.  Furthermore, the child order created will not be an actual prescription, but merely represents new instructions to the patient regarding how to take a medication. |
| LINKED_OP_MED_ID | NUMERIC (18,0) | The unique ID of the orders record. When Home Health and Hospice clinicians need to document a medication administration against an inpatient medication, a copy of the medication is created with an order mode of inpatient to document the administration. This column holds a link to the original outpatient medication. |
| INTERFACE_STAT_C | INTEGER |  |
| PRESC_ORD_SIG | VARCHAR (3500) | The originally prescribed medication instructions for an order. This will be null if the original  and current medication instructions are identical or if the order is not for a controlled medication that was electronically prescribed. |
| PRESC_ORD_MED_NAME | VARCHAR (700) | The originally prescribed medication name for an order. This will be null if the original medication name and current medication name are identical or if the order is not for a controlled medication that was electronically prescribed. |
| PRESC_ORD_REFILLS | VARCHAR (20) | The originally prescribed refills for an order. This will be null if the original refills and current refills are identical or if the order is not for a controlled medication that was electronically prescribed. |
| PRESC_ORD_QUANTITY | VARCHAR (50) | The originally prescribed quantity for an order. This will be null if the original quantity and current quantity are identical or if the order is not for a controlled medication that was electronically prescribed. |
| TXT_AUTHPROV_EXT_YN | VARCHAR (1) |  |
| TXT_ORDPROV_EXT_YN | VARCHAR (1) |  |
| WAS_FMLY_CHECKED_YN | VARCHAR (1) |  |
| SELECTED_CRCL_SRC_C | INTEGER |  |
| CRCL_ORD_SPEC_VAL | NUMERIC (18,4) | This column stores the creatinine clearance (CrCL) value in the order. |
| SELECTED_SCR_SRC_C | INTEGER |  |
| SCR_ORD_SPEC_VAL | NUMERIC (18,4) | The serum creatinine (sCr) value for the order record. |
| TRANSIG_LANGUAGE_ID | NUMERIC (18,0) | The unique identifier of the language record used for translating patient-facing information in this order record. |
| TRANSIG_AUTO_YN | VARCHAR (1) |  |
| ORIG_DOSE_BEFORE_SWITCH | VARCHAR (254) | The original dose of the medication before the dose was adjusted. |
| ORIG_DOSE_UNIT_BEFORE_SWITCH_C | INTEGER |  |
| WEIGHT_CHANGE_WARNING_TYPE_C | INTEGER |  |
| MAXDOSE_HARDSTOP_YN | VARCHAR (1) |  |
| TXT_AUTHPROV_DIST_C | INTEGER |  |
| TXT_AUTHPROV_CTY_C | VARCHAR (66) |  |
| TXT_AUTHPROV_CTRY_C | VARCHAR (66) |  |
| TXT_ORDPROV_HOUSE | VARCHAR (254) | The house number of the ordering provider for this order record. |
| TXT_ORDPROV_DIST_C | INTEGER |  |
| TXT_ORDPROV_CNTY_C | VARCHAR (66) |  |
| TXT_ORDPROV_CNTRY_C | VARCHAR (66) |  |
| MAX_BSA | NUMERIC (18,5) | The maximum Body Surface Area (BSA) for an order, if the selected BSA is greater than this BSA then the selected BSA will be capped at this value. |
| RX_NUM_UNREAD_MSG | INTEGER | Stores a count of number of unread MAR messages for the order. |
| MAX_DAILY_DOSE | NUMERIC (19,4) | Max daily dose value entered by the provider or defaulted as the calculated daily dose |
| MAX_DLY_DOSE_UNIT_C | INTEGER |  |
| TXT_AUTHPROV_HOUSE | VARCHAR (254) | The house number of the authorizing provider for this order record. |
| RX_ADVANCPREP_MOD_YN | VARCHAR (1) |  |
| UNROUNDED_DOSE_MIN | NUMERIC (19,4) | The unrounded dose of this order. If the dose has a range (e.g. 1-2 mg), this is the lower end of the range. If the dose does not have a range, then this will store the dose. |
| UNROUNDED_DOSE_MAX | NUMERIC (19,4) | The unrounded dose of this order. If the dose has a range (e.g. 1-2 mg), this is the upper end of the range. Otherwise, this is null. |
| UNROUND_DOSE_UNIT_C | INTEGER |  |
| ION_SPEC_AC_AMT | NUMERIC (18,4) | This column shows the amount of acetate that a provider entered in this order record. This column will be empty if a chloride:acetate ratio or maximize option was selected. |
| ION_SPEC_AC_UNIT_C | INTEGER |  |
| ION_MAXIMIZE_C | INTEGER |  |
| ION_RATIO | VARCHAR (12) | This column shows the chloride:acetate ratio option that was selected. This column is empty when a specified acetate amount was entered or when a maximize option was selected. |
| ION_BASED_TPN_YN | VARCHAR (1) |  |
| CALC_CL_AC_RATIO | NUMERIC (18,2) | This column stores the calculated chloride:acetate ratio for an ion-based total parenteral nutrition (TPN). |
| ION_PRI_CALC_AMT_C | INTEGER |  |
| USE_AUC_DOSE_YN | VARCHAR (1) |  |
| ION_OUT_OF_DATE_YN | VARCHAR (1) |  |
| EPRES_PHARMACY_ID | NUMERIC (18,0) | This column stores the ID of the pharmacy that accepted the prescription. |
| EPRES_PHARMACIST_ID | VARCHAR (18) | This column stores the ID of the pharmacist or pharmacy technician who accepted the prescription. |
| RX_ACCEPT_DTTM | DATETIME (Local) | Stores the instant at which the prescription was accepted. |
| RPTSIG_EXISTS_YN | VARCHAR (1) |  |
| HOLD_PENDING_PA_YN | VARCHAR (1) |  |
| SEND_PA_REQ_YN | VARCHAR (1) |  |
| PA_ORG_ID | NUMERIC (18,0) | The unique ID of the data exchange organization associated with the order record, which specifies the payer that a prior authorization request should be sent to when a medication order is signed. |
| SCRIPT_SUP_ID | VARCHAR (18) | The unique identifier of the provider under whose supervision a prescription was placed. |
| REORDER_AUTOLINK_C | INTEGER |  |
| RX_ORIG_COMP_NAME | VARCHAR (254) | This item saves the original composed name for an order after its name is edited by end users. |
| ONE_STEP_MEDPROC_ID | NUMERIC (18,0) | The unique ID of the order record. This item points to a procedure order record for the procedure used to administer the medication. The item is populated when administering a medication that is documented as administered in an Ophthalmology or Orthopedic context. |
| SPEC_DOSE_LMT_HR | INTEGER | The number of hours the dosing limit represents. |
| SPEC_MED_TYPE_C | INTEGER |  |
| BULK_CHG_FRM_FILE_YN | VARCHAR (1) |  |
| BEN_TYP_C | INTEGER |  |
| BEN_AUTH_TYP_C | INTEGER |  |
| BEN_AUTH_CODE | VARCHAR (30) | A string representing the benefit authorization code for the order. Certain codes allow different amounts for dispense/refill amounts. |
| BEN_ALL_REFIL_YN | VARCHAR (1) |  |
| RX_VALID_NUM | VARCHAR (30) | A prescription validation number for the order. |
| RX_TRANSITION_ID | NUMERIC (18,0) | The unique identifier for the patient follow-up tracking record, which stores information about how a patient is transitioning from one medication to another. |
| RX_TRANSITION_STAT_C | INTEGER |  |
| RX_TRANSITION_STAT_RSN_C | INTEGER |  |
| RX_TRANSITION_STAT_CMT | VARCHAR (508) | This item stores any additional comments about why the medication transition status was changed. |
| RX_TRANSITION_STAT_USR_ID | VARCHAR (18) | The unique identifier of the user who changed the transition status of the medication. |
| RX_TRANSITION_STAT_UTC_DTTM | DATETIME (UTC) | The date and time the medication transition status of the order was changed. |
| PERMISSION_DRUG_C | INTEGER |  |
| MEDSYNC_IS_SYNCED_YN | VARCHAR (1) |  |
| DISCON_LOCAL_TIME | DATETIME (Local) | This item stores the instant in the patient's local time zone that an order was discontinued. |
| RX_REQUEST_TYPE_C | INTEGER |  |
| IS_SRC_ORD_REC_YN | VARCHAR (1) |  |
| DISC_WAIT_PA_YN | VARCHAR (1) |  |
| MEDICAL_COND_ID | NUMERIC (18,0) | Contains the billing indication selected on order signing. This is used by Dutch community members for proper billing of their "add-on" medications. In particular, it's used to determine if the NDC being billed is entitled or not. |
| EXT_DFLT_DOSE | VARCHAR (254) | Stores a default dose amount from an external source passed in via Active Guidelines, to allow for later comparison between this default dose and the actual dose in the order. |
| EXT_DFLT_DOSE_UNIT | VARCHAR (254) | Stores a default dose unit from an external source passed in via Active Guidelines, to allow for later comparison between this default dose and the actual dose in the order. |
| EXT_DFLT_FREQ | VARCHAR (254) | Stores a default frequency name from an external source passed in via Active Guidelines, to allow for later comparison between this default and the actual value in the order. |
| EXT_DFLT_PRIOR | VARCHAR (254) | Stores a default priority from an external source passed in via Active Guidelines, to allow for later comparison between this default and the actual value in the order. |
| EXT_DFTL_ROUTE | VARCHAR (254) | Stores a default route from an external source passed in via Active Guidelines, to allow for later comparison between this default and the actual value in the order. |
| ERX_ORD_NAME | VARCHAR (700) | The name of an order that was electronically prescribed. |

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
| 1 | ORDER_ID | ORDER_MED_5 | ORDER_ID | Unknown | No | No |  |
| 1 | ORDER_ID | ORDER_MED_6 | ORDER_MED_ID | Unknown | No | No |  |
| 1 | ORDER_ID | ORDER_MED_7 | ORDER_ID | No | No | No |  |

_(482 total; showing first 30)_
