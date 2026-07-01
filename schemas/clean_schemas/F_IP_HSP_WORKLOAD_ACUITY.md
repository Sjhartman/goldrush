# F_IP_HSP_WORKLOAD_ACUITY

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=F_IP_HSP_WORKLOAD_ACUITY

## Description

This table stores information pertaining to Workload Acuity scoring systems. Each row is a filed score identified by the associated patient CSN, date-time of filing, and scoring system used. The table calculates and stores the subscores from each rule group in the specified scoring system, as well as associated information about each filed score.

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
| ACUITY_SYSTEM_ID | NUMERIC (18,0) | This item stores the scoring system record ID used to calculate the score. |
| SCORE_LOC_DTTM | DATETIME (Local) | This item stores the instant at which the rule and system scores are calculated.  If the score is manually filed, this is the time it was filed; if the score was calculated by a batch job, it is the time when the batch job was run. |
| SCORE_UTC_DTTM | DATETIME (UTC) | This column stores the instant at which the rule and system scores are calculated in UTC.  If the score is manually filed, this is the time it was filed; if the score was calculated by a batch job, it is the time when the batch job was run. |
| SCORE_DATE_LOC | No | This item stores the date portion of SCORE_LOC_DTTM for reporting purposes. |
| SCORE_TIME_LOC | No | This item stores the time portion of SCORE_DTTM_LOC in the form "minutes since midnight" for reporting purposes. |
| DEPT_ID | NUMERIC (18,0) | This item stores the patient's department at the time the score was filed. |
| TRTMT_TM_NURSE_CUR_ID | VARCHAR (18) | This column stores the provider ID of the most recently assigned treatment team member with a Nursing relationship at the time the score was filed.  The Nursing relationship is defined in System Definitions (LSD). If multiple treatment team relationships are defined under Nursing, it is assumed that the value on the first line is the primary Nursing relationship. |
| SCORE_TOTAL | NUMERIC (18,5) | This column stores the total score at the time the score was filed. |
| SCORE_MEDICATIONS | NUMERIC (18,5) | This column stores the score corresponding to the Medications group as set in the Scoring System Editor. |
| SCORE_ASSESSMENTS | NUMERIC (18,5) | This column stores the score corresponding to the Assessments group as set in the Scoring System Editor. |
| SCORE_RISKS | NUMERIC (18,5) | This column stores the score corresponding to the Risks group as set in the Scoring System Editor. |
| SCORE_ADMISSION_TRANSFER | NUMERIC (18,5) | This column stores the score corresponding to the Admission/Transfer group as set in the Scoring System Editor. |
| SCORE_DISCHARGE | NUMERIC (18,5) | This column stores the score corresponding to the Discharge group as set in the Scoring System Editor. |
| SCORE_ORDERS | NUMERIC (18,5) | This column stores the score corresponding to the Orders group as set in the Scoring System Editor. |
| SCORE_LDA_CARE | NUMERIC (18,5) | This column stores the score corresponding to the LDA Care group as set in the Scoring System Editor. |
| SCORE_WOUNDS | NUMERIC (18,5) | This column stores the score corresponding to the Wounds group as set in the Scoring System Editor. |
| SCORE_ADL | NUMERIC (18,5) | This column stores the score corresponding to the ADLs group as set in the Scoring System Editor. |
| UPDATE_DATE | No | This column stores the date and time when this row was created or last updated. |
| PAT_ID | VARCHAR (18) | The unique ID of the patient record for this row. |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| B-TREE INDEX | EIX_F_IP_HSP_ACUITY_DEPT | DEPT_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_F_IP_HSP_ACUITY_LOC_DTTM | SCORE_LOC_DTTM | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_F_IP_HSP_ACUITY_NURSE | TRTMT_TM_NURSE_CUR_ID | 1 | Yes | Yes |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | PAT_ENC_CSN_ID | ALT_ORD_PROV_SINGL | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 1 | PAT_ENC_CSN_ID | AN_RELINK_INFO | PAT_ENC_CSN_ID | No | Unknown | No |  |
| 1 | PAT_ENC_CSN_ID | DENT_ORTH_EXAM_NOTES | PAT_ENC_CSN_ID | No | Unknown | No |  |
| 1 | PAT_ENC_CSN_ID | FAC_CHG_OVERRIDE | PAT_ENC_CSN_ID | No | Unknown | No |  |
| 1 | PAT_ENC_CSN_ID | FAM_HX_PAT_ONLY | PAT_ENC_CSN_ID | No | Unknown | No |  |
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

_(185 total; showing first 30)_
