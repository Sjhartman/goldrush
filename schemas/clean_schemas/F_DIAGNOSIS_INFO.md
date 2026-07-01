# F_DIAGNOSIS_INFO

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=F_DIAGNOSIS_INFO

## Description

This table will be deprecated in the Epic February 2026 release. This derived table finds all diagnoses for all patients. It looks at encounters, the problem list, professional and hospital claims, the hospital account, the hospital admission diagnosis list, surgical cases, medical history, and referrals to collect the diagnoses. It stores how many times a diagnosis was recorded for a particular patient from a particular source and also the first and the last date it was recorded from any source.

## Metadata

| Property | Value |
| --- | --- |
| Type | Derived Table |
| Load Frequency | INCREMENTAL |
| Release Version | Rel August 2020 |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| DX_ID | NUMERIC (18,0) | The unique ID of the diagnosis record (EDG .1) associated with the patient. |
| PAT_ID | VARCHAR (18) | The unique ID assigned to the patient record (EPT .1). This ID may be encrypted if you have elected to use enterprise reporting?s security utility. |
| UPDATE_DATE | No | The date and time when this row was created or last updated in Clarity. |
| NUM_ENC_DX | No | The number of times this diagnosis appeared on the patient's encounter diagnosis list. |
| LAST_DATE_ENC_DX | No | The last date on which this diagnosis appeared on the patient's encounter diagnosis list. |
| FIRST_DATE_ENC_DX | No | The first date on which this diagnosis appeared on the patient's encounter diagnosis list. |
| NUM_PROBLEM_LIST | No | The number of times this diagnosis appeared on the patient's problem list. |
| LAST_DATE_PROB_LIST | No | The last date on which this diagnosis appeared on the patient's problem list. |
| FIRST_DATE_PROB_LIST | No | The first date on which this diagnosis appeared on the patient's problem list. |
| NUM_HSP_ACT_DX | No | The number of times this diagnosis appeared on the patient's hospital account. |
| LAST_DT_HSP_ACT_DX | No | The last date on which this diagnosis appeared on the patient's hospital account. |
| FIRST_DT_HSP_ACT_DX | No | The first date on which this diagnosis appeared on the patient's hospital account. |
| NUM_HSP_ADM_DX | No | The number of times this diagnosis appeared on the patient's hospital admission diagnosis list. |
| LAST_DT_HSP_ADM_DX | No | The last date on which this diagnosis appeared on the patient's hospital admission list. |
| FIRST_DT_HSP_ADM_DX | No | The first date on which this diagnosis appeared on the patient's hospital admission list. |
| NUM_INV_DX | No | The number of times this diagnosis appeared on a professional claim for the patient. |
| LAST_DATE_INV_DX | No | The last date on which this diagnosis appeared on a professional claim for the patient. |
| FIRST_DATE_INV_DX | No | The first date on which this diagnosis appeared on a professional claim for the patient. |
| NUM_CLM_DX | No | The number of times this diagnosis appeared on the patient's hospital claim. |
| LAST_DATE_CLM_DX | No | The last date on which this diagnosis appeared on the patient's hospital claim. |
| FIRST_DATE_CLM_DX | No | The first date on which this diagnosis appeared on the patient's hospital claim. |
| NUM_OR_CASE_DX | No | The number of times this diagnosis appeared on the patient's surgical case. |
| LAST_DT_OR_CASE_DX | No | The last date on which this diagnosis appeared on the patient's surgical case. |
| FIRST_DT_OR_CASE_DX | No | The first date on which this diagnosis appeared on the patient's surgical case. |
| LAST_DATE | No | The last date on which this diagnosis was recorded, from any source. |
| FIRST_DATE | No | The first date on which this diagnosis was recorded, from any source. |
| NUM_MED_HIST_DX | No | The number of times this diagnosis appeared on the patient's medical history. |
| LAST_DT_MED_HIST_DX | No | The last date on which this diagnosis appeared on the patient's medical history . |
| FIRST_DT_MED_HIST_DX | No | The first date on which this diagnosis appeared on the patient's medical history . |
| NUM_HSP_ACT_EXTINJ | No | The number of times this diagnosis appeared on the patient's hospital account as an external injury. |
| LAST_DT_HSP_ACT_EXTINJ | No | The last date on which this diagnosis appeared on the patient's hospital account as an external injury. |
| FIRST_DT_HSP_ACT_EXTINJ | No | The first date on which this diagnosis appeared on the patient's hospital account as an external injury. |
| NUM_REF_DX | No | The number of times this diagnosis appeared on referrals related to the patient. |
| LAST_DATE_REF_DX | No | The last date on which this diagnosis appeared on a referral related to the patient. This comes from the entry date of the referral. |
| FIRST_DATE_REF_DX | No | The first date on which this diagnosis appeared on a referral related to the patient. This comes from the entry date of the referral. |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | DX_ID | ADVERSE_EVENT_TERM_INFO | DX_ID | No | Unknown | No |  |
| 1 | DX_ID | CLARITY_EDG | DX_ID | Unknown | Unknown | No |  |
| 1 | DX_ID | EDG_DBC_INFO | DX_ID | No | Unknown | No |  |
| 1 | DX_ID | V_CUBE_D_DIAGNOSIS | DIAGNOSIS_ID | Unknown | Unknown | No |  |
| 2 | PAT_ID | ANTICOAG_SELF_REGULATING | PAT_ID | No | Unknown | No |  |
| 2 | PAT_ID | CARE_COORDINATION | PAT_ID | Unknown | Unknown | No |  |
| 2 | PAT_ID | CLAIMS_DERIVE_PAT_FLAGS | PAT_ID | No | Unknown | No |  |
| 2 | PAT_ID | COMMUNITY_RESRC_REVIEWED | PAT_ID | No | Unknown | No |  |
| 2 | PAT_ID | D_PAT_GEOGRAPHIC_CLASS | PAT_ID | Unknown | Unknown | No |  |
| 2 | PAT_ID | EPT_MEM_INFO | PAT_ID | No | Unknown | No |  |
| 2 | PAT_ID | EXT_DATA_LAST_DONE | PAT_ID | No | Unknown | No |  |
| 2 | PAT_ID | F_IBD_ADULT_FORM_PAT | PAT_ID | Unknown | Unknown | No |  |
| 2 | PAT_ID | HH_PAT_INFO | PAT_ID | Unknown | Unknown | No |  |
| 2 | PAT_ID | HM_STATUS_UPD | PAT_ID | No | Unknown | No |  |
| 2 | PAT_ID | IMMNZTN_LAST_REVIEW | PAT_ID | No | Unknown | No |  |
| 2 | PAT_ID | PATIENT | PAT_ID | No | Unknown | No |  |
| 2 | PAT_ID | PATIENT_2 | PAT_ID | No | Unknown | No |  |
| 2 | PAT_ID | PATIENT_3 | PAT_ID | No | Unknown | No |  |
| 2 | PAT_ID | PATIENT_4 | PAT_ID | No | Unknown | No |  |
| 2 | PAT_ID | PATIENT_5 | PAT_ID | No | Unknown | No |  |
| 2 | PAT_ID | PATIENT_6 | PAT_ID | No | Unknown | No |  |
| 2 | PAT_ID | PATIENT_CONF_ADDR | PAT_ID | No | Unknown | No |  |
| 2 | PAT_ID | PATIENT_MISC_COMMENTS | PAT_ID | No | Unknown | No |  |
| 2 | PAT_ID | PATIENT_MYC | PAT_ID | Unknown | Unknown | No |  |
| 2 | PAT_ID | PATIENT_OPT | PAT_ID | No | Unknown | No |  |
| 2 | PAT_ID | PAT_ENC_LAST_HX_CT | PAT_ID | Unknown | Unknown | No |  |
| 2 | PAT_ID | PAT_RES_CODE | PAT_ID | No | Unknown | No |  |
| 2 | PAT_ID | PROB_LIST_REVIEWED | PAT_ID | No | Unknown | No |  |
| 2 | PAT_ID | REGADDL_PAT | PAT_ID | No | Unknown | No |  |
| 2 | PAT_ID | SCF_FHIR_MAP | PAT_ID | No | Unknown | No |  |

_(36 total; showing first 30)_
