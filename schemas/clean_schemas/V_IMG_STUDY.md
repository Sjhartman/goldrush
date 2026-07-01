# V_IMG_STUDY

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=V_IMG_STUDY

## Description

This view is designed to simplify reporting on orders performed in the imaging applications. It combines information for orders scheduled via non-invasive appointments and invasive cases into a single datasource. The primary source of data is the F_IMG_STUDY data mart, which is not intended to be used by itself. Use this view instead.

## Metadata

| Property | Value |
| --- | --- |
| Type | View |
| Release Version | Rel 2010 |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| ORDER_ID | NUMERIC (18,0) | The unique ID of the order record associated with this procedure order. |
| PAT_ID | VARCHAR (18) | The unique ID of the patient record for this order. This column is frequently used to link to the PATIENT table. |
| PAT_MRN_ID | VARCHAR (102) | The patient's medical record number (MRN), of the type associated with the patient's current primary location. |
| PAT_NAME | VARCHAR (200) | The patient?s name in the format Lastname, Firstname MI. |
| PAT_NM_WMRN | .2 | A unique patient identifier that consists of the patient name and MRN. This column is often used for grouping and display purposes in reports. |
| PAT_SEX_C | VARCHAR (66) |  |
| PAT_AGE_AT_EXAM | FLOAT | The age of the patient (in years) as of the date of the exam. If the exam has ended, this will be the age as of end exam. If not, this will be the age as of the scheduled appointment date. If an appointment has not been scheduled for this exam, this value will be null. |
| ACCESSION_NUM | VARCHAR (254) | The accession number associated with an order. |
| ORDERING_LOGIN_DEP_ID | NUMERIC (18,0) | This is the login department of the user placing the order in the system. |
| ORDERING_CONTACT_DEP_ID | NUMERIC (18,0) | This is the department of the ordering contact for the order record. |
| ORDERING_CSN_ID | NUMERIC (18,0) | This is the contact serial number of the ordering encounter for this order. |
| PERFORMING_CSN_ID | NUMERIC (18,0) | This is the contact serial number of the encounter where this order was performed. Most "appointment-level" information will be linkable via this CSN. This is not necessarily the same as the order's appointment serial number. |
| PERFORMING_DEP_ID | 7070 645 53011 | The unique ID of the department where this procedure was performed. In the event of a panel, this is the first of the many appointments. In the event of a joint appointment, this is the department that is listed first. For invasive imaging procedures, this is the department linked to the invasive location. In the event of a mammography conversion, this may look to ORD 645, Performing Department, which is only populated for conversions and not for exams performed in Epic. |
| PERFORMING_PROV_ID | 7040 | The unique ID of the resource where this procedure was performed. In the event of a panel, this is the first of the many appointments. In the event of a joint appointment, this is the resource that is listed first. For invasive imaging procedures, this is the primary surgeon on the log. |
| STUDY_STATUS_C | INTEGER |  |
| ORDERING_PROV_ID | 34030 8005 100 | The unique ID of the ordering provider. The column will hold the first field that has a value in the following list: ordering provider, referring provider, authorizing provider. |
| AUTHORIZING_PROV_ID | VARCHAR (18) | The unique ID of the provider authorizing the order. |
| ORDERING_DTTM | DATETIME (Local) | The date and time the order was put in the system. |
| END_EXAM_DTTM | 52129 | The date and time when the exam for the procedure order has ended. |
| FINALIZING_DTTM | DATETIME (Local) | This item stores the instant that a study is finalized. |
| FINALIZING_PROV_ID | VARCHAR (18) | This item stores the physician who finalized a study. |
| LOG_ID | VARCHAR (18) | For imaging procedures that are scheduled via invasive scheduling, this will hold the log ID. |
| PROC_ID | 40 | The unique ID of the procedure record corresponding to this order. Note: This is not the CPT(TM) code. It is an internal identifier that is typically not visible to a user, and can be used to link to CLARITY_EAP. In the event performable procedures are in use, this is the performed procedure ID. |
| PROC_LINE | No | In the event an order has multiple performed procedures tied to it, this column tracks which line the procedure is. |
| PROC_NAME | VARCHAR (189) | The name of each procedure. |
| PROC_CODE | VARCHAR (40) | The code for each procedure. |
| PROC_CAT_ID | 10050 | The unique ID of the procedure category that will be used within the imaging applications. First check the EpicCare override procedure category, and if that is null default to the procedure category. |
| NUM_CPT_CODES | INTEGER | The number of unique CPT codes linked to the performed procedure via the performable/chargeable procedure link. This includes technical, professional and global linked charges. |
| IS_CANCELED_YN | VARCHAR (1) |  |
| BEGIN_EXAM_DTTM | 52119 | The date and time when the procedure order (exam) is to begin. |
| STUDY_GRP_ORDER_ID | NUMERIC (18,0) | The unique identifier of the master procedure record used for grouped imaging orders. |
| ORIGINAL_ORDER_ID | NUMERIC (18,0) | When this item is the result of a procedure order change, it stores a pointer to the previous order at the same level in the order tree hierarchy. This item is not reliable for reporting purposes, as procedures may be changed without populating I ORD 720 on the child order found in this table. Use ORDER_PROC_5.ORIGINATING_ORD_ID instead. |
| REFERRAL_ID | NUMERIC (18,0) | Stores the associated referral ID for orders that generated a referral. Can be used to link to the REFERRAL table. |
| PAT_CLASS_C | 10110 55 55 |  |
| MAX_ORD_DATE_REAL | No | This is the most recent contact for an order. For joining to contact-specific order tables such as ORDER_STATUS, use the ORDER_ID as well as this column to match on ORD_DATE_REAL in order to only return one row per order.   This is a numeric representation of the date of this encounter in your system. The integer portion of the number specifies the date of the encounter. The digits after the decimal point indicate multiple visits on one day. |
| TECH_USER_ID | VARCHAR (18) | The unique ID of the employee record of the technologist who performed this procedure. |
| DICTATING_USER_ID | VARCHAR (18) | The first user that dictates on a study. Links to CLARITY_EMP. This corresponds to the first action in the imaging audit trail where the action was 10 - Sent to Transcription. |
| DICTATING_DTTM | 52901 | The date and time of the first time the study was dictated. This corresponds to the first action in the imaging audit trail where the action was 10 - Sent to Transcription. |
| TRANS_USER_ID | VARCHAR (18) | The first user that transcribes a study. Links to CLARITY_EMP. This corresponds to the first action in the imaging audit trail where the action was 11 - Transcribed. |
| TRANS_DTTM | 52901 | The date and time of the first time the study was transcribed. This corresponds to the first action in the imaging audit trail where the action was 11 - Transcribed. |
| SCHED_EXAM_DTTM | ORC | The scheduled exam date and time for the procedure. This is either the date and time the appointment or case was scheduled to be performed. |
| SCHED_ON_DTTM | 7544 610 625 | The date and time the appointment or case was scheduled on. It is the date and time the appointment was made (for non-invasive exams) or the date and time the case was added to the schedule (for invasive procedures). In the event an appointment or case is rescheduled or changed, this will be the original time it was scheduled. |
| ORD_PROC_ID | NUMERIC (18,0) | The unique ID of the procedure record corresponding to this order. Note: This is not the CPT(TM) code. It is an internal identifier that is typically not visible to a user, and can be used to link to CLARITY_EAP. Unlike the PROC_ID column on this table, the ORD_PROC_ID column will always hold the ordered procedure ID, even if a specific performable is present. |
| CHECKIN_DTTM | DATETIME (Local) | The date and time the order was checked in. If the check in action is performed multiple times, this represents the first check in time that was not canceled. |
| PPS_START_DTTM | 52512 | The DICOM Performed Procedure Step (PPS) start date and time. If a modality sends multiple PPS start times, this will be the minimum date and time of the multiple values. |
| PPS_END_DTTM | 52514 | The DICOM Performed Procedure Step (PPS) end date and time. If a modality sends multiple PPS end times, this will be the maximum date and time of the multiple values. |
| CANCELING_DTTM | DATETIME (Local) | The date and time in which the order was canceled. If the order has not been canceled then this column will be null. |
| CANCELING_USER_ID | VARCHAR (18) | The unique ID of the user who canceled the order. If the order has not been canceled then this column will be null. |
| RESULT_NOTE_CSN | NUMERIC (18,0) | The contact serial number (CSN) of the result note for the study. Use this to join to the HNO_NOTE_TEXT table in order to search the narrative and impression for the study. |
| ABNORMAL_YN | VARCHAR (1) |  |
| INTERESTING_STUDY_C | INTEGER |  |
| ORDER_PRIORITY_C | INTEGER |  |
| HSP_ACCOUNT_ID | NUMERIC (18,0) | The unique ID of the hospital account linked to the order. For non-invasive procedures scheduled to appointments, the hospital account is pulled from the imaging appointment encounter. For invasive procedures scheduled to cases, the hospital account is pulled from the case's linked hospital encounter. |
| PERFORMING_LOC_ID | 501 501 4001 | The unique ID of the location where this procedure was performed. If the procedure is a non-invasive procedure, this is the revenue location tied to the performing department. If this is an invasive procedure, it is the invasive location of the case. |
| PRELIM_USER_ID | VARCHAR (18) | The first user that marks a study as preliminary. Links to CLARITY_EMP. This corresponds to the first action in the imaging audit trail where the action was 12 - Marked as Preliminary. |
| PRELIM_DTTM | 52901 | The date and time of the first time the study was marked as preliminary. This corresponds to the first action in the imaging audit trail where the action was 12 - Marked as Preliminary. |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ORDER_ID | ADT_ORDERS_ERRORS | ORDER_ID | No | Unknown | No |  |
| 1 | ORDER_ID | ADT_ORDER_INFORMATION | ORDER_ID | No | Unknown | No |  |
| 1 | ORDER_ID | APPT_REQUEST | REQUEST_ID | No | Unknown | No |  |
| 1 | ORDER_ID | CL_ORD_FST_LST_SCH | ORDER_ID | No | Unknown | No |  |
| 1 | ORDER_ID | DENT_ORD_NOADD | ORDER_ID | No | Unknown | No |  |
| 1 | ORDER_ID | DUPMED_DISMISS_HH_INFO | ORDER_ID | No | Unknown | No |  |
| 1 | ORDER_ID | ENDOSCOPY_METRICS | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_ID | EXTERNAL_ORDER_INFO | ORDER_ID | No | Unknown | No |  |
| 1 | ORDER_ID | F_IMG_STUDY | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_ID | F_IP_HSP_SUM_ORDER | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_ID | F_LAB_ORDERS | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_ID | F_MU_OBJ_EH_PLACED_ORDER | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_ID | F_MU_OBJ_EH_RESULTD_ORDER | ORDER_PROC_ID | Unknown | Unknown | No |  |
| 1 | ORDER_ID | F_ONC_PRIOR_AUTH_ORDERS | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_ID | F_OPIOID_ORDERS | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_ID | F_RX_ORDER | ORDER_MED_ID | Unknown | Unknown | No |  |
| 1 | ORDER_ID | HH_MED_ORD_IN_POC_DETAIL | ORDER_MED_ID | No | Unknown | No |  |
| 1 | ORDER_ID | HV_ORDER_PROC | ORDER_PROC_ID | Unknown | Unknown | No |  |
| 1 | ORDER_ID | MED_DETAILS_EXT_ORD | ORDER_ID | No | Unknown | No |  |
| 1 | ORDER_ID | MERCHANDISE_ORDER_INFO | ORDER_ID | Yes | Unknown | No |  |
| 1 | ORDER_ID | MU_EH_QRDA_I_ORDER | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_ID | ORDERS | ORDER_ID | No | Unknown | No |  |
| 1 | ORDER_ID | ORDER_AUTH_INFO | ORDER_ID | No | Unknown | No |  |
| 1 | ORDER_ID | ORDER_MED | ORDER_MED_ID | Unknown | Unknown | No |  |
| 1 | ORDER_ID | ORDER_MEDINFO | ORDER_MED_ID | Unknown | Unknown | No |  |
| 1 | ORDER_ID | ORDER_MED_2 | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_ID | ORDER_MED_3 | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_ID | ORDER_MED_4 | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_ID | ORDER_MED_5 | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_ID | ORDER_MED_6 | ORDER_MED_ID | Unknown | Unknown | No |  |

_(796 total; showing first 30)_
