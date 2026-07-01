# F_ED_ENCOUNTERS

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=F_ED_ENCOUNTERS

## Description

The F_ED_ENCOUNTERS table stores commonly used information for ED encounters. Each emergency department encounter has a single row in this table. Encounters that are pending or cancelled are not included in this table.

## Metadata

| Property | Value |
| --- | --- |
| Type | Derived Table |
| Load Frequency | INCREMENTAL |
| Release Version | Rel 2015 |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| PAT_ENC_CSN_ID | NUMERIC (18,0) | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| UPDATE_DATE | No | This column contains the last date and time at which this row was updated. |
| ED_EPISODE_ID | NUMERIC (18,0) | The unique ID of the Inpatient episode record for the ED visit. |
| PAT_ID | VARCHAR (18) | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| AGE_AT_ARRIVAL_YEARS | EPT | This column is the patient's calculated age in years upon arrival. |
| AGE_AT_ARRIVAL_MONTHS | EPT | This column is the patient's calculated age in months upon arrival. |
| ENC_ADDRESS_LINE | No | The line on which the patient's address is documented on or before the day after arrival. This column is used to link to PAT_ADDR_CHNG_HX. |
| ADT_ARRIVAL_DATE | DATETIME | The date of the patient's arrival. |
| ADT_ARRIVAL_DTTM | 10820 | The date and time of arrival for this patient contact. |
| MEANS_OF_ARRIVAL_C | VARCHAR (66) |  |
| AMBULANCE_CODE_C | INTEGER |  |
| PRIVATE_HOSPITAL_ENC_C | INTEGER |  |
| DISASTER_NUM | VARCHAR (50) | This column stores the disaster number, which is a number given by the ambulance company to patients during catastrophes that cause massive patient influxes to the hospital. |
| ACUITY_LEVEL_C | VARCHAR (66) |  |
| HOSPITAL_ADMISSION_DTTM | 18850 | The date and time that the patient was first admitted to the facility, bedded in the ED, or confirmed for an HOV for this contact, regardless of patient's base patient class. |
| ADMISSION_EVENT_ID | No | The ID number of the admission event record from the ADT master file for this patient stay. |
| EMERGENCY_ADMISSION_DTTM | 10296 | The date and time during the hospital encounter when the patient first received a base patient class of emergency. |
| EMERGENCY_ADMISSION_EVENT_ID | NUMERIC (18,0) | The event record for the hospital encounter where the patient first received a base patient class of emergency. |
| FIRST_CHIEF_COMPLAINT_ID | NUMERIC (18,0) | This column stores the chief complaint ID stored on line 1. |
| FIRST_CHIEF_COMPLAINT_OTHER | No | The custom reason for visit entered when the clinical system user chooses ?Other? as a reason for visit on line 1. |
| NUM_CHIEF_COMPLAINTS_ENC | No | The number of chief complaints documented on the encounter. |
| ED_DISPOSITION_C | VARCHAR (66) |  |
| ED_DISPOSITION_DTTM | DATETIME (Local) | The date and time that the disposition was entered. |
| ED_DISPOSITION_PAT_CONDITION_C | INTEGER |  |
| PRIMARY_DX_ID | NUMERIC (18,0) | The primary diagnosis ID for the encounter. This column can be used to link to CLARITY_EDG. |
| PRIMARY_DX_LINE | No | The line number associated with the primary diagnosis. This can be used with PAT_ENC_CSN_ID to link to the primary diagnosis in PAT_ENC_DX. |
| PRIMARY_DX_ED_YN | VARCHAR (1) |  |
| NUM_DX_ENC | No | The number of visit diagnoses documented on this encounter. |
| NUM_ED_DX_ENC | No | The number of ED visit diagnoses documented on this encounter. |
| ED_DEPARTURE_DTTM | 49020 | Date and time the patient left the ED. |
| ED_PRIMARY_CARE_AREA_ID | NUMERIC (18,0) | The unique ID for the primary area of care for the patient during their stay in the ED. |
| FIRST_EMERGENCY_DEPARTMENT_ID | NUMERIC (18,0) | The unique ID of the first emergency department the patient was roomed in. |
| LAST_EMERGENCY_DEPARTMENT_ID | NUMERIC (18,0) | The unique ID of the last emergency department the patient was roomed in. |
| HOSPITAL_DISCHARGE_DATE | DATETIME | The hospital discharge date for this patient contact. |
| HOSPITAL_DISCHARGE_DTTM | 18855 | The hospital discharge date and time for this patient contact. |
| DISCHARGE_EVENT_ID | No | The ID number of the discharge event record from the ADT master file for this patient stay. |
| LAST_DEPARTMENT_ID | NUMERIC (18,0) | The ID number of the unit for the most recent location of the patient for this patient contact. |
| ADT_SERVICE_AREA_ID | NUMERIC (18,0) | The ID number of the service area for the most recent location of the patient for this patient contact. |
| DISCHARGE_DISPOSITION_C | VARCHAR (66) |  |
| DISCHARGE_DESTINATION_C | VARCHAR (66) |  |
| INPATIENT_ADMISSION_DTTM | 10290 | The date and time of inpatient admission. This is the date and time during the hospital encounter when the patient first received a base patient class of inpatient. This data will come from the encounter with CSN stored in INPATIENT_PAT_ENC_CSN_ID. This could be the same encounter as the ED encounter, or it could be an inpatient encounter within 1 hour of hospital discharge if this encounter was never inpatient. |
| INPATIENT_ADMISSION_EVENT_ID | NUMERIC (18,0) | The ADT event record for when the patient first received a base patient clas of inpatient. This data will come from the encounter with CSN stored in INPATIENT_PAT_ENC_CSN_ID. This could be the same encounter as the ED encounter, or it could be an inpatient encounter within 1 hour of hospital discharge if this encounter was never inpatient. |
| INPATIENT_PAT_ENC_CSN_ID | NUMERIC (18,0) | The encounter CSN for an inpatient encounter within 1 hour of hospital discharge if this encounter was never inpatient (PAT_ENC_HSP.INP_ADM_DATE is null). This corresponds to the inpatient portion of a stay in discharge/readmit workflows. If this encounter was a combined ED/IP encounter, then this will be the same as the encounter CSN. |
| PREV_HSP_PAT_ENC_CSN_ID | NUMERIC (18,0) | The encounter CSN for the previous hospital encounter if that encounter was discharged less than 60 days ago. |
| PREV_HSP_ENC_ED_YN | No | This column stores whether the previous encounter (whose CSN is stored in PREV_HSP_ENC_CSN_ID) was an ED encounter. |
| PREV_HSP_ENC_INPATIENT_YN | No | This column stores whether the previous encounter (whose CSN is stored in PREV_HSP_ENC_CSN_ID) was an inpatient encounter. |
| PREV_HSP_ENC_DATEDIFF | No | This column stores the time difference in days between the arrival time of this encounter and the discharge time of the encounter whose encounter CSN is stored in PREV_HSP_ENC_CSN_ID. |
| PREV_HSP_ENC_HOURDIFF | No | This column stores the time difference in hours between the arrival time of this encounter and the discharge time of the encounter whose encounter CSN is stored in PREV_HSP_ENC_CSN_ID. |
| HOSPITAL_ACCOUNT_ID | NUMERIC (18,0) | The unique ID number of the hospital account for this patient contact. |
| PCP_AT_ENC_PROV_ID | VARCHAR (18) | The unique ID of the provider record for the patient?s General Primary Care Provider as of the date of the encounter. This ID may be encrypted if you have elected to use enterprise reporting?s security utility. |
| FIRST_ED_ATTEND_PROV_ID | VARCHAR (18) | The unique ID of the attending provider for the patient who was first assigned to the patient as an ED attending. |
| LAST_ED_ATTEND_PROV_ID | VARCHAR (18) | The unique ID of the attending provider for the patient who was last unassigned to the patient as an ED attending. |
| LONGEST_ED_ATTEND_PROV_ID | VARCHAR (18) | The unique ID of the attending provider for the patient who had the most time assigned to the patient as an ED attending. |
| LOA_PAT_ENC_CSN_ID | NUMERIC (18,0) | The unique contact serial number for the contact on leave of absence when this encounter happened. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| LOA_LINE | INTEGER | The line number for the information associated with this LOA contact. Multiple LOAs can be associated with a contact. |
| PREV_ED_PAT_ENC_CSN_ID | NUMERIC (18,0) | The encounter CSN for the previous emergency encounter if that encounter was discharged less than 60 days ago.  This encounter CSN may be the same as the encounter CSN found in PREV_HSP_PAT_ENC_CSN_ID, if the most recent hospital encounter within the last 60 days is also an emergency encounter. |
| PREV_ED_ENC_DATEDIFF | No | This column stores the time difference in days between the arrival time of this encounter and the discharge time of the encounter whose encounter CSN is stored in PREV_ED_ENC_CSN_ID. |
| PREV_ED_ENC_HOURDIFF | No | This column stores the time difference in hours between the arrival time of this encounter and the discharge time of the encounter whose encounter CSN is stored in PREV_ED_ENC_CSN_ID |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| B-TREE INDEX | EIX_F_ED_ENC_PAT_ID | PAT_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_F_ED_PREV_HSP_PAT_ENC_CSN | PREV_HSP_PAT_ENC_CSN_ID | 1 | Yes | Yes |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | PAT_ENC_CSN_ID | ALT_ORD_PROV_SINGL | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 1 | PAT_ENC_CSN_ID | AN_RELINK_INFO | PAT_ENC_CSN_ID | No | Unknown | No |  |
| 1 | PAT_ENC_CSN_ID | DENT_ORTH_EXAM_NOTES | PAT_ENC_CSN_ID | No | Unknown | No |  |
| 1 | PAT_ENC_CSN_ID | FAC_CHG_OVERRIDE | PAT_ENC_CSN_ID | No | Unknown | No |  |
| 1 | PAT_ENC_CSN_ID | FAM_HX_PAT_ONLY | PAT_ENC_CSN_ID | No | Unknown | No |  |
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
| 1 | PAT_ENC_CSN_ID | HH_PAT_CERT_PERIOD | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |

_(883 total; showing first 30)_
