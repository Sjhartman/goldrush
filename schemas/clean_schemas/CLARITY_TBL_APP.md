# CLARITY_TBL_APP

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=CLARITY_TBL_APP

## Description

Contains a list of applications that use a given table record along with whether the table is marked as core.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | FULL |
| Load Frequency | WEEKLY - FULL |
| Chronicles INI | E0B |
| Release Version | MU6 - EPIC 2002 |
| May contain EHI? | No |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| TABLE_ID | VARCHAR (254) | The unique identifier (.1 item) for the table record. |
| LINE | INTEGER | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| APPLICATION_C | INTEGER |  |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this Chronicles record. This is populated only if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| CORE_TABLE_YN | VARCHAR (1) |  |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| BITMAP INDEX | EIX_CLARITY_TBL_APP__AP_C | APPLICATION_C | 1 | Yes | Yes |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | TABLE_ID | CLARITY_TBL | TABLE_ID | No | No | No |  |
| 1 | TABLE_ID | CLARITY_TBL_2 | TABLE_ID | No | No | No |  |
| 1 | TABLE_ID | EHI_DEPENDENCIES | TABLE_ID | No | No | No |  |
| 1 | TABLE_ID | EHI_TRACKING_TBL | TABLE_ID | No | No | No |  |
| 3 | APPLICATION_C | ZC_ACTIVE_APPS | ACTIVE_APPS_C | No | No | No |  |
| 3 | APPLICATION_C | ZC_APPLICATION | APPLICATION_C | No | No | No |  |
| 4 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 4 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 4 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 5 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 5 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 5 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
