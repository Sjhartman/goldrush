# ORDER_MED_5

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=ORDER_MED_5

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
| Release Version | Rel 2018 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| ORDER_ID | NUMERIC (18,0) | The unique identifier for the order record. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| FREE_TXT_SUP_PROV_NAME | VARCHAR (192) | This is the name of the supervising provider. |
| FREE_TXT_SUP_PROV_IS_EXT_YN | VARCHAR (1) |  |
| FREE_TXT_SUP_PROV_DEA | VARCHAR (192) | This is the Drug Enforcement Administration (DEA) number of the supervising provider. |
| FREE_TXT_SUP_PROV_NPI | VARCHAR (192) | This is the National Provider Identifier (NPI) of the supervising provider. |
| FREE_TXT_SUP_PROV_PHONE | VARCHAR (254) | This is the phone number of the supervising provider. |
| FREE_TXT_SUP_PROV_FAX | VARCHAR (254) | This is the fax number of the supervising provider. |
| FREE_TXT_SUP_PROV_STREET | VARCHAR (254) | This is the street address of the supervising provider. |
| FREE_TXT_SUP_PROV_CITY | VARCHAR (254) | This is the city of the supervising provider. |
| FREE_TXT_SUP_PROV_STATE_C | VARCHAR (66) |  |
| FREE_TXT_SUP_PROV_ZIP | VARCHAR (254) | This is the zip code of the supervising provider. |
| FREE_TXT_SUP_PROV_HOUSE | VARCHAR (254) | This is the house number of the supervising provider for medication instructions. |
| FREE_TXT_SUP_PROV_DISTRICT_C | INTEGER |  |
| FREE_TXT_SUP_PROV_COUNTY_C | VARCHAR (66) |  |
| FREE_TXT_SUP_PROV_COUNTRY_C | VARCHAR (66) |  |
| MLSIG_SIGTYPE_C | INTEGER |  |
| HOME_HEALTH_DUE_COMMENT | VARCHAR (300) | The comments entered about the home health medication due time or the person responsible for home health medication administration. |
| HH_RESP_PERS_C | INTEGER |  |
| BASE_MED_ORDER_ID | NUMERIC (18,0) | The unique identifier for the order record representing a multi-product prescription group, containing this order record and others which represent individual product prescriptions within the group. |
| MULTI_PROD_IMS_YN | VARCHAR (1) |  |
| PA_DISP_OVERRIDE_YN | VARCHAR (1) |  |
| DDD_ATC_CODE_C | INTEGER |  |
| DDD_WHO_ROUTE_C | INTEGER |  |
| DISALLOW_RENEWAL_REASON_C | INTEGER |  |
| RX_VALID_UNTIL_X_DATE | DATETIME | The date until which the prescription is valid. |
| COMMUNICABLE_YN | VARCHAR (1) |  |
| SIC_YN | VARCHAR (1) |  |
| CONCERNS_INITIATION_YN | VARCHAR (1) |  |
| DISALLOW_RENEWAL_REASON_TEXT | VARCHAR (100) | Free text explanation for disallowing the renewal. |
| PREVENT_RENEWAL_YN | VARCHAR (1) |  |
| TREATMENT_TYPE_YN | VARCHAR (1) |  |
| SELECTED_CRCL_SEX_C | VARCHAR (66) |  |
| RX_TYPE_C | INTEGER |  |
| MED_PROVENANCE | VARCHAR (3500) | This item stores provenance information about medications from external health record systems. |
| MEDD *(deprecated)* | NUMERIC (18,3) |  |
| PAIN_AGREEMENT_YN | VARCHAR (1) |  |
| SEPARATE_ACCT_RSN | VARCHAR (80) | Physician's grounds for medication requiring a separate account for health insurance reimbursement. |
| PRN_MIN_INTRVL | INTEGER | Stores the mimimum amount of time that should pass between subsequent administrations of a PRN medication. |
| PRN_MIN_INTRVL_UN_C | INTEGER |  |
| EXT_KANTA_PERM_YN | VARCHAR (1) |  |
| KANTA_BKGRND_CREATED_YN | VARCHAR (1) |  |
| DISCON_CHART_CORR_YN | VARCHAR (1) |  |
| IS_PAUSED_FMK_YN | VARCHAR (3) |  |
| WAS_PAUSED_FMK_YN | VARCHAR (3) |  |
| PAUSE_ON_SIGNING_YN | VARCHAR (3) |  |
| HOME_HEALTH_GIVE_PRN_YN | VARCHAR (1) |  |
| PIN_STATUS_C | INTEGER |  |
| PCA_MORPHINE_EQUIV_CONV_FACTOR *(deprecated)* | NUMERIC (18,3) |  |
| PCA_TOTAL_DOSE_FLO_ID *(deprecated)* | VARCHAR (18) |  |
| NO_RENEW_REASON_C | INTEGER |  |
| ORIG_RX_ORDER_CLASS_C | VARCHAR (66) |  |
| ORDER_INST_UTC_DTTM | DATETIME (UTC) | The date and time the order was placed in UTC. This is the same as the data in ORDER_MED.ORDER_INST, but in UTC. |
| TOTAL_MME_PER_FILL *(deprecated)* | NUMERIC (18,2) |  |
| HH_NOT_DAILY_YN | VARCHAR (1) |  |
| REIMBURSEMNT_CODE_C | INTEGER |  |
| RX_TEST_BILL_DTTM | DATETIME (UTC) | The instant the test billing order was created. |
| CONFIDENTIALITY_FLAG_C | INTEGER |  |
| ORDERED_DAYS_SUPPLY_PER_FILL | INTEGER | The calculated minimum days supply of the medication ordered. The value for this item is calculated when the order is signed, or when the order is edited by the pharmacy. |
| FMK_PARENT_ORDER_MED_ID | NUMERIC (18,0) | The order ID of the original FMK medication order from which this order was reordered. |
| FMK_PARENT_REL_C | INTEGER |  |
| AUTH_PROV_NADEAN | VARCHAR (30) | Authorizing provider's Narcotic Addiction DEA Number |
| PAUSE_START_DTTM | DATETIME (Local) | The start instant for the pause period of a medication order. |
| PAUSE_END_DTTM | DATETIME (Local) | The end instant for the pause period of a medication order. |
| VISI_FLAG_YN | VARCHAR (1) |  |
| PREVIOUS_INR_DATE | DATETIME | The date of the patient's last INR assessment. |
| NEXT_INR_DATE | DATETIME | The next date on which a patient's international normalized ratio (INR) should be assessed. |
| INTERFACE_ORDER_YN | No | Indicates whether order is an interface order. Interface orders are created from an interface or have an interface order source. |
| USER_SEL_ORDER_TEMPLATE_OTL_ID | VARCHAR (50) | The unique ID of the order template record which a user selected to create the order record for this row. |
| DISP_RECPNT_NAME | VARCHAR (254) | This item holds the recipient name for the dispatch request. |
| DISP_RECPNT_CITY | VARCHAR (50) | This item holds the city for this dispatch request. |
| DISP_RECPNT_STATE_C | VARCHAR (66) |  |
| DISP_RECPNT_ZIP | VARCHAR (20) | This item holds the zip code for this dispatch request. |
| DISP_RECPNT_COUNTRY_2_C | VARCHAR (66) |  |
| DISP_RECPNT_HOUSE | VARCHAR (254) | This item holds the house number for this dispatch request. |
| DISP_RECPNT_COUNTY_2_C | VARCHAR (66) |  |
| DISP_RECPNT_DISTRICT_C | INTEGER |  |
| HH_IN_BAG_YN | VARCHAR (1) |  |
| HH_IN_PILL_BOX_YN | VARCHAR (1) |  |
| HH_BAG_START_DATE | DATETIME | The start date of a home health medication prepacked in a bag. |
| HH_BAG_END_DATE | DATETIME | The end date of a home health medication prepacked in a bag. |
| HH_PILL_START_DATE | DATETIME | The start date of a home health medication dispensed in a pill box. |
| HH_PILL_END_DATE | DATETIME | The end date of a home health medication dispensed in a pill box. |
| SLV_APPLICATION_STATUS_C | INTEGER |  |
| SLV_STATUS_UPDATE_UTC_DTTM | DATETIME (UTC) | This item holds the instant that the SLV application status was updated. |
| BRAND_SEL_RSN_C | INTEGER |  |
| DISCON_LOCALLY_C | INTEGER |  |
| DISCON_PAT_ENC_DATE_REAL | NUMERIC (18,2) | The encounter or visit in which the medication was discontinued. |
| UNIQUE_ORDER_IDENTIFIER | VARCHAR (192) | Order identifier that is unique for all deployments |
| REC_W_MAP_ERX_YN | VARCHAR (1) |  |
| HH_OVERRIDE_DOSE_YN | VARCHAR (1) |  |
| HH_IN_BAG_REVIEWED_YN | VARCHAR (1) |  |
| HH_DUE_TIMES_REVIEWED_YN | VARCHAR (1) |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ORDER_ID | ADT_ORDERS_ERRORS | ORDER_ID | No | No | No |  |
| 1 | ORDER_ID | ADT_ORDER_INFORMATION | ORDER_ID | No | No | No |  |
| 1 | ORDER_ID | APPT_REQUEST | REQUEST_ID | No | No | No |  |
| 1 | ORDER_ID | CL_ORD_FST_LST_SCH | ORDER_ID | No | No | No |  |
| 1 | ORDER_ID | DENT_ORD_NOADD | ORDER_ID | No | No | No |  |
| 1 | ORDER_ID | DUPMED_DISMISS_HH_INFO | ORDER_ID | No | No | No |  |
| 1 | ORDER_ID | ENDOSCOPY_METRICS | ORDER_ID | Unknown | No | No |  |
| 1 | ORDER_ID | EXTERNAL_ORDER_INFO | ORDER_ID | No | No | No |  |
| 1 | ORDER_ID | F_IMG_STUDY | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_ID | F_IP_HSP_SUM_ORDER | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_ID | F_LAB_ORDERS | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_ID | F_MU_OBJ_EH_PLACED_ORDER | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_ID | F_MU_OBJ_EH_RESULTD_ORDER | ORDER_PROC_ID | Unknown | Unknown | No |  |
| 1 | ORDER_ID | F_ONC_PRIOR_AUTH_ORDERS | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_ID | F_OPIOID_ORDERS | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_ID | F_RX_ORDER | ORDER_MED_ID | Unknown | Unknown | No |  |
| 1 | ORDER_ID | HH_MED_ORD_IN_POC_DETAIL | ORDER_MED_ID | No | No | No |  |
| 1 | ORDER_ID | HV_ORDER_PROC | ORDER_PROC_ID | Unknown | No | No |  |
| 1 | ORDER_ID | MED_DETAILS_EXT_ORD | ORDER_ID | No | No | No |  |
| 1 | ORDER_ID | MERCHANDISE_ORDER_INFO | ORDER_ID | Yes | No | No |  |
| 1 | ORDER_ID | MU_EH_QRDA_I_ORDER | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_ID | ORDERS | ORDER_ID | No | No | No |  |
| 1 | ORDER_ID | ORDER_AUTH_INFO | ORDER_ID | No | No | No |  |
| 1 | ORDER_ID | ORDER_MED | ORDER_MED_ID | Unknown | No | No |  |
| 1 | ORDER_ID | ORDER_MEDINFO | ORDER_MED_ID | Unknown | No | No |  |
| 1 | ORDER_ID | ORDER_MED_2 | ORDER_ID | Unknown | No | No |  |
| 1 | ORDER_ID | ORDER_MED_3 | ORDER_ID | Unknown | No | No |  |
| 1 | ORDER_ID | ORDER_MED_4 | ORDER_ID | Unknown | No | No |  |
| 1 | ORDER_ID | ORDER_MED_6 | ORDER_MED_ID | Unknown | No | No |  |
| 1 | ORDER_ID | ORDER_MED_7 | ORDER_ID | No | No | No |  |

_(279 total; showing first 30)_
