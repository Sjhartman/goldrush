# TEST_EXPIRATION

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=TEST_EXPIRATION

## Description

Test expiration times.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | FULL |
| Load Frequency | WEEKLY - FULL |
| Chronicles INI | OVT |
| Release Version | SPRING 2007 |
| May contain EHI? | No |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| TEST_ID | VARCHAR (18) | The unique ID of the test record. |
| LINE | No | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| EFFECTIVE_DATE | DATETIME | The effective date of this contact in calendar format. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| CM_CT_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this contact. This is only populated if you use IntraConnect. |
| EXP_TIME | INTEGER | The amount of time from specimen collection until it expires |
| EXP_TIME_UNIT_C | INTEGER |  |
| EXP_NEAR | INTEGER | The amount of time before a test expires when it is considered near expiring. |
| EXP_NEAR_UNIT_C | INTEGER |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | TEST_ID | PROTOCOL_DB_MAIN | PROTOCOL_ID | Unknown | No | No |  |
| 1 | TEST_ID | TEST_MSTR_DB_MAIN | TEST_ID | Unknown | No | No |  |
| 1 | TEST_ID | ZC_QC_TEST_CAT_ID | QC_TEST_CAT_ID_C | Unknown | Unknown | No |  |
| 4 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 4 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 4 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 5 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 5 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 5 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 6 | CM_CT_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 6 | CM_CT_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 6 | CM_CT_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 8 | EXP_TIME_UNIT_C | ZC_DFLT_UNIT | DFLT_UNIT_C | No | No | No |  |
| 10 | EXP_NEAR_UNIT_C | ZC_DFLT_UNIT | DFLT_UNIT_C | No | No | No |  |
