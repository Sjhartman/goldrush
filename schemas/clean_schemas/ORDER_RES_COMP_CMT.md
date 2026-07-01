# ORDER_RES_COMP_CMT

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=ORDER_RES_COMP_CMT

## Description

This table contains result component value comments for orders that are populated by the Incoming Results Interface. These result component value comments are not populated through Enter/Edit Results. The data in this table is only populated if the result component value normally stored in the Value_Internal (I ORD 2010) item (ORDER_RESULTS.ORD_VALUE or ORDER_RESULTS.ORD_NUM_VALUE) is too long to be stored in that item.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | ORD |
| Release Version | SPRING 2007 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| ORDER_ID | NUMERIC (18,0) | The order ID for this order/procedure. |
| CONTACT_DATE_REAL | FLOAT | This is a numeric representation of the date of this encounter in your system.  The integer portion of the number specifies the date of the encounter. The digits after the decimal point indicate multiple visits on one day. |
| LINE_COMP | INTEGER | The line count associated with the result component. This line number will match with the LINE column in the ORDER_RESULTS table. It is probable that this table will not have all the lines from the ORDER_RESULTS table since this table only contains data for the components that do not have data in item that stores the result component in the Order record. |
| CONTACT_DATE | DATETIME | The date of this contact in calendar format. |
| COMPONENT_ID | NUMERIC (18,0) | The unique ID of each result component for each result.  Additional data about result components can be found in the CLARITY_COMPONENT table. |
| LINE_COMMENT | INTEGER | The line count associated with each line of the result component comments. There can be multiple lines of comments, therefore each line has a line number. |
| CM_CT_OWNER_ID | VARCHAR (25) | The contact owner deployment of this record; used in Community Model record sharing. |
| RESULTS_COMP_CMT | VARCHAR (1000) | The result component value comments for this order record which are populated by the Incoming Results Interface.  These result comments are NOT populated by Enter/Edit Results. This column is populated when the result component values that are normally stored in the result component in the Order record (ORDER_RESULTS.ORD_VALUE or ORDER_RESULTS.ORD_NUM_VALUE) are too long to be stored in the result component in the Order record. |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| B-TREE INDEX | EIX_ORDER_RES_CMP_CMT_CNTCT_DT | CONTACT_DATE | 1 | Yes | Yes |  |

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
| 1 | ORDER_ID | F_OPIOID_ORDERS | ORDER_ID | Unknown | Unknown | No |  |
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

_(114 total; showing first 30)_
