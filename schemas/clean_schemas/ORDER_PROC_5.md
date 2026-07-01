# ORDER_PROC_5

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=ORDER_PROC_5

## Description

The ORDER_PROC_5 table enables you to report on the procedures ordered in the clinical system. This procedure table has the same basic structure as ORDER_PROC, but was created as a fifth table to prevent ORDER_PROC_4 from getting any larger.

**Overflow table** for ORDER_PROC (102 cols). Contains additional columns for the same records — join on the shared primary key column.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | ORD |
| Release Version | Rel 2017 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| ORDER_ID | NUMERIC (18,0) | The unique identifier for the order record. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| CC_TEX_RECIPIENT | VARCHAR (254) | Stores free text of CC recipient. This is used to store the CC recipient for a result that has been received on the incoming interface. This item stores the recipient if it is not an SER or EAF record. Also see items 2133 and 2134. Results Routing does not consider this item as it is only used for audit trail purposes. |
| PRIME_DEP_RECIPIENT_ID | NUMERIC (18,0) | This item stores the primary recipient if it is a DEP record. This is used to store the primary recipient for a result that has been received on the incoming interface. Results Routing does not consider this item as it is only used for audit trail purposes. |
| CC_DEP_RECIPIENT_ID | NUMERIC (18,0) | This item stores the CC recipient if it is a DEP record. This is used to store the CC recipient for a result that has been received on the incoming interface. Results Routing does not consider this item as it is only used for audit trail purposes. |
| FAST_DECISION_C | INTEGER |  |
| FUTURE_RELATIVE_EXPECTED_DT_C | INTEGER |  |
| FUTURE_EXPECTED_DATE_COMMENT_C | INTEGER |  |
| FUTURE_EXPECTED_DATE_DETAILS | VARCHAR (254) | This item holds the free-text details entered if the future expected date comment (FUTURE_EXPECTED_DATE_COMMENT_C) is "Other (Specify)". |
| MODIFY_TRACK_C | VARCHAR (1) |  |
| POOL_WAS_MANUAL_YN | VARCHAR (1) |  |
| INCOMPLETE_CHILD_ORDERS | INTEGER | Store the number of child orders which have not yet reached completed/canceled status. meaning they are either not yet released or are currently active. |
| ORDER_INST_UTC_DTTM | DATETIME (UTC) | The instant when the order was created in UTC. |
| MINUTES_BTWN_SCHED_AND_COLL | INTEGER | The number of minutes between the scheduled and collected instants for a lab. Negative values indicate early collection. |
| APPT_WINDOW_START_TIME | DATETIME (Local) | This is the start of the appointment window for the preferred appointment window. |
| MYC_TKT_GEN_STAT_C | INTEGER |  |
| OVERREAD_SRC_ORD_ID | NUMERIC (18,0) | Stores the order record ID that is marked for imaging overread. |
| APPT_WINDOW_END_TIME | DATETIME (Local) | This is the end of the appointment window for the preferred appointment window. |
| PROC_ESTIMATE_ID | NUMERIC (18,0) | A link to a patient estimate record that contains patient cost estimate information for procedure orders. |
| SHOULD_GENERATE_PAT_EST_YN | VARCHAR (1) |  |
| OSVA_SRV_TYPE_C | INTEGER |  |
| OSVA_CAN_ARCHIVE_YN | VARCHAR (1) |  |
| OSVA_CAN_VIEW_C | INTEGER |  |
| OSVA_START_DATE | DATETIME | The authorized start date to view service events if the service provider is authorized to view documents for a specific date range. |
| OSVA_END_DATE | DATETIME | The authorized end date to view service events if the service provider is authorized to view documents for a specific date range. |
| FINANCIAL_CLEARANCE_STATUS_C | INTEGER |  |
| FINANCIAL_CLEARANCE_UTC_DTTM | DATETIME (UTC) | Records the UTC instant an order was financially cleared |
| REC_FROM_OUTSIDE_C | INTEGER |  |
| SENDING_ORG_ID | NUMERIC (18,0) | The sending organization that provided the information to create the reconciled outside order |
| FNDAVTR_DOC_INFO_ID | VARCHAR (18) | Stores the Document ID of the image for the findings avatar |
| FNDAVTR_INREPORT_YN | VARCHAR (1) |  |
| IMG_PUBLIC_RSLT_DTTM | DATETIME (Local) | The instant in local time at which the imaging result was made public, as defined by the order's study status (e.g. physician finalized the exam) as configured by the imaging analyst team (I RDF 192). |
| IMG_EXAM_PAT_CLASS_C | 52138 |  |
| ORDER_RECEIVED_DTTM | 52355 | The date and time the order was received. |
| OUTSOURCED_SVC_AUTHORIZED_AMT | NUMERIC (18,2) | The amount for which the financial commitment is authorized. |
| OUTSOURCED_SVC_PROV_NAME | VARCHAR (254) | The service provider name for the financial commitment. |
| OUTSOURCED_SVC_PROV_ADDRESS | VARCHAR (254) | The service provider address for the financial commitment. |
| ACTV_EXCLUDE_FROM_CDS_REASON_C | INTEGER |  |
| ACTV_EXCLUDE_FROM_CDS_UTC_DTTM | DATETIME (UTC) | The instance in UTC when the "Exclude From Decision Support" was updated on the order record. |
| ACTV_EXCLUDE_FROM_CDS_DTTM | DATETIME (Local) | The instance when the "Exclude From Decision Support" was updated on the order record. |
| LEAVE_TYPE_C | INTEGER |  |
| LEAVE_START_DATE | DATETIME | Start date of the medical leave. |
| LEAVE_END_DATE | DATETIME | End date of the medical leave. |
| LEAVE_DURATION | INTEGER | Duration of the medical leave in days. |
| LEAVE_LIGHTDUTY_YN | VARCHAR (1) |  |
| LEAVE_LIGHTDUTY_START_DATE | DATETIME | Start date of the light duty period. |
| LEAVE_LIGHTDUTY_END_DATE | DATETIME | End date of the light duty period. |
| LEAVE_LIGHTDUTY_DURATION | INTEGER | Duration of the light duty period in days. |
| LEAVE_EXCUSED_ACTIVITIES_YN | VARCHAR (1) |  |
| LEAVE_EXCUSED_START_DATE | DATETIME | Start date of the excused activities period. |
| LEAVE_EXCUSED_END_DATE | DATETIME | End date of the excuse period. |
| LEAVE_EXCUSED_DURATION | INTEGER | Duration of the excuse period in days. |
| LEAVE_EXCUSED_COMMENTS | VARCHAR (508) | Comments about the excused activities for the excuse period. |
| DELIVERY_REQUEST_ORDER_ID | NUMERIC (18,0) | The order ID of the blood component order this order record is requesting a delivery from. |
| DELIVERY_REQUEST_AMOUNT | INTEGER | The number of units being requested from the blood component order record. |
| ORIGINATING_ORD_ID | NUMERIC (18,0) | This column contains the originating order ID. It is related conceptually to ORDER_PROC_2.ORIGINAL_ORDER_ID, but rather than pointing back to the previous order ID at the same level in the order tree hierarchy, this column will point back to the initial order created by the ordering end user. Use this column to find out information about the initial order, or to determine if an order went through a change procedure workflow which generated new order records. |
| PROC_CHANGED_YN | VARCHAR (1) |  |
| ACTIVE_PROC_TYPE_C | INTEGER |  |
| DELIVERY_REQUEST_UNIT_C | INTEGER |  |
| BILL_AREA_ID | NUMERIC (18,0) | The bill area this order is associated with. |
| LINK_ECONSULT_ENC_CSN | NUMERIC (18,0) | Stores the contact serial number for the encounter associated with this e-consult order. This item is only used when the e-consult order is placed from EpicCare Link or EpicWeb. |
| ADT_ORDER_TYPE_C | INTEGER |  |
| SOURCE_ORG_ID | NUMERIC (18,0) | This item holds the originating organization ID for this order. Most frequently this will be the organization that the order exists on, but it is possible to receive external orders, created elsewhere. |
| BI_PRELIM_OUTCOME_C | INTEGER |  |
| PARENT_ORD_INST_DTTM | DATETIME (Local) | The instant when the parent order was created, local to this order's time zone. |
| RAD_EXAM_END_UTC_DTTM | DATETIME (UTC) | The date and time an order's exam is ended in the Universal Time Coordinated (UTC) format. |
| LUNG_CANCER_HX_YN | VARCHAR (1) |  |
| PAT_AGE_AT_EXAM | INTEGER | The age of the patient (in years) as of the date of the exam. If the exam has ended, this will be the age as of end exam. If not, this will be the age as of the scheduled appointment date. If an appointment has not been scheduled for this exam, this value will be null. |
| PRIORITIZED_UTC_DTTM | DATETIME (UTC) | Stores the prioritized instant for the result in UTC |
| RESULT_UPDATE_UTC_DTTM | DATETIME (UTC) | Stores the last update instant for a result in UTC |
| CREATED_BY_APPT_REQUEST_ID | NUMERIC (18,0) | Contains the parent request responsible for creating this order. |
| ORD_REFLEX_SCHEDEVENT_C | INTEGER |  |
| IS_ORD_RES_NET_YN | VARCHAR (1) |  |
| PROC_SVC_TYPE_CODE_C | INTEGER |  |
| PERFORMED_IN_ISO_YN | VARCHAR (1) |  |
| RFL_FORMALITY_C | INTEGER |  |
| RFL_REQUESTING_AUTHORITY_C | INTEGER |  |
| RFL_FIRST_APPOINTMENT_BY_DATE | DATETIME | The date that the first appointment for the referral should occur by. |
| RFL_LIVING_SITUATION_C | INTEGER |  |
| RFL_CHILD_SERVICE_C | INTEGER |  |
| RFL_PARENTAL_RESP_C | INTEGER |  |
| RFL_CONSENT_TO_TREAT_STAT_C | INTEGER |  |
| RFL_CASE_WORKER_NAME | VARCHAR (508) | The case manager of the child psychology case for this psychology referral order. |
| LUNG_OUTCOME_C | INTEGER |  |
| MAM_INDICATION_C | INTEGER |  |
| ORD_END_DATE_REAL | FLOAT | The latest contact date for the order in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| HAS_LAB_SPEC_YN | VARCHAR (1) |  |
| HAS_RSLT_CNCT_YN | VARCHAR (1) |  |
| HAS_CORR_YN | VARCHAR (1) |  |
| LAB_REDRAW_REASON_C | INTEGER |  |
| PANEL_RELEASE_DTTM | DATETIME (Local) | If this order is a performable order on a test panel, this item stores the local date and time when the associated orderable was released. This column will only be populated for performable orders on test panels. It will not be populated for the orderable order on test panels. |
| PANEL_RELEASE_UTC_DTTM | DATETIME (UTC) | If this order is a performable order on a test panel, this item contains the UTC date and time when the associated orderable was released. This column will only be populated for performable orders on test panels. It will not be populated for the orderable order on test panels. |
| LAST_RSLT_LAB_ID | NUMERIC (18,0) | The unique ID of the resulting lab from the last contact where the procedure result status is not null. |
| PROC_COND_GRP_C | INTEGER |  |
| PROTCL_STAT_UTC_DTTM | DATETIME (UTC) | This is the instant of the schedule state of the protocol for the order was set. |
| MAM_TECH_IMG_DOC_REV_DTTM | DATETIME (UTC) | Stores the instant when the last technologist image documentation was reviewed. |
| MAM_TECH_IMG_DOC_REV_USER_ID | VARCHAR (18) | Stores the user ID of the last person to review the technologist imaging documentation. |
| NMD_3_MAM_INDICATION_C | INTEGER |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ORDER_ID | ADT_ORDERS_ERRORS | ORDER_ID | No | No | No |  |
| 1 | ORDER_ID | ADT_ORDER_INFORMATION | ORDER_ID | No | No | No |  |
| 1 | ORDER_ID | APPT_REQUEST | REQUEST_ID | No | No | No |  |
| 1 | ORDER_ID | CL_ORD_FST_LST_SCH | ORDER_ID | No | No | No |  |
| 1 | ORDER_ID | DENT_ORD_NOADD | ORDER_ID | No | No | No |  |
| 1 | ORDER_ID | DUPMED_DISMISS_HH_INFO | ORDER_ID | No | No | No |  |
| 1 | ORDER_ID | ENDOSCOPY_METRICS | ORDER_ID | Unknown | No | No |  |
| 1 | ORDER_ID | EXTERNAL_ORDER_INFO | ORDER_ID | No | No | No |  |
| 1 | ORDER_ID | F_IMG_STUDY | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_ID | F_IP_HSP_SUM_ORDER | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_ID | F_LAB_ORDERS | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_ID | F_MU_OBJ_EH_PLACED_ORDER | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_ID | F_MU_OBJ_EH_RESULTD_ORDER | ORDER_PROC_ID | Unknown | Unknown | No |  |
| 1 | ORDER_ID | F_ONC_PRIOR_AUTH_ORDERS | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_ID | F_OPIOID_ORDERS | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_ID | F_RX_ORDER | ORDER_MED_ID | Unknown | Unknown | No |  |
| 1 | ORDER_ID | HH_MED_ORD_IN_POC_DETAIL | ORDER_MED_ID | No | No | No |  |
| 1 | ORDER_ID | HV_ORDER_PROC | ORDER_PROC_ID | Unknown | No | No |  |
| 1 | ORDER_ID | MED_DETAILS_EXT_ORD | ORDER_ID | No | No | No |  |
| 1 | ORDER_ID | MERCHANDISE_ORDER_INFO | ORDER_ID | Yes | No | No |  |
| 1 | ORDER_ID | MU_EH_QRDA_I_ORDER | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_ID | ORDERS | ORDER_ID | No | No | No |  |
| 1 | ORDER_ID | ORDER_AUTH_INFO | ORDER_ID | No | No | No |  |
| 1 | ORDER_ID | ORDER_MED | ORDER_MED_ID | Unknown | No | No |  |
| 1 | ORDER_ID | ORDER_MEDINFO | ORDER_MED_ID | Unknown | No | No |  |
| 1 | ORDER_ID | ORDER_MED_2 | ORDER_ID | Unknown | No | No |  |
| 1 | ORDER_ID | ORDER_MED_3 | ORDER_ID | Unknown | No | No |  |
| 1 | ORDER_ID | ORDER_MED_4 | ORDER_ID | Unknown | No | No |  |
| 1 | ORDER_ID | ORDER_MED_5 | ORDER_ID | Unknown | No | No |  |
| 1 | ORDER_ID | ORDER_MED_6 | ORDER_MED_ID | Unknown | No | No |  |

_(595 total; showing first 30)_
