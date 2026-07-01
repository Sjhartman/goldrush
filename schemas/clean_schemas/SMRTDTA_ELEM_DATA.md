# SMRTDTA_ELEM_DATA

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=SMRTDTA_ELEM_DATA

## Description

The SMRTDTA_ELEM_DATA table stores metadata (context, linked records, time of entry, etc.) concerning SmartData element values entered by users through SmartForms, SmartTools or other documentation tools that file discrete data to SmartData elements. The actual element values entered by end users are stored in the SMRTDTA_ELEM_VALUE table.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | HLV |
| Release Version | Summer 2009 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| HLV_ID | NUMERIC (18,0) | The unique ID of the SmartData element value. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| ELEMENT_ID | VARCHAR (192) | The SmartData identifier (SDI) for this row. |
| CUR_VALUE_DATETIME | DATETIME (Local) | The date and time when the SmartData element value was entered by a user through a SmartForm, SmartTool or other documentation tool that files discrete data to SmartData elements. |
| CUR_VALUE_USER_ID | VARCHAR (18) | The unique ID of the user who entered the SmartData element value for this row. This column is frequently used to link to the CLARITY_EMP table. |
| CUR_VALUE_SOURCE | VARCHAR (255) | Describes the source of value entered by a user through a SmartForm, SmartTool or other documentation tool that files discrete data to SmartData elements. This data can take several forms including, but not limited to the following: the programmatic ID of the ActiveX component used  to input data, the activity where the user entered the data (NoteWriter, Patient Instructions etc.), and the unique ID of the SmartForm. |
| CONTEXT_NAME | VARCHAR (192) | The name of the context associated with this row. Contexts organize SmartData element data into different categories and determine under what circumstances data is stored. Examples of contexts include "Patient" and "Episode". |
| CONTACT_SERIAL_NUM | NUMERIC (18,0) | The unique contact serial number for a contact this record is linked to. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| RECORD_ID_VARCHAR | VARCHAR (254) | The unique ID of the linked record that is associated with the SmartData element value of the current row. The type of linked record (patient, order, note, etc.) is determined by the context specified in the CONTEXT_NAME column of the current row. This column will be populated with a varchar version of the numeric ID if the type is numeric. |
| RECORD_ID_NUMERIC | NUMERIC (18,0) | The unique ID of the linked record that is associated with the SmartData element value of the current row. The type of linked record (patient, order, note, etc.) is determined by the context specified in the CONTEXT_NAME column of the current row. This column is only populated if the linked record ID is in numeric format. |
| CUR_SOURCE_LQF_ID | VARCHAR (18) | The unique ID of the SmartForm that is the source of the current value. If the source is not a SmartForm, this column will not be populated. In either case, the CUR_VALUE_SOURCE column is populated with the source. |
| UPDATE_DATE | No | *** Deprecated *** In SMRTDTA_ELEM_DATA, the column UPDATE_DATE has been deprecated. This column should no longer be used to track updates to SMRTDTA_ELEM_DATA. Flip "Track row updates?" to "Yes" in the Information Activity to enable capturing of row updates on SMRTDTA_ELEM_DATA using ESP_CR_ALTERED_ROWS. |
| PAT_LINK_ID | VARCHAR (18) | The unique ID of the patient record linked to the SmartData element. This column is frequently used to link to the PATIENT table. |
| REC_ARCHIVED_YN | No | Indicates whether the SmartData Element Value record is archived at the record level. |
| SRC_NOTE_ID | VARCHAR (254) | Links to the note record that created the current value. |
| SRC_NOTE_STATUS_C | VARCHAR (66) |  |
| CUR_VAL_UTC_DTTM | DATETIME (UTC) | UTC version of HLV 70 |
| CLIN_ATTACH_STAT_C | INTEGER |  |
| SRC_CLIN_ATTACH_ID | VARCHAR (18) | The SmartText ID of the clinical attachment |
| SRC_CLIN_ATTACH_DTE | NUMERIC (18,2) | The system date (DTE) of the SmartText source. |
| CUR_VALUE_ADDENDUM | INTEGER | If this SmartData element was edited during an addendum, this column will be populated with the number of that addendum. |
| SET_BY_C | INTEGER |  |
| AI_PAT_ENC_CSN_ID | NUMERIC (18,0) | Stores the patient contact that this HLV has an AI suggestion from. |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| BITMAP INDEX | EIX_CONTEXT_NAME | CONTEXT_NAME | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_SMRTDTA_ELEM_DATA_ID_NUM | RECORD_ID_NUMERIC | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_SMRTDTA_ELEM_DATA_ID_NUM | CONTEXT_NAME | 2 | Yes | Yes |  |
| B-TREE INDEX | EIX_SMRTDTA_ELEM_DATA_ID_VAR | RECORD_ID_VARCHAR | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_SMRTDTA_ELEM_DATA_ID_VAR | CONTEXT_NAME | 2 | Yes | Yes |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | HLV_ID | SMRTDTA_ELEM_AIEXTRACTED | HLV_ID | No | No | No |  |
| 1 | HLV_ID | SMRTDTA_ELEM_AUTH | HLV_ID | No | No | No |  |
| 1 | HLV_ID | SMRTDTA_ELEM_BEREAVE | HLV_ID | No | No | No |  |
| 1 | HLV_ID | SMRTDTA_ELEM_CONCEPT | HLV_ID | No | No | No |  |
| 1 | HLV_ID | SMRTDTA_ELEM_CONTENT_REV | HLV_ID | No | No | No |  |
| 1 | HLV_ID | SMRTDTA_ELEM_CUST_SERVICE | HLV_ID | No | No | No |  |
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
| 2 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |

_(234 total; showing first 30)_
