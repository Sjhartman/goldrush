# DOCS_RCVD_PED_VITALS

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=DOCS_RCVD_PED_VITALS

## Description

Contains pediatric vitals (aka birth history) received through external documents and stored in DXR.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | DXR |
| Release Version | Rel 2018 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| DOCUMENT_ID | NUMERIC (22,0) | The unique identifier (.1 item) for the document record. |
| CONTACT_DATE_REAL | FLOAT | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| LINE | INTEGER | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| CONTACT_DATE | DATETIME | The date of this contact in calendar format. |
| PED_VITAL_REF_ID | VARCHAR (174) | This item stores the unique reference identifier associated with the pediatric vital. |
| PED_VITAL_SOURCE_VALUE | VARCHAR (40) | This item stores the source value of a received pediatric vital before it is converted. |
| PED_VITAL_SOURCE_UNIT | VARCHAR (40) | This item stores the source unit of a received pediatric vital before it is converted. |
| PED_VITAL_BIRTH_LENGTH_CM | NUMERIC (18,2) | This item stores the patient birth length (unit is cm). |
| PED_VITAL_BIRTH_WEIGHT_KG | NUMERIC (18,2) | This item stores the patient weight when discharged after birth (unit is kg). |
| PED_VITAL_BIRTH_HC_IN_CM | NUMERIC (18,2) | This item stores the patient head circumference at birth (unit is cm). |
| PED_VITAL_APGAR_1_C | INTEGER |  |
| PED_VITAL_APGAR_5_C | INTEGER |  |
| PED_VITAL_APGAR_10_C | INTEGER |  |
| PED_VITAL_GEST_AGE | INTEGER | This item stores the patient gestation age at birth (unit is days). |
| PED_VITAL_NOURISH_HAD_BM_YN | VARCHAR (1) |  |
| PED_VITAL_NRSH_MTHD_HAD_FRM_YN | VARCHAR (1) |  |
| PED_VITAL_DELIV_METHOD_C | VARCHAR (66) |  |
| PED_VITAL_HOSP_DAYS | NUMERIC (18,2) | This item stores the duration of the patient stay at birth (unit is days). |
| PED_VITAL_DISCHARGE_WEIGHT_KG | NUMERIC (18,2) | This item stores the patient weight when discharged after birth (unit is kg). |
| PED_VITAL_MULT_BIRTH_TOTAL_NUM | INTEGER | This item holds the total number of births during the mother's labor and delivery of this newborn patient. |
| PED_VITAL_MULTI_BIRTH_ORDER | INTEGER | For multiple births, the place in the birth order of the current newborn patient. |
| PED_VITAL_CHECKSUM | INTEGER | This item stores the checksum associated with the pediatric vital. |
| PED_VITAL_SOURCE_DXR_CSN | NUMERIC (22,0) | This item will store the contact serial number of the DXR record that owns the instance of this ped vital. |
| PED_VITAL_LAST_UPD_DTTM | DATETIME (UTC) | This item stores the instant the vitals were most recently updated. |
| PED_VITAL_SINGLE_SRC_ORG_ID | NUMERIC (18,0) | This item stores the source organizations for Pediatric Vitals with single sources. |
| PAT_DEL_UTC_DTTM | DATETIME (UTC) | Patient delivery instant (UTC). |
| PED_VITAL_NOUR_METH_C | INTEGER |  |
| PED_VITAL_LABOR_DURATION | VARCHAR (254) | Stores the duration of labor. |
| PED_VITAL_HOSP_NAME | VARCHAR (254) | This item stores the name of the hospital where the patient was born. |
| PED_VITAL_HOSP_LOC | VARCHAR (254) | This item stores the location of the hospital where born. |
| PED_VITAL_COMMENT | VARCHAR (254) | This item stores the comments for a patient's birth history. |
| DELIVERY_EVENT_REF_IDENT | VARCHAR (174) | Stores the reference ID for the newborn encounter for the vital |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | DOCUMENT_ID | DOCS_RCVD | DOCUMENT_ID | Unknown | No | No |  |
| 1 | DOCUMENT_ID | DOCS_RCVD_FMK_INFO | DOCUMENT_ID | No | No | No |  |
| 1 | DOCUMENT_ID | V_EHI_DXR_LINKED_PATS | DOCUMENT_ID | Unknown | Unknown | No |  |
| 1 | DOCUMENT_ID | DISPENSE_QUERY_INFO | DOCUMENT_ID | No | No | No |  |
| 2 | CONTACT_DATE_REAL | CONTACT_DATE_REAL |  |  |  |  |  |
| 1 | DOCUMENT_ID | DOCS_RCVD_DETAILS | DOCUMENT_ID | Unknown | No | No |  |
| 2 | CONTACT_DATE_REAL | CONTACT_DATE_REAL |  |  |  |  |  |
| 1 | DOCUMENT_ID | DOCS_RCVD_DETAILS_2 | DOCUMENT_ID | No | No | No |  |
| 2 | CONTACT_DATE_REAL | CONTACT_DATE_REAL |  |  |  |  |  |
| 1 | DOCUMENT_ID | DOCS_RCVD_DETAILS_3 | DOCUMENT_ID | No | No | No |  |
| 2 | CONTACT_DATE_REAL | CONTACT_DATE_REAL |  |  |  |  |  |
| 1 | DOCUMENT_ID | DOCS_RCVD_SFM_QUERY_INFO | DOCUMENT_ID | No | No | No |  |
| 2 | CONTACT_DATE_REAL | CONTACT_DATE_REAL |  |  |  |  |  |
| 1 | DOCUMENT_ID | MEDCOM_RCVD_DETAILS | DOCUMENT_ID | No | No | No |  |
| 2 | CONTACT_DATE_REAL | CONTACT_DATE_REAL |  |  |  |  |  |
| 11 | PED_VITAL_APGAR_1_C | ZC_OB_DEL_APGAR_1 | OB_DEL_APGAR_1_C | No | No | No |  |
| 12 | PED_VITAL_APGAR_5_C | ZC_OB_DEL_APGAR_1 | OB_DEL_APGAR_1_C | No | No | No |  |
| 13 | PED_VITAL_APGAR_10_C | ZC_OB_DEL_APGAR_1 | OB_DEL_APGAR_1_C | No | No | No |  |
| 17 | PED_VITAL_DELIV_METHOD_C | ZC_DELIVERY_TYPE | DELIVERY_TYPE_C | No | No | No |  |
| 17 | PED_VITAL_DELIV_METHOD_C | ZC_PED_DELIVR_METH | PED_DELIVR_METH_C | No | No | No |  |
| 25 | PED_VITAL_SINGLE_SRC_ORG_ID | ORG_DETAILS | ORGANIZATION_ID | No | No | No |  |
| 25 | PED_VITAL_SINGLE_SRC_ORG_ID | ORG_DETAILS_COSMOS | ORGANIZATION_ID | No | No | No |  |
| 25 | PED_VITAL_SINGLE_SRC_ORG_ID | ORG_E_RX_NETWORK | ORGANIZATION_ID | No | No | No |  |
| 27 | PED_VITAL_NOUR_METH_C | ZC_PED_NOUR_METH | PED_NOUR_METH_C | No | No | No |  |
