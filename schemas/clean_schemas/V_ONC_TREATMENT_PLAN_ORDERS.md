# V_ONC_TREATMENT_PLAN_ORDERS

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=V_ONC_TREATMENT_PLAN_ORDERS

## Description

A dimensional view which combines the various pieces of the treatment plan structure (plan, cycle, day, and order). It includes links to the episode, the patient, and the visit on which the plan was created, as well as some high-level info at those levels. The view contains one row for each order template (OTP) on the treatment plan.  This view may contain more than a single row for each OTP in some cases, like plans with linked days.

## Metadata

| Property | Value |
| --- | --- |
| Type | View |
| Release Version | Rel 2015 |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| TREATMENT_PLAN_ID | NUMERIC (18,0) | The record ID for the treatment plan. |
| PLAN_RECORD_TYPE_C | INTEGER |  |
| PLAN_STATUS_C | INTEGER |  |
| PLAN_STATUS_NAME | 30 |  |
| PLAN_VERSION | INTEGER | The lowest version in which the treatment plan was edited. This data is used to determine which features are enabled for the plan. |
| PLAN_CREATED_DATETIME | DATETIME (Attached) | The date and time at which the treatment plan was created. |
| PLAN_CREATOR_USER_ID | VARCHAR (18) | The user ID of the person who created the treatment plan. |
| PLAN_START_DATE | DATETIME | The start date of the treatment plan. |
| PLAN_DISCON_DATETIME | DATETIME (Local) | The date and time at which the treatment plan was discontinued. |
| PLAN_DISCON_USER_ID | VARCHAR (18) | The user ID of the person who discontinued the treatment plan. |
| PLAN_DISCON_REASON_C | VARCHAR (66) |  |
| PLAN_DISCON_REASON_NAME | 120 |  |
| PLAN_NAME | VARCHAR (200) | The name of the treatment plan. |
| PLAN_DISPLAY_NAME | VARCHAR (500) | The treatment plan display name as entered by the user. |
| PROTOCOL_ID | NUMERIC (18,0) | The ID of the protocol from which the treatment plan was generated. |
| PROTOCOL_CONTACT_DATE_REAL | FLOAT | The contact date real of the protocol from which the treatment plan was generated. The contact date real is a unique, internal contact date in decimal format. The integer portion of the number indicates the date of the contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| PROTOCOL_CONTACT_NUM | VARCHAR (5) | The contact number of the protocol from which the treatment plan was generated. |
| PROTOCOL_NAME | VARCHAR (200) | The record name of the protocol from which the treatment plan was generated. |
| PROTOCOL_DISPLAY_NAME | VARCHAR (500) | The display name of the protocol from which the treatment plan was generated. |
| PROTOCOL_IS_RESEARCH_YN | VARCHAR (1) |  |
| PLAN_PROV_ID | VARCHAR (18) | The provider ID of the person who is managing the treatment plan. |
| REFERRAL_ID | NUMERIC (18,0) | The ID of the linked referral used for prior authorization of the treatment plan. |
| TREATMENT_GOAL_C | INTEGER |  |
| TREATMENT_GOAL_NAME | 10000 |  |
| EPISODE_ID | NUMERIC (18,0) | The ID of the episode record to which the treatment plan is linked. |
| EPISODE_TYPE_ID | NUMERIC (18,0) | The record ID of the episode type for the episode to which the treatment plan is linked. |
| EPISODE_TYPE_NAME | VARCHAR (254) | The name of the episode type for the episode to which the treatment plan is linked. |
| PAT_ID | VARCHAR (18) | The record ID of the patient to whom the treatment plan was applied. |
| PLAN_STARTING_CYCLE_NUM | INTEGER | The cycle number of the cycle marked as the 'start cycle' in the treatment plan. |
| CYCLE_ID | VARCHAR (100) | The internal, plan-level ID for the treatment cycle. Note that this cycle ID is NOT unique across treatment plans. |
| CYCLE_NAME | 1010 | The name of the treatment cycle. |
| CYCLE_NUM | INTEGER | The user-facing cycle number of the treatment cycle. |
| CYCLE_START_DATE | DATETIME | The start date of the treatment cycle. |
| CYCLE_STATUS_C | INTEGER |  |
| CYCLE_STATUS_NAME | 1020 |  |
| TREATMENT_DAY_ID | NUMERIC (18,0) | The record ID of the treatment day. Note that the the treatment day ID may not be unique within the treatment plan. If the treatment cycle in which this treatment day resides is a repeating cycle, and this day (and other days in the same cycle, or days in the future cycles which repeat) are also planned, the day ID found in this column will be the same across those treatment days. If a modification is made to any orders within a treatment day and those changes are not propagated, or if the treatment day is started, then the treatment day will have a unique ID. |
| TREAT_DAY_CONTACT_DATE_REAL | FLOAT | The contact date real of the treatment day.  The contact date real is a unique, internal contact date in decimal format. The integer portion of the number indicates the date of the contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| TREATMENT_DAY_NAME | 5015 | The name of the treatment day. |
| DAY_NUM | INTEGER | The day number of the treatment day. |
| DAY_TYPE_C | VARCHAR (66) |  |
| TREATMENT_DAY_TREATMENT_DATE | DATETIME | This column initially stores the date of the planned treatment. This date is updated when certain actions are taken on the treatment day. The actions that update this value include starting, completing, deferring, and marking the day as given externally. The updated date in this case is the date on which the action (starting, completing, deferring, or marking the day as given externally) was taken. |
| TREATMENT_DAY_PLANNED_DATE | DATETIME | This column stores the date of the planned treatment. This date is updated when the treatment day's date is adjusted due to changes in the plan's, cycle's, or day's date. |
| DAY_LENGTH | INTEGER | The number of calendar days that are represented by the treatment day. |
| DAY_STARTED_DATETIME | DATETIME (UTC) | The date and time at which the treatment day was started. |
| DAY_STATUS_C | INTEGER |  |
| DAY_STATUS_NAME | 5050 |  |
| DAY_STATUS_CHANGE_USER_ID | VARCHAR (18) | The ID of the user who last changed the status of the treatment day. |
| DAY_STATUS_CHANGE_DATETIME | DATETIME (Local) | The date and time at which the day status last changed. |
| DAY_STATUS_CHANGE_COMMENTS | VARCHAR (254) | The status change comments for the treatment day. |
| CANCEL_DAY_REASON_C | INTEGER |  |
| CANCEL_DAY_REASON_NAME | 305 |  |
| DEFER_DAY_REASON_C | INTEGER |  |
| DEFER_DAY_REASON_NAME | 300 |  |
| DAY_GIVEN_EXTERNAL_REASON_C | INTEGER |  |
| DAY_GIVEN_EXTERNAL_REASON_NAME | 315 |  |
| ORDER_TEMPLATE_ID | 60 | The record ID for the order template. |
| ORDER_TEMPLATE_IS_DELETED_YN | 60 | Y/N flag to indicate whether this order template was deleted from its corresponding treatment day. |
| ORDER_CATEGORY_C | 75 |  |
| ORDER_CATEGORY_NAME | 30 |  |
| ORDER_TEMPLATE_SOURCE_AOG_ID | 160 | If the order template was added from an advanced order group (AOG), this column will hold the ID of the advanced order group order template from which this order template was added. |
| ORDER_TEMPLATE_DISPLAY_NAME | VARCHAR (500) | The display name of the order template. This is the name of the order, as it appeared in the order composer, when the order template was generated. |
| ORDER_TEMPLATE_DESCRIPTION | VARCHAR (254) | The description of the order template. This is the record name for the medication or procedure record at the time the order template was generated. |
| PROC_ID | NUMERIC (18,0) | The record ID of the procedure from which the order template was created. |
| MEDICATION_ID | NUMERIC (18,0) | The record ID of the medication from which the order template was created. |
| ORDER_DISCRETE_DOSE_MIN | VARCHAR (254) | The minimum dose for the order template. If the medication dose was entered as a range, this column will hold the minimum discrete dose amount. If the medication dose was NOT entered as a range, this column will hold the discrete dose amount. |
| ORDER_DISCRETE_DOSE_MAX | VARCHAR (254) | The maximum dose for the order template. If the medication dose was entered as a range, this column will hold the maximum discrete dose amount. If the medication dose was NOT entered as a range, this column will be blank. |
| ORDER_DOSE_UNIT_C | INTEGER |  |
| ORDER_DOSE_UNIT_NAME | VARCHAR (254) |  |
| ORDER_TYPE_C | INTEGER |  |
| ORDER_TYPE_NAME | VARCHAR (254) |  |
| ORDERING_MODE_C | INTEGER |  |
| ORDER_ID | NUMERIC (18,0) | The record ID for the order linked to the order template. |
| ORDER_RELEASED_PAT_ENC_CSN_ID | NUMERIC (18,0) | The contact serial number (CSN) of the patient encounter in which the order was released. |
| ORDER_REQUIRES_PRIOR_AUTH_YN | VARCHAR (1) |  |
| ORDER_TEMPLATE_SIGNED_PROV_ID | VARCHAR (18) | The provider ID of the person whose authorization makes it possible to release the order. For a dual-sign medication order, this column holds the provider ID of the person who provided the second signature. For all other orders, this column holds the provider ID of the person who signed the order. |
| ORDER_TEMPLATE_SIGNED_DATETIME | DATETIME (Local) | The date and time when the order template was authorized for release. For a dual-sign medication order, this column holds the date and time when the second signature was provided. For all other orders, this column holds the date and time when the order was signed. |
| DUAL_SIGN_FIRST_SIGN_PROV_ID | VARCHAR (18) | For a dual-sign medication order, this column holds the provider ID of the person who provided the first signature. For all other orders, this column is blank. |
| DUAL_SIGN_FIRST_SIGN_DATETIME | DATETIME (Local) | For a dual-sign medication order, this column holds the date and time when the first signature was provided. For all other orders, this column is blank. |
| ORDERING_PROV_ID | VARCHAR (18) | The provider ID of the ordering provider for the order template. |
| AUTH_PROV_ID | VARCHAR (18) | The provider ID of the authorizing provider for the order template. |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | TREATMENT_PLAN_ID | DENT_TREATMENT | TREATMENT_ID | No | Unknown | No |  |
| 1 | TREATMENT_PLAN_ID | TPL_HSB_EPT_LINK | TREATMENT_PLAN_ID | Unknown | Unknown | No |  |
| 1 | TREATMENT_PLAN_ID | TPL_INFO | TREATMENT_PLAN_ID | No | Unknown | No |  |
| 2 | PLAN_RECORD_TYPE_C | ZC_PLAN_REC_TYP | PLAN_REC_TYP_C | No | Unknown | No |  |
| 3 | PLAN_STATUS_C | ZC_PLAN_STATUS | PLAN_STATUS_C | No | Unknown | No |  |
| 7 | PLAN_CREATOR_USER_ID | CLARITY_EMP | USER_ID | Unknown | Unknown | No |  |
| 7 | PLAN_CREATOR_USER_ID | CLARITY_EMP_2 | USER_ID | Unknown | Unknown | No |  |
| 7 | PLAN_CREATOR_USER_ID | CLARITY_EMP_3 | USER_ID | Unknown | Unknown | No |  |
| 7 | PLAN_CREATOR_USER_ID | CLARITY_EMP_4 | USER_ID | No | Unknown | No |  |
| 7 | PLAN_CREATOR_USER_ID | CLARITY_EMP_DEMO | USER_ID | No | Unknown | No |  |
| 7 | PLAN_CREATOR_USER_ID | EMP_BASIC_INFO | USER_ID | No | Unknown | No |  |
| 7 | PLAN_CREATOR_USER_ID | EMP_DOC_SETTINGS | USER_NUMBER_ID | No | Unknown | No |  |
| 7 | PLAN_CREATOR_USER_ID | F_RX_USER | USER_ID | Unknown | Unknown | No |  |
| 7 | PLAN_CREATOR_USER_ID | IB_MESSAGE_SETTINGS | USER_ID | No | Unknown | No |  |
| 7 | PLAN_CREATOR_USER_ID | LOGIN_INFO | USER_NUMBER_ID | No | Unknown | No |  |
| 7 | PLAN_CREATOR_USER_ID | QC_RESULTS_REVIEW | USER_NUMBER_ID | No | Unknown | No |  |
| 7 | PLAN_CREATOR_USER_ID | USER_SIDEBAR_RPT | USER_NUMBER_ID | Unknown | Unknown | No |  |
| 7 | PLAN_CREATOR_USER_ID | V_CUBE_D_USER | USER_ID | Unknown | Unknown | No |  |
| 7 | PLAN_CREATOR_USER_ID | V_CUBE_RX_USER | USER_ID | Unknown | Unknown | No |  |
| 10 | PLAN_DISCON_USER_ID | CLARITY_EMP | USER_ID | Unknown | Unknown | No |  |
| 10 | PLAN_DISCON_USER_ID | CLARITY_EMP_2 | USER_ID | Unknown | Unknown | No |  |
| 10 | PLAN_DISCON_USER_ID | CLARITY_EMP_3 | USER_ID | Unknown | Unknown | No |  |
| 10 | PLAN_DISCON_USER_ID | CLARITY_EMP_4 | USER_ID | No | Unknown | No |  |
| 10 | PLAN_DISCON_USER_ID | CLARITY_EMP_DEMO | USER_ID | No | Unknown | No |  |
| 10 | PLAN_DISCON_USER_ID | EMP_BASIC_INFO | USER_ID | No | Unknown | No |  |
| 10 | PLAN_DISCON_USER_ID | EMP_DOC_SETTINGS | USER_NUMBER_ID | No | Unknown | No |  |
| 10 | PLAN_DISCON_USER_ID | F_RX_USER | USER_ID | Unknown | Unknown | No |  |
| 10 | PLAN_DISCON_USER_ID | IB_MESSAGE_SETTINGS | USER_ID | No | Unknown | No |  |
| 10 | PLAN_DISCON_USER_ID | LOGIN_INFO | USER_NUMBER_ID | No | Unknown | No |  |
| 10 | PLAN_DISCON_USER_ID | QC_RESULTS_REVIEW | USER_NUMBER_ID | No | Unknown | No |  |

_(441 total; showing first 30)_
