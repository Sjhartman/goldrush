# TPL_UPDATE_INFO

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=TPL_UPDATE_INFO

## Description

The update information for the treatment plan.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | TPL |
| Release Version | SPRING 2008 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| TREATMENT_PLAN_ID | NUMERIC (18,0) | The treatment plan ID. |
| LINE | No | The line number that corresponds to each update of the treatment plan in this row. |
| CM_PHY_OWNER_ID | VARCHAR (25) | ID of the physical deployment owner for this record.  Physical owners will be where the data is hosted, either on the cross-over server or the owner deployment. |
| CM_LOG_OWNER_ID | VARCHAR (25) | ID of the logical deployment owner for this record.  Logical owners show the deployment where the record was created but doesn't represent if the record is a part of version skew. |
| UPDATED_BY_USER_ID | VARCHAR (18) | The user ID of the person who performed an update of the treatment plan in this row. |
| UPDATED_ON_TM | DATETIME (Local) | The date/time in external format of an update to the treatment plan in this row. |
| UPDATED_IN_PAT_ENC_CSN_ID | NUMERIC (18,0) | Stores the contact serial number (CSN) of a patient visit in which this plan was updated and saved. This item is empty if the update occurred outside of an encounter context. |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | TREATMENT_PLAN_ID | DENT_TREATMENT | TREATMENT_ID | No | No | No |  |
| 1 | TREATMENT_PLAN_ID | TPL_HSB_EPT_LINK | TREATMENT_PLAN_ID | Unknown | No | No |  |
| 1 | TREATMENT_PLAN_ID | TPL_INFO | TREATMENT_PLAN_ID | No | No | No |  |
| 3 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 4 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 4 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 4 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 5 | UPDATED_BY_USER_ID | CLARITY_EMP | USER_ID | Unknown | No | No |  |
| 5 | UPDATED_BY_USER_ID | CLARITY_EMP_2 | USER_ID | Unknown | No | No |  |
| 5 | UPDATED_BY_USER_ID | CLARITY_EMP_3 | USER_ID | Unknown | No | No |  |
| 5 | UPDATED_BY_USER_ID | CLARITY_EMP_4 | USER_ID | No | No | No |  |
| 5 | UPDATED_BY_USER_ID | CLARITY_EMP_DEMO | USER_ID | No | No | No |  |
| 5 | UPDATED_BY_USER_ID | EMP_BASIC_INFO | USER_ID | No | No | No |  |
| 5 | UPDATED_BY_USER_ID | EMP_DOC_SETTINGS | USER_NUMBER_ID | No | No | No |  |
| 5 | UPDATED_BY_USER_ID | F_RX_USER | USER_ID | Unknown | Unknown | No |  |
| 5 | UPDATED_BY_USER_ID | IB_MESSAGE_SETTINGS | USER_ID | No | No | No |  |
| 5 | UPDATED_BY_USER_ID | LOGIN_INFO | USER_NUMBER_ID | No | No | No |  |
| 5 | UPDATED_BY_USER_ID | QC_RESULTS_REVIEW | USER_NUMBER_ID | No | No | No |  |
| 5 | UPDATED_BY_USER_ID | USER_SIDEBAR_RPT | USER_NUMBER_ID | Unknown | No | No |  |
| 5 | UPDATED_BY_USER_ID | V_CUBE_D_USER | USER_ID | Unknown | Unknown | No |  |
| 5 | UPDATED_BY_USER_ID | V_CUBE_RX_USER | USER_ID | Unknown | Unknown | No |  |
| 7 | UPDATED_IN_PAT_ENC_CSN_ID | ALT_ORD_PROV_SINGL | PAT_ENC_CSN_ID | Unknown | No | No |  |
| 7 | UPDATED_IN_PAT_ENC_CSN_ID | AN_RELINK_INFO | PAT_ENC_CSN_ID | No | No | No |  |
| 7 | UPDATED_IN_PAT_ENC_CSN_ID | DENT_ORTH_EXAM_NOTES | PAT_ENC_CSN_ID | No | No | No |  |
| 7 | UPDATED_IN_PAT_ENC_CSN_ID | FAC_CHG_OVERRIDE | PAT_ENC_CSN_ID | No | No | No |  |
| 7 | UPDATED_IN_PAT_ENC_CSN_ID | FAM_HX_PAT_ONLY | PAT_ENC_CSN_ID | No | No | No |  |
| 7 | UPDATED_IN_PAT_ENC_CSN_ID | F_ED_ENCOUNTERS | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 7 | UPDATED_IN_PAT_ENC_CSN_ID | F_HH_CERT_ATTRIBUTES | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |

_(142 total; showing first 30)_
