# MAR_ADMIN_INFO

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=MAR_ADMIN_INFO

## Description

This table contains the currently active medication administration data. This includes all scheduled and acted upon administrations currently showing on the MAR.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | ORD |
| Release Version | Summer 2009 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| ORDER_MED_ID | NUMERIC (18,0) | The unique ID of the medication order. |
| LINE | INTEGER | The line count for the item. |
| CM_PHY_OWNER_ID | VARCHAR (25) | ID of the physical deployment owner for this record.  Physical owners will be where the data is hosted, either on the cross-over server or the owner deployment. |
| CM_LOG_OWNER_ID | VARCHAR (25) | ID of the logical deployment owner for this record.  Logical owners show the deployment where the record was created but doesn't represent if the record is a part of version skew. |
| TAKEN_TIME | DATETIME (Local) | The user-specified time that the action took place. |
| MAR_ORIG_DUE_TM | DATETIME (Local) | The original due time for the administration. |
| EDITED_LINE | INTEGER | The line number of the previously saved data for this administration. |
| SCHEDULED_TIME | DATETIME (Local) | The scheduled time on the MAR. |
| SAVED_TIME | DATETIME (Local) | The instant the medication administration was saved. |
| MAR_SCHD_DTTM | DATETIME (Local) | The instant the original due time was created by the scheduler.  This item is not populated for data saved by a user, including user-created due times. |
| MAR_TIME_SOURCE_C | INTEGER |  |
| MAR_ACTION_C | VARCHAR (66) |  |
| MAR_ENC_CSN | NUMERIC (18,0) | The unique contact serial number for the encounter that was accessed to administer the medication.  This number is unique across all patients and encounters in the system. |
| MAR_UNIT_NUM | VARCHAR (184) | The blood unit number associated with this administration. |
| USER_ID | VARCHAR (18) | The unique ID of the user that took action on the administration. |
| SEC_USER_ID | VARCHAR (18) | The unique ID of the secondary user associated with this administration. |
| MAR_DOC_USER_ID | VARCHAR (18) | User (EMP) ID of the user who documented the med administration. This item is null unless the administering user (ORD 11110) is different than the documenting user. |
| SIG | VARCHAR (184) | The dose value of the administration. |
| ROUTE_C | INTEGER |  |
| COMMENTS | VARCHAR (1000) | The comment associated with the administration. |
| REASON_C | INTEGER |  |
| SITE_C | VARCHAR (66) |  |
| INFUSION_RATE | VARCHAR (184) | The rate at which the medication was infused. |
| MAR_INF_RATE_UNIT_C | INTEGER |  |
| DOSE_UNIT_C | INTEGER |  |
| MAR_DURATION | VARCHAR (184) | The length of time the administration took to complete or infuse. |
| MAR_DURATION_UNIT_C | INTEGER |  |
| DEVICE_ID | VARCHAR (40) | The unique ID of the device that sent the administration data. |
| DEV_RECV_TIME | DATETIME (Local) | The instant the device recorded this administration data. |
| IDFY_DEV_DATA_C | INTEGER |  |
| MAR_IMM_LINK_ID | NUMERIC (18,0) | The unique ID of the immunization associated with this administration. |
| REQ_FLO_REASON_C | INTEGER |  |
| OVRD_LINK_STATUS_C | INTEGER |  |
| MAR_OVRD_LNK_USR_ID | VARCHAR (18) | The unique ID of the user that updated the linked status of the override pull administration. |
| FLO_DOC_MISSING_YN | VARCHAR (1) |  |
| CHART_CORR_ID | NUMERIC (18,0) | The unique ID of the chart correction associated with this administration. |
| MAR_ADMIN_DEPT_ID | NUMERIC (18,0) | The unique ID of the department associated with this administration. A department is associated with an administration by checking the following locations in this order: the order's dispensing department, the order's routing department, and the patient's location at the time of the administration. |
| MAR_COSIGN_COMPL_YN | VARCHAR (1) |  |
| MAR_ORD_DAT | NUMERIC (18,2) | The order contact for this administration. |
| SCAN_MODE_YN | VARCHAR (1) |  |
| DUE_ACTION_C | VARCHAR (66) |  |
| MAR_BILLING_PROV_ID | VARCHAR (18) | This stores the 'billing provider' for a given administration. |
| PAT_SUPPLIED_YN | VARCHAR (1) |  |
| PENDING_TYPE_C | INTEGER |  |
| MED_OVERRIDE_COUNT *(deprecated)* | INTEGER | In table MAR_ADMIN_INFO, the column MER_OVERRIDE_COUNT (ORD 11410) has been deprecated. This column has been replaced by MED_OVERRIDE_ALERT_ID. The deprecated columns data is no longer available since it is no longer extracted to clarity.  Previous Description:- The count of how many MAR override alerts are medication not scanned alerts. |
| PAT_OVERRIDE_COUNT *(deprecated)* | INTEGER | In table MAR_ADMIN_INFO, the column PAT_OVERRIDE_COUNT (ORD 11420) has been deprecated. This column has been replaced by PAT_OVERRIDE_ALERT_ID. The deprecated columns data is no longer available since it is no longer extracted to clarity.  Previous description: The count of how many MAR override alerts are patient not scanned alerts. |
| MED_OVRIDE_ALERT_ID | NUMERIC (18,0) | This column will list the overridden "Med not scanned" alert ID for an administration |
| PAT_OVRIDE_ALERT_ID | NUMERIC (18,0) | This column will list the overridden "Patient not scanned" alert ID for an administration |
| PAT_SCANCOMP_C | INTEGER |  |
| MED_SCANCOMP_C | INTEGER |  |
| BCMA_PAT_SCANCOMP_C | INTEGER |  |
| BCMA_MED_SCANCOMP_C | INTEGER |  |
| MAR_BLOOD_INFO_LN | INTEGER | The line number for the blood unit information associated with this administration. Together with ORDER_MED_ID, this forms the foreign key to the BLOOD_ADMIN_INFO table. |
| WAS_TIMELY_ADMIN_C | INTEGER |  |
| CLIENT_SRC_C | INTEGER |  |
| SUBSEQUENT_PARENT | INTEGER | If an administration is a subsequent bag due time, this item identifies the administration line number that created it. |
| SUBSEQUENT_CHILDREN | INTEGER | If an administration is part of a split bag sequence, this item identifies the line number of the subsequent bag administration that follows this administration as part of the current dose. |
| SUBSEQUENT_INFO_DAT | INTEGER | This item stores a DAT (of this record) used by the split bag workflow. The DAT is where information is stored regarding the number and kind of split in effect for this administration. |
| CYCLIC_RATE_PARENT_LINE | INTEGER | The line number of the parent administration of this cyclic rate change due time. |
| DDD_VALUE | NUMERIC (18,4) | The defined daily dose value of the administration. |
| MORPHINE_EQUIV_MG_DOSE | NUMERIC (18,3) | This column stores a non-rate-based or non-continuous medication administration's equivalent dose in terms of milligrams of morphine. This value represents the relative amount of opiates a patient received from the administration. For medications which do not contain an opioid as defined in System Definitions, this value is 0. For continuous opioids and opioids with a rate-based dose, this value is null. Patches are considered to have a rate-based dose for this column. This is not calculated for blood product, feeding product, or patient-controlled analgesic (PCA) administrations. |
| MORPHINE_EQUIV_MG_PER_HR_RATE | NUMERIC (18,3) | This column stores a rate-based or continuous medication administration's equivalent dose rate in terms of milligrams of morphine infused per hour. This value represents the relative amount of opiates a patient received over the duration of the administration. For medications which do not contain an opioid as defined in system definitions, this value will be zero. For non-continuous opioids and opioids with a non-rate-based dose, this value will be null. Patches are considered to have a rated-based dose for this column. This item is not calculated for blood product, feeding product, or patient-controlled analgesic (PCA) administrations. |
| ORIGINAL_AMOUNT | VARCHAR (184) | In workflows where weight-based dose simplification or unit conversion can happen, this column contains the originally documented amount. |
| ORIGINAL_UNIT_C | INTEGER |  |
| MAR_ORD_CONTACT_DATE_REAL | FLOAT | The ORD contact date for this administration in decimal format. The integer portion of the number indicates the date of the contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| CUP_IDENT | VARCHAR (24) | This is the ID that dictates which cup an administration belongs to. |
| CUP_SCANCOMP_C | INTEGER |  |
| CUP_SCAN_STATUS_C | INTEGER |  |
| SCHEDULED_DOSE_UNIT_C | INTEGER |  |
| SCHEDULED_DOSE | VARCHAR (184) | The dose that was scheduled to be due for the administration of an order with multiple possible doses. |
| CONCENTRATION | VARCHAR (254) | The concentration for the administration. |
| DUR_BASED_PARENT_LINE | INTEGER | The line number of the administration that created this duration-based due time. |
| DUR_BASED_CHILD_LINE | INTEGER | The line number of the duration-based due time administration that was created by this administration. |
| CYCLIC_RATE_CHILD_LINE | INTEGER | The line number of the following child administration of this cyclic rate change due time. |
| SCHEDULED_AMOUNT | VARCHAR (184) | Scheduled administration amount when the order has multiple doses. |
| SCHEDULED_AMOUNT_UNIT_C | INTEGER |  |
| CUP_OVRIDE_ALERT_ID | NUMERIC (18,0) | This item will list the overridden "Container not scanned" alert for an administration. |
| BCMA_CUP_SCANCOMP_C | INTEGER |  |
| MULTILINE_SIG_PERIOD | VARCHAR (50) | Stores the multiline sig period that created the administration instance. |
| MULTILINE_SIG_PART | VARCHAR (50) | Stores the multiline sig part that created the administration instance. |
| MAR_PEND_USER_ID | VARCHAR (18) | The unique ID of the user with deferred signoff for the administration. |
| MAR_PEND_SECOND_USER_ID | VARCHAR (18) | The verifying user with deferred signoff |
| TCI_CONCENTRATION | VARCHAR (184) | Target concentration of the TCI pump |
| TCI_CONCENTRATION_UNIT_C | INTEGER |  |
| TCI_MODEL_C | INTEGER |  |
| TCI_TARGET_C | INTEGER |  |
| HOLD_DUR_DOSES | INTEGER | Stores the number of doses that a medication should be on hold for |
| HOLD_DUR_INST_DTTM | DATETIME (Local) | Stores the instant that a medication should be on hold until |
| HOLD_DUR_RETURN | INTEGER | Stores the number of doses that were returned after the hold was completed, for cases where doses were given to the patient for self-administration |
| MAR_PSP_IDENT | VARCHAR (180) | This is the identifier that dictates which patient-specific package belongs to an administration. This can also be a comma delimited list of identifiers if multiple patient-specific packages are scanned for a single administration. |
| PSP_SCANCOMP_C | INTEGER |  |
| PSP_OVRIDE_ALERT_ID | NUMERIC (18,0) | This item will list the overridden "Patient-Specific Package not scanned" alert ID for an administration. |
| BCMA_PSP_SCANCOMP_C | INTEGER |  |
| MAR_DUAL_SIGN_SOURCE_C | INTEGER |  |
| PENDED_DUE_ACTION_C | VARCHAR (66) |  |
| TAKEN_UTC_DTTM | DATETIME (UTC) | This is the instant that the administration action took place in UTC. |
| SAVED_UTC_DTTM | DATETIME (UTC) | This is the instant that the administration is saved in UTC. |
| MAR_ORIG_DUE_UTC_DTTM | DATETIME (UTC) | Contains the original due time for the administration in UTC. |
| DUR_BASED_PARENT_ORDER_ID | NUMERIC (18,0) | For a duration-based child administration, this item stores the order ID of its parent. When the duration-based parent and child administrations are on the same order, this item is null. |
| AN_BCMA_MED_SCANCOMP_C | INTEGER | Surrogate key used to uniquely identify rows in this (and only this) table on Cogito Cloud only, do not assume the surrogate key in this table will correspond to the surrogate key in another table |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| B-TREE INDEX | EIX_MARADMIN_ACTION_SAVED_TIME | MAR_ACTION_C | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_MARADMIN_ACTION_SAVED_TIME | SAVED_TIME | 2 | Yes | Yes |  |
| B-TREE INDEX | EIX_MARADMIN_ACTION_SCHED_TIME | MAR_ACTION_C | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_MARADMIN_ACTION_SCHED_TIME | SCHEDULED_TIME | 2 | Yes | Yes |  |
| B-TREE INDEX | EIX_MARADMIN_ACTION_USER | USER_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_MARADMIN_MAR_ENC_CSN | MAR_ENC_CSN | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_MARADMIN_MAR_ENC_CSN | ORDER_MED_ID | 2 | Yes | Yes |  |
| B-TREE INDEX | EIX_MARADMIN_SAVED_TIME | SAVED_TIME | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_MARADMIN_SAVED_TIME | USER_ID | 2 | Yes | Yes |  |
| B-TREE INDEX | EIX_MARADMIN_TAKEN_TIME | TAKEN_TIME | 1 | Yes | Yes |  |

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
| 1 | ORDER_MED_ID | ORDER_MED_6 | ORDER_MED_ID | Unknown | No | No |  |

_(437 total; showing first 30)_
