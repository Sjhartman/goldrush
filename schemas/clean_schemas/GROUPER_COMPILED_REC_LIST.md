# GROUPER_COMPILED_REC_LIST

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=GROUPER_COMPILED_REC_LIST

## Description

Contains the compiled list of records for a grouper.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | VCG |
| Release Version | Rel 2017 |
| May contain EHI? | No |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| COMPILED_GROUPER_ID | VARCHAR (18) | The unique identifier (VCG-.1) of the base record to which the compiled record is linked. Avoid using this column when linking to this table. Use BASE_GROUPER_ID instead. |
| LINE | INTEGER | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| GROUPER_RECORDS_VARCHAR_ID | VARCHAR (91) | Contains the IDs of the records contained in a compiled grouper record. This column contains record IDs for master files with both string- and numeric-based IDs. In IntraConnect environments, this column will contain record CIDs instead of IDs. |
| GROUPER_RECORDS_NUMERIC_ID | NUMERIC (18,0) | Contains the IDs of the records contained in a compiled grouper record. This column only contains record IDs for master files with numeric-based IDs. In IntraConnect environments, this column will contain record CIDs instead of IDs. |
| BASE_GROUPER_ID | VARCHAR (18) | The unique identifier (VCG-.1) of the base record to which the compiled record is linked. When linking to this table, use this column to join on. |
| COMPILED_CONTEXT | VARCHAR (3) | The context (master file) of the records contained in the compiled grouper. |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| B-TREE INDEX | EIX_VCG_COMP_REC_LIST_BASEID | BASE_GROUPER_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_VCG_COMP_REC_LIST_BASEID | GROUPER_RECORDS_NUMERIC_ID | 2 | Yes | Yes |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | COMPILED_GROUPER_ID | GROUPER_ITEMS | GROUPER_ID | No | No | No |  |
| 1 | COMPILED_GROUPER_ID | GROUPER_ITEMS_2 | GROUPER_ID | No | No | No |  |
| 3 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 4 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 4 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 4 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 7 | BASE_GROUPER_ID | GROUPER_ITEMS | GROUPER_ID | No | No | No |  |
| 7 | BASE_GROUPER_ID | GROUPER_ITEMS_2 | GROUPER_ID | No | No | No |  |
