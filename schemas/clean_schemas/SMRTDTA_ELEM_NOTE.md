# SMRTDTA_ELEM_NOTE

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=SMRTDTA_ELEM_NOTE

## Description

This table is a bridge between note context SmartData element values and the source note records.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | HLV |
| Release Version | Rel February 2022 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| HLV_ID | NUMERIC (18,0) | The unique identifier (.1 item) for the value record. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| NOTE_ID | VARCHAR (254) | The unique ID of the linked note record that is associated with the SmartData element value. |
| ELEMENT_ID | VARCHAR (50) | The SmartData identifier (SDI) for this row. |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| B-TREE INDEX | EIX_SMRTDTANOTE_NOTE_ID | NOTE_ID | 1 | Yes | Yes |  |

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
| 2 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |

_(61 total; showing first 30)_
