# CLARITY_ADT

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=CLARITY_ADT

## Description

The CLARITY_ADT table is the master table for ADT event history information. This table contains several foreign keys for other ADT tables.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | ADT |
| Release Version | EPIC 2000 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| EVENT_ID | NUMERIC (18,0) | The unique ID number of the ADT event record. |
| EVENT_TYPE_C | INTEGER |  |
| EVENT_SUBTYPE_C | INTEGER |  |
| DEPARTMENT_ID | NUMERIC (18,0) | The ID number of the unit of the event record at the effective time. |
| ROOM_ID | VARCHAR (18) | The ID number of the room of the event record at the effective time. |
| ROOM_CSN_ID | NUMERIC (18,0) | The serial number for the room contact of the event record. This number is unique across all room contacts in the system. |
| BED_ID | VARCHAR (18) | The ID number of the bed of the event record at the effective time. |
| BED_CSN_ID | NUMERIC (18,0) | The serial number for the bed contact of the event record. This number is unique across all bed contacts in the system. |
| BED_STATUS_C | INTEGER |  |
| EFFECTIVE_TIME | DATETIME (Local) | The instant when the event was supposed to have happened. |
| PAT_ID | VARCHAR (18) | The ID of the patient of the event record at the effective time. |
| PAT_ENC_DATE_REAL *(deprecated)* | FLOAT | *** Deprecated *** The deprecated column's content is no longer available since it is no longer populated in Chronicles. ****** This is a numeric representation of the date of this encounter in your system. The integer portion of the number specifies the date of the encounter. The digits after the decimal point indicate multiple visits on one day. |
| PAT_ENC_CSN_ID | NUMERIC (18,0) | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| EVENT_TIME | DATETIME (Local) | The instant when the event record was actually created. |
| USER_ID | VARCHAR (18) | The ID number of the user who created the event record. |
| PAT_CLASS_C | VARCHAR (66) |  |
| PAT_SERVICE_C | VARCHAR (66) |  |
| PAT_LVL_OF_CARE_C | VARCHAR (66) |  |
| DELETE_TIME | DATETIME (Local) | The instant when the event record was actually deleted. |
| CANC_EVENT_ID | NUMERIC (18,0) | The ID number of the canceled event record that this event record replaces. |
| XFER_EVENT_ID | NUMERIC (18,0) | The ID number of the 'transfer out' event type event record which with this 'transfer in' event type event record corresponds to a transfer action for the patient of the event records. |
| SWAP_EVENT_ID | NUMERIC (18,0) | The ID number of the 'transfer in' event type event record which with this 'transfer out' event type event record corresponds to a swap action for the patients of the event records. |
| COMMENTS | VARCHAR (255) | The free text comment associated with the event record. This is used to hold overridden confirmation warnings by the user for the event type event record action. |
| REASON_C | VARCHAR (66) |  |
| ACCOMMODATION_C | VARCHAR (66) |  |
| ACCOM_REASON_C | INTEGER |  |
| ADM_EVENT_ID | No |  |
| DIS_EVENT_ID | No |  |
| CM_PHY_OWNER_ID | VARCHAR (25) | ID of the physical deployment owner for this record.  Physical owners will be where the data is hosted, either on the cross-over server or the owner deployment. |
| CM_LOG_OWNER_ID | VARCHAR (25) | ID of the logical deployment owner for this record.  Logical owners show the deployment where the record was created but doesn't represent if the record is a part of version skew. |
| ALT_EVENT_TYPE_C | INTEGER |  |
| ORIG_EVENT_TIME | DATETIME (Local) | The instant when the original subtype record for this event was actually created. |
| PREV_UPD_EVNT_TIME | DATETIME (Local) | The instant when the last previous update subtype record for this event was actually created. |
| ORIG_EFF_TIME | DATETIME (Local) | The instant when the original subtype record for this event was supposed to have happened. |
| PREV_UPD_EFF_TIME | DATETIME (Local) | The instant when the last previous update subtype record for this event was supposed to have happened. |
| XFER_IN_EVENT_ID | NUMERIC (18,0) | The ID number of the 'transfer in' type record which with this 'transfer out' type record corresponds to a transfer action for the patient CSN of these records. |
| NEXT_OUT_EVENT_ID | NUMERIC (18,0) | The ID number of the next 'transfer out' or 'discharge' type record for this bed for the patient CSN of these records. |
| LAST_IN_EVENT_ID | NUMERIC (18,0) | The ID number of the last 'transfer in' or 'admission' type record for this bed for the patient CSN of these records. |
| STATUS_OF_BED_C | VARCHAR (66) |  |
| EVT_CANCEL_USER_ID | VARCHAR (18) | This Item records the user that cancels an ADT contact. |
| BASE_PAT_CLASS_C | INTEGER |  |
| PREV_EVENT_ID *(deprecated)* | NUMERIC (18,0) |  |
| SEQ_NUM_IN_ENC | NUMERIC (18,0) | This column contains the sequence number for this event within a patient encounter. You can use this number to determine the order of events for a particular encounter. Only non-canceled events are included within this sequence. |
| SEQ_NUM_IN_BED_MIN | NUMERIC (18,0) | This column contains a sequence number to identify the correct order of events when multiple events for the same bed are effective within the same minute. |
| CANCEL_REASON_C | VARCHAR (66) |  |
| OUT_EVENT_TYPE_C | INTEGER |  |
| IN_EVENT_TYPE_C | INTEGER |  |
| FROM_BASE_CLASS_C | INTEGER |  |
| TO_BASE_CLASS_C | INTEGER |  |
| LABOR_STATUS_C | INTEGER |  |
| FIRST_IP_IN_IP_YN | VARCHAR (1) |  |
| ORDER_ID | NUMERIC (18,0) | This item is a link to the ORD record directly responsible for generating an ADT event. |
| SOURCE_LOC_EVNT_ID | NUMERIC (18,0) | The unique ID of the Patient Location event that generated this Admission, Discharge, Transfer, or Leave of Absence (ADT) event. This signifies that this ADT event was created from a Patient Location update. |
| EVNT_REVIEW_C | INTEGER |  |
| REVIEW_DTTM | DATETIME (UTC) | The date and time when this event was reviewed by the user. |
| REVIEW_USER_ID | VARCHAR (18) | The unique ID of the user who reviewed this event. |
| LOA_REASON_C | INTEGER |  |
| ORIGINAL_EVENT_ID | No | The unique ID of the original event that this event record replaces. If this event record has not been canceled or updated, this column will be equal to the EVENT_ID column. This column is not necessarily equal to the CANC_EVENT_ID column. If the original event has been updated multiple times, then this column will show the ID of the original event, not the ID of the event that was most recently replaced by this record. |
| ACTION_SOURCE_C | INTEGER |  |
| ENC_SERIES_HSP_ACCOUNT_ID *(deprecated)* | NUMERIC (18,0) |  |
| ENC_SERIES_FINANCIAL_CLASS_C *(deprecated)* | VARCHAR (66) |  |
| ENC_SERIES_PRIMARY_PAYER_ID *(deprecated)* | NUMERIC (18,0) |  |
| ENC_SERIES_PRIMARY_PLAN_ID *(deprecated)* | NUMERIC (18,0) |  |
| ENC_SERIES_OUT_FIN_CL_EV_TYP_C *(deprecated)* | INTEGER |  |
| ENC_SERIES_IN_FIN_CL_EV_TYP_C *(deprecated)* | INTEGER |  |
| ENC_SERIES_FROM_FIN_CLASS_C *(deprecated)* | VARCHAR (66) |  |
| ENC_SERIES_TO_FIN_CLASS_C *(deprecated)* | VARCHAR (66) |  |
| ENC_SERIES_OUT_PAYER_EV_TYP_C *(deprecated)* | INTEGER |  |
| ENC_SERIES_IN_PAYER_EV_TYP_C *(deprecated)* | INTEGER |  |
| ENC_SERIES_FROM_PAYER_ID *(deprecated)* | NUMERIC (18,0) |  |
| ENC_SERIES_TO_PAYER_ID *(deprecated)* | NUMERIC (18,0) |  |
| ENC_SERIES_OUT_PLAN_EV_TYP_C *(deprecated)* | INTEGER |  |
| ENC_SERIES_IN_PLAN_EV_TYP_C *(deprecated)* | INTEGER |  |
| ENC_SERIES_FROM_PLAN_ID *(deprecated)* | NUMERIC (18,0) |  |
| ENC_SERIES_TO_PLAN_ID *(deprecated)* | NUMERIC (18,0) |  |
| SPLIT_ACCT_HSP_ACCOUNT_ID | NUMERIC (18,0) | The unique ID of the hospital account for the associated event. This column will only be set for admissions enabled for split accounts. |
| SPLIT_ACCT_FINANCIAL_CLASS_C | VARCHAR (66) |  |
| SPLIT_ACCT_PRIMARY_PAYER_ID | NUMERIC (18,0) | The unique ID of the responsible primary payer for the associated event. This column will only be set for admissions enabled for split accounts. |
| SPLIT_ACCT_PRIMARY_PLAN_ID | NUMERIC (18,0) | The unique ID of the responsible primary plan for the associated event. This column will only be set for admissions enabled for split accounts. |
| SPLIT_ACCT_OUT_FIN_CL_EV_TYP_C | INTEGER |  |
| SPLIT_ACCT_IN_FIN_CL_EV_TYP_C | INTEGER |  |
| SPLIT_ACCT_FROM_FIN_CLASS_C | VARCHAR (66) |  |
| SPLIT_ACCT_TO_FIN_CLASS_C | VARCHAR (66) |  |
| SPLIT_ACCT_OUT_PAYER_EV_TYP_C | INTEGER |  |
| SPLIT_ACCT_IN_PAYER_EV_TYP_C | INTEGER |  |
| SPLIT_ACCT_FROM_PAYER_ID | NUMERIC (18,0) | The unique ID of the payer prior this event. |
| SPLIT_ACCT_TO_PAYER_ID | NUMERIC (18,0) | The unique ID of the payer after this event. |
| SPLIT_ACCT_OUT_PLAN_EV_TYP_C | INTEGER |  |
| SPLIT_ACCT_IN_PLAN_EV_TYP_C | INTEGER |  |
| SPLIT_ACCT_FROM_PLAN_ID | NUMERIC (18,0) | The unique ID of the plan prior to this event. |
| SPLIT_ACCT_TO_PLAN_ID | NUMERIC (18,0) | The unique ID of the plan after this event. |
| IS_LOA_UPDATE_YN | VARCHAR (1) |  |
| EVENT_CONVERTED_FLAG_C | INTEGER |  |
| EFFECTIVE_UTC_DTTM | DATETIME (UTC) | The instant when the event was supposed to have happened in UTC. |
| OFF_SERVICE_YN | VARCHAR (1) |  |
| OFF_LEVEL_CARE_YN | VARCHAR (1) |  |
| CONVERTED_TO_EVENT_ID | NUMERIC (18,0) | When an event converts from an LOA Out to a Discharge or from a Discharge to an LOA Out, as indicated in I ADT 95 (Event Conversion Flag), a new ADT event is created which is not linked to the canceled event via I ADT 92 (Event Pointer). This item points to that new ADT event. |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| B-TREE INDEX | EIX_CLARITY_ADT_BECSID | BED_CSN_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_CLARITY_ADT_CSN_SUBTYPE | PAT_ENC_CSN_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_CLARITY_ADT_CSN_SUBTYPE | EVENT_SUBTYPE_C | 2 | Yes | Yes |  |
| B-TREE INDEX | EIX_CLARITY_ADT_DEID | DEPARTMENT_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_CLARITY_ADT_EFFTIME | EFFECTIVE_TIME | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_CLARITY_ADT_EVENT_TIME | EVENT_TIME | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_CLARITY_ADT_EVENT_TIME | USER_ID | 2 | Yes | Yes |  |
| B-TREE INDEX | EIX_CLARITY_ADT_EVENT_TYPE | EVENT_TYPE_C | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_CLARITY_ADT_EVENT_TYPE | EVENT_SUBTYPE_C | 2 | Yes | Yes |  |
| B-TREE INDEX | EIX_CLARITY_ADT_PAENCSID_CMP | PAT_ENC_CSN_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_CLARITY_ADT_PAENCSID_CMP | EFFECTIVE_TIME | 2 | Yes | Yes |  |
| B-TREE INDEX | EIX_CLARITY_ADT_ROCSID | ROOM_CSN_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_CLARITY_ADT_USID | USER_ID | 1 | Yes | Yes |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | EVENT_ID | ADT_DOC_IDENTIFIERS | EVENT_ID | No | No | No |  |
| 1 | EVENT_ID | ADT_PAS_EPSD_ENC | EVENT_ID | Yes | No | No |  |
| 1 | EVENT_ID | F_IP_HSP_TRANSFER | EVENT_ID | Unknown | Unknown | No |  |
| 1 | EVENT_ID | V_ADT_IP_DISCHARGES | EVENT_ID | Unknown | Unknown | No |  |
| 1 | EVENT_ID | V_ADT_LTC_CENSUS | EVENT_ID | Unknown | Unknown | No |  |
| 1 | EVENT_ID | V_ADT_OBSERVATIONS | EVENT_ID | Unknown | Unknown | No |  |
| 1 | EVENT_ID | V_ADT_OR_ADMITS | EVENT_ID | Unknown | Unknown | No |  |
| 1 | EVENT_ID | V_PAT_PAIN_ASSESSMENT | EVENT_ID | Unknown | Unknown | No |  |
| 2 | EVENT_TYPE_C | ZC_ALT_EVENT_TYPE | ALT_EVENT_TYPE_C | No | No | No |  |
| 2 | EVENT_TYPE_C | ZC_EVENT_TYPE | EVENT_TYPE_C | No | No | No |  |
| 3 | EVENT_SUBTYPE_C | ZC_EVENT_SUBTYPE | EVENT_SUBTYPE_C | No | No | No |  |
| 4 | DEPARTMENT_ID | BH_DEP | DEPARTMENT_ID | No | No | No |  |
| 4 | DEPARTMENT_ID | CLARITY_DEP | DEPARTMENT_ID | No | No | No |  |
| 4 | DEPARTMENT_ID | CLARITY_DEP_2 | DEPARTMENT_ID | No | No | No |  |
| 4 | DEPARTMENT_ID | CLARITY_DEP_3 | DEPARTMENT_ID | No | No | No |  |
| 4 | DEPARTMENT_ID | CLARITY_DEP_4 | DEPARTMENT_ID | No | No | No |  |
| 4 | DEPARTMENT_ID | CLARITY_DEP_5 | DEPARTMENT_ID | No | No | No |  |
| 4 | DEPARTMENT_ID | CLARITY_DEP_MYC | DEPARTMENT_ID | No | No | No |  |
| 4 | DEPARTMENT_ID | DEPT_QUEUE_MSG_SETTINGS | DEPARTMENT_ID | No | No | No |  |
| 4 | DEPARTMENT_ID | DEPT_VERIFIED_INFO | DEPARTMENT_ID | No | No | No |  |
| 4 | DEPARTMENT_ID | DEP_BATCH_LTR_GEN | DEPARTMENT_ID | No | No | No |  |
| 4 | DEPARTMENT_ID | DEP_CE_SETTINGS | DEPARTMENT_ID | No | No | No |  |
| 4 | DEPARTMENT_ID | DP_HIDE_SENSITIVE_CONFIG | DEPARTMENT_ID | No | No | No |  |
| 4 | DEPARTMENT_ID | ED_ALRT_DFLT | DEPARTMENT_ID | No | No | No |  |
| 4 | DEPARTMENT_ID | ED_DEP_SETTINGS | DEP_ID | No | No | No |  |
| 4 | DEPARTMENT_ID | EXT_CAL_DEPT_CONFIG | DEPARTMENT_ID | No | No | No |  |
| 4 | DEPARTMENT_ID | VISIT_MODE_CONFIG_DEP | DEPARTMENT_ID | No | No | No |  |
| 4 | DEPARTMENT_ID | V_CUBE_D_DEPARTMENT | DEPARTMENT_ID | Unknown | Unknown | No |  |
| 4 | DEPARTMENT_ID | V_CUBE_D_DEP_LOC | DEPARTMENT_ID | Unknown | Unknown | No |  |
| 5 | ROOM_ID | ED_ROOM_INFO | ROOM_ID | Unknown | No | No |  |

_(515 total; showing first 30)_
