# TPL_TXDAYS

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=TPL_TXDAYS

## Description

This table contains the treatment days in a treatment plan record or the steps in a pathway record.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | TPL |
| Release Version | SPRING 2008 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| TREATMENT_PLAN_ID | NUMERIC (18,0) | The treatment plan ID. |
| LINE | No | The line number that corresponds to each treatment day in the treatment plan in this row. |
| CM_PHY_OWNER_ID | VARCHAR (25) | ID of the physical deployment owner for this record.  Physical owners will be where the data is hosted, either on the cross-over server or the owner deployment. |
| CM_LOG_OWNER_ID | VARCHAR (25) | ID of the logical deployment owner for this record.  Logical owners show the deployment where the record was created but doesn't represent if the record is a part of version skew. |
| TREATMENT_DAY_ID | NUMERIC (18,0) | The treatment day row ID of a treatment day in the treatment plan. |
| TREATMENT_DAY_SRC *(deprecated)* | VARCHAR (254) | *** Deprecated *** In table TPL_TXDAYS, the column TREATMENT_DAY_SRC for TPL item 5005 has been deprecated. Formerly this column and item stored the source ID of a treatment day in a treatment plan or therapy plan, but the Treatment Day Source item is no longer maintained in Chroncles, so the column's contents are not reliable. |
| TX_DAY_TYPE_C | VARCHAR (66) |  |
| TREATMENT_DAY_DAT | VARCHAR (50) | The contact date (DAT) of a treatment day record in the treatment plan. |
| TREATMENT_DAY_NAME | VARCHAR (254) | The treatment day name of a treatment day in the treatment plan. |
| TRT_CYCLE | VARCHAR (100) | The cycle containing a treatment day in the treatment plan. |
| TX_STATUS_CHG_DATE *(deprecated)* | DATETIME |  |
| TREATMENT_DATE | DATETIME | The planned date in external format when a treatment day in the treatment plan is expected to occur. |
| PAT_ENC_CSN_ID | NUMERIC (18,0) | The contact serial number (CSN) of the first patient encounter in which an order from this treatment day was released. |
| TRT_DAY_STATUS_C | INTEGER |  |
| TRT_DAY_WAIT_AFTER | NUMERIC (18,0) | The number of days to wait after a treatment day in the treatment plan. |
| TRT_DAY_MAX_LEAD | NUMERIC (18,0) | The max lead of a treatment day in the treatment plan. |
| TRT_DAY_MAX_LAG | NUMERIC (18,0) | The max lag of a treatment day in the treatment plan. |
| TRT_DAY_UNIQ_ID | VARCHAR (254) | A cycle-level unique ID of a treatment day in the treatment plan. |
| TRT_DAY_NUM | INTEGER | The treatment day number for this treatment day. |
| STEP_START_DTTM | 5300 | The start date and time of the step. |
| MANUAL_STRT_STP_YN | VARCHAR (1) |  |
| MANUAL_STRT_USER_ID | VARCHAR (18) | The user who manually started the step. |
| MANUAL_STRT_DTTM | DATETIME (Local) | The date and time when the step was manually started. |
| STEP_DURATION_SECS | NUMERIC (18,0) | This item stores the duration of the step in seconds. This value can be added to the start date and time to get the end date and time of the step. |
| TX_STAT_CHG_USER_ID | VARCHAR (18) | This item stores the ID of the user who changed the status of this treatment day. |
| TX_DAY_UNLINKABL_YN | VARCHAR (1) |  |
| DAY_LENGTH | INTEGER | The number of calendar days that are represented by the treatment day. |
| TX_STATUS_CHG_DTTM | DATETIME (Local) | Stores the instant at which the day status changed. |
| DAY_CREATED_BY_ID | VARCHAR (18) | Stores the ID of the user who created the treatment day. |
| DAY_CREATE_DTTM | DATETIME (Local) | Instant when the treatment day was created. |
| DAY_CREATE_COMMENT | VARCHAR (450) | Additional comment entered by user when creating the treatment day. |
| DAY_SOURCE_UID | VARCHAR (100) | Stores the unique ID of the day from which it was created. |
| TX_PLANNED_DT | DATETIME | Stores the planned date for the treatment day. |
| TX_STARTED_DTTM | DATETIME (UTC) | Stores the instant at which the day was started. |
| DAY_SOURCE_CSN | NUMERIC (18,0) | When the treatment plan day is created from a protocol (PRL), the source treatment day (OSQ)'s contact serial number will be set in this item.  If the treatment plan day is copied or deferred, this item will be copied into the new day. |
| AUTO_COMP_STATUS_C | INTEGER |  |
| TREAT_DAY_CONTACT_DATE_REAL | FLOAT | The contact date real of the treatment day (TRG) record which is held in this row.  The contact date real is a unique, internal contact date in decimal format. The integer portion of the number indicates the date of the contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| DEFERRED_FROM_LN | INTEGER | If this treatment day was created by deferring another treatment day, this item will contain the line number of that deferred treatment day. |
| CONVERSION_SOURCE | INTEGER | If this treatment day is part of a conversion cycle created when converting a plan for transition of treatment, this will be the line number of the corresponding day in the original cycle. |
| CONVERSION_TARGET | INTEGER | If this day was replaced for conversion, this will be the day (given by line in SI TPl 5000) that replaced it. |
| DAY_SOURCE_INSTANCE_NUM | INTEGER | For the clinical protocol treatment day contact indicated by the contact serial number in the DAY_SOURCE_CSN column, this column stores the instance number (or repetition number) represented by this day in the treatment plan. |
| TX_SCHED_DATE | DATETIME | Stores the date for which the treatment day is scheduled. |
| TX_SCHED_CONFLICT_C | INTEGER |  |
| DAY_PATTERN_SOURCE_LINE | INTEGER | For this day, if it was created from a pattern day, this item will store the source line in SI TPL 13000 it was created from. |
| DAY_NOTE_ID | VARCHAR (254) | The unique ID of the note record that contains the notes for a given day in the treatment plan. |
| DAY_CREATION_METHOD_C | INTEGER |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | TREATMENT_PLAN_ID | DENT_TREATMENT | TREATMENT_ID | No | No | No |  |
| 1 | TREATMENT_PLAN_ID | TPL_HSB_EPT_LINK | TREATMENT_PLAN_ID | Unknown | No | No |  |
| 1 | TREATMENT_PLAN_ID | TPL_INFO | TREATMENT_PLAN_ID | No | No | No |  |
| 3 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 4 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 4 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 4 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 5 | TREATMENT_DAY_ID | DENTAL_VISIT_INFO | REGIMEN_ID | No | No | No |  |
| 5 | TREATMENT_DAY_ID | TRG_INFO | REGIMEN_ID | Unknown | No | No |  |
| 5 | TREATMENT_DAY_ID | V_EHI_TRG_FILTER | REGIMEN_ID | Unknown | Unknown | No |  |
| 7 | TX_DAY_TYPE_C | ZC_DAY_TYPE | DAY_TYPE_C | No | No | No |  |
| 13 | PAT_ENC_CSN_ID | ALT_ORD_PROV_SINGL | PAT_ENC_CSN_ID | Unknown | No | No |  |
| 13 | PAT_ENC_CSN_ID | AN_RELINK_INFO | PAT_ENC_CSN_ID | No | No | No |  |
| 13 | PAT_ENC_CSN_ID | DENT_ORTH_EXAM_NOTES | PAT_ENC_CSN_ID | No | No | No |  |
| 13 | PAT_ENC_CSN_ID | FAC_CHG_OVERRIDE | PAT_ENC_CSN_ID | No | No | No |  |
| 13 | PAT_ENC_CSN_ID | FAM_HX_PAT_ONLY | PAT_ENC_CSN_ID | No | No | No |  |
| 13 | PAT_ENC_CSN_ID | F_ED_ENCOUNTERS | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 13 | PAT_ENC_CSN_ID | F_HH_CERT_ATTRIBUTES | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 13 | PAT_ENC_CSN_ID | F_HH_OASIS_SINGLE | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 13 | PAT_ENC_CSN_ID | F_HH_OASIS_SINGLE_2 | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 13 | PAT_ENC_CSN_ID | F_HH_OASIS_SINGLE_3 | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 13 | PAT_ENC_CSN_ID | F_HH_OASIS_SINGLE_4 | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 13 | PAT_ENC_CSN_ID | F_HH_OASIS_SINGLE_5 | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 13 | PAT_ENC_CSN_ID | F_IBD_ADULT_FORM_ENC | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 13 | PAT_ENC_CSN_ID | F_IBD_FORM_RESP | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 13 | PAT_ENC_CSN_ID | F_IP_HSP_ADMISSION | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 13 | PAT_ENC_CSN_ID | F_IP_HSP_SEPSIS3 | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 13 | PAT_ENC_CSN_ID | F_IRIS_ENC | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |

_(204 total; showing first 30)_
