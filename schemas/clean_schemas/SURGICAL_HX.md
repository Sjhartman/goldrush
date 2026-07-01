# SURGICAL_HX

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=SURGICAL_HX

## Description

The SURGICAL_HX table contains data from medical history contacts entered in clinical system patient encounters. Since one patient encounter may contain multiple medical history contacts, each contact is uniquely identified by a combination of the patient encounter serial number and a line number.

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
| PAT_ID | VARCHAR (18) | The unique ID assigned to the patient record. This ID may be encrypted if you have elected to use enterprise reporting?s encryption utility. |
| PAT_ENC_DATE_REAL | No | This is a numeric representation of the date of this encounter in your system. The integer portion of the number specifies the date of the encounter. The digits after the decimal point indicate multiple visits on one day. |
| END_HIST_DATE_REAL | No | This column has been deprecated since it cannot be used with table-based tracking unless a full extract of EPT is run. This is very bad for performance. |
| LINE | No | The line number of the surgical history contact within the encounter. |
| PROC_ID | NUMERIC (18,0) | The unique ID of the procedure record associated with the surgical history contact. Note: This is NOT the CPT(R) code. It is an internal identifier that is typically not visible to a user. |
| PROC_CODE *(deprecated)* | VARCHAR (40) |  |
| SURGICAL_HX_DATE | VARCHAR (255) | The free-text date entered in a patient's Surgical History for the procedure. |
| COMMENTS | VARCHAR (401) | Free-text comments entered for the procedure in the surgical history contact. |
| PROC_COMMENTS | No | Free-text comments entered for the "other" procedure in the patient's surgical history. |
| CONTACT_DATE | DATETIME | The contact date of the encounter associated with this surgical history contact. Note: There may be multiple encounters on the same calendar date. |
| CM_CT_OWNER_ID | VARCHAR (25) | ID of the deployment owner for this contact. |
| PAT_ENC_CSN_ID | NUMERIC (18,0) | A unique serial number for this encounter. This number is unique across all patients and encounters in the system. |
| SURGICAL_HX_SRC_C | INTEGER |  |
| HX_LNK_ENC_CSN | NUMERIC (18,0) | The Contact Serial Number of the encounter in which the history was created/edited. If the history was created/edited outside of the context of an encounter, then this column will be blank. |
| SURGICAL_HX_SRG_CSN | NUMERIC (18,0) | Stores the contact serial number of the surgery contact related to the current procedure. |
| SURG_LATERALITY_C | INTEGER |  |
| SURG_HX_START_DT | DATETIME | The starting date for the range of possible dates extracted from the free text date entered in column SURGICAL_HX_DATE. It is filled in automatically when the patient's history is saved. The ending date is in column SURG_HX_END_DT. |
| SURG_HX_END_DT | DATETIME | The ending date for the range of possible dates extracted from the free text date entered in column SURGICAL_HX_DATE. It is filled in automatically when the patient's history is saved. The starting date is in SURG_HX_END_DT. |
| SURG_HX_ORDER_ID | NUMERIC (18,0) | The unique ID of the order related to the current surgical history procedure |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| B-TREE INDEX | EIX_SURGICAL_HXENC | PAT_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_SURGICAL_HXENC | PAT_ENC_DATE_REAL | 2 | Yes | Yes |  |
| B-TREE INDEX | EIX_SURGICAL_HX_PRID | PROC_ID | 1 | Yes | Yes |  |

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

_(477 total; showing first 30)_
