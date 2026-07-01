# PROBLEM_LIST_HX

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=PROBLEM_LIST_HX

## Description

This table contains data relating to the history of problems from patients' problem lists in the clinical system.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | LPL |
| Release Version | SUMMER 2004 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| PROBLEM_LIST_ID | NUMERIC (18,0) | The unique ID of this Problem List entry. |
| LINE | No | Used to identify the particular problem within the historical problems |
| HX_PROBLEM_ID | NUMERIC (18,0) | ID of the diagnosis associated with this historical problem |
| HX_DESCRIPTION | VARCHAR (254) | The historical display name of the problem. Only contains data if the default display name is changed. |
| HX_DATE_NOTED | DATETIME | Represents the historical value of the first possible date that a problem could have been noted/onset on.    A problem's noted date is documented as a fuzzy date, meaning that it can capture approximate date data ("2012", "1/2012") or exact data ("3/5/2012"). This column captures the earliest date of the effective range. See HX_NOTED_END_DATE for the latest counterpart. For example, if 2012 is documented in hyperspace, then HX_NOTED_DATE will be 1/1/2012 and HX_NOTED_END_DATE will be 12/31/2012. |
| HX_DATE_RESOLVED | DATETIME | The date on which this problem was resolved. |
| HX_COMMENT | VARCHAR (1024) | The historical preview text (first characters) of all the Overview notes entered for a Problem List entry. |
| HX_DATE_OF_ENTRY | DATETIME | The date that the problem was added to or updated on the patient's Problem List in calendar format. |
| HX_ENTRY_USER_ID | VARCHAR (18) | The ID of the user who edited this problem on the patient's Problem List. This ID may be encrypted. |
| HX_STATUS *(deprecated)* | VARCHAR (254) |  |
| HX_LEVEL_URGENCY *(deprecated)* | VARCHAR (254) |  |
| HX_PRIORITY *(deprecated)* | VARCHAR (254) |  |
| HX_MYCHART_YN | VARCHAR (1) |  |
| CM_PHY_OWNER_ID | VARCHAR (25) | ID of the physical deployment owner for this record.  Physical owners will be where the data is hosted, either on the cross-over server or the owner deployment. |
| CM_LOG_OWNER_ID | VARCHAR (25) | ID of the logical deployment owner for this record.  Logical owners show the deployment where the record was created but doesn't represent if the record is a part of version skew. |
| HX_CHRONIC_YN | VARCHAR (1) |  |
| HX_PRINCIPAL_YN | VARCHAR (1) |  |
| HX_IS_HOSP_YN | VARCHAR (1) |  |
| HX_PROBLEM_EPT_CSN | NUMERIC (18,0) | Contact Serial Number (CSN) of the patient encounter where this historical problem list was documented. |
| HX_STATUS_C | INTEGER |  |
| HX_LEVEL_URGENCY_C | INTEGER |  |
| HX_PRIORITY_C | INTEGER |  |
| HX_ENTRY_INST | DATETIME (Local) | The date and time when the problem was updated on the patient's problem list. |
| HX_PROBLEM_POA_C | INTEGER |  |
| HX_STAGE_ID | NUMERIC (18,0) | This column holds the history of all stages ever associated with this problem. |
| HX_NOTED_END_DATE | DATETIME | Represents the historical value of the last possible date that a problem could have been noted/onset on.    A problem's noted date is documented as a fuzzy date, meaning that it can capture approximate date data ("2012", "1/2012") or exact data ("3/5/2012"). This column captures the latest date of the effective range. See HX_NOTED_DATE for the latest counterpart. For example, if 2012 is documented in hyperspace, then HX_NOTED_DATE will be 1/1/2012 and HX_NOTED_END_DATE will be 12/31/2012.  Note that the value may be empty, even if HX_NOTED_DATE is populated |
| HX_HOST_MODULE_C | INTEGER |  |
| MERGE_PROB_TYPE_C | INTEGER |  |
| HX_DIAG_START_DATE | DATETIME | Represents the earliest possible date that a problem could have been diagnosed on at a particular edit. The latest possible date is stored in HX_DIAG_END_DATE.  If these values are the same, then the date is exact rather than fuzzy. For a problem or condition affecting a patient, the diagnosis date is defined as the date when a qualified professional first recognized the presence of that condition with sufficient certainty, regardless of whether it was fully characterized at that time. For diseases such as cancer, this may be the earliest date of a clinical diagnosis from before it was histologically confirmed, not the date of confirmation if that occurred later. |
| HX_DIAG_END_DATE | DATETIME | Represents the last possible date that a problem could have been diagnosed on at a particular edit. The earliest possible date is stored in HX_DIAG_START_DATE. If these values are the same, then the date is exact rather than fuzzy. For a problem or condition affecting a patient, the diagnosis date is defined as the date when a qualified professional first recognized the presence of that condition with sufficient certainty, regardless of whether it was fully characterized at that time. For diseases such as cancer, this may be the earliest date of a clinical diagnosis from before it was histologically confirmed, not the date of confirmation if that occurred later. |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| B-TREE INDEX | EIX_PLHX_CSN_ID | HX_PROBLEM_EPT_CSN | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_PLHX_PROB_ID | HX_PROBLEM_ID | 1 | Yes | Yes |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | PROBLEM_LIST_ID | ADVERSE_EVENT_INFO | ADVERSE_EVENT_ID | No | No | No |  |
| 1 | PROBLEM_LIST_ID | ALLERGY | ALLERGY_ID | Unknown | No | No |  |
| 1 | PROBLEM_LIST_ID | COMPLICATIONS | PROBLEM_LIST_ID | No | No | No |  |
| 1 | PROBLEM_LIST_ID | HH_PBLST_INFO | PROBLEM_LIST_ID | Unknown | No | No |  |
| 1 | PROBLEM_LIST_ID | IMMUNE | IMMUNE_ID | Unknown | No | No |  |
| 1 | PROBLEM_LIST_ID | PL_SYSTEMS | PROBLEM_LIST_ID | Unknown | No | No |  |
| 1 | PROBLEM_LIST_ID | PROBLEM_LIST | PROBLEM_LIST_ID | Unknown | No | No |  |
| 1 | PROBLEM_LIST_ID | PROBLEM_LIST_ALL | PROBLEM_LIST_ID | No | No | No |  |
| 1 | PROBLEM_LIST_ID | PROB_TXP_MODIFIERS | PROBLEM_LIST_ID | Unknown | No | No |  |
| 1 | PROBLEM_LIST_ID | V_IMMUNIZATION_ADMINS | IMMUNE_ID | Unknown | Unknown | No |  |
| 3 | HX_PROBLEM_ID | ADVERSE_EVENT_TERM_INFO | DX_ID | No | No | No |  |
| 3 | HX_PROBLEM_ID | CLARITY_EDG | DX_ID | Unknown | No | No |  |
| 3 | HX_PROBLEM_ID | EDG_DBC_INFO | DX_ID | No | No | No |  |
| 3 | HX_PROBLEM_ID | V_CUBE_D_DIAGNOSIS | DIAGNOSIS_ID | Unknown | Unknown | No |  |
| 9 | HX_ENTRY_USER_ID | CLARITY_EMP | USER_ID | Unknown | No | No |  |
| 9 | HX_ENTRY_USER_ID | CLARITY_EMP_2 | USER_ID | Unknown | No | No |  |
| 9 | HX_ENTRY_USER_ID | CLARITY_EMP_3 | USER_ID | Unknown | No | No |  |
| 9 | HX_ENTRY_USER_ID | CLARITY_EMP_4 | USER_ID | No | No | No |  |
| 9 | HX_ENTRY_USER_ID | CLARITY_EMP_DEMO | USER_ID | No | No | No |  |
| 9 | HX_ENTRY_USER_ID | EMP_BASIC_INFO | USER_ID | No | No | No |  |
| 9 | HX_ENTRY_USER_ID | EMP_DOC_SETTINGS | USER_NUMBER_ID | No | No | No |  |
| 9 | HX_ENTRY_USER_ID | F_RX_USER | USER_ID | Unknown | Unknown | No |  |
| 9 | HX_ENTRY_USER_ID | IB_MESSAGE_SETTINGS | USER_ID | No | No | No |  |
| 9 | HX_ENTRY_USER_ID | LOGIN_INFO | USER_NUMBER_ID | No | No | No |  |
| 9 | HX_ENTRY_USER_ID | QC_RESULTS_REVIEW | USER_NUMBER_ID | No | No | No |  |
| 9 | HX_ENTRY_USER_ID | USER_SIDEBAR_RPT | USER_NUMBER_ID | Unknown | No | No |  |
| 9 | HX_ENTRY_USER_ID | V_CUBE_D_USER | USER_ID | Unknown | Unknown | No |  |
| 9 | HX_ENTRY_USER_ID | V_CUBE_RX_USER | USER_ID | Unknown | Unknown | No |  |
| 14 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 14 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |

_(165 total; showing first 30)_
