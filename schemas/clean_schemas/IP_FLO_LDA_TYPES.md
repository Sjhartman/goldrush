# IP_FLO_LDA_TYPES

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=IP_FLO_LDA_TYPES

## Description

This table contains the groups that this flowsheet group (LDA) can be sorted into. This allows for easy reporting.

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
| LDA_TYPE_OT_C | INTEGER |  |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this Chronicles record. This is populated only if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this Chronicles record was extracted. This is populated only if you use IntraConnect. |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| B-TREE INDEX | EIX_IP_FLO_LDA_T_TYPE_ID_CDR | LDA_TYPE_OT_C | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_IP_FLO_LDA_T_TYPE_ID_CDR | ID | 2 | Yes | Yes |  |
| B-TREE INDEX | EIX_IP_FLO_LDA_T_TYPE_ID_CDR | CONTACT_DATE_REAL | 3 | Yes | Yes |  |

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
| 6 | LDA_TYPE_OT_C | ZC_LINES_GROUP | LINES_GROUP_C | No | No | No |  |
| 7 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 7 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 7 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 8 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 8 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 8 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
