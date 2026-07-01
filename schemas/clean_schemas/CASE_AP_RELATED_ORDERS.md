# CASE_AP_RELATED_ORDERS

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=CASE_AP_RELATED_ORDERS

## Description

The CASE_AP_RELATED_ORDERS table contains information about other orders related to the Anatomic Pathology case. This information is only populated for legacy data. Newer data is populated in the ORD_LAB_LINKED_ORD table.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | REQ |
| Release Version | Rel February 2022 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| REQUISITION_ID | NUMERIC (18,0) | The unique identifier (.1 item) for the requisition record. |
| LINE | INTEGER | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| ORDER_ID | NUMERIC (18,0) | The unique ID of an order related to the anatomic pathology case.  This information is only populated for legacy data. Newer data is populated in the LAB_LINKED_ORD_ID column of the ORD_LAB_LINKED_ORD table. |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | REQUISITION_ID | EXT_ID_BUNDLE_MAP_DB_MAIN | MAPPING_ID | No | No | No |  |
| 1 | REQUISITION_ID | ID_BUNDLE_DEMOG_DB_MAIN | DEMOG_ID | No | No | No |  |
| 1 | REQUISITION_ID | LAB_CASE_DB_MAIN | CASE_ID | Unknown | No | No |  |
| 1 | REQUISITION_ID | REQ_ALL_MAIN | REQUISITION_ID | No | No | No |  |
| 1 | REQUISITION_ID | REQ_DB_MAIN | REQUISITION_ID | Unknown | No | No |  |
| 3 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 4 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 4 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 4 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 5 | ORDER_ID | ADT_ORDERS_ERRORS | ORDER_ID | No | No | No |  |
| 5 | ORDER_ID | ADT_ORDER_INFORMATION | ORDER_ID | No | No | No |  |
| 5 | ORDER_ID | APPT_REQUEST | REQUEST_ID | No | No | No |  |
| 5 | ORDER_ID | CL_ORD_FST_LST_SCH | ORDER_ID | No | No | No |  |
| 5 | ORDER_ID | DENT_ORD_NOADD | ORDER_ID | No | No | No |  |
| 5 | ORDER_ID | DUPMED_DISMISS_HH_INFO | ORDER_ID | No | No | No |  |
| 5 | ORDER_ID | ENDOSCOPY_METRICS | ORDER_ID | Unknown | No | No |  |
| 5 | ORDER_ID | EXTERNAL_ORDER_INFO | ORDER_ID | No | No | No |  |
| 5 | ORDER_ID | F_IMG_STUDY | ORDER_ID | Unknown | Unknown | No |  |
| 5 | ORDER_ID | F_IP_HSP_SUM_ORDER | ORDER_ID | Unknown | Unknown | No |  |
| 5 | ORDER_ID | F_LAB_ORDERS | ORDER_ID | Unknown | Unknown | No |  |
| 5 | ORDER_ID | F_MU_OBJ_EH_PLACED_ORDER | ORDER_ID | Unknown | Unknown | No |  |
| 5 | ORDER_ID | F_MU_OBJ_EH_RESULTD_ORDER | ORDER_PROC_ID | Unknown | Unknown | No |  |
| 5 | ORDER_ID | F_ONC_PRIOR_AUTH_ORDERS | ORDER_ID | Unknown | Unknown | No |  |
| 5 | ORDER_ID | F_OPIOID_ORDERS | ORDER_ID | Unknown | Unknown | No |  |
| 5 | ORDER_ID | F_RX_ORDER | ORDER_MED_ID | Unknown | Unknown | No |  |
| 5 | ORDER_ID | HH_MED_ORD_IN_POC_DETAIL | ORDER_MED_ID | No | No | No |  |
| 5 | ORDER_ID | HV_ORDER_PROC | ORDER_PROC_ID | Unknown | No | No |  |
| 5 | ORDER_ID | MED_DETAILS_EXT_ORD | ORDER_ID | No | No | No |  |

_(84 total; showing first 30)_
