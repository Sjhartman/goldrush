# V_PAT_ADT_LOCATION_HX

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=V_PAT_ADT_LOCATION_HX

## Description

A dimensional view used to find a patient's department, room and/or bed at a given datetime.  The view contains one row for each admission, transfer in, or leave of absence return ADT event and contains columns for in and out times.  By equal joining to this view on an inpatient CSN and theta joining on a given instant, you can find one row with the patient's department, room and bed at the given instant. Please note that this view was tested on ADT from Epic's ADT application. If you are using interfaces to capture ADT data, you may experience odd behavior.

## Metadata

| Property | Value |
| --- | --- |
| Type | View |
| Release Version | Rel 2010 |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| EVENT_ID | NUMERIC (18,0) | The unique ID number of the ADT event record. |
| PAT_ENC_CSN | NUMERIC (18,0) | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| EVENT_TYPE_C | INTEGER |  |
| IN_DTTM | DATETIME (Local) | The instant when the patient was moved to the department/room/bed. |
| OUT_DTTM | DATETIME (Local) | The instant when the patient was moved out of the department/room/bed. If the patient is still in the department/room/bed, this column will return the current instant.   The column PAT_OUT_DTTM will return the instant when the patient was moved out of the department/room/bed, but will return nothing if the patient is still in the department/room/bed. |
| ADT_DEPARTMENT_ID | NUMERIC (18,0) | The ID number of the department of the event record at the effective time. |
| ADT_DEPARTMENT_NAME | VARCHAR (254) | The name of the department. |
| ADT_DEPARTMENT_NM_WID | .2 | A unique department identifier that consists of the name and the department ID. This column is often used for grouping, sorting and display purposes in reports. |
| ADT_ROOM_ID | VARCHAR (18) | The ID number of the room of the event record during the effective time span. |
| ADT_ROOM_CSN | NUMERIC (18,0) | The serial number for the room contact of the event record. This number is unique across all room contacts in the system. |
| ADT_ROOM_NM_WID | .2 | A unique room identifier that consists of the name and the room ID. This column is often used for grouping, sorting and display purposes in reports. |
| ADT_BED_ID | VARCHAR (18) | The ID number of the bed of the event record during the effective time span. |
| ADT_BED_CSN | NUMERIC (18,0) | The serial number for the bed contact of the event record. This number is unique across all bed contacts in the system. |
| ADT_BED_LABEL_WID | .2 | A unique bed identifier that consists of the name and the bed ID. This column is often used for grouping, sorting and display purposes in reports. |
| ADT_LOC_ID | NUMERIC (18,0) | The unique ID of the location that serves as the parent to the department in your facility?s ADT organizational structure. |
| ADT_LOC_NAME | VARCHAR (200) | The name of the ADT location. |
| ADT_LOC_NM_WID | VARCHAR (254) | A unique location identifier that consists of the name and the location ID. This column is often used for grouping, sorting and display purposes in reports. |
| ADT_SERV_AREA_ID | NUMERIC (18,0) | The unique ID for the service area to which this location is assigned. |
| ADT_SERV_AREA_NAME | VARCHAR (200) | The name of the service area. |
| ADT_SERV_AREA_NM_WID | VARCHAR (254) | A unique service area identifier that consists of the name and the service area ID. This column is often used for grouping, sorting and display purposes in reports. |
| PAT_OUT_DTTM | DATETIME (Local) | The instant when the patient was moved out of the department/room/bed. If the patient is still in the department/room/bed, this column will return nothing.   The column OUT_DTTM will return the instant when the patient was moved out of the department/room/bed, but will return the current instant if the patient is still in the department/room/bed. |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | EVENT_ID | ADT_DOC_IDENTIFIERS | EVENT_ID | No | Unknown | No |  |
| 1 | EVENT_ID | ADT_PAS_EPSD_ENC | EVENT_ID | Yes | Unknown | No |  |
| 1 | EVENT_ID | CLARITY_ADT | EVENT_ID | Yes | Unknown | No |  |
| 1 | EVENT_ID | F_IP_HSP_TRANSFER | EVENT_ID | Unknown | Unknown | No |  |
| 1 | EVENT_ID | V_ADT_IP_DISCHARGES | EVENT_ID | Unknown | Unknown | No |  |
| 1 | EVENT_ID | V_ADT_LTC_CENSUS | EVENT_ID | Unknown | Unknown | No |  |
| 1 | EVENT_ID | V_ADT_OBSERVATIONS | EVENT_ID | Unknown | Unknown | No |  |
| 1 | EVENT_ID | V_ADT_OR_ADMITS | EVENT_ID | Unknown | Unknown | No |  |
| 1 | EVENT_ID | V_PAT_PAIN_ASSESSMENT | EVENT_ID | Unknown | Unknown | No |  |
| 2 | PAT_ENC_CSN | ALT_ORD_PROV_SINGL | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 2 | PAT_ENC_CSN | AN_RELINK_INFO | PAT_ENC_CSN_ID | No | Unknown | No |  |
| 2 | PAT_ENC_CSN | DENT_ORTH_EXAM_NOTES | PAT_ENC_CSN_ID | No | Unknown | No |  |
| 2 | PAT_ENC_CSN | FAC_CHG_OVERRIDE | PAT_ENC_CSN_ID | No | Unknown | No |  |
| 2 | PAT_ENC_CSN | FAM_HX_PAT_ONLY | PAT_ENC_CSN_ID | No | Unknown | No |  |
| 2 | PAT_ENC_CSN | F_ED_ENCOUNTERS | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 2 | PAT_ENC_CSN | F_HH_CERT_ATTRIBUTES | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 2 | PAT_ENC_CSN | F_HH_OASIS_SINGLE | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 2 | PAT_ENC_CSN | F_HH_OASIS_SINGLE_2 | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 2 | PAT_ENC_CSN | F_HH_OASIS_SINGLE_3 | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 2 | PAT_ENC_CSN | F_HH_OASIS_SINGLE_4 | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 2 | PAT_ENC_CSN | F_HH_OASIS_SINGLE_5 | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 2 | PAT_ENC_CSN | F_IBD_ADULT_FORM_ENC | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 2 | PAT_ENC_CSN | F_IBD_FORM_RESP | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 2 | PAT_ENC_CSN | F_IP_HSP_ADMISSION | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 2 | PAT_ENC_CSN | F_IP_HSP_SEPSIS3 | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 2 | PAT_ENC_CSN | F_IRIS_ENC | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 2 | PAT_ENC_CSN | F_MU_OBJ_EH_ADMISSION | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 2 | PAT_ENC_CSN | F_MU_QM_EH_2014_ED_VISIT | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 2 | PAT_ENC_CSN | F_MU_QM_EH_2014_IP_ADMSN | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 2 | PAT_ENC_CSN | F_QM_AMI | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |

_(213 total; showing first 30)_
