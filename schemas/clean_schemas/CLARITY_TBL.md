# CLARITY_TBL

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=CLARITY_TBL

## Description

This table contains a list of table (E0B) records that exist in the Clarity Compass along with pertinent information including the name, how often the table is loaded, how the table is loaded, related master file details, and Oracle?-related settings.

**Overflow table** for CLARITY_TBL_2 (93 cols). Contains additional columns for the same records — join on the shared primary key column.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | FULL |
| Load Frequency | WEEKLY - FULL |
| Chronicles INI | E0B |
| Release Version | MU6 - EPIC 2002 |
| May contain EHI? | No |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| TABLE_ID | VARCHAR (254) | The unique identifier (.1 item) for the table record. |
| TABLE_NAME | VARCHAR (254) | The name of the Clarity table. |
| EXTRACT_FILENAME | VARCHAR (254) | This column contains the file name that is used when the records are extracted into a flat file. |
| RELEASED_VERSION_C | NUMERIC (8,3) |  |
| LAST_MOD_VERSION_C | NUMERIC (8,3) |  |
| BS_TEMPLATE_ID | INTEGER |  |
| DEPENDENT_INI | VARCHAR (254) | This column contains the INI an incremental extract is dependent upon. During ETL, this information is necessary so the extracts wait for the build process of that corresponding INI to complete. |
| IS_JOB_DIVIDED_YN | VARCHAR (254) |  |
| IS_EXTRACTED_YN | VARCHAR (254) |  |
| LOAD_FREQUENCY | VARCHAR (254) |  |
| LOAD_TYPE | VARCHAR (254) |  |
| ROUTINE_NAME | VARCHAR (254) | The tag that is called by the Clarity Console to run the extract, if the table is not extracted using a KB_SQL query. |
| ORA_DATA_TBLSPACE *(deprecated)* | VARCHAR (254) |  |
| ORA_INDEX_TBLSPACE *(deprecated)* | VARCHAR (254) |  |
| ORA_OVRFL_TBLSPACE *(deprecated)* | VARCHAR (254) |  |
| IS_PARTITIONED_YN | VARCHAR (254) |  |
| PARTITION_TYPE | VARCHAR (254) |  |
| PARTITION_RANGE | VARCHAR (508) | A comma-delimited list that determines how the table will be partitioned. If the PARTITION_TYPE is RANGE, this will be a list of dates, if it is LIST, this will be a list of category IDs, if it is HASH, this will be a list of unique value buckets. This is only applicable if you use Oracle as your RDBMS. |
| PARTITION_KEY | VARCHAR (254) | The value from this column will be used, along with the PARTITION_RANGE, to determine which table partition the data should go in. This is only applicable if you use Oracle as your RDBMS. |
| IS_IX_ORGANIZED_YN | VARCHAR (254) |  |
| SUB_PARTITION_KEY | VARCHAR (254) | The value from this column will be used, along with the PARITION_KEY and PARTITION_RANGE, to determine which table partition the data should go in. This is only applicable if you use Oracle as your RDBMS. |
| SUB_PARTITION_VAL | VARCHAR (254) | A comma-delimited list that determines how the table partitions will be sub-divided. If the PARTITION_TYPE is RANGE-HASH, this will be a list of unique value buckets, if it is RANGE-LIST, this will be a list of category IDs. This is only applicable if you use Oracle as your RDBMS. |
| TBL_DESCRIPTOR | VARCHAR (254) | This is the descriptor value for the table.  The descriptor is used by other database records as pointers to table records. |
| TBL_DESCRIPTOR_OVR | VARCHAR (254) | This is the override descriptor value for the table.  The descriptor is used by other database records as pointers to table records.  If the override table descriptor is filled in for a particular record, the record is an override of the standard system released record. |
| TABLE_INTRODUCTION | VARCHAR (2000) | This column contains a brief but poignant description for the specified table. |
| CHRONICLES_MF | VARCHAR (254) | For standard Chronicles-based tables, this item stores the master file initials the table is extracted from. For non-Chronicles-based tables, this item may be null. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| IS_PRESERVED_YN | VARCHAR (1) |  |
| ORA_STG_TBLSPACE *(deprecated)* | VARCHAR (30) |  |
| ORA_STG_OVRFLTBLSP *(deprecated)* | VARCHAR (30) |  |
| TABLE_NOTES | VARCHAR (254) | This column, which will be preserved during upgrades, contains any customer-created notes for the table record. |
| DATA_RETAINED_YN | VARCHAR (1) |  |
| DEPRECATED_YN | VARCHAR (1) |  |
| EXTRACT_TEMPLATE_C | INTEGER |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | TABLE_ID | CLARITY_TBL_2 | TABLE_ID | No | No | No |  |
| 1 | TABLE_ID | EHI_DEPENDENCIES | TABLE_ID | No | No | No |  |
| 1 | TABLE_ID | EHI_TRACKING_TBL | TABLE_ID | No | No | No |  |
| 4 | RELEASED_VERSION_C | ZC_VERSION | VERSION_C | No | No | No |  |
| 5 | LAST_MOD_VERSION_C | ZC_VERSION | VERSION_C | No | No | No |  |
| 6 | BS_TEMPLATE_ID | ZC_EXTRACT_TEMPLATE | EXTRACT_TEMPLATE_C | No | No | No |  |
| 27 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 27 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 27 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 28 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 28 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 28 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 35 | EXTRACT_TEMPLATE_C | ZC_EXTRACT_TEMPLATE | EXTRACT_TEMPLATE_C | No | No | No |  |
