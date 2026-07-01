# ORD_BLOOD_ADMIN

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=ORD_BLOOD_ADMIN

## Description

Administrable Procedure Items in Orders (ORD).

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
| ORDER_ID | NUMERIC (18,0) | The unique ID of the child/instance order that is associated with transfusion documentation for a unit of blood. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| ADMIN_PX_TYPE_C | INTEGER |  |
| BLOOD_UNIT_NUM | VARCHAR (30) | The primary identifier for the blood product.  This is not necessarily unique. Populated via interface, or administration form for procedures. |
| BLOOD_CODING_SYS_C | INTEGER |  |
| BLOOD_UNIT_NM_SRC_C | INTEGER |  |
| BLOOD_PRODUCT_CODE | VARCHAR (50) | Secondary identifier to be paired with unit number (when dealing with divisions of a unit of blood). |
| BLOOD_EXPIRATN_INST | DATETIME (Local) | The expiration instant as specified on the unit of blood.  This may be populated by the interface. |
| BLOOD_START_INSTANT | DATETIME (Local) | Based on administration actions, the start of the transfusion. |
| BLOOD_END_INSTANT | DATETIME (Local) | Based on administration actions, the end of the transfusion. |
| BLOOD_UNIT_RES_ID | NUMERIC (18,0) | Corresponds to the Interfaced information about the scanned unit. |
| BLOOD_CODABAR_REG | VARCHAR (10) | The CODABAR registration number from the bag of blood associated with this order. |
| IS_BLOOD_YN | VARCHAR (1) |  |
| TRANSFUSE_AMOUNT | INTEGER | If this is a blood transfusion order, this column is the amount of blood that was ordered. |
| TRANSFUSE_AMOUNT_UNIT_C | INTEGER |  |
| PREPARE_AMOUNT | INTEGER | If this is a blood prepare order, this column is the amount of blood that was ordered. |
| PREPARE_AMOUNT_UNIT_C | INTEGER |  |
| WEIGHT_BLD_AMOUNT | NUMERIC (18,1) | The weight-based amount this blood prepare or transfuse order was placed in. |
| WEIGHT_BLD_UNIT_C | INTEGER |  |
| SAV_PAT_BLOODREQT_YN | VARCHAR (1) |  |
| NO_NEED_BLOODREQT_YN | VARCHAR (1) |  |
| BLOOD_MAIN_ADMIN | INTEGER | The administration line in ORD 11000 holding the main blood details. |
| BLOOD_PRODUCT_TYP_C | INTEGER |  |

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

_(109 total; showing first 30)_
