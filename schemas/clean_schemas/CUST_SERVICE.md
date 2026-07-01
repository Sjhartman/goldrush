# CUST_SERVICE

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=CUST_SERVICE

## Description

The CUST_SERVICE table stores information entered into system's Customer Service module. This can be used to report on communication between medical facility staff and patients.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | NCS |
| Release Version | EPIC 2000 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| COMM_ID | NUMERIC (18,0) | The unique identifier for the customer service communication. |
| ENTRY_USER_ID | VARCHAR (18) | The unique ID of the user who created the customer service communication. |
| ENTRY_DATE | DATETIME | The date the customer service communication was entered. |
| SOURCE_TYPE_C | INTEGER |  |
| SOURCE_MEMBER_ID | VARCHAR (18) | If the source of the customer service communication is a person who receives care at your facility or is a member of your health plan, this column contains the Patient (EPT) ID of that member. |
| TOPIC_C | VARCHAR (66) |  |
| SUBJECT_TYPE_C | INTEGER |  |
| RES_C | VARCHAR (66) |  |
| RES_USER_ID | VARCHAR (18) | The unique ID of the user who resolved the customer service communication. |
| RES_DATE | DATETIME | The date the customer service communication was resolved. |
| RES_SATISFACTION | INTEGER | The recorded satisfaction of the customer service communication. |
| PRIORITY_C | VARCHAR (66) |  |
| SUMMARY | VARCHAR (255) | The summary of the customer service communication. |
| SOURCE_STAFF_ID | VARCHAR (18) | If the source of the customer service communication is an employee of your facility, this column contains the Provider (SER) ID of that employee. |
| SOURCE_PLAN_GRP_ID | VARCHAR (35) | If the source of the customer service communication is a plan group, this column contains the Payor Plan Group (PPG) ID of that plan group. |
| SOURCE_CARRIER_ID | VARCHAR (18) | If the source of the customer service communication is a carrier, this column contains the Carrier (MCR) ID of that carrier. |
| SOURCE_ACCOUNT_ID | NUMERIC (18,0) | If the source of the customer service communication is a guarantor account, this column contains the Accounts Receivable (EAR) ID of that guarantor account. |
| SOURCE_NETWORK_ID | VARCHAR (18) | If the source of the customer service communication is a provider network, this column contains the Network Database (NET) ID of that provider network. |
| SUBJ_MEMBER_ID | VARCHAR (18) | If the subject of the customer service communication is a person who receives care at your facility or is a member of your health plan, this column contains the Patient (EPT) ID of that member. |
| SUBJ_STAFF_ID | VARCHAR (18) | If the subject of the customer service communication is an employee of your facility, this column contains the Provider (SER) ID of that employee. |
| SUBJ_PLAN_GRP_ID | VARCHAR (35) | If the subject of the customer service communication is a plan group, this column contains the Payor Plan Group (PPG) ID of that plan group. |
| SUBJ_CARRIER_ID | VARCHAR (18) | If the subject of the customer service communication is a carrier, this column contains the Carrier (MCR) ID of that carrier. |
| SUBJ_NETWORK_ID | VARCHAR (18) | If the subject of the customer service communication is a provider network, this column contains the Network Database (NET) ID of that provider network. |
| SUBJ_VENDOR_ID | VARCHAR (18) | If the subject of the customer service communication is a vendor, this column contains the Vendor (VEN) ID of that vendor. |
| SUBJ_REFERRAL_ID | NUMERIC (18,0) | If the subject of the customer service communication is a referral, this column contains the Referral Database (RFL) ID of that referral. |
| SUBJ_CLAIM_ID | NUMERIC (18,0) | If the subject of the customer service communication is a claim, this column contains the Claims System (CLM) ID of that claim. |
| PAT_ENC_CSN_ID | NUMERIC (18,0) | The unique identifier of the patient encounter related to the customer service communication. |
| RKP_ID | VARCHAR (18) | The unique ID of the risk panel for the customer service communication. |
| LOB_ID | VARCHAR (18) | The line of business for the customer service communication. |
| REC_SENSITIVITY_C | INTEGER |  |
| REC_COMM_ORIGIN_C | INTEGER |  |
| SRC_CUSTOMER | VARCHAR (255) | If the source type of the customer service communication is a custom value, this column contains the free text source. For example, the name of the person who called your facility's customer service representative. |
| SRC_VENDOR_ID | VARCHAR (18) | If the source of the customer service communication is a vendor, this column contains the Vendor (VEN) ID of that vendor. |
| SRC_PAYOR_ID | NUMERIC (18,0) | If the source of the customer service communication is a payor, this column contains the Payor Master (EPM) ID of that payor. |
| RECORD_ENTRY_TIME | 140 | The time the customer service communication was entered. |
| SUB_CUSTOMER | VARCHAR (255) | If the subject type of the customer service communication is a custom value, this column contains the free text subject. For example, the name of the person the customer service communication is about. |
| SUB_LOCATION_ID | NUMERIC (18,0) | If the subject of the customer service communication is a location, this column contains the Facility Profile (EAF) ID of that location. |
| SUB_POS_ID | NUMERIC (18,0) | If the subject of the customer service communication is a place of service, this column contains the Facility Profile (EAF) ID of that place of service. |
| SUB_DEPT_ID | NUMERIC (18,0) | If the subject of the customer service communication is a department, this column contains the Department (DEP) ID of that department. |
| REC_RES_TIME | 320 | The time the customer service communication was resolved. |
| NCS_TEXT *(deprecated)* | VARCHAR (255) | Deprecated - The text for the customer service communication. |
| CM_PHY_OWNER_ID | VARCHAR (25) | ID of the physical deployment owner for this record.  Physical owners will be where the data is hosted, either on the cross-over server or the owner deployment. |
| CM_LOG_OWNER_ID | VARCHAR (25) | ID of the logical deployment owner for this record.  Logical owners show the deployment where the record was created but doesn't represent if the record is a part of version skew. |
| LAB_SPECIMEN_ID | VARCHAR (18) | Laboratory specimen associated with this laboratory communication log. |
| LAB_TEST_ID | VARCHAR (18) | Laboratory performable test associated with this communication. |
| SUBJ_REQ_GRP_ID | NUMERIC (18,0) | The unique ID of the requisition grouper associated with the laboratory communication log. |
| LAB_LOG_STATUS_C | INTEGER |  |
| LAB_LOG_TYPE_C | INTEGER |  |
| LAB_ORDER_ID | NUMERIC (18,0) | unique comm log entry |
| EXTERNAL_ID_NUM | VARCHAR (254) | The external ID for the customer service communication. |
| SUBJECT_EAR_ID | NUMERIC (18,0) | If the subject of the customer service communication is a guarantor account, this column contains the Accounts Receivable (EAR) ID of that guarantor account. |
| VALID_CRM_YN | VARCHAR (1) |  |
| NOT_RESOLVED_YN | VARCHAR (1) |  |
| RESPOND_BY_METHOD_C | INTEGER |  |
| RESPOND_METHOD_INFO | VARCHAR (254) | Respond By method information |
| RES_1ST_ATTEMPT_YN | VARCHAR (1) |  |
| CRM_OWNER_YN | VARCHAR (1) |  |
| CRM_CUR_OWNER_ID | VARCHAR (18) | The unique ID of the user who is the current CRM owner. |
| OWN_BUS_SEG_EAF_ID | NUMERIC (18,0) | Owning business segment, for use in business segmentation. Only populated if the customer service communication is created in a payor business segment. Not populated when the record is created in a service area. |
| CREATION_SA_PBS_ID | NUMERIC (18,0) | The unique ID of the service area or payer business segment where the customer service communication was created. |
| SUB_TOPIC_C | INTEGER |  |
| HAR_ID | NUMERIC (18,0) | If the subject of the customer service communication is a hospital account, this column contains the Hospital Account (HAR) ID. |
| ENTRY_DEPARTMENT_ID | NUMERIC (18,0) | This field contains the login department of the user who created the record. |
| ROUT_HX_HTH_ID | NUMERIC (18,0) | The routing history thread for the customer service communication. |
| SOURCE_PBA_ID | VARCHAR (18) | If the source of the customer service communication is a premium billing account, this column contains the PB Account (PBA) ID. |
| SUBJECT_PBA_ID | VARCHAR (18) | If the subject of the customer service communication is a premium billing account, this column contains the PB Account (PBA) ID. |
| LAB_REQ_ID | NUMERIC (18,0) | Laboratory requisition associated with this laboratory communication log. |
| LAB_CASE_ID | NUMERIC (18,0) | The unique ID of the laboratory case associated with the laboratory communication log. |
| USER_CONTEXT_C | VARCHAR (66) |  |
| REOPEN_FIRST_ATT_YN | VARCHAR (1) |  |
| RECORD_STATE_C | INTEGER |  |
| WAS_REOPENED_YN | VARCHAR (1) |  |
| CREAT_QUICK_CRM_ID | NUMERIC (18,0) | ID of the Quick CRM (HGM record) from which this CRM was created. |
| EXTERNAL_SOURCE | VARCHAR (254) | The identifier assigned to this CRM by the external source that created it. |
| BANK_RECON_ID | NUMERIC (18,0) | If the subject of the customer service communication is a bank reconciliation, this column contains the Cash (CSH) ID of that bank reconciliation. |
| SUBJECT_APC_ID | NUMERIC (18,0) | This field stores the link to the subject AP Check. |
| SOURCE_PROSPECT_ID | NUMERIC (18,0) | If the source of the customer service communication is a prospective patient, this column contains the Requisition Grouper (RQG) ID of that prospective patient. |
| SUBJECT_PROSPECT_ID | NUMERIC (18,0) | If the subject of the customer service communication is a prospective patient, this column contains the Requisition Grouper (RQG) ID of that prospective patient. |
| SOURCE_SUBMITTER_ID | NUMERIC (18,0) | If the source of the customer service communication is a submitter, this column contains the Submitter (SMT) ID of that submitter. |
| SUBJECT_ORDER_ID | NUMERIC (18,0) | If the subject of the customer service communication is an order, this column contains the Order (ORD) ID. |
| SUBJECT_CAMPAIGN_ID | NUMERIC (18,0) | If the subject of the customer service communication is a campaign, this column contains the Campaign (CCT) ID of that campaign. |
| SUBJECT_DECISION_ID | NUMERIC (18,0) | If the subject of the customer service communication is a decision, this column contains the Financial Assistance Tracker (FNT) ID of that decision. |
| SUBJECT_ESTIMATE_ID | NUMERIC (18,0) | If the subject of the customer service communication is an estimate, this column contains the Estimate (PES) ID of that estimate. |
| ENTRY_UTC_DTTM | DATETIME (UTC) | The date and time when the customer service communication was entered, in UTC format. |
| RESOLUTION_UTC_DTTM | DATETIME (UTC) | The date and time when the customer service communication was resolved, in UTC format. |
| SOURCE_RESP_PRTY_GUID | VARCHAR (128) | If the source of the customer service communication is a responsible party for a patient, this column contains the GUID of that responsible party. |
| SUBJECT_RESP_PRTY_GUID | VARCHAR (128) | If the subject of the customer service communication is a responsible party for a patient, this column contains the GUID of that responsible party. |
| SOURCE_USER_ID | VARCHAR (18) | If the source of the customer service communication is an employee, this column contains the ID of that user record. |
| VOID_USER_ID | VARCHAR (18) | The user who voided this NCS |
| VOID_UTC_DTTM | DATETIME (UTC) | Instant at which this NCS was voided. |
| SUBJECT_PROJECT_ID | NUMERIC (18,0) | Stores the subject analytics project (CPJ) record ID. |
| APPEAL_DECISION_DATE | DATETIME | The date the appeal's outcome was decided. |
| APPEAL_SENT_TO_IRE_DATE | DATETIME | The date the appeal case was sent to the Independent Review Entity. |
| MOCK_RECORD_YN | VARCHAR (1) |  |
| SUBJECT_AUTH_REQUEST_ID | NUMERIC (18,0) | Auth Request (AUG) that this CRM is about. |
| RESOLVE_AUTH_REQUEST_ID | NUMERIC (18,0) | Authorization Request (AUG) created to resolve this CRM. |
| CREATION_WORKFLOW_LOCATOR_ID | NUMERIC (18,0) | The unique ID of the locator record of type Customer Service Workflow that was used to create this Customer Service record. |
| APPEAL_GRIEVANCE_NOTIF_DATE | DATETIME | The date the appeal or grievance's notification was sent out. |
| SUBJECT_CLAIM_RECON_ID | VARCHAR (18) | If the subject of the customer service communication is a rejected claim, this column contains the rejected claim (CRD) ID of that rejected claim. |
| SUBJECT_COVERAGE_ID | NUMERIC (18,0) | Coverage (CVG) that this CRM is about. |
| SUBJECT_RESEARCH_ID | VARCHAR (18) | If the source of the customer service communication is a research study, this column contains the ID of that research study. |
| AUTO_RES_C | INTEGER |  |
| SUBJECT_USER_ID | VARCHAR (18) | Stores the subject employee for the customer service record. |
| REC_COMM_SUBORIGIN_C | INTEGER |  |
| CREATION_WORKQUEUE_ID | VARCHAR (18) | Stores the Workqueue (WQF) ID a CRM was created from. |
| OLD_ECI_ID_TEMP_MRG | INTEGER | Old ECI ID in the unmerged deployment. |
| OLD_NCS_ID_TEMP_MRG | INTEGER | Old CRM internal ID in the unmerged deployment. |
| OLD_NCS_CID_TEMP_MRG | INTEGER | Old CRM CID in the unmerged deployment. |
| IS_CRM_TICKET_YN | VARCHAR (1) |  |
| OVERRIDE_BUS_SEG_POS_ID | NUMERIC (18,0) | The user specified business segment that the CRM should be owned by. |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | COMM_ID | CUST_SERVICE_2 | COMM_ID | No | No | No |  |
| 1 | COMM_ID | CUST_SERVICE_TRANSFER | COMM_ID | No | No | No |  |
| 1 | COMM_ID | CUST_SERV_ORG_FILTER_SA | COMM_ID | No | No | No |  |
| 1 | COMM_ID | V_ADT_TC_DEST | COMM_ID | Unknown | Unknown | No |  |
| 1 | COMM_ID | V_ADT_TRANSFER_CENTER | COMM_ID | Unknown | Unknown | No |  |
| 2 | ENTRY_USER_ID | CLARITY_EMP | USER_ID | Unknown | No | No |  |
| 2 | ENTRY_USER_ID | CLARITY_EMP_2 | USER_ID | Unknown | No | No |  |
| 2 | ENTRY_USER_ID | CLARITY_EMP_3 | USER_ID | Unknown | No | No |  |
| 2 | ENTRY_USER_ID | CLARITY_EMP_4 | USER_ID | No | No | No |  |
| 2 | ENTRY_USER_ID | CLARITY_EMP_DEMO | USER_ID | No | No | No |  |
| 2 | ENTRY_USER_ID | EMP_BASIC_INFO | USER_ID | No | No | No |  |
| 2 | ENTRY_USER_ID | EMP_DOC_SETTINGS | USER_NUMBER_ID | No | No | No |  |
| 2 | ENTRY_USER_ID | F_RX_USER | USER_ID | Unknown | Unknown | No |  |
| 2 | ENTRY_USER_ID | IB_MESSAGE_SETTINGS | USER_ID | No | No | No |  |
| 2 | ENTRY_USER_ID | LOGIN_INFO | USER_NUMBER_ID | No | No | No |  |
| 2 | ENTRY_USER_ID | QC_RESULTS_REVIEW | USER_NUMBER_ID | No | No | No |  |
| 2 | ENTRY_USER_ID | USER_SIDEBAR_RPT | USER_NUMBER_ID | Unknown | No | No |  |
| 2 | ENTRY_USER_ID | V_CUBE_D_USER | USER_ID | Unknown | Unknown | No |  |
| 2 | ENTRY_USER_ID | V_CUBE_RX_USER | USER_ID | Unknown | Unknown | No |  |
| 4 | SOURCE_TYPE_C | ZC_NCS_SRC_TYPE | SOURCE_TYPE_C | No | No | No |  |
| 5 | SOURCE_MEMBER_ID | ANTICOAG_SELF_REGULATING | PAT_ID | No | No | No |  |
| 5 | SOURCE_MEMBER_ID | CARE_COORDINATION | PAT_ID | Unknown | No | No |  |
| 5 | SOURCE_MEMBER_ID | CLAIMS_DERIVE_PAT_FLAGS | PAT_ID | No | No | No |  |
| 5 | SOURCE_MEMBER_ID | COMMUNITY_RESRC_REVIEWED | PAT_ID | No | No | No |  |
| 5 | SOURCE_MEMBER_ID | D_PAT_GEOGRAPHIC_CLASS | PAT_ID | Unknown | Unknown | No |  |
| 5 | SOURCE_MEMBER_ID | EPT_MEM_INFO | PAT_ID | No | No | No |  |
| 5 | SOURCE_MEMBER_ID | EXT_DATA_LAST_DONE | PAT_ID | No | No | No |  |
| 5 | SOURCE_MEMBER_ID | F_IBD_ADULT_FORM_PAT | PAT_ID | Unknown | Unknown | No |  |
| 5 | SOURCE_MEMBER_ID | HH_PAT_INFO | PAT_ID | Unknown | No | No |  |
| 5 | SOURCE_MEMBER_ID | HM_STATUS_UPD | PAT_ID | No | No | No |  |

_(779 total; showing first 30)_
