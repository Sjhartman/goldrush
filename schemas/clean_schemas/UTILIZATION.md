# UTILIZATION

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=UTILIZATION

## Description

This table contains information for utilization data.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | UTL |
| Release Version | Rel 2018 |
| May contain EHI? | No |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| UTILIZATION_ID | NUMERIC (18,0) | The unique identifier (.1 item) for the utilization data record. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| UTILIZATION_TYPE_C | INTEGER |  |
| UTILIZATION_DATE | DATETIME | The date for which utilization data was run. |
| UTILIZATION_GROUP_ID | NUMERIC (18,0) | The unique ID of the utilization group that determines the configuration that populated the utilization data. |
| LOCATION_ID | NUMERIC (18,0) | The unique ID of the location for which the utilization data was generated. If utilization was run across locations, this will be the parent location ID. |
| BLOCK_ID | NUMERIC (18,0) | The unique ID of the block for which the utilization data was generated. |
| ROOM_ID | VARCHAR (18) | The unique ID of the room for which the utilization data was generated. |
| CASE_ID | VARCHAR (18) | The unique ID of the case that corresponds to the utilization data. |
| LOG_ID | VARCHAR (18) | The unique ID of the log that corresponds to the utilization data. |
| AVAILABLE_TIME | INTEGER | The number of available minutes allocated to the block or room. This reflects the most recent calculation of available time for utilization data. |
| MANUAL_RELEASED_TIME | INTEGER | The number of manually released minutes for the block or room. This reflects the most recent calculation of available time for utilization data. |
| PERFORM_PROCEDURE_IN | INTEGER | The number of performed procedure minutes that credited as in block to the block or in template to the room. |
| PERFORM_PROCEDURE_OVERBOOK | INTEGER | The number of performed procedure minutes that credited as overbook to the block. |
| PERFORM_PROCEDURE_OUT | INTEGER | The number of performed procedure minutes that credited as out of block to the block or out of template to the room. |
| PERFORM_SETUP_CLEANUP_IN | INTEGER | The number of performed setup and cleanup minutes that credited as in block to the block or in template to the room. |
| PERFORM_SETUP_CLEANUP_OVERBOOK | INTEGER | The number of performed setup and cleanup minutes that credited as overbook to the block. |
| PERFORM_SETUP_CLEANUP_OUT | INTEGER | The number of performed setup and cleanup minutes that credited as out of block to the block or out of template to the room. |
| PERFORM_NUM_CASES | NUMERIC (18,0) | The number of cases that credited to the block or room for performed utilization. |
| PERFORM_NUM_SURGEONS | NUMERIC (18,0) | The number of unique surgeons from the list of cases that credited to the block or room for performed utilization. |
| PERFORM_NUM_BLOCKS | NUMERIC (18,0) | The number of blocks to which the case credited for performed utilization. |
| SCHED_PROCEDURE_IN | INTEGER | The number of scheduled procedure minutes that credited as in block to the block or in template to the room. This reflects the most recent calculation of scheduled utilization data. |
| SCHED_PROCEDURE_OVERBOOK | INTEGER | The number of scheduled procedure minutes that credited as overbook to the block. This reflects the most recent calculation of scheduled utilization data. |
| SCHED_PROCEDURE_OUT | INTEGER | The number of scheduled procedure minutes that credited as out of block to the block or out of template to the room. This reflects the most recent calculation of scheduled utilization data. |
| SCHED_SETUP_CLEANUP_IN | INTEGER | The number of scheduled setup and cleanup minutes that credited as in block to the block or in template to the room. This reflects the most recent calculation of scheduled utilization data. |
| SCHED_SETUP_CLEANUP_OVERBOOK | INTEGER | The number of scheduled setup and cleanup minutes that credited as overbook to the block. This reflects the most recent calculation of scheduled utilization data. |
| SCHED_SETUP_CLEANUP_OUT | INTEGER | The number of scheduled setup and cleanup minutes that credited as out of block to the block or out of template to the room. This reflects the most recent calculation of scheduled utilization data. |
| SCHED_NUM_CASES | NUMERIC (18,0) | The number of cases that credited to the block or room for scheduled utilization. This reflects the most recent calculation of scheduled utilization data. |
| SCHED_NUM_SURGEONS | NUMERIC (18,0) | The number of unique surgeons from the list of cases that credited to the block or room for scheduled utilization. This reflects the most recent calculation of scheduled utilization data. |
| SCHED_NUM_BLOCKS | NUMERIC (18,0) | The number of blocks to which the case credited for scheduled utilization. This reflects the most recent calculation of scheduled utilization data. |
| LAST_RUN_BLOCK_DTTM | DATETIME (Attached) | The last date and time that performed block utilization data was calculated for this record. |
| LAST_RUN_ROOM_DTTM | DATETIME (Attached) | The last date and time that performed room utilization data was calculated for this record. |
| RECORD_STATUS_C | INTEGER |  |
| RECORD_CREATION_DATE | DATETIME | The date the record was created. |
| INSTANT_OF_UPDATE_DTTM | DATETIME (Local) | The date and time the record was last updated. |
| CONVERTED_REC_YN | VARCHAR (1) |  |
| DEPARTMENT_ID | NUMERIC (18,0) | The department for which the utilization data was generated. |
| PROC_ENC_CSN_ID | NUMERIC (18,0) | The procedural encounter that corresponds to the utilization data. |
| CASE_LOG_ROOM_ID | VARCHAR (18) | The room that the procedure was attributed to. Only for type UTL-35=3-Case. |
| AFFECT_BY_PAT_DEL_YN | VARCHAR (1) | Surrogate key used to uniquely identify rows in this (and only this) table on Cogito Cloud only, do not assume the surrogate key in this table will correspond to the surrogate key in another table |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | UTILIZATION_ID | V_OR_UTIL_BLOCK_SUMMARY | UTILIZATION_ID | Unknown | Unknown | No |  |
| 1 | UTILIZATION_ID | V_OR_UTIL_ROOM_SUMMARY | UTILIZATION_ID | Unknown | Unknown | No |  |
| 2 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 2 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 2 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 3 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 4 | UTILIZATION_TYPE_C | ZC_UTILIZATION_TYPE | UTILIZATION_TYPE_C | No | No | No |  |
| 6 | UTILIZATION_GROUP_ID | EVENT_GROUP_INFO | EVENT_GROUP_ID | Unknown | No | No |  |
| 6 | UTILIZATION_GROUP_ID | OR_TANK | TANK_ID | Unknown | No | No |  |
| 6 | UTILIZATION_GROUP_ID | OR_TANK_2 | TANK_ID | No | No | No |  |
| 7 | LOCATION_ID | ANALYTICS_SYSTEM_SETTINGS | FACILITY_ID | No | No | No |  |
| 7 | LOCATION_ID | ARPB_SA_SETTINGS | FACILITY_ID | No | No | No |  |
| 7 | LOCATION_ID | CLARITY_LOC | LOC_ID | Unknown | No | No |  |
| 7 | LOCATION_ID | CLARITY_LOC_2 | LOC_ID | Unknown | No | No |  |
| 7 | LOCATION_ID | CLARITY_POS | POS_ID | No | No | No |  |
| 7 | LOCATION_ID | CLARITY_POS_2 | POS_ID | No | No | No |  |
| 7 | LOCATION_ID | CLARITY_SA | SERV_AREA_ID | Unknown | No | No |  |
| 7 | LOCATION_ID | CL_LOC_HIERARCHY | LOC_ID | Unknown | No | No |  |
| 7 | LOCATION_ID | CV_PCI_D2B_SETTINGS | FACILITY_ID | No | No | No |  |
| 7 | LOCATION_ID | EAF_CLM_ALTADR_INF | FACILITY_ID | No | No | No |  |
| 7 | LOCATION_ID | EAF_CLM_RMT_SETUP | FACILITY_ID | No | No | No |  |
| 7 | LOCATION_ID | EAF_EXP_APPT_LOG | FACILITY_ID | No | No | No |  |
| 7 | LOCATION_ID | EAF_SEARCH_TERMS | FACILITY_ID | No | No | No |  |
| 7 | LOCATION_ID | ESCALATION_THRESH_SGL | FACILITY_ID | No | No | No |  |
| 7 | LOCATION_ID | FAC_CONNECT | FACILITY_ID | No | No | No |  |
| 7 | LOCATION_ID | FAC_DIRECT_ADDR | FACILITY_ID | Unknown | No | No |  |
| 7 | LOCATION_ID | HH_FAC_INFO | FACILITY_ID | No | No | No |  |
| 7 | LOCATION_ID | MC_FACILITY_GL_SEGMENTS | FACILITY_ID | No | No | No |  |

_(231 total; showing first 30)_
