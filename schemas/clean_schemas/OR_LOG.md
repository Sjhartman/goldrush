# OR_LOG

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=OR_LOG

## Description

The OR_LOG table contains information about surgical and procedural log (ORL) records.

**Primary table** in this group (124 cols). Overflow siblings joined on shared key: OR_LOG_2 (109 cols), OR_LOG_3 (13 cols). Prefer this table for most queries.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | ORL |
| Release Version | MU1 - MAY 2001 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| LOG_ID | VARCHAR (18) | The unique ID of the procedural log record for this row. |
| LOG_NAME | VARCHAR (80) | The name of the surgical log record. |
| SURGERY_DATE | DATETIME | The date on which the case was performed. |
| CASE_TYPE_C | INTEGER |  |
| CASE_CLASS_C | INTEGER |  |
| TRAUMA_CASE_YN | VARCHAR (1) |  |
| PAT_ID | VARCHAR (18) | The unique ID of the patient associated with the procedural log record. |
| PAT_AGE *(deprecated)* | INTEGER | The age of the patient associated with the surgical log. |
| PAT_TYPE_C | VARCHAR (66) |  |
| POSTOP_CONSCIOUS_C *(deprecated)* | INTEGER |  |
| PREOP_CONSCIOUS_C *(deprecated)* | INTEGER |  |
| PREOP_BED_ID *(deprecated)* | VARCHAR (18) |  |
| PACU_BED_ID *(deprecated)* | VARCHAR (18) |  |
| NUM_OF_PANELS | INTEGER | The number of panels in the surgical log. |
| REQUEST_PERSON | VARCHAR (255) | The name of the person requesting the surgery |
| TOTAL_TIME_NEEDED | INTEGER | The total time needed for the log in minutes |
| REFER_PROV_ID | VARCHAR (18) | The unique ID of the physician who referred the patient associated with the log. |
| PAT_PREOP_COND_C *(deprecated)* | INTEGER |  |
| PAT_POSTOP_COND_C *(deprecated)* | INTEGER |  |
| ASA_RATING_C *(deprecated)* | VARCHAR (66) |  |
| DISCHARGE_TO_C | INTEGER |  |
| DISPOSITION_TIME | DATETIME (Local) | The time at which the patient was discharged. NOTE: Only the time value of this field is to be used. The date should always be 1/1/1900 for historical reasons. |
| DISCHARGED_BY_ID | VARCHAR (18) | The unique ID of the person who discharged the patient. |
| EXPIRED_YN | VARCHAR (1) |  |
| EXPIRED_WHERE_C | INTEGER |  |
| EXPIRED_TIME | DATETIME (Local) | If needed, records the time at which the patient expired |
| REPORTED_TO_ID | VARCHAR (18) | The unique ID of the person to whom the report for the surgery was given. |
| REPORTED_BY_ID | VARCHAR (18) | The unique ID of the person who gave the report to the person whom the report for the surgery of the log was given. |
| X_RAYS_TAKEN_YN | VARCHAR (1) |  |
| PREOP_XRAYS_YN | VARCHAR (1) |  |
| PREOP_VISIT_YN | VARCHAR (1) |  |
| LATEX_ALLERGIC_YN | VARCHAR (1) |  |
| EST_BLOOD_LOSS | NUMERIC (12,2) | The estimated amount of blood lost during the surgery. |
| ROOM_ID | VARCHAR (18) | The unique ID of the room in which the procedure in the procedural log was performed. This column is frequently used to link to CLARITY_SER. |
| LOC_ID | NUMERIC (18,0) | The unique ID of the location where the procedure was performed. This column is frequently used to link to CLARITY_LOC. |
| PRIORITY_C | INTEGER |  |
| ADD_ON_CASE_YN *(deprecated)* | VARCHAR (1) |  |
| STATUS_C | INTEGER |  |
| SERVICE_C | VARCHAR (66) |  |
| SCHED_START_TIME | DATETIME (Local) | The date and time at which the surgery in the surgical log was performed. |
| VOID_REASON_C | INTEGER |  |
| TOUCHED_BY_EOD_YN | VARCHAR (1) |  |
| CHECKIN_INSTANT | DATETIME (Local) | The date and time at which the log was checked-in. |
| PATIENT_ESCORT | VARCHAR (254) | The person escorting the patient for the surgery. This is a free text value. |
| CASE_REQUEST_ID | VARCHAR (18) | The unique ID of the surgical case attached to this log. |
| RECORD_CREATE_DATE | DATETIME | The creation date of this surgical log. |
| REC_CREATE_USER_ID | VARCHAR (18) | The unique ID of the user who created this surgical log. |
| SPECIAL_NEEDS *(deprecated)* | VARCHAR (254) | The special needs for the patient associated with the surgical log.  This column has been deprecated. The column had no KBSQL code prior to deprecation, and so was extracting null values. Further, this column would have only been able to extract line 1 of this item. Please use column SPECIAL_NEEDS in table OR_LOG_SPECNEED instead. |
| PRE_OP_DIAG *(deprecated)* | VARCHAR (254) | The free text description of the pre-op diagnosis for this surgical log.  This data is now extracted in table OR_LOG_PREOPDX . |
| POST_OP_DX *(deprecated)* | VARCHAR (254) | The free text description of the post-op diagnosis for this surgical log.  This data is now extracted in table OR_LOG_POSTOPDX. |
| ADT_CSN *(deprecated)* | INTEGER | Contact serial number for an ADT admit contact. |
| BLD_LOS_UNIT *(deprecated)* | VARCHAR (30) |  |
| RESEARCH_IND_C | INTEGER |  |
| PACU1_LOC_C | INTEGER |  |
| REASON_OVER_C | INTEGER |  |
| IOP_XRAYS_YN *(deprecated)* | VARCHAR (1) |  |
| POSTOP_DEST_C *(deprecated)* | VARCHAR (66) |  |
| IS_CONFIDENTIAL_YN | VARCHAR (1) |  |
| PANEL1_EXCL_HX_YN | VARCHAR (1) |  |
| PANEL2_EXCL_HX_YN | VARCHAR (1) |  |
| PANEL3_EXCL_HX_YN | VARCHAR (1) |  |
| PANEL4_EXCL_HX_YN | VARCHAR (1) |  |
| PANEL5_EXCL_HX_YN | VARCHAR (1) |  |
| ADDENDA_COUNT | No | The number of addenda on posted logs. This will return the number of addenda on the log if the log status is posted, otherwise, returns null. |
| REQ_BY_PHONE | VARCHAR (50) | The phone number of the person who requested that the case be created. |
| PATIENT_ID_VERB_YN | VARCHAR (1) |  |
| PAT_HAS_ID_BAND_YN | VARCHAR (1) |  |
| PAT_BLOOD_BAND_YN | VARCHAR (1) |  |
| BLOOD_BAND_NUMBER | VARCHAR (10) | The number of the patient's blood band. |
| CONSENT_CONF_BY_ID | VARCHAR (18) | The unique ID of the surgeon or staff member who confirmed consent. |
| OR_REP_TO_PACU_ID | VARCHAR (18) | The unique ID of the PACU staff member to whom the OR report was given. |
| REP_GIVEN_TO_OTHER *(deprecated)* | VARCHAR (40) |  |
| DESTINATION *(deprecated)* | VARCHAR (40) |  |
| PROPH_AB_REQ_YN *(deprecated)* | VARCHAR (1) |  |
| WEIGHT *(deprecated)* | NUMERIC (12,2) | The weight of the patient in pounds. |
| ADMIT_SOURCE_C *(deprecated)* | VARCHAR (66) |  |
| ADMITTING_SRVC_C *(deprecated)* | VARCHAR (66) |  |
| ADMITTING_PHYS_ID *(deprecated)* | VARCHAR (18) | The unique ID of the admitting physician. |
| ADMIT_BED_TYPE_C *(deprecated)* | VARCHAR (66) |  |
| INTRAOP_DISCH_TO_C | INTEGER |  |
| INPATIENT_DATA_ID | VARCHAR (18) | The unique ID of the inpatient data store record. |
| TOTAL_COST *(deprecated)* | NUMERIC (12,2) | The cost associated with the entire surgical case. |
| SURGEON_COST | NUMERIC (12,2) | The cost associated with the surgeons.   The item from which this column extracts is no longer populated in released workflows, but may include historical data. |
| ANES_STAFF_COST | NUMERIC (12,2) | The cost associated with the anesthesia staff.  The item from which this column extracts is no longer populated in released workflows, but may include historical data. |
| OR_COST | NUMERIC (12,2) | The cost associated with the operating room.  The item from which this column extracts is no longer populated in released workflows, but may include historical data. |
| SURG_STAFF_COST | NUMERIC (12,2) | The cost associated with the surgical staff.  The item from which this column extracts is no longer populated in released workflows, but may include historical data. |
| SURG_EQUIP_COST | NUMERIC (12,2) | The cost associated with the surgical equipment.  The item from which this column extracts is no longer populated in released workflows, but may include historical data. |
| ANES_EQUIP_COST | NUMERIC (12,2) | The cost associated with the anesthesia equipment.  The item from which this column extracts is no longer populated in released workflows, but may include historical data. |
| INSTR_COST | NUMERIC (12,2) | The cost associated with the surgical instruments.  The item from which this column extracts is no longer populated in released workflows, but may include historical data. |
| PROC_COST | NUMERIC (12,2) | The cost associated with the procedures.  The item from which this column extracts is no longer populated in released workflows, but may include historical data. |
| LOCATION_COST *(deprecated)* | NUMERIC (12,2) | The cost associated with the location. |
| STAND_ALONE_YN | VARCHAR (1) |  |
| VOID_COMMENTS | VARCHAR (254) | The free text comments entered when the log was voided. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this Chronicles record. This is populated only if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this Chronicles record was extracted. This is populated only if you use IntraConnect. |
| LOG_ACCEPTED_YN | VARCHAR (1) |  |
| PROC_LEVEL_C *(deprecated)* | INTEGER |  |
| PROJ_END_INSTANT *(deprecated)* | DATETIME (Local) |  |
| LOG_START_INSTANT *(deprecated)* | DATETIME (Local) |  |
| USER_PROJ_END_TIME | DATETIME (Local) | The projected end time entered by the user to override the projected end time computed by the system. |
| OR_TIME_EVTS_ENT_C | INTEGER |  |
| PROC_NOT_PERF_C | INTEGER |  |
| PROC_NOT_PERF_COM | VARCHAR (254) | Stores the comments, if the procedure not performed. |
| LOG_TYPE_C | INTEGER |  |
| PHASE_TWO_BED_ID *(deprecated)* | VARCHAR (18) |  |
| PAT_SOUND_LIKE *(deprecated)* | VARCHAR (192) | *** Deprecated *** In table OR_LOG, the column PAT_SOUND_LIKE (ORL/478) has been deprecated. The deprecated column's content is no longer available since it is no longer populated in Chronicles.  This item stores the sounds like string for the patient. |
| CASE_ID | VARCHAR (18) | This column stores the case ID (ORC) for this log. |
| IS_CLINICAL_TRL_YN *(deprecated)* | VARCHAR (1) |  |
| BLOOD_LOSS_UNIT_C | INTEGER |  |
| SCHED_INSTR_EDIT_YN | VARCHAR (1) |  |
| PAT_INSTR_EDITED_YN | VARCHAR (1) |  |
| NURSE_NOTES_EDIT_YN | VARCHAR (1) |  |
| POSITION_NOTES_E_YN | VARCHAR (1) |  |
| EMERG_STATUS_YN | VARCHAR (1) |  |
| IS_JOINT_RVSN_YN *(deprecated)* | VARCHAR (1) |  |
| RECORD_STATUS_C | INTEGER |  |
| FORM_ID_COUNTER | INTEGER | Annotated images form ID counter. |
| CHRGS_AT_ADDEND_YN | VARCHAR (1) |  |
| USING_EAP_YN | VARCHAR (1) |  |
| PRIMARY_PHYS_ID | VARCHAR (18) | The unique ID of the physician who is the primary physician for this log. |
| COST_BENCHMARK_USED_SUPPLY | NUMERIC (18,2) | The used supply cost benchmark for the procedure performed on the log. |
| COST_BENCHMARK_USED_IMPLANT | NUMERIC (18,2) | The used implant cost benchmark for the procedure performed on the log. |
| PRIMARY_PERFORMING_PROV_ID | VARCHAR (18) | Stores the primary performing surgeon/provider for panel 1; used by reports for faster searching. This is only relevant if the system is configured to allow other surgeon/provider roles to be considered the primary performing provider in I EAF 54347. |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| B-TREE INDEX | EIX_OR_LOG_ADONCAYN | ADD_ON_CASE_YN | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_OR_LOG_CACLC | CASE_CLASS_C | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_OR_LOG_CASE_ID | CASE_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_OR_LOG_CATYC | CASE_TYPE_C | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_OR_LOG_DIBYID | DISCHARGED_BY_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_OR_LOG_EXYN | EXPIRED_YN | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_OR_LOG_LOID | LOC_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_OR_LOG_PAAG | PAT_AGE | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_OR_LOG_PAID | PAT_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_OR_LOG_PATYC | PAT_TYPE_C | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_OR_LOG_PRC | PRIORITY_C | 1 | Yes | Yes |  |
| BITMAP INDEX | EIX_OR_LOG_PROC_NOT_PERF | PROC_NOT_PERF_C | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_OR_LOG_RECRUSID | REC_CREATE_USER_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_OR_LOG_REPRID | REFER_PROV_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_OR_LOG_ROID | ROOM_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_OR_LOG_SCHED_START_TIME | SCHED_START_TIME | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_OR_LOG_SEC | SERVICE_C | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_OR_LOG_STC | STATUS_C | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_OR_LOG_SUDA | SURGERY_DATE | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_OR_LOG_TRCAYN | TRAUMA_CASE_YN | 1 | Yes | Yes |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | LOG_ID | F_LOG_BASED | LOG_ID | Unknown | Unknown | No |  |
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
| 4 | CASE_TYPE_C | ZC_OR_CASE_TYPE | CASE_TYPE_C | No | No | No |  |
| 5 | CASE_CLASS_C | ZC_OR_CASE_CLASS | CASE_CLASS_C | No | No | No |  |
| 7 | PAT_ID | ANTICOAG_SELF_REGULATING | PAT_ID | No | No | No |  |
| 7 | PAT_ID | CARE_COORDINATION | PAT_ID | Unknown | No | No |  |
| 7 | PAT_ID | CLAIMS_DERIVE_PAT_FLAGS | PAT_ID | No | No | No |  |
| 7 | PAT_ID | COMMUNITY_RESRC_REVIEWED | PAT_ID | No | No | No |  |
| 7 | PAT_ID | D_PAT_GEOGRAPHIC_CLASS | PAT_ID | Unknown | Unknown | No |  |
| 7 | PAT_ID | EPT_MEM_INFO | PAT_ID | No | No | No |  |
| 7 | PAT_ID | EXT_DATA_LAST_DONE | PAT_ID | No | No | No |  |
| 7 | PAT_ID | F_IBD_ADULT_FORM_PAT | PAT_ID | Unknown | Unknown | No |  |
| 7 | PAT_ID | HH_PAT_INFO | PAT_ID | Unknown | No | No |  |
| 7 | PAT_ID | HM_STATUS_UPD | PAT_ID | No | No | No |  |
| 7 | PAT_ID | IMMNZTN_LAST_REVIEW | PAT_ID | No | No | No |  |
| 7 | PAT_ID | PATIENT | PAT_ID | No | No | No |  |

_(269 total; showing first 30)_
