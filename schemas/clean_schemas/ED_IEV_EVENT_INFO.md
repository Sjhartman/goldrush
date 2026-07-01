# ED_IEV_EVENT_INFO

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=ED_IEV_EVENT_INFO

## Description

This table contains information about the current event records.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | IEV |
| Release Version | EPIC 2002 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| EVENT_ID | VARCHAR (18) | The unique ID of the event record. |
| LINE | No | The line number for the information associated with this event. Multiple pieces of information can be associated with this record. |
| EVENT_TYPE | VARCHAR (18) | The associated event template for this event record. This column is frequently used to link to the ED_EVENT_TMPL_INFO table. |
| EVENT_STATUS_NAME *(deprecated)* | VARCHAR (8) |  |
| EVENT_DISPLAY_NAME | VARCHAR (300) | The display name of the event. |
| EVENT_TIME | DATETIME (Local) | The instant when the event occurred. |
| EVENT_RECORD_TIME | DATETIME (Local) | The instant when the event was recorded. |
| EVENT_USER_ID | VARCHAR (18) | The unique ID of the user who initiated the event. This column is frequently used to link to the CLARITY_EMP table. |
| EVENT_CMT | VARCHAR (2000) | The comments entered for the event. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| EVENT_DEPT_ID | NUMERIC (18,0) | The unique ID of the department in which this event was fired. |
| ADT_EVENT_ID | NUMERIC (18,0) | The unique ID of the Admission, Transfer, Discharge, or Leave of Absence (ADT) event record link that is associated with this event. The following ED events have linked ADT evens: ED Roomed (A) ED Transfer (T) ED Admit to Hospital (T) |
| STAFFED_BEDS | NUMERIC (18,0) | The number of staffed beds for a department at the time of the event. This item is populated only if you are using the Staffed Beds activity. |
| EVENT_KEY | VARCHAR (254) | A unique key associated with this event. The key is stored in other master files in order to reference this event. |
| EVENT_NOTE_ID | VARCHAR (254) | The unique ID of the note that is associated with this event. |
| EVENT_FINDING_ID | NUMERIC (18,0) | The unique ID of the result that is associated with this event. This column is frequently used to link to the ORDER_RES table. |
| EVENT_IMPLANT_ID | VARCHAR (18) | The unique ID of the implant that is associated with this event. This column is frequently used to link to the OR_IMP table. |
| EVENT_LINE_DATA_ID | VARCHAR (18) | The line number of the associated data stored for this event in OpTime's Log Entry activity. This column can be used to link to the OR_LNLG_GENERAL table. |
| EVENT_PROV_ID | VARCHAR (18) | The unique ID associated with the provider record for this event. For example, an Assign Attending event stores the provider who was assigned in this column. This column is frequently used to link to the CLARITY_SER table. |
| LOCATION_ID | NUMERIC (18,0) | The unique ID of the patient location record that is associated with this event. This link is available only for emergency department contacts and for any location definition in the patient location facility master file that is associated with an event template master file. This column can be used to link to the CL_PLC table. |
| REC_PAT_LOC_ID *(deprecated)* | NUMERIC (18,0) | This column is deprecated and does not extract any data. When this column was created, the patient location master file was reserved for future development. Since then, LOCATION_ID in the ED_IEV_EVENT_INFO table was created to retrieve the data for which this column was intended. Use that table instead. |
| EVENT_STATUS_C | INTEGER |  |
| REC_VERB_ORD_TYPE_C | INTEGER |  |
| REC_VRB_ORD_COMM_ID | VARCHAR (18) | The unique ID of the provider who is the Inpatient reconciliation verbal order communicator for this event. This column is frequently used to link to the CLARITY_SER table. |
| REC_VRB_SIGNER_ID | VARCHAR (18) | The unique ID of the provider who is the Inpatient reconciliation verbal order signer for this event. This column is frequently used to link to the CLARITY_SER table. |
| REC_VRB_ORD_MODE_C | INTEGER |  |
| REC_ORD_PROV_ID | VARCHAR (18) | The unique ID of the provider who is the Inpatient reconciliation ordering provider for this event. This column is frequently used to link to the CLARITY_SER table. |
| REC_PROC_AUTH_ID | VARCHAR (18) | The unique ID of the provider who is the Inpatient reconciliation procedure authorizing provider for this event. This column is frequently used to link to the CLARITY_SER table. |
| REC_MED_AUTH_ID | VARCHAR (18) | The unique ID of the provider who is the Inpatient reconciliation medication authorizing provider for this event. This column is frequently used to link to the CLARITY_SER table. |
| REC_PROC_MSG_RCP_ID | VARCHAR (18) | The unique ID of the provider who is the Inpatient reconciliation procedure cosign message recipient for this event. This column is frequently used to link to the CLARITY_SER table. |
| REC_MED_MSG_RCP_ID | VARCHAR (18) | The unique ID of the provider who is the Inpatient reconciliation medication cosign message recipient for this event. This column is frequently used to link to the CLARITY_SER table. |
| REC_IS_PROC_HOSP_YN | VARCHAR (1) |  |
| REC_IS_MED_HOSP_YN | VARCHAR (1) |  |
| REC_VERB_ORD_CMT | VARCHAR (508) | The comments entered by the user who placed the Inpatient reconciliation verbal order associated with the event. |
| REC_ADMIT_STATUS_C | INTEGER |  |
| IP_REC_NOTE_ID | VARCHAR (254) | The unique ID of the order reconciliation (process of reviewing a orders when the patient moves to another level or area of care) note that is the associated with this event. |
| EVENT_LOG_ID | VARCHAR (18) | The unique ID of the surgical log that is associated with this event. This column is frequently used to link to the OR_LOG table. |
| EVENT_SUPPLY_ID | VARCHAR (18) | The unique ID of the supply that is associated with "supply used" events generated in Cupid "add supply" workflows. This column should be used to link to the OR_SPLY table. |
| EVENT_INI_RECORD_ID | VARCHAR (254) | The master file and ID of the source of a duplicate procedure alert event. For example, this item usually holds LDG-ID (the ID of the procedure duplicate group used) or EAP-ID (the ID of the procedure used). |
| EVENT_CONTEXT | VARCHAR (1024) | For some events, this column holds the context of the event. Lab Ordered events might store the order ID here. Duplicate procedure alert events might store information on specific user actions in response to the alert. |
| SOURCE_PX_ID | NUMERIC (18,0) | The unique ID of the source procedure that is associated with this duplicate procedure check. |
| SOURCE_PX_INFO | VARCHAR (254) | Detailed information about the duplicate procedure checked in SOURCE_PX_ID. |
| MATCH_PX_ID | NUMERIC (18,0) | The unique ID of the matched procedure that is associated with this duplicate procedure check. |
| MATCH_PX_INFO | VARCHAR (254) | Detailed information about the duplicate procedure checked in MATCH_PX_ID. |
| EVENT_SIGN_OFF_ID | NUMERIC (18,0) | The record that contains all the sign off information for this event. |
| OB_DEL_RECORD_ID | NUMERIC (18,0) | Store delivery record ID for OB events. This column can be linked to HSB master file - column SUMMARY_BLOCK_ID in OB_HSB_DELIVERY table. |
| DEPT_SCORE | NUMERIC (18,2) | Stores the numeric department score for department-specific events records. When a department scoring system is coordinated with a department event, the score calculated is saved in this item. It groups the score to the specific event instant, type, etc. from which the score was calculated. |
| STAFF_ROLE_C | VARCHAR (66) |  |
| STAFF_IS_ATTN_YN | VARCHAR (1) |  |
| LINKED_IEV_REC_ID | VARCHAR (18) | When linking two events, this item holds the record ID of the linked event. Use this in combination with the line number. |
| LINKED_IEV_LINE | INTEGER | When linking two events, this item holds the line number of the linked event within its respective record. Use this in combination with the record ID. |
| EVENT_TYPE_VERSION | NUMERIC (18,2) | If the data model for a particular event type changes, this item can be used to say which version of the data model is being used. Assume that blank is version 1. The version number only has meaning in relation to EVENT_TYPE. |
| EVENT_OWNER_ID | VARCHAR (18) | Stores the owner of the event. |
| PEND_ACTIVE_C | INTEGER |  |
| PEND_STATUS_C | INTEGER |  |
| PEND_RESTORED_BY_ID | VARCHAR (18) | Unique ID of the user who restored the pended orders. |
| PEND_RESTORED_DTTM | DATETIME (UTC) | Instant the pended orders were restored. |
| PEND_DELETED_BY_ID | VARCHAR (18) | Unique ID of the user who deleted pended orders. |
| PEND_DELETED_I_DTTM | DATETIME (UTC) | The instant pended orders were deleted. |
| PEND_COMMENT | VARCHAR (255) | User or autogenerated comment about the pended orders. |
| PEND_CHANGE_COUNT | INTEGER | Count of number of changes from a user perspective (some actions will not count as changes) |
| PEND_INSTANT_DTTM | DATETIME (UTC) | Instant that the pended orders were created. |
| PEND_CREATE_TYPE_C | INTEGER |  |
| EVENT_SOURCE_CSN_ID | NUMERIC (18,0) | This item contains the source CSN associated with a filed event. In the case of an event filed to an admission due to a redirected appointment, this contains the appointment contact. |
| EVENT_OVRIDE_RSN_C | INTEGER |  |
| EVENT_LABEL | VARCHAR (500) | The label for the value associated with an event. |
| EVENT_VALUE | VARCHAR (4000) | The value associated with an event. |
| FULLY_STAFF_YN | VARCHAR (1) |  |
| NOTIFY_STATUS_C | INTEGER |  |
| NOTIFY_PND_STATUS_C | INTEGER |  |
| AN_LINKED_EVENT_ID | VARCHAR (18) | Stores the record ID of an event that is linked to another Anesthesia event. |
| AN_LINKED_EVENT_LINE | INTEGER | When linking an Anesthesia event to another event, this item holds the line number of the linked event within its respective record. |
| ED_C_CLIENT_SRC_C | INTEGER |  |
| CT_EVENT_FILED_BY_C | VARCHAR (66) |  |
| ALLOW_UPD_PROV_ON_TRANS_YN | VARCHAR (1) |  |
| TRANSPORT_ID | NUMERIC (18,0) | This item stores the ID of the transport request that triggered the event, if applicable. |
| TXPORT_HLR_ID | NUMERIC (18,0) | The unique ID of the logistics patient transport request (HLR) that triggered the event. |
| EVENT_ORIGIN_C | INTEGER |  |
| RX_REQUEST_TYPE_C | INTEGER |  |
| RX_REQUEST_PHARMACY_ID | NUMERIC (18,0) | If this event represents orders created from an incoming Rx request, this indicates the pharmacy that requested the medications. |
| RX_REQUEST_VIEWED_YN | VARCHAR (1) |  |
| TRANSFER_DEST_DEPT_ID | NUMERIC (18,0) | The department where the patient is expected to reside once they are admitted or transferred (including discharge-readmits and transferring to another facility). |
| EVENT_SOURCE_C | VARCHAR (66) |  |
| REC_ROLE_ADMIT_USERROL_C | INTEGER |  |
| REC_ROLE_ADMIT_STATUS_C | INTEGER | Surrogate key used to uniquely identify rows in this (and only this) table on Cogito Cloud only, do not assume the surrogate key in this table will correspond to the surrogate key in another table |
| DISCHARGE_NAV_CONFIG_ID | NUMERIC (18,0) | Stores the Navigator Configuration for the Discharge Review section that was used when filing a Discharge Ord Rec event. |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| B-TREE INDEX | EIX_EDIEVEVENTINFO_EVTDEPTID | EVENT_DEPT_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_EDIEVEVENTINFO_EVTUSERID | EVENT_USER_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_EDIEV_TYPE_LINE | EVENT_TYPE | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_EDIEV_TYPE_LINE | EVENT_ID | 2 | Yes | Yes |  |
| B-TREE INDEX | EIX_EDIEV_TYPE_LINE | LINE | 3 | Yes | Yes |  |
| B-TREE INDEX | EIX_ED_IEV_EVENT_INFO_LOG_ID | EVENT_LOG_ID | 1 | Yes | Yes |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | EVENT_ID | ED_IEV_PAT_INFO | EVENT_ID | Unknown | No | No |  |
| 1 | EVENT_ID | IP_MAR_BARCODE_ITM | EVENT_ID | Unknown | No | No |  |
| 3 | EVENT_TYPE | ED_EVENT_TMPL_INFO | RECORD_ID | Unknown | No | No |  |
| 8 | EVENT_USER_ID | CLARITY_EMP | USER_ID | Unknown | No | No |  |
| 8 | EVENT_USER_ID | CLARITY_EMP_2 | USER_ID | Unknown | No | No |  |
| 8 | EVENT_USER_ID | CLARITY_EMP_3 | USER_ID | Unknown | No | No |  |
| 8 | EVENT_USER_ID | CLARITY_EMP_4 | USER_ID | No | No | No |  |
| 8 | EVENT_USER_ID | CLARITY_EMP_DEMO | USER_ID | No | No | No |  |
| 8 | EVENT_USER_ID | EMP_BASIC_INFO | USER_ID | No | No | No |  |
| 8 | EVENT_USER_ID | EMP_DOC_SETTINGS | USER_NUMBER_ID | No | No | No |  |
| 8 | EVENT_USER_ID | F_RX_USER | USER_ID | Unknown | Unknown | No |  |
| 8 | EVENT_USER_ID | IB_MESSAGE_SETTINGS | USER_ID | No | No | No |  |
| 8 | EVENT_USER_ID | LOGIN_INFO | USER_NUMBER_ID | No | No | No |  |
| 8 | EVENT_USER_ID | QC_RESULTS_REVIEW | USER_NUMBER_ID | No | No | No |  |
| 8 | EVENT_USER_ID | USER_SIDEBAR_RPT | USER_NUMBER_ID | Unknown | No | No |  |
| 8 | EVENT_USER_ID | V_CUBE_D_USER | USER_ID | Unknown | Unknown | No |  |
| 8 | EVENT_USER_ID | V_CUBE_RX_USER | USER_ID | Unknown | Unknown | No |  |
| 10 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 10 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 10 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 11 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 11 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 11 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 12 | EVENT_DEPT_ID | BH_DEP | DEPARTMENT_ID | No | No | No |  |
| 12 | EVENT_DEPT_ID | CLARITY_DEP | DEPARTMENT_ID | No | No | No |  |
| 12 | EVENT_DEPT_ID | CLARITY_DEP_2 | DEPARTMENT_ID | No | No | No |  |
| 12 | EVENT_DEPT_ID | CLARITY_DEP_3 | DEPARTMENT_ID | No | No | No |  |
| 12 | EVENT_DEPT_ID | CLARITY_DEP_4 | DEPARTMENT_ID | No | No | No |  |
| 12 | EVENT_DEPT_ID | CLARITY_DEP_5 | DEPARTMENT_ID | No | No | No |  |
| 12 | EVENT_DEPT_ID | CLARITY_DEP_MYC | DEPARTMENT_ID | No | No | No |  |

_(592 total; showing first 30)_
