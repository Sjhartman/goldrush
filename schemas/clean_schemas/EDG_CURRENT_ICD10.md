# EDG_CURRENT_ICD10

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=EDG_CURRENT_ICD10

## Description

Diagnosis terms can map to multiple codes in a code set. This table discretely lists the mapped codes for term-type diagnoses. Code-type diagnoses will also have a row in this table if the code is in ICD-10-CM.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | EDG |
| Release Version | Rel 2010 |
| May contain EHI? | No |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| DX_ID | NUMERIC (18,0) | The unique identifier (.1 item) for the diagnosis record. |
| LINE | INTEGER | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| CODE | VARCHAR (254) | For term-type records, this is the record's current mapped ICD-10-CM code. Code-type records of the ICD-10-CM code set will have a value here as well. |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | DX_ID | ADVERSE_EVENT_TERM_INFO | DX_ID | No | No | No |  |
| 1 | DX_ID | CLARITY_EDG | DX_ID | Unknown | No | No |  |
| 1 | DX_ID | EDG_DBC_INFO | DX_ID | No | No | No |  |
| 1 | DX_ID | V_CUBE_D_DIAGNOSIS | DIAGNOSIS_ID | Unknown | Unknown | No |  |
| 3 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 4 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 4 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 4 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
