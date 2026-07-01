# DESKTOP_ACTIVITY

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=DESKTOP_ACTIVITY

## Description

The DESKTOP_ACTIVITY table contains information about activity records used by Hyperspace.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | E2N |
| Release Version | Rel 2017 |
| May contain EHI? | No |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| ACTIVITY_ID | NUMERIC (18,0) | The unique identifier (.1 item) for the activity record. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| ACTIVITY_NAME | VARCHAR (200) | The name of the activity record. |
| DISPLAY_NAME | VARCHAR (508) | The display name of the activity record. |
| ACTIVITY_DESCRIPTOR | VARCHAR (200) | The descriptor of the activity record. |
| RELEASED_ACTIVITY_DESCRIPTOR | VARCHAR (192) | Stores descriptor of the released E2N activity record that is similar to this record |
| REL_DESCRIPTOR_CALC_LOCAL_DTTM | DATETIME (Local) | The last time the system tried to attribute a released activity descriptor in I E2N 910 |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 2 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 2 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 3 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
