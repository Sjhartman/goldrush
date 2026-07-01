# RX_MED_NDC_CODE

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=RX_MED_NDC_CODE

## Description

This table contains medications' NDC codes.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | ERX |
| Release Version | EPIC 2002 |
| May contain EHI? | No |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| MEDICATION_ID | NUMERIC (18,0) | The unique ID for this medication record. |
| LINE | No | The line number for this item. |
| NDC_CODE | VARCHAR (50) | The unique, 12-digit NDC code for each manufacturer-supplied form (tablet, capsule, injection, etc.), strength, and packaged quantity of every drug. |
| CM_PHY_OWNER_ID | VARCHAR (25) | ID of the physical deployment owner for this record.  Physical owners will be where the data is hosted, either on the cross-over server or the owner deployment. |
| CM_LOG_OWNER_ID | VARCHAR (25) | ID of the logical deployment owner for this record.  Logical owners show the deployment where the record was created but doesn't represent if the record is a part of version skew. |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | MEDICATION_ID | CLARITY_MEDICATION | MEDICATION_ID | Unknown | No | No |  |
| 1 | MEDICATION_ID | MED_ADS_INFO | MEDICATION_ID | No | No | No |  |
| 1 | MEDICATION_ID | RX_MED_FIVE | MEDICATION_ID | No | No | No |  |
| 1 | MEDICATION_ID | RX_MED_FOUR | MEDICATION_ID | No | No | No |  |
| 1 | MEDICATION_ID | RX_MED_ONE | MEDICATION_ID | No | No | No |  |
| 1 | MEDICATION_ID | RX_MED_THREE | MEDICATION_ID | No | No | No |  |
| 1 | MEDICATION_ID | RX_MED_TWO | MEDICATION_ID | No | No | No |  |
| 1 | MEDICATION_ID | V_CUBE_D_MEDICATION | MEDICATION_ID | Unknown | Unknown | No |  |
| 4 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 4 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 4 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 5 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 5 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 5 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
