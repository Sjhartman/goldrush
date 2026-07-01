# IP_FLO_MEASUREMNTS

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=IP_FLO_MEASUREMNTS

## Description

This table contains the list of FLO records which belong to the group.

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
| MEASUREMENT_ID | VARCHAR (18) | This is the list of the measurements for this flowsheet group. |
| STRT_REMOVED_YN | VARCHAR (1) |  |
| AN_HIDE_ROW_YN | VARCHAR (1) |  |
| AN_HIDE_IN_SUM_YN | VARCHAR (1) |  |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this Chronicles record. This is populated only if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this Chronicles record was extracted. This is populated only if you use IntraConnect. |
| REQUIRED_STATUS_C | INTEGER |  |

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
| 6 | MEASUREMENT_ID | FLO_CNTX_INFO | ID | No | No | No |  |
| 6 | MEASUREMENT_ID | IP_FLO_GP_DATA | FLO_MEAS_ID | No | No | No |  |
| 6 | MEASUREMENT_ID | IP_FLO_GP_DATA_2 | FLO_MEAS_ID | No | No | No |  |
| 10 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 10 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 10 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 11 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 11 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 11 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 12 | REQUIRED_STATUS_C | ZC_QF_DATA_REQ | QF_DATA_REQ_C | No | No | No |  |
