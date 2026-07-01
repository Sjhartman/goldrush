# FDC_ID

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=FDC_ID

## Description

The FDC_ID table contains the system ID numbers for your flowsheet datacaptor information. Each flowsheet datacaptor may have multiple IDs; therefore, a line number is used to identify each identification number for a flowsheet datacaptor.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | FDC |
| Release Version | SPRING 2008 |
| May contain EHI? | No |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| RECORD_ID | NUMERIC (18,0) | The unique ID number assigned to the record. |
| LINE | No | This column holds the line number used to identify an ID for a flowsheet datacaptor record. Since flowsheet datacaptor records can have multiple IDs, a line number is used to identify an individual ID on that record. |
| CM_PHY_OWNER_ID | VARCHAR (25) | ID of the physical deployment owner for this record.  Physical owners will be where the data is hosted, either on the cross-over server or the owner deployment. |
| CM_LOG_OWNER_ID | VARCHAR (25) | ID of the logical deployment owner for this record.  Logical owners show the deployment where the record was created but doesn't represent if the record is a part of version skew. |
| MPI_ID_TYPE_ID | NUMERIC (18,0) | The MPI ID type associated with the flowsheet datacaptor ID. |
| MPI_ID | VARCHAR (50) | The MPI ID of the corresponding MPI ID type for the record. |
| MPI_FROM_DATE | DATETIME | The effective from date for the MPI ID on the record. |
| MPI_TO_DATE | DATETIME | The effective to date of the MPI ID on the record. |
| MPI_RET_CHK_PP_ID | NUMERIC (18,0) | MPI Retrieval Check Programming Point |
| MPI_RET_CHK_RULE_ID | VARCHAR (18) | MPI Retrieval check rule |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | RECORD_ID | FLOWSHEET_DC_INFO | RECORD_ID | No | No | No |  |
| 3 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 4 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 4 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 4 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 5 | MPI_ID_TYPE_ID | IDENTITY_ID_TYPE | ID_TYPE | No | No | No |  |
| 5 | MPI_ID_TYPE_ID | V_ZZLOV_DRG_TYPES | DRG_ID_TYPE_ID | Unknown | Unknown | No |  |
| 9 | MPI_RET_CHK_PP_ID | CLARITY_LPP | LPP_ID | Unknown | No | No |  |
| 10 | MPI_RET_CHK_RULE_ID | CLARITY_CER | RULE_ID | No | No | No |  |
| 10 | MPI_RET_CHK_RULE_ID | CL_CHRG_EDIT_RULE | RULE_ID | No | No | No |  |
