# FIN_DIV

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=FIN_DIV

## Description

This table contains the extracted information of the Financial Division.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | BIL |
| Release Version | Rel 2012 |
| May contain EHI? | No |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| FIN_DIV_ID | NUMERIC (18,0) | The unique identifier (.1 item) for the financial division record. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| FIN_DIV_NM | VARCHAR (200) | The name of financial division. |
| ABBR | VARCHAR (12) | An abbreviation for this record, since we update category lists. |
| RPT_GRP_1 | VARCHAR (254) | Free text report grouper for Financial Division; one of ten. |
| RPT_GRP_2 | VARCHAR (254) | Free text report grouper for Financial Division; two of ten. |
| RPT_GRP_3 | VARCHAR (254) | Free text report grouper for Financial Division; three of ten. |
| RPT_GRP_4 | VARCHAR (254) | Free text report grouper for Financial Division; four of ten. |
| RPT_GRP_5 | VARCHAR (254) | Free text report grouper for Financial Division; five of ten. |
| RPT_GRP_6 | VARCHAR (254) | Free text report grouper for Financial Division; six of ten. |
| RPT_GRP_7 | VARCHAR (254) | Free text report grouper for Financial Division; seven of ten. |
| RPT_GRP_8 | VARCHAR (254) | Free text report grouper for Financial Division; eight of ten. |
| RPT_GRP_9 | VARCHAR (254) | Free text report grouper for Financial Division; nine of ten. |
| RPT_GRP_10 | VARCHAR (254) | Free text report grouper for Financial Division; ten of ten. |
| RPT_GRP11_C | INTEGER |  |
| RPT_GRP12_C | INTEGER |  |
| RPT_GRP13_C | INTEGER |  |
| RPT_GRP14_C | INTEGER |  |
| RPT_GRP15_C | INTEGER |  |
| RPT_GRP16_C | INTEGER |  |
| RPT_GRP17_C | INTEGER |  |
| RPT_GRP18_C | INTEGER |  |
| RPT_GRP19_C | INTEGER |  |
| RPT_GRP20_C | INTEGER |  |
| EXTERNAL_IDENT | VARCHAR (40) | The external ID for this financial division record. |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | FIN_DIV_ID | BILL_AREA | BILL_AREA_ID | Unknown | No | No |  |
| 1 | FIN_DIV_ID | FIN_SUBDIV | FIN_SUBDIV_ID | No | No | No |  |
| 1 | FIN_DIV_ID | V_BIL_ALL | BILL_AREA_ID | Unknown | Unknown | No |  |
| 1 | FIN_DIV_ID | V_CUBE_D_BILL_AREA | BILL_AREA_ID | Unknown | Unknown | No |  |
| 2 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 2 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 2 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 3 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 16 | RPT_GRP11_C | ZC_FIN_DIV_RPT_GRP | FIN_DIV_RPT_GRP_C | No | No | No |  |
| 17 | RPT_GRP12_C | ZC_FIN_DIV_RPT_G_2 | FIN_DIV_RPT_G_2_C | No | No | No |  |
| 18 | RPT_GRP13_C | ZC_FIN_DIV_RPT_G_3 | FIN_DIV_RPT_G_3_C | No | No | No |  |
| 19 | RPT_GRP14_C | ZC_FIN_DIV_RPT_G_4 | FIN_DIV_RPT_G_4_C | No | No | No |  |
| 20 | RPT_GRP15_C | ZC_FIN_DIV_RPT_G_5 | FIN_DIV_RPT_G_5_C | No | No | No |  |
| 21 | RPT_GRP16_C | ZC_FIN_DIV_RPT_G_6 | FIN_DIV_RPT_G_6_C | No | No | No |  |
| 22 | RPT_GRP17_C | ZC_FIN_DIV_RPT_G_7 | FIN_DIV_RPT_G_7_C | No | No | No |  |
| 23 | RPT_GRP18_C | ZC_FIN_DIV_RPT_G_10 | FIN_DIV_RPT_G_10_C | No | No | No |  |
| 24 | RPT_GRP19_C | ZC_FIN_DIV_RPT_G_8 | FIN_DIV_RPT_G_8_C | No | No | No |  |
| 25 | RPT_GRP20_C | ZC_FIN_DIV_RPT_G_9 | FIN_DIV_RPT_G_9_C | No | No | No |  |
