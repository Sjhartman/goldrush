# MYC_MESG_RCP_POOL

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=MYC_MESG_RCP_POOL

## Description

This table holds the final pool recipients (HIP records) for this Patient Access Message (WMG) record.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | WMG |
| Release Version | SUMMER 2005 |
| May contain EHI? | No |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| MESSAGE_ID | VARCHAR (18) | The unique ID used to identify a web based chart system message record. |
| LINE | No | The line number used to identify each row of read data associated with an individual web based chart system message record. |
| CM_PHY_OWNER_ID | VARCHAR (25) | ID of the physical deployment owner for this record.  Physical owners will be where the data is hosted, either on the cross-over server or the owner deployment. |
| CM_LOG_OWNER_ID | VARCHAR (25) | ID of the logical deployment owner for this record.  Logical owners show the deployment where the record was created but doesn't represent if the record is a part of version skew. |
| IB_POOL_RECIP_ID | NUMERIC (18,0) | This stores the HIP ID of the final In Basket pool recipient. |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | MESSAGE_ID | MYC_MESG | MESSAGE_ID | Unknown | No | No |  |
| 1 | MESSAGE_ID | MYC_MESG_FRST_LAST | MESSAGE_ID | Unknown | Unknown | No |  |
| 1 | MESSAGE_ID | V_MYC_MESG | MESSAGE_ID | Unknown | Unknown | No |  |
| 3 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 4 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 4 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 4 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 5 | IB_POOL_RECIP_ID | CLARITY_HIP | REGISTRY_ID | Unknown | No | No |  |
| 5 | IB_POOL_RECIP_ID | IB_REG_BASE_DEPLY | REGISTRY_ID | No | No | No |  |
