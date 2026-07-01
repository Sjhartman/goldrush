# ORDER_RAD_PRELIM

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=ORDER_RAD_PRELIM

## Description

This table stores prelimming physician information for imaging procedures.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | ORD |
| Release Version | FALL 2004 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| ORDER_PROC_ID | NUMERIC (18,0) | The unique ID of the procedure order record. |
| LINE | No | The line count for this table as determined by the number of preliming radiologists for an order. |
| CM_LOG_OWNER_ID | VARCHAR (25) | ID of the logical deployment owner for this record.  Logical owners show the deployment where the record was created but doesn't represent if the record is a part of version skew. |
| CM_PHY_OWNER_ID | VARCHAR (25) | ID of the physical deployment owner for this record.  Physical owners will be where the data is hosted, either on the cross-over server or the owner deployment. |
| PROV_ID | VARCHAR (18) | The unique provider ID of the radiologist who did the preliminary read for the order. |
| PRELIM_DT | DATETIME | The date when the provider marked the study as preliminary. |
| PRELIM_UTC_DTTM | DATETIME (UTC) | This item captures the date and time in the Universal Time Coordinated (UTC) format that the reading physician listed in the Prelimming Physician (I ORD 52200) item made a change to the study. |
| PRELIM_LOCAL_DTTM | DATETIME (Attached) | This virtual item calculates the instant that the provider listed in the Prelimming Provider (I ORD 52200) item marked the study as Prelim, local to the time zone of the provider's client. |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| B-TREE INDEX | EIX_ORDER_RAD_PRELIM_003 | PROV_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_ORDER_RAD_PRELIM_004 | PRELIM_DT | 1 | Yes | Yes |  |

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

_(92 total; showing first 30)_
