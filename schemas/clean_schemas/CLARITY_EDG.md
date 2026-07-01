# CLARITY_EDG

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=CLARITY_EDG

## Description

The CLARITY_EDG table contains basic information about diagnoses.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | EDG |
| Release Version | EPIC 2000 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| DX_ID | NUMERIC (18,0) | The unique ID of the diagnosis record in your system. |
| DX_NAME | VARCHAR (200) | The name of the diagnosis. |
| DX_STATUS *(deprecated)* | VARCHAR (10) |  |
| DX_GROUP | VARCHAR (200) | The name of the diagnosis group to which the diagnosis belongs. |
| ICD9_CODE *(deprecated)* | VARCHAR (20) | *** Deprecated *** In table CLARITY_EDG, the column ICD9_CODE (EDG 2000) has been deprecated. Refer to the Diagnosis and ICD Procedure Updates section of https://galaxy.epic.com/redirect.aspx?documentid=1577542 to determine the correct column to use. |
| PARENT_DX_ID | No | The parent of the diagnosis as determined by the ICD-9 code. For example, if the ICD code for this diagnosis is V70.7, this value will be the DX_ID of the diagnosis with an ICD code of V70 (of the same code set). Uses the EPIC_DX_PARENT function to calculate this value.  Can use PARENT_DX_ID to link to a second copy of CLARITY_EDG to get information on the parent diagnosis, such as the parent diagnosis name. |
| EC_INACTIVE_YN | VARCHAR (1) |  |
| SPEC_BILLING_YN | VARCHAR (1) |  |
| SHOWN_IN_MYC_YN | VARCHAR (1) |  |
| PAT_FRIENDLY_TEXT | VARCHAR (255) | A description of the diagnosis that is easy for patients to understand. |
| EXTERNAL_ID | VARCHAR (254) | The unique identifier of the diagnosis record. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The physical owner deployment of this record, , used in Community Model record sharing. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The logical owner deployment of this record, used in Community Model record sharing. |
| DX_CODE_TYPE *(deprecated)* | INTEGER |  |
| DX_ICD9_IMO_ID *(deprecated)* | VARCHAR (254) |  |
| ICD9_CODE_NO_ADD *(deprecated)* | VARCHAR (20) | *** Deprecated *** In table CLARITY_EDG, the column ICD9_CODE_NO_ADD (EDG 2001) has been deprecated. Refer to the Diagnosis and ICD Procedure Updates section of https://galaxy.epic.com/redirect.aspx?documentid=1577542 to determine the correct column to use. |
| DX_OTHER_DESC | VARCHAR (254) | This column displays additional information about the diagnosis.  EDG item 200 is a free-text field in the database that can be used for ICD-9 codes or other descriptive information. |
| RECORD_STATE_C | INTEGER |  |
| RECORD_TYPE_C | INTEGER |  |
| REFERENCE_CODE *(deprecated)* | VARCHAR (20) |  |
| HISTORICAL_REF_CODE *(deprecated)* | VARCHAR (20) | *** Deprecated *** In table CLARITY_EDG, the column HISTORICAL_REF_CODE (EDG 2000) has been deprecated. Refer to the Diagnosis and ICD Procedure Updates section of https://galaxy.epic.com/redirect.aspx?documentid=1577542 to determine the correct column to use. |
| DX_IMO_ID | VARCHAR (254) | Stores the IMO id corresponding to the record from the IMO table that was used to create this EDG record. |
| HX_REF_CODE_NO_ADD *(deprecated)* | VARCHAR (20) | *** Deprecated *** In table CLARITY_EDG, the column HX_REF_CODE_NO_ADD (EDG 2001) has been deprecated. Refer to the Diagnosis and ICD Procedure Updates section of https://galaxy.epic.com/redirect.aspx?documentid=1577542 to determine the correct column to use. |
| DIAGNOSIS_CODE | No | *** Deprecated ***  In table CLARITY_EDG, the column DIAGNOSIS_CODE (EDG) has been deprecated. Refer to the Diagnosis and ICD Procedure Updates section of https://galaxy.epic.com/redirect.aspx?documentid=1577542 to determine the correct column to use. |
| DX_CHRONIC_FLAG_YN | VARCHAR (1) |  |
| MCC_FLG_YN | VARCHAR (1) |  |
| CC_FLG_YN | VARCHAR (1) |  |
| HCC_MODEL_CAT | VARCHAR (15) | CMS-HCC Model Category number |
| HCC_COMM_FACT | VARCHAR (15) | HCC community factor |
| HCC_INST_FACT | VARCHAR (15) | HCC institutional factor |
| RXHCC_MODEL_CAT | VARCHAR (15) | RxHCC Model Category |
| RXHCC_REL_FACT | VARCHAR (15) | RxHCC Relative Factor |
| RXHCC_DOL_COEFF | VARCHAR (15) | RxHCC Dollar Coefficient |
| GENERIC_DX_C | INTEGER |  |
| REF_BILL_CODE | 4100 2001 2002 | The reference code of the record. This value is only available for records of type "both" or "code." To determine the record's code set, use REF_BILL_CODE_SET_C. |
| REF_BILL_CODE_SET_C | 4101 |  |
| CURRENT_ICD9_LIST | VARCHAR (254) | For term-type and both-type records, this is the record's current mapped ICD-9-CM codes as a list. Values are separated by a comma and a space. Code-type records of the ICD-9-CM code set will have a value here as well that represents their reference code. |
| CURRENT_ICD10_LIST | 4104 2002 2001 | For term-type and both-type records, this is the record's current mapped ICD-10-CM codes as a list. Values are separated by a comma and a space. Code-type records of the ICD-10-CM code set will have a value here as well that represents their reference code. |
| IMO_TERM_ID | VARCHAR (30) | This stores the entry of the first column in ICDx_LEXICALS_TEXT_IMO table.  Item 3000 stores the entry of the second column in ICDx_IMO table. |
| PREFERRED_TERM_ID | NUMERIC (18,0) | This is a foreign key linking to the preferred clinical term for a code, another EDG record. |
| PAT_FRIENDLY_ID | NUMERIC (18,0) | This points to the term record that should be used as patient friendly term for a code type EDG record. |
| DX_GROUP_ID | VARCHAR (18) | The ID of the diagnosis group to which this diagnosis belongs. |
| PREF_GEN_TERM_ID | NUMERIC (18,0) | The preferred generic term for the specific term in this row. This is used when converting a specific term to a generic term, for example, when moving a specific visit diagnosis to a problem list that only allows generic terms. |
| INSTANT_OF_UPDATE_DTTM | DATETIME (Local) | The instant when the diagnosis record was last locked or unlocked before this row was extracted. Changes to the instant of update do not trigger a Clarity extract, so values in this column may not represent the current value in Chronicles. |
| DX_RISK_DEGREE_C | INTEGER |  |
| DX_RISK_CHRONIC_C | INTEGER |  |
| DX_RISK_TYPE_C | INTEGER |  |
| CUR_MPD_ICPC_DELIM | VARCHAR (254) | Comma-delimited list of this record's current mapped ICPC codes. |
| CUR_MPD_THL_DISPLAY | VARCHAR (254) | Displays ICD-10-THL diagnosis codes with symbols. |
| CUR_MPD_ICDO3_DELIM | VARCHAR (254) | Comma-delimited list of this record's current mapped ICD-O-3 codes. |
| DX_LATERALITY_C | INTEGER |  |
| FULLY_SPECIFIED_CODE_YN | VARCHAR (1) |  |
| IS_STAGEABLE_CANCER_YN | VARCHAR (1) |  |
| PRIMARY_DX_ALLOWED_C | INTEGER |  |
| HL_TERM_ID | VARCHAR (10) | ID provided by HL for identifying this term. |
| CUR_MPD_MONDO_DELIM | VARCHAR (254) | Comma-delimited list of this record's current mapped MONDO codes. |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | DX_ID | ADVERSE_EVENT_TERM_INFO | DX_ID | No | No | No |  |
| 1 | DX_ID | EDG_DBC_INFO | DX_ID | No | No | No |  |
| 1 | DX_ID | V_CUBE_D_DIAGNOSIS | DIAGNOSIS_ID | Unknown | Unknown | No |  |
| 6 | PARENT_DX_ID | ADVERSE_EVENT_TERM_INFO | DX_ID | No | No | No |  |
| 6 | PARENT_DX_ID | CLARITY_EDG | DX_ID | Unknown | No | No |  |
| 6 | PARENT_DX_ID | EDG_DBC_INFO | DX_ID | No | No | No |  |
| 6 | PARENT_DX_ID | V_CUBE_D_DIAGNOSIS | DIAGNOSIS_ID | Unknown | Unknown | No |  |
| 12 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 12 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 12 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 13 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 13 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 13 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 18 | RECORD_STATE_C | ZC_DEL_STATUS | DEL_STATUS_C | No | No | No |  |
| 18 | RECORD_STATE_C | ZC_EDG_REC_STAT | EDG_REC_STAT_C | No | No | No |  |
| 18 | RECORD_STATE_C | ZC_ERS_REC_STAT | RECORD_STATUS_C | No | No | No |  |
| 18 | RECORD_STATE_C | ZC_HCD_REC_STATE | HCD_REC_STATE_C | No | No | No |  |
| 18 | RECORD_STATE_C | ZC_HFL_RECORD_STAT | HFL_RECORD_STAT_C | No | No | No |  |
| 18 | RECORD_STATE_C | ZC_IMM_REC_STATUS | IMM_REC_STATUS_C | No | No | No |  |
| 18 | RECORD_STATE_C | ZC_LLB_STATUS | LLB_STATUS_C | No | No | No |  |
| 18 | RECORD_STATE_C | ZC_LMA_RECORD_STAT | LMA_RECORD_STAT_C | No | No | No |  |
| 18 | RECORD_STATE_C | ZC_MEM_REC_STATUS | MEM_REC_STATUS_C | No | No | No |  |
| 18 | RECORD_STATE_C | ZC_OR_REC_STATUS | OR_REC_STATUS_C | No | No | No |  |
| 18 | RECORD_STATE_C | ZC_PBA_REC_STAT | PBA_REC_STAT_C | No | No | No |  |
| 18 | RECORD_STATE_C | ZC_PROV_REC_STATE | PROV_REC_STATE_C | No | No | No |  |
| 18 | RECORD_STATE_C | ZC_RECORD_STATE_2 | RECORD_STATE_2_C | No | No | No |  |
| 18 | RECORD_STATE_C | ZC_RECORD_STATE_3 | RECORD_STATE_3_C | No | No | No |  |
| 18 | RECORD_STATE_C | ZC_RECORD_STATE_4 | RECORD_STATE_4_C | No | No | No |  |
| 18 | RECORD_STATE_C | ZC_RECORD_STATE_6 | RECORD_STATE_6_C | No | No | No |  |
| 18 | RECORD_STATE_C | ZC_RECORD_STATE_7 | RECORD_STATE_7_C | No | No | No |  |

_(56 total; showing first 30)_
