# PAT_ENC

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=PAT_ENC

## Description

The patient encounter table contains one record for each patient encounter in your system. By default, this table does not contain Registration or PCP/Clinic Change contacts (encounter types 1 and 31). It does contain all appointments, office visits, telephone encounters, and other types of encounters. The primary key for the patient encounter table is PAT_ENC_CSN_ID. Note that there is an index named EIX_FILT_PAT_ENC_RFL on the REFERRAL_ID column in Oracle that does not appear in the index list. The index is created by EFN_FAUX_RFL_FILT_INX.

**Primary table** in this group (143 cols). Overflow siblings joined on shared key: PAT_ENC_2 (101 cols), PAT_ENC_3 (101 cols), PAT_ENC_4 (102 cols), PAT_ENC_5 (100 cols), PAT_ENC_6 (94 cols), PAT_ENC_7 (80 cols), PAT_ENC_8 (44 cols). Prefer this table for most queries.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | EPT |
| Release Version | EPIC 2000 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| PAT_ID | VARCHAR (18) | The unique ID assigned to the patient record. This ID may be encrypted if you have elected to use enterprise reporting?s encryption utility. |
| PAT_ENC_DATE_REAL | No | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| PAT_ENC_CSN_ID | NUMERIC (18,0) | A unique serial number for this encounter. This number is unique across all patients and encounters in the system. |
| CONTACT_DATE | DATETIME | The date of this contact in calendar format. |
| ENC_TYPE_C | VARCHAR (66) |  |
| ENC_TYPE_TITLE | No | This column is deprecated. The column previously extracted the category title. In order to avoid data consistency issues, use ENC_TYPE_C to link to ZC_DISP_ENC_TYPE instead. |
| AGE *(deprecated)* | FLOAT | In table PAT_ENC, the column AGE has been deprecated.  To look up the deprecated column's value after the Clarity Compass upgrade, join column PAT_ENC.PAT_ID to PATIENT.PAT_ID, and calculate the difference between PAT_ENC.CONTACT_DATE and PATIENT.BIRTH_DATE.   In many cases, the CONTACT_DATE column that the AGE column was based on will not be the most relevant date for the contact. For example for an admission, you may wish to join PATIENT.PAT_ID to PAT_ENC_HSP.PAT_ID and calculate the difference between PAT_ENC_HSP.HOSP_ADMSN_TIME or PAT_ENC_HSP.HOSP_DISCH_TIME and PATIENT.BIRTH_DATE. |
| PCP_PROV_ID | VARCHAR (18) | The unique ID of the provider record for the patient?s General Primary Care Provider as of the date of the encounter. This ID may be encrypted if you have elected to use enterprise reporting?s security utility. |
| FIN_CLASS_C | VARCHAR (66) |  |
| VISIT_PROV_ID | VARCHAR (18) | The unique ID for the visit provider associated with this encounter. In cases where there are multiple providers for one encounter, this is the ID of the first provider in the list. This item may be NULL if there is no provider for this encounter. This ID may be encrypted. |
| VISIT_PROV_TITLE | VARCHAR (66) |  |
| DEPARTMENT_ID | NUMERIC (18,0) | The ID of the department for the encounter. If there are multiple departments for the encounter, this is the ID of the first department in the list. |
| BP_SYSTOLIC | FLOAT | The systolic portion of the patient?s blood pressure measured at this encounter. |
| BP_DIASTOLIC | FLOAT | The diastolic portion of the patient?s blood pressure measured at this encounter. |
| TEMPERATURE | FLOAT | The patient?s temperature taken during this encounter. This value is in degrees Fahrenheit regardless of how the temperature reading was entered. |
| PULSE | INTEGER | The patient?s pulse taken during this encounter. |
| WEIGHT | FLOAT | The patient?s weight as recorded during this encounter. Note: This field is stored in ounces regardless of how the weight was entered. Divide this number by 16 to report the patient?s weight in pounds. |
| HEIGHT | VARCHAR (270) | The patient?s height as recorded during this encounter. This field is a string and may contain indicators for feet and/or inches. |
| RESPIRATIONS | INTEGER | The patient?s respiration rate as recorded during this encounter. |
| LMP_DATE | DATETIME | The date of the patient?s Last Menstrual Period. Only contains data for encounters with female patients. |
| LMP_OTHER_C *(deprecated)* | INTEGER |  |
| HEAD_CIRCUMFERENCE | FLOAT | The patient?s Head Circumference as recorded during this encounter. This item will contain data only for patients younger than the age specified in Miscellaneous Configuration. Note: This value is stored in centimeters. |
| ENC_CLOSED_YN | VARCHAR (1) |  |
| ENC_CLOSED_USER_ID | VARCHAR (18) | The unique ID of the system user who closed the patient encounter. This ID may be encrypted. |
| ENC_CLOSE_DATE | DATETIME | The date on which the patient encounter was closed. |
| LOS_PRIME_PROC_ID | NUMERIC (18,0) | The ID of the procedure record corresponding to the primary LOS code for this encounter. Note: This is not the CPT? code. It is an internal identifier that is typically not visible to a user. |
| LOS_PROC_CODE | 18205 |  |
| LOS_MODIFIER1_ID | VARCHAR (20) | The first Level of Service modifier applied to the encounter. This item will appear empty if no modifier is present. |
| LOS_MODIFIER2_ID | VARCHAR (20) | The second Level of Service modifier applied to the encounter. This item will appear empty if no modifier is present. |
| LOS_MODIFIER3_ID | VARCHAR (20) | The third Level of Service modifier applied to the encounter. This item will appear empty if no modifier is present. |
| LOS_MODIFIER4_ID | VARCHAR (20) | The fourth Level of Service modifier applied to the encounter. This item will appear empty if no modifier is present. |
| CHKIN_INDICATOR_C | INTEGER |  |
| CHKIN_INDICATOR_DT | DATETIME | The date associated with the visit indicator as entered by an system user at Check In. |
| APPT_STATUS_C | INTEGER |  |
| APPT_BLOCK_C | VARCHAR (66) |  |
| APPT_TIME | DATETIME (Local) | The scheduled appointment date and time for the encounter recorded using a twenty-four hour clock, i.e. 1 P.M. on January 4, 2000, would be 01/04/2000 13:00. |
| APPT_LENGTH | INTEGER | Scheduled appointment length in minutes. |
| APPT_MADE_DATE | DATETIME | The date on which the appointment was made. Note that this may be updated if the appointment is changed. To determine the date on which the appointment was first entered into the system, use the column APPT_MADE_DATE in the derived table F_SCHED_APPT, or join to the audit trail table PAT_ENC_ES_AUD_ACT where LINE = 1. |
| APPT_PRC_ID | VARCHAR (18) | The unique ID of the visit type (PRC .1) assigned to the encounter when the appointment is made. |
| CHECKIN_TIME | 7200 | The date and time the patient was checked in for the appointment for this encounter. Note that the date portion of this value is always the appointment date, regardless of the date on which the appointment was actually checked in. Also, the time portion of this value can be modified by users in the application. This may or may not be more accurate than the system-audited time. To determine the check in instant recorded by the system, use the CHECKIN_AUD_DTTM column in PAT_ENC_7. |
| CHECKOUT_TIME | 7210 | The date and time the patient was checked out for this encounter. Note that the date portion of this value is always the appointment date, regardless of the date on which the appointment was actually checked out. Also, the time portion of this value can be modified by users in the application. This may or may not be more accurate than the system-audited time. To determine the check out instant recorded by the system, use the CHECKOUT_AUD_DTTM column in PAT_ENC_7. |
| ARVL_LST_DL_TIME | 7233 | The date and time the encounter was deleted from the arrival list.  NOTE: This column will try to pull from the ARRIVAL LIST DELETE WHEN item (EPT 7233) first, then if it finds nothing there it will pull from AUDITED INSTANT (EPT 7544). |
| ARVL_LST_DL_USR_ID | 7234 | The unique ID of the system user who removed the encounter from the arrival list. This ID may be encrypted.  NOTE: This column will try to pull from the ARRIVAL LIST DELETE BY WHOM item (EPT 7234) first, then if it finds nothing there it will pull from AUDITED USER ID (EPT 7543). |
| APPT_ENTRY_USER_ID | VARCHAR (18) | The unique ID of the system user who entered the appointment. Note that this may be updated if the appointment is changed. To determine the user who first entered the appointment into the system, use the column APPT_ENTRY_USER_ID in the derived table F_SCHED_APPT, or join to the audit trail table PAT_ENC_ES_AUD_ACT where LINE = 1. |
| APPT_CANC_USER_ID | VARCHAR (18) | The unique ID of the user who canceled the appointment. |
| APPT_CANCEL_DATE | DATETIME | The date the appointment was canceled. If the appointment was not canceled this field is NULL. |
| CHECKIN_USER_ID | VARCHAR (18) | The unique ID of the system user who checked in the patient for this encounter. If the encounter has not been through the Check In process this field will be NULL. This ID may be encrypted. |
| CANCEL_REASON_C | INTEGER |  |
| APPT_SERIAL_NO | NUMERIC (18,0) | A non-unique serial number for the appointment. The APPT_SERIAL_NO is the same as the PAT_ENC_CSN_ID unless the appointment is canceled and rescheduled. In that case, the APPT_SERIAL_NO for the rescheduled appointment is the same as the initial appointment; however, these appointments have different PAT_ENC_CSN_IDs. |
| HOSP_ADMSN_TIME | 18850 | The date and time that the patient was first admitted to the facility, bedded in the ED, or confirmed for an HOV for this contact, regardless of patient's base patient class. |
| HOSP_DISCHRG_TIME | 18855 | The hospital discharge date and time for this patient contact. |
| HOSP_ADMSN_TYPE_C | VARCHAR (66) |  |
| NONCVRED_SERVICE_YN | VARCHAR (1) |  |
| REFERRAL_REQ_YN | VARCHAR (1) |  |
| REFERRAL_ID | NUMERIC (18,0) | The unique ID of the referral record linked to this appointment. |
| ACCOUNT_ID | NUMERIC (18,0) | The ID number of the guarantor account assigned to the visit at the time it is scheduled or when it is checked in. This ID may be encrypted. |
| COVERAGE_ID | NUMERIC (18,0) | The ID number of the coverage record assigned to the visit at the time it is scheduled or when it is checked in. This ID may be encrypted. |
| AR_EPISODE_ID *(deprecated)* | VARCHAR (254) | In the table PAT_ENC, the column AR_EPISODE_ID (EPT,2208) has been deprecated. The deprecated column's content/data is no longer available since it is no longer populated in Chronicles. |
| CLAIM_ID | NUMERIC (18,0) | The unique ID of the billing system Claim record (CLM record) linked to charges associated with this visit. |
| PRIMARY_LOC_ID | NUMERIC (18,0) | The unique ID of the patient?s primary location as of the contact date of the encounter. Note: This may not be the same as the patient?s current primary location. |
| CHARGE_SLIP_NUMBER | VARCHAR (18) | The encounter form number or charge slip number assigned to this encounter. Note: The charge slip number is also stored in the financial table CLARITY_TDL. You can use this field to link to CLARITY_TDL to identify financial transactions associated with the encounter. |
| VISIT_EPM_ID | No |  |
| VISIT_EPP_ID | No |  |
| VISIT_FC | EPM |  |
| COPAY_DUE | NUMERIC (12,2) | The dollar amount shown in the Copay Due field of the scheduling system's Check In Patient activity. This amount may be calculated by the system using the patient's coverage benefit information or be manually entered by a user. This field may also be empty if no copay amount was entered when the patient's appointment was checked in. |
| COPAY_COLLECTED | NUMERIC (12,2) | The amount in the Copay Collected field entered by the user during Check In.  Note: If your facility uses the Registration or POS copay form at check-in/check-out, users may collect more than one copay per appointment.  The value in this field only reflects the last copay collected for any given appointment.  Data for all copays collected can be found in the PAT_ENC_COPAY_COLL table.  If your facility uses the AR copay form, this is the correct data source to use. |
| COPAY_SOURCE_C | INTEGER |  |
| COPAY_TYPE_C | INTEGER |  |
| COPAY_REF_NUM | VARCHAR (255) | The reference number of the copay as recorded for this encounter during Check In. This could be the check number or credit card number for the copay.  Note: If your facility uses the Registration or POS copay form at check-in/check-out, users may collect more than one copay per appointment.  The value in this field only reflects the last copay collected for any given appointment.  Data for all copays collected can be found in the PAT_ENC_COPAY_COLL table.  If your facility uses the AR copay form, this is the correct data source to use. |
| COPAY_PMT_EXPL_C | INTEGER |  |
| UPDATE_DATE | No | The time this patient encounter was pulled into enterprise reporting. |
| SERV_AREA_ID | No |  |
| HSP_ACCOUNT_ID | NUMERIC (18,0) | The ID number of the hospital billing account assigned to the encounter. |
| ADM_FOR_SURG_YN | VARCHAR (1) |  |
| SURGICAL_SVC_C | VARCHAR (66) |  |
| INPATIENT_DATA_ID | VARCHAR (18) | The ID number of the record used to determine how inpatient data is stored for the encounter. |
| IP_EPISODE_ID | NUMERIC (18,0) | The ID number of the inpatient episode of care. This includes discharges from the ED. |
| APPT_QNR_ANS_ID *(deprecated)* | VARCHAR (18) | This column is deprecated and does not extract any data. To report on answers to appointment questionnaires, use the table PAT_ENC_QNRS_ANS. |
| ATTND_PROV_ID | VARCHAR (18) | The unique ID of the attending provider. |
| ORDERING_PROV_TEXT | VARCHAR (255) | Data from a free text field that contains information on the provider who placed the order. |
| ES_ORDER_STATUS_C | INTEGER |  |
| EXTERNAL_VISIT_ID | VARCHAR (254) | The ID for the contact as assigned by a non-system. Usually populated by an interface. |
| CONTACT_COMMENT | VARCHAR (1000) | Comments entered by the provider for the contact. |
| OUTGOING_CALL_YN | VARCHAR (1) |  |
| DATA_ENTRY_PERSON | VARCHAR (100) | This is the name of the user who created the encounter. |
| IS_WALK_IN_YN | VARCHAR (1) |  |
| CM_CT_OWNER_ID | VARCHAR (25) | ID of the deployment owner for this contact. |
| REFERRAL_SOURCE_ID | VARCHAR (18) | The referral ID number of the referring physician. This physician may be from an external organization. |
| SIGN_IN_TIME | 7230 | The date and time the patient was signed in for the appointment for this encounter. Note that the date portion of this value is always the appointment date, regardless of the date on which the appointment was actually signed in. Also, the time portion of this value can be modified by users in the application. This may or may not be more accurate than the system-audited time. To determine the check in instant recorded by the system, use the SIGNIN_AUD_DTTM column in PAT_ENC_7. |
| SIGN_IN_USER_ID | VARCHAR (18) | The unique ID of the system user who signed in the patient for this encounter.  If the encounter has not been through the Sign In process this field will be NULL.  This ID may be encrypted. |
| APPT_TARGET_DATE | DATETIME | Target date on which to schedule the appointment. |
| WC_TPL_VISIT_C | INTEGER |  |
| ROUTE_SUM_PRNT_YN | VARCHAR (1) |  |
| CONSENT_TYPE_C | INTEGER |  |
| PHONE_REM_STAT_C | INTEGER |  |
| APPT_CONF_STAT_C | INTEGER |  |
| APPT_CONF_PERS *(deprecated)* | VARCHAR (254) |  |
| APPT_CONF_INST | DATETIME (Local) | Date and time this appointment was confirmed via scheduling system. |
| CANCEL_REASON_CMT | VARCHAR (1000) | The free text entered in the Comment field during appointment cancellation. |
| ORDERING_PROV_ID | VARCHAR (18) | The unique ID of the ordering provider for an appointment as entered on the Orders form of the Appointment Info activity. |
| BMI | NUMERIC (18,2) | This is the patient's Body Mass Index, which is calculated based on the recorded height and weight. |
| BSA | NUMERIC (18,2) | This is the patient's Body Surface Area, which is calculated based on the recorded height and weight. |
| AVS_PRINT_TM | DATETIME (Local) | The instant that the After Visit Summary (AVS) was printed for this encounter. |
| AVS_FIRST_USER_ID | VARCHAR (18) | Unique ID of the user who first prints out the After Visit Summary (AVS) for the encounter. |
| ENC_MED_FRZ_RSN_C | INTEGER |  |
| WC_TPL_VISIT_CMT | VARCHAR (254) | Comments related to anticipated account type stored in EPT 2245 |
| HOSP_LICENSE_C | INTEGER |  |
| ACCREDITATION_C | INTEGER |  |
| CERTIFICATION_C | INTEGER |  |
| ENTITY_C | INTEGER |  |
| EFFECTIVE_DATE_DT | DATETIME | The date of the encounter. The returned date is handled differently depending on the contact type of the encounter: If it is a surgery encounter, the date of the surgery will be returned. If it is a Hospital encounter, Admission/Discharge/Transfer (ADT) info will be used to return an appropriate date. If ADT info cannot be found, then the  Hospital Admission date (I EPT 18850) will be returned. If the Hospital Admission Date cannot be found, the temporary admission date (I EPT 18846) will be returned.. |
| DISCHARGE_DATE_DT | DATETIME | The discharge date for the encounter. |
| EFFECTIVE_DEPT_ID | NUMERIC (18,0) | The effective department ID. The department is found by returning the first department to have a value in the following order: 1) Hospital Unit 2) Procedure Pass Department (the effective department of linked appointment or admission) 3) Hospice Intake Department 4) Appointment Department 5) Waiting List Department 6) OR Department |
| TOBACCO_USE_VRFY_YN *(deprecated)* | VARCHAR (1) |  |
| PHON_CALL_YN | VARCHAR (1) |  |
| PHON_NUM_APPT | VARCHAR (30) | Phone number that all calls for this appointment should go to. |
| ENC_CLOSE_TIME | 18119 | This column contains the time that this encounter was closed. |
| COPAY_PD_THRU | INTEGER |  |
| INTERPRETER_NEED_YN | VARCHAR (1) |  |
| VST_SPECIAL_NEEDS_C | INTEGER |  |
| INTRP_ASSIGNMENT_C | INTEGER |  |
| ASGND_INTERP_TYPE_C | INTEGER |  |
| INTERPRETER_VEND_C | INTEGER |  |
| INTERPRETER_NAME | VARCHAR (100) | Stores the name of the interpreter assigned to interpreter for an appoinment when the interpreter doesn't have a provider record (i.e. assigned from an outside vendor). |
| CHECK_IN_KIOSK_ID | VARCHAR (18) | Which Kiosk the appointment is checked in |
| BENEFIT_PACKAGE_ID | NUMERIC (18,0) | Stores the benefit package used when calculating the copay. |
| BENEFIT_COMP_ID | VARCHAR (200) | Stores the Component or Component group that were used to find the Adjudication Table when adjudicating the copay. |
| BEN_ADJ_TABLE_ID | NUMERIC (18,0) | Stores the Adjudication Table used to determine the copay. |
| BEN_ADJ_FORMULA_ID | NUMERIC (18,0) | Stores the Adjudication Formula used to determine the copay. |
| BEN_ENG_SP_AMT | NUMERIC (12,2) | Stores the adjudicated self-pay amount (the amount required to be paid by the patient) when determining the copay amount for the visit. |
| BEN_ADJ_COPAY_AMT | NUMERIC (12,2) | Stores the adjudicated copy amount for the visit according to the patient's coverage benefits. |
| BEN_ADJ_METHOD_C | INTEGER |  |
| DOWNTIME_CSN | NUMERIC (18,0) | Downtime contact serial number |
| ENTRY_TIME | DATETIME (Local) | The instant this patient contact was created. This column is used for running standard Clarity validations against Chronicles. |
| ENC_CREATE_USER_ID | VARCHAR (18) | The ID number of the user who create the patient or encounter record. |
| ENC_INSTANT | DATETIME (Local) | The instant an encounter was created |
| ED_ARRIVAL_KIOSK_ID | VARCHAR (18) | The kiosk workstation that performed the ED arrival. |
| EFFECTIVE_DATE_DTTM | 87317 | The start date and time of an encounter. The start date is pulled from the date stored in the EFFECTIVE_DATE_DT column. The time references the first populated time in the following fields: hospital admission time (EPT 18851), hospital temporary admission time (EPT 18847), ADT arrival time (EPT 10815), and expected admission time (EPT 10300).  The SlicerDicer reporting application uses this column to determine the EffectiveStartDate of encounters. |
| CALCULATED_ENC_STAT_C | INTEGER |  |
| APPT_CONF_USER_ID | VARCHAR (18) | The unique ID associated with the user record that confirmed the appointment. This column is frequently used to link to the CLARITY_EMP table. |
| APPT_CANC_UTC_DTTM | DATETIME (UTC) | The UTC date and time that the appointment was canceled. |
| APPT_CANC_DTTM | DATETIME (Attached) | The date and time the appointment was canceled, in the local time zone of the primary appointment department. |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| B-TREE INDEX | EIX_PAT_ENC_001 | APPT_SERIAL_NO | 1 | Yes | Yes |  |
| BITMAP INDEX | EIX_PAT_ENC_APPT_STATUS_C | APPT_STATUS_C | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_PAT_ENC_CODA | CONTACT_DATE | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_PAT_ENC_ENC_CLOSE_USER | ENC_CLOSED_USER_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_PAT_ENC_IPDATAID | INPATIENT_DATA_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_PAT_ENC_IPEPID | IP_EPISODE_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_PAT_ENC_PRLOID | PRIMARY_LOC_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_PAT_ENC_PTENC | PAT_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_PAT_ENC_PTENC | PAT_ENC_DATE_REAL | 2 | Yes | Yes |  |
| B-TREE INDEX | EIX_PAT_ENC_VITALS | PAT_ID | 1 | No | Yes |  |
| B-TREE INDEX | EIX_PAT_ENC_VITALS | CONTACT_DATE | 2 | No | Yes |  |
| B-TREE INDEX | EIX_PAT_ENC_VITALS | HEIGHT | 3 | No | Yes |  |
| B-TREE INDEX | EIX_PAT_ENC_VITALS | WEIGHT | 4 | No | Yes |  |
| B-TREE INDEX | EIX_PAT_ENC_VITALS | BP_DIASTOLIC | 5 | No | Yes |  |
| B-TREE INDEX | EIX_PAT_ENC_VITALS | BP_SYSTOLIC | 6 | No | Yes |  |
| B-TREE INDEX | EIX_PAT_ENC_VIT_BP | BP_SYSTOLIC | 1 | No | Yes |  |
| B-TREE INDEX | EIX_PAT_ENC_VIT_BP | BP_DIASTOLIC | 2 | No | Yes |  |
| B-TREE INDEX | EIX_PAT_ENC_VIT_BP | PAT_ID | 3 | No | Yes |  |
| B-TREE INDEX | EIX_PAT_ENC_VIT_BP | CONTACT_DATE | 4 | No | Yes |  |
| B-TREE INDEX | EIX_PAT_ENC_VIT_HT | HEIGHT | 1 | No | Yes |  |
| B-TREE INDEX | EIX_PAT_ENC_VIT_HT | PAT_ID | 2 | No | Yes |  |
| B-TREE INDEX | EIX_PAT_ENC_VIT_HT | CONTACT_DATE | 3 | No | Yes |  |
| B-TREE INDEX | EIX_PAT_ENC_VIT_WT | WEIGHT | 1 | No | Yes |  |
| B-TREE INDEX | EIX_PAT_ENC_VIT_WT | PAT_ID | 2 | No | Yes |  |
| B-TREE INDEX | EIX_PAT_ENC_VIT_WT | CONTACT_DATE | 3 | No | Yes |  |

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

_(713 total; showing first 30)_
