# IP_FLO_CUSTOM_LIST

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=IP_FLO_CUSTOM_LIST

## Description

This table contains the possible choices for this flowsheet row. It also contains the corresponding charge row values and trigger values.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | FLO |
| Release Version | SPRING 2006 |
| May contain EHI? | No |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| ID | VARCHAR (18) | The unique ID of the flowsheet group/row. |
| CONTACT_DATE_REAL | No | A unique, internal contact date in decimal format. The integer portion of the number indicates the date of the contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| LINE | No | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| CONTACT_DATE | VARCHAR (254) | The date of this contact in calendar format. |
| CM_CT_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this contact. This is populated only if you use IntraConnect. |
| CUST_LIST *(deprecated)* | VARCHAR (254) |  |
| CUSTLST_EXTID_TP_C | INTEGER |  |
| CUSTLIST_EXT_ID | VARCHAR (192) | This is the external ID for the custom list. |
| CHG_ROW_PROC_ID | NUMERIC (18,0) | This is the associated item that is the procedure code that should be triggered when the custom list is picked. |
| CHG_ROW_SPC_VAL | INTEGER | This item is the quantity for the corresponding procedure. |
| CHG_ROW_ONOFF_C | INTEGER |  |
| CUST_LIST_ABNORML_YN | VARCHAR (1) |  |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this Chronicles record. This is populated only if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this Chronicles record was extracted. This is populated only if you use IntraConnect. |
| CUST_LIST_ABBR | VARCHAR (254) | The abbreviaton of the custom list choice, if defined. This column is null if the abbreviation is not defined. |
| CUST_LIST_VALUE | VARCHAR (254) | The value of the custom list choice. |
| CUST_LIST_MAP_VALUE | VARCHAR (254) | The abbreviaton of the custom list choice, if defined. This column is the value of the custom list choice if the abbreviation is not defined. This column is functionally equivalent to COALESCE(CUST_LIST_ABBR, CUST_LIST_VALUE). |
| CUST_LIST_PAT_FRIENDLY_TEXT | VARCHAR (200) | Patient-friendly language for a custom list choice. |
| CL_HIDE_FROM_PAT_YN | VARCHAR (1) |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ID | FLO_CNTX_INFO | ID | No | No | No |  |
| 1 | ID | IP_FLO_GP_DATA | FLO_MEAS_ID | No | No | No |  |
| 1 | ID | IP_FLO_GP_DATA_2 | FLO_MEAS_ID | No | No | No |  |
| 1 | ID | IP_FLO_OVRTM_SNGL | ID | No | No | No |  |
| 2 | CONTACT_DATE_REAL | CONTACT_DATE_REAL |  |  |  |  |  |
| 5 | CM_CT_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 5 | CM_CT_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 5 | CM_CT_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 7 | CUSTLST_EXTID_TP_C | ZC_CUSTLIST_EXTID | CUSTLIST_EXTID_C | No | No | No |  |
| 9 | CHG_ROW_PROC_ID | CLARITY_EAP | PROC_ID | No | No | No |  |
| 9 | CHG_ROW_PROC_ID | CLARITY_EAP_2 | PROC_ID | No | No | No |  |
| 9 | CHG_ROW_PROC_ID | CLARITY_EAP_3 | PROC_ID | No | No | No |  |
| 9 | CHG_ROW_PROC_ID | CLARITY_EAP_4 | PROC_ID | No | No | No |  |
| 9 | CHG_ROW_PROC_ID | CLARITY_EAP_5 | PROC_ID | No | No | No |  |
| 9 | CHG_ROW_PROC_ID | CLARITY_EAP_IMM | PROC_ID | Unknown | No | No |  |
| 9 | CHG_ROW_PROC_ID | PROC_CONSENT_CONFIG | PROC_ID | No | No | No |  |
| 9 | CHG_ROW_PROC_ID | PROC_UM | PROC_ID | No | No | No |  |
| 9 | CHG_ROW_PROC_ID | V_CUBE_D_PROCEDURE | PROCEDURE_ID | Unknown | Unknown | No |  |
| 11 | CHG_ROW_ONOFF_C | ZC_CHG_ROW_ONOFF | CHG_ROW_ONOFF_C | No | No | No |  |
| 13 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 13 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 13 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 14 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 14 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 14 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
