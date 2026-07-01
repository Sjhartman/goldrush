# F_PAT_MYCHART_STATUS_HX

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=F_PAT_MYCHART_STATUS_HX

## Description

This table can be used to determine the MyChart status of a patient at a time. This transforms the PAT_MYC_STAT_HX table such that each row in the derived table represents a MyChart status and timeframe the patient was at that MyChart status. If the END_DTTM column is NULL, then the patient is currently at that status. Otherwise, the END_DTTM is column is equal to the the START_DTTM of the next timeframe. Other helper columns can be used to join back to PAT_MYC_STAT_HX in order to determine how and why the status change occured.

## Metadata

| Property | Value |
| --- | --- |
| Type | Derived Table |
| Load Frequency | INCREMENTAL |
| Release Version | Rel 2018 |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| PAT_ID | VARCHAR (18) | The patient associated with the status time range |
| START_DTTM | DATETIME (Local) | The beginning of the time range. This time is in the local time zone. For situations where durations or sorting of time stamps are required, use the UTC equivalent (START_UTC_DTTM). |
| UPDATE_DATE | No | Timestamp indicating when the row was populated |
| END_DTTM | DATETIME (Local) | The end of the time range, NULL if this row is for the current status. This time is in the local time zone. For situations where durations or sorting of time stamps are required, use the UTC equivalent (END_UTC_DTTM). |
| START_DT | No | The beginning of the time range as a calendar date. This date is in the local time zone. For situations where durations or sorting of time stamps are required, use the UTC equivalent (START_UTC_DT). |
| END_DT | No | The end of the time range as a calendar date, NULL if this row is for the current status. This date is in the local time zone. For situations where durations or sorting of time stamps are required, use the UTC equivalent (END_UTC_DT). |
| MYCHART_STATUS_C | INTEGER |  |
| START_LINE | No | The audit trail line from PAT_MYC_STAT_HX associated with the beginning of the time range |
| PREV_MYCHART_STATUS_C | INTEGER |  |
| PREV_START_LINE | No | The audit trail line from PAT_MYC_STAT_HX associated with the beginning of the time range for the prior interval for the patient. Can be used as a foreign key for a self join to the previous row's START_LINE. |
| PENDING_ACTIVATION_HX_LINE | No | For time ranges associated with an active account, the line from PAT_MYC_STAT_HX associated with the pending activation line prior to the activation line. This can be used to associate information about an activation code generation to an activation in order to determine how an account became active. Can be used as a foreign key to PAT_MYC_STAT_HX but should not be used as a foreign key for a self join. |
| CODE_GEN_OR_REUSED_BOOL | No | This column contains 1 if there is an activation code generation or re-use associated with the START_TMSTP and 0 otherwise. A code can be re-used for example, if the patient has an activation code, but receives the code a second time on a subsequent AVS. Counting rows where this column contains 1 shows how many opportunities a patient had to activate. When this column contains 1, MYCHART_STATUS_C will equal 3 - Pending Activation in most cases, except  In the case when codes are generated for active proxy only patients. In this case the value of MYCHART_STATUS_C = 1 - Active because the proxy only account is still considered active. |
| START_UTC_DTTM | DATETIME (UTC) | UTC Equivalent of START_DTTM |
| END_UTC_DTTM | DATETIME (UTC) | UTC Equivalent of END_DTTM |
| START_UTC_DT | No | UTC Equivalent of START_DT |
| END_UTC_DT | No | UTC Equivalent of END_DT |

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

_(36 total; showing first 30)_
