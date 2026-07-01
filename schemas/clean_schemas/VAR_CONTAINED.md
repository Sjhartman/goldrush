# VAR_CONTAINED

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=VAR_CONTAINED

## Description

The VAR_CONTAINED table contains the list of simple or complex variants contained within a complex variant.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | VAR |
| Release Version | Rel 2018 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| VARIANT_ID | NUMERIC (18,0) | The unique identifier for the variant record. |
| LINE | INTEGER | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| CONTD_VARIANT_ID | NUMERIC (18,0) | The unique ID of the variant contained within this complex variant. |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| B-TREE INDEX | EIX_CONTD_VARIANT | CONTD_VARIANT_ID | 1 | Yes | Yes |  |

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
| 5 | CONTD_VARIANT_ID | VARIANT | VARIANT_ID | No | No | No |  |
