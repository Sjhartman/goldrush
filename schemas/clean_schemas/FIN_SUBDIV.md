# FIN_SUBDIV

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=FIN_SUBDIV

## Description

This table contains the extracted information of the Financial Subdivision.

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
| FIN_SUBDIV_ID | NUMERIC (18,0) | The unique identifier (.1 item) for the Financial Subdivision record. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| FIN_SUBDIV_NM | VARCHAR (200) | The name of financial subdivision. |
| ABBR | VARCHAR (12) | An abbreviation for this Financial Subdivision, since we update category lists. |
| FIN_DIV_ID | NUMERIC (18,0) | Financial division which this Financial Subdivision belongs to. |
| RPT_GRP1 | VARCHAR (254) | Free text report grouper for Financial Subdivision; one of ten. |
| RPT_GRP2 | VARCHAR (254) | Free text report grouper for Financial Subdivision; two of ten. |
| RPT_GRP3 | VARCHAR (254) | Free text report grouper for Financial Subdivision; two of ten. |
| RPT_GRP4 | VARCHAR (254) | Free text report grouper for Financial Subdivision; four of ten. |
| RPT_GRP5 | VARCHAR (254) | Free text report grouper for Financial Subdivision; five of ten. |
| RPT_GRP6 | VARCHAR (254) | Free text report grouper for Financial Subdivision; six of ten. |
| RPT_GRP7 | VARCHAR (254) | Free text report grouper for Financial Subdivision; seven of ten. |
| RPT_GRP8 | VARCHAR (254) | Free text report grouper for Financial Subdivision; eight of ten. |
| RPT_GRP9 | VARCHAR (254) | Free text report grouper for Financial Subdivision; nine of ten. |
| RPT_GRP10 | VARCHAR (254) | Free text report grouper for Financial Subdivision; ten of ten. |
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
| EXTERNAL_IDENT | VARCHAR (40) | The external ID for this financial subdivision record. |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | FIN_SUBDIV_ID | BILL_AREA | BILL_AREA_ID | Unknown | No | No |  |
| 1 | FIN_SUBDIV_ID | FIN_DIV | FIN_DIV_ID | No | No | No |  |
| 1 | FIN_SUBDIV_ID | V_BIL_ALL | BILL_AREA_ID | Unknown | Unknown | No |  |
| 1 | FIN_SUBDIV_ID | V_CUBE_D_BILL_AREA | BILL_AREA_ID | Unknown | Unknown | No |  |
| 2 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 2 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 2 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 3 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 6 | FIN_DIV_ID | BILL_AREA | BILL_AREA_ID | Unknown | No | No |  |
| 6 | FIN_DIV_ID | FIN_DIV | FIN_DIV_ID | No | No | No |  |
| 6 | FIN_DIV_ID | FIN_SUBDIV | FIN_SUBDIV_ID | No | No | No |  |
| 6 | FIN_DIV_ID | V_BIL_ALL | BILL_AREA_ID | Unknown | Unknown | No |  |
| 6 | FIN_DIV_ID | V_CUBE_D_BILL_AREA | BILL_AREA_ID | Unknown | Unknown | No |  |
| 17 | RPT_GRP11_C | ZC_FIN_SDIV_RPT_G1 | FIN_SDIV_RPT_G1_C | No | No | No |  |
| 18 | RPT_GRP12_C | ZC_FIN_SDIV_RPT_G2 | FIN_SDIV_RPT_G2_C | No | No | No |  |
| 19 | RPT_GRP13_C | ZC_FIN_SDIV_RPT_G3 | FIN_SDIV_RPT_G3_C | No | No | No |  |
| 20 | RPT_GRP14_C | ZC_FIN_SDIV_RPT_G4 | FIN_SDIV_RPT_G4_C | No | No | No |  |
| 21 | RPT_GRP15_C | ZC_FIN_SDIV_RPT_G5 | FIN_SDIV_RPT_G5_C | No | No | No |  |
| 22 | RPT_GRP16_C | ZC_FIN_SDIV_RPT_G6 | FIN_SDIV_RPT_G6_C | No | No | No |  |
| 23 | RPT_GRP17_C | ZC_FIN_SDIV_RPT_G7 | FIN_SDIV_RPT_G7_C | No | No | No |  |
| 24 | RPT_GRP18_C | ZC_FIN_SDIV_RPT_G8 | FIN_SDIV_RPT_G8_C | No | No | No |  |
| 25 | RPT_GRP19_C | ZC_FIN_SDIV_RPT_G9 | FIN_SDIV_RPT_G9_C | No | No | No |  |
| 26 | RPT_GRP20_C | ZC_FIN_SDIV_RP_G10 | FIN_SDIV_RP_G10_C | No | No | No |  |
