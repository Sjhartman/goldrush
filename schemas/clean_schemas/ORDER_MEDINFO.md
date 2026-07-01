# ORDER_MEDINFO

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=ORDER_MEDINFO

## Description

The ORDER_MEDINFO table is an addendum table for ORDER_MED and enables you to report on detail medication information for each order in clinical system (prescriptions). We have also included patient and contact identification information for each record.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | ORD |
| Release Version | FALL 2004 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| ORDER_MED_ID | NUMERIC (18,0) | The unique ID of the medication order (prescription) record. |
| MED_LINKED_PROC_ID | NUMERIC (18,0) | The linked procedure ID for the medication.  Depending on pharmacy billing configuration, you may have only one procedure ID (code) for all medications or many. |
| MED_CNCT_DAT_REAL | No | The real medication contact date (DAT) used in this order. |
| LAST_ADMIN_INST | DATETIME (Local) | The last instant that the medication order is administrated in the Medication Administration Record (MAR). |
| NUMBER_OF_DOSES | INTEGER | The total number of doses of the medication order that should be given to the patient. |
| DOSES_REMAINING | INTEGER | The total number of the medication order which has not been given to patient. |
| RESUME_STATUS_C | INTEGER |  |
| MIXTURE_TYPE_NAME *(deprecated)* | VARCHAR (254) |  |
| MODIFIED_RX_MIX_YN | VARCHAR (254) |  |
| INFUSION_TYPE_C *(deprecated)* | INTEGER |  |
| MIN_RATE | NUMERIC (19,4) | The minimum rate number. |
| MAX_RATE | NUMERIC (19,4) | The maximum rate number. |
| RATE_UNIT_C | INTEGER |  |
| MIN_DURATION | NUMERIC (19,4) | The minimum duration. |
| MAX_DURATION | NUMERIC (19,4) | The maximum duration. |
| DURATION_UNIT_NAME *(deprecated)* | VARCHAR (254) |  |
| TPN_SITE_NAME *(deprecated)* | VARCHAR (254) |  |
| MIN_VOLUME | NUMERIC (19,4) | The minimum volume. |
| MAX_VOLUME | NUMERIC (19,4) | The maximum volume. |
| VOLUME_UNIT_C | INTEGER |  |
| CALC_VOLUME_YN | VARCHAR (254) |  |
| STABILITY | NUMERIC (12,2) | The stability value. |
| STABILITY_UNIT_NAM *(deprecated)* | VARCHAR (254) |  |
| MEDICATION_ID | NUMERIC (18,0) | The ID of the medication prescribed for the patient. |
| PAT_SUPP_MED_YN | VARCHAR (254) |  |
| PAT_SUPP_DOSES | INTEGER | Specifies the number of doses the patient supplies if the medication is patient supplied. |
| CALC_MIN_DOSE | NUMERIC (19,4) | The minimum calculated administer dose. |
| CALC_MAX_DOSE | NUMERIC (19,4) | The maximum calculated administer dose. |
| CALC_DOSE_UNIT_C | INTEGER |  |
| CALC_DOSE_INFO | VARCHAR (1000) | The calculation steps to get calculated administer dose from the ordered dose. |
| ADMIN_MIN_DOSE | NUMERIC (19,4) | The minimum administer dose. |
| ADMIN_MAX_DOSE | NUMERIC (19,4) | The maximum administer dose. |
| ADMIN_DOSE_UNIT_C | INTEGER |  |
| DONOT_DISP_YN | VARCHAR (254) |  |
| DONOT_DISP_DOSE | INTEGER | It is to specify the number of doses which will not be dispensed if the DONOT_DISP_YN column is 'Y' for Yes. |
| PAT_ID | VARCHAR (18) | The unique ID assigned to the patient record. This ID may be encrypted if you have elected to use enterprise reporting?s encryption utility. |
| PAT_ENC_DATE_REAL | FLOAT | This is a numeric representation of the date of this encounter in your system. The integer portion of the number specifies the date of the encounter. The digits after the decimal point indicate multiple visits on one day. |
| PAT_ENC_CSN_ID | 226 | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| CM_PHY_OWNER_ID | VARCHAR (25) | ID of the physical deployment owner for this record.  Physical owners will be where the data is hosted, either on the cross-over server or the owner deployment. |
| CM_LOG_OWNER_ID | VARCHAR (25) | ID of the logical deployment owner for this record.  Logical owners show the deployment where the record was created but doesn't represent if the record is a part of version skew. |
| ORDERING_DATE | DATETIME | The date the order was placed  in calendar format. |
| ORDER_CLASS_C | VARCHAR (66) |  |
| CONC_NAME_C | INTEGER |  |
| LET_EXPIRE_USER_ID | VARCHAR (18) | The ID of the user who marked order as Let Expire. |
| TIME_LET_EXPIRE | DATETIME (Local) | The time when the physician marked the order as Let Expire. |
| EXP_AFT_START_TIME | DATETIME (Local) | The date and time the order will expire, based on the amount of time a physician entered for the order to expire after the start time. |
| EXP_BEF_END_TIME | DATETIME (Local) | The date and time the order will expire, based on the amount of time a physician entered for the order to expire before the end time. |
| ORD_COPIED_C | INTEGER |  |
| ORDER_SOURCE_C | INTEGER |  |
| DFLT_DISCRETE_FREQ | INTEGER |  |
| DFLT_DISCRETE_DOSE | INTEGER |  |
| REV_ORD_GRANU_YN | VARCHAR (1) |  |
| EXP_DAYS_YN | VARCHAR (1) |  |
| MED_CONTACT_DT | DATETIME | This is the order contact date in human readable form. |
| DOSE_CALC_WARNING | VARCHAR (1000) | Contains the dose warning generated when the order was entered or verified. |
| MIXTURE_TYPE_C | INTEGER |  |
| MED_DURATION_UNIT_C | INTEGER |  |
| TPN_SITE_C | INTEGER |  |
| STABILITY_UNIT_C | INTEGER |  |
| DISP_INDIV_YN | VARCHAR (1) |  |
| MR_IS_PERSISTENT_YN | VARCHAR (1) |  |
| MAR_ADMIN_TYPE_C | INTEGER |  |
| ORD_COMP_YN | VARCHAR (1) |  |
| ADMIN_ORD_STAT_C *(deprecated)* | INTEGER |  |
| MEDS_SUSPEND_RSN_C *(deprecated)* | INTEGER |  |
| RATE_CALC_INFO | VARCHAR (2000) | Stores the rate calculation info. |
| RATE_CALC_WARNING | VARCHAR (500) | Contains the rate warning generated when the order was entered or verified. |
| DFLT_DISCRETE_C | INTEGER |  |
| PT_SIG_SMARTTEXT_ID | VARCHAR (18) | The unique identifier of the SmartText record used to generate medication instructions for the patient based on order details. A SmartText record is a text template that can contain text and dynamic data. |
| DISPENSABLE_MED_ID | NUMERIC (18,0) | This is the unique ID of the medication that is the order's dispensable product. This column is frequently used to link to the CLARITY_MEDICATION table.  We recommend using this column in place of other similar columns to report on medication orders. Other columns that contain a medication ID in ORDER_MED and its addendum tables can contain orderable records or templates that do not represent real medications.  When Intelligent Medication Selection (IMS) runs for an order, this column will choose the medication record evaluated for IMS rather than the IMS mixture template. |
| TIMELY_THRESHOLD | INTEGER | Number of minutes between the scheduled time for an administration and the actual time given before the administration is considered Late/Early. This is a calculated value specific to each order, derived from settings in the ordered medication, ordered frequency, and System Definitions. |
| RX_MANUAL_OVERFILL | NUMERIC (18,2) | The overfill in mL a user enters during verification. If this is not entered, overfill is pulled from the ERX level. |
| RX_OVERFILL_VOL | NUMERIC (18,2) | Holds the volume of the mixture/TPN after overfill has been applied. This is the sum of the volumes of ingredients that contribute to volume. This can be slightly different from volume plus overfill amount (either manual overfill or from the ERX record) due to dispense rounding factors. |
| ADM_INSTR_CHANGE_YN *(deprecated)* | VARCHAR (1) |  |
| IS_FAM_YN | VARCHAR (1) |  |
| ONE_STEP_MED_YN | VARCHAR (1) |  |
| RX_OVERFILL_TYPE_C | INTEGER |  |
| PRIOR_AUTH_STATUS_C | INTEGER |  |
| REFERRAL_AUTH_STATUS_C | INTEGER |  |
| RECIPE_AMOUNT | NUMERIC (19,4) | The recipe quantity amount for a ratio-based mixture medication (a medication which consists of a drug diluted in a base at a fixed concentration). |
| RECIPE_UNIT_C | INTEGER |  |
| ADMIN_INSTRUCTIONS_CHANGE_DTTM | DATETIME (Local) | Tracks the instant when the administration instructions were changed from their system default. |
| ADDL_DUES_REMAINING | INTEGER | The count of due times that need to be accounted for before the order can be considered complete, in addition to those that represent ordered due times. |
| HAS_COMPONENT_DATA_C | INTEGER |  |
| ORDERED_VOLUME_MED_UNIT_C | INTEGER |  |
| ORDERED_VOLUME | NUMERIC (19,4) | The volume as ordered. This volume can be in mL or in weight-based units. |
| RX_ENERGY_BASED_YN | VARCHAR (1) |  |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| B-TREE INDEX | EIX_ORDER_MEDINFO_DISPID_ORDID | DISPENSABLE_MED_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_ORDER_MEDINFO_DISPID_ORDID | ORDER_MED_ID | 2 | Yes | Yes |  |
| B-TREE INDEX | EIX_ORDER_MEDINFO_MEID | MEDICATION_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_ORDER_MEDINFO_PAID_CMP | PAT_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_ORDER_MEDINFO_PAID_CMP | PAT_ENC_DATE_REAL | 2 | Yes | Yes |  |

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
| 1 | ORDER_MED_ID | ORDER_MED_2 | ORDER_ID | Unknown | No | No |  |
| 1 | ORDER_MED_ID | ORDER_MED_3 | ORDER_ID | Unknown | No | No |  |
| 1 | ORDER_MED_ID | ORDER_MED_4 | ORDER_ID | Unknown | No | No |  |
| 1 | ORDER_MED_ID | ORDER_MED_5 | ORDER_ID | Unknown | No | No |  |
| 1 | ORDER_MED_ID | ORDER_MED_6 | ORDER_MED_ID | Unknown | No | No |  |
| 1 | ORDER_MED_ID | ORDER_MED_7 | ORDER_ID | No | No | No |  |

_(295 total; showing first 30)_
