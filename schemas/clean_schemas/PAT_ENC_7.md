# PAT_ENC_7

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=PAT_ENC_7

## Description

This table supplements the PAT_ENC, PAT_ENC_2, PAT_ENC_3, PAT_ENC_4, PAT_ENC_5, and PAT_ENC_6 tables. It contains additional information related to patient encounters or appointments.

**Overflow table** for PAT_ENC (143 cols). Contains additional columns for the same records — join on the shared primary key column.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | EPT |
| Release Version | Rel November 2019 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| PAT_ENC_CSN_ID | NUMERIC (18,0) | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| PAT_ID | VARCHAR (18) | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| PAT_ENC_DATE_REAL | FLOAT | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| CONTACT_DATE | DATETIME | The date of this contact in calendar format. |
| CM_CT_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this contact. This is only populated if you use IntraConnect. |
| NOTIFY_REP_ADMSN_C | INTEGER |  |
| REP_NOTIFIED_C | INTEGER |  |
| NOTIFY_REP_COMMENTS | VARCHAR (508) | Information about notifying a patient's family or representative of their admission. |
| NOTIFY_PCP_ADMSN_C | INTEGER |  |
| PCP_NOTIFIED_C | INTEGER |  |
| NOTIFY_PCP_COMMENTS | VARCHAR (508) | Information about notifying a patient's PCP of their admission. |
| ROC_PLANNING_PAT_ENC_CSN_ID | NUMERIC (18,0) | Stores the unique contact serial number of the resumption of care planning contact linked to this contact |
| NUM_PREV_EPSD_C | INTEGER |  |
| PAT_QUESR_LAST_REASGN_UTC_DTTM | DATETIME (UTC) | Track the last instant the encounter was updated via the questionnaire reassignment batch job. |
| COULD_DIR_SCHED_C | INTEGER |  |
| COULD_OPEN_SCHED_C | INTEGER |  |
| COULD_TKT_SCHED_C | INTEGER |  |
| SPEC_ORD_RSLT_NOT_AUTO_RLS_YN | VARCHAR (1) |  |
| APPOINTMENT_SEARCH_START_DATE | DATETIME | The search start date chosen during scheduling. |
| RECENTLY_AT_SCHOOL_C | INTEGER |  |
| VAP_PROPOSAL_DTTM | DATETIME (Attached) | The last instant the visit auto pay proposal was updated, formatted with time zone attached. |
| VAP_PROPOSAL_USER_ID | VARCHAR (18) | The last user who updated the visit auto pay proposal. |
| VAP_PROPOSAL_OVERRIDE_YN | VARCHAR (1) |  |
| VAP_CONSENTED_AMT | NUMERIC (18,2) | The amount to which the guarantor consented as the visit auto pay arrangement for this visit. |
| VAP_SOURCE_C | INTEGER |  |
| VAP_PROPOSED_AMT | NUMERIC (18,2) | The proposed consent amount for visit auto pay for the encounter. |
| VAP_SOURCE_RULE_MSG | VARCHAR (254) | The patient rule error message for the rule this visit passed to propose visit auto pay (SSD-4841). If no visit auto pay was proposed by the system, this will be blank. |
| LMP_COMMENT | VARCHAR (254) | Free-text comments about the last menstrual period |
| CONTACT_NUM | INTEGER | The system-assigned number used to uniquely identify each of a given patient's encounters. |
| ABN_REQUIRED_YN | VARCHAR (1) |  |
| IS_ABN_SIGNED_C | VARCHAR (66) |  |
| MSP_IS_MEDICARE_HMO_C | VARCHAR (66) |  |
| REG_COMMENTS_DATE | DATETIME | The date corresponding to the comment in PAT_ENC_REG_CMT table for this encounter. |
| AUTO_MSG_DISABLED_YN | VARCHAR (1) |  |
| DONT_AUTO_LINK_YN | VARCHAR (1) |  |
| RSN_FOR_NO_INC_MSG_C | INTEGER |  |
| CHECKIN_AUD_DTTM | DATETIME (Attached) | The date and time of the system-audited check-in.  If a check-in was canceled or the appointment was checked in multiple times, this column will store the time of the first check-in action after the last cancel check-in action. If there was a cancel check-in action without a subsequent check-in action, this column will be null. This may or may not be more accurate than the user-editable time recorded by the CHECKIN_TIME column in PAT_ENC. |
| CHECKOUT_AUD_DTTM | DATETIME (Attached) | The date and time of the system-audited check-out.   If the check-out was canceled, this column will store the time of the first check-out action after the last cancel check-out action. If there was a cancel check-out action without a subsequent check-out action, this column will be null. This may or may not be more accurate than the user-editable time recorded by the CHECKOUT_TIME column in PAT_ENC. |
| SIGNIN_AUD_DTTM | DATETIME (Attached) | The date and time of the system-audited sign-in action.   If a sign-in was canceled or the appointment was signed in multiple times, this column will store the time of the first sign-in action after the last cancel sign-in action. If there was a cancel sign-in action without a subsequent sign-in action, this column will be null. This may or may not be more accurate than the user-editable time recorded by the SIGN_IN_TIME column in PAT_ENC.  Additionally, if the system is configured to automatically sign in walk-in appointments, a cancel check-in event will behave like a cancel sign-in event for walk-ins. |
| HAS_HORMONE_DATA_YN | VARCHAR (1) |  |
| NLP_CAPD_DISABLE_UTC_DTTM | DATETIME (UTC) | Stores the UTC instant of the first note that was prevented from being sent to NoteReader CDI because of encounter filtering. |
| ECHKIN_FORALL_ELIGIBLE_YN | VARCHAR (1) |  |
| MEDS_REQUEST_LWS_ID | VARCHAR (18) | This is the destination to use with the encounter primary pharmacy stored in EPT 17162. |
| PEND_LOC_RECORD_ID | NUMERIC (18,0) | Stores the patient location where a patient has been pre-assigned to. |
| SELF_ARR_ALLOW_C | INTEGER |  |
| ARR_ALLOW_ERR_C | INTEGER |  |
| EVISIT_SUBMITTED_DTTM | DATETIME (Local) | The instant in system local time at which the patient submitted the E-Visit.  If conversion 888449 has not completed, this column might not have data for some submitted E-Visits. Consider using V_PAT_ENC_EVISIT.EVISIT_SUBMITTED_DTTM instead, which will always have a submission time for all submitted E-Visits. Talk to your operational database administrator or Epic representative to determine whether the conversion has finished. |
| EVISIT_TURNAROUND_IN_MINUTES | INTEGER | The amount of time, in minutes, between when a patient submitted the E-Visit and when a provider signed the encounter. If the encounter is not an E-Visit, or if the E-Visit was not both submitted and signed, then this column will be NULL. |
| ENC_AUTH_UTC_DTTM | DATETIME (UTC) | The instant in UTC that the encounter was first authorized |
| ENC_AUTH_DTTM | DATETIME (Attached) | The local instant that the encounter was first authorized |
| ENC_TIME_APPT_AUTH_STATUS_C | INTEGER |  |
| INCL_PRIOR_AUTH_MTRC_YN | VARCHAR (1) |  |
| PRECERT_AUTHORIZATION_STATUS_C | INTEGER |  |
| ENC_TIME_PRECERT_AUTH_STATUS_C | INTEGER |  |
| APPT_PAT_TIME_ZONE_C | INTEGER |  |
| APPT_START_PAT_TZ_DTTM | DATETIME (Attached) | The start instant of the appointment in the time zone where the patient will be for virtual visits. |
| APPT_ARRIVAL_PAT_TZ_DTTM | DATETIME (Attached) | The arrival instant of the appointment in the time zone where the patient will be for virtual visits. |
| IS_VIDEO_VISIT_YN | VARCHAR (1) |  |
| IS_VIDEO_VISIT_SUCCESSFUL_YN | VARCHAR (1) |  |
| VIDEO_VISIT_FAILURE_REASON_C | INTEGER |  |
| CALCULATED_TELEHEALTH_MODE_C | INTEGER |  |
| PREGNANCY_INTENTION_C | INTEGER |  |
| PREGNANCY_COUNSELED_YN | VARCHAR (1) |  |
| BIRTH_CONTROL_COUNSELED_YN | VARCHAR (1) |  |
| RSN_NO_BCM_COUNSELING_C | INTEGER |  |
| INTAKE_RSN_NO_CONTRACEPTIVE_C | INTEGER |  |
| CONTRACEPTIVE_DELIVERY_C | INTEGER |  |
| EXIT_RSN_NO_CONTRACEPTIVE_C | INTEGER |  |
| IS_VAP_DECLINED_YN | VARCHAR (1) |  |
| EPISODE_UPDATE_EFF_DATE | DATETIME | The date when the information in this episode update encounter will start being used. |
| EPISODE_UPD_CREAT_RSN_C | INTEGER |  |
| CAD_EOD_PROCESSED_YN | VARCHAR (1) |  |
| VISIT_MSG_DECLINE_YN | VARCHAR (1) |  |
| ODVV_PAT_WAIT_MINUTES | INTEGER | The amount of time, in minutes, that the patient perceived waiting in the On Demand Video Visit queue. This is calculated, based on the On Demand Department build, as the time difference between the event set as the ODVV Start event and the ODVV End event. In the default configuration, this is calculated as the amount of time between the patient enqueueing for the On Demand Video Visit (R LEV 92000 - Start of Patient Perceived Wait Time) and a simultaneous patient and provider video connection (R LEV 84511 - Patient and Provider Connected). This item will be null for all encounters that are not On Demand Video Visits. |
| BILL_FOR_DENIAL_YN | VARCHAR (1) |  |
| MYC_EPIC_LINKSOURCE_C | INTEGER |  |
| ECHKIN_CUTOFF_DATE | DATETIME | The last date that eCheck-In can be completed for an encounter. |
| OR_ADMIT_GRP_ENC_DATE | DATETIME | The date that the encounter is contributing to for each of the groups and hospitals in EPT items 88600 and 88601. |
| MYC_WEB_BUILDER_UCI | INTEGER | Records the UCI of the microsite from which the patient was referred to MyChart online scheduling when the UCI is provided in an Epic-built microsite linkSource. |
| COULD_ONLINE_SCHED_VERSION | NUMERIC (18,1) | This column tracks the version of the logic used for our "Could Have Been Scheduled Online Items" in I EPT 28156, I EPT 28158, and I EPT 28162. If this item is not populated, then the contact has a default value of 1 indicating the initial version.  If one of the above items has a change in it's logic, then a new version will be created here. Notably, changes in logic can be item-specific, so older versions can still be up-to-date for the unaffected items. |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| B-TREE INDEX | EIX_PAT_ENC_7_CONTACT | PAT_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_PAT_ENC_7_CONTACT | PAT_ENC_DATE_REAL | 2 | Yes | Yes |  |

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

_(320 total; showing first 30)_
