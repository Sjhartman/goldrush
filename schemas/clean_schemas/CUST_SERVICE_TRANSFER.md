# CUST_SERVICE_TRANSFER

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=CUST_SERVICE_TRANSFER

## Description

The CUST_SERVICE_TRANSFER table contains information about patient transfer requests that have been documented in a customer service communication record. This can be used to report on communication documented by staff who facilitate calls between referring providers and admitting providers for potential transfer patients.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | NCS |
| Release Version | Rel 2015 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| COMM_ID | NUMERIC (18,0) | The unique ID of the customer service communication record. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| TRANS_PAT_SSN | VARCHAR (192) | The social security number of the patient for whom the transfer is requested. |
| TRANS_REF_PROV | VARCHAR (50) | The name of the referring provider who is requesting the patient be transferred. |
| TRANS_PAT_NAME | VARCHAR (50) | The name of the patient for whom the transfer is requested. |
| TRANS_PAT_AGE | INTEGER | The age of the patient for whom the transfer is requested. |
| TRANS_PAT_SEX_C | VARCHAR (66) |  |
| TRANS_PAT_POINT_OF_ORIGIN_C | VARCHAR (66) |  |
| TRANS_REASON_C | INTEGER |  |
| TRANS_LVL_OF_CARE_C | VARCHAR (66) |  |
| TRANS_PAT_CLASS_C | VARCHAR (66) |  |
| TRANS_ACCOMMODATION_CODE_C | VARCHAR (66) |  |
| TRANS_ACCOMMODATION_REASON_C | INTEGER |  |
| TRANS_HOSPITAL_SERVICE_C | VARCHAR (66) |  |
| TRANS_NEEDED_BY_DT | DATETIME | The date the patient transfer is needed by. |
| TRANS_CLIN_ACCEPTED_YN | VARCHAR (1) |  |
| TRANS_CLIN_DECISION_USER_ID | VARCHAR (18) | The unique ID of the user who recorded the clinical decision for the transfer request. |
| TRANS_FIN_ACCEPTED_YN | VARCHAR (1) |  |
| TRANS_FIN_DECISION_USER_ID | VARCHAR (18) | The unique ID of the user who recorded the financial decision for the transfer request. |
| TRANS_DECISION_REASON_C | INTEGER |  |
| TRANS_REF_ORG_C | INTEGER |  |
| TRANS_PAT_DOB_DT | DATETIME | The date of birth of the patient for whom the transfer is requested. |
| TRANS_CLIN_DECISION_DATETIME | DATETIME (UTC) | The date and time when the clinical decision regarding the patient transfer request was recorded. |
| TRANS_FIN_DECISION_DATETIME | DATETIME (UTC) | The date and time when the financial decision regarding the patient transfer request was recorded. |
| REQUEST_STATUS_C | INTEGER |  |
| DEST_DECLINE_RSN_C | INTEGER |  |
| CANCEL_STATUS_RSN_C | INTEGER |  |
| CANCEL_STATUS_CAT_C | INTEGER |  |
| DEST_DECLINE_CAT_C | INTEGER |  |
| REFERRING_PROV_ID | VARCHAR (18) | The unique ID of the provider record documented as the referring provider for a transfer center request. |
| REFERRING_LOC_ID | NUMERIC (18,0) | The unique ID of the location record documented as the referring location for a transfer center request. |
| TRANSFER_TYPE_C | INTEGER |  |
| REFERRING_LOC_IS_OTHER_YN | VARCHAR (1) |  |
| FREETEXT_REFERRING_LOC_NAME | VARCHAR (80) | The referring location of a Transfer Center request, stored as free text. |
| REQUEST_IS_EMTALA_YN | VARCHAR (1) |  |
| TRANSFER_REGION_ID | NUMERIC (18,0) | Region associated with the Transfer Center request. |
| DEST_LOC_ID | NUMERIC (18,0) | Location associated with this destination planning record for a Transfer Center request. |
| MODE_OF_TXPORT_C | VARCHAR (66) |  |
| TXPORT_SERVICE_ID | NUMERIC (18,0) | Which EMS/Transportation service will be in charge of moving a transferred patient from the referring location to the destination location. |
| TXPORT_SERVICE_IS_OTHER_YN | VARCHAR (1) |  |
| TXPORT_CONTACT_NUM | VARCHAR (50) | The contact number for the transportation service provider moving the patient to the destination location. |
| EXPECTED_ARRIVAL_DTTM | 11506 | The date and time the patient is expected to arrive at the destination location. |
| TXPORT_DISPATCH_UTC_DTTM | DATETIME (UTC) | The date and time that the transportation service provider was dispatched to pick up the patient being transferred. |
| TXPORT_PICK_UP_UTC_DTTM | DATETIME (UTC) | The date and time that the patient was picked up from the referring location. |
| PAT_ARRIVAL_UTC_DTTM | DATETIME (UTC) | What time the patient arrived at the destination location. |
| FREETEXT_TXPORT_SERVICE_NAME | VARCHAR (60) |  |
| SOURCE_ADMISSION_DTTM | 11400 | The date and time of a request's source encounter. For manually entered encounters.  For linked hospital encounters, use PAT_ENC_HSP__INP_ADM_DATE, for the inpatient admission date/time, and/or PAT_ENC_HSP__HOSP_ADMSN_TIME, for the date and time that the patient was first admitted to the facility, bedded in the ED, or confirmed for an HOV for this contact, regardless of patient's base patient class.  For appointment encounters, use  PAT_ENC_APPT__CONTACT_DATE for the date and PAT_ENC_APPT__PROV_START_TIME for the time. |
| SOURCE_ADMSN_LVL_OF_CARE_C | VARCHAR (66) |  |
| TRANS_BACK_TO_REFERRING_LOC_YN | VARCHAR (1) |  |
| PAT_IS_IN_STATE_RESIDENT_YN | VARCHAR (1) |  |
| TRANS_REFER_ZONE_C | INTEGER |  |
| TRANS_REQ_ZONE_C | INTEGER |  |
| TRANS_DEST_ZONE_C | INTEGER |  |
| REQUESTED_DEST_LOC_ID | NUMERIC (18,0) | Holds the record ID of the EAF record for the requested destination of the Transfer Center request. |
| TC_PRIORITY_C | INTEGER |  |
| TC_PRIORITY_SRC_C | INTEGER |  |
| PRIN_ACC_PROV_CONTACT_IDENT | INTEGER | This stores the line number of the Contact Log entry that is the principal accepting provider for the Transfer Center request. |
| REFERRING_PROV_ADDR_ID | VARCHAR (30) | This provides a link to the address of the referring provider. To obtain the address information, join to the table CLARITY_SER_ADDR on the ADDR_UNIQUE_ID column. If you use IntraConnect, you also need to join the REFERRING_PROV_ID column to CLARITY_SER_ADDR.PROV_ID. |
| TARGET_DEST_COMM_ID | NUMERIC (18,0) | Holds the child NCS record of this record that represents the target destination. |
| FIRST_REQUEST_TYPE_C | VARCHAR (66) |  |
| FIRST_TRANSFER_TYPE_C | INTEGER |  |
| TC_NEEDS_TXPORT_YN | VARCHAR (1) |  |
| TXPORT_REFERRING_FACILITY_YN | VARCHAR (1) |  |
| TXPORT_ADDRESS_HOUSE_NUMBER | VARCHAR (254) | House number/building number for a transfer center request's pickup location |
| TXPORT_ADDRESS_CITY | VARCHAR (60) | City for transfer center request's pickup address. |
| TXPORT_ADDRESS_STATE_C | VARCHAR (66) |  |
| TXPORT_ADDRESS_ZIP | VARCHAR (20) | Zip code for transfer center request's pickup address. |
| TXPORT_ADDRESS_DISTRICT_C | INTEGER |  |
| TXPORT_ADDRESS_COUNTY_C | VARCHAR (66) |  |
| TXPORT_ADDRESS_COUNTRY_C | VARCHAR (66) |  |
| SOURCE_ENC_DEPT | VARCHAR (91) | The department where a source encounter on a request occurred. For manually entered encounters.  For linked hospital encounters, use PAT_ENC_HSP__DEPARTMENT_ID. For linked appointment encounters, use PAT_ENC_APPT__DEPARTMENT_ID. |
| SOURCE_ENC_ROOM_AND_BED | VARCHAR (401) | The bed (and room, if applicable) that a patient was assigned to in a manually entered source encounter.  For linked hospital encounters, use  PAT_ENC_HSP__ROOM_ID and PAT_ENC_HSP__BED_ID instead. |
| SOURCE_ENC_NO_ENC_YN | VARCHAR (1) |  |
| MOCK_RECORD_YN | VARCHAR (1) |  |
| REPORTING_REGION_RECORD_ID | NUMERIC (18,0) | This links to the associated Transfer Center reporting region (SEC) record found in NCS 11130. If the login locations of the core Transfer Center region are updated, this reporting region maintains the original login locations for historical reporting. |
| LINKED_TRANSFER_PEND_ID | VARCHAR (18) | If this request is a direct transfer, then this item will link to the transfer pend. It will not be populated for new encounter pends. |
| TC_FUTURE_RSN_C | INTEGER |  |
| TRANS_REVERT_STATUS_DATE | DATETIME | Stores the date for when this request will move from the future request status back to pending. |
| TRANS_FUTURE_COMMENT | VARCHAR (236) | Stores a comment related to the reason for putting this request into the Future tab. |
| TC_REQUEST_STATUS_MOD_C | INTEGER | Surrogate key used to uniquely identify rows in this (and only this) table on Cogito Cloud only, do not assume the surrogate key in this table will correspond to the surrogate key in another table |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | COMM_ID | CUST_SERVICE | COMM_ID | Unknown | No | No |  |
| 1 | COMM_ID | CUST_SERVICE_2 | COMM_ID | No | No | No |  |
| 1 | COMM_ID | CUST_SERV_ORG_FILTER_SA | COMM_ID | No | No | No |  |
| 1 | COMM_ID | V_ADT_TC_DEST | COMM_ID | Unknown | Unknown | No |  |
| 1 | COMM_ID | V_ADT_TRANSFER_CENTER | COMM_ID | Unknown | Unknown | No |  |
| 2 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 2 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 2 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 3 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 8 | TRANS_PAT_SEX_C | ZC_PREF_PCP_SEX | PREF_PCP_SEX_C | No | No | No |  |
| 8 | TRANS_PAT_SEX_C | ZC_SEX | RCPT_MEM_SEX_C | No | No | No |  |
| 9 | TRANS_PAT_POINT_OF_ORIGIN_C | ZC_ADM_SOURCE | ADMIT_SOURCE_C | No | No | No |  |
| 10 | TRANS_REASON_C | ZC_TRANS_REASON | TRANS_REASON_C | No | No | No |  |
| 11 | TRANS_LVL_OF_CARE_C | ZC_LVL_OF_CARE | LEVEL_OF_CARE_C | No | No | No |  |
| 12 | TRANS_PAT_CLASS_C | ZC_ACCT_CLASS_HA | ACCT_CLASS_HA_C | No | No | No |  |
| 12 | TRANS_PAT_CLASS_C | ZC_OVERRIDE_CLASS | OVERRIDE_CLASS_C | No | No | No |  |
| 12 | TRANS_PAT_CLASS_C | ZC_PAT_CLASS | ADT_PAT_CLASS_C | No | No | No |  |
| 13 | TRANS_ACCOMMODATION_CODE_C | ZC_ACCOMMODATION | ACCOMMODATION_C | No | No | No |  |
| 14 | TRANS_ACCOMMODATION_REASON_C | ZC_ACCOM_REASON | ACCOM_REASON_C | No | No | No |  |
| 15 | TRANS_HOSPITAL_SERVICE_C | ZC_PAT_SERVICE | HOSP_SERV_C | No | No | No |  |
| 15 | TRANS_HOSPITAL_SERVICE_C | ZC_PRIM_SVC_HA | PRIM_SVC_HA_C | No | No | No |  |
| 15 | TRANS_HOSPITAL_SERVICE_C | ZC_SCNDRY_SVC_HA | SCNDRY_SVC_HA_C | No | No | No |  |
| 18 | TRANS_CLIN_DECISION_USER_ID | CLARITY_EMP | USER_ID | Unknown | No | No |  |
| 18 | TRANS_CLIN_DECISION_USER_ID | CLARITY_EMP_2 | USER_ID | Unknown | No | No |  |
| 18 | TRANS_CLIN_DECISION_USER_ID | CLARITY_EMP_3 | USER_ID | Unknown | No | No |  |
| 18 | TRANS_CLIN_DECISION_USER_ID | CLARITY_EMP_4 | USER_ID | No | No | No |  |
| 18 | TRANS_CLIN_DECISION_USER_ID | CLARITY_EMP_DEMO | USER_ID | No | No | No |  |
| 18 | TRANS_CLIN_DECISION_USER_ID | EMP_BASIC_INFO | USER_ID | No | No | No |  |

_(236 total; showing first 30)_
