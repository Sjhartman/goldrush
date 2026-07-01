# ORDER_DX_PROC

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=ORDER_DX_PROC

## Description

The ORDER_DX_PROC table enables you to report on the diagnoses associated with procedures ordered in clinical system. Since one procedure order may be associated with multiple diagnoses, each row in this table is one procedure - diagnosis relation. We have also included patient and contact identification information for each record. Note that system settings may or may not require that procedures be associated with diagnoses. This table contains only information for those procedures and diagnoses that have been explicitly associated. Check with your clinical system Application Administrator to determine how your organization has this set up.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | ORD |
| Release Version | EPIC 2000 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| ORDER_PROC_ID | NUMERIC (18,0) | The unique ID of the procedure order record. |
| LINE | No | The line number for the information associated with this procedure record. Multiple pieces of information can be associated with this record. |
| PAT_ID | VARCHAR (18) | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| PAT_ENC_DATE_REAL | FLOAT | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| PAT_ENC_CSN_ID | 226 | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| DX_ID | NUMERIC (18,0) | The unique ID of the diagnosis record associated with the procedure order. |
| ICD9_CODE *(deprecated)* | VARCHAR (192) | *** Deprecated *** In table ORDER_DX_PROC, the column ICD9_CODE (EDG 40) has been deprecated. Link to the CLARITY_EDG table using ORDER_DX_PROC.DX_ID column. Refer to the Diagnosis and ICD Procedure Updates section of https://galaxy.epic.com/redirect.aspx?documentid=1577542 to determine the correct column to use. |
| DX_QUALIFIER_C | VARCHAR (66) |  |
| COMMENTS | VARCHAR (1024) | Comments added when the procedure was ordered |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| DX_CHRONIC_YN | VARCHAR (1) |  |
| ENC_ICD_CODE | 180 | *** Deprecated *** In table ORDER_DX_PROC, the column ENC_ICD_CODE (EDG 2000) has been deprecated. Link to the CLARITY_EDG table using ORDER_DX_PROC.DX_ID column. Refer to the Diagnosis and ICD Procedure Updates section of https://galaxy.epic.com/redirect.aspx?documentid=1577542 to determine the correct column to use. |
| ASSOC_DX_DESC | VARCHAR (254) | This column stores a free text diagnosis description entered by the end user.  Also referred to as the "display as" field. |
| ASSOC_REQ_DX_ID | NUMERIC (18,0) | The unique ID of the original requisition diagnosis associated with the order. Diagnoses stored by this item might be entered for either clinical or billing purposes. |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| B-TREE INDEX | EIX_ORDER_DX_PROC_CSN_ID | PAT_ENC_CSN_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_ORDER_DX_PROC_DXID | DX_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_ORDER_DX_PROC_PAID | PAT_ID | 1 | Yes | Yes |  |

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

_(243 total; showing first 30)_
