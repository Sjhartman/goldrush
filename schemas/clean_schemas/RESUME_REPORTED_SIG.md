# RESUME_REPORTED_SIG

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=RESUME_REPORTED_SIG

## Description

This table contains information on how home medications with reported sigs were reconciled at discharge.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | IEV |
| Release Version | Rel February 2022 |
| May contain EHI? | No |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| EVENT_ID | VARCHAR (18) | The unique identifier (.1 item) for the discharge reconciliation event record. |
| LINE | INTEGER | The line number for a reconciliation action on a medication with a reported sig. Multiple pieces of information can be associated with this record. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| ORDER_MED_ID | NUMERIC (18,0) | The ID of the medication order with a reported sig that was resumed at discharge. |
| EVENT_LINE_NUM | INTEGER | The line number of the signing event for this change. Together with EVENT_ID, this forms the foreign key to the ED_IEV_EVENT_INFO table. All lines of this table with the same EVENT_ID and EVENT_LINE_NUM represents changes filed at the same time. |
| PAT_SIG_REPLY_C | INTEGER |  |
| RPT_SIG_LINE_NUM | INTEGER | The line number in the reported sig trail of the order that was reconciled. Together with ORDER_MED_ID, this forms the foreign key to the ORDER_RPTD_SIG_HX table. |

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
| 5 | ORDER_MED_ID | ADT_ORDERS_ERRORS | ORDER_ID | No | No | No |  |
| 5 | ORDER_MED_ID | ADT_ORDER_INFORMATION | ORDER_ID | No | No | No |  |
| 5 | ORDER_MED_ID | APPT_REQUEST | REQUEST_ID | No | No | No |  |
| 5 | ORDER_MED_ID | CL_ORD_FST_LST_SCH | ORDER_ID | No | No | No |  |
| 5 | ORDER_MED_ID | DENT_ORD_NOADD | ORDER_ID | No | No | No |  |
| 5 | ORDER_MED_ID | DUPMED_DISMISS_HH_INFO | ORDER_ID | No | No | No |  |
| 5 | ORDER_MED_ID | ENDOSCOPY_METRICS | ORDER_ID | Unknown | No | No |  |
| 5 | ORDER_MED_ID | EXTERNAL_ORDER_INFO | ORDER_ID | No | No | No |  |
| 5 | ORDER_MED_ID | F_IMG_STUDY | ORDER_ID | Unknown | Unknown | No |  |
| 5 | ORDER_MED_ID | F_IP_HSP_SUM_ORDER | ORDER_ID | Unknown | Unknown | No |  |
| 5 | ORDER_MED_ID | F_LAB_ORDERS | ORDER_ID | Unknown | Unknown | No |  |
| 5 | ORDER_MED_ID | F_MU_OBJ_EH_PLACED_ORDER | ORDER_ID | Unknown | Unknown | No |  |
| 5 | ORDER_MED_ID | F_MU_OBJ_EH_RESULTD_ORDER | ORDER_PROC_ID | Unknown | Unknown | No |  |
| 5 | ORDER_MED_ID | F_ONC_PRIOR_AUTH_ORDERS | ORDER_ID | Unknown | Unknown | No |  |
| 5 | ORDER_MED_ID | F_OPIOID_ORDERS | ORDER_ID | Unknown | Unknown | No |  |
| 5 | ORDER_MED_ID | F_RX_ORDER | ORDER_MED_ID | Unknown | Unknown | No |  |
| 5 | ORDER_MED_ID | HH_MED_ORD_IN_POC_DETAIL | ORDER_MED_ID | No | No | No |  |
| 5 | ORDER_MED_ID | HV_ORDER_PROC | ORDER_PROC_ID | Unknown | No | No |  |
| 5 | ORDER_MED_ID | MED_DETAILS_EXT_ORD | ORDER_ID | No | No | No |  |
| 5 | ORDER_MED_ID | MERCHANDISE_ORDER_INFO | ORDER_ID | Yes | No | No |  |
| 5 | ORDER_MED_ID | MU_EH_QRDA_I_ORDER | ORDER_ID | Unknown | Unknown | No |  |
| 5 | ORDER_MED_ID | ORDERS | ORDER_ID | No | No | No |  |

_(82 total; showing first 30)_
