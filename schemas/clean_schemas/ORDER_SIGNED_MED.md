# ORDER_SIGNED_MED

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=ORDER_SIGNED_MED

## Description

This table contains the users, providers, and messages related to medication verbal orders and cosign orders.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | ORD |
| Release Version | MU1 - EPIC 2002 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| ORDER_MED_ID | NUMERIC (18,0) | The unique orders record ID for the medication order. |
| LINE | No | The line count for the table. |
| PAT_ID *(deprecated)* | VARCHAR (18) | This column has been deprecated. Please join this table with the ORDER_MED table to find this value. The unique ID assigned to the patient record (EPT .1). This ID may be encrypted if you have elected to use enterprise reporting?s encryption utility. |
| PAT_ENC_DATE_REAL | No | This column has been deprecated. Please join this table with the ORDER_MED table to find this value. This is a numeric representation of the date of this encounter in your system. The integer portion of the number specifies the date of the encounter. The digits after the decimal point indicate multiple visits on one day. |
| PAT_ENC_CSN_ID | 210 | This column has been deprecated. Please join this table with the ORDER_MED table to find this value. A unique serial number for this encounter. This number is unique across all patients and encounters in the system. |
| SIGNED_TYPE_C | INTEGER |  |
| VERB_COMM_PROV_ID | VARCHAR (18) | The unique provider record ID for the provider communicating the verbal order. |
| VERB_SGNER_USER_ID | VARCHAR (18) | The unique user record ID for the user signing the verbal order. |
| VERB_MSGRC_USER_ID | VARCHAR (18) | The unique user record ID for the recipient of the In Basket message for the verbal order. |
| VERB_MSG_ID | VARCHAR (18) | The unique In Basket message record ID of the In Basket message created by the verbal order. |
| VERB_SIGNED_TIME | DATETIME (Local) | The date and time the verbal order was signed. |
| VERBAL_MODE_C | INTEGER |  |
| ORDER_PROV_ID | VARCHAR (18) | The unique provider record ID for the ordering provider. |
| AUTH_PROV_ID | VARCHAR (18) | The unique provider record ID for the authorizing provider. |
| CSGN_MSGRC_USER_ID | VARCHAR (18) | The unique user record ID for the recipient of the cosigned In Basket message. |
| CSGN_MSG_ID | VARCHAR (18) | The unique In Basket message record ID of the cosigned In Basket message. |
| CSGN_SIGNED_TIME | DATETIME (Local) | The date and time the order was cosigned. |
| COSIGNER_ID | VARCHAR (18) | The unique user record ID for the order cosigner. |
| IS_HOSPITALIST_YN | VARCHAR (1) |  |
| CM_PHY_OWNER_ID | VARCHAR (25) | ID of the physical deployment owner for this record.  Physical owners will be where the data is hosted, either on the cross-over server or the owner deployment. |
| CM_LOG_OWNER_ID | VARCHAR (25) | ID of the logical deployment owner for this record.  Logical owners show the deployment where the record was created but don't represent if the record is a part of version skew. |
| VERB_ORD_CMT | VARCHAR (508) | Verbal order comment. |
| CSGN_CREATE_DTTM | DATETIME (UTC) | When the cosign requirement was created (UTC Time). |
| DFI_ID | NUMERIC (18,0) | Link to related DFI record tracking the deficiency associated with this cosign requirement. |
| CSGN_RQRD_C | INTEGER |  |
| LINKED_GRP_GUID | VARCHAR (38) | This item holds a GUID for linking a group of linked orders.  This will be used for tracking the cosign messages sent to providers. |
| SIG_REQ_CRT_USER_ID | VARCHAR (18) | If the order signature requirement was manually created, this item stores the ID of the user who created the requirement. |
| SIG_REQ_CRT_SRC_C | INTEGER |  |
| SIG_REQ_CRT_ENC | NUMERIC (18,0) | This item stores the CSN of the patient encounter where a cosign or verbal sign requirement was created. This item is populated when a cosign or verbal signature requirement is generated. |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| B-TREE INDEX | EIX_ORDER_SIGNED_MED_CSN_ID | PAT_ENC_CSN_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_ORDER_SIGNED_MED_PAID_CMP | PAT_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_ORDER_SIGNED_MED_PAID_CMP | PAT_ENC_DATE_REAL | 2 | Yes | Yes |  |
| B-TREE INDEX | EIX_SIGNEDMED_CSGN_SIGN_TIME | CSGN_SIGNED_TIME | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_SIGNEDMED_VERB_SIGN_TIME | VERB_SIGNED_TIME | 1 | Yes | Yes |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ORDER_MED_ID | ADT_ORDERS_ERRORS | ORDER_ID | No | No | No |  |
| 1 | ORDER_MED_ID | ADT_ORDER_INFORMATION | ORDER_ID | No | No | No |  |
| 1 | ORDER_MED_ID | APPT_REQUEST | REQUEST_ID | No | No | No |  |
| 1 | ORDER_MED_ID | CL_ORD_FST_LST_SCH | ORDER_ID | No | No | No |  |
| 1 | ORDER_MED_ID | DENT_ORD_NOADD | ORDER_ID | No | No | No |  |
| 1 | ORDER_MED_ID | DUPMED_DISMISS_HH_INFO | ORDER_ID | No | No | No |  |
| 1 | ORDER_MED_ID | ENDOSCOPY_METRICS | ORDER_ID | Unknown | No | No |  |
| 1 | ORDER_MED_ID | EXTERNAL_ORDER_INFO | ORDER_ID | No | No | No |  |
| 1 | ORDER_MED_ID | F_IMG_STUDY | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_MED_ID | F_IP_HSP_SUM_ORDER | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_MED_ID | F_LAB_ORDERS | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_MED_ID | F_MU_OBJ_EH_PLACED_ORDER | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_MED_ID | F_MU_OBJ_EH_RESULTD_ORDER | ORDER_PROC_ID | Unknown | Unknown | No |  |
| 1 | ORDER_MED_ID | F_ONC_PRIOR_AUTH_ORDERS | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_MED_ID | F_OPIOID_ORDERS | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_MED_ID | F_RX_ORDER | ORDER_MED_ID | Unknown | Unknown | No |  |
| 1 | ORDER_MED_ID | HH_MED_ORD_IN_POC_DETAIL | ORDER_MED_ID | No | No | No |  |
| 1 | ORDER_MED_ID | HV_ORDER_PROC | ORDER_PROC_ID | Unknown | No | No |  |
| 1 | ORDER_MED_ID | MED_DETAILS_EXT_ORD | ORDER_ID | No | No | No |  |
| 1 | ORDER_MED_ID | MERCHANDISE_ORDER_INFO | ORDER_ID | Yes | No | No |  |
| 1 | ORDER_MED_ID | MU_EH_QRDA_I_ORDER | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_MED_ID | ORDERS | ORDER_ID | No | No | No |  |
| 1 | ORDER_MED_ID | ORDER_AUTH_INFO | ORDER_ID | No | No | No |  |
| 1 | ORDER_MED_ID | ORDER_MED | ORDER_MED_ID | Unknown | No | No |  |
| 1 | ORDER_MED_ID | ORDER_MEDINFO | ORDER_MED_ID | Unknown | No | No |  |
| 1 | ORDER_MED_ID | ORDER_MED_2 | ORDER_ID | Unknown | No | No |  |
| 1 | ORDER_MED_ID | ORDER_MED_3 | ORDER_ID | Unknown | No | No |  |
| 1 | ORDER_MED_ID | ORDER_MED_4 | ORDER_ID | Unknown | No | No |  |
| 1 | ORDER_MED_ID | ORDER_MED_5 | ORDER_ID | Unknown | No | No |  |
| 1 | ORDER_MED_ID | ORDER_MED_6 | ORDER_MED_ID | Unknown | No | No |  |

_(335 total; showing first 30)_
