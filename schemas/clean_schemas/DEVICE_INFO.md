# DEVICE_INFO

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=DEVICE_INFO

## Description

This table displays high-level information for device (DEV) records.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | DEV |
| Release Version | Summer 2009 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| DEVICE_ID | VARCHAR (40) | The unique identifier for the device record. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| DEVICE_NAME | VARCHAR (254) | The name for this device. |
| RECORD_STATE_C | INTEGER |  |
| DEVICE_DESC | VARCHAR (254) | Stores a free text description of the device. |
| DEVICE_TYPE_ID | NUMERIC (18,0) | The device type of this device. |
| DEVICE_GROUP_YN | VARCHAR (1) |  |
| DEVICE_GROUP_ID *(deprecated)* | VARCHAR (40) | *** Deprecated *** In table DEVICE_INFO, the column DEVICE_GROUP_ID (DEV/42) has been deprecated.  The deprecated column's content/data is no longer available since it is no longer extracted to Clarity. |
| LOAD_USING_GRPID_YN | VARCHAR (1) |  |
| FIXED_DEVICE_YN | VARCHAR (1) |  |
| DEVICE_IP | VARCHAR (75) | The IP address of the device, if it has one. |
| INTERFACE_TYPE_C | INTEGER |  |
| DEFAULT_INTERVAL | INTEGER | This column stores the interval between data points in the data validate activity. |
| CURRENT_INP_ID *(deprecated)* | VARCHAR (18) | *** Deprecated *** In table DEVICE_INFO, the column CURRENT_INP_ID (DEV/75) has been deprecated.  The deprecated table's content/data is no longer populated in Chronicles and is no longer available. |
| CURRENT_IN_USE | INTEGER | The number of devices currently in use. |
| DEV_UNIT_EDIT_YN *(deprecated)* | VARCHAR (1) |  |
| DEF_AUTOVALID_YN | VARCHAR (1) |  |
| CURRENT_FSD_ID | VARCHAR (18) | The current FSD for auto-validation. |
| CURRENT_FSD_DATE | DATETIME | The current FSD's date for auto validation. |
| AUTO_VAL_INTER_NUM *(deprecated)* | INTEGER | *** Deprecated *** In table DEVICE_INFO, the column AUTO_VAL_INTER_NUM (DEV/230) has been deprecated.  The deprecated column's content/data is no longer available since it is no longer extracted to Clarity   The interval of auto-validation. |
| PERFORM_AUTO_VAL_YN *(deprecated)* | VARCHAR (1) |  |
| DEFAULT_WORKSTN_ID | VARCHAR (18) | This column stores the LWS workstation associated with this device.  This setting affects only the Devices Visit Navigator section. Setting a workstation of type 1-Workstation allows this device to be added to the 'Quick-list' devices list of the navigator section for encounters opened on that workstation. This setting is only available for non-fixed devices. This setting only affects outpatient departments where a device in a room will be used for the patient in the room. For inpatient departments, the unit/room/bed settings should be used to automatically attach the appropriate devices. |
| SPECIALTY_AREA_C *(deprecated)* | INTEGER |  |
| NOADD_EDIT_DTTM *(deprecated)* | DATETIME | *** Deprecated *** In table DEVICE_INFO, the column NOADD_EDIT_DTTM (DEV/90030) has been deprecated. The deprecated column's data is no longer available since it is no longer populated in Chronicles. |
| NOADD_ITEMS_EDITED *(deprecated)* | VARCHAR (254) | *** Deprecated *** In table DEVICE_INFO, the column NOADD_ITEMS_EDITED (DEV/90040) has been deprecated. The deprecated column's data is no longer available since it is no longer populated in Chronicles. |
| HOSPITAL_ID | NUMERIC (18,0) | This item stores the EAF ID of the hospital that this device belongs to. |
| DEPARTMENT_ID | NUMERIC (18,0) | An item designed to hold the department for a fixed device. |
| FIXED_ROOM_ID | VARCHAR (18) | An item to hold the room a fixed device is located in. |
| FIXED_BED_ID | VARCHAR (18) | An item to hold the bed for fixed devices. |
| GROUPER_ID | VARCHAR (18) | An item to hold a VCG (grouper) record that is a list of departments this device is allowed in. |
| PATIENT_LOCATION_ID | NUMERIC (18,0) | The unique ID of the patient location (PLF) where a device can be found. A quick-add button makes it easy for a clinician to associate this device to a patient in the same location. |
| VENTILATOR_CLASS_C | INTEGER | Surrogate key used to uniquely identify rows in this (and only this) table on Cogito Cloud only, do not assume the surrogate key in this table will correspond to the surrogate key in another table |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 2 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 2 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 3 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 5 | RECORD_STATE_C | ZC_DEL_STATUS | DEL_STATUS_C | No | No | No |  |
| 5 | RECORD_STATE_C | ZC_EDG_REC_STAT | EDG_REC_STAT_C | No | No | No |  |
| 5 | RECORD_STATE_C | ZC_ERS_REC_STAT | RECORD_STATUS_C | No | No | No |  |
| 5 | RECORD_STATE_C | ZC_HCD_REC_STATE | HCD_REC_STATE_C | No | No | No |  |
| 5 | RECORD_STATE_C | ZC_HFL_RECORD_STAT | HFL_RECORD_STAT_C | No | No | No |  |
| 5 | RECORD_STATE_C | ZC_IMM_REC_STATUS | IMM_REC_STATUS_C | No | No | No |  |
| 5 | RECORD_STATE_C | ZC_LLB_STATUS | LLB_STATUS_C | No | No | No |  |
| 5 | RECORD_STATE_C | ZC_LMA_RECORD_STAT | LMA_RECORD_STAT_C | No | No | No |  |
| 5 | RECORD_STATE_C | ZC_MEM_REC_STATUS | MEM_REC_STATUS_C | No | No | No |  |
| 5 | RECORD_STATE_C | ZC_OR_REC_STATUS | OR_REC_STATUS_C | No | No | No |  |
| 5 | RECORD_STATE_C | ZC_PBA_REC_STAT | PBA_REC_STAT_C | No | No | No |  |
| 5 | RECORD_STATE_C | ZC_PROV_REC_STATE | PROV_REC_STATE_C | No | No | No |  |
| 5 | RECORD_STATE_C | ZC_RECORD_STATE_2 | RECORD_STATE_2_C | No | No | No |  |
| 5 | RECORD_STATE_C | ZC_RECORD_STATE_3 | RECORD_STATE_3_C | No | No | No |  |
| 5 | RECORD_STATE_C | ZC_RECORD_STATE_4 | RECORD_STATE_4_C | No | No | No |  |
| 5 | RECORD_STATE_C | ZC_RECORD_STATE_6 | RECORD_STATE_6_C | No | No | No |  |
| 5 | RECORD_STATE_C | ZC_RECORD_STATE_7 | RECORD_STATE_7_C | No | No | No |  |
| 5 | RECORD_STATE_C | ZC_RECORD_STAT_EPM | RECORD_STAT_EPM_C | No | No | No |  |
| 5 | RECORD_STATE_C | ZC_RECORD_STAT_EPP | RECORD_STAT_EPP_C | No | No | No |  |
| 5 | RECORD_STATE_C | ZC_RECORD_STAT_ETX | RECORD_STAT_ETX_C | No | No | No |  |
| 5 | RECORD_STATE_C | ZC_RECORD_STAT_HRV | RECORD_STAT_HRV_C | No | No | No |  |
| 5 | RECORD_STATE_C | ZC_RECORD_STAT_RMC | RECORD_STAT_RMC_C | No | No | No |  |
| 7 | DEVICE_TYPE_ID | DEVICE_TYPE_INFO | DEVICE_TYPE_ID | No | No | No |  |
| 13 | INTERFACE_TYPE_C | ZC_INTERFACE_TYPE | INTERFACE_TYPE_C | No | No | No |  |

_(90 total; showing first 30)_
