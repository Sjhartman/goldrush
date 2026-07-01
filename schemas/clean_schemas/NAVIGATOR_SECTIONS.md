# NAVIGATOR_SECTIONS

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=NAVIGATOR_SECTIONS

## Description

The NAVIGATOR_SECTIONS table contains information about navigators. Only navigators that are sections (I LVN 100=3) are included.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | LVN |
| Release Version | Rel February 2020 |
| May contain EHI? | No |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| NAVIGATOR_ID | NUMERIC (18,0) | The unique identifier (.1 item) for the navigator record. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record was extracted. This is only populated if you use IntraConnect. |
| SECTION_CAPTION | VARCHAR (192) | Display caption for the navigator section. |
| SECTION_NAME | VARCHAR (254) | Name of the navigator record. |
| SECTION_DESCRIPTOR | VARCHAR (192) | Descriptor for the navigator record. |
| RELEASED_NAVIGATOR_ID | NUMERIC (18,0) | This item stores the LVN ID of a released navigator section record that is similar to this record. Similarity is based on item 1020 (Section Handler ProgID) and item 1021 (Section View Path). This is used for improving efficiency reports, so that activity attributed to custom LVN records can be counted for metrics that use released records. Note that this won't be set for all custom records. |
| REL_NAVIGATOR_CALC_LOCAL_DTTM | DATETIME (Local) | The last time the system tried to attribute a released navigator section in I LVN 910 |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 2 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 2 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 3 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 7 | RELEASED_NAVIGATOR_ID | NAVIGATOR_SECTIONS | NAVIGATOR_ID | Yes | No | No |  |
