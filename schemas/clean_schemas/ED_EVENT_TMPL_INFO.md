# ED_EVENT_TMPL_INFO

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=ED_EVENT_TMPL_INFO

## Description

This table contains the noadd single items (name, ID, record state?) for a given event template.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | FULL |
| Load Frequency | WEEKLY - FULL |
| Chronicles INI | LEV |
| Release Version | EPIC 2002 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| RECORD_ID | VARCHAR (18) | The unique ID of the event template record. |
| RECORD_NAME | VARCHAR (100) | The name of the event template. |
| RECORD_STATE_NAME | VARCHAR (8) |  |
| DISPLAY_NAME | VARCHAR (100) | The display name of the event template. |
| EVENT_NAME | VARCHAR (100) | The name of the event that gets recorded to patient event. |
| TEMP_NAME_EDIT | VARCHAR (100) | The temporary event name, same as the record name. |
| ITEMS_EDITED_TIME | DATETIME (Local) | The instant when noadd items were edited. |
| UPDATE_TIME | No | The date and time the record information was last extracted. |
| CM_PHY_OWNER_ID | VARCHAR (25) | ID of the physical deployment owner for this record.  Physical owners will be where the data is hosted, either on the cross-over server or the owner deployment. |
| CM_LOG_OWNER_ID | VARCHAR (25) | ID of the logical deployment owner for this record.  Logical owners show the deployment where the record was created but doesn't represent if the record is a part of version skew. |
| INP_NOTE_TYPE_C | VARCHAR (66) |  |
| CASE_TRKING_EVENT_C | VARCHAR (66) |  |
| FLOWSHEET_ROW_ID | VARCHAR (18) | The flowsheet row associated with this event template. |
| FLWSHT_ADD_ROWS_YN | VARCHAR (1) |  |
| LEV_LDAPLASSESS_YN | VARCHAR (1) |  |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| BITMAP INDEX | EIX_5668 | CM_PHY_OWNER_ID | 1 | No | Yes |  |
| BITMAP INDEX | EIX_5669 | CM_LOG_OWNER_ID | 1 | No | Yes |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 9 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 9 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 9 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 10 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 10 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 10 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 11 | INP_NOTE_TYPE_C | ZC_NOTE_TYPE_IP | TYPE_IP_C | No | No | No |  |
| 12 | CASE_TRKING_EVENT_C | ZC_OR_PAT_EVENTS | TRACKING_EVENT_C | No | No | No |  |
| 13 | FLOWSHEET_ROW_ID | FLO_CNTX_INFO | ID | No | No | No |  |
| 13 | FLOWSHEET_ROW_ID | IP_FLO_GP_DATA | FLO_MEAS_ID | No | No | No |  |
| 13 | FLOWSHEET_ROW_ID | IP_FLO_GP_DATA_2 | FLO_MEAS_ID | No | No | No |  |
