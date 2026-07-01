# F_IP_ORD_FLO_VOLUME

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=F_IP_ORD_FLO_VOLUME

## Description

This table stores information about volume flowsheet documentation pertaining to orders. Each row is a pairing of flowsheet documentation and its associated order, as well as the measurement value.

## Metadata

| Property | Value |
| --- | --- |
| Type | Derived Table |
| Load Frequency | INCREMENTAL |
| Release Version | Rel August 2023 |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| VOLUME_FSD_ID | VARCHAR (18) | The unique ID for the flowsheet data record. |
| VOLUME_FSD_LINE | INTEGER | The line count for the item. |
| VOLUME_ORDER_ID | NUMERIC (18,0) | The unique IDs of the orders that are added to this patient's flowsheet row. This is a multiple-response item. |
| UPDATE_DATE | No | This column stores the date and time when this row was created or last updated. |
| VOLUME_MEAS_VALUE | VARCHAR (2500) | The actual value of the flowsheet reading. |
| VOLUME_REC_DTTM | DATETIME (Local) | The instant the reading was taken. |
| INPATIENT_DATA_ID | VARCHAR (18) | The unique ID of the inpatient data record. |
| PAT_ENC_CSN_ID | NUMERIC (18,0) | Link to Contact Serial Number in EPT for associated encounter. |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | VOLUME_FSD_ID | IP_FLWSHT_REC | FSD_ID | No | Unknown | No |  |
| 1 | VOLUME_FSD_ID | V_EHI_FSD_FILTER | FSD_ID | Unknown | Unknown | No |  |
| 3 | VOLUME_ORDER_ID | ADT_ORDERS_ERRORS | ORDER_ID | No | Unknown | No |  |
| 3 | VOLUME_ORDER_ID | ADT_ORDER_INFORMATION | ORDER_ID | No | Unknown | No |  |
| 3 | VOLUME_ORDER_ID | APPT_REQUEST | REQUEST_ID | No | Unknown | No |  |
| 3 | VOLUME_ORDER_ID | CL_ORD_FST_LST_SCH | ORDER_ID | No | Unknown | No |  |
| 3 | VOLUME_ORDER_ID | DENT_ORD_NOADD | ORDER_ID | No | Unknown | No |  |
| 3 | VOLUME_ORDER_ID | DUPMED_DISMISS_HH_INFO | ORDER_ID | No | Unknown | No |  |
| 3 | VOLUME_ORDER_ID | ENDOSCOPY_METRICS | ORDER_ID | Unknown | Unknown | No |  |
| 3 | VOLUME_ORDER_ID | EXTERNAL_ORDER_INFO | ORDER_ID | No | Unknown | No |  |
| 3 | VOLUME_ORDER_ID | F_IMG_STUDY | ORDER_ID | Unknown | Unknown | No |  |
| 3 | VOLUME_ORDER_ID | F_IP_HSP_SUM_ORDER | ORDER_ID | Unknown | Unknown | No |  |
| 3 | VOLUME_ORDER_ID | F_LAB_ORDERS | ORDER_ID | Unknown | Unknown | No |  |
| 3 | VOLUME_ORDER_ID | F_MU_OBJ_EH_PLACED_ORDER | ORDER_ID | Unknown | Unknown | No |  |
| 3 | VOLUME_ORDER_ID | F_MU_OBJ_EH_RESULTD_ORDER | ORDER_PROC_ID | Unknown | Unknown | No |  |
| 3 | VOLUME_ORDER_ID | F_ONC_PRIOR_AUTH_ORDERS | ORDER_ID | Unknown | Unknown | No |  |
| 3 | VOLUME_ORDER_ID | F_OPIOID_ORDERS | ORDER_ID | Unknown | Unknown | No |  |
| 3 | VOLUME_ORDER_ID | F_RX_ORDER | ORDER_MED_ID | Unknown | Unknown | No |  |
| 3 | VOLUME_ORDER_ID | HH_MED_ORD_IN_POC_DETAIL | ORDER_MED_ID | No | Unknown | No |  |
| 3 | VOLUME_ORDER_ID | HV_ORDER_PROC | ORDER_PROC_ID | Unknown | Unknown | No |  |
| 3 | VOLUME_ORDER_ID | MED_DETAILS_EXT_ORD | ORDER_ID | No | Unknown | No |  |
| 3 | VOLUME_ORDER_ID | MERCHANDISE_ORDER_INFO | ORDER_ID | Yes | Unknown | No |  |
| 3 | VOLUME_ORDER_ID | MU_EH_QRDA_I_ORDER | ORDER_ID | Unknown | Unknown | No |  |
| 3 | VOLUME_ORDER_ID | ORDERS | ORDER_ID | No | Unknown | No |  |
| 3 | VOLUME_ORDER_ID | ORDER_AUTH_INFO | ORDER_ID | No | Unknown | No |  |
| 3 | VOLUME_ORDER_ID | ORDER_MED | ORDER_MED_ID | Unknown | Unknown | No |  |
| 3 | VOLUME_ORDER_ID | ORDER_MEDINFO | ORDER_MED_ID | Unknown | Unknown | No |  |
| 3 | VOLUME_ORDER_ID | ORDER_MED_2 | ORDER_ID | Unknown | Unknown | No |  |
| 3 | VOLUME_ORDER_ID | ORDER_MED_3 | ORDER_ID | Unknown | Unknown | No |  |
| 3 | VOLUME_ORDER_ID | ORDER_MED_4 | ORDER_ID | Unknown | Unknown | No |  |

_(195 total; showing first 30)_
