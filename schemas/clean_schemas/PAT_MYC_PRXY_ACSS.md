# PAT_MYC_PRXY_ACSS

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=PAT_MYC_PRXY_ACSS

## Description

Proxy access in web based chart system provides the means for one patient to view data for another patient. A typical use of this functionality is for a parent to be able to view their minor child's medical record. The items in this table keep track of current proxy relationships.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | EPT |
| Release Version | EPIC 2002 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| PAT_ID | VARCHAR (18) | The unique ID assigned to the patient record. This ID may be encrypted if you have elected to use enterprise reporting?s security utility. |
| LINE | No | Since a patient may have more than one proxy relationship, the line number identifies each relationship for a given patient. |
| PROXY_PAT_ID | VARCHAR (18) | The unique ID of the patient who has proxy access to the record of the patient who is identified in PAT_ID. |
| MYC_PRXY_RELATN_C | INTEGER |  |
| FROM_DATE | DATETIME | The date from which the proxy relationship is valid. |
| TO_DATE | DATETIME | The date when the proxy relationship expires. |
| ACCESS_ECL_ID | VARCHAR (18) | The unique ID of the access class in use when the proxy views the patient's record. |
| CM_PHY_OWNER_ID | VARCHAR (25) | ID of the physical deployment owner for this record.  Physical owners will be where the data is hosted, either on the cross-over server or the owner deployment. |
| CM_LOG_OWNER_ID | VARCHAR (25) | ID of the logical deployment owner for this record.  Logical owners show the deployment where the record was created but doesn't represent if the record is a part of version skew. |
| MYC_PROXY_CMT | VARCHAR (254) | The comments entered for proxy relationship. |
| PROXY_RELATION_ID | VARCHAR (18) | This is the relationship ID for the proxy relation as defined by a the row in this table. This ID can be used to uniquely identify the child  (subject) record given the parent ID and this ID. |
| PROXY_WPR_ID | VARCHAR (18) | The MyChart account ID for the proxy (delegate) of this patient. |
| PROXY_STATUS_C | INTEGER |  |
| PROXY_PROFILE_ID | VARCHAR (254) | This contains the web profile that should be assigned to the delegate when accessing the subject's information |
| EXP_NOTIFIED_DATE | DATETIME | Date when last notification for proxy access expiration was sent |
| PROXY_LST_ACSS_DT | DATETIME | This is the most recent access date for a delegate accessing a proxy subject's record in MyChart. |
| PRXY_ENTERED_REL_C | VARCHAR (66) |  |
| PROXY_PREFERENCES_ID | NUMERIC (18,0) | The ID number of the communication preferences record for the proxy. |
| PROXY_ACCESS_AVAIL_UTC_DTTM | DATETIME (UTC) | This item stores the most recent instant the proxy had a pending activation workflow occur where the proxy received the necessary information to  sign up and become active on MyChart; for example, receiving a code. If  the proxy was inactivated or had their activation code disabled, this is  set to null. |
| PROXY_LST_ACSS_UTC_DTTM | DATETIME (UTC) | This item stores the most recent instant that the related proxy accessed this patient within MyChart. |
| MYC_PRXY_REL_STATUS_C | INTEGER |  |
| CONFRM_ATTEMPT_CNT | INTEGER | A count of the number of attempts the proxy has made to confirm their relationship with this patient, prior to entering the correct identifying information. |
| PROXY_ACCESS_SOURCE_C | INTEGER |  |
| PRXY_ACSS_MANUALLY_MODIFIED_YN | VARCHAR (1) |  |

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

_(90 total; showing first 30)_
