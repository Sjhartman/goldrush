# OB_TOTAL

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=OB_TOTAL

## Description

This patient information table holds the obstetrics information for each patient history contact.  The table contains information on multiple births, induced abortions, spontaneous abortions, ectopics, molars, gravidity, parity, abortions, related comments, full-term, premature, living, and live births.  These values are all running totals across the patient's lifetime, calculated at the time of the history contact.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | EPT |
| Release Version | SPRING 2007 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| PAT_ENC_CSN_ID | NUMERIC (18,0) | Contact serial number is unique across all patients and all contacts |
| PAT_ID | VARCHAR (18) | The unique ID assigned to the patient record. This ID may be encrypted if you have elected to use enterprise reporting?s encryption utility. |
| PAT_ENC_DATE_REAL | No | This is a numeric representation of the date of this encounter in your system. The integer portion of the number specifies the date of the encounter. The digits after the decimal point indicate multiple visits on one day. |
| CONTACT_DATE | DATETIME | The date for the encounter in standard date format. Note: There may be multiple encounters on the same calendar date. |
| CM_CT_OWNER_ID | VARCHAR (25) | ID of the deployment owner for this contact. |
| OB_MULTIPLE_BIRTHS | INTEGER | This column holds the number of multiple births. |
| OB_THERAPEUTIC_AB | INTEGER | This column holds the number of induced abortions. Along with values in columns OB_SPONTANEOUS_AB and OB_ECTOPICS comprise OB_ABORTIONS. |
| OB_SPONTANEOUS_AB | INTEGER | This column holds the number of spontaneous abortions.  Along with the value in OB_THERAPEUTIC_AB and OB_ECTOPICS, comprise OB_ABORTIONS. |
| OB_ECTOPICS | INTEGER | This column holds the number of ectopic pregnancies. This number is included with the values in column OB_THERAPEUTIC_AB and OB_SPONTANEOUS_AB to calculate the value in OB_ABORTIONS. |
| OB_GPTPAL_C *(deprecated)* | INTEGER |  |
| OB_GRAVIDITY | VARCHAR (254) | This column holds the number of total pregnancies for a patient. This column is the sum of the values in columns OB_PARITY and OB_ABORTIONS. |
| OB_PARITY | VARCHAR (254) | The column contains information regarding how many pregnancies the patient carried past a gestational age (GA) of 24 weeks. The value in this column, along with the value in OB_ABORTIONS,  comprises OB_GRAVIDITY. |
| OB_ABORTIONS | VARCHAR (254) | This item is used to comment on obstetrics abortions reported at each contact. This column along with value in column OB_PARITY, makes up column OB_GRAVIDITY.  This item is the sum total of columns OB_THERAPEUTIC_AB, OB_SPONTANEOUS_AB, OB_ECTOPICS. |
| OB_COMMENT | VARCHAR (254) | This holds general comments for the patient's obstetric history. |
| OB_FULL_TERM | VARCHAR (254) | This holds the number of full term pregnancies for a patient.  Along with the value in column OB_PREMATURE, sums to the value in column OB_PARITY. |
| OB_PREMATURE | VARCHAR (254) | This items holds the number of pregnancies which ended at a premature gestational age (GA). Along with column OB_FULL_TERM, sums to OB_PARITY. |
| OB_LIVING | VARCHAR (254) | This item holds the number of the patient's currently living children as documented in the obstetric history. |
| OB_PREG_HX_C | INTEGER |  |
| HX_LINK_ENC_CSN_ID | NUMERIC (18,0) | This column will link a history encounter to the patient encounter it is associated with, if one exists. If the history was updated outside of the context of an encounter, then it will be null.  This column can be used to link to the PAT_ENC and PAT_ENC_HSP tables on the PAT_ENC_CSN_ID column. |
| OB_LIVE_BIRTHS | VARCHAR (254) | A count of the number of children born alive for a patient. |
| OB_MOLAR | VARCHAR (254) | The number of molar pregnancies the patient has had. |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| B-TREE INDEX | EIX_OB_TOTAL_CONTACT | PAT_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_OB_TOTAL_CONTACT | PAT_ENC_DATE_REAL | 2 | Yes | Yes |  |

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

_(274 total; showing first 30)_
