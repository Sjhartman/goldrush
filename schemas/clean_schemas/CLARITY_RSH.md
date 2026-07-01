# CLARITY_RSH

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=CLARITY_RSH

## Description

This view contains research study and client record information.

## Metadata

| Property | Value |
| --- | --- |
| Type | View |
| Release Version | MU3 - EPIC 2002 |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| RESEARCH_ID | VARCHAR (18) | The unique ID number of research study or client record |
| RESEARCH_NAME | VARCHAR (255) | The name of the research study or client record |
| RESEARCH_STATUS_C | INTEGER |  |
| SERV_AREA_ID *(deprecated)* | NUMERIC (18,0) |  |
| LOC_ID *(deprecated)* | NUMERIC (18,0) |  |
| STUDY_CODE | VARCHAR (255) | External ID for research study or client record. This code will appear on research study or client related charges. |
| PROV_ID | VARCHAR (18) | The principal investigator for the research study. |
| APPROVED_AMOUNT | NUMERIC (12,2) | Total dollar amount approved for research study. |
| BILLING_CONTACT | VARCHAR (255) | The billing contact person associated with the research study or client record. |
| FEE_SCHEDULE_ID | NUMERIC (18,0) | The fee schedule ID associated with the research study or client record. |
| CREDIT_GL_COMP | VARCHAR (100) | The Credit GL component associated with this research study or client record. |
| DEBIT_GL_COMP | VARCHAR (100) | The Debit GL component associated with this research study or client record. |
| CREATE_DATE | DATETIME | Research or client record create date |
| CM_PHY_OWNER_ID | VARCHAR (25) | ID of the physical deployment owner for this record.  Physical owners will be where the data is hosted, either on the cross-over server or the owner deployment. |
| CM_LOG_OWNER_ID | VARCHAR (25) | ID of the logical deployment owner for this record.  Logical owners show the deployment where the record was created but doesn't represent if the record is a part of version skew. |
| UPDATE_INSTANT_TM | DATETIME (Local) | Instant of update to the research study or client record. |
| MED_DISCOUNT | NUMERIC (18,2) | Informational medication discount percentage for this research study or client record. |
| STUDY_REPORT_ID | VARCHAR (18) | This column contains the ID of the study's report. |
| IRB_APPROVAL_NUM | VARCHAR (30) | The Institutional Review Board (IRB) (or ethics committee) approval number. |
| ALLOW_PCP_YN | VARCHAR (1) |  |
| ALLOW_ADMITTING_YN | VARCHAR (1) |  |
| ALLOW_ATTENDING_YN | VARCHAR (1) |  |
| ALLOW_TT_YN | VARCHAR (1) |  |
| GUARANTOR_PAT_ID | VARCHAR (18) | The unique ID of the administrative patient (EPT ID) created for the research study or client record as a guarantor. |
| CR_BY_INTERFACE_YN | VARCHAR (1) |  |
| RECORD_STATUS_C | INTEGER |  |
| NCT_NUM | VARCHAR (20) | The National Clinical Trials Number is a registry number specified for all studies registered with ClinicalTrials.gov. |
| RPT_GRP_TXT_1 | VARCHAR (80) | You have the ability to specify groupers for reporting purposes. This is a free-text report grouper. |
| RPT_GRP_TXT_2 | VARCHAR (80) | You have the ability to specify groupers for reporting purposes. This is a free-text report grouper. |
| RPT_GRP_TXT_3 | VARCHAR (80) | You have the ability to specify groupers for reporting purposes. This is a free-text report grouper. |
| RPT_GRP_TXT_4 | VARCHAR (80) | You have the ability to specify groupers for reporting purposes. This is a free-text report grouper. |
| RPT_GRP_TXT_5 | VARCHAR (80) | You have the ability to specify groupers for reporting purposes. This is a free-text report grouper. |
| RPT_GRP_CAT_1_C | INTEGER |  |
| RPT_GRP_CAT_2_C | INTEGER |  |
| RPT_GRP_CAT_3_C | INTEGER |  |
| RPT_GRP_CAT_4_C | INTEGER |  |
| RPT_GRP_CAT_5_C | INTEGER |  |
| STUDY_TYPE_C | INTEGER |  |
| FSC_USE_TYPE_C | INTEGER |  |
| PATIENT_FACING_NAME | VARCHAR (300) | Patient-facing name of the research study. It may appear in MyChart or other patient-facing areas. |
| PATIENT_FACING_DESC_ID | VARCHAR (18) | ID of SmartText record containing the research study's patient-facing description. |
| MYC_REQ_ENABLED_YN | VARCHAR (1) |  |
| MYC_REQUIRE_PA_YN | VARCHAR (1) |  |
| MYC_VISIBLE_YN | VARCHAR (1) |  |
| RSLT_SUPPRESS_SCHM_ID | NUMERIC (18,0) | Results Routing Scheme (LRS) record that determines how to suppress result messages for non-study team recipients. |
| ADV_EVT_TERM_SET_ID | VARCHAR (18) | The ID of the grouper record that stores the term set used to document adverse events for this study. |
| STUDY_STATUS_C | INTEGER |  |
| IRB_APPROVAL_DATE | DATETIME | The date when the research study most recently received IRB approval. |
| IRB_EXPIRATION_DATE | DATETIME | The date when the current IRB approval will expire for the research study. |
| RECORD_TYPE_C | INTEGER |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | RESEARCH_ID | RSH_CLIENT_INFO | CLIENT_ID | No | Unknown | No |  |
| 1 | RESEARCH_ID | RSH_MULTISITE_INFO | RESEARCH_ID | No | Unknown | No |  |
| 1 | RESEARCH_ID | RSH_RCVD_DOC | RESEARCH_ID | No | Unknown | No |  |
| 1 | RESEARCH_ID | RSH_RESEARCH_INFO | RESEARCH_ID | No | Unknown | No |  |
| 1 | RESEARCH_ID | RSH_RESEARCH_INFO_2 | RESEARCH_ID | No | Unknown | No |  |
| 3 | RESEARCH_STATUS_C | ZC_RESEARCH_STATUS | RESEARCH_STATUS_C | No | Unknown | No |  |
| 7 | PROV_ID | CLARITY_SER | PROV_ID | Unknown | Unknown | No |  |
| 7 | PROV_ID | CLARITY_SER_2 | PROV_ID | Unknown | Unknown | No |  |
| 7 | PROV_ID | CLARITY_SER_3 | PROV_ID | Unknown | Unknown | No |  |
| 7 | PROV_ID | CLARITY_SER_4 | PROV_ID | No | Unknown | No |  |
| 7 | PROV_ID | CLARITY_SER_MYC | PROV_ID | Unknown | Unknown | No |  |
| 7 | PROV_ID | D_PROV_PRIMARY_HIERARCHY | PROV_ID | Unknown | Unknown | No |  |
| 7 | PROV_ID | ED_SER_SETTINGS | PROV_ID | Unknown | Unknown | No |  |
| 7 | PROV_ID | EXT_CAL_PROV_CONFIG | PROV_ID | No | Unknown | No |  |
| 7 | PROV_ID | OR_SER_EQUIPMENT | PROV_ID | Unknown | Unknown | No |  |
| 7 | PROV_ID | OR_SER_ROOM | PROV_ID | Unknown | Unknown | No |  |
| 7 | PROV_ID | PROV_BATCH_LTR_GEN | PROV_ID | Unknown | Unknown | No |  |
| 7 | PROV_ID | PROV_GROUP | PROV_ID | No | Unknown | No |  |
| 7 | PROV_ID | V_CUBE_D_PROVIDER | PROVIDER_ID | Unknown | Unknown | No |  |
| 10 | FEE_SCHEDULE_ID | CLARITY_FSC | FEE_SCHEDULE_ID | No | Unknown | No |  |
| 14 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | Unknown | No |  |
| 14 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | Unknown | No |  |
| 14 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | Unknown | No |  |
| 15 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | Unknown | No |  |
| 15 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | Unknown | No |  |
| 15 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | Unknown | No |  |
| 18 | STUDY_REPORT_ID | REPORT_DETAILS | LRP_ID | No | Unknown | No |  |
| 24 | GUARANTOR_PAT_ID | ANTICOAG_SELF_REGULATING | PAT_ID | No | Unknown | No |  |
| 24 | GUARANTOR_PAT_ID | CARE_COORDINATION | PAT_ID | Unknown | Unknown | No |  |
| 24 | GUARANTOR_PAT_ID | CLAIMS_DERIVE_PAT_FLAGS | PAT_ID | No | Unknown | No |  |

_(93 total; showing first 30)_
