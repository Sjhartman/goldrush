# VAR_REPEAT_EXPANSION

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=VAR_REPEAT_EXPANSION

## Description

This table stores information about repeat expansion variants, including the repeated nucleotides and the number of times the nucleotides are repeated.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | VAR |
| Release Version | Rel November 2022 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| VARIANT_ID | NUMERIC (18,0) | The unique identifier (.1 item) for the variant record. |
| LINE | INTEGER | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| REPEAT_NUCLEOTIDES | VARCHAR (100) | The sequence of the nucleotides in a single unit of the repeat expansion variant. |
| REPEAT_NUMBER | INTEGER | The number of times a sequence of nucleotides (in REPEAT_NUCLEOTIDES) is repeated. |
| REPEAT_NUMBER_LEADING | INTEGER | Repeat number is to record the repeated number in repeat expansion variant. For structured numeric values, this is the number used with the operator (or leading number if there is a range). |
| REPEAT_NUMBER_TRAILING | INTEGER | Repeat number is to record the repeated number in repeat expansion variant. For structured numeric values, this is the upper bound value if there is a range. Otherwise, this item is not populated. |
| RPT_NUM_COMPARE_OPERATO_C | INTEGER |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | VARIANT_ID | VARIANT | VARIANT_ID | No | No | No |  |
| 3 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 4 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 4 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 4 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 9 | RPT_NUM_COMPARE_OPERATO_C | ZC_COMPARE_OPERATO | COMPARE_OPERATO_C | No | No | No |  |
