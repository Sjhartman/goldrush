# F_PAT_CODES

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=F_PAT_CODES

## Description

This table will be deprecated in the Epic November 2025 release. This table is not the current recommendation for reporting on patient codes. F_PAT_CODES is a derived table containing information about each distinct patient code.  This is driven by information obtained from Doc Flowsheets, the MAR, and the Code Narrator.  Each time a provider documents a code start it signals the beginning of a code.  Other events, such as compressions, cardioversions, administered meds, etc. are also recorded.  The contact serial number is provided so you can link back to the patient's hospital records.

## Metadata

| Property | Value |
| --- | --- |
| Type | Derived Table |
| Load Frequency | INCREMENTAL |
| Release Version | Rel 2010 |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| EVENT_ID | VARCHAR (18) | The unique ID of the event record. |
| LINE | No | The line number to distinguish between codes with the same ID.  This matches up directly with the line number for the event signifying the start of the code. |
| PAT_ENC_CSN_ID | NUMERIC (18,0) | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| CODE_STATUS_C | VARCHAR (66) |  |
| CODE_START_DTTM | DATETIME (Local) | The instant when the patient started coding. |
| CODE_END_DTTM | DATETIME (Local) | The instant when the patient stopped coding, either due to expiration or resuscitation. |
| CODE_TYPE | VARCHAR (100) | The type of code, whether cardiac or respiratory. |
| FST_CARDIAC_RHYTHM | VARCHAR (2500) | The first cardiac rhythm that presented during the code. |
| FST_CARDIOVERT_DTTM | DATETIME (Local) | The instant when the first attempt to cardiovert the patient during the code occurred. |
| WITNESSED_YN | No | Whether the onset of the code was witnessed. |
| MONITORED_YN | No | Whether the patient was monitored at the onset of the code, either with an ECG, apnea, or pulse ox monitor. |
| MONITOR_ECG_YN | No | Whether the patient was monitored at the onset of the code with an ECG. |
| MONITOR_APNEA_YN | No | Whether the patient was monitored at the onset of the code with an apnea monitor. |
| MONITOR_PULSE_OX_YN | No | Whether the patient was monitored at the onset of the code with a pulse ox monitor. |
| PAT_SURVIVED_CODE | VARCHAR (2500) | Whether the patient survived the code. |
| CODE_TERMN_RSN | VARCHAR (255) | The reason why the care team stopped trying to resuscitate the patient, whether due to expiration or successful resuscitation.  If the code termination reason is documented as "Other", then this column will display the comment that was entered.  Otherwise, it will display the value entered into the flowsheet row. |
| CARDIOVERT_ATTEMPTS | No | The number of cardioversion attempts that occurred during a code. |
| PULSE_AT_ONSET_YN | No | Whether or not the patient had a pulse at the onset of the code. |
| RESPS_AT_ONSET | VARCHAR (100) | The description of the patient's respirations at the onset of the code. |
| ETT_AT_ONSET_YN | No | Whether a non-surgical airway was in place at the onset of the code. |
| TRACH_AT_ONSET_YN | No | Whether a surgical airway was in place at the onset of the code. |
| CHEST_TUBE_AT_ONSET_YN | No | Whether a chest tube was in place at the onset of the code. |
| ETT_PLACED_YN | No | Whether a non-surgical airway was placed during the code. |
| TRACH_PERFORM_YN | No | Whether a surgical airway was placed during the code. |
| CHEST_TUBE_PLACED_YN | No | Whether a chest tube was placed during the code. |
| PAT_CONSC_AT_ONSET | VARCHAR (100) | Whether the patient was conscious at the onset of the code. |
| BLOOD_RECEIVED_ML | No | The amount of blood received, in mL, during the code. |
| EPI_ADMINS | No | The number of times a unit of epinephrine was administered during the code. |
| ADENOSINE_ADMINS | No | The number of times a unit of adenosine was administered during the code. |
| AMIODARONE_ADM_YN | No | Whether amiodarone was administered during the code. |
| ATROPINE_ADMINS | No | The number of times a unit of atropine was administered during the code. |
| LIDOCAINE_ADMINS | No | The number of times a unit of lidocaine was administered during the code. |
| ASYSTOLIC_RHYTHM_YN | No | Whether the patient ever had an asystolic rhythm during the code. |
| COMPRESSIONS_YN | No | Whether compressions were used as an intervention during the code. |
| GLASGOW_COMA_SCALE | No | The patient's Glasgow Coma Score as recorded during the code. |
| UPDATE_DATE | No | The date and time this row was last updated (the last time the row was extracted or the last time this column was backfilled). |
| DEPARTMENT_ID | NUMERIC (18,0) | The ID number of the department in which the code occurred. |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | EVENT_ID | ED_IEV_PAT_INFO | EVENT_ID | Unknown | Unknown | No |  |
| 1 | EVENT_ID | IP_MAR_BARCODE_ITM | EVENT_ID | Unknown | Unknown | No |  |
| 3 | PAT_ENC_CSN_ID | ALT_ORD_PROV_SINGL | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 3 | PAT_ENC_CSN_ID | AN_RELINK_INFO | PAT_ENC_CSN_ID | No | Unknown | No |  |
| 3 | PAT_ENC_CSN_ID | DENT_ORTH_EXAM_NOTES | PAT_ENC_CSN_ID | No | Unknown | No |  |
| 3 | PAT_ENC_CSN_ID | FAC_CHG_OVERRIDE | PAT_ENC_CSN_ID | No | Unknown | No |  |
| 3 | PAT_ENC_CSN_ID | FAM_HX_PAT_ONLY | PAT_ENC_CSN_ID | No | Unknown | No |  |
| 3 | PAT_ENC_CSN_ID | F_ED_ENCOUNTERS | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 3 | PAT_ENC_CSN_ID | F_HH_CERT_ATTRIBUTES | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 3 | PAT_ENC_CSN_ID | F_HH_OASIS_SINGLE | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 3 | PAT_ENC_CSN_ID | F_HH_OASIS_SINGLE_2 | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 3 | PAT_ENC_CSN_ID | F_HH_OASIS_SINGLE_3 | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 3 | PAT_ENC_CSN_ID | F_HH_OASIS_SINGLE_4 | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 3 | PAT_ENC_CSN_ID | F_HH_OASIS_SINGLE_5 | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 3 | PAT_ENC_CSN_ID | F_IBD_ADULT_FORM_ENC | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 3 | PAT_ENC_CSN_ID | F_IBD_FORM_RESP | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 3 | PAT_ENC_CSN_ID | F_IP_HSP_ADMISSION | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 3 | PAT_ENC_CSN_ID | F_IP_HSP_SEPSIS3 | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 3 | PAT_ENC_CSN_ID | F_IRIS_ENC | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 3 | PAT_ENC_CSN_ID | F_MU_OBJ_EH_ADMISSION | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 3 | PAT_ENC_CSN_ID | F_MU_QM_EH_2014_ED_VISIT | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 3 | PAT_ENC_CSN_ID | F_MU_QM_EH_2014_IP_ADMSN | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 3 | PAT_ENC_CSN_ID | F_QM_AMI | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 3 | PAT_ENC_CSN_ID | F_QM_CAC | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 3 | PAT_ENC_CSN_ID | F_QM_HBIPS | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 3 | PAT_ENC_CSN_ID | F_QM_HEART_FAILURE | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 3 | PAT_ENC_CSN_ID | F_QM_IMMUNIZATION | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 3 | PAT_ENC_CSN_ID | F_QM_PC_BABY | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 3 | PAT_ENC_CSN_ID | F_QM_PC_MOM | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 3 | PAT_ENC_CSN_ID | F_QM_PNEUMONIA | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |

_(140 total; showing first 30)_
