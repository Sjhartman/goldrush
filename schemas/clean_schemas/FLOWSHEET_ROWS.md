# FLOWSHEET_ROWS

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=FLOWSHEET_ROWS

## Description

This table displays flowsheet row information for device variable records (FDC).

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | FDC |
| Release Version | Summer 2009 |
| May contain EHI? | No |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| RECORD_ID | NUMERIC (18,0) | The unique identifier (.1 item) for the flowsheet data capture record. |
| LINE | No | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| FLOWSHEET_ROW_ID | VARCHAR (18) | The unique ID for the flowsheet row or group linked to the flowsheet data capture record. |
| FLO_LIST_YN | VARCHAR (1) |  |
| DISABLE_AUTOFILE_YN | VARCHAR (1) |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | RECORD_ID | FLOWSHEET_DC_INFO | RECORD_ID | No | No | No |  |
| 3 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 4 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 4 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 4 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 5 | FLOWSHEET_ROW_ID | FLO_CNTX_INFO | ID | No | No | No |  |
| 5 | FLOWSHEET_ROW_ID | IP_FLO_GP_DATA | FLO_MEAS_ID | No | No | No |  |
| 5 | FLOWSHEET_ROW_ID | IP_FLO_GP_DATA_2 | FLO_MEAS_ID | No | No | No |  |
