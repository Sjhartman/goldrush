# IP_ORDER_REC

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=IP_ORDER_REC

## Description

This table contains Inpatient order reconciliation information.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | IEV |
| Release Version | SPRING 2008 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| EVENT_ID | VARCHAR (18) | The unique ID of the event record. |
| LINE | No | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| RECON_ORD_ID | NUMERIC (18,0) | The unique ID of the order that is associated with this event. |
| EVENT_LINE_NUM | NUMERIC (18,0) | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| REC_ACTION_C | INTEGER |  |
| REC_REORDER_ID | NUMERIC (18,0) | The unique ID of the order that is associated with this reorder reconciliation event. |
| REC_COMMENT | VARCHAR (254) | Stores a comment relating to the reconciliation action taken on the order. |
| REC_LAST_DOSE_C | INTEGER |  |
| DISCONTINUE_RSN_C | INTEGER |  |
| RESUME_REASON_C | INTEGER |  |
| STOP_TAKING_RSN_C *(deprecated)* | INTEGER |  |
| REMOVE_REASON_C | INTEGER |  |
| CANCEL_REASON_C | VARCHAR (66) |  |
| REC_LAST_DOSE_TIME | VARCHAR (254) | The time when the last dose was given for a prior-to-arrival (PTA) medication. |
| SUSPEND_RSN_C | INTEGER |  |
| TAKING_BEF_ADM_C | INTEGER |  |
| ORDREC_SORT_POC_C | INTEGER |  |
| IP_ORDREC_REV_HRS | FLOAT | The number of hours after a completed transfer event that the review not needed status for One Step Order Reconciliation orders is valid. |
| IP_ORDREC_REV_EXP_DTTM | DATETIME (UTC) | The time at which the review not needed status for One Step Order Reconciliation orders expires. |
| DISCONTINUE_NOTE | VARCHAR (100) | If the reconciliation action (I IEV 1020) indicates a discontinue, this item indicates the note for discontinuation (if one was specified by the user). |
| ORDER_REC_HOLD_ACTION_C | INTEGER |  |
| HOLD_INFO_LINE_NUMBER | INTEGER | The line number in the order record that contains additional hold information for this order reconciliation action, if applicable. The values in this column can be linked to the LINE column in the ORDER_HOLD_INFO table. |
| ORD_REC_ACT_BUTTON_C | INTEGER |  |
| ORDER_COMMENT | VARCHAR (254) | Store contact-specific comment for an order |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | EVENT_ID | ED_IEV_PAT_INFO | EVENT_ID | Unknown | No | No |  |
| 1 | EVENT_ID | IP_MAR_BARCODE_ITM | EVENT_ID | Unknown | No | No |  |
| 3 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 4 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 4 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 4 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 5 | RECON_ORD_ID | ADT_ORDERS_ERRORS | ORDER_ID | No | No | No |  |
| 5 | RECON_ORD_ID | ADT_ORDER_INFORMATION | ORDER_ID | No | No | No |  |
| 5 | RECON_ORD_ID | APPT_REQUEST | REQUEST_ID | No | No | No |  |
| 5 | RECON_ORD_ID | CL_ORD_FST_LST_SCH | ORDER_ID | No | No | No |  |
| 5 | RECON_ORD_ID | DENT_ORD_NOADD | ORDER_ID | No | No | No |  |
| 5 | RECON_ORD_ID | DUPMED_DISMISS_HH_INFO | ORDER_ID | No | No | No |  |
| 5 | RECON_ORD_ID | ENDOSCOPY_METRICS | ORDER_ID | Unknown | No | No |  |
| 5 | RECON_ORD_ID | EXTERNAL_ORDER_INFO | ORDER_ID | No | No | No |  |
| 5 | RECON_ORD_ID | F_IMG_STUDY | ORDER_ID | Unknown | Unknown | No |  |
| 5 | RECON_ORD_ID | F_IP_HSP_SUM_ORDER | ORDER_ID | Unknown | Unknown | No |  |
| 5 | RECON_ORD_ID | F_LAB_ORDERS | ORDER_ID | Unknown | Unknown | No |  |
| 5 | RECON_ORD_ID | F_MU_OBJ_EH_PLACED_ORDER | ORDER_ID | Unknown | Unknown | No |  |
| 5 | RECON_ORD_ID | F_MU_OBJ_EH_RESULTD_ORDER | ORDER_PROC_ID | Unknown | Unknown | No |  |
| 5 | RECON_ORD_ID | F_ONC_PRIOR_AUTH_ORDERS | ORDER_ID | Unknown | Unknown | No |  |
| 5 | RECON_ORD_ID | F_OPIOID_ORDERS | ORDER_ID | Unknown | Unknown | No |  |
| 5 | RECON_ORD_ID | F_RX_ORDER | ORDER_MED_ID | Unknown | Unknown | No |  |
| 5 | RECON_ORD_ID | HH_MED_ORD_IN_POC_DETAIL | ORDER_MED_ID | No | No | No |  |
| 5 | RECON_ORD_ID | HV_ORDER_PROC | ORDER_PROC_ID | Unknown | No | No |  |
| 5 | RECON_ORD_ID | MED_DETAILS_EXT_ORD | ORDER_ID | No | No | No |  |
| 5 | RECON_ORD_ID | MERCHANDISE_ORDER_INFO | ORDER_ID | Yes | No | No |  |
| 5 | RECON_ORD_ID | MU_EH_QRDA_I_ORDER | ORDER_ID | Unknown | Unknown | No |  |
| 5 | RECON_ORD_ID | ORDERS | ORDER_ID | No | No | No |  |

_(166 total; showing first 30)_
