# CLARITY_BED

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=CLARITY_BED

## Description

This table reflects the data in the Hospital Beds (BED) master file.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | FULL |
| Load Frequency | WEEKLY - FULL |
| Chronicles INI | BED |
| Release Version | EPIC 2000 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| BED_CSN_ID | NUMERIC (18,0) | The serial number for the bed contact of the bed record. This number is unique across all bed contacts in the system. |
| BED_ID | VARCHAR (18) | The ID number of the bed record. |
| BED_CONT_DATE_REAL | FLOAT | This is a numeric representation of the date of this contact in your system. The integer portion of the number specifies the date of the contact. The digits after the decimal point indicate multiple visits on one day. |
| BED_LABEL | VARCHAR (256) | The name of the bed. |
| RECORD_STATE | VARCHAR (64) |  |
| CONTACT_DATE | DATETIME | The contact date of the bed record. |
| ROOM_ID | VARCHAR (18) | The ID number for the room of the bed record. |
| TELEPHONE_NUMBER | VARCHAR (50) | The phone number of the bed record. |
| CENSUS_INCLUSN_YN | VARCHAR (1) |  |
| BED_STATUS_C | VARCHAR (66) |  |
| POOL_BED_YN | VARCHAR (1) |  |
| END_CONT_DATE_REAL | FLOAT | The most recent contact date in decimal format. |
| ACCOMMODATION_C | VARCHAR (66) |  |
| SVC_PRIORITY_C | INTEGER |  |
| DFLT_SVC_PRI_C | INTEGER |  |
| ADDL_FLAG_C | INTEGER |  |
| EVS_OPT_OUT_YN | VARCHAR (1) |  |
| PERIOPERATIVE_YN | VARCHAR (1) |  |
| ED_HOLD_YN | VARCHAR (1) |  |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| ED_HOLD_EX_DTTM | 49010 | This table holds the expiration date and time for ED hold. |
| ED_HOLD_ARR_MODE_C | VARCHAR (66) |  |
| ED_HOLD_CREATE_DTTM | DATETIME (Local) | This table contains the ED hold creation times. |
| HAAG_INCLUDE_C | INTEGER |  |
| IVR_NAME | VARCHAR (254) | This item holds the name of this bed as it should be pronounced by the IVR. |
| IS_BUNK_C | INTEGER |  |
| LEVEL_OF_CARE_GROUPER_C | INTEGER |  |
| SERVICE_GROUPER_C | INTEGER |  |
| GO_LIVE_DATE | DATETIME | The date on which the bed became available for patient admissions |
| PERMANENTLY_CLOSED_DATE | DATETIME | Indicates the date on which this bed has closed and should no longer be used for patient encounters. |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | BED_CSN_ID | BED_OVERTIME | BED_CSN_ID | No | No | No |  |
| 7 | ROOM_ID | ED_ROOM_INFO | ROOM_ID | Unknown | No | No |  |
| 10 | BED_STATUS_C | ZC_BED_STATUS | BED_STATUS_C | No | No | No |  |
| 14 | SVC_PRIORITY_C | ZC_SVC_PRIORITY | SVC_PRIORITY_C | No | No | No |  |
| 15 | DFLT_SVC_PRI_C | ZC_SVC_PRIORITY | SVC_PRIORITY_C | No | No | No |  |
| 16 | ADDL_FLAG_C | ZC_ADDL_FLAG | ADDL_FLAG_C | No | No | No |  |
| 20 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 20 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 20 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 21 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 21 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 21 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 23 | ED_HOLD_ARR_MODE_C | ZC_ARRIV_MEANS | MEANS_OF_ARRV_C | No | No | No |  |
| 25 | HAAG_INCLUDE_C | ZC_HAAG_INCLUDE | HAAG_INCLUDE_C | No | No | No |  |
| 27 | IS_BUNK_C | ZC_IS_BUNK | IS_BUNK_C | No | No | No |  |
| 28 | LEVEL_OF_CARE_GROUPER_C | ZC_LEVEL_OF_CARE_GROUPER | LEVEL_OF_CARE_GROUPER_C | No | No | No |  |
| 29 | SERVICE_GROUPER_C | ZC_SERVICE_GROUPER | SERVICE_GROUPER_C | No | No | No |  |
