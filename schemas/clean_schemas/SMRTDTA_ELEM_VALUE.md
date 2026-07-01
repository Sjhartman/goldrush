# SMRTDTA_ELEM_VALUE

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=SMRTDTA_ELEM_VALUE

## Description

The SMRTDTA_ELEM_VALUE table stores SmartData element values entered by users through SmartForms, SmartTools and other documentation tools that file discrete data to SmartData elements. The metadata concerning the entry of these values is stored in the SMRTDTA_ELEM_DATA table.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | HLV |
| Release Version | Summer 2009 |
| May contain EHI? | No |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| HLV_ID | NUMERIC (18,0) | The unique ID of the SmartData element value. |
| LINE | No | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| SMRTDTA_ELEM_VALUE | VARCHAR (4000) | The SmartData element value entered by a user through a SmartForm, SmartTool or other documentation tool that files discrete data to SmartData elements. If the value entered is a record ID or category value and you use IntraConnect, this is the Community ID (CID). Note: This column only extracts the first 3000 characters of data. |
| ELEM_NW_ID_VAL_NUM | NUMERIC (18,0) | The SmartData element value entered by a user through a SmartForm, SmartTool or other documentation tool that files discrete data to SmartData elements. This column is only populated if that data is a record ID or category value and is of numeric format. If you use IntraConnect, this is the Community ID (CID). |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | HLV_ID | SMRTDTA_ELEM_AIEXTRACTED | HLV_ID | No | No | No |  |
| 1 | HLV_ID | SMRTDTA_ELEM_AUTH | HLV_ID | No | No | No |  |
| 1 | HLV_ID | SMRTDTA_ELEM_BEREAVE | HLV_ID | No | No | No |  |
| 1 | HLV_ID | SMRTDTA_ELEM_CONCEPT | HLV_ID | No | No | No |  |
| 1 | HLV_ID | SMRTDTA_ELEM_CONTENT_REV | HLV_ID | No | No | No |  |
| 1 | HLV_ID | SMRTDTA_ELEM_CUST_SERVICE | HLV_ID | No | No | No |  |
| 1 | HLV_ID | SMRTDTA_ELEM_DATA | HLV_ID | No | No | No |  |
| 1 | HLV_ID | SMRTDTA_ELEM_DATASET | HLV_ID | No | No | No |  |
| 1 | HLV_ID | SMRTDTA_ELEM_DEFICIENCY | HLV_ID | No | No | No |  |
| 1 | HLV_ID | SMRTDTA_ELEM_DOCUMENT | HLV_ID | No | No | No |  |
| 1 | HLV_ID | SMRTDTA_ELEM_DONOR | HLV_ID | Unknown | No | No |  |
| 1 | HLV_ID | SMRTDTA_ELEM_ENCOUNTER | HLV_ID | No | No | No |  |
| 1 | HLV_ID | SMRTDTA_ELEM_EPISODE | HLV_ID | No | No | No |  |
| 1 | HLV_ID | SMRTDTA_ELEM_EPISODE_GRP | HLV_ID | No | No | No |  |
| 1 | HLV_ID | SMRTDTA_ELEM_FIN_ASST_CAS | HLV_ID | No | No | No |  |
| 1 | HLV_ID | SMRTDTA_ELEM_HISTORY | HLV_ID | No | No | No |  |
| 1 | HLV_ID | SMRTDTA_ELEM_INFERT_CYCLE | HLV_ID | No | No | No |  |
| 1 | HLV_ID | SMRTDTA_ELEM_LAB_RESULT | HLV_ID | No | No | No |  |
| 1 | HLV_ID | SMRTDTA_ELEM_NOTE | HLV_ID | No | No | No |  |
| 1 | HLV_ID | SMRTDTA_ELEM_ORDER | HLV_ID | No | No | No |  |
| 1 | HLV_ID | SMRTDTA_ELEM_ORGAN | HLV_ID | No | No | No |  |
| 1 | HLV_ID | SMRTDTA_ELEM_PATIENT | HLV_ID | No | No | No |  |
| 1 | HLV_ID | SMRTDTA_ELEM_PAT_ENTERED | HLV_ID | No | No | No |  |
| 1 | HLV_ID | SMRTDTA_ELEM_PROBLEM | HLV_ID | No | No | No |  |
| 1 | HLV_ID | SMRTDTA_ELEM_REGISTRY | HLV_ID | No | No | No |  |
| 1 | HLV_ID | SMRTDTA_ELEM_RESULT | HLV_ID | No | No | No |  |
| 1 | HLV_ID | SMRTDTA_ELEM_RESULT_CNCT | HLV_ID | No | No | No |  |
| 1 | HLV_ID | SMRTDTA_ELEM_STAGE | HLV_ID | No | No | No |  |
| 1 | HLV_ID | SMRTDTA_ELEM_SYNOPTIC | HLV_ID | No | No | No |  |
| 1 | HLV_ID | SMRTDTA_ELEM_WAITING_LST | HLV_ID | No | No | No |  |

_(36 total; showing first 30)_
