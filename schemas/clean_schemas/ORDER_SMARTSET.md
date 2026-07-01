# ORDER_SMARTSET

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=ORDER_SMARTSET

## Description

This table contains data on smartsets and smartgroups that orders originated from.

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
| ORDER_ID | NUMERIC (18,0) | Unique ID of the order record being retrieved |
| CM_PHY_OWNER_ID | VARCHAR (25) | ID of the physical deployment owner for this record.  Physical owners will be where the data is hosted, either on the cross-over server or the owner deployment. |
| CM_LOG_OWNER_ID | VARCHAR (25) | ID of the logical deployment owner for this record.  Logical owners show the deployment where the record was created but doesn't represent if the record is a part of version skew. |
| SS_PRL_ID | NUMERIC (18,0) | The ID of the SmartSet or Order Set the order came from. |
| SS_DAT | VARCHAR (254) | The contact date of the contact in the SmartSet that the order came from. |
| SS_SECTION_ID | NUMERIC (18,0) | If a merge template was used, this item will contain the section within the merge template that this order came from.  If no merge template was used, this item will contain the section within the SmartSet that this order came from. |
| SS_SECTION_NAME | VARCHAR (254) | The name of the section whose ID is in SS_SECTION_ID. |
| SS_SECTION_DAT | VARCHAR (254) | The DAT of the contact that was used for the section whose ID is in SS_SECTION_ID. |
| SS_SG_KEY | VARCHAR (254) | The unique key assigned to the merged SmartGroup that contained this order.  This is an arbitrary string value. |
| SS_SG_NAME | VARCHAR (254) | The name of the SmartGroup that contained this order. |
| MERGE_TMPL_ID | NUMERIC (18,0) | The ID of the merge template used when merging this SmartSet during ordering, if any. |
| SS_MERGE_DAT | VARCHAR (254) | The contact date of the contact from the merge template record that was used in this order?s ordering session. |
| SS_PRL_SRC_TYPE_C | INTEGER |  |
| PAT_ENC_CSN_ID | NUMERIC (18,0) | The unique contact serial number for the patient contact associated with this order. This number is unique across patients and encounters in your system. If you use IntraConnect this is the Unique Contact Identifier (UCI). |
| ORDERSET_START_DATE | VARCHAR (508) | Order set start date. |
| SSMRG_DCACTION_C | INTEGER |  |
| KEYSTONE_ORDER_YN | VARCHAR (1) |  |
| ORDERSET_OFFSET | INTEGER | This column stores the default offset from the order set when an order is signed and held. The offset is represented in seconds. For example, if the offset is 2 hours, the value stored in the order will be 7200. |

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

_(202 total; showing first 30)_
