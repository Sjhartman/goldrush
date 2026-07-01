# OTP_INFO_1

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=OTP_INFO_1

## Description

This table is a continuation of related table OTP_INFO. It stores additional information about a treatment plan order, such as verbal signing information, inpatient medication information, etc.

**Overflow table** for OTP_INFO (100 cols). Contains additional columns for the same records — join on the shared primary key column.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | OTP |
| Release Version | SPRING 2008 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| OTP_ID | NUMERIC (18,0) | The unique identifier for the patient order template record. |
| CM_PHY_OWNER_ID | VARCHAR (25) | ID of the physical deployment owner for this record.  Physical owners will be where the data is hosted, either on the cross-over server or the owner deployment. |
| CM_LOG_OWNER_ID | VARCHAR (25) | ID of the logical deployment owner for this record.  Logical owners show the deployment where the record was created but doesn't represent if the record is a part of version skew. |
| TRANSPORTATION_C | INTEGER |  |
| IP_DISC_INTERVAL_ID | VARCHAR (18) | The discrete interval associated with the order template in this row. |
| IP_STANDING_COUNT | NUMERIC (18,0) | The standing count associated with the order template in this row. |
| IP_STAND_CNT_TYPE_C | INTEGER |  |
| IP_INCLUDE_NOW_C | INTEGER |  |
| SCHED_EXTRA_DOSE_TM | DATETIME (Local) | The time at which to schedule the first occurrence of the associated order template in this row. |
| COST_CENTER_ID | NUMERIC (18,0) | The unique identifier for the cost center associated with the order template in this row. |
| ORDERING_MODE_C | INTEGER |  |
| SELF_ADMIN_YN | VARCHAR (1) |  |
| PAT_SUPP_MED_YN | VARCHAR (1) |  |
| PAT_SUPPLIED_DOSES | NUMERIC (18,0) | The number of patient supplied doses. |
| CALC_DOSE_AMOUNT | VARCHAR (254) | The calculated dose to administer for the order template in this row. |
| CALC_DOSE_UNIT_C | INTEGER |  |
| DOSE_CALC_INFO | VARCHAR (1000) | The dose calculation information for the order template in this row. |
| ADMIN_DOSE | VARCHAR (100) | The amount to administer for the medication in this order template. |
| ADMIN_UNIT_C | INTEGER |  |
| VERB_ORD_TYPE_C | INTEGER |  |
| VERB_ORD_COMM_ID | VARCHAR (18) | The provider ID of the verbal order communicator for the order template in this row. |
| VERB_ORD_SIGNER_ID | VARCHAR (18) | The user ID of the verbal order signer for the order template in this row. |
| VERB_ORD_MSGRCP_ID | VARCHAR (18) | The user ID of the verbal order message recipient for the order template in this row. |
| VERB_ORD_MSG_ID | VARCHAR (18) | The ID of the verbal order message. |
| VERB_ORD_SIGN_INST | DATETIME (Attached) | The date/time in external format when the verbal order was signed. |
| VERB_ORD_MODE_C | INTEGER |  |
| ORD_PROV_ID | VARCHAR (18) | The provider ID of the ordering provider for the order template in this row. |
| AUTH_PROV_ID | VARCHAR (18) | The unique identifier for the authorizing provider for the order template in this row. |
| VERB_ORD_CMT *(deprecated)* | VARCHAR (500) |  |
| CALC_RATE_FRM_VD_YN | VARCHAR (1) |  |
| CONDITION_FLAG | NUMERIC (18,0) | The condition flag for the order template in this row. |
| MED_DOSE_PP_DESC | VARCHAR (2000) | The free text description of the dose calculation for the order template in this row. |
| OTP_ISOLATION_C | INTEGER |  |
| OTP_CODESTATUS_C | VARCHAR (66) |  |
| CODESTATUS_COMMENT | VARCHAR (1024) | The code status comments for the order template in this row. |
| DIET_C | INTEGER |  |
| DIET_COMMENTS | VARCHAR (1024) | The diet comments in the order template in this row. |
| DOSE_ADJ_TYPE_C | INTEGER |  |
| DOSE_ADJ_OVERRID_YN | VARCHAR (1) |  |
| EFQ_OVRD_DAY_TYPE | INTEGER | If column EFQ_OVRD_REL_DAYS in table OTP_FREQ_OV_REL_D is populated, this item specifies what the numeric values in that item represent. If this item's value is 1, then column EFQ_OVRD_CYCL_LEN stores relative days, otherwise OTP_FREQ_OV_REL_D  stores weekdays. |
| EFQ_OVRD_CYCL_LEN | INTEGER | If EFQ_OVRD_DAY_TYPE is 1 (meaning the override times stored in the record are relative cycles), then this item stores the length of the cycle. |
| ORX_ID | NUMERIC (18,0) | Networked Order Lookup Index Panel ID of an order template record applied to a patient. |
| MED_DFL_DISCRETE_YN | VARCHAR (1) |  |
| CSGN_CREATE_DTTM | DATETIME (UTC) | When the cosign requirement was created (UTC Time). |
| DFI_ID | NUMERIC (18,0) | The unique identifier for the Deficiency Instance record associated with the cosignature requirement for this order. |
| CSGN_RQRD_C | INTEGER |  |
| PT_SIG_SMARTTEXT_ID | VARCHAR (18) | Stores the SmartText ID used for generating the patient sig. If blank, then the standard sig generation logic was used. |
| MEDS_ACTION_VERB_C | INTEGER |  |
| PRIOR_AUTH_NEEDED_YN | VARCHAR (1) |  |
| UNROUNDED_DOSE_MIN | NUMERIC (19,4) | The unrounded dose of this order. If the dose has a range (e.g. 1-2 mg), this is the lower end of the range. If the dose does not have a range, then this will store the dose. |
| UNROUNDED_DOSE_MAX | NUMERIC (19,4) | The unrounded dose of this order. If the dose has a range (e.g. 1-2 mg), this is the upper end of the range. Otherwise, this is null. |
| UNROUND_DOSE_UNIT_C | INTEGER |  |
| LAST_DEVIATION_DTTM *(deprecated)* | DATETIME (UTC) |  |
| UPDATE_REASON_C | INTEGER |  |
| UPDATE_COMMENT | VARCHAR (254) | This column reflects the comment (associated with the reason in column UPDATE_REASON_C) explaining why a patient order template was most recently edited. To see past comments, view the OTP_AUDIT_TRAIL table. |
| ASSISTANCE_MEDICAL_COND_ID | NUMERIC (18,0) | The unique ID associated with an Indication that is used to justify the use of an expensive medication for a patient. |
| ASSISTANCE_ELIGIBILITY_FREETXT | VARCHAR (1000) | The reason why an Indication record was not selected by the user. |
| HOSP_PERFORMED_YN | VARCHAR (1) |  |
| TO_PHARMACY_ID | NUMERIC (18,0) | The pharmacy that the order will be sent to. |
| MLSIG_SIGTYPE_C | INTEGER |  |
| COLLECTED_BY_USER_ID | VARCHAR (18) | This is the user who collected the specimen. |
| COUNT_RANGE | VARCHAR (20) | This item stores a ranged value for the count of the order that goes along with the standing count type, indicating the number of hours, days, weeks, or occurrences for which the order will take place. Currently only available in Finland. |
| COUNT_RANGE_STND_TP_C | INTEGER |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | OTP_ID | ADT_PAT_ORDER_TEMPLATE | OTP_ID | No | No | No |  |
| 1 | OTP_ID | CL_OTP_FST_LST_SCH | OTP_ID | Unknown | No | No |  |
| 1 | OTP_ID | OTP_DOSE_PARAMS | OTP_ID | Unknown | No | No |  |
| 1 | OTP_ID | OTP_INFO | OTP_ID | Unknown | No | No |  |
| 1 | OTP_ID | OTP_INFO_2 | OTP_ID | Unknown | No | No |  |
| 1 | OTP_ID | OTP_INFO_3 | OTP_ID | Unknown | No | No |  |
| 1 | OTP_ID | OTP_INFO_4 | OTP_ID | Unknown | No | No |  |
| 1 | OTP_ID | OTP_INFO_5 | OTP_ID | No | No | No |  |
| 1 | OTP_ID | OTP_ROUTING | OTP_ID | Unknown | No | No |  |
| 2 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 2 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 2 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 3 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 4 | TRANSPORTATION_C | ZC_TRANSPORT | TRANSPORT_C | No | No | No |  |
| 5 | IP_DISC_INTERVAL_ID | FREQ_INCL_OR_EXCL_DEPS | FREQ_ID | No | No | No |  |
| 5 | IP_DISC_INTERVAL_ID | FREQ_INCL_OR_EXCL_FACS | FREQ_ID | No | No | No |  |
| 5 | IP_DISC_INTERVAL_ID | FREQ_INCL_OR_EXCL_LEDS | FREQ_ID | No | No | No |  |
| 5 | IP_DISC_INTERVAL_ID | IP_FREQUENCY | FREQ_ID | No | No | No |  |
| 7 | IP_STAND_CNT_TYPE_C | ZC_STND_TP | STND_TP_C | No | No | No |  |
| 8 | IP_INCLUDE_NOW_C | ZC_IP_INCLUDE_NOW | IP_INCLUDE_NOW_C | No | No | No |  |
| 10 | COST_CENTER_ID | CL_COST_CNTR | COST_CNTR_ID | No | No | No |  |
| 11 | ORDERING_MODE_C | ZC_ORDERING_MODE | ORDERING_MODE_C | No | No | No |  |
| 16 | CALC_DOSE_UNIT_C | ZC_MED_UNIT | DISP_QTYUNIT_C | No | No | No |  |
| 19 | ADMIN_UNIT_C | ZC_MED_UNIT | DISP_QTYUNIT_C | No | No | No |  |
| 20 | VERB_ORD_TYPE_C | ZC_VERB_ORD_TYPE | SIGNED_TYPE_C | No | No | No |  |
| 21 | VERB_ORD_COMM_ID | CLARITY_SER | PROV_ID | Unknown | No | No |  |
| 21 | VERB_ORD_COMM_ID | CLARITY_SER_2 | PROV_ID | Unknown | No | No |  |
| 21 | VERB_ORD_COMM_ID | CLARITY_SER_3 | PROV_ID | Unknown | No | No |  |

_(141 total; showing first 30)_
