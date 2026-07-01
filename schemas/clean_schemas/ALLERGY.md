# ALLERGY

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=ALLERGY

## Description

The ALLERGY table contains information about the allergies noted in your patients' clinical system records. You would use this table if you wanted to report on the number of patients who are allergic to sulfa drugs, for example. To determine the allergic reaction, link to the ALLERGY_REACTIONS table.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | LPL |
| Release Version | EPIC 2000 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| ALLERGY_ID | NUMERIC (18,0) | The unique ID used to identify the allergy record. |
| PAT_ID | VARCHAR (18) | The unique ID assigned to the patient record (EPT .1). This ID may be encrypted if you have elected to use enterprise reporting?s security utility. |
| ALLERGEN_ID | NUMERIC (18,0) | The unique ID assigned to the allergen (Agent) record. |
| DESCRIPTION | VARCHAR (100) | Stores a description for the allergy name. If a record for the allergen exists, this column will store the name of the allergen record. If a record for the allergen does not exist and "other" is chosen, this column will store the allergen name as entered by the provider. |
| REACTION | VARCHAR (4000) | This column contains the free text reaction comments. The actual reaction category value responses are stored in the ALLERGY_REACTIONS table which is linked via the ALLERGY_ID columns in both tables. |
| DATE_NOTED | DATETIME | The date the patient made it known that they had experienced an allergic reaction in calendar format. |
| STATUS *(deprecated)* | VARCHAR (10) |  |
| ENTERED_DATE *(deprecated)* | DATETIME | The date the allergy was entered into the patient?s record (formatted as MM/DD/YYYY from a cache DTE).  NOTE: If an allergy record is edited/updated, this will show the most recent change date.  Deprecated. This data can now be found in ALRGY_ENTERED_DTTM. |
| ENTRY_USER_ID | VARCHAR (18) | The unique ID of the clinical system user who entered this allergy into the patient?s record. This ID may be encrypted.  NOTE: If an allergy record is edited/updated, this will show the most recent change user ID. |
| SEVERITY_C | INTEGER |  |
| UPDATE_DATE | No | *** Deprecated *** This column is not reliably populated, row update tracking should be used instead. ****** The extract date and time of the record for this table. |
| CM_PHY_OWNER_ID | VARCHAR (25) | ID of the physical deployment owner for this record.  Physical owners will be where the data is hosted, either on the cross-over server or the owner deployment. |
| CM_LOG_OWNER_ID | VARCHAR (25) | ID of the logical deployment owner for this record.  Logical owners show the deployment where the record was created but doesn't represent if the record is a part of version skew. |
| ALLERGY_SEVERITY_C | INTEGER |  |
| ALRGY_STATUS_C | INTEGER |  |
| ALRGY_DLET_RSN_C | INTEGER |  |
| ALRGY_DLT_CMT | VARCHAR (300) | This item contains the comment about why an allergy was deleted from a patient's chart. |
| CONTRA_EXP_DT | DATETIME | The date that the contraindication will expire. |
| ALRGY_ENTERED_DTTM | 3040 | The date and time the allergy was entered into the patient's record using a calendar format. NOTE: If an allergy record is edited/updated this will show the most recent change. |
| ALLERGY_SYNONYM | VARCHAR (254) | Stores the synonym for allergy name. |
| REC_ARCHIVED_YN | No | Indicates whether the Allergy record is archived at the record level. |
| ALLERGY_CERTAINTY_C | INTEGER |  |
| ALLERGY_SOURCE_C | INTEGER |  |
| ALLERGY_PAT_CSN | NUMERIC (18,0) | The patient contact corresponding to the patient encounter in which this allergy was edited. |
| ALRGY_EST_START_DATE_VAL *(deprecated)* | VARCHAR (6) | *** Deprecated *** In table Allergy, the column ALRGY_EST_START_DATE_VAL has been deprecated. The deprecated column's content/data is no longer available since it is no longer populated in Chronicles.   A conversion will be run to move the data from the item (I LPL 3027) to the new item Allergy Noted Date Accuracy (I LPL 3021).  Previously, this column allowed formats of YYYY or YYYYMM to store the estimated start date of an allergy. Now, ALLERGY_NOTED_DATE_ACCURACY_C stores the accuracy of the date stored in DATE_NOTED. |
| ALLERGY_NOTED_DATE_ACCURACY_C | INTEGER |  |
| ALRGY_TRANSMTL_UTC_DTTM | DATETIME (UTC) | This item is used to store the last successful instant of transmittal to an external allergies list. It is currently only used for the SFM PLL drug reactions list in Norway. |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| B-TREE INDEX | EIX_ALLERGY_PAID | PAT_ID | 1 | Yes | Yes |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ALLERGY_ID | ADVERSE_EVENT_INFO | ADVERSE_EVENT_ID | No | No | No |  |
| 1 | ALLERGY_ID | COMPLICATIONS | PROBLEM_LIST_ID | No | No | No |  |
| 1 | ALLERGY_ID | HH_PBLST_INFO | PROBLEM_LIST_ID | Unknown | No | No |  |
| 1 | ALLERGY_ID | IMMUNE | IMMUNE_ID | Unknown | No | No |  |
| 1 | ALLERGY_ID | PL_SYSTEMS | PROBLEM_LIST_ID | Unknown | No | No |  |
| 1 | ALLERGY_ID | PROBLEM_LIST | PROBLEM_LIST_ID | Unknown | No | No |  |
| 1 | ALLERGY_ID | PROBLEM_LIST_ALL | PROBLEM_LIST_ID | No | No | No |  |
| 1 | ALLERGY_ID | PROB_TXP_MODIFIERS | PROBLEM_LIST_ID | Unknown | No | No |  |
| 1 | ALLERGY_ID | V_IMMUNIZATION_ADMINS | IMMUNE_ID | Unknown | Unknown | No |  |
| 2 | PAT_ID | ANTICOAG_SELF_REGULATING | PAT_ID | No | No | No |  |
| 2 | PAT_ID | CARE_COORDINATION | PAT_ID | Unknown | No | No |  |
| 2 | PAT_ID | CLAIMS_DERIVE_PAT_FLAGS | PAT_ID | No | No | No |  |
| 2 | PAT_ID | COMMUNITY_RESRC_REVIEWED | PAT_ID | No | No | No |  |
| 2 | PAT_ID | D_PAT_GEOGRAPHIC_CLASS | PAT_ID | Unknown | Unknown | No |  |
| 2 | PAT_ID | EPT_MEM_INFO | PAT_ID | No | No | No |  |
| 2 | PAT_ID | EXT_DATA_LAST_DONE | PAT_ID | No | No | No |  |
| 2 | PAT_ID | F_IBD_ADULT_FORM_PAT | PAT_ID | Unknown | Unknown | No |  |
| 2 | PAT_ID | HH_PAT_INFO | PAT_ID | Unknown | No | No |  |
| 2 | PAT_ID | HM_STATUS_UPD | PAT_ID | No | No | No |  |
| 2 | PAT_ID | IMMNZTN_LAST_REVIEW | PAT_ID | No | No | No |  |
| 2 | PAT_ID | PATIENT | PAT_ID | No | No | No |  |
| 2 | PAT_ID | PATIENT_2 | PAT_ID | No | No | No |  |
| 2 | PAT_ID | PATIENT_3 | PAT_ID | No | No | No |  |
| 2 | PAT_ID | PATIENT_4 | PAT_ID | No | No | No |  |
| 2 | PAT_ID | PATIENT_5 | PAT_ID | No | No | No |  |
| 2 | PAT_ID | PATIENT_6 | PAT_ID | No | No | No |  |
| 2 | PAT_ID | PATIENT_CONF_ADDR | PAT_ID | No | No | No |  |
| 2 | PAT_ID | PATIENT_MISC_COMMENTS | PAT_ID | No | No | No |  |
| 2 | PAT_ID | PATIENT_MYC | PAT_ID | Unknown | No | No |  |
| 2 | PAT_ID | PATIENT_OPT | PAT_ID | No | No | No |  |

_(188 total; showing first 30)_
