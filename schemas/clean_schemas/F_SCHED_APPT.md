# F_SCHED_APPT

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=F_SCHED_APPT

## Description

This table contains information about appointments, with one row per appointment. It is derived from the PAT_ENC table and contains columns simplifying common reporting needs.

## Metadata

| Property | Value |
| --- | --- |
| Type | Derived Table |
| Load Frequency | INCREMENTAL |
| Release Version | Rel 2010 |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| PAT_ENC_CSN_ID | NUMERIC (18,0) | The unique contact serial number for this appointment. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| UPDATE_DATE | No | The date and time when this row was created or last updated. |
| CONTACT_DATE | DATETIME | The date of the appointment. This stores the same date as the APPT_DTTM column, but at midnight. |
| PAT_ID | VARCHAR (18) | The unique ID assigned to the patient record. This ID may be encrypted if you have elected to use enterprise reporting?s encryption utility. |
| APPT_STATUS_C | INTEGER |  |
| DEPARTMENT_ID | NUMERIC (18,0) | The ID of the department for the encounter. If there are multiple departments for the encounter, this is the ID of the first department in the list. |
| PROV_ID | VARCHAR (18) | The unique ID of the appointment provider. This is frequently used to join to the CLARITY_SER table. For joint appointments, this contains the ID of the primary provider on the appointment. |
| PRC_ID | VARCHAR (18) | The unique ID of the visit type for the appointment. |
| APPT_MADE_DTTM | No | The date and time that the appointment was made. |
| APPT_MADE_DATE | No | The date on which the appointment was made. This stores the same date as the APPT_MADE_DTTM column, but at midnight. Note that this may not store the same value as PAT_ENC.APPT_MADE_DATE. PAT_ENC.APPT_MADE_DATE may change when the appointment is changed, but the value of this column stays the same, and is thus what you should use when determining the date on which an appointment was entered in the system. |
| APPT_BLOCK_C | VARCHAR (66) |  |
| APPT_DTTM | DATETIME (Local) | The date and time of the appointment, stored in the time zone of the appointment department. Use APPT_UTC_DTTM to get the time in UTC. |
| APPT_LENGTH | INTEGER | The total scheduled length of the appointment in minutes. |
| CHECKIN_DTTM | DATETIME (Attached) | The date and time of the system-audited check-in.  If a check-in was canceled or the appointment was checked in multiple times, this column will store the time of the first check-in action after the last cancel check-in action. If there was a cancel check-in action without a subsequent check-in action, this column will be null. This may or may not be more accurate than the user-editable time recorded by the CHECKIN_TIME column in PAT_ENC. |
| CHECKOUT_DTTM | DATETIME (Attached) | The date and time of the system-audited check-out.   If the check-out was canceled, this column will store the time of the first check-out action after the last cancel check-out action. If there was a cancel check-out action without a subsequent check-out action, this column will be null. This may or may not be more accurate than the user-editable time recorded by the CHECKOUT_TIME column in PAT_ENC. |
| ARVL_LIST_REMOVE_DTTM | No | The date and time of the system-audited removal from arrival list action. |
| SIGNIN_DTTM | DATETIME (Attached) | The date and time of the system-audited sign-in action.   If a sign-in was canceled or the appointment was signed in multiple times, this column will store the time of the first sign-in action after the last cancel sign-in action. If there was a cancel sign-in action without a subsequent sign-in action, this column will be null. This may or may not be more accurate than the user-editable time recorded by the SIGN_IN_TIME column in PAT_ENC.  Additionally, if the system is configured to automatically sign in walk-in appointments, a cancel check-in event will behave like a cancel sign-in event for walk-ins. |
| PAGED_DTTM | DATETIME (Attached) | The date and time that the patient was paged after checking in for their appointment. |
| ROOMED_DTTM | No | The date and time that the patient was roomed, based on when clinical data were saved. |
| NURSE_LEAVE_DTTM | No | The date and time that the nurse left the room. |
| PHYS_ENTER_DTTM | No | The date and time that the physician entered the room. |
| VISIT_END_DTTM | No | The date and time that the encounter ended. |
| APPT_ENTRY_USER_ID | No | The unique ID of the user who made the appointment. |
| APPT_CANC_USER_ID | VARCHAR (18) | The unique ID of the user who canceled the appointment. |
| APPT_CANC_DTTM | DATETIME (Attached) | The date and time the appointment was canceled, in the local time zone of the primary appointment department. |
| APPT_CANC_DATE | DATETIME | The date that the appointment was canceled, if it was canceled. This is the value in the APPT_CANC_DTTM column at midnight. |
| CANCEL_REASON_C | INTEGER |  |
| APPT_SERIAL_NUM | NUMERIC (18,0) | The appointment serial number for the appointment. This value is unique among appointments that are not canceled, and can be used to group together canceled and rescheduled appointments. |
| RESCHED_APPT_CSN_ID | No | The contact serial number of the non-canceled appointment rescheduled from the appointment. |
| REFERRAL_ID | NUMERIC (18,0) | The unique ID of the referral attached to the appointment. |
| ACCOUNT_ID | NUMERIC (18,0) | The unique ID of the visit account associated with the appointment. |
| COVERAGE_ID | NUMERIC (18,0) | The unique ID of the visit coverage associated with the appointment. |
| CHARGE_SLIP_NUMBER | VARCHAR (18) | The encounter form number or charge slip number assigned to this appointment. |
| HSP_ACCOUNT_ID | NUMERIC (18,0) | The unique ID of the hospital account associated with the appointment. |
| APPT_CONF_STAT_C | INTEGER |  |
| APPT_CONF_USER_ID | VARCHAR (18) | The unique ID associated with the user record that confirmed the appointment. This column is frequently used to link to the CLARITY_EMP table. |
| APPT_CONF_DTTM | DATETIME (Local) | The date and time that the appointment was confirmed. |
| CHECK_IN_KIOSK_ID | VARCHAR (18) | The unique ID of the workstation record for the check-in kiosk. |
| SCHED_FROM_KIOSK_ID | VARCHAR (18) | The unique ID of the workstation record for the kiosk from which the appointment was scheduled. |
| CHECK_OUT_KIOSK_ID | VARCHAR (18) | The unique ID of the workstation record for the check-out kiosk. |
| IP_DOC_CONTACT_CSN | NUMERIC (18,0) | For Hospital Outpatient Visit (HOV) encounters, this column stores the unique contact serial number for the patient contact which is used for clinical documentation.  This can be set for appointment contacts if they are not converted to HOVs. |
| WALK_IN_YN | VARCHAR (1) |  |
| SEQUENTIAL_YN | VARCHAR (1) |  |
| CNS_WARNING_OVERRIDDEN_YN | No | Indicates whether or not the user overrode a warning that the patient chronically no-shows and should be booked in an overbook opening. Y indicates that the warning was overridden. N indicates that no such warning was displayed and overridden. |
| SAME_DAY_CANC_YN | No | Indicates that the appointment was canceled on the day of the appointment. |
| OVERBOOKED_YN | No | Indicates whether or not the appointment was booked into an overbook opening. Y indicates that the appointment was overbooked. N indicates that the appointment was not overbooked. If this is a joint appointment, Y will indicate that the appointment was overbooked with at least one of the providers. |
| OVERRIDE_YN | No | Indicates whether or not the appointment was scheduled outside of the template. Y indicates that it was scheduled outside of the template, and N indicates that it was not. If this is a joint appointment, this column will have Y if it is outside of the regular schedule for at least one of the providers. |
| UNAVAILABLE_TIME_YN | No | Indicates whether or not the appointment was scheduled into unavailable time. Y indicates that it was scheduled into time marked unavailable, and N indicates that it was not. If this is a joint appointment, this column will have Y if it is was scheduled into time marked unavailable for at least one of the providers. |
| REFERRAL_REQ_YN | No | Indicates whether or not the appointment requires a referral as determined by the visit coverage and appointment information. Y indicates that a referral is required. N indicates that a referral is not required. |
| REFERRING_PROV_ID | VARCHAR (18) | The unique ID of the referring provider for this appointment. This column is frequently used to join to the CLARITY_SER table. |
| SAME_DAY_YN | No | Indicates whether or not the appointment was made on the day of the appointment. Y indicates that it is a same day appointment. N indicates that it is not a same day appointment. |
| NUMBER_OF_CALLS | No | The number of calls made to the patient about the appointment using communication tracking functionality. |
| CHANGE_CNT | No | The number of times that an appointment has been changed. If an appointment has not been changed, this will be 0. |
| JOINT_APPT_YN | No | Indicates whether or not the appointment is a joint appointment. Y indicates that it is a joint appointment, and N indicates that it is not. |
| CM_CT_OWNER_ID | VARCHAR (25) | ID of the deployment owner for this contact. |
| PHONE_REM_STAT_C | INTEGER |  |
| COPAY_DUE | NUMERIC (12,2) | The dollar amount in the Copay Due field on scheduling system?s Check In Patient window. This field may be calculated by the Benefit Engine or entered or modified by the user. It is a dollar amount field and may be NULL if no copay was recorded at Check In. |
| COPAY_COLLECTED | NUMERIC (12,2) | The total copay collected for the visit. |
| COPAY_USER_ID | No | The unique ID of the user who collected the copay. If copay was collected multiple times, this stores the ID of the first copay collection user. |
| FIRST_ROOM_ASSIGN_DTTM | DATETIME (Local) | The date and time when the patient was first assigned to a room for an appointment.  This column is only populated for outpatient appointments where the "Room Patient" button is used for room assignment.  This is distinct from roomed times as calculated by clinical timestamps and the Arrival List. |
| BEGIN_CHECKIN_DTTM | DATETIME (Local) | The date and time when the first check-in began. If a user cancels out of the check-in workflow this field will not be populated. Also, if a user cancels check-in this field will be cleared.  This column is only populated for Hyperspace checkins through the scheduling application. It does not get populated for check-ins performed in Text, Welcome or via an automatic process such as through Cadence end of day processing. |
| APPT_ARRIVAL_DTTM | DATETIME (Attached) | This column stores the time by which a patient should arrive for his or her appointment. |
| APPT_UTC_DTTM | DATETIME (UTC) | The date and time of the appointment, in UTC. Use APPT_DTTM to get the date and time of the appointment in the appointment department's time zone. |
| APPT_CANC_UTC_DTTM | DATETIME (UTC) | The UTC date and time that the appointment was canceled. |
| APPT_MADE_UTC_DTTM | No | The date and time that the appointment was made, stored in UTC. To get the time in the time zone of the user who created it, use APPT_MADE_DTTM.  This column will not be populated for appointments created prior to Epic 2012. |
| APPT_SCHED_SOURCE_C | INTEGER |  |
| PAT_ONLINE_YN | VARCHAR (1) |  |
| ECHKIN_STATUS_C | INTEGER |  |
| PAT_SCHED_MYC_STAT_C | INTEGER |  |
| LATE_CANCEL_YN | VARCHAR (1) |  |
| COULD_DIR_SCHED_C | INTEGER |  |
| COULD_OPEN_SCHED_C | INTEGER |  |
| COULD_TKT_SCHED_C | INTEGER |  |
| COULD_ONLINE_SCHED_VERSION | NUMERIC (18,1) | This column tracks the version of the logic used for our "Could Have Been Scheduled Online Items" in I EPT 28156, I EPT 28158, and I EPT 28162. If this item is not populated, then the contact has a default value of 1 indicating the initial version.  If one of the above items has a change in it's logic, then a new version will be created here. Notably, changes in logic can be item-specific, so older versions can still be up-to-date for the unaffected items. |
| SILENTLY_SCHEDULED_YN | No | Whether this appointment was silently scheduled, meaning it has an order attached to it that was silently scheduled. |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| B-TREE INDEX | EIX_F_SCHED_APPT_DATE | CONTACT_DATE | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_F_SCHED_APPT_DTTM | APPT_DTTM | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_F_SCHED_APPT_UPD | UPDATE_DATE | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_F_SCHED_IP_DOC_CSN | IP_DOC_CONTACT_CSN | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_F_SCHED_PAT_ID | PAT_ID | 1 | Yes | Yes |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | PAT_ENC_CSN_ID | ALT_ORD_PROV_SINGL | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 1 | PAT_ENC_CSN_ID | AN_RELINK_INFO | PAT_ENC_CSN_ID | No | Unknown | No |  |
| 1 | PAT_ENC_CSN_ID | DENT_ORTH_EXAM_NOTES | PAT_ENC_CSN_ID | No | Unknown | No |  |
| 1 | PAT_ENC_CSN_ID | FAC_CHG_OVERRIDE | PAT_ENC_CSN_ID | No | Unknown | No |  |
| 1 | PAT_ENC_CSN_ID | FAM_HX_PAT_ONLY | PAT_ENC_CSN_ID | No | Unknown | No |  |
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
| 1 | PAT_ENC_CSN_ID | HAUD_ENC | ENC_CSN | Unknown | Unknown | No |  |
| 1 | PAT_ENC_CSN_ID | HH_PAT_CERT_PERIOD | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |

_(713 total; showing first 30)_
