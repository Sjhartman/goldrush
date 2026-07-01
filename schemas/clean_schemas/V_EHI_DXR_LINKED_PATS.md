# V_EHI_DXR_LINKED_PATS

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=V_EHI_DXR_LINKED_PATS

## Description

Placeholder view for DXR EHI data that needs to be marked as both static and dynamic.

## Metadata

| Property | Value |
| --- | --- |
| Type | View |
| Release Version | Rel May 2022 |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| DOCUMENT_ID | NUMERIC (22,0) | This item stores the Received Document record ID. |
| PAT_ID | VARCHAR (18) | The unique ID of the patient for this received document. |
| CM_PHY_OWNER_ID | VARCHAR (25) | Physical owner item |
| CM_LOG_OWNER_ID | VARCHAR (25) | Logical Owner Item |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | DOCUMENT_ID | DOCS_RCVD | DOCUMENT_ID | Unknown | Unknown | No |  |
| 1 | DOCUMENT_ID | DOCS_RCVD_FMK_INFO | DOCUMENT_ID | No | Unknown | No |  |
| 2 | PAT_ID | ANTICOAG_SELF_REGULATING | PAT_ID | No | Unknown | No |  |
| 2 | PAT_ID | CARE_COORDINATION | PAT_ID | Unknown | Unknown | No |  |
| 2 | PAT_ID | CLAIMS_DERIVE_PAT_FLAGS | PAT_ID | No | Unknown | No |  |
| 2 | PAT_ID | COMMUNITY_RESRC_REVIEWED | PAT_ID | No | Unknown | No |  |
| 2 | PAT_ID | D_PAT_GEOGRAPHIC_CLASS | PAT_ID | Unknown | Unknown | No |  |
| 2 | PAT_ID | EPT_MEM_INFO | PAT_ID | No | Unknown | No |  |
| 2 | PAT_ID | EXT_DATA_LAST_DONE | PAT_ID | No | Unknown | No |  |
| 2 | PAT_ID | F_IBD_ADULT_FORM_PAT | PAT_ID | Unknown | Unknown | No |  |
| 2 | PAT_ID | HH_PAT_INFO | PAT_ID | Unknown | Unknown | No |  |
| 2 | PAT_ID | HM_STATUS_UPD | PAT_ID | No | Unknown | No |  |
| 2 | PAT_ID | IMMNZTN_LAST_REVIEW | PAT_ID | No | Unknown | No |  |
| 2 | PAT_ID | PATIENT | PAT_ID | No | Unknown | No |  |
| 2 | PAT_ID | PATIENT_2 | PAT_ID | No | Unknown | No |  |
| 2 | PAT_ID | PATIENT_3 | PAT_ID | No | Unknown | No |  |
| 2 | PAT_ID | PATIENT_4 | PAT_ID | No | Unknown | No |  |
| 2 | PAT_ID | PATIENT_5 | PAT_ID | No | Unknown | No |  |
| 2 | PAT_ID | PATIENT_6 | PAT_ID | No | Unknown | No |  |
| 2 | PAT_ID | PATIENT_CONF_ADDR | PAT_ID | No | Unknown | No |  |
| 2 | PAT_ID | PATIENT_MISC_COMMENTS | PAT_ID | No | Unknown | No |  |
| 2 | PAT_ID | PATIENT_MYC | PAT_ID | Unknown | Unknown | No |  |
| 2 | PAT_ID | PATIENT_OPT | PAT_ID | No | Unknown | No |  |
| 2 | PAT_ID | PAT_ENC_LAST_HX_CT | PAT_ID | Unknown | Unknown | No |  |
| 2 | PAT_ID | PAT_RES_CODE | PAT_ID | No | Unknown | No |  |
| 2 | PAT_ID | PROB_LIST_REVIEWED | PAT_ID | No | Unknown | No |  |
| 2 | PAT_ID | REGADDL_PAT | PAT_ID | No | Unknown | No |  |
| 2 | PAT_ID | SCF_FHIR_MAP | PAT_ID | No | Unknown | No |  |
| 2 | PAT_ID | TEETH_REVIEWED | PAT_ID | No | Unknown | No |  |
| 2 | PAT_ID | VALID_PATIENT | PAT_ID | No | Unknown | No |  |

_(40 total; showing first 30)_
