# RXNORM_CODES

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=RXNORM_CODES

## Description

This table contains the RxNorm code for the medications.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | ERX |
| Release Version | Rel 2012 |
| May contain EHI? | No |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| MEDICATION_ID | NUMERIC (18,0) | The unique identifier (.1 item) for the medication record. |
| LINE | INTEGER | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| RXNORM_CODE_LEVEL_C | INTEGER |  |
| RXNORM_CODE | VARCHAR (64) | This is the RxNorm code which represents this ERX at the level specified in RXNORM_CODE_LEVEL_C. |
| RXNORM_PRIMARY_YN | VARCHAR (1) |  |
| RXNORM_TERM_TYPE_C | INTEGER |  |
| RXNORM_HISTORIC_YN | VARCHAR (1) |  |

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
| 3 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 4 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 4 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 4 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 5 | RXNORM_CODE_LEVEL_C | ZC_RXNORM_CODE_LEVEL | RXNORM_CODE_LEVEL_C | No | No | No |  |
| 8 | RXNORM_TERM_TYPE_C | ZC_RXNORM_TERM_TYPE | RXNORM_TERM_TYPE_C | No | No | No |  |
