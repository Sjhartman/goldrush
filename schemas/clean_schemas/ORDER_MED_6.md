# ORDER_MED_6

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=ORDER_MED_6

## Description

This table enables you to report on medications ordered. This table should be used with ORDER_MED.

**Overflow table** for ORDER_MED (139 cols). Contains additional columns for the same records — join on the shared primary key column.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | ORD |
| Release Version | Rel May 2021 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| ORDER_MED_ID | NUMERIC (18,0) | The unique identifier for the medication order record. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| AUTH_SER_ADDRESS_ID | VARCHAR (508) | The unique ID for the address of the order's authorizing provider. It is used to identify an address using the address unique ID (I SER 21000) stored in the provider record. |
| ORDER_SER_ADDR_ID | VARCHAR (508) | The unique ID for the address of the order's ordering provider. It is used to identify an address using the address unique ID (I SER 21000) stored in the provider record. |
| SUP_SER_ADDRESS_ID | VARCHAR (508) | The unique ID for the address of the order's supervising provider. It is used to identify an address using the address unique ID (I SER 21000) stored in the provider record. |
| NORWAY_FEST_REIMB_PURSUANT_C | INTEGER |  |
| NORWAY_REIMBURSEMENT_CODE | VARCHAR (150) | Reimbursement Code for Norway |
| NORWAY_REIMBURSEMENT_DX_ID | NUMERIC (18,0) | Reimbursement diagnosis for Norway H-prescriptions |
| HELFO_APPLICATION_YN | VARCHAR (1) |  |
| HELFO_SENT_DATE | DATETIME | Helfo application sent date for Norway Reimbursement |
| HELFO_VALID_DATE | DATETIME | The date until which the Helfo application for Norway Reimbursement is valid |
| HELFO_APPLICANT_NAME | VARCHAR (200) | Name of the provider who applied for Helfo approval for Norway Reimbursement |
| BRUKSOMRADE | VARCHAR (280) | The bruksomr?de ("area of use") of an order, similar in concept to Indications of Use. |
| BRUKSOMRADE_MEDICAL_COND_ID | NUMERIC (18,0) | The bruksomr?de ("area of use") of an order, similar in concept to Indications of Use. This is set when a user chooses a discrete value when placing an order. |
| ASSISTANCE_MEDICAL_COND_ID | NUMERIC (18,0) | The unique ID associated with an Indication that is used to justify the use of an expensive medication for a patient. |
| ASSISTANCE_ELIGIBILITY_FREETXT | VARCHAR (1000) | The reason why an Indication record was not selected by the user. |
| BLOOD_SUGAR_TESTS_PER_DAY | INTEGER | Integer storing the number of blood sugar tests per day for an order |
| INITIATED_PROV_ID | VARCHAR (18) | Stores a reference to a SER record to indicate who initiated an order |
| INITIATED_ORG_LOC_ID | NUMERIC (18,0) | Stores reference to EAF record that corresponds to the initiated organizaiton |
| EXPECTED_FILL_DATE | DATETIME | This item encapsulates the logic used to determine when prescriptions at integrated pharmacies are due for fills. The date in this item accounts for factors such as duplicate prescriptions, fills in progress, and pending RARs. |
| USE_DISCRETE_ANTICOAG_DOSE_C | INTEGER |  |
| TEMP_LONG_TERM_IN_C | INTEGER |  |
| MIXTURE_INFO | VARCHAR (1500) | Stores the free text mixture preparation information. |
| PRIORITIZED_INST_UTC_DTTM | DATETIME (UTC) | This item stores the prioritized instant (date and time) for an order in UTC time zone. It represents the most relevant date and time an action was taken on an order. |
| PRIORITIZED_INST_DTTM | DATETIME (Local) | This item stores the prioritized instant (date and time) for an order in local time zone. It represents the most relevant date and time an action was taken on an order. |
| NEXT_SCH_INST_AT_DISCON_DTTM | DATETIME (Local) | The next scheduled date and time for the order at the time of discontinue. |
| NEXT_SCH_AT_DISCON_OFF_SCH_YN | VARCHAR (1) |  |
| ORD_SIG_HAS_IOU_YN | VARCHAR (1) |  |
| MED_DIRECTIONS_LONG | VARCHAR (1000) | Contains the directions for taking a medication order. |
| USER_CHANGED_END_TIME_YN | VARCHAR (1) |  |
| ORIG_MED_DIRECTIONS_LONG | VARCHAR (1000) | Contains the original directions for taking a medication order. |
| DISCON_LOGIN_DEPARTMENT_ID | NUMERIC (18,0) | Stores the login department of the user who discontinued the order |
| NO_REIMBURS_CODESET | VARCHAR (30) | Holds the code set of the selected reimbursement code. |
| STANDING_COUNT | INTEGER | This item stores a numeric value for the count of the order that goes along with the standing count type, indicating the number of hours, days, weeks, or occurrences for which the order will take place. |
| STANDING_COUNT_TP_C | INTEGER |  |
| COUNT_RANGE | VARCHAR (20) | This item stores a ranged value for the count of the order that goes along with the standing count type, indicating the number of hours, days, weeks, or occurrences for which the order will take place. Currently only available in Finland. |
| COUNT_RANGE_STND_TP_C | INTEGER |  |
| ORIGINAL_SESSIONKEY | VARCHAR (20) | The original session in which this order was created.  (In a few cases, this may be earlier than the ORD-455 sessionkey if you pend an order set, then add an order to it after unpending.)  Used by discontinue logic for locating all related orders, even if they are not all signed at the same time. |
| ORIG_ORD_PROV_ID | VARCHAR (18) | This will hold the SER ID of the ordering provider at the time the order was signed or sign & held. |
| ORDER_START_TM | DATETIME (Local) | The time when the medication order is to start. |
| PROTOCOLLED_ORDER_ID | NUMERIC (18,0) | For an order that was placed from an imaging protocol, this item contains the protocolled imaging procedure order from which the order was placed. |
| PRIMARY_LANG_SIG_ID | NUMERIC (18,0) | This item contains the SIG record used to compose the primary language sig (I ORD 7055) when it was composed using multilingual sig composition. |
| TRANSLATED_SIG_ID | NUMERIC (18,0) | This item contains the SIG record used to compose the translated sig (I ORD 7054) when it was composed using multilingual sig composition. |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ORDER_MED_ID | ADT_ORDERS_ERRORS | ORDER_ID | No | No | No |  |
| 1 | ORDER_MED_ID | ADT_ORDER_INFORMATION | ORDER_ID | No | No | No |  |
| 1 | ORDER_MED_ID | APPT_REQUEST | REQUEST_ID | No | No | No |  |
| 1 | ORDER_MED_ID | CL_ORD_FST_LST_SCH | ORDER_ID | No | No | No |  |
| 1 | ORDER_MED_ID | DENT_ORD_NOADD | ORDER_ID | No | No | No |  |
| 1 | ORDER_MED_ID | DUPMED_DISMISS_HH_INFO | ORDER_ID | No | No | No |  |
| 1 | ORDER_MED_ID | ENDOSCOPY_METRICS | ORDER_ID | Unknown | No | No |  |
| 1 | ORDER_MED_ID | EXTERNAL_ORDER_INFO | ORDER_ID | No | No | No |  |
| 1 | ORDER_MED_ID | F_IMG_STUDY | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_MED_ID | F_IP_HSP_SUM_ORDER | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_MED_ID | F_LAB_ORDERS | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_MED_ID | F_MU_OBJ_EH_PLACED_ORDER | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_MED_ID | F_MU_OBJ_EH_RESULTD_ORDER | ORDER_PROC_ID | Unknown | Unknown | No |  |
| 1 | ORDER_MED_ID | F_ONC_PRIOR_AUTH_ORDERS | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_MED_ID | F_OPIOID_ORDERS | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_MED_ID | F_RX_ORDER | ORDER_MED_ID | Unknown | Unknown | No |  |
| 1 | ORDER_MED_ID | HH_MED_ORD_IN_POC_DETAIL | ORDER_MED_ID | No | No | No |  |
| 1 | ORDER_MED_ID | HV_ORDER_PROC | ORDER_PROC_ID | Unknown | No | No |  |
| 1 | ORDER_MED_ID | MED_DETAILS_EXT_ORD | ORDER_ID | No | No | No |  |
| 1 | ORDER_MED_ID | MERCHANDISE_ORDER_INFO | ORDER_ID | Yes | No | No |  |
| 1 | ORDER_MED_ID | MU_EH_QRDA_I_ORDER | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_MED_ID | ORDERS | ORDER_ID | No | No | No |  |
| 1 | ORDER_MED_ID | ORDER_AUTH_INFO | ORDER_ID | No | No | No |  |
| 1 | ORDER_MED_ID | ORDER_MED | ORDER_MED_ID | Unknown | No | No |  |
| 1 | ORDER_MED_ID | ORDER_MEDINFO | ORDER_MED_ID | Unknown | No | No |  |
| 1 | ORDER_MED_ID | ORDER_MED_2 | ORDER_ID | Unknown | No | No |  |
| 1 | ORDER_MED_ID | ORDER_MED_3 | ORDER_ID | Unknown | No | No |  |
| 1 | ORDER_MED_ID | ORDER_MED_4 | ORDER_ID | Unknown | No | No |  |
| 1 | ORDER_MED_ID | ORDER_MED_5 | ORDER_ID | Unknown | No | No |  |
| 1 | ORDER_MED_ID | ORDER_MED_7 | ORDER_ID | No | No | No |  |

_(238 total; showing first 30)_
