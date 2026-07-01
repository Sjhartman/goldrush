# PROVTEAM_REC_INFO

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=PROVTEAM_REC_INFO

## Description

This table extracts the basic record information for the provider team including the name and the date the record was created. Provider teams are groups of providers that can be assigned to a patient.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | PCT |
| Release Version | Summer 2009 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| ID | NUMERIC (18,0) | The unique ID of the team record for this row. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| RECORD_NAME | VARCHAR (200) | The name of the record. |
| RECORD_STATUS_C | INTEGER |  |
| RECORD_TYPE_C | INTEGER |  |
| CURRENT_CONTACT | NUMERIC (18,0) | The contact serial number for the current PCT contact. |
| RECORD_CREATION_DT | DATETIME | This stores the date the record was created. |
| INSTANT_OF_UPD_TM | DATETIME (Local) | This stores the instant the record was last locked/unlocked. |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 2 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 2 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 3 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 5 | RECORD_STATUS_C | ZC_RECORD_STATUS_2 | RECORD_STATUS_2_C | No | No | No |  |
| 5 | RECORD_STATUS_C | ZC_RECORD_STS | RECORD_STS_C | No | No | No |  |
| 6 | RECORD_TYPE_C | ZC_RECORD_TYPE_8 | RECORD_TYPE_8_C | No | No | No |  |
