# OR_LOG_ALL_STAFF

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=OR_LOG_ALL_STAFF

## Description

The OR_LOG_ALL_STAFF table contains information about all staff members associated with a procedural case that has been performed. This includes physicians, procedural staff, anesthesia staff, pre-op nurses, and recovery nurses.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | ORL |
| Release Version | Rel 2014 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| LOG_ID | VARCHAR (18) | The unique ID associated with the procedural log record for this row. |
| LINE | INTEGER | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this Chronicles record. This is populated only if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this Chronicles record was extracted. This is populated only if you use IntraConnect. |
| STAFF_TYPE_MAP_C | INTEGER |  |
| STAFF_ID | VARCHAR (18) | The unique ID of the provider record that represents the staff member. |
| ROLE_C | INTEGER |  |
| SERVICE_C | VARCHAR (66) |  |
| PANEL | INTEGER | The panel number for the staff member. This will only have a value for physicians. |
| STAFF_TYPE_C | VARCHAR (66) |  |
| ANES_STAFF_TYPE_C | INTEGER |  |
| ACCOUNTBLE_STAFF_YN | VARCHAR (1) |  |
| TIME_DURATION_MINS | INTEGER | The length of time the staff member is documented as either in room or responsible in minutes for the log represented by this row. |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| B-TREE INDEX | EIX_ACCOUNTABLE_STAFF | LOG_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_ACCOUNTABLE_STAFF | STAFF_TYPE_MAP_C | 2 | Yes | Yes |  |
| B-TREE INDEX | EIX_ACCOUNTABLE_STAFF | ACCOUNTBLE_STAFF_YN | 3 | Yes | Yes |  |
| B-TREE INDEX | EIX_PRIMARY_PHYSICIAN | LOG_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_PRIMARY_PHYSICIAN | ROLE_C | 2 | Yes | Yes |  |
| B-TREE INDEX | EIX_PRIMARY_PHYSICIAN | PANEL | 3 | Yes | Yes |  |

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
| 5 | STAFF_TYPE_MAP_C | ZC_OR_STAFF_TYP_MAP | STAFF_TYPE_MAP_C | No | No | No |  |
| 6 | STAFF_ID | CLARITY_SER | PROV_ID | Unknown | No | No |  |
| 6 | STAFF_ID | CLARITY_SER_2 | PROV_ID | Unknown | No | No |  |
| 6 | STAFF_ID | CLARITY_SER_3 | PROV_ID | Unknown | No | No |  |
| 6 | STAFF_ID | CLARITY_SER_4 | PROV_ID | No | No | No |  |
| 6 | STAFF_ID | CLARITY_SER_MYC | PROV_ID | Unknown | No | No |  |
| 6 | STAFF_ID | D_PROV_PRIMARY_HIERARCHY | PROV_ID | Unknown | Unknown | No |  |

_(41 total; showing first 30)_
