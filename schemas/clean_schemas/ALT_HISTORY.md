# ALT_HISTORY

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=ALT_HISTORY

## Description

This table contains general history information for each type of medication warning or advisory. Since each warning could be triggered in different activities at different times, it contains general warning information for each time the warning was triggered. To get patient information, link this table to the ALERT table and then link the ALERT table to the PATIENT or PAT_ENC table. To get order related information for each medication warning or advisory, link this table to ALT_ORDINFO. To get specific medication or condition information for each medication warning type, link this table to specific medication warning related tables, such as the ALT_DRUG_ALLERGY table for drug-allergy warnings; the ALT_DRUG_DFALC table for drug-drug, drug-food, and drug-alcohol warnings; the ALT_DRUG_DUPTHERPY and ALT_DRUG_DUPTHYMED tables for duplicate therapy warnings; the ALT_DRUG_IV and ALT_DRUG_IVMED tables for IV warnings; and the ALT_DRUG_PREGNANCY and ALT_DRUG_PREGMED tables for pregnancy warnings.

**Primary table** in this group (101 cols). Overflow siblings joined on shared key: ALT_HISTORY_2 (98 cols), ALT_HISTORY_3 (13 cols). Prefer this table for most queries.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | ALT |
| Release Version | SUMMER 2005 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| ALT_ID | NUMERIC (18,0) | The unique warning ID for each warning. You could link it to ALERT.ALT_ID to get patient and vendor information in table ALERT. |
| ALT_DATE_REAL | No | This is a numeric representation of the date of the contact. The integer portion of the number specifies the date of the encounter. The digits after the decimal point indicate multiple times on one day. |
| ALT_CSN_ID | NUMERIC (18,0) | A unique serial number for this contact. This number is unique across all warnings in the system. |
| CONTACT_DATE | DATETIME | The date of this contact in calendar format. |
| CM_CT_OWNER_ID | VARCHAR (25) | ID of the deployment owner for this contact. |
| USER_INTSET_CSN | NUMERIC (18,0) | A unique serial number for the user level interaction setting contact used during interaction checking.  Interaction Setting could be set up at user, profile, and system levels.  If user level is released, we will use it here during interaction checking. |
| SYS_INTSET_CSN | NUMERIC (18,0) | A unique serial number for the profile or system level interaction setting contact used during interaction checking.  Interaction Setting could be set up at user, profile, and system levels.  No matter if user level is released, we always use whole or part of information from profile or system level during interaction checking. |
| ALT_STATUS_C | INTEGER |  |
| USER_ID | VARCHAR (18) | The unique ID of the user who triggered the warning. This column is frequently used to link to the CLARITY_EMP table. |
| ALT_ACTION_INST | DATETIME (Attached) | The instant when the warning is gone after some actions.  For medication interactions, it is the instant after you click Override & Accept or Cancel button on the warning pop-up form. |
| ALT_GROUP_INFO | VARCHAR (255) | The unique value to group all warnings in the same group. For medication interactions, it will be the same for all warnings on the same warning pop-up form. You could use this column to find out all medication interactions shown at the same time. |
| SHOWN_PLACE_C | INTEGER |  |
| OVERALL_OVR_RSN_C | INTEGER |  |
| OVERALL_OVR_CMNT | VARCHAR (508) | For medication interactions, when you override & accept the warning pop-up form, if an overall override comment is given at the bottom of the form, it will be saved here. We only extract the first 255 characters. |
| SPEC_OVR_RSN_C | INTEGER |  |
| SPEC_OVR_CMNT | VARCHAR (1000) | For medication interactions, when you override & accept the warning pop-up form, if a specific override comment is given on the right of the form, it will be saved here. We only extract the first 1000 characters. |
| IMMUNIZATION_LPL_ID | NUMERIC (18,0) | The patient?s immunization problem list ID for a specific immunization-allergy interaction. |
| BPA_FUP_ASYNC_FRQ_C *(deprecated)* | INTEGER |  |
| BPA_FUP_IB_FREQ_C *(deprecated)* | INTEGER |  |
| IMPORTANCE_LVL_C | VARCHAR (66) |  |
| PROVIDER_TYPE_C | VARCHAR (66) |  |
| WAS_SHOWN_C | INTEGER |  |
| SPECIFIC_DEFR_RSN_C | INTEGER |  |
| SCANNED_BARCODE | VARCHAR (100) | The barcode that was scanned to cause the warning |
| NDC_CSN_ID | VARCHAR (254) | CSN for the NDC in the scanned barcode |
| BARCODE_ERX_ID | NUMERIC (18,0) | If a med NDC barcode is scanned, this is the ERX ID that the NDC maps to. |
| BARCODE_ORD_ID | NUMERIC (18,0) | When an ORD ID barcode is scanned, this is the order ID. |
| PAT_CSN_ID *(deprecated)* | NUMERIC (18,0) |  |
| ALERT_TYPE_OVTIME_C *(deprecated)* | INTEGER |  |
| SIGN_OFF_EMP_ID | VARCHAR (18) | The unique ID of the user who signed off on the warning. This is used in an EpicEurope workflow where pharmacists need to sign off on warnings that were reviewed by a pharmacy technician. |
| SIGN_OFF_DATETIME | DATETIME (UTC) | The date and time when the user signed off on the warning. This is used in an EpicEurope workflow where pharmacists need to sign off on warnings that were reviewed by a pharmacy technician. |
| SIGN_OFF_COMMENT | VARCHAR (510) | The optional comments entered by the user who signed off on the warning. This is used in an EpicEurope workflow where pharmacists need to sign off on warnings that were reviewed by a pharmacy technician. |
| DOSING_WEIGHT | NUMERIC (12,3) | Weight used for dose checking. Always stored in kilograms. |
| WT_RECORD_DATETIME | DATETIME (Local) | The instant at which the weight was recorded. |
| WT_SOURCE_C | INTEGER |  |
| WT_COMMENTS | VARCHAR (500) | Generated comment for weight. |
| DOSING_HEIGHT | NUMERIC (12,3) | Height used for dosing warning. Always stored in inches. |
| HT_RECORD_DATETIME | DATETIME (Local) | The instant at which the height was recorded. |
| HT_SOURCE_C | INTEGER |  |
| DOSING_BSA | NUMERIC (12,3) | The body surface area used for dosing checking. Always stored in m2. |
| BSA_SOURCE_C | INTEGER |  |
| BSA_CALC_DETAIL | VARCHAR (508) | The body surface area calculation details with weight, height and recorded instants. |
| GERI_ALRT_SEV_LVL_C | INTEGER |  |
| PEDI_ALRT_SEV_LVL_C | INTEGER |  |
| PRC_MANAGE_LEVEL_C | INTEGER |  |
| ALERT_ALLERGEN_ID | NUMERIC (18,0) | The allergen ID of drug-allergy warning. |
| ALLERGY_LEVEL_C | INTEGER |  |
| INACT_INGRED_IND_YN | VARCHAR (1) |  |
| INACT_REVIEW_YN | VARCHAR (1) |  |
| ALERT_ROOT_ALLER_ID | NUMERIC (18,0) | This column stores the allergen ID of the allergen that caused the warning to fire. |
| ALERT_MED_CLASS_ID | NUMERIC (18,0) | Contains the allergen class of the medication for a cross-sensitive warning. |
| PATIENT_DEP_ID | NUMERIC (18,0) | This column stores the patient's department at the time when the warning was fired. |
| ALERT_ALLERGY_ID | NUMERIC (18,0) | The problem list record that contains the allergen for a drug-allergy warning. |
| INT_DTMS_FDDB_ID | NUMERIC (18,0) | The interaction record ID for drug-drug/food/alcohol if the vendor is Medispan or NDDF Plus. |
| DRUG_INT_BASIC_ID | NUMERIC (18,0) | The interaction ID for drug-drug/food/alcohol if vendor is Basic.  This column is no longer in use as Basic is no longer supported as a vendor. |
| DRUG_INT_SVRTY_C | INTEGER |  |
| DRUG_INT_FDDB_SVR_C | INTEGER |  |
| DRUG_INT_BASICLVL_C | INTEGER |  |
| DRUG_INT_NDDF_SVR_C | VARCHAR (66) |  |
| DRUG_INT_GS_SVR_C | INTEGER |  |
| DUP_ALERT_CLS_C | INTEGER |  |
| DUP_ALERT_ALLOW | INTEGER | The duplicate allowance for duplicate therapy warning. |
| DUP_ALERT_SIGN_C | INTEGER |  |
| IVCHEK_CSN | NUMERIC (18,0) | The corresponding Contact Serial Number for IVC. |
| IVCHEK_CSRATING_C | INTEGER |  |
| IVCHEK_SOLUTION_NUM | INTEGER | The corresponding solution line of IVC record for Medispan IV warning. |
| IV_TEST_RESULT_C | INTEGER |  |
| PREG_ALRT_SIG_LVL_C | INTEGER |  |
| LACT_ALRT_SEV_LVL_C | INTEGER |  |
| DRUG_DIS_SEV_NDDF_C | INTEGER |  |
| PA_PTCODE_C | INTEGER |  |
| PA_FDA_C | INTEGER |  |
| PA_BRIGGS_C | INTEGER |  |
| LA_CODE_C | INTEGER |  |
| LA_RATING_C | INTEGER |  |
| LA_AAP_C | INTEGER |  |
| TPN_COMPONENT_VAL | NUMERIC (18,2) | Value for a TPN component or compatibility calculation. |
| TPN_COMP_UNIT_C | INTEGER |  |
| TPN_RANGE_MIN | NUMERIC (18,2) | The minimum in the acceptable range for a component in a TPN warning. |
| TPN_RANGE_MAX | NUMERIC (18,2) | The maximum in the acceptable range for a component in a TPN warning. |
| TPN_COMPONENT_C | INTEGER |  |
| DRUG_INT_GS_WFG_YN | VARCHAR (1) |  |
| DRUG_INT_GS_PRES_YN | VARCHAR (1) |  |
| DRUG_INT_GS_RXTX_YN | VARCHAR (1) |  |
| DRUG_INT_GS_RX_YN | VARCHAR (1) |  |
| DM_ALERT_SIGN_C | INTEGER |  |
| BPA_TRGR_ACTION_C | INTEGER |  |
| CONTACT_NUM | INTEGER | The number of the ALT contacts for the given ALT record. |
| IS_NONFILTERED_YN | VARCHAR (1) |  |
| ALLERGY_REPLACE_ID | NUMERIC (18,0) | It stores the replacement allergen ID as of when the drug-allergy warning is fired. |
| DRUG_ALLERGY_GRP_C | INTEGER |  |
| OVERRIDDEN_INT_ID | NUMERIC (18,0) | It stores customer record ID that overrides drug-drug, drug-food, or drug-alcohol (Medi-Span). |
| INT_MANAGE_CODE_C | INTEGER |  |
| BPA_ACK_SDE_ID *(deprecated)* | NUMERIC (18,0) |  |
| BPA_ACK_SDE_CTXT_ID *(deprecated)* | NUMERIC (18,0) |  |
| BPA_ACK_SDE_VALUE *(deprecated)* | VARCHAR (254) |  |
| DEFAULT_GEST_AGE | INTEGER | Save the default gestational age in weeks if default gestational age is used for dose checking. |
| ORDER_CONTEXT_C | INTEGER |  |
| BPA_ACK_APP_OPT_C | INTEGER |  |
| BPA_ACK_LOCKOUT_TM | INTEGER | NOTE: Use column BPA_ACK_LOCKOUT_TM_FLOAT in ALT_HISTORY_2 instead for higher precision. That column is a floating point type, so it can also represent minutes instead of only hours.  The lockout time associated with the acknowledge reason chosen in the advisory. |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| B-TREE INDEX | EIX_ALT_HISTORY_ALTID | ALT_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_ALT_HISTORY_EMPID | USER_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_ALT_HIST_ALT_ACTION_INST | ALT_ACTION_INST | 1 | Yes | Yes |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ALT_ID | ALERT | ALT_ID | No | No | No |  |
| 3 | ALT_CSN_ID | ALT_DRUG_AGE | ALT_CSN_ID | Unknown | Unknown | No |  |
| 3 | ALT_CSN_ID | ALT_DRUG_ALLERGY | ALT_CSN_ID | Unknown | Unknown | No |  |
| 3 | ALT_CSN_ID | ALT_DRUG_DFALC | ALT_CSN_ID | Unknown | Unknown | No |  |
| 3 | ALT_CSN_ID | ALT_DRUG_DISEASE | ALT_CSN_ID | Unknown | Unknown | No |  |
| 3 | ALT_CSN_ID | ALT_DRUG_DUPTHERPY | ALT_CSN_ID | Unknown | Unknown | No |  |
| 3 | ALT_CSN_ID | ALT_DRUG_IV | ALT_CSN_ID | Unknown | Unknown | No |  |
| 3 | ALT_CSN_ID | ALT_DRUG_LACTATION | ALT_CSN_ID | Unknown | Unknown | No |  |
| 3 | ALT_CSN_ID | ALT_DRUG_PREGNANCY | ALT_CSN_ID | Unknown | Unknown | No |  |
| 3 | ALT_CSN_ID | ALT_DRUG_TPN | ALT_CSN_ID | Unknown | Unknown | No |  |
| 3 | ALT_CSN_ID | ALT_HISTORY_2 | ALT_CSN_ID | No | No | No |  |
| 3 | ALT_CSN_ID | ALT_HISTORY_3 | ALT_CSN_ID | No | No | No |  |
| 3 | ALT_CSN_ID | F_IP_HSP_ALERT | ALERT_CSN_ID | Unknown | Unknown | No |  |
| 3 | ALT_CSN_ID | F_RX_OE_DRUG_WARNINGS | ALT_CSN_ID | Unknown | Unknown | No |  |
| 3 | ALT_CSN_ID | V_CUBE_F_ALERT | ALERT_CSN_ID | Unknown | Unknown | No |  |
| 3 | ALT_CSN_ID | V_DRUG_WARNINGS | ALT_CSN_ID | Unknown | Unknown | No |  |
| 5 | CM_CT_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | Yes | No |  |
| 5 | CM_CT_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | Yes | No |  |
| 5 | CM_CT_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | Yes | No |  |
| 6 | USER_INTSET_CSN | RX_INTSET_OT | CONTACT_SERIAL_NUM | No | Yes | No |  |
| 7 | SYS_INTSET_CSN | RX_INTSET_OT | CONTACT_SERIAL_NUM | No | Yes | No |  |
| 8 | ALT_STATUS_C | ZC_ALT_STATUS | ALT_STATUS_C | No | Yes | No |  |
| 9 | USER_ID | CLARITY_EMP | USER_ID | Unknown | Yes | No |  |
| 9 | USER_ID | CLARITY_EMP_2 | USER_ID | Unknown | Yes | No |  |
| 9 | USER_ID | CLARITY_EMP_3 | USER_ID | Unknown | Yes | No |  |
| 9 | USER_ID | CLARITY_EMP_4 | USER_ID | No | Yes | No |  |
| 9 | USER_ID | CLARITY_EMP_DEMO | USER_ID | No | Yes | No |  |
| 9 | USER_ID | EMP_BASIC_INFO | USER_ID | No | Yes | No |  |
| 9 | USER_ID | EMP_DOC_SETTINGS | USER_NUMBER_ID | No | Yes | No |  |
| 9 | USER_ID | F_RX_USER | USER_ID | Unknown | Unknown | No |  |

_(227 total; showing first 30)_
