# PAT_ENC_DX

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=PAT_ENC_DX

## Description

The patient encounter diagnosis table contains one record for each diagnosis associated with each encounter level of service. This table will contain all diagnoses specified on the Order Summary screen.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | EPT |
| Release Version | EPIC 2000 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| PAT_ID | VARCHAR (18) | The unique ID assigned to the patient record (EPT .1). This ID may be encrypted if you have elected to use enterprise reporting?s security utility. |
| PAT_ENC_DATE_REAL | No | This is a numeric representation of the date of this encounter in your system. The integer portion of the number specifies the date of the encounter. The digits after the decimal point indicate multiple visits on one day. |
| LINE | No | The line number of the diagnosis within the encounter. This is the second column in the primary key and uniquely identifies this diagnosis on the encounter. |
| CONTACT_DATE | DATETIME | The contact date of the encounter associated with this diagnosis. Note: There may be multiple encounters on the same calendar date. |
| PAT_ENC_CSN_ID | NUMERIC (18,0) | A unique serial number for this encounter. This number is unique across all patients and encounters in the system. |
| DX_ID | NUMERIC (18,0) | The unique ID of the diagnosis record associated with the patient encounter. Note: This is NOT the ICD9 diagnosis code. It is an internal identifier that is typically not visible to a user. |
| ICD9_CODE | 18400 | *** Deprecated *** In table PAT_ENC_DX, the column ICD9_CODE (EDG 40) has been deprecated. Link to the CLARITY_EDG table using PAT_ENC_DX.DX_ID column. Refer to the Diagnosis and ICD Procedure Updates section of https://galaxy.epic.com/redirect.aspx?documentid=1577542 to determine the correct column to use. |
| ANNOTATION | VARCHAR (200) | The annotation (description) text entered for this diagnosis by the clinical system user. This field is NULL if no annotation was entered during the encounter.  Order entry in clinical system limits this field to 160 characters. |
| DX_QUALIFIER_C | VARCHAR (25) |  |
| PRIMARY_DX_YN | VARCHAR (1) | This is a one character field that indicates whether this diagnosis was the primary diagnosis for the encounter. If the diagnosis was the primary this field will have a value of 'Y' otherwise it will have a value of 'N'. |
| COMMENTS | VARCHAR (1024) | Any text comment associated with the encounter diagnosis. This field is NULL if no comment was provided. |
| CM_CT_OWNER_ID | VARCHAR (25) | ID of the deployment owner for this contact. |
| DX_CHRONIC_YN | VARCHAR (1) |  |
| ENC_ICD_CODE | 18400 | *** Deprecated *** In table PAT_ENC_DX, the column ENC_ICD_CODE (EDG 2000) has been deprecated. Link to the CLARITY_EDG table using PAT_ENC_DX.DX_ID column. Refer to the Diagnosis and ICD Procedure Updates section of https://galaxy.epic.com/redirect.aspx?documentid=1577542 to determine the correct column to use. |
| DX_STAGE_ID | NUMERIC (18,0) | The stage for the diagnosis. |
| UPDATE_DATE | No | The extract date and time of the row for this table. |
| DX_UNIQUE | VARCHAR (254) | Unique identifier given when a diagnosis is added to the encounter diagnosis list. |
| DX_ED_YN | VARCHAR (1) |  |
| DX_LINK_PROB_ID | NUMERIC (18,0) | Stores the problem ID of the linked problem. |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| B-TREE INDEX | EIX_PAT_ENC_DXENC | PAT_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_PAT_ENC_DXENC | PAT_ENC_DATE_REAL | 2 | Yes | Yes |  |
| B-TREE INDEX | EIX_PAT_ENC_DX_DX_CSN | DX_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_PAT_ENC_DX_DX_CSN | PAT_ENC_CSN_ID | 2 | Yes | Yes |  |

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

_(176 total; showing first 30)_
