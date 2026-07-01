# TREATMENT_TEAM

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=TREATMENT_TEAM

## Description

This table stores information about patient treatment teams such as relationship, specialty, department, and start/end time. Each row represents a member of a patient's treatment team.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | EPT |
| Release Version | Summer 2009 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| PAT_ENC_CSN_ID | NUMERIC (18,0) | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| LINE | No | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| PAT_ID | VARCHAR (18) | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| PAT_ENC_DATE_REAL | No | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| CONTACT_DATE | DATETIME | The date of this contact in calendar format. |
| CM_CT_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this contact. This is only populated if you use IntraConnect. |
| TR_TEAM_BILL_PR_ID | VARCHAR (18) | The unique ID of the billing provider record. |
| TR_TEAM_EM_CODE_ID | NUMERIC (18,0) | The evaluation and management code for billing within the treatment team. |
| TR_TEAM_EM_REQ_C | INTEGER |  |
| TR_TEAM_SPEC_C | VARCHAR (66) |  |
| TR_TEAM_COMMENT | VARCHAR (1024) | The comment for the treatment team. |
| TR_TEAM_ISDE_YN | VARCHAR (1) |  |
| TR_TEAM_BILL_YN | VARCHAR (1) |  |
| TR_TEAM_ID | VARCHAR (18) | The unique ID of the treatment team provider record. |
| TR_TEAM_REL_C | VARCHAR (66) |  |
| TR_TEAM_COMM_C | INTEGER |  |
| TR_TEAM_INFO_C | VARCHAR (66) |  |
| TR_TEAM_DEP_ID | NUMERIC (18,0) | The department of treatment team members. |
| TR_TEAM_BEG_DTTM | DATETIME (Local) | The date and time the treatment team member started for the patient. |
| TR_TEAM_END_DTTM | DATETIME (Local) | The date and time the treatment team member ended for the patient. |
| TR_TEAM_POS_ID | NUMERIC (18,0) | The place of service for treatment team members. |
| TR_TEAM_ED_YN | VARCHAR (1) |  |
| TR_TEAM_TEAM_ADD_YN | VARCHAR (1) |  |
| TR_TEAM_ADDR_ID | VARCHAR (40) | Stores the address unique ID for the Treatment Team members. The value here matches up with one of the provider's address identifiers (SER item 21000). |
| TR_TEAM_SRC_CSN_ID | NUMERIC (18,0) | This item stores the contact serial number corresponding to the encounter responsible for assigning a specific member of the treatment team. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| B-TREE INDEX | EIX_TREATMENT_TEAM_CONTACT | PAT_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_TREATMENT_TEAM_CONTACT | PAT_ENC_DATE_REAL | 2 | Yes | Yes |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | PAT_ENC_CSN_ID | ALT_ORD_PROV_SINGL | PAT_ENC_CSN_ID | Unknown | No | No |  |
| 1 | PAT_ENC_CSN_ID | AN_RELINK_INFO | PAT_ENC_CSN_ID | No | No | No |  |
| 1 | PAT_ENC_CSN_ID | DENT_ORTH_EXAM_NOTES | PAT_ENC_CSN_ID | No | No | No |  |
| 1 | PAT_ENC_CSN_ID | FAC_CHG_OVERRIDE | PAT_ENC_CSN_ID | No | No | No |  |
| 1 | PAT_ENC_CSN_ID | FAM_HX_PAT_ONLY | PAT_ENC_CSN_ID | No | No | No |  |
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

_(365 total; showing first 30)_
