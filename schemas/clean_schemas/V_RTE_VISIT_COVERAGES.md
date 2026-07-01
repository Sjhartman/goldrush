# V_RTE_VISIT_COVERAGES

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=V_RTE_VISIT_COVERAGES

## Description

This view is used by a datalink query that populates Eligibility Metrics based on visit coverages.

## Metadata

| Property | Value |
| --- | --- |
| Type | View |
| Release Version | Rel November 2019 |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| PAT_ENC_CSN_ID | NUMERIC (18,0) | A unique serial number for this encounter. This number is unique across all patients and encounters in the system. |
| PAT_ID | VARCHAR (18) | The unique ID assigned to the patient record. This ID may be encrypted if you have elected to use enterprise reporting?s encryption utility. |
| CONTACT_DATE | No | This is the contact date of the patient encounter. Taken from the V_REG_VERIF_METRICS table as the applicable value of either ENC_SERVICE_DATE or HAR_SERVICE_DATE. |
| COVERAGE_ID | NUMERIC (18,0) | The unique ID assigned to the coverage record. This ID may be encrypted if you have elected to use enterprise reporting?s encryption utility. |
| PAYOR_ID | NUMERIC (18,0) | The unique ID assigned to the payor. |
| BENEFIT_PLAN_ID | NUMERIC (18,0) | The unique ID assigned to the benefit plan record in the system. |
| FINANCIAL_CLASS_C | VARCHAR (66) |  |
| DEPARTMENT_ID | NUMERIC (18,0) | The unique ID number assigned to the department record. |
| SERV_AREA_ID | No | The unique ID of the service area in which this department is located. This is the service area for the department, calculated by the function EPIC_DEPTOSA; this function is needed because the service area is linked to the location record and not to the department record directly. |
| LOCATION_ID | NUMERIC (18,0) | The unique ID of the revenue location to which the department is linked. |
| COVERAGE_TYPE_C | INTEGER |  |
| USE_ELCT_VERIF_YN | VARCHAR (1) |  |
| IS_RX_COVERAGE_YN | No | Flag to indicate if the coverage represents an ambulatory pharmacy coverage. |
| CREATED_BY_CTU_YN | No | Flag to indicate if the coverage was created by the Coverage Term Utility. |
| IS_NON_INSURANCE_PAYER_YN | No | Flag to indicate if the coverage is for a non-insurance payer. These are payers that are mapped to reference payer 41 (non-insurance). |

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

_(261 total; showing first 30)_
