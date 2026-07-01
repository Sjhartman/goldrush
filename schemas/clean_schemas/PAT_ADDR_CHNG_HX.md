# PAT_ADDR_CHNG_HX

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=PAT_ADDR_CHNG_HX

## Description

This table keeps track of changes in the patient's address.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | EPT |
| Release Version | SUMMER 2004 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| PAT_ID | VARCHAR (18) | Patient ID for whom address is changed. |
| LINE | No | Line count in the address change history. |
| ADDR_HX_LINE1 | VARCHAR (254) | First line of patient's home address, current between dates recorded in columns EFF_START_DATE and EFF_END_DATE. |
| ADDR_HX_LINE2 | VARCHAR (254) | Second line of patient's home address, current between dates recorded in columns EFF_START_DATE and EFF_END_DATE. |
| ADDR_HX_LN_EXTRA | VARCHAR (254) | Additional line of patient's home address, current between dates recorded in columns EFF_START_DATE and EFF_END_DATE. |
| CITY_HX | VARCHAR (254) | Patient's home city, current between dates recorded in columns EFF_START_DATE and EFF_END_DATE. |
| COUNTY_HX_C | VARCHAR (66) |  |
| STATE_HX_C | VARCHAR (66) |  |
| ZIP_HX | VARCHAR (20) | Patient's home ZIP, current between dates recorded in columns EFF_START_DATE and EFF_END_DATE. |
| COUNTRY_HX *(deprecated)* | VARCHAR (128) |  |
| ADDR_CHNG_SOURCE_C | INTEGER |  |
| EFF_START_DATE | DATETIME | Effective start date of changed address (date when address was changed). |
| EFF_END_DATE | No | Effective end date of changed address (date of the next address change or NULL if this is the last address change). |
| CM_PHY_OWNER_ID | VARCHAR (25) | ID of the physical deployment owner for this record.  Physical owners will be where the data is hosted, either on the cross-over server or the owner deployment. |
| CM_LOG_OWNER_ID | VARCHAR (25) | ID of the logical deployment owner for this record.  Logical owners show the deployment where the record was created but doesn't represent if the record is a part of version skew. |
| PREV_HOUSE_NUM | VARCHAR (254) | Audit trail item used to store the previous house number when a new house number is entered or if the current primary address is edited. |
| PREV_DISTRICT_C | INTEGER |  |
| SIGNIFICANT_CHANGE_YN | VARCHAR (1) |  |
| ADDR_HX_VALID_YN | VARCHAR (1) |  |
| PREV_FLOOR | VARCHAR (254) | Audit trail item used to store the previous floor number when a new floor number is entered or if the current primary address is edited. |
| PREV_UNIT | VARCHAR (254) | Audit trail item used to store the previous unit number when a new unit number is entered or if the current primary address is edited. |
| PREV_BLDG_NAM | VARCHAR (254) | Audit trail item used to store the previous building name when a new building is entered or if the current primary address is edited. |
| COUNTRY_C | VARCHAR (66) |  |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| B-TREE INDEX | EIX_ADDR_CHNG_HX_EFF_END_DT | EFF_END_DATE | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_ADDR_CHNG_HX_EFF_START_DT | EFF_START_DATE | 1 | Yes | Yes |  |

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

_(53 total; showing first 30)_
