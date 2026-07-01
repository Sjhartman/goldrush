# BILL_AREA

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=BILL_AREA

## Description

This table contains the extracted information of the Bill Area master file (BIL).

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | BIL |
| Release Version | Summer 2009 |
| May contain EHI? | No |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| BILL_AREA_ID | NUMERIC (18,0) | The unique identifier (.1 item) for the bill area record. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| RECORD_NAME | VARCHAR (200) | The record name of this bill area. |
| RECORD_STATUS_C | INTEGER |  |
| ABBR | VARCHAR (12) | An abbreviation for this Bill Area, since we update category lists. |
| GL_PREFIX | VARCHAR (254) | The General Ledger prefix for this Bill Area |
| RPT_GRP_ONE | VARCHAR (254) | Free text report grouper for Bill Area; one of ten. |
| RPT_GRP_TWO | VARCHAR (254) | Free text report grouper for Bill Area; two of ten. |
| RPT_GRP_THREE | VARCHAR (254) | Free text report grouper for Bill Area; three of ten. |
| RPT_GRP_FOUR | VARCHAR (254) | Free text report grouper for Bill Area; four of ten. |
| RPT_GRP_FIVE | VARCHAR (254) | Free text report grouper for Bill Area; five of ten. |
| RPT_GRP_SIX | VARCHAR (254) | Free text report grouper for Bill Area; six of ten. |
| RPT_GRP_SEVEN | VARCHAR (254) | Free text report grouper for Bill Area; seven of ten. |
| RPT_GRP_EIGHT | VARCHAR (254) | Free text report grouper for Bill Area; eight of ten. |
| RPT_GRP_NINE | VARCHAR (254) | Free text report grouper for Bill Area; nine of ten. |
| RPT_GRP_TEN | VARCHAR (254) | Free text report grouper for Bill Area; ten of ten. |
| RPT_GRP_ELEVEN_C | INTEGER |  |
| RPT_GRP_TWELVE_C | INTEGER |  |
| RPT_GRP_THIRTEEN_C | INTEGER |  |
| RPT_GRP_FOURTEEN_C | INTEGER |  |
| RPT_GRP_FIFTEEN_C | INTEGER |  |
| RPT_GRP_SIXTEEN_C | INTEGER |  |
| RPT_GRP_SEVENTEEN_C | INTEGER |  |
| RPT_GRP_EIGHTEEN_C | INTEGER |  |
| RPT_GRP_NINETEEN_C | INTEGER |  |
| RPT_GRP_TWENTY_C | INTEGER |  |
| RECORD_CREATION_DT | DATETIME | Stores the date the record was created |
| INSTANT_OF_UPDATE | DATETIME (Local) | Stores the instant the record was last locked/unlocked |
| FIN_DIV_ID | NUMERIC (18,0) | Financial Division which this Bill Area belongs to. |
| FIN_SUBDIV_ID | NUMERIC (18,0) | Financial Subdivision which this Bill Area belongs to. |
| EFF_FROM_DATE | DATETIME | Date when the Bill Area becomes effective. |
| EFF_TO_DATE | DATETIME | Date when the Bill Area becomes ineffective. |
| EXTERNAL_IDENT | VARCHAR (40) | The external ID for this bill area record. |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | BILL_AREA_ID | FIN_DIV | FIN_DIV_ID | No | No | No |  |
| 1 | BILL_AREA_ID | FIN_SUBDIV | FIN_SUBDIV_ID | No | No | No |  |
| 1 | BILL_AREA_ID | V_BIL_ALL | BILL_AREA_ID | Unknown | Unknown | No |  |
| 1 | BILL_AREA_ID | V_CUBE_D_BILL_AREA | BILL_AREA_ID | Unknown | Unknown | No |  |
| 2 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 2 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 2 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 3 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 5 | RECORD_STATUS_C | ZC_RECORD_STATUS_2 | RECORD_STATUS_2_C | No | No | No |  |
| 5 | RECORD_STATUS_C | ZC_RECORD_STS | RECORD_STS_C | No | No | No |  |
| 18 | RPT_GRP_ELEVEN_C | ZC_RPT_GRP_11_BIL | RPT_GRP_11_BIL_C | No | No | No |  |
| 19 | RPT_GRP_TWELVE_C | ZC_RPT_GRP_12_BIL | RPT_GRP_12_BIL_C | No | No | No |  |
| 20 | RPT_GRP_THIRTEEN_C | ZC_RPT_GRP_13_BIL | RPT_GRP_13_BIL_C | No | No | No |  |
| 21 | RPT_GRP_FOURTEEN_C | ZC_RPT_GRP_14_BIL | RPT_GRP_14_BIL_C | No | No | No |  |
| 22 | RPT_GRP_FIFTEEN_C | ZC_RPT_GRP_15_BIL | RPT_GRP_15_BIL_C | No | No | No |  |
| 23 | RPT_GRP_SIXTEEN_C | ZC_RPT_GRP_16_BIL | RPT_GRP_16_BIL_C | No | No | No |  |
| 24 | RPT_GRP_SEVENTEEN_C | ZC_RPT_GRP_17_BIL | RPT_GRP_17_BIL_C | No | No | No |  |
| 25 | RPT_GRP_EIGHTEEN_C | ZC_RPT_GRP_18_BIL | RPT_GRP_18_BIL_C | No | No | No |  |
| 26 | RPT_GRP_NINETEEN_C | ZC_RPT_GRP_19_BIL | RPT_GRP_19_BIL_C | No | No | No |  |
| 27 | RPT_GRP_TWENTY_C | ZC_RPT_GRP_20_BIL | RPT_GRP_20_BIL_C | No | No | No |  |
| 30 | FIN_DIV_ID | BILL_AREA | BILL_AREA_ID | Unknown | No | No |  |
| 30 | FIN_DIV_ID | FIN_DIV | FIN_DIV_ID | No | No | No |  |
| 30 | FIN_DIV_ID | FIN_SUBDIV | FIN_SUBDIV_ID | No | No | No |  |
| 30 | FIN_DIV_ID | V_BIL_ALL | BILL_AREA_ID | Unknown | Unknown | No |  |
| 30 | FIN_DIV_ID | V_CUBE_D_BILL_AREA | BILL_AREA_ID | Unknown | Unknown | No |  |
| 31 | FIN_SUBDIV_ID | BILL_AREA | BILL_AREA_ID | Unknown | No | No |  |
| 31 | FIN_SUBDIV_ID | FIN_DIV | FIN_DIV_ID | No | No | No |  |
| 31 | FIN_SUBDIV_ID | FIN_SUBDIV | FIN_SUBDIV_ID | No | No | No |  |

_(32 total; showing first 30)_
