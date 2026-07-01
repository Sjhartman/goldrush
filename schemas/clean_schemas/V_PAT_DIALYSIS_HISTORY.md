# V_PAT_DIALYSIS_HISTORY

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=V_PAT_DIALYSIS_HISTORY

## Description

Stores all dialysis history information. Each row represents a single dialysis entry, including a start/end date and details about the dialysis received during that time.

## Metadata

| Property | Value |
| --- | --- |
| Type | View |
| Release Version | Rel November 2018 |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| PAT_ID | No | The unique identifier (.1 item) of the patient for this dialysis entry. |
| DIALYSIS_CENTER_ID | No | Stores the dialysis center for this entry. |
| DIALYSIS_DEPARTMENT_ID | NUMERIC (18,0) | Stores the department primarily responsible for managing this dialysis entry. |
| DIALYSIS_TYPE_C | No | Stores the type of dialysis, e.g. hemo, acute, etc. |
| DIALYSIS_START_DATE | No | Stores the start date for the dialysis entry. |
| DIALYSIS_END_DATE | No | Stores the end date for the dialysis entry. |
| DIALYSIS_COMMENTS | No | Stores comments for the dialysis entry. |
| EPISODE_ID | NUMERIC (18,0) | The unique identifier (.1 item) of the dialysis episode. Only applies to dialysis entries that have been converted to the nephrology episode framework. |
| HX_CSN_ID | NUMERIC (18,0) | The unique serial number for the dialysis history encounter. Only applies to dialysis entries that have not been converted to the nephrology episode framework. |
| HX_LINE | No | The line number for this entry in the dialysis history encounter. Only applies to dialysis entries that have not been converted to the nephrology episode framework. |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | PAT_ID | ANTICOAG_SELF_REGULATING | PAT_ID | No | Unknown | No |  |
| 1 | PAT_ID | CARE_COORDINATION | PAT_ID | Unknown | Unknown | No |  |
| 1 | PAT_ID | CLAIMS_DERIVE_PAT_FLAGS | PAT_ID | No | Unknown | No |  |
| 1 | PAT_ID | COMMUNITY_RESRC_REVIEWED | PAT_ID | No | Unknown | No |  |
| 1 | PAT_ID | D_PAT_GEOGRAPHIC_CLASS | PAT_ID | Unknown | Unknown | No |  |
| 1 | PAT_ID | EPT_MEM_INFO | PAT_ID | No | Unknown | No |  |
| 1 | PAT_ID | EXT_DATA_LAST_DONE | PAT_ID | No | Unknown | No |  |
| 1 | PAT_ID | F_IBD_ADULT_FORM_PAT | PAT_ID | Unknown | Unknown | No |  |
| 1 | PAT_ID | HH_PAT_INFO | PAT_ID | Unknown | Unknown | No |  |
| 1 | PAT_ID | HM_STATUS_UPD | PAT_ID | No | Unknown | No |  |
| 1 | PAT_ID | IMMNZTN_LAST_REVIEW | PAT_ID | No | Unknown | No |  |
| 1 | PAT_ID | PATIENT | PAT_ID | No | Unknown | No |  |
| 1 | PAT_ID | PATIENT_2 | PAT_ID | No | Unknown | No |  |
| 1 | PAT_ID | PATIENT_3 | PAT_ID | No | Unknown | No |  |
| 1 | PAT_ID | PATIENT_4 | PAT_ID | No | Unknown | No |  |
| 1 | PAT_ID | PATIENT_5 | PAT_ID | No | Unknown | No |  |
| 1 | PAT_ID | PATIENT_6 | PAT_ID | No | Unknown | No |  |
| 1 | PAT_ID | PATIENT_CONF_ADDR | PAT_ID | No | Unknown | No |  |
| 1 | PAT_ID | PATIENT_MISC_COMMENTS | PAT_ID | No | Unknown | No |  |
| 1 | PAT_ID | PATIENT_MYC | PAT_ID | Unknown | Unknown | No |  |
| 1 | PAT_ID | PATIENT_OPT | PAT_ID | No | Unknown | No |  |
| 1 | PAT_ID | PAT_ENC_LAST_HX_CT | PAT_ID | Unknown | Unknown | No |  |
| 1 | PAT_ID | PAT_RES_CODE | PAT_ID | No | Unknown | No |  |
| 1 | PAT_ID | PROB_LIST_REVIEWED | PAT_ID | No | Unknown | No |  |
| 1 | PAT_ID | REGADDL_PAT | PAT_ID | No | Unknown | No |  |
| 1 | PAT_ID | SCF_FHIR_MAP | PAT_ID | No | Unknown | No |  |
| 1 | PAT_ID | TEETH_REVIEWED | PAT_ID | No | Unknown | No |  |
| 1 | PAT_ID | VALID_PATIENT | PAT_ID | No | Unknown | No |  |
| 1 | PAT_ID | V_PAT_ABO | PAT_ID | Unknown | Unknown | No |  |
| 1 | PAT_ID | V_PAT_FACT | PAT_ID | Unknown | Unknown | No |  |

_(234 total; showing first 30)_
