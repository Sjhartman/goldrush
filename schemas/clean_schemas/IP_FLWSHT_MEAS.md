# IP_FLWSHT_MEAS

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=IP_FLWSHT_MEAS

## Description

This table contains the patient-specific measurements from flowsheets.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | FSD |
| Release Version | EPIC 2002 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| FSD_ID | VARCHAR (18) | The unique ID for the flowsheet data record. |
| LINE | INTEGER | The line count for the item. |
| FLO_MEAS_ID | VARCHAR (18) | The unique ID for the flowsheet group/row associated with this reading. |
| OCCURANCE | INTEGER | If the flowsheet group/row appears multiple times, this will distinguish the occurrence. |
| RECORDED_TIME | DATETIME (Local) | The instant the reading was taken. |
| ENTRY_TIME | DATETIME (Local) | The instant the reading was entered. |
| TAKEN_USER_ID | VARCHAR (18) | The unique ID of the user taking the flowsheet readings. |
| ENTRY_USER_ID | VARCHAR (18) | The unique ID of the user entering the readings. |
| MEAS_VALUE | VARCHAR (2500) | The actual value of the flowsheet reading. |
| MEAS_COMMENT | VARCHAR (350) | The free text comments associated with the reading. |
| EDITED_LINE | INTEGER | The line number of the previous value of an edited record. |
| ISACCEPTED_YN | VARCHAR (1) |  |
| CM_PHY_OWNER_ID | VARCHAR (25) | ID of the physical deployment owner for this record.  Physical owners will be where the data is hosted, either on the cross-over server or the owner deployment. |
| CM_LOG_OWNER_ID | VARCHAR (25) | ID of the logical deployment owner for this record.  Logical owners show the deployment where the record was created but doesn't represent if the record is a part of version skew. |
| IP_SIGNIFICANT_YN | VARCHAR (1) |  |
| CAPTURE_DEVICE_ID | VARCHAR (40) | This item stores information of the Device ID for the device from which data is captured from. |
| RECEIVED_INSTANT | DATETIME (Local) | Instant at which value was received at the interface |
| CHART_CORR_ID | NUMERIC (18,0) | Stores the ID of the last Chart Correction action taken on a flowsheet cell. |
| AUTOVALIDATE_YN | VARCHAR (1) |  |
| NEEDS_COSIGN_C | INTEGER |  |
| FLT_ID | VARCHAR (18) | The unique ID of the flowsheet template (FLT) which was used to enter the data in this cell. |
| FLO_DAT_USED | NUMERIC (8,2) | This column stores the contact date (DAT) of the flowsheet row or group that is used to define the data. |
| MEAS_LOCATION | VARCHAR (508) | This item stores the location associated with the flowsheet data reading. |
| UPDATE_DATE | No | *** Deprecated *** In table IP_FLWSHT_MEAS, the column UPDATE_DATE has been deprecated.  This column should no longer be used to track updates to IP_FLWSHT_MEAS.  Flip "Track row updates?" to "Yes" in the Information Activity to enable capturing of row updates on IP_FLWSHT_MEAS using ESP_CR_ALTERED_ROWS.   The date and time this row was last updated (the last time it was extracted or this column was backfilled). |
| FLO_CNCT_DATE_REAL | No | This column converts the contact date (DAT) of the flowsheet group or row to DTE, based on the value in column FLO_DAT_USED. |
| USER_PENDED_BY_ID | VARCHAR (18) | User ID of the user who pended this flowsheet value. |
| INSTANT_PENDED_DTTM | DATETIME (Local) | Date/time at which a flowsheet value is pended. |
| ABNORMAL_C | INTEGER |  |
| THRDPRTY_SRC_C | INTEGER |  |
| PAT_REPORTED_STATUS_C | INTEGER |  |
| MYPT_ID | VARCHAR (18) | The MyChart account from which the data was entered. |
| DOCUMENTATION_SOURCE_C | INTEGER |  |
| IS_FROM_SPEECH_YN | No | Indicates whether a filed flowsheet value was entered using speech entry. |
| ABNORMAL_TYPE_C | INTEGER |  |
| FLO_NETWORKED_INI | VARCHAR (3) | The INI to which the value for this row is associated. |
| FLO_CATEGORY_INI *(deprecated)* | VARCHAR (3) |  |
| FLO_CATEGORY_ITEM *(deprecated)* | VARCHAR (20) |  |
| FLO_CATEGORY_VALUE *(deprecated)* | VARCHAR (66) |  |
| DOC_METHOD_C | INTEGER |  |
| MACRO_RECORD_ID | NUMERIC (18,0) | When the documentation method in FSD-1360 is 1-Value From Macro this is the macro HGM record ID. |
| DOCUMENTING_INPATIENT_DATA_ID | VARCHAR (18) | Stores the INP ID of the encounter where the property documentation occurred. This item will not be populated for non-property rows, or for any property values documented prior to the existence of this item. |
| SPEECH_ENTERED_METHOD_C | INTEGER |  |
| CLIENT_APP_TARGET_C | INTEGER |  |
| EXCLUDED_YN | VARCHAR (1) | Surrogate key used to uniquely identify rows in this (and only this) table on Cogito Cloud only, do not assume the surrogate key in this table will correspond to the surrogate key in another table |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| B-TREE INDEX | EIX_FLO_ID_ENTRY_TIME | ENTRY_TIME | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_FLO_ID_ENTRY_TIME | ENTRY_USER_ID | 2 | Yes | Yes |  |
| B-TREE INDEX | EIX_FLO_ID_ENTRY_TM | FLO_MEAS_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_FLO_ID_ENTRY_TM | ENTRY_TIME | 2 | Yes | Yes |  |
| B-TREE INDEX | EIX_FLO_ID_REC_TM | FLO_MEAS_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_FLO_ID_REC_TM | RECORDED_TIME | 2 | Yes | Yes |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | FSD_ID | IP_FLWSHT_REC | FSD_ID | No | No | No |  |
| 1 | FSD_ID | V_EHI_FSD_FILTER | FSD_ID | Unknown | Unknown | No |  |
| 3 | FLO_MEAS_ID | FLO_CNTX_INFO | ID | No | No | No |  |
| 3 | FLO_MEAS_ID | IP_FLO_GP_DATA | FLO_MEAS_ID | No | No | No |  |
| 3 | FLO_MEAS_ID | IP_FLO_GP_DATA_2 | FLO_MEAS_ID | No | No | No |  |
| 7 | TAKEN_USER_ID | CLARITY_EMP | USER_ID | Unknown | No | No |  |
| 7 | TAKEN_USER_ID | CLARITY_EMP_2 | USER_ID | Unknown | No | No |  |
| 7 | TAKEN_USER_ID | CLARITY_EMP_3 | USER_ID | Unknown | No | No |  |
| 7 | TAKEN_USER_ID | CLARITY_EMP_4 | USER_ID | No | No | No |  |
| 7 | TAKEN_USER_ID | CLARITY_EMP_DEMO | USER_ID | No | No | No |  |
| 7 | TAKEN_USER_ID | EMP_BASIC_INFO | USER_ID | No | No | No |  |
| 7 | TAKEN_USER_ID | EMP_DOC_SETTINGS | USER_NUMBER_ID | No | No | No |  |
| 7 | TAKEN_USER_ID | F_RX_USER | USER_ID | Unknown | Unknown | No |  |
| 7 | TAKEN_USER_ID | IB_MESSAGE_SETTINGS | USER_ID | No | No | No |  |
| 7 | TAKEN_USER_ID | LOGIN_INFO | USER_NUMBER_ID | No | No | No |  |
| 7 | TAKEN_USER_ID | QC_RESULTS_REVIEW | USER_NUMBER_ID | No | No | No |  |
| 7 | TAKEN_USER_ID | USER_SIDEBAR_RPT | USER_NUMBER_ID | Unknown | No | No |  |
| 7 | TAKEN_USER_ID | V_CUBE_D_USER | USER_ID | Unknown | Unknown | No |  |
| 7 | TAKEN_USER_ID | V_CUBE_RX_USER | USER_ID | Unknown | Unknown | No |  |
| 8 | ENTRY_USER_ID | CLARITY_EMP | USER_ID | Unknown | No | No |  |
| 8 | ENTRY_USER_ID | CLARITY_EMP_2 | USER_ID | Unknown | No | No |  |
| 8 | ENTRY_USER_ID | CLARITY_EMP_3 | USER_ID | Unknown | No | No |  |
| 8 | ENTRY_USER_ID | CLARITY_EMP_4 | USER_ID | No | No | No |  |
| 8 | ENTRY_USER_ID | CLARITY_EMP_DEMO | USER_ID | No | No | No |  |
| 8 | ENTRY_USER_ID | EMP_BASIC_INFO | USER_ID | No | No | No |  |
| 8 | ENTRY_USER_ID | EMP_DOC_SETTINGS | USER_NUMBER_ID | No | No | No |  |
| 8 | ENTRY_USER_ID | F_RX_USER | USER_ID | Unknown | Unknown | No |  |
| 8 | ENTRY_USER_ID | IB_MESSAGE_SETTINGS | USER_ID | No | No | No |  |
| 8 | ENTRY_USER_ID | LOGIN_INFO | USER_NUMBER_ID | No | No | No |  |
| 8 | ENTRY_USER_ID | QC_RESULTS_REVIEW | USER_NUMBER_ID | No | No | No |  |

_(76 total; showing first 30)_
