# V_PAT_HX_TOB_USE

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=V_PAT_HX_TOB_USE

## Description

This view calculates the current pack years for a patient based on current tobacco use information documented.

## Metadata

| Property | Value |
| --- | --- |
| Type | View |
| Release Version | Rel February 2022 |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| PAT_ID | No | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| TOB_PACK_YEARS | No | Stores the calculated amount of pack years based on the patient's smoking tobacco use. |
| TOB_CURRENT_PPD | No | Stores the patient's current packs per day of smoking tobacco use. |
| TOB_START_DATE | No | Stores the patient's original start date for smoking tobacco. |
| TOB_QUIT_DATE | No | Stores the patient's quit date for smoking tobacco if they have quit smoking. |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | PAT_ID | ANTICOAG_SELF_REGULATING | PAT_ID | No | Unknown | No |  |
| 1 | PAT_ID | CARE_COORDINATION | PAT_ID | Unknown | Unknown | No |  |
| 1 | PAT_ID | CLAIMS_DERIVE_PAT_FLAGS | PAT_ID | No | Unknown | No |  |
| 1 | PAT_ID | COMMUNITY_RESRC_REVIEWED | PAT_ID | No | Unknown | No |  |
| 1 | PAT_ID | D_PAT_GEOGRAPHIC_CLASS | PAT_ID | Unknown | Unknown | No |  |
| 1 | PAT_ID | EPT_MEM_INFO | PAT_ID | No | Unknown | No |  |
| 1 | PAT_ID | EXT_DATA_LAST_DONE | PAT_ID | No | Unknown | No |  |
| 1 | PAT_ID | F_IBD_ADULT_FORM_PAT | PAT_ID | Unknown | Unknown | No |  |
| 1 | PAT_ID | HH_PAT_INFO | PAT_ID | Unknown | Unknown | No |  |
| 1 | PAT_ID | HM_STATUS_UPD | PAT_ID | No | Unknown | No |  |
| 1 | PAT_ID | IMMNZTN_LAST_REVIEW | PAT_ID | No | Unknown | No |  |
| 1 | PAT_ID | PATIENT | PAT_ID | No | Unknown | No |  |
| 1 | PAT_ID | PATIENT_2 | PAT_ID | No | Unknown | No |  |
| 1 | PAT_ID | PATIENT_3 | PAT_ID | No | Unknown | No |  |
| 1 | PAT_ID | PATIENT_4 | PAT_ID | No | Unknown | No |  |
| 1 | PAT_ID | PATIENT_5 | PAT_ID | No | Unknown | No |  |
| 1 | PAT_ID | PATIENT_6 | PAT_ID | No | Unknown | No |  |
| 1 | PAT_ID | PATIENT_CONF_ADDR | PAT_ID | No | Unknown | No |  |
| 1 | PAT_ID | PATIENT_MISC_COMMENTS | PAT_ID | No | Unknown | No |  |
| 1 | PAT_ID | PATIENT_MYC | PAT_ID | Unknown | Unknown | No |  |
| 1 | PAT_ID | PATIENT_OPT | PAT_ID | No | Unknown | No |  |
| 1 | PAT_ID | PAT_ENC_LAST_HX_CT | PAT_ID | Unknown | Unknown | No |  |
| 1 | PAT_ID | PAT_RES_CODE | PAT_ID | No | Unknown | No |  |
| 1 | PAT_ID | PROB_LIST_REVIEWED | PAT_ID | No | Unknown | No |  |
| 1 | PAT_ID | REGADDL_PAT | PAT_ID | No | Unknown | No |  |
| 1 | PAT_ID | SCF_FHIR_MAP | PAT_ID | No | Unknown | No |  |
| 1 | PAT_ID | TEETH_REVIEWED | PAT_ID | No | Unknown | No |  |
| 1 | PAT_ID | VALID_PATIENT | PAT_ID | No | Unknown | No |  |
| 1 | PAT_ID | V_PAT_ABO | PAT_ID | Unknown | Unknown | No |  |
| 1 | PAT_ID | V_PAT_FACT | PAT_ID | Unknown | Unknown | No |  |

_(31 total; showing first 30)_
