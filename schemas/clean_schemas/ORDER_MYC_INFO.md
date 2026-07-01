# ORDER_MYC_INFO

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=ORDER_MYC_INFO

## Description

When sharing a lab result with a web-based chart system patient, the clinician may choose to attach a Result Comment. Data for the Result Comment patient note is stored in this table.

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
| ORDER_PROC_ID | NUMERIC (18,0) | The unique ID of the procedure order record that is being released/unreleased. |
| RELEASE_TIME | DATETIME (Local) | If this field is null, it means that the order result has not been released for the web-based chart system. If it has a timestamp value in it, then the order result has been released. NOTE: for the actual time the lab result was released to the web-based chart system patient, refer to RELEASE_TIME in table ORDER_MYC_RELEASE.  Once the conversion to populate ORD-32001 is finished, the rows in this column will stop being populated. Once ORD-32000 is officially deprecated, this column will also be removed. |
| PATIENT_NOTE_ID | VARCHAR (254) | The unique ID of the note to the web-based chart system patient that is associated with the order. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| RELEASED_YN | VARCHAR (1) |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ORDER_PROC_ID | ADT_ORDERS_ERRORS | ORDER_ID | No | No | No |  |
| 1 | ORDER_PROC_ID | ADT_ORDER_INFORMATION | ORDER_ID | No | No | No |  |
| 1 | ORDER_PROC_ID | APPT_REQUEST | REQUEST_ID | No | No | No |  |
| 1 | ORDER_PROC_ID | CL_ORD_FST_LST_SCH | ORDER_ID | No | No | No |  |
| 1 | ORDER_PROC_ID | DENT_ORD_NOADD | ORDER_ID | No | No | No |  |
| 1 | ORDER_PROC_ID | DUPMED_DISMISS_HH_INFO | ORDER_ID | No | No | No |  |
| 1 | ORDER_PROC_ID | ENDOSCOPY_METRICS | ORDER_ID | Unknown | No | No |  |
| 1 | ORDER_PROC_ID | EXTERNAL_ORDER_INFO | ORDER_ID | No | No | No |  |
| 1 | ORDER_PROC_ID | F_IMG_STUDY | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_PROC_ID | F_IP_HSP_SUM_ORDER | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_PROC_ID | F_LAB_ORDERS | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_PROC_ID | F_MU_OBJ_EH_PLACED_ORDER | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_PROC_ID | F_MU_OBJ_EH_RESULTD_ORDER | ORDER_PROC_ID | Unknown | Unknown | No |  |
| 1 | ORDER_PROC_ID | F_ONC_PRIOR_AUTH_ORDERS | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_PROC_ID | F_OPIOID_ORDERS | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_PROC_ID | F_RX_ORDER | ORDER_MED_ID | Unknown | Unknown | No |  |
| 1 | ORDER_PROC_ID | HH_MED_ORD_IN_POC_DETAIL | ORDER_MED_ID | No | No | No |  |
| 1 | ORDER_PROC_ID | HV_ORDER_PROC | ORDER_PROC_ID | Unknown | No | No |  |
| 1 | ORDER_PROC_ID | MED_DETAILS_EXT_ORD | ORDER_ID | No | No | No |  |
| 1 | ORDER_PROC_ID | MERCHANDISE_ORDER_INFO | ORDER_ID | Yes | No | No |  |
| 1 | ORDER_PROC_ID | MU_EH_QRDA_I_ORDER | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_PROC_ID | ORDERS | ORDER_ID | No | No | No |  |
| 1 | ORDER_PROC_ID | ORDER_AUTH_INFO | ORDER_ID | No | No | No |  |
| 1 | ORDER_PROC_ID | ORDER_MED | ORDER_MED_ID | Unknown | No | No |  |
| 1 | ORDER_PROC_ID | ORDER_MEDINFO | ORDER_MED_ID | Unknown | No | No |  |
| 1 | ORDER_PROC_ID | ORDER_MED_2 | ORDER_ID | Unknown | No | No |  |
| 1 | ORDER_PROC_ID | ORDER_MED_3 | ORDER_ID | Unknown | No | No |  |
| 1 | ORDER_PROC_ID | ORDER_MED_4 | ORDER_ID | Unknown | No | No |  |
| 1 | ORDER_PROC_ID | ORDER_MED_5 | ORDER_ID | Unknown | No | No |  |
| 1 | ORDER_PROC_ID | ORDER_MED_6 | ORDER_MED_ID | Unknown | No | No |  |

_(104 total; showing first 30)_
