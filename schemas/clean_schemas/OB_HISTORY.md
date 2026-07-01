# OB_HISTORY

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=OB_HISTORY

## Description

Stores the patients OB history. Only the most recent history contact is in this view.

## Metadata

| Property | Value |
| --- | --- |
| Type | View |
| Release Version | SPRING 2007 |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| PAT_ENC_CSN_ID | NUMERIC (18,0) | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| LINE | INTEGER | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| PAT_ID | VARCHAR (18) | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| PAT_ENC_DATE_REAL | FLOAT | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| CONTACT_DATE | DATETIME | The date of this contact in calendar format. |
| CM_CT_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this contact. This is only populated if you use IntraConnect. |
| OB_HX_MULT_PREG_GRP | No | Contains a date that groups the births for pregnancies with multiple births. It is recommended to use OB_HX_PREG_EPS_ID instead of this column |
| OB_HX_OUTCOME_DT | DATETIME (Local) | The outcome date and time.    For values that are not fully confident (for example, if just the year was documented), the confidence is stored in the OB_HSB_DELIVERY.OB_HX_OUTC_FUZZY_C column. For those values, this column contains the local time zone representation of midnight on the earliest date that the value could represent, relative to the time zone where the delivery was documented. |
| OB_HX_GEST_AGE | VARCHAR (254) | The gestational age of the newborn at the time of delivery. |
| OB_HX_DEL_TYPE_C | VARCHAR (66) |  |
| OB_HX_DELIVERY_SITE | 35803 |  |
| OB_HX_CLINICIAN | .2 | The name of the clinician who attended the delivery.  If there is any value in OB_HSB_DELIVERY.OB_DEL_DELIV_MD_ID, the name of that provider will be displayed. If there is no value in OB_DEL_DELIV_MD_ID, the free text comment from OB_HSB_DELIVERY.OB_HX_CLINICIAN_FT will be displayed. |
| OB_HX_LABOR_LENGTH | 35101 | The length of the first stage of labor in minutes. |
| OB_HX_BIRTH_WEIGHT | NUMERIC (18,2) | The weight of the newborn at the time of birth in ounces. |
| OB_HX_INFANT_SEX_C | VARCHAR (66) |  |
| OB_HX_INFANT_NAME | VARCHAR (254) | The name of the newborn. |
| OB_HX_APGAR_1 | INTEGER |  |
| OB_HX_ANESTH_C | VARCHAR (66) |  |
| OB_HX_IS_LIVING_C | INTEGER |  |
| OB_HX_PREGNANCY_CMT | VARCHAR (254) | The free text comments regarding the pregnancy or delivery. |
| OB_HX_APGAR_5 | INTEGER |  |
| OB_HX_SRC_C *(deprecated)* | INTEGER |  |
| OB_HX_OUTCOME_C | INTEGER |  |
| OB_HX_PRETERM_LA_YN | VARCHAR (1) |  |
| OB_HX_LAB_LEN_2ND | 35100 | The length of the second stage of labor in minutes. |
| OB_HX_PREG_EPS_ID | NUMERIC (18,0) | The unique ID associated with the pregnancy episode for this outcome. |
| HX_LINK_ENC_CSN_ID | NUMERIC (18,0) | The unique contact serial number (CSN) of the patient encounter this history contact is associated with, if one exists. If the history was updated outside of the context of an encounter, then it will be null. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| OB_HX_DEL_REC_ID | NUMERIC (18,0) | The unique ID associated with the delivery record for this outcome. |
| OB_HX_PREG_ORDER | INTEGER | The order in which a given pregnancy occurred in relation to all documented pregnancies. |

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
| 1 | PAT_ENC_CSN_ID | F_SCHED_APPT | PAT_ENC_CSN_ID | Unknown | Unknown | No |  |
| 1 | PAT_ENC_CSN_ID | HAUD_ENC | ENC_CSN | Unknown | Unknown | No |  |

_(350 total; showing first 30)_
