# V_NOTE_VIEW_INFO

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=V_NOTE_VIEW_INFO

## Description

The replacement tables are V_NOTE_SHARE_W_PAT_INFO, HNO_INFO, ZC_NOTE_TYPE, ZC_NOTE_TYPE_IP, and MYC_PAT_NOTE_VIEW. The replacement columns are documented in the column descriptions for each column in this view. This view displays information about note HNO records in the system, particularly with regards to views of the note in MyChart. This only includes notes that are considered clinical encounter notes. This excludes encounter letters and result notes.

## Metadata

| Property | Value |
| --- | --- |
| Type | View |
| Release Version | Rel 2018 |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| NOTE_ID | VARCHAR (254) | In table V_NOTE_VIEW_INFO, the column NOTE_ID (HNO/.1) will be deprecated in Aug 2027. This column has been replaced by column NOTE_ID (HNO/.1) in table V_NOTE_SHARE_W_PAT_INFO. To look up the deprecated column's value after the Clarity Compass upgrade, use the column NOTE_ID in table V_NOTE_SHARE_W_PAT_INFO to get the NOTE_ID value.  The unique ID of the note. |
| PAT_ID | VARCHAR (18) | In table V_NOTE_VIEW_INFO, the column PAT_ID (EPT/.1) will be deprecated in Aug 2027. This column has been replaced by column PAT_ID (HNO/505) in table V_NOTE_SHARE_W_PAT_INFO. To look up the deprecated column's value after the Clarity Compass upgrade, use the column PAT_ID in table V_NOTE_SHARE_W_PAT_INFO to get the PAT_ID value.  The unique ID assigned to the patient record. This ID may be encrypted if you have elected to use enterprise reporting?s encryption utility. |
| PAT_ENC_CSN_ID | NUMERIC (18,0) | In table V_NOTE_VIEW_INFO, the column PAT_ENC_CSN_ID (EPT/8) will be deprecated in Aug 2027. This column has been replaced by column PAT_ENC_CSN_ID (HNO/508) in table V_NOTE_SHARE_W_PAT_INFO. To look up the deprecated column's value after the Clarity Compass upgrade, use the column PAT_ENC_CSN_ID in table V_NOTE_SHARE_W_PAT_INFO to get the PAT_ENC_CSN_ID value.  A unique serial number for this encounter. This number is unique across all patients and encounters in the system. |
| ENC_START_DTTM | 87317 | In table V_NOTE_VIEW_INFO, the column ENC_START_DTTM (EPT/87317, 87314) will be deprecated in Aug 2027. This column has been replaced by column EFFECTIVE_DATE_DTTM (EPT/87317, 87314) in table V_NOTE_SHARE_W_PAT_INFO. To look up the deprecated column's value after the Clarity Compass upgrade, use the column EFFECTIVE_DATE_DTTM in table V_NOTE_SHARE_W_PAT_INFO to get the EFFECTIVE_DATE_DTTM value.  The start date and time of an encounter. The start date is pulled from the date stored in the EFFECTIVE_DATE_DT column. The time references the first populated time in the following fields: hospital admission time (EPT 18851), hospital temporary admission time (EPT 18847), ADT arrival time (EPT 10815), and expected admission time (EPT 10300).  The SlicerDicer reporting application uses this column to determine the EffectiveStartDate of encounters. |
| ENC_PROV_ID | 7040 | In table V_NOTE_VIEW_INFO, the column ENC_PROV_ID (EPT/7040, 18867) will be deprecated in Aug 2027. This column has been replaced by column AUTH_LNKED_PROV_ID (EMP/17500) in table V_NOTE_SHARE_W_PAT_INFO. To look up the deprecated column's value after the Clarity Compass upgrade, use the column AUTH_LNKED_PROV_ID in table V_NOTE_SHARE_W_PAT_INFO to get the AUTH_LNKED_PROV_ID value.  The unique ID for the visit provider or admission provider associated with this encounter. In cases where there are multiple providers for one encounter, this is the ID of the first provider in the list. This item may be NULL if there is no provider for this encounter. This ID may be encrypted. |
| ENC_DEPARTMENT_ID | NUMERIC (18,0) | In table V_NOTE_VIEW_INFO, the column ENC_DEPARTMENT_ID (EPT/87316) will be deprecated in Aug 2027. This column has been replaced by column ENC_DEPARTMENT_ID (EPT/87316) in table V_NOTE_SHARE_W_PAT_INFO. To look up the deprecated column's value after the Clarity Compass upgrade, use the column ENC_DEPARTMENT_ID in table V_NOTE_SHARE_W_PAT_INFO to get the ENC_DEPARTMENT_ID value.  The effective department ID. The department is found by returning the first department to have a value in the following order: 1) Hospital Unit 2) Procedure Pass Department (the effective department of linked appointment or admission) 3) Hospice Intake Department 4) Appointment Department 5) Waiting List Department 6) OR Department |
| ENC_REV_LOC_ID | NUMERIC (18,0) | In table V_NOTE_VIEW_INFO, the column ENC_REV_LOC_ID (DEP/4001) will be deprecated in Aug 2027. This column has been replaced by column REV_LOC_ID (DEP/4001) in table V_NOTE_SHARE_W_PAT_INFO. To look up the deprecated column's value after the Clarity Compass upgrade, use the column REV_LOC_ID  in table V_NOTE_SHARE_W_PAT_INFO to get the REV_LOC_ID value.  The unique ID of the revenue location to which the department is linked. |
| ENC_SERV_AREA_ID | No | In table V_NOTE_VIEW_INFO, the column ENC_SERV_AREA_ID will be deprecated in Aug 2027. This column has been replaced by column SERV_AREA_ID in table V_NOTE_SHARE_W_PAT_INFO. To look up the deprecated column's value after the Clarity Compass upgrade, use the column SERV_AREA_ID in table V_NOTE_SHARE_W_PAT_INFO to get the SERV_AREA_ID value.  The unique ID of the service area in which this department is located. This is the service area for the department, calculated by the function EPIC_DEPTOSA; this function is needed because the service area is linked to the location record and not to the department record directly. |
| TIMES_READ | INTEGER | In table V_NOTE_VIEW_INFO, the column TIMES_READ (HNO/-1) will be deprecated in Aug 2027. To look up the deprecated column's value after the Clarity Compass upgrade, create a temporary table mycViews:  "SELECT noteView.NOTE_ID,                 COUNT( * ) AS TIMES_READ,                 MIN ( noteView.PATIENT_VIEW_TIME ) AS FIRST_READ_DTTM,                 MAX ( noteView.PATIENT_VIEW_TIME ) AS LAST_READ_DTTM       FROM [{{REPORTING_DATABASE}}]..MYC_PAT_NOTE_VIEW noteView       GROUP BY noteView.NOTE_ID ) mycViews"  Then join the table that references V_NOTE_VIEW_INFO to table HNO_INFO column NOTE_ID, and then join to the temporary table mycViews column NOTE_ID on HNO_INFO.NOTE_ID to get the TIMES_READ value.   The number of times that the HNO record has been viewed in MyChart. |
| FIRST_READ_DTTM | DATETIME (Local) | In table V_NOTE_VIEW_INFO, the column FIRST_READ_DTTM (HNO/32030) will be deprecated in Aug 2027. This column has been replaced by column FIRST_READ_DTTM (HNO/32030) in table V_NOTE_SHARE_W_PAT_INFO. To look up the deprecated column's value after the Clarity Compass upgrade, use the column FIRST_READ_DTTM in table V_NOTE_SHARE_W_PAT_INFO to get the FIRST_READ_DTTM value.  The first time that this note was viewed in MyChart. |
| LAST_READ_DTTM | DATETIME (Local) | In table V_NOTE_VIEW_INFO, the column LAST_READ_DTTM (HNO/32030) will be deprecated in Aug 2027. To look up the deprecated column's value after the Clarity Compass upgrade, create a temporary table mycViews:  "SELECT noteView.NOTE_ID,                 COUNT( * ) AS TIMES_READ,                 MIN ( noteView.PATIENT_VIEW_TIME ) AS FIRST_READ_DTTM,                 MAX ( noteView.PATIENT_VIEW_TIME ) AS LAST_READ_DTTM       FROM [{{REPORTING_DATABASE}}]..MYC_PAT_NOTE_VIEW noteView       GROUP BY noteView.NOTE_ID ) mycViews"  Then join the table that references V_NOTE_VIEW_INFO to table HNO_INFO column NOTE_ID, and then join to the temporary table mycViews column NOTE_ID on HNO_INFO.NOTE_ID to get the LAST_READ_DTTM value.  The most recent time that this note was viewed in MyChart. |
| DAYS_TO_READ | 87317 87314 32030 | In table V_NOTE_VIEW_INFO, the column DAYS_TO_READ (EPT/87317,87314 and HNO/32030) will be deprecated in Aug 2027. To look up the deprecated column's value after the Clarity Compass upgrade, create a temporary table mycViews:  "SELECT noteView.NOTE_ID,                 COUNT( * ) AS TIMES_READ,                 MIN ( noteView.PATIENT_VIEW_TIME ) AS FIRST_READ_DTTM,                 MAX ( noteView.PATIENT_VIEW_TIME ) AS LAST_READ_DTTM       FROM [{{REPORTING_DATABASE}}]..MYC_PAT_NOTE_VIEW noteView       GROUP BY noteView.NOTE_ID ) mycViews"  Then join the table that references V_NOTE_VIEW_INFO to table HNO_INFO column NOTE_ID, and then join to the temporary table mycViews column NOTE_ID on HNO_INFO.NOTE_ID to get the DAYS_TO_READ value.  The number of days between the note's associated encounter start date and the first time that the note was viewed in MyChart. |
| NOTE_TYPE_C | VARCHAR (66) |  |
| NOTE_TYPE_NAME | VARCHAR (254) |  |
| UCN_NOTE_TYPE_C | VARCHAR (66) |  |
| UCN_NOTE_TYPE_NAME | VARCHAR (254) |  |
| AMB_NOTE_YN | VARCHAR (1) |  |
| UNSIGNED_YN | VARCHAR (1) |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | NOTE_ID | ABN_NOTES | ABN_NOTE_ID | Unknown | Unknown | No |  |
| 1 | NOTE_ID | ABN_NOTE_INFO | NOTE_ID | No | Unknown | No |  |
| 1 | NOTE_ID | CODING_CLA_NOTES | NOTE_ID | Unknown | Unknown | No |  |
| 1 | NOTE_ID | FA_NOTES_QUERY | NOTE_ID | No | Unknown | No |  |
| 1 | NOTE_ID | FIN_ASST_LETTER | NOTE_ID | No | Unknown | No |  |
| 1 | NOTE_ID | FIN_ASST_NOTE | NOTE_ID | No | Unknown | No |  |
| 1 | NOTE_ID | HNO_CVG_REQUEST | NOTE_ID | Unknown | Unknown | No |  |
| 1 | NOTE_ID | HNO_INFO | NOTE_ID | No | Unknown | No |  |
| 1 | NOTE_ID | HNO_INFO_2 | NOTE_ID | No | Unknown | No |  |
| 1 | NOTE_ID | HNO_MYC_LET_INFO | NOTE_ID | No | Unknown | No |  |
| 1 | NOTE_ID | HSP_ACCT_LETTERS | NOTE_ID | Unknown | Unknown | No |  |
| 1 | NOTE_ID | HSP_ACCT_NOTES | NOTE_ID | Unknown | Unknown | No |  |
| 1 | NOTE_ID | LETTER_EXTERNAL_INFO | NOTE_ID | No | Unknown | No |  |
| 1 | NOTE_ID | NOTES_ACCT | NOTE_ID | Unknown | Unknown | No |  |
| 1 | NOTE_ID | NOTES_LAB | NOTE_ID | Unknown | Unknown | No |  |
| 1 | NOTE_ID | NOTES_MC_CLM | NOTE_ID | Unknown | Unknown | No |  |
| 1 | NOTE_ID | NOTES_MC_PBA | NOTE_ID | No | Unknown | No |  |
| 1 | NOTE_ID | NOTES_MC_SER | NOTE_ID | Unknown | Unknown | No |  |
| 1 | NOTE_ID | NOTE_PARENT_NOTE | NOTE_ID | No | Unknown | No |  |
| 1 | NOTE_ID | PATIENT_FYI_FLAGS | NOTE_ID | Unknown | Unknown | No |  |
| 1 | NOTE_ID | REG_HX_NOTES | NOTE_ID | Unknown | Unknown | No |  |
| 1 | NOTE_ID | SAVED_LETTER_HNO | NOTE_ID | Unknown | No | No |  |
| 1 | NOTE_ID | V_EHI_PBA_NOTES_MC_PBA | NOTE_ID | Unknown | Unknown | No |  |
| 1 | NOTE_ID | V_NOTE_CHARACTERISTICS | NOTE_ID | Unknown | Unknown | No |  |
| 1 | NOTE_ID | V_NOTE_SHARE_W_PAT_INFO | NOTE_ID | Unknown | Unknown | No |  |
| 2 | PAT_ID | ANTICOAG_SELF_REGULATING | PAT_ID | No | Unknown | No |  |
| 2 | PAT_ID | CARE_COORDINATION | PAT_ID | Unknown | Unknown | No |  |
| 2 | PAT_ID | CLAIMS_DERIVE_PAT_FLAGS | PAT_ID | No | Unknown | No |  |
| 2 | PAT_ID | COMMUNITY_RESRC_REVIEWED | PAT_ID | No | Unknown | No |  |
| 2 | PAT_ID | D_PAT_GEOGRAPHIC_CLASS | PAT_ID | Unknown | Unknown | No |  |

_(269 total; showing first 30)_
