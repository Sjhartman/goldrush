# VESSEL_DOC

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=VESSEL_DOC

## Description

Table contains items that represents anatomy of body (vessel related items).

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | VEL |
| Release Version | Summer 2009 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| RECORD_ID | NUMERIC (18,0) | The unique identifier (.1 item) for the anatomy record. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| RECORD_NAME | VARCHAR (200) | Stores record name (.2) |
| RECORD_STATUS_C | INTEGER |  |
| ANATOMY_TYPE_C | INTEGER |  |
| ANATOMY_EXT_NAME | VARCHAR (254) | Indicates the external name used for the anatomy in reports and the user interface. |
| ANATOMY_ABBREV | VARCHAR (40) | Indicates anatomy abbreviation used in the user interface |
| ANATOMY_IDENTIFIER | VARCHAR (254) | Indicates anatomy internal identifier, this is used by the CAST tool. |
| VESSEL_LOCATION_C | INTEGER |  |
| RECORD_CREATION_DT | DATETIME | Stores the date the record was created |
| INSTANT_OF_UPD_DTTM | DATETIME (Local) | Stores the instant the record was last locked/unlocked |
| ORTHO_LATERALITY_C | INTEGER |  |
| ORTHO_SURG_LOC_C | INTEGER |  |
| ORTHO_RAD_LOC_C | VARCHAR (66) |  |
| ORGAN_C | INTEGER |  |
| RT_LOCATION_CODE | VARCHAR (50) | Stores the concept code that represents a radiotherapy body location. |
| RT_LOCATION_CODESYSTEM_C | INTEGER | Surrogate key used to uniquely identify rows in this (and only this) table on Cogito Cloud only, do not assume the surrogate key in this table will correspond to the surrogate key in another table |
| ANATOMY_PAT_FRIENDLY_NAME | VARCHAR (254) | Item contains a name for the anatomical region that is suitable to show to patients |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | RECORD_ID | TOOTH_TEMPLATE | RECORD_ID | No | No | No |  |
| 2 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 2 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 2 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 3 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 5 | RECORD_STATUS_C | ZC_RECORD_STATUS_2 | RECORD_STATUS_2_C | No | No | No |  |
| 5 | RECORD_STATUS_C | ZC_RECORD_STS | RECORD_STS_C | No | No | No |  |
| 6 | ANATOMY_TYPE_C | ZC_ANATOMY_TYPE | ANATOMY_TYPE_C | No | No | No |  |
| 10 | VESSEL_LOCATION_C | ZC_VESSEL_LOCATION | VESSEL_LOCATION_C | No | No | No |  |
| 13 | ORTHO_LATERALITY_C | ZC_ORTHO_LATERALITY | ORTHO_LATERALITY_C | No | No | No |  |
| 14 | ORTHO_SURG_LOC_C | ZC_OR_OP_REGION | OPERATING_REGION_C | No | No | No |  |
| 15 | ORTHO_RAD_LOC_C | ZC_ANATOMY_REGION | ANATOMY_REGION_C | No | No | No |  |
| 16 | ORGAN_C | ZC_TX_CLASS | TX_CLASS_C | No | No | No |  |
| 18 | RT_LOCATION_CODESYSTEM_C | ZC_CODESYSTEM | CODESYSTEM_C | No | No | No |  |
