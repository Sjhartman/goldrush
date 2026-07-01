# MEDS_REV_HX_LIST

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=MEDS_REV_HX_LIST

## Description

This table lists the patient's current medications from each time a user reviewed the patient's medications. Reviewing user and other information about each instance of medication review is in the MEDS_REV_HX table. The list of medications at the most recent review instance is in the MEDS_REV_LAST_LIST table. Reviewing user and other information about the most recent review of medications is in the PATIENT table in columns MEDS_LAST_REV_TM, MEDS_LST_REV_USR_ID, and MEDS_LAST_REV_CSN.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | EPT |
| Release Version | SPRING 2008 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| PAT_ID | VARCHAR (18) | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| CONTACT_SERIAL_NUM | NUMERIC (18,0) | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect this is the Unique Contact Identifier (UCI). |
| LINE_COUNT | No | The line number of the associated instance of medication review in the patient's record. Together with PAT_ID, this forms the foreign key to the MEDS_REV_HX table. |
| VALUE_COUNT | No | The line number of one of the multiple medication orders that are associated with the patient and the instance of medication review from the MEDS_REV_HX table. |
| MEDICATION_ORDER_ID | NUMERIC (18,0) | The unique ID of one of the patient's current medication orders at the time of review. |
| TAKING_YN | VARCHAR (1) | Indicates whether the associated medication order was marked as taking at the time of review. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | PAT_ID | ANTICOAG_SELF_REGULATING | PAT_ID | No | Yes | No |  |
| 1 | PAT_ID | CARE_COORDINATION | PAT_ID | Unknown | Yes | No |  |
| 1 | PAT_ID | CLAIMS_DERIVE_PAT_FLAGS | PAT_ID | No | Yes | No |  |
| 1 | PAT_ID | COMMUNITY_RESRC_REVIEWED | PAT_ID | No | Yes | No |  |
| 1 | PAT_ID | D_PAT_GEOGRAPHIC_CLASS | PAT_ID | Unknown | Unknown | No |  |
| 1 | PAT_ID | EPT_MEM_INFO | PAT_ID | No | Yes | No |  |
| 1 | PAT_ID | EXT_DATA_LAST_DONE | PAT_ID | No | Yes | No |  |
| 1 | PAT_ID | F_IBD_ADULT_FORM_PAT | PAT_ID | Unknown | Unknown | No |  |
| 1 | PAT_ID | HH_PAT_INFO | PAT_ID | Unknown | Yes | No |  |
| 1 | PAT_ID | HM_STATUS_UPD | PAT_ID | No | Yes | No |  |
| 1 | PAT_ID | IMMNZTN_LAST_REVIEW | PAT_ID | No | Yes | No |  |
| 1 | PAT_ID | PATIENT | PAT_ID | No | Yes | No |  |
| 1 | PAT_ID | PATIENT_2 | PAT_ID | No | Yes | No |  |
| 1 | PAT_ID | PATIENT_3 | PAT_ID | No | Yes | No |  |
| 1 | PAT_ID | PATIENT_4 | PAT_ID | No | Yes | No |  |
| 1 | PAT_ID | PATIENT_5 | PAT_ID | No | Yes | No |  |
| 1 | PAT_ID | PATIENT_6 | PAT_ID | No | Yes | No |  |
| 1 | PAT_ID | PATIENT_CONF_ADDR | PAT_ID | No | Yes | No |  |
| 1 | PAT_ID | PATIENT_MISC_COMMENTS | PAT_ID | No | Yes | No |  |
| 1 | PAT_ID | PATIENT_MYC | PAT_ID | Unknown | Yes | No |  |
| 1 | PAT_ID | PATIENT_OPT | PAT_ID | No | Yes | No |  |
| 1 | PAT_ID | PAT_ENC_LAST_HX_CT | PAT_ID | Unknown | Unknown | No |  |
| 1 | PAT_ID | PAT_RES_CODE | PAT_ID | No | Yes | No |  |
| 1 | PAT_ID | PROB_LIST_REVIEWED | PAT_ID | No | Yes | No |  |
| 1 | PAT_ID | REGADDL_PAT | PAT_ID | No | Yes | No |  |
| 1 | PAT_ID | SCF_FHIR_MAP | PAT_ID | No | Yes | No |  |
| 1 | PAT_ID | TEETH_REVIEWED | PAT_ID | No | Yes | No |  |
| 1 | PAT_ID | VALID_PATIENT | PAT_ID | No | Yes | No |  |
| 1 | PAT_ID | V_PAT_ABO | PAT_ID | Unknown | Unknown | No |  |
| 1 | PAT_ID | V_PAT_FACT | PAT_ID | Unknown | Unknown | No |  |

_(230 total; showing first 30)_
