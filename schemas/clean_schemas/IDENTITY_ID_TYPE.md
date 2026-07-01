# IDENTITY_ID_TYPE

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=IDENTITY_ID_TYPE

## Description

The IDENTITY_ID_TYPE table contains the list of ID Types in your system.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | IIT |
| Release Version | EPIC 2002 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| ID_TYPE | NUMERIC (18,0) | The master person index ID Type. |
| ID_TYPE_NAME | VARCHAR (200) | The name of the ID Type. |
| CM_PHY_OWNER_ID | VARCHAR (25) | ID of the physical deployment owner for this record.  Physical owners will be where the data is hosted, either on the cross-over server or the owner deployment. |
| CM_LOG_OWNER_ID | VARCHAR (25) | ID of the logical deployment owner for this record.  Logical owners show the deployment where the record was created but doesn't represent if the record is a part of version skew. |
| RECORD_STATUS_C | INTEGER |  |
| ID_INI_C | VARCHAR (66) |  |
| ABBR | VARCHAR (192) | The abbreviation for the ID type. |
| ID_NUM_RULES_C | INTEGER |  |
| MACHINE_RULES_C | INTEGER |  |
| MACHINE_START_NUM | NUMERIC (18,0) | If system generated ID numbers are being used, and the system generation method is set to "Start generating from a pre-set number", this item determines the starting ID number. A simple "one-up" algorithm is used to obtain the next free ID. |
| USER_ID_FORMAT_C | INTEGER |  |
| USER_ID_LENGTH | INTEGER | If user entered ID numbers are being used, and the ID format is either numeric or alphanumeric, this item specifies the ID length. If null, no length checking is done. |
| VERIFY_FORMAT_MSG | VARCHAR (254) | A short message to the user explaining the expected format. |
| FORMAT_PROMPT_MSG | VARCHAR (254) | A short message to prompt the user, explaining the required format of the permanent ID. |
| ALLOW_MULT_IDS_YN | VARCHAR (1) |  |
| CRT_ID_DFLT_PRT_YN | VARCHAR (1) |  |
| USE_EFF_DATES_YN | VARCHAR (1) |  |
| ID_TYPE_DESCRIPTOR | VARCHAR (192) | Enter the descriptor for this ID type. |
| CCOW_IDENTIFIER | VARCHAR (192) | This column holds the CCOW Full Identifier, which is created by adding the string in the CCOW extension to "patient.id.mrn." The CCOW Full Identifier functions as an alias for referencing this ID type within a shared context. |
| CCOW_MRN_YN | VARCHAR (1) |  |
| CCOW_EXTENSION | VARCHAR (254) | The CCOW extension in this column is the suffix of the patient ID context key. It is used to share patient IDs across separate applications. This item is free-text. |
| ALLOW_VIEW_YN | VARCHAR (1) |  |
| ALLOW_DUP_IDS_YN | VARCHAR (1) |  |
| DOWNTIME_MODE_YN | VARCHAR (1) |  |
| CONVERT_UPPERCAS_YN | VARCHAR (1) |  |
| RESERVE_ON_EMPI_C | INTEGER |  |
| USE_TEMP_ID_RULE_YN | VARCHAR (1) |  |
| TEMP_ID_BYPASS_YN | VARCHAR (1) |  |
| CHART_LOC_REQD_YN | VARCHAR (1) |  |
| TEMP_ID_NUM_RULES_C | INTEGER |  |
| TEMP_MACH_RULES_C | INTEGER |  |
| TEMP_MACH_START_NUM | INTEGER | If system generated ID numbers are being used, and the system generation method is set to "Start generating from a pre-set number", this item determines the starting ID number. |
| TEMP_USER_ID_FMT_C | INTEGER |  |
| TEMP_USER_ID_LENGTH | INTEGER | If user entered ID numbers are being used, and the ID format is either numeric or alphanumeric, this item specifies the ID length. |
| TEMP_VER_ERR_TEXT | VARCHAR (254) | A short message to the user explaining the expected format. |
| TEMP_PROMPT_MSG | VARCHAR (254) | A short message to prompt the user, explaining the required format of the temporary ID. |
| TEMP_START_TEMP_ID | INTEGER | The starting ID number for temporary IDs for this ID type. |
| HL7_ASSIGN_AUTH | VARCHAR (91) | The HL7 2.X assigning authority for this Epic ID Type. |
| HL7_ID_TYPE | VARCHAR (91) | The HL7 2.X ID type for this Epic ID Type. |
| HL7_CODING_SYSTEM | VARCHAR (192) | The HL7 2.X coding system for this Epic ID Type. |
| PASSPORT_COUNTRY_C | VARCHAR (66) |  |
| UNOS_DNR_ID_TYPE_YN | VARCHAR (1) |  |
| UNOS_RCP_ID_TYPE_YN | VARCHAR (1) |  |
| HL7_ID_TYPE_VERSION | VARCHAR (64) | Version of ID Type for sending/matching with external systems |
| PREVENT_HX_REUSE_YN | VARCHAR (1) |  |
| ALLOW_LEAD_SPACES_YN | VARCHAR (1) | Surrogate key used to uniquely identify rows in this (and only this) table on Cogito Cloud only, do not assume the surrogate key in this table will correspond to the surrogate key in another table |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ID_TYPE | V_ZZLOV_DRG_TYPES | DRG_ID_TYPE_ID | Unknown | Unknown | No |  |
| 3 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 4 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 4 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 4 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 5 | RECORD_STATUS_C | ZC_DEL_STATUS | DEL_STATUS_C | No | No | No |  |
| 5 | RECORD_STATUS_C | ZC_EDG_REC_STAT | EDG_REC_STAT_C | No | No | No |  |
| 5 | RECORD_STATUS_C | ZC_ERS_REC_STAT | RECORD_STATUS_C | No | No | No |  |
| 5 | RECORD_STATUS_C | ZC_HCD_REC_STATE | HCD_REC_STATE_C | No | No | No |  |
| 5 | RECORD_STATUS_C | ZC_HFL_RECORD_STAT | HFL_RECORD_STAT_C | No | No | No |  |
| 5 | RECORD_STATUS_C | ZC_IMM_REC_STATUS | IMM_REC_STATUS_C | No | No | No |  |
| 5 | RECORD_STATUS_C | ZC_LLB_STATUS | LLB_STATUS_C | No | No | No |  |
| 5 | RECORD_STATUS_C | ZC_LMA_RECORD_STAT | LMA_RECORD_STAT_C | No | No | No |  |
| 5 | RECORD_STATUS_C | ZC_MEM_REC_STATUS | MEM_REC_STATUS_C | No | No | No |  |
| 5 | RECORD_STATUS_C | ZC_OR_REC_STATUS | OR_REC_STATUS_C | No | No | No |  |
| 5 | RECORD_STATUS_C | ZC_PBA_REC_STAT | PBA_REC_STAT_C | No | No | No |  |
| 5 | RECORD_STATUS_C | ZC_PROV_REC_STATE | PROV_REC_STATE_C | No | No | No |  |
| 5 | RECORD_STATUS_C | ZC_RECORD_STATE_2 | RECORD_STATE_2_C | No | No | No |  |
| 5 | RECORD_STATUS_C | ZC_RECORD_STATE_3 | RECORD_STATE_3_C | No | No | No |  |
| 5 | RECORD_STATUS_C | ZC_RECORD_STATE_4 | RECORD_STATE_4_C | No | No | No |  |
| 5 | RECORD_STATUS_C | ZC_RECORD_STATE_6 | RECORD_STATE_6_C | No | No | No |  |
| 5 | RECORD_STATUS_C | ZC_RECORD_STATE_7 | RECORD_STATE_7_C | No | No | No |  |
| 5 | RECORD_STATUS_C | ZC_RECORD_STAT_EPM | RECORD_STAT_EPM_C | No | No | No |  |
| 5 | RECORD_STATUS_C | ZC_RECORD_STAT_EPP | RECORD_STAT_EPP_C | No | No | No |  |
| 5 | RECORD_STATUS_C | ZC_RECORD_STAT_ETX | RECORD_STAT_ETX_C | No | No | No |  |
| 5 | RECORD_STATUS_C | ZC_RECORD_STAT_HRV | RECORD_STAT_HRV_C | No | No | No |  |
| 5 | RECORD_STATUS_C | ZC_RECORD_STAT_RMC | RECORD_STAT_RMC_C | No | No | No |  |
| 6 | ID_INI_C | ZC_ID_INI | ID_INI_C | No | No | No |  |

_(40 total; showing first 30)_
