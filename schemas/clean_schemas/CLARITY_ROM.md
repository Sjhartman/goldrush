# CLARITY_ROM

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=CLARITY_ROM

## Description

This table reflects the information in the Hospital Rooms (ROM) master file.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | FULL |
| Load Frequency | WEEKLY - FULL |
| Chronicles INI | ROM |
| Release Version | EPIC 2000 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| ROOM_CSN_ID | NUMERIC (18,0) | The serial number for the room contact of the room record. This number is unique across all room contacts in the system. |
| ROOM_ID | VARCHAR (18) | The ID number of the room record. |
| ROM_CONT_DATE_REAL | FLOAT | This is a numeric representation of the date of this contact in your system. The integer portion of the number specifies the date of the contact. The digits after the decimal point indicate multiple visits on one day. |
| RECORD_STATE *(deprecated)* | VARCHAR (8) |  |
| ROOM_NAME | VARCHAR (200) | The name of the room. |
| CONTACT_DATE | DATETIME | The contact date of the room record. |
| ROOM_NUMBER | VARCHAR (192) | The external identifier for the room record. |
| ROOM_READY_YN | VARCHAR (1) |  |
| DEPARTMENT_ID | NUMERIC (18,0) | The ID number for the unit of the room record. |
| ACCOMMODATION_C | VARCHAR (66) |  |
| BED_POOL_MAX_NUM | INTEGER | The maximum number of pool beds of the room record. |
| BED_POOL_BED_NAME | VARCHAR (254) | The name for the pool beds of the room record. |
| BED_POOL_CENSUS_YN | VARCHAR (1) |  |
| END_CONT_DATE_REAL | FLOAT | The most recent contact date in decimal format. |
| WALK_ORDER | VARCHAR (40) | A number or word used to sort rooms, by their physical location in a unit, into a list used by caregivers to guide the order in which they see their patients. |
| STATION_ID | VARCHAR (18) | The ID number for the Chart Station used by the room |
| CM_PHY_OWNER_ID | VARCHAR (25) | ID of the physical deployment owner for this record.  Physical owners will be where the data is hosted, either on the cross-over server or the owner deployment. |
| CM_LOG_OWNER_ID | VARCHAR (25) | ID of the logical deployment owner for this record.  Logical owners show the deployment where the record was created but doesn't represent if the record is a part of version skew. |
| RECORD_STATE_C | INTEGER |  |
| IVR_NAME | VARCHAR (254) | This item holds the name of this room as it should be pronounced by the IVR. |
| BED_POOL_IN_HAAG_C | INTEGER |  |
| GO_LIVE_DATE | DATETIME | The date on which the room became available for patient admissions |
| PERMANENTLY_CLOSED_DATE | DATETIME | Indicates the date on which this room has closed and should no longer be used for patient encounters. |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| B-TREE INDEX | EIX_CLARITY_ROM_DEID | DEPARTMENT_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_CLARITY_ROM_STID | STATION_ID | 1 | Yes | Yes |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ROOM_CSN_ID | ED_ROOM_INFO_DYNAM | ROOM_CSN_ID | Unknown | No | No |  |
| 2 | ROOM_ID | ED_ROOM_INFO | ROOM_ID | Unknown | No | No |  |
| 9 | DEPARTMENT_ID | BH_DEP | DEPARTMENT_ID | No | No | No |  |
| 9 | DEPARTMENT_ID | CLARITY_DEP | DEPARTMENT_ID | No | No | No |  |
| 9 | DEPARTMENT_ID | CLARITY_DEP_2 | DEPARTMENT_ID | No | No | No |  |
| 9 | DEPARTMENT_ID | CLARITY_DEP_3 | DEPARTMENT_ID | No | No | No |  |
| 9 | DEPARTMENT_ID | CLARITY_DEP_4 | DEPARTMENT_ID | No | No | No |  |
| 9 | DEPARTMENT_ID | CLARITY_DEP_5 | DEPARTMENT_ID | No | No | No |  |
| 9 | DEPARTMENT_ID | CLARITY_DEP_MYC | DEPARTMENT_ID | No | No | No |  |
| 9 | DEPARTMENT_ID | DEPT_QUEUE_MSG_SETTINGS | DEPARTMENT_ID | No | No | No |  |
| 9 | DEPARTMENT_ID | DEPT_VERIFIED_INFO | DEPARTMENT_ID | No | No | No |  |
| 9 | DEPARTMENT_ID | DEP_BATCH_LTR_GEN | DEPARTMENT_ID | No | No | No |  |
| 9 | DEPARTMENT_ID | DEP_CE_SETTINGS | DEPARTMENT_ID | No | No | No |  |
| 9 | DEPARTMENT_ID | DP_HIDE_SENSITIVE_CONFIG | DEPARTMENT_ID | No | No | No |  |
| 9 | DEPARTMENT_ID | ED_ALRT_DFLT | DEPARTMENT_ID | No | No | No |  |
| 9 | DEPARTMENT_ID | ED_DEP_SETTINGS | DEP_ID | No | No | No |  |
| 9 | DEPARTMENT_ID | EXT_CAL_DEPT_CONFIG | DEPARTMENT_ID | No | No | No |  |
| 9 | DEPARTMENT_ID | VISIT_MODE_CONFIG_DEP | DEPARTMENT_ID | No | No | No |  |
| 9 | DEPARTMENT_ID | V_CUBE_D_DEPARTMENT | DEPARTMENT_ID | Unknown | Unknown | No |  |
| 9 | DEPARTMENT_ID | V_CUBE_D_DEP_LOC | DEPARTMENT_ID | Unknown | Unknown | No |  |
| 16 | STATION_ID | CT_STATION | STATION_ID | Unknown | No | No |  |
| 17 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 17 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 17 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 18 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 18 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 18 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 19 | RECORD_STATE_C | ZC_DEL_STATUS | DEL_STATUS_C | No | No | No |  |
| 19 | RECORD_STATE_C | ZC_EDG_REC_STAT | EDG_REC_STAT_C | No | No | No |  |
| 19 | RECORD_STATE_C | ZC_ERS_REC_STAT | RECORD_STATUS_C | No | No | No |  |

_(50 total; showing first 30)_
