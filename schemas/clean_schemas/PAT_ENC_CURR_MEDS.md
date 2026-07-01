# PAT_ENC_CURR_MEDS

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=PAT_ENC_CURR_MEDS

## Description

The PAT_ENC_CURR_MEDS table enables you to report on current (as well as active) medications per encounter as listed in clinical system.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | EPT |
| Release Version | MU13 - MAY 2001 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| PAT_ID | VARCHAR (18) | The unique ID assigned to the patient record. This ID may be encrypted if you have elected to use enterprise reporting?s encryption utility. |
| PAT_ENC_DATE_REAL | No | This is a numeric representation of the date of this encounter in your system. The integer portion of the number specifies the date of the encounter. The digits after the decimal point indicate multiple visits on one day. |
| LINE | No | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| PAT_ENC_CSN_ID | NUMERIC (18,0) | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| CONTACT_DATE | DATETIME | The date of this contact in calendar format. |
| CURRENT_MED_ID | NUMERIC (18,0) | The current medication order ID for the encounter. |
| IS_ACTIVE_YN | VARCHAR (1) |  |
| UPDATE_DATE | No | The date and time of the extract in calendar format. NOTE: Uses the EPIC_GET_DATETIME to return the time and date that this record was extracted. |
| MEDICATION_ID *(deprecated)* | NUMERIC (18,0) |  |
| CM_CT_OWNER_ID | VARCHAR (25) | ID of the deployment owner for this contact. |
| ADD_TO_LIST_TM | DATETIME (Local) | The time that this medication is added to the encounter medication list from other encounters. |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| B-TREE INDEX | EIX_PAT_ENC_CURR_MEDSENC | PAT_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_PAT_ENC_CURR_MEDSENC | PAT_ENC_DATE_REAL | 2 | Yes | Yes |  |
| B-TREE INDEX | EIX_PAT_ENC_CURR_MEDS_CODA | CONTACT_DATE | 1 | Yes | Yes |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | PAT_ID | ANTICOAG_SELF_REGULATING | PAT_ID | No | No | No |  |
| 1 | PAT_ID | CARE_COORDINATION | PAT_ID | Unknown | No | No |  |
| 1 | PAT_ID | CLAIMS_DERIVE_PAT_FLAGS | PAT_ID | No | No | No |  |
| 1 | PAT_ID | COMMUNITY_RESRC_REVIEWED | PAT_ID | No | No | No |  |
| 1 | PAT_ID | D_PAT_GEOGRAPHIC_CLASS | PAT_ID | Unknown | Unknown | No |  |
| 1 | PAT_ID | EPT_MEM_INFO | PAT_ID | No | No | No |  |
| 1 | PAT_ID | EXT_DATA_LAST_DONE | PAT_ID | No | No | No |  |
| 1 | PAT_ID | F_IBD_ADULT_FORM_PAT | PAT_ID | Unknown | Unknown | No |  |
| 1 | PAT_ID | HH_PAT_INFO | PAT_ID | Unknown | No | No |  |
| 1 | PAT_ID | HM_STATUS_UPD | PAT_ID | No | No | No |  |
| 1 | PAT_ID | IMMNZTN_LAST_REVIEW | PAT_ID | No | No | No |  |
| 1 | PAT_ID | PATIENT | PAT_ID | No | No | No |  |
| 1 | PAT_ID | PATIENT_2 | PAT_ID | No | No | No |  |
| 1 | PAT_ID | PATIENT_3 | PAT_ID | No | No | No |  |
| 1 | PAT_ID | PATIENT_4 | PAT_ID | No | No | No |  |
| 1 | PAT_ID | PATIENT_5 | PAT_ID | No | No | No |  |
| 1 | PAT_ID | PATIENT_6 | PAT_ID | No | No | No |  |
| 1 | PAT_ID | PATIENT_CONF_ADDR | PAT_ID | No | No | No |  |
| 1 | PAT_ID | PATIENT_MISC_COMMENTS | PAT_ID | No | No | No |  |
| 1 | PAT_ID | PATIENT_MYC | PAT_ID | Unknown | No | No |  |
| 1 | PAT_ID | PATIENT_OPT | PAT_ID | No | No | No |  |
| 1 | PAT_ID | PAT_ENC_LAST_HX_CT | PAT_ID | Unknown | Unknown | No |  |
| 1 | PAT_ID | PAT_RES_CODE | PAT_ID | No | No | No |  |
| 1 | PAT_ID | PROB_LIST_REVIEWED | PAT_ID | No | No | No |  |
| 1 | PAT_ID | REGADDL_PAT | PAT_ID | No | No | No |  |
| 1 | PAT_ID | SCF_FHIR_MAP | PAT_ID | No | No | No |  |
| 1 | PAT_ID | TEETH_REVIEWED | PAT_ID | No | No | No |  |
| 1 | PAT_ID | VALID_PATIENT | PAT_ID | No | No | No |  |
| 1 | PAT_ID | V_PAT_ABO | PAT_ID | Unknown | Unknown | No |  |
| 1 | PAT_ID | V_PAT_FACT | PAT_ID | Unknown | Unknown | No |  |

_(227 total; showing first 30)_
