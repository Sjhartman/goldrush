# GENE_IDENT

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=GENE_IDENT

## Description

Version-independent information about a gene record such as its name or HUGO Gene Nomenclature (HGNC) ID.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | GEN |
| Release Version | Rel February 2022 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| GENE_ID | NUMERIC (18,0) | The unique identifier (.1 item) for the gene record. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| RECORD_SYMBOL | VARCHAR (200) | The current symbol for this gene. In cases of disagreement, the current HGNC symbol will be used. |
| RECORD_STATUS_2_C | INTEGER |  |
| CURR_CONTACT_DATE_REAL | FLOAT | The date when the gene was last updated. |
| GENE_HGNC_IDENT | INTEGER | HGNC ID. A unique ID created by the Hugo Gene Nomenclature Committee (HGNC) for every approved symbol. |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 2 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 2 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 3 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 5 | RECORD_STATUS_2_C | ZC_RECORD_STATUS_2 | RECORD_STATUS_2_C | No | No | No |  |
| 5 | RECORD_STATUS_2_C | ZC_RECORD_STS | RECORD_STS_C | No | No | No |  |
