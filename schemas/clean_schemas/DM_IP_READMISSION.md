# DM_IP_READMISSION

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=DM_IP_READMISSION

## Description

This registry stores both current and historical information related to the topic of readmissions. This registry consolidates hospital admission information from many subject areas including lab values, vitals, medications, diagnoses, and social history. Only hospital admissions that meet specific inclusion criteria have information stored in this registry. Note: This table does not contain information on the concept of index admissions and subsequent readmissions. See F_IP_HSP_ADMISSION for details on this definition of readmission.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | RDT |
| Release Version | Rel 2015 |
| May contain EHI? | No |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| RECORD_ID | NUMERIC (18,0) | The unique identifier (.1 item) for the registry data record. |
| DM_DATE | No | The date the current row's values were extracted. |
| REGISTRY_STATUS_C | INTEGER |  |
| PAT_ID | VARCHAR (18) | The unique ID of the record for this row.  This column holds the ID as of when the row was extracted. If the patient was merged or unmerged after this record was deleted from Chronicles, this PAT_ID may not reflect the current ID of the patient. To reference the current ID of the patient, use the PAT_ID column in the PAT_ENC table. Join to the PAT_ENC table on the CSN columns in each table. |
| PAT_ENC_CSN_ID | No | The unique contact serial number of the patient encounter for this row. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| IS_ENCOUNTER_A_READMISSION_YN | No | Indicates whether an encounter is a readmission, based on the parameters given in the associated rule.  Rule: DM IP IS ENCOUNTER A READMISSION (84095) |
| HAS_READMISSION_BPA_YN | No | Indicates whether a patient meets the criteria in the intervention record specified in the associated rule. The column will store N if the patient does not meet the criteria, the associated rule is not configured, or if the intervention record does not include a triggering action of "16-Reporting Workbench."  Rule: DM IP QUALIFIES FOR READMISSION INTERVENTION (84067) |
| DISCHARGE_DISPOSITION_C | VARCHAR (66) |  |
| DISCHARGE_DEST_C | VARCHAR (66) |  |
| HOSPITAL_SERVICE_C | VARCHAR (66) |  |
| PAT_CLASS_C | VARCHAR (66) |  |
| ADMISSION_TYPE_C | VARCHAR (66) |  |
| ADMISSION_SOURCE_ID | NUMERIC (18,0) | This column stores the organization at which the patient was located before they arrived at the hospital for their visit.  Rule: DM IP ADMISSION SOURCE (84073) |
| ADMISSION_DEPARTMENT_ID | No | This column stores the first unit that a patient was admitted to during their hospital encounter.  Rule: DM IP ADMITTING DEPARTMENT (84075) |
| ADMISSION_DATE | DATETIME | This column stores the hospital admission date of a patient encounter. If the patient was admitted through the ED, this will be the date the patient was roomed in the ED.  Rule: DM IP ADMISSION DATE (INPATIENT OR ED) (84076) |
| INPATIENT_ADMISSION_DATE | No | This column stores the date when a patient admission's patient class was mapped to an Inpatient base class.  Rule: DM IP INPATIENT ADMISSION DATE (84078) |
| DISCHARGE_DATE | DATETIME | This column stores the date that the patient was discharged for the given encounter.  Rule: DM IP DISCHARGE DATE (84028) |
| PAT_AGE_YEARS_AT_ADMISSION | No | This column stores the age of the patient at the time of admission for the given encounter.  Rule: DM IP AGE AT ADMISSION (84030) |
| MEMBER_OF_ASTHMA_REGISTRY | No | This column stores 1 if the patient is a member of the Asthma registry and 0 if the patient is not.  Rule: DM IP IS MEMBER OF ASTHMA REGISTRY (84083) |
| MEMBER_OF_CKD_REGISTRY | No | This column stores 1 if the patient is a member of the Chronic Kidney Disease (CKD) registry and 0 if the patient is not.  Rule: DM IP IS MEMBER OF CHRONIC KIDNEY DISEASE REGISTRY (84084) |
| MEMBER_OF_COPD_REGISTRY | No | This column stores 1 if the patient is a member of the Chronic Obstructive Pulmonary Disease (COPD) registry and 0 if the patient is not.  Rule: DM IP IS MEMBER OF COPD REGISTRY (84085) |
| MEMBER_OF_CHF_REGISTRY | No | This column stores 1 if the patient is a member of the Chronic Heart Failure (CHF) registry and 0 if the patient is not.  Rule: DM IP IS MEMBER OF CHF REGISTRY (84031) |
| MEMBER_OF_CAD_REGISTRY | No | This column stores 1 if the patient is a member of the Coronary Artery Disease (CAD) registry and 0 if the patient is not.  Rule: DM IP IS MEMBER OF CORONARY ARTERY DISEASE REGISTRY (84086) |
| MEMBER_OF_CF_REGISTRY | No | This column stores 1 if the patient is a member of the Cystic Fibrosis (CF) registry and 0 if the patient is not.  Rule: DM IP IS MEMBER OF CYSTIC FIBROSIS REGISTRY (84087) |
| MEMBER_OF_DIABETES_REGISTRY | No | This column stores 1 if the patient is a member of the Diabetes registry and 0 if the patient is not.  Rule: DM IP IS MEMBER OF DIABETES REGISTRY (84088) |
| MEMBER_OF_HIV_REGISTRY | No | This column stores 1 if the patient is a member of the Human Immunodeficiency Virus (HIV) registry and 0 if the patient is not.  Rule: DM IP IS MEMBER OF HUMAN IMMUNODEFICIENCY VIRUS REGISTRY (84089) |
| MEMBER_OF_HTN_REGISTRY | No | This column stores 1 if the patient is a member of the Hypertension (HTN) registry and 0 if the patient is not.  Rule: DM IP IS MEMBER OF HYPERTENSION REGISTRY (84090) |
| MEMBER_OF_OBESITY_REGISTRY | No | This column stores 1 if the patient is a member of the Obesity registry and 0 if the patient is not.  Rule: DM IP IS MEMBER OF OBESITY REGISTRY (84091) |
| MEMBER_OF_OPO_REGISTRY | No | This column stores 1 if the patient is a member of the Osteoporosis registry and 0 if the patient is not.  Rule: DM IP IS MEMBER OF OSTEOPOROSIS REGISTRY (84092) |
| MEMBER_OF_PREDIABETES_REGISTRY | No | This column stores 1 if the patient is a member of the Prediabetes registry and 0 if the patient is not.  Rule: DM IP IS MEMBER OF PREDIABETES REGISTRY (84093) |
| MEMBER_OF_TOBACCO_REGISTRY | No | This column stores 1 if the patient is a member of the Tobacco registry and 0 if the patient is not.  Rule: DM IP IS MEMBER OF TOBACCO REGISTRY (84094) |
| MOST_RECENT_HEIGHT | No | This column stores the patient's most recently recorded height in inches for the specified encounter.  Rule: DM IP HEIGHT (84037) |
| MOST_RECENT_WEIGHT | NUMERIC (18,2) | This column stores the patient's most recently recorded weight, in ounces, for the specified encounter.  Rule: DM IP WEIGHT (84038) |
| MOST_RECENT_BMI | NUMERIC (18,2) | This column stores the patient's most recently calculated BMI.  Rule: DM IP MOST RECENT BMI FOR VISIT (84052) |
| NUM_ACTIVE_MEDICATION_ORDERS | No | This column stores the number of active inpatient and outpatient medication orders (that are not complete) for the patient. PTA medications and cross-encounter medications are included.  Rule: DM IP MEDICATION COUNT (84053) |
| MOST_RECENT_SYSTOLIC_BP | NUMERIC (18,2) | This column stores the patient's most recently recorded systolic blood pressure measurement for the given encounter.  Rule: DM IP MOST RECENT SYSTOLIC BP FOR VISIT (84054) |
| MOST_RECENT_DIASTOLIC_BP | NUMERIC (18,2) | This column stores the patient's most recently recorded diastolic blood pressure measurement for the given encounter.  Rule: DM IP MOST RECENT DIASTOLIC BP FOR VISIT (84055) |
| MOST_RECENT_PULSE | NUMERIC (18,0) | This column stores the patient's most recently recorded pulse measurement for the given encounter.  Rule: DM IP MOST RECENT PULSE FOR VISIT (84056) |
| MOST_RECENT_TEMPERATURE | NUMERIC (18,2) | This column stores a patient's most recently documented temperature in degrees Fahrenheit for a given encounter.  Rule: DM IP TEMPERATURE (84081) |
| MOST_RECENT_LAB_COMPON_VAL | No | This column stores the most recent lab value for the lab specified in the associated rule recorded during an admission.  Rule: DM IP MOST RECENT LAB VALUE: ENCOUNTER (84082) |
| MOST_RECENT_PULSE_OXI | NUMERIC (18,0) | This column stores the patient's last recorded pulse oximetry reading for the given encounter.  Rule: DM IP MOST RECENT PULSE OXIMETRY FOR VISIT (84057) |
| MOST_RECENT_RESPIRATIONS | NUMERIC (18,0) | This column stores the patient's last recorded respirations measurement for the given encounter.  Rule: DM IP MOST RECENT RESPIRATIONS FOR VISIT (84058) |
| LENGTH_OF_STAY | No | This column stores the duration of stay between discharge (or today if still admitted) and the time when the patient was first admitted, including time spent on leave of absence.  Rule: DM IP DURATION OF STAY OF VISIT (84060) |
| INPATIENT_LENGTH_OF_STAY | No | This column stores the total time the patient had a base class of Inpatient, including time spent on leave of absence from an inpatient admission.  Rule: DM IP LENGTH OF STAY OF VISIT (84061) |
| DAYS_SINCE_LAST_ADMISSION | No | This column stores the number of days between the encounter's admission date and the patient's last discharge date prior to that.  Rule: DM IP NUMBER OF DAYS SINCE LAST ADMISSION WITHIN ORGANIZATION (84062) |
| NUM_ED_VISITS | No | This column stores the number of emergency department (ED) visits prior to and including the start date of the specified encounter. This is calculated using only Epic data.  Rule: DM IP NUMBER OF EMERGENCY VISITS WITHIN ORGANIZATION IN THE LAST X DAYS (84063) |
| NUM_HOSPITAL_ENC | No | This column stores the number of admissions the patient has had within a given timeframe, excluding the given encounter and HOVs. This is calculated using only Epic data.  Rule: DM IP NUMBER OF HOSPITAL ADMISSIONS WITHIN THE ORGANIZATION IN THE LAST X DAYS (84064) |
| FROM_ED_DURING_BUSINESS_HOURS | No | This column stores 1 if the patient arrived in the emergency department during business hours, 0 if they arrived outside of business hours, and null if there was no arrival.  Rule: DM IP FROM ED DURING BUSINESS HOURS (84039) |
| NUM_COMPLETED_NON_SURGICAL_PX | No | This column stores the number of non-surgical procedures performed that match or do not match on the parameters given in the associated rule for the encounter.  Rule: DM IP NUMBER OF NON-SURGICAL PROCEDURES PERFORMED (84097) |
| NUM_COMPLETED_SURGICAL_PX | No | This column stores the number of surgical procedures performed during a given patient encounter.  Rule: DM IP NUMBER OF SURGICAL PROCEDURES PERFORMED (84098) |
| PAT_POSTAL_CODE | VARCHAR (24) | This column stores the most recently listed postal code for the patient.  Rule: DM IP PATIENT ZIP CODE (84041) |
| PAT_RACE_C | INTEGER |  |
| PAT_ETHNICITY_C | INTEGER |  |
| LANGUAGE_SPOKEN_C | VARCHAR (66) |  |
| LANGUAGE_WRITTEN_C | VARCHAR (66) |  |
| PAT_SEX_C | VARCHAR (66) |  |
| PAT_MARITAL_STATUS_C | INTEGER |  |
| NUM_ADDRESS_CHANGES | No | This column stores the number of address changes for a patient over a number of months specified in the given rule prior to the given patient encounter.  Rule: DM IP NUMBER OF ADDRESS CHANGES OVER PREVIOUS X MONTHS (4125) |
| PAYOR_ID | No | This column stores the primary coverage payor for a patient encounter.  Rule: DM IP PRIMARY COVERAGE PAYOR FOR ENCOUNTER (4126) |
| BENEFIT_PLAN_ID | No | This column stores the primary coverage plan for a patient encounter.  Rule: DM IP PRIMARY COVERAGE PLAN FOR ENCOUNTER (4127) |
| IS_ENC_MEDICARE_YN | No | Indicates whether an encounter has an effective Medicare coverage..  Rule: DM IP IS ENCOUNTER MEDICARE (4122) |
| IS_ENC_MEDICAID_YN | No | Indicates whether an encounter has an effective Medicaid coverage.  Rule: DM IP IS ENCOUNTER MEDICAID (4123) |
| PCP_PRIMARY_DEPARTMENT_ID | No | This column stores the patient's PCP primary department ID.  Rule: DM IP PCP CLINIC (84050) |
| PAT_PREFERRED_PHARMACY_ID | NUMERIC (18,0) | This column stores the ID of the first pharmacy in the list of a patient's preferred pharmacies (I EPT 18800).  Rule: DM IP PATIENT'S PREFERRED PHARMACY (84026) |
| NO_SHOW_RATE | No | This column stores the no-show rate of a patient for 365 days prior to the admission date on the contact being evaluated.  Rule: DM IP NO SHOW RATE FROM ADMISSION DATE (31020) |
| NUM_DISCHARGE_RX | No | This column stores a count of active outpatient medications at the time of discharge for a given encounter. This count includes patient-reported medications. If the patient is still admitted, this column will store null.  Rule: DM IP NUMBER OF OUTPATIENT MEDS AT DISCHARGE (84460) |
| PAT_PCP_PROV_ID | No | This column stores the Provider ID (SER ID) of the patient's PCP for a given encounter, based on the PCP type specified in the associated rule. By default, the General PCP for the patient will be returned.  Rule: DM IP PATIENT PCP ID (84461) |
| PAT_HAS_FOLLOWUP_DOCUMENTED_YN | No | This column stores Y if a patient has any documented follow-ups, N otherwise.  Rule: DM IP PATIENT HAS FOLLOWUP DOCUMENTED (84462) |
| ADMSN_MIN_SINCE_MIDNIGHT | No | This column stores the number of minutes since midnight that the patient was admitted. If the patient was admitted through the ED, this will be the number of minutes after midnight that they were first roomed.  Rule: DM IP MINUTES FROM MIDNIGHT TO ADMISSION TIME (84450) |
| DISCHARGE_MIN_SINCE_MIDNIGHT | No | This column stores the number of minutes since midnight that the patient was discharged. If the patient has not been discharged yet, this will be blank.  Rule: DM IP MINUTES FROM MIDNIGHT TO DISCHARGE (84452) |
| INPAT_ADMSN_MIN_SINCE_MIDNIGHT | No | This column stores the number of minutes since midnight that the patient was first admitted with a base patient class of inpatient.  Rule: DM IP MINUTES FROM MIDNIGHT TO INPATIENT ADMISSION TIME (84451) |
| ED_ARRIVAL_MIN_SINCE_MIDNIGHT | No | This column stores the number of minutes since midnight that the patient was arrived in the ED. If the patient was not seen in the ED, this will be blank.  Rule: DM IP MINUTES FROM MIDNIGHT TO ED ARRIVAL (84453) |
| REVENUE_LOCATION_ID | No | This column stores the ID of the revenue location associated with the current unit of the patient's encounter. If the patient is discharged, this will be the revenue location associated with their discharging department.  Rule: DM IP REVENUE LOCATION (84051) |
| PRESENT_ON_ADMSN_DX_CODE_LIST | No | This column stores the patient's admission diagnoses for the given encounter as a pipe-delimited list of ICD-10 codes corresponding to a patient encounter's hospital diagnoses from EPT 18430. If there are no admission diagnoses, the value will be null.  Rule: DM IP PRESENT ON ADMISSION DIAGNOSES: CODED (84033) |
| HOSPITAL_ACQUIRED_DX_CODE_LIST | No | This column stores the patient's hospital acquired diagnoses for the given encounter as a pipe-delimited list of ICD-10 codes corresponding to a patient encounter's hospital acquired diagnoses from EPT 18430. If there are no hospital acquired diagnoses, this value will be null.  Rule: DM IP HOSPITAL ACQUIRED DIAGNOSES: CODED (84034) |
| VISIT_DX_CODE_LIST | No | This column stores the patient's hospital diagnoses for the given encounter as a pipe-delimited list of ICD-10 codes corresponding to a patient encounter's hospital diagnoses from EPT 18430. If there are no hospital diagnoses, this value will be null.  Rule: DM IP HOSPITAL DIAGNOSES: CODED (84036) |
| ADMISSION_DX_CODE_LIST | No | This column stores the patient encounter's admitting diagnoses as a pipe-delimited list of ICD-10 codes associated with the admitting diagnoses from EPT 10150. If there are no admitting diagnoses, this value will be null.  Rule: DM IP ADMITTING DIAGNOSES: CODED (84074) |
| DISCHARGE_DX_CODE_LIST | No | This column stores the patient's discharge diagnoses for the given encounter as a pipe-delimited list of ICD-10 codes corresponding to a patient encounter's discharge diagnoses from EPT 10207. If there are no discharge diagnoses or the encounter is not yet discharged, this value will be null.  Rule: DM IP DISCHARGE DIAGNOSES: CODED (84035) |
| PRINCIPAL_PROBLEM_DX_CODE_LIST | No | This column stores the principal problem associated with a patient encounter as a pipe-delimited list of ICD-10 codes associated with the LPL record in EPT 18431. If no principal problem is listed, this value will be null.  Rule: DM IP PRINCIPAL PROBLEM: CODED (84080) |
| READMISSION_RISK_SCORE | No | This column stores the latest valid score for the scoring system specified in System Definitions item 34678 Default Readmission Risk Scoring System.  Rule: DM IP LATEST READMISSION RISK SCORE (84463) |
| DISCHARGED_DECEASED_YN | No | This column stores whether or not the encounter's discharge disposition was 'Expired.' If null, then a discharge disposition was not found for this patient, or the patient is still admitted.  Rule: DM IP DISCHARGED AS DECEASED (84464) |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| B-TREE INDEX | EIX_DM_IP_READMISSION_PATCSN | PAT_ENC_CSN_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_DM_IP_READMISSION_PATID | PAT_ID | 1 | Yes | Yes |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | RECORD_ID | DM_ACG_RISK | RECORD_ID | Unknown | Yes | No |  |
| 1 | RECORD_ID | DM_ACO | RECORD_ID | Unknown | Yes | No |  |
| 1 | RECORD_ID | DM_ACO_EXT | RECORD_ID | Unknown | Yes | No |  |
| 1 | RECORD_ID | DM_ACTIVE_PAT | RECORD_ID | Unknown | Yes | No |  |
| 1 | RECORD_ID | DM_ADHD | RECORD_ID | Unknown | Yes | No |  |
| 1 | RECORD_ID | DM_ADHD_EXT | RECORD_ID | Unknown | Yes | No |  |
| 1 | RECORD_ID | DM_ADOL_TRANS | RECORD_ID | Unknown | Yes | No |  |
| 1 | RECORD_ID | DM_ADOL_TRANS_EXT | RECORD_ID | Unknown | Yes | No |  |
| 1 | RECORD_ID | DM_ADULT_ADHD | RECORD_ID | Unknown | Yes | No |  |
| 1 | RECORD_ID | DM_ADULT_ASTHMA | RECORD_ID | Unknown | Yes | No |  |
| 1 | RECORD_ID | DM_ADULT_DIABETES | RECORD_ID | Unknown | Yes | No |  |
| 1 | RECORD_ID | DM_ADULT_FTM | RECORD_ID | Unknown | Yes | No |  |
| 1 | RECORD_ID | DM_ADULT_FTM_EXT | RECORD_ID | Unknown | Yes | No |  |
| 1 | RECORD_ID | DM_ADULT_HIV | RECORD_ID | Unknown | Yes | No |  |
| 1 | RECORD_ID | DM_ADULT_HYPERTENSION | RECORD_ID | Unknown | Yes | No |  |
| 1 | RECORD_ID | DM_ADULT_MTF | RECORD_ID | Unknown | Yes | No |  |
| 1 | RECORD_ID | DM_ADULT_MTF_EXT | RECORD_ID | Unknown | Yes | No |  |
| 1 | RECORD_ID | DM_ADULT_OBESITY | RECORD_ID | Unknown | Yes | No |  |
| 1 | RECORD_ID | DM_ALS | RECORD_ID | Unknown | Yes | No |  |
| 1 | RECORD_ID | DM_ANESTHESIA | RECORD_ID | Unknown | Yes | No |  |
| 1 | RECORD_ID | DM_ANESTHESIA_2 | RECORD_ID | Unknown | Yes | No |  |
| 1 | RECORD_ID | DM_ASTHMA | RECORD_ID | Unknown | Yes | No |  |
| 1 | RECORD_ID | DM_ASTHMA_EXT | RECORD_ID | Unknown | Yes | No |  |
| 1 | RECORD_ID | DM_ATRIAL_FIBRILLATION | RECORD_ID | Unknown | Yes | No |  |
| 1 | RECORD_ID | DM_BREAST_HEALTH | RECORD_ID | Unknown | Yes | No |  |
| 1 | RECORD_ID | DM_CAD | RECORD_ID | Unknown | Yes | No |  |
| 1 | RECORD_ID | DM_CAD_DIABETES | RECORD_ID | Unknown | Yes | No |  |
| 1 | RECORD_ID | DM_CAD_EXT | RECORD_ID | Unknown | Yes | No |  |
| 1 | RECORD_ID | DM_CANCER_PATIENT | RECORD_ID | Unknown | Yes | No |  |
| 1 | RECORD_ID | DM_CANCER_PROBLEM | RECORD_ID | Unknown | Yes | No |  |

_(492 total; showing first 30)_
