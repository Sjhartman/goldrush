# IP_DATA_STORE

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=IP_DATA_STORE

## Description

This table contains generic information related to a patient's inpatient stay, including data on patient education, notes, and other topics.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | INP |
| Release Version | EPIC 2002 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| INPATIENT_DATA_ID | VARCHAR (18) | The unique ID of the inpatient data store record. |
| RECORD_STATUS_NAME *(deprecated)* | VARCHAR (50) |  |
| PAT_ID *(deprecated)* | VARCHAR (18) | The unique ID of the patient associated with this INP record. This column has been deprecated because it may not be updated when patient merges happen. To look up the deprecated columns' value after the Clarity Compass upgrade, join column IP_DATA_STORE.EPT_CSN to PAT_ENC_HSP. PAT_ENC_CSN_ID and get the PAT_ID value. |
| TEMPLATE_ID | VARCHAR (18) | The unique ID of the flowsheet template. |
| DISCH_INST_HNO_ID | VARCHAR (254) | The HNO ID of the patient's discharge instructions, for discharge instructions created in version Epic Aug 2021 or prior. In version Epic Nov 2021 and later, the discharge instruction information that was previously stored in INP will now be stored in HNO for Note Type 18-Discharge Instructions, with information about instances where discharge instructions were reviewed, updated, or signed extracted in the Clarity table DISCH_INSTR_HISTORY. |
| EDU_STATUS_NM *(deprecated)* | VARCHAR (50) |  |
| EDU_NOBARRIER_C *(deprecated)* | INTEGER |  |
| EDU_SPOKEN *(deprecated)* | VARCHAR (255) | The languages spoken by the patient. This column is no longer populated as all of the Patient Education data is now stored in the PED masterfile.  Please use the PED-based tables (such as CL_PAT_EDU) instead. |
| EDU_EMOTIONAL *(deprecated)* | INTEGER | The stress scale (1-10) as related by the patient.  This column is no longer populated as all of the Patient Education data is now stored in the PED masterfile.  Please use the PED-based tables (such as CL_PAT_EDU) instead. |
| EDU_NEEDS *(deprecated)* | VARCHAR (80) | Other educational needs for the patient. This column is no longer populated as all of the Patient Education data is now stored in the PED masterfile.  Please use the PED-based tables (such as CL_PAT_EDU) instead. |
| EDU_ANSWERED_BY *(deprecated)* | VARCHAR (50) | The person who provided information for educational assessment. This column is no longer populated as all of the Patient Education data is now stored in the PED masterfile.  Please use the PED-based tables (such as CL_PAT_EDU) instead. |
| EDU_RELATION_C *(deprecated)* | INTEGER |  |
| EDU_RECEIVED_BY *(deprecated)* | VARCHAR (50) | The person who received the information from the patient. This column is no longer populated as all of the Patient Education data is now stored in the PED masterfile.  Please use the PED-based tables (such as CL_PAT_EDU) instead. |
| EDU_DATE *(deprecated)* | DATETIME | The date of the patient's education assessment. This column is no longer populated as all of the Patient Education data is now stored in the PED masterfile.  Please use the PED-based tables (such as CL_PAT_EDU) instead. |
| CM_PHY_OWNER_ID | VARCHAR (25) | ID of the physical deployment owner for this record.  Physical owners will be where the data is hosted, either on the cross-over server or the owner deployment. |
| CM_LOG_OWNER_ID | VARCHAR (25) | ID of the logical deployment owner for this record.  Logical owners show the deployment where the record was created but doesn't represent if the record is a part of version skew. |
| RECORD_STATUS_C | INTEGER |  |
| EPT_CSN | NUMERIC (18,0) | Link to Contact Serial Number in EPT for associated encounter. |
| BRST_STAT_INST_TM | DATETIME (Local) | Stores the last instant that Breastfeeding Status was saved. |
| PAIN_EDU_INST_TM | DATETIME (Local) | Stores the last instant the Pain Education was saved. |
| HC_INSTANT_TM | DATETIME (Local) | Stores the last instant that the Head Circumference was saved. |
| PF_INSTANT_TM | DATETIME (Local) | Stores the last instant that Peak Flow was saved. |
| EXINGC_INSTANT_TM | DATETIME (Local) | Stores the last instant that Exclude in Growth Charts information was saved. |
| ALT_PRINT_INST_TM | DATETIME (Local) | Stores the last instant OurPractice Advisory (OPA) alert information was saved. |
| AK_CONVERTED_YN | VARCHAR (1) |  |
| IP_NOTE_MOD_INST_TM | DATETIME (UTC) | The time the Notes were last modified for this Inpatient Data record. |
| REC_ARCHIVED_YN | No | Indicates whether the Inpatient Data Store record is archived at the record level. |
| UPDATE_DATE | No | The date and time this row was last updated (the last time it was extracted or this column was backfilled). |
| PRIME_SINGLE_COLUMN_DTTM | DATETIME (Local) | Timestamp where all single column flowsheet data for the linked primary encounter is stored |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| B-TREE INDEX | EIX_EPT_CSN | EPT_CSN | 1 | Yes | Yes |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 4 | TEMPLATE_ID | IP_FLT_DATA | TEMPLATE_ID | No | No | No |  |
| 5 | DISCH_INST_HNO_ID | ABN_NOTES | ABN_NOTE_ID | Unknown | No | No |  |
| 5 | DISCH_INST_HNO_ID | ABN_NOTE_INFO | NOTE_ID | No | No | No |  |
| 5 | DISCH_INST_HNO_ID | CODING_CLA_NOTES | NOTE_ID | Unknown | No | No |  |
| 5 | DISCH_INST_HNO_ID | FA_NOTES_QUERY | NOTE_ID | No | No | No |  |
| 5 | DISCH_INST_HNO_ID | FIN_ASST_LETTER | NOTE_ID | No | No | No |  |
| 5 | DISCH_INST_HNO_ID | FIN_ASST_NOTE | NOTE_ID | No | No | No |  |
| 5 | DISCH_INST_HNO_ID | HNO_CVG_REQUEST | NOTE_ID | Unknown | No | No |  |
| 5 | DISCH_INST_HNO_ID | HNO_INFO | NOTE_ID | No | No | No |  |
| 5 | DISCH_INST_HNO_ID | HNO_INFO_2 | NOTE_ID | No | No | No |  |
| 5 | DISCH_INST_HNO_ID | HNO_MYC_LET_INFO | NOTE_ID | No | No | No |  |
| 5 | DISCH_INST_HNO_ID | HSP_ACCT_LETTERS | NOTE_ID | Unknown | No | No |  |
| 5 | DISCH_INST_HNO_ID | HSP_ACCT_NOTES | NOTE_ID | Unknown | No | No |  |
| 5 | DISCH_INST_HNO_ID | LETTER_EXTERNAL_INFO | NOTE_ID | No | No | No |  |
| 5 | DISCH_INST_HNO_ID | NOTES_ACCT | NOTE_ID | Unknown | No | No |  |
| 5 | DISCH_INST_HNO_ID | NOTES_LAB | NOTE_ID | Unknown | No | No |  |
| 5 | DISCH_INST_HNO_ID | NOTES_MC_CLM | NOTE_ID | Unknown | Unknown | No |  |
| 5 | DISCH_INST_HNO_ID | NOTES_MC_PBA | NOTE_ID | No | No | No |  |
| 5 | DISCH_INST_HNO_ID | NOTES_MC_SER | NOTE_ID | Unknown | Unknown | No |  |
| 5 | DISCH_INST_HNO_ID | NOTE_PARENT_NOTE | NOTE_ID | No | No | No |  |
| 5 | DISCH_INST_HNO_ID | PATIENT_FYI_FLAGS | NOTE_ID | Unknown | No | No |  |
| 5 | DISCH_INST_HNO_ID | REG_HX_NOTES | NOTE_ID | Unknown | No | No |  |
| 5 | DISCH_INST_HNO_ID | SAVED_LETTER_HNO | NOTE_ID | Unknown | No | No |  |
| 5 | DISCH_INST_HNO_ID | V_EHI_PBA_NOTES_MC_PBA | NOTE_ID | Unknown | Unknown | No |  |
| 5 | DISCH_INST_HNO_ID | V_NOTE_CHARACTERISTICS | NOTE_ID | Unknown | Unknown | No |  |
| 5 | DISCH_INST_HNO_ID | V_NOTE_SHARE_W_PAT_INFO | NOTE_ID | Unknown | Unknown | No |  |
| 5 | DISCH_INST_HNO_ID | V_NOTE_VIEW_INFO | NOTE_ID | Unknown | Unknown | No |  |
| 15 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 15 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 15 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |

_(153 total; showing first 30)_
