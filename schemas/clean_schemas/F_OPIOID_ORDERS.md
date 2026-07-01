# F_OPIOID_ORDERS

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=F_OPIOID_ORDERS

## Description

This derived table stores information on opioid outpatient medication orders and is intended to boost the performance of the opioid order metrics view, V_ORD_MED_OPIOID_METRICS. It is not designed to be used in a standalone fashion.

## Metadata

| Property | Value |
| --- | --- |
| Type | Derived Table |
| Load Frequency | INCREMENTAL |
| Release Version | Rel November 2019 |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| ORDER_ID | NUMERIC (18,0) | The unique ID of the order record associated with this medication order. This is an internal unique identifier for ORD master file records in this table and cannot be used to link to CLARITY_MEDICATION. |
| UPDATE_DATE | No | The date and time when this row was created or last updated. |
| HAS_NALOXONE_YN | No | Stores whether or not the patient had an active order for naloxone at the time prescription was ordered. |
| PROV_REV_PDMP_IN_ENC_YN | No | Stores whether or not the authorizing provider reviewed the PDMP from the ordering encounter. |
| PDMP_REV_IN_ENC_YN | No | Stores whether or not any user reviewed the PDMP from the ordering encounter. |
| DAYS_SINCE_PROV_REV_PDMP | No | Stores the number of days, counting back from the order date, since the last time the authorizing provider reviewed the PDMP prior to the order date. PDMP reviews recorded after the order instant are ignored, even if they occurred on the same day. |
| DAYS_SINCE_LAST_PDMP_REV | No | Stores the number of days, counting back from the order date, since the last time any user reviewed the PDMP for the patient prior to the order date. PDMP reviews recorded after the order instant are ignored, even if they occurred on the same day. |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ORDER_ID | ADT_ORDERS_ERRORS | ORDER_ID | No | Unknown | No |  |
| 1 | ORDER_ID | ADT_ORDER_INFORMATION | ORDER_ID | No | Unknown | No |  |
| 1 | ORDER_ID | APPT_REQUEST | REQUEST_ID | No | Unknown | No |  |
| 1 | ORDER_ID | CL_ORD_FST_LST_SCH | ORDER_ID | No | Unknown | No |  |
| 1 | ORDER_ID | DENT_ORD_NOADD | ORDER_ID | No | Unknown | No |  |
| 1 | ORDER_ID | DUPMED_DISMISS_HH_INFO | ORDER_ID | No | Unknown | No |  |
| 1 | ORDER_ID | ENDOSCOPY_METRICS | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_ID | EXTERNAL_ORDER_INFO | ORDER_ID | No | Unknown | No |  |
| 1 | ORDER_ID | F_IMG_STUDY | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_ID | F_IP_HSP_SUM_ORDER | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_ID | F_LAB_ORDERS | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_ID | F_MU_OBJ_EH_PLACED_ORDER | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_ID | F_MU_OBJ_EH_RESULTD_ORDER | ORDER_PROC_ID | Unknown | Unknown | No |  |
| 1 | ORDER_ID | F_ONC_PRIOR_AUTH_ORDERS | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_ID | F_RX_ORDER | ORDER_MED_ID | Unknown | Unknown | No |  |
| 1 | ORDER_ID | HH_MED_ORD_IN_POC_DETAIL | ORDER_MED_ID | No | Unknown | No |  |
| 1 | ORDER_ID | HV_ORDER_PROC | ORDER_PROC_ID | Unknown | Unknown | No |  |
| 1 | ORDER_ID | MED_DETAILS_EXT_ORD | ORDER_ID | No | Unknown | No |  |
| 1 | ORDER_ID | MERCHANDISE_ORDER_INFO | ORDER_ID | Yes | Unknown | No |  |
| 1 | ORDER_ID | MU_EH_QRDA_I_ORDER | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_ID | ORDERS | ORDER_ID | No | Unknown | No |  |
| 1 | ORDER_ID | ORDER_AUTH_INFO | ORDER_ID | No | Unknown | No |  |
| 1 | ORDER_ID | ORDER_MED | ORDER_MED_ID | Unknown | Unknown | No |  |
| 1 | ORDER_ID | ORDER_MEDINFO | ORDER_MED_ID | Unknown | Unknown | No |  |
| 1 | ORDER_ID | ORDER_MED_2 | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_ID | ORDER_MED_3 | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_ID | ORDER_MED_4 | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_ID | ORDER_MED_5 | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_ID | ORDER_MED_6 | ORDER_MED_ID | Unknown | Unknown | No |  |
| 1 | ORDER_ID | ORDER_MED_7 | ORDER_ID | No | Unknown | No |  |

_(72 total; showing first 30)_
