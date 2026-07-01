# PAT_ENC_RSN_VISIT

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=PAT_ENC_RSN_VISIT

## Description

The PAT_ENC_RSN_VISIT contains the data entered as the Reason for Visit for a clinical system encounter. Each row in this table is one reason for visit associated with a patient encounter. One patient encounter may have multiple reasons for visit; therefore, the item LINE is used to identify each reason for visit within an encounter.

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
| PAT_ENC_CSN_ID | NUMERIC (18,0) | A unique serial number for this encounter. This number is unique across all patients and encounters in the system. |
| LINE | No | The line number of the reason for visit within the encounter. |
| CONTACT_DATE | DATETIME | The contact date of the encounter associated with this reason for visit. Note: There may be multiple encounters on the same calendar date. |
| ENC_REASON_ID | NUMERIC (18,0) | The ID of the record associated with the Reason for Visit entered in an encounter. |
| ENC_REASON_NAME *(deprecated)* | VARCHAR (254) |  |
| ENC_REASON_OTHER | No | The custom reason for visit entered when the clinical system user chooses ?Other? as a reason for visit. |
| COMMENTS | VARCHAR (4000) | The comments associated with the reason for visit entered in a clinical system exam encounter. |
| CM_CT_OWNER_ID | VARCHAR (25) | ID of the deployment owner for this contact. |
| RFV_ONSET_DT | DATETIME | The onset date for reason for call/visit stored on this line.  Typically this value will only be collected during call workflows such as a telephone encounter. |
| BODY_LOC_ID | NUMERIC (18,0) | The body location associated with the reason for visit for this patient encounter. This column is frequently used to link to the VESSEL_DOC table. |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| B-TREE INDEX | EIX_PAT_ENC_RSN_VISITENC | PAT_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_PAT_ENC_RSN_VISITENC | PAT_ENC_DATE_REAL | 2 | Yes | Yes |  |
| B-TREE INDEX | EIX_PAT_ENC_RSN_VISIT_ENREID | ENC_REASON_ID | 1 | Yes | Yes |  |

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

_(157 total; showing first 30)_
