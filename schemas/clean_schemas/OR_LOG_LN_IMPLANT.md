# OR_LOG_LN_IMPLANT

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=OR_LOG_LN_IMPLANT

## Description

This table contains the line IDs (ORM) for the implant information of the surgical/invasive procedure log (ORL).

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | ORL |
| Release Version | SPRING 2006 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| LOG_ID | VARCHAR (18) | The unique ID of the procedural log record. |
| LINE | No | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this Chronicles record. This is populated only if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this Chronicles record was extracted. This is populated only if you use IntraConnect. |
| IMPLANTS_ID | VARCHAR (18) | List of line record IDs, each of which stores the information for a single procedure and its related diagnoses. |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| B-TREE INDEX | EIX_OR_LOG_LN_IMPLANT_IMPLANTS | IMPLANTS_ID | 1 | Yes | Yes |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | LOG_ID | F_LOG_BASED | LOG_ID | Unknown | Unknown | No |  |
| 1 | LOG_ID | OR_LOG | LOG_ID | Unknown | No | No |  |
| 1 | LOG_ID | OR_LOG_2 | LOG_ID | Unknown | No | No |  |
| 1 | LOG_ID | OR_LOG_3 | LOG_ID | No | No | No |  |
| 1 | LOG_ID | OR_LOG_METRIC_DETAILS | LOG_ID | No | No | No |  |
| 1 | LOG_ID | OR_LOG_PRECEDING | LOG_ID | No | No | No |  |
| 1 | LOG_ID | OR_LOG_VIRTUAL | LOG_ID | No | No | No |  |
| 1 | LOG_ID | UK_CRM_PACEMKR_PROC | LOG_ID | No | No | No |  |
| 1 | LOG_ID | V_CASE_CHARGES | LOG_ID | Unknown | Unknown | No |  |
| 1 | LOG_ID | V_CASE_COSTS | LOG_ID | Unknown | Unknown | No |  |
| 1 | LOG_ID | V_CASE_ON_TIME_START | LOG_ID | Unknown | Unknown | No |  |
| 1 | LOG_ID | V_CASE_PHYS_TURNOVER | LOG_ID | Unknown | Unknown | No |  |
| 1 | LOG_ID | V_CASE_ROOM_TURNOVER | LOG_ID | Unknown | Unknown | No |  |
| 1 | LOG_ID | V_CASE_VOLUME | LOG_ID | Unknown | Unknown | No |  |
| 1 | LOG_ID | V_DECISION_TO_INCISION | LOG_ID | Unknown | Unknown | No |  |
| 1 | LOG_ID | V_LOG_BASED | LOG_ID | Unknown | Unknown | No |  |
| 1 | LOG_ID | V_LOG_TIMING_EVENTS | LOG_ID | Unknown | Unknown | No |  |
| 3 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 4 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 4 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 4 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 5 | IMPLANTS_ID | OR_LNLG_ADV_EVENT | RECORD_ID | Unknown | No | No |  |
| 5 | IMPLANTS_ID | OR_LNLG_ANEST_INFO | RECORD_ID | Unknown | No | No |  |
| 5 | IMPLANTS_ID | OR_LNLG_ANES_COMPL | RECORD_ID | Unknown | No | No |  |
| 5 | IMPLANTS_ID | OR_LNLG_ANES_EQUIP | RECORD_ID | Unknown | No | No |  |
| 5 | IMPLANTS_ID | OR_LNLG_ANES_RESP | RECORD_ID | No | No | No |  |
| 5 | IMPLANTS_ID | OR_LNLG_ANES_STAFF | RECORD_ID | Unknown | No | No |  |
| 5 | IMPLANTS_ID | OR_LNLG_ARR_THERAP | RECORD_ID | Unknown | No | No |  |

_(63 total; showing first 30)_
