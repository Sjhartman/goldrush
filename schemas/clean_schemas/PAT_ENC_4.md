# PAT_ENC_4

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=PAT_ENC_4

## Description

This table supplements the PAT_ENC, PAT_ENC_2, and PAT_ENC_3 tables. It contains additional information related to patient encounters or appointments.

**Overflow table** for PAT_ENC (143 cols). Contains additional columns for the same records — join on the shared primary key column.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | EPT |
| Release Version | Rel 2012 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| PAT_ENC_CSN_ID | NUMERIC (18,0) | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| PAT_ID | VARCHAR (18) | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| PAT_ENC_DATE_REAL | FLOAT | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| CONTACT_DATE | DATETIME | The date of this contact in calendar format. |
| CM_CT_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this contact. This is only populated if you use IntraConnect. |
| UNAV_TIME_RSN_C | INTEGER |  |
| OVBK_OVR_USER_ID | VARCHAR (18) | The unique ID of the user who authorized the appointment to be overbooked. |
| CANC_CHKIN_USER_ID | VARCHAR (18) | The unique ID of the user who canceled check in. If check in is canceled more than once, this will store the ID of the last user to do so. Note that cancel check in may also be used to cancel a check-out. Actions of this type will also be regarded. That is, the ID of the user performing the most recent cancel check in action will be stored here, whether the Cancel Check In functionality is used on an Arrived or Completed appointment. |
| RESEARCH_ID *(deprecated)* | VARCHAR (18) | The unique ID of the research study code associated with this research dummy patient.   This over-time column has been deprecated and replaced with a no-add column PATIENT_4.RESEARCH_ID. Reports should be updated immediately to use the new column. |
| RESCHED_FROM_DTTM | 7505 | The date and time of the canceled appointment from which this appointment was rescheduled. |
| FAMILY_SIZE | INTEGER | The number of members in the patient's family. |
| FAMILY_INCOME | NUMERIC (18,2) | The income for the patients family. |
| VISIT_NUMBER | VARCHAR (32) | The visit number for the given contact. |
| PAT_CNCT_IND_C | VARCHAR (66) |  |
| DENTAL_STUDENT_ID | VARCHAR (18) | The unique ID of the provider who is the dental student associated with the patient. |
| LOC_VISIT_ID | NUMERIC (18,0) | The unique ID of the location that is associated with the visit. |
| COPAY_NOT_COVERED_C | INTEGER |  |
| COPAY_COLL_FLAG_YN | VARCHAR (1) | The copay collected flag that indicates whether a copay was collected from the patient encounter. |
| COPAY_COLL_PERSON | VARCHAR (127) | The unique ID number of the person who collected the patient's copay for the encounter. |
| COPAY_WAIVE_RSN_C | INTEGER |  |
| COPAY_MIN_VALUE | NUMERIC (18,2) | The value of the minimum copay. |
| COPAY_RECEIPT_NUM | VARCHAR (127) | The receipt number of the copay collected. |
| BEN_ADJ_COINS_AMT | NUMERIC (18,2) | The adjudicated coinsurance amount for the visit calculated by the benefits engine. |
| BEN_ADJ_DEDUCT_AMT | NUMERIC (18,2) | The portion of the self-pay amount applied to the deductible for the visit. |
| PAT_HOMELESS_YN | VARCHAR (1) |  |
| PAT_HOMELESS_TYP_C | VARCHAR (66) |  |
| PERCENTAGE_OF_FPL | NUMERIC (18,2) | Indicates where the patient falls on the federal poverty level as a percentage. |
| RFL_REQ_PLAN *(deprecated)* | INTEGER |  |
| MSG_RECEIVED_DTTM | 19500 | The date and time the encounter creation In Basket message was received. |
| CALLED_IN_FROM_C | INTEGER |  |
| TOBACCO_USE_VRFY_YN | VARCHAR (1) | This column indicates whether the patient's tobacco usage has been verified. A Y indicates the usage was verified. An N or null indicates the tobacco usage was not verified. It extracts a virtual item, which is calculated using EPT-19202. |
| CR_TX_TYPE_C | INTEGER |  |
| ORIG_ENC_CSN | NUMERIC (18,0) | Holds the CSN of the encounter this Remote Consult encounter is responding to. |
| HEALTH_INFO_ROI_ID | VARCHAR (254) | The unique ID of the created ROI request for an Electronic Copy of Health Information. |
| DISCH_INSTR_REQ_YN | VARCHAR (1) |  |
| DISCH_INSTR_ROI_ID | VARCHAR (254) | The unique ID of the created ROI request for an Electronic Copy of Discharge Instructions. |
| NOSHOW_PH_RSLT_C | INTEGER |  |
| PHYS_BP_COMMENTS | VARCHAR (260) | This column contains the comments entered for the last recorded blood pressure for this visit. |
| PHYS_TEMP_COMMENTS | VARCHAR (260) | This column contains the comments entered for the last recorded temperature for this visit. |
| PHYS_TEMPSRC_COMNTS | VARCHAR (260) | This column contains the comments entered for the last recorded temperature source for this visit. |
| PHYS_PULSE_COMMENTS | VARCHAR (260) | This column contains the comments entered for the last recorded pulse for this visit. |
| PHYS_WEIGHT_COMNTS | VARCHAR (260) | This column contains the comments entered for the last recorded weight for this visit. |
| PHYS_HEIGHT_COMNTS | VARCHAR (260) | This column contains the comments entered for the last recorded height for this visit. |
| PHYS_RESP_COMMENTS | VARCHAR (260) | This column contains the comments entered for the last recorded respirations for this visit. |
| PHYS_SPO2_COMMENTS | VARCHAR (260) | This column contains the comments entered for the last recorded oxygen saturation level (SpO2) for this visit. |
| PHYS_PF_COMMENTS | VARCHAR (260) | This column contains the comments entered for the last recorded peak flow for this visit. |
| INTERPRT_ASGN_CMT | VARCHAR (254) | Comments regarding the interpreter assigned to the patient's contact. |
| PAT_HOUSING_STAT_C | INTEGER |  |
| BCRA_AGE | INTEGER | The patient's age at the time of the risk assessment. |
| BCRA_MENARCHE_AGE_C | INTEGER |  |
| BCRA_FST_LIVBIRTH_C | INTEGER |  |
| BCRA_FST_DEG_REL_C | INTEGER |  |
| BCRA_NUM_BIOPSY_C | INTEGER |  |
| BCRA_ATYP_HYPLSA_C | INTEGER |  |
| BCRA_RACE_C | INTEGER |  |
| DO_NOT_DFLT_PHRM_YN | VARCHAR (1) |  |
| VIS_NEW_TO_SYS_YN | VARCHAR (1) |  |
| VIS_NEW_TO_DEP_YN | VARCHAR (1) |  |
| VIS_NEW_TO_PROV_YN | VARCHAR (1) |  |
| VIS_NEW_TO_SPEC_YN | VARCHAR (1) |  |
| VIS_NEW_TO_SERV_AREA_YN | VARCHAR (1) |  |
| COLOR_FLAG *(deprecated)* | VARCHAR (254) | *** Deprecated *** In table PAT_ENC_4, the column COLOR_FLAG (EPT/17655) has been deprecated. The deprecated column's content/data is no longer available since it is no longer populated in Chronicles. |
| LB_ENC_START_DT | DATETIME | This identifies the start date of a Lab Requisition encounter. |
| LB_ENC_END_DT | DATETIME | This identifies the end date of a Lab Requisition encounter. |
| WAITING_LIST_ID | NUMERIC (18,0) | The unique ID of the Waiting List record associated with this encounter. This column can be used to link to the WAITING_LIST_INFO table. |
| SUBMITTER_ID | NUMERIC (18,0) | The submitting organization that the results for the lab orders on this encounter should be sent to. |
| BILL_TO_SUBMITTER_C | INTEGER |  |
| SUBMITTER_ACCT_ID | NUMERIC (18,0) | The submitter account to be used when billing laboratory procedures. |
| DUTCH_LBZ_MAINPX_ID | NUMERIC (18,0) | The unique ID of the main LBZ procedure record for the patient encounter. This column is frequently used to link to the CLARITY_EAP_OT table. |
| DUTCH_LBZ_CURSTAT_C | INTEGER |  |
| ADMIN_CAT_CODE_C | INTEGER |  |
| UK_RESIDENT_12M_YN | VARCHAR (1) |  |
| STAGE_2_OUTCOME_C | INTEGER |  |
| STAGE_2_DATE | DATETIME | This is the date that a Stage 2 Interview was conducted. |
| CAB_UBRN | VARCHAR (16) | The Choose and Book unique booking reference number. This identifier will be dual stored on the referral record linked to this appointment (item RFL 900). Only appointments interfaced from Choose and Book will populate this field. |
| CAB_USRN | VARCHAR (36) | The Choose and Book unique slot reference number. This is the identifier of the slot that was created in Epic and sent to Choose and Book and subsequently used by Choose and Book to create this appointment. |
| APPT_CREATION_UTC | DATETIME (UTC) | Stores the instant that an appointment was created in UTC. This item is set once when the appointment is created and is not modified at all during the life of the appointment. |
| APPT_ARRIVAL_MINUTES | INTEGER | The number of minutes before the appointment time a patient should arrive by. |
| APPT_ARRIVAL_DTTM | DATETIME (Attached) | This column stores the time by which a patient should arrive for his or her appointment. |
| DUTCH_LBZ_ENC_TYP_C | INTEGER |  |
| ALL_MEDS_ACTD_ON_YN | VARCHAR (1) |  |
| EXTMED_RECONCILD_YN | VARCHAR (1) |  |
| LB_BLNG_ENC_SRVC_DT | DATETIME | This identifies the service date of the Billing encounter used for Lab Billing. The date is in the time zone of the lab department that created the encounter. |
| ECHKIN_STATUS_C | INTEGER |  |
| PB_VISIT_HAR_ID | NUMERIC (18,0) | The hospital account record used by the Professional Billing system for a given contact. |
| APPT_NUDGE_STATUS_C | INTEGER |  |
| APPT_NUDGE_STRT_OFF | INTEGER | If the current appointment was nudged, this column stores the difference between the new start time and the original start time. For example, if an 8:05 apopintment was nudged to 8:00, this column would show "-5".  This column will only be populated if the appointment nudge feature changed the appointment start time. |
| APPT_NUDGE_LEN_OFF | INTEGER | If the current appointment was nudged, this column stores the difference between the new appointment length and the original appointment length. For example, if a 30 minute appointment was nudged to 20 minutes, this column would show "-10".  This column will only be populated if the appointment nudge feature changed the appointment length. |
| EXPORT_TO_IRIS_C | INTEGER |  |
| REF_HOSP_ID | NUMERIC (18,0) | This column stores the location that referred the patient for the current appointment.  This column will only be populated if your organization has chosen to gather this information during scheduling or registration. |
| TECHNICAL_REFERRAL_ID | NUMERIC (18,0) | The MassHealth technical referral associated with the encounter. |
| CR_CLIENT_REF_IDNT | VARCHAR (40) | Used to store the client ID returned by the copay reduction web service |
| CR_BENEFIT_REF_IDNT | VARCHAR (40) | The benefit reference ID number of the patient for the current encounter. |
| CR_MESSAGE_ENGLISH | VARCHAR (254) | The copay message returned by the web service in English. |
| CR_MESSAGE_SPANISH | VARCHAR (254) | The copay message returned by the web service in Spanish. |
| CR_QUERY_SENT_UTC_DTTM | DATETIME (UTC) | Instant the copay reduction web service query was sent to the server |
| CR_RESP_RECVD_UTC_DTTM | DATETIME (UTC) | Specifies the instant when the response to the copay reduction web service query was received |
| CR_QUERY_ERROR | VARCHAR (254) | Specifies the error received in the response to the query sent out to get the copay reduction for the current patient encounter. |
| COPAY_REDUCTION_AMT | NUMERIC (18,2) | The amount by which the copay should be reduced for the current visit |
| VIS_NEW_TO_LOC_YN | VARCHAR (1) |  |
| IS_ACDNT_RELATED_YN | VARCHAR (1) |  |
| RFL_REQ_BEN_PLAN_ID | NUMERIC (18,0) | REFERRAL REQUIRED PLAN. Contains ID from EPP record for benefit plan. |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| B-TREE INDEX | EIX_PAT_ENC_4_CONTACT | PAT_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_PAT_ENC_4_CONTACT | PAT_ENC_DATE_REAL | 2 | Yes | Yes |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | PAT_ENC_CSN_ID | ALT_ORD_PROV_SINGL | PAT_ENC_CSN_ID | Unknown | No | No |  |
| 1 | PAT_ENC_CSN_ID | AN_RELINK_INFO | PAT_ENC_CSN_ID | No | No | No |  |
| 1 | PAT_ENC_CSN_ID | DENT_ORTH_EXAM_NOTES | PAT_ENC_CSN_ID | No | No | No |  |
| 1 | PAT_ENC_CSN_ID | FAC_CHG_OVERRIDE | PAT_ENC_CSN_ID | No | No | No |  |
| 1 | PAT_ENC_CSN_ID | FAM_HX_PAT_ONLY | PAT_ENC_CSN_ID | No | No | No |  |
| 1 | PAT_ENC_CSN_ID | F_ED_ENCOUNTERS | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 1 | PAT_ENC_CSN_ID | F_HH_CERT_ATTRIBUTES | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 1 | PAT_ENC_CSN_ID | F_HH_OASIS_SINGLE | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 1 | PAT_ENC_CSN_ID | F_HH_OASIS_SINGLE_2 | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 1 | PAT_ENC_CSN_ID | F_HH_OASIS_SINGLE_3 | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 1 | PAT_ENC_CSN_ID | F_HH_OASIS_SINGLE_4 | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 1 | PAT_ENC_CSN_ID | F_HH_OASIS_SINGLE_5 | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 1 | PAT_ENC_CSN_ID | F_IBD_ADULT_FORM_ENC | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 1 | PAT_ENC_CSN_ID | F_IBD_FORM_RESP | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 1 | PAT_ENC_CSN_ID | F_IP_HSP_ADMISSION | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 1 | PAT_ENC_CSN_ID | F_IP_HSP_SEPSIS3 | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 1 | PAT_ENC_CSN_ID | F_IRIS_ENC | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 1 | PAT_ENC_CSN_ID | F_MU_OBJ_EH_ADMISSION | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 1 | PAT_ENC_CSN_ID | F_MU_QM_EH_2014_ED_VISIT | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 1 | PAT_ENC_CSN_ID | F_MU_QM_EH_2014_IP_ADMSN | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 1 | PAT_ENC_CSN_ID | F_QM_AMI | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 1 | PAT_ENC_CSN_ID | F_QM_CAC | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 1 | PAT_ENC_CSN_ID | F_QM_HBIPS | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 1 | PAT_ENC_CSN_ID | F_QM_HEART_FAILURE | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 1 | PAT_ENC_CSN_ID | F_QM_IMMUNIZATION | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 1 | PAT_ENC_CSN_ID | F_QM_PC_BABY | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 1 | PAT_ENC_CSN_ID | F_QM_PC_MOM | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 1 | PAT_ENC_CSN_ID | F_QM_PNEUMONIA | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 1 | PAT_ENC_CSN_ID | F_SCHED_APPT | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 1 | PAT_ENC_CSN_ID | HAUD_ENC | ENC_CSN | Unknown | Unknown | No |  |

_(482 total; showing first 30)_
