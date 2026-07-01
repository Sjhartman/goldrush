# FLOWSHEET

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=FLOWSHEET

## Description

This table contains review flowsheet or synopsis records from your system. It includes the flowsheet (or synopsis) ID, the flowsheet name, the flowsheet's short title, and whether the record is a review flowsheet or synopsis record.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | FSH |
| Release Version | Rel 2010 |
| May contain EHI? | No |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| FLOWSHEET_ID | NUMERIC (18,0) | This is a unique numerical number that each flowsheet record is given to help differentiate it from other flowsheet records |
| CM_PHY_OWNER_ID | VARCHAR (25) | This community's physical owner of this record |
| CM_LOG_OWNER_ID | VARCHAR (25) | The community's logical owner of this record |
| FLOWSHEET_NAME | VARCHAR (254) | This is the record name of the flowsheet. |
| SHORT_TITLE | VARCHAR (254) | This is considered the "Display Name" of the FSH Master File.  If you want something short to appear instead of the record name, populate this item for a flowsheet record. |
| FLOWSHEET_TYPE_C | INTEGER |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 2 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 2 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 3 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 6 | FLOWSHEET_TYPE_C | ZC_FLOWSHEET_TYPE | FLOWSHEET_TYPE_C | No | No | No |  |
