# PAT_ENC_HSP_2

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=PAT_ENC_HSP_2

## Description

The PAT_ENC_HSP_2 table is the subsequent table for the PAT_ENC_HSP table, which is the primary table for hospital encounter information. Each record in this table is based on a patient contact serial number.

**Overflow table** for PAT_ENC_HSP (133 cols). Contains additional columns for the same records — join on the shared primary key column.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | EPT |
| Release Version | Summer 2009 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| PAT_ENC_CSN_ID | NUMERIC (18,0) | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| PAT_ID | VARCHAR (18) | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| PAT_ENC_DATE_REAL | FLOAT | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| CONTACT_DATE | DATETIME | The date of this contact in calendar format. |
| CM_CT_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this contact. This is only populated if you use IntraConnect. |
| EX_DIS_DT_ENTR_DTTM | DATETIME (Local) | The instant of entry of expected discharge date. |
| EX_DIS_TM_ENTR_DTTM | DATETIME (Local) | The instant of entry of expected discharge time. |
| CONTRACT_REG_FLAG | VARCHAR (150) | Indicates whether an HOV contact was registered using the Contract Registration workflow. If this workflow was not used, this column is null. |
| CONTRACT_CODE_C | INTEGER |  |
| ACCEPTS_BLOOD_C | INTEGER |  |
| ED_ARRIVAL_DETAILS | VARCHAR (254) | Free text information holding any details regarding the ED Arrival. |
| CONS_SEDATION_C | VARCHAR (66) |  |
| RESTRAINT_SECLUS_C | VARCHAR (66) |  |
| HSPTL_ATTND_PROV_ID | VARCHAR (18) | The unique ID of the hospital attending provider. This column is frequently used to link to the CLARITY_SER table. |
| HOSP_ADMSN_STATUS_C | VARCHAR (66) |  |
| MULTI_PREG_YN | VARCHAR (1) |  |
| DISASTER_NUM | VARCHAR (50) | This column stores the disaster number, which is a number given by the ambulance company to patients during catastrophes that cause massive patient influxes to the hospital. |
| EXP_DIS_USER_ID | VARCHAR (18) | The unique ID associated with the last user who changed the expected discharge date and/or time for this row. This column is frequently used to link to the CLARITY_EMP table. |
| LEGACY_ADT_ENC_YN | VARCHAR (1) |  |
| SRC_PATTERN_CSN_ID | NUMERIC (18,0) | The Contact Serial Number (CSN) of the Admission Pattern record associated with the projected bed usage for this patient encounter. If this projection is manually modified an end user, the column stores null. |
| MU_ADV_DIR_FLO_YN *(deprecated)* | VARCHAR (1) |  |
| POLICE_BADGE_NUM | VARCHAR (30) | The badge number of the escorting police officer if the patient was escorted by a police officer to the hospital. |
| POLICE_REPORT_NUM | VARCHAR (30) | The police report number associated with an incident recorded by the escorting police officer if the patient was escorted by a police officer to the hospital. |
| POLICE_PRECINCT_NUM | VARCHAR (30) | The precinct number of the escorting police officer if the patient was escorted by a police officer to the hospital. |
| RELIG_AFFIL_VIS_C | INTEGER |  |
| ADM_SRC_POS_ID | NUMERIC (18,0) | The unique ID of the organization at which the patient was located before arriving at the hospital. |
| DIS_DEST_POS_ID | NUMERIC (18,0) | The unique ID of the organization to which the patient will go after hospital discharge. |
| SURVEY_OPT_OUT_YN | VARCHAR (1) |  |
| ENC_CLOSED_OR_COMPLETED_DATE | DATETIME | The date that the encounter was closed or completed. |
| BEDSIDE_ACTIVATION_DTTM | DATETIME (UTC) | The instant (in UTC) a patient or proxy first used a Bedside tablet to access this admission. |
| KI_ED_ARR_DTTM | 10821 | The date and time the patient arrived to the emergency department and used the Welcome kiosk. |
| ED_DISPO_PAT_COND_C | INTEGER |  |
| ADOPTION_TYPE_C | INTEGER |  |
| PRI_PROBLEM_ID | NUMERIC (18,0) | The unique ID of the principal problem for a patient's hospitalization. |
| EXPECTED_DISCHRG_APPROX_TIME_C | INTEGER |  |
| HSP_ADM_EVENT_ID | NUMERIC (18,0) | The unique ID of the hospital admission ADT event. |
| HSP_DIS_EVENT_ID | NUMERIC (18,0) | The unique ID of the hospital discharge ADT event. |
| DISCH_MILEST_KICKOFF_UTC_DTTM | DATETIME (UTC) | Displays the date and time that discharge milestones were initiated. |
| DISCH_MILEST_KICKOFF_USER_ID | VARCHAR (18) | User id that initiated discharge milestones. |
| DISCH_MILEST_AUTO_MANAGED_YN | VARCHAR (1) |  |
| PREDICTED_LOS | NUMERIC (18,2) | The Length of Stay value determined by the Predictive Model run. |
| EXP_LOS_UPD_SRC_C | INTEGER |  |
| BEDSIDE_ACTIVATION_LOC_DTTM | DATETIME (Local) | The instant a patient or proxy first used a MyChart Bedside tablet to access this admission, in local time. |
| ED_ENC_SRC_C | INTEGER |  |
| ED_DEPART_UTC_DTTM | DATETIME (UTC) | The ED Departure date and time in UTC. |
| ADT_ARRIVAL_UTC_DTTM | DATETIME (UTC) | The arrival date and time in UTC. |
| HOSP_DISCH_UTC_DTTM | DATETIME (UTC) | The hospital discharge date and time in UTC. |
| HOSP_ADMSN_UTC_DTTM | DATETIME (UTC) | The hospital admission date and time in UTC. |
| INP_ADMSN_UTC_DTTM | DATETIME (UTC) | The date and time that the patient first reached a patient class of Inpatient in UTC. |
| ED_HISTORICAL_YN | VARCHAR (1) |  |
| MED_REM_ON_ADMSN_YN *(deprecated)* | VARCHAR (1) |  |
| BEDSIDE_TV_ACTIVATION_UTC_DTTM | DATETIME (UTC) | This item records the instant, in UTC, a Bedside TV device was first activated for the admission. |
| BEDSIDE_TV_ACTIVATION_LOC_DTTM | DATETIME (Local) | This item records the instant, in the patient local time zone, at which a Bedside TV device was first activated for the admission. |
| PATIENT_TASK_COMPLETION_RATE | INTEGER | Aggregated task progression rates across all active tasks currently assigned to the patient. |
| START_MED_REM_DISCHG_YN | VARCHAR (1) |  |
| EXPECTED_DISCHARGE_UNKNOWN_YN | VARCHAR (1) |  |
| DUAL_ADMISSION_CSN | NUMERIC (18,0) | In a dual admission scenario this will point from the encounter on leave to the admitted encounter. |
| LOA_PAT_ENC_CSN_ID | NUMERIC (18,0) | This column is only populated when the encounter for this row is admitted and the patient currently has an encounter on a leave of absence. This column displays the unique contact serial number of the patient encounter that is on a leave of absence. |
| INITIAL_ADT_PAT_STAT_C | INTEGER |  |
| NOTIFICATION_SENT_FIRST_IP_YN | VARCHAR (1) |  |
| NOTIFICATION_SENT_OBS_ADMSN_YN | VARCHAR (1) |  |
| IB_ALERT_LENGTH_OF_STAY_MSG_ID | VARCHAR (18) | The unique ID of the In Basket Message that was sent to alert that a patient has gone past the approved length of stay. |
| INITIAL_ADMIT_CONF_STAT_C | INTEGER |  |
| TRANSFER_COMMENTS | VARCHAR (254) | The transfer comments entered by the user during the most recent transfer. |
| MED_READINESS_DTTM | 11420 | The medical readiness date and time for this patient encounter. This date and time may be expected or confirmed, depending on whether the patient is medically ready or not. |
| MED_READINESS_TIMEFRAM_C | INTEGER |  |
| MED_READINESS_YN | VARCHAR (1) |  |
| MED_READINESS_INST_ENTRY_DTTM | DATETIME (UTC) | The instant at which this patient's medical readiness information was last updated |
| MED_READINESS_USER_ID | VARCHAR (18) | The unique ID of the user who last updated medical readiness information for this patient encounter |
| MED_READINESS_SOURCE_C | INTEGER |  |
| EXPECTED_DISCH_DISP_C | INTEGER |  |
| EXP_DISCH_DISP_USER_ID | VARCHAR (18) | This item logs the last user that changed the expected discharge disposition. |
| EXP_DISCH_DISP_ENTRY_UTC_DTTM | DATETIME (UTC) | The instant of entry of expected discharge disposition. |
| PRIMARY_LINKED_PAT_ENC_CSN_ID | NUMERIC (18,0) | The unique contact serial number of the primary linked hospital encounter.  Encounters are considered linked if the start of encounter B occurs after the start of encounter A, but within 6 hours after the discharge of encounter A (including before the discharge of encounter A). Any encounters that would be linked to encounter B by that definition are instead linked to encounter A. This means that there is exactly one primary encounter for every series of linked encounters and that the primary linked encounter is the one within a series that has the earliest start time. |
| BEDSIDE_WB_ACTIVATE_UTC_DTTM | DATETIME (UTC) | This item records the UTC instant at which an admission activated a Bedside Whiteboard. |
| BEDSIDE_WB_ACTIVATE_LOCAL_DTTM | DATETIME (Local) | Records the instant a patient had a Bedside Whiteboard activated in local time. |
| TODO_ADM_DISCLAIMER_ACTIVE_YN | VARCHAR (1) | Surrogate key used to uniquely identify rows in this (and only this) table on Cogito Cloud only, do not assume the surrogate key in this table will correspond to the surrogate key in another table |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| B-TREE INDEX | EIX_PAT_ENC_HSP_2_CONTACT | PAT_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_PAT_ENC_HSP_2_CONTACT | PAT_ENC_DATE_REAL | 2 | Yes | Yes |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | PAT_ENC_CSN_ID | ALT_ORD_PROV_SINGL | PAT_ENC_CSN_ID | Unknown | No | No |  |
| 1 | PAT_ENC_CSN_ID | AN_RELINK_INFO | PAT_ENC_CSN_ID | No | No | No |  |
| 1 | PAT_ENC_CSN_ID | DENT_ORTH_EXAM_NOTES | PAT_ENC_CSN_ID | No | No | No |  |
| 1 | PAT_ENC_CSN_ID | FAC_CHG_OVERRIDE | PAT_ENC_CSN_ID | No | No | No |  |
| 1 | PAT_ENC_CSN_ID | FAM_HX_PAT_ONLY | PAT_ENC_CSN_ID | No | No | No |  |
| 1 | PAT_ENC_CSN_ID | F_ED_ENCOUNTERS | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 1 | PAT_ENC_CSN_ID | F_HH_CERT_ATTRIBUTES | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 1 | PAT_ENC_CSN_ID | F_HH_OASIS_SINGLE | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 1 | PAT_ENC_CSN_ID | F_HH_OASIS_SINGLE_2 | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 1 | PAT_ENC_CSN_ID | F_HH_OASIS_SINGLE_3 | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 1 | PAT_ENC_CSN_ID | F_HH_OASIS_SINGLE_4 | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 1 | PAT_ENC_CSN_ID | F_HH_OASIS_SINGLE_5 | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 1 | PAT_ENC_CSN_ID | F_IBD_ADULT_FORM_ENC | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 1 | PAT_ENC_CSN_ID | F_IBD_FORM_RESP | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 1 | PAT_ENC_CSN_ID | F_IP_HSP_ADMISSION | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 1 | PAT_ENC_CSN_ID | F_IP_HSP_SEPSIS3 | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 1 | PAT_ENC_CSN_ID | F_IRIS_ENC | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 1 | PAT_ENC_CSN_ID | F_MU_OBJ_EH_ADMISSION | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 1 | PAT_ENC_CSN_ID | F_MU_QM_EH_2014_ED_VISIT | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 1 | PAT_ENC_CSN_ID | F_MU_QM_EH_2014_IP_ADMSN | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 1 | PAT_ENC_CSN_ID | F_QM_AMI | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 1 | PAT_ENC_CSN_ID | F_QM_CAC | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 1 | PAT_ENC_CSN_ID | F_QM_HBIPS | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 1 | PAT_ENC_CSN_ID | F_QM_HEART_FAILURE | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 1 | PAT_ENC_CSN_ID | F_QM_IMMUNIZATION | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 1 | PAT_ENC_CSN_ID | F_QM_PC_BABY | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 1 | PAT_ENC_CSN_ID | F_QM_PC_MOM | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 1 | PAT_ENC_CSN_ID | F_QM_PNEUMONIA | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 1 | PAT_ENC_CSN_ID | F_SCHED_APPT | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 1 | PAT_ENC_CSN_ID | HAUD_ENC | ENC_CSN | Unknown | Unknown | No |  |

_(694 total; showing first 30)_
