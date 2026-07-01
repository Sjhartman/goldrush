# F_RX_ORDER

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=F_RX_ORDER

## Description

The F_RX_ORDER table contains information about medication orders prepared or supplied by inpatient pharmacies that is typically used in reports. Orders must be signed and released to be included in the table.

## Metadata

| Property | Value |
| --- | --- |
| Type | Derived Table |
| Load Frequency | INCREMENTAL |
| Release Version | Rel 2015 |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| ORDER_MED_ID | NUMERIC (18,0) | The unique ID of the medication order. |
| REPORT_DATE | 31 | The date the order was released. For conditional orders it is the initiation time. If the conditional order was never initiated, it is null. This column is commonly used as a date range in reports. |
| UPDATE_DATE | No | The date and time this row was last updated. |
| PAT_DEPT_ID | 48080 | The unique ID of the patient department at the time the order was released. For override pulls and bulk charges, this is the dispense department of the order. If an order's department cannot be found, the department of the order's encounter is used instead (PAT_ENC.EFFECTIVE_DEPT_ID). |
| ORDERING_DATE_REAL | FLOAT | The unique, internal contact date of the ordering contact of the order. This column is frequently used to link to the ORDER_DISP_INFO table. |
| FIRST_VERIFY_DATE_REAL | FLOAT | The unique, internal contact date of the first verification contact of the order. This column is frequently used to link to the ORDER_DISP_INFO table. |
| FIRST_VERIFY_DATE_REAL_LINE | No | The line number for the information associated with the last action taken in the verification queue during the order verification process. If the order was verified, this is the verification audit trail that corresponds with FIRST_VERIFY_DATE_REAL. This column is frequently used to link to the ORDER_RXVER_TRACE table. |
| LAST_VERIFY_DATE_REAL | FLOAT | The unique, internal contact date of the last verification contact of the order triggered by a user. This is the last verification contact where ORDER_MED.MED_VERIFY_TYPE_C is NOT 4-Modify On Patient Transfer, 5-Modify On Order Transfer, or 6-NDC replacement. This column is frequently used to link to the ORDER_DISP_INFO table to get information changed from orders that have been reverified. The last verification contact regardless of verify type can be found in ORDER_RXVER_NOADSN.LAST_VERIFY_DATE_REAL. |
| FIRST_DISPENSE_DATE_REAL | FLOAT | The unique, internal contact date of the first dispense contact of the order. This column is frequently used to link to the ORDER_DISP_INFO table. |
| FIRST_ADMIN_DATE_REAL | FLOAT | The unique, internal contact date of the first administration contact of the order. This is the first contact chronologically by the documented taken time, not the time the documentation occurred. This column is frequently used to link to the ORDER_DISP_INFO table. |
| FIRST_ADMIN_DATE_REAL_LINE | INTEGER | The line number for the information associated with the MAR action that created the first administration contact, FIRST_ADMIN_DATE_REAL. Only actions that create administration contacts and represent a patient taking medication (MAR_ADMIN_INFO.MAR_ACTION_C is 1-Given, 6-New Bag, 12-Bolus, 13-Push or custom actions mapped to these actions) are included. This column is frequently used to link to the MAR_ADMIN_INFO table. |
| FIRST_PEND_VERIFY_DATE_REAL | FLOAT | The unique, internal contact date of the first pend verify contact of the order. This column is frequently used to link to the ORDER_DISP_INFO table. |
| EFF_START_DTTM | DATETIME (Local) | The effective date and time when the medication order started. This might be different from the start time saved to the order. This column is used to attribute active orders to dates and departments over time. If EFF_START_DTTM is null, then the order is never considered active. See the description for EFF_END_DTTM for an example of how to use these two columns to find all orders active during a time range.  Special cases are described below where this column does not return the same date and time as ORDER_MED.ORDER_START_TIME:  EFF_START_DTTM is null for the following scenarios: * Bulk charge order is fully returned or linked to a clinical order * Non-clinical override pull is fully returned * Order is not released * Override pull is linked to a clinical order * Order released on cancelled or no show appointment * Order is conditional but was not initiated  One-step medication orders and unlinked override pulls return the first administration time.  Non-clinical override pulls return the time the order was created.  Bulk charge orders return the first date and time to have a value in the following order: * Service date and time * Service date * Order creation date and time |
| EFF_END_DTTM | 7069 | The effective date and time when the medication order ended. This might be different from the end time saved to the order. This column is used to attribute active orders to dates and departments over time. EFF_END_DTTM is not inclusive. If EFF_END_DTTM is null and EFF_START_DTTM is not null, the order is still active as of the last Clarity extract. Use EFF_START_DTTM and EFF_END_DTTM to find all orders active during a time range:  SELECT * FROM F_RX_ORDER WHERE EFF_START_DTTM <= [end of date and time range] AND (EFF_END_DTTM IS NULL OR EFF_END_DTTM) > [start of date and time range])   If the effective start and end date and time would be the same, EFF_END_DTTM returns EFF_START_DTTM + 1 minute because effective end time is not inclusive. Special cases are described below where the EFF_END_DTTM is not the same as ORDER_MED.ORDER_END_TIME:  EFF_END_DTTM returns null if EFF_START_DTTM is null. See the description for EFF_START_DTTM for when EFF_START_DTTM is null.  One-step medication orders and unlinked override pulls return the time of the last administration + 1 minute.  Non-clinical override pulls return the time the order was created.  Bulk charge orders return the first date and time to have a value in the following order: * Service date and time * Service date * Order creation date and time  The discharge time of the encounter is returned if there is no end time or if the discharge time is before the end time.  Some orders might not have an end time even though they should not be considered active. To avoid these orders being considered active forever, EFF_END_DTTM returns EFF_START_DTTM + 1 minute so that the order is only considered active for the day it started. This applies only if all of the following are true: * Order does not fit the other scenarios above * Order has no end time * Order's encounter is not an admission or there is no admission time |
| IVENT_BOOL | No | This column stores 1 if at least one intervention was documented for this order, otherwise it stores 0. |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| B-TREE INDEX | EIX_F_RX_ORDER_DATE | REPORT_DATE | 1 | Yes | Yes |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ORDER_MED_ID | ADT_ORDERS_ERRORS | ORDER_ID | No | Unknown | No |  |
| 1 | ORDER_MED_ID | ADT_ORDER_INFORMATION | ORDER_ID | No | Unknown | No |  |
| 1 | ORDER_MED_ID | APPT_REQUEST | REQUEST_ID | No | Unknown | No |  |
| 1 | ORDER_MED_ID | CL_ORD_FST_LST_SCH | ORDER_ID | No | Unknown | No |  |
| 1 | ORDER_MED_ID | DENT_ORD_NOADD | ORDER_ID | No | Unknown | No |  |
| 1 | ORDER_MED_ID | DUPMED_DISMISS_HH_INFO | ORDER_ID | No | Unknown | No |  |
| 1 | ORDER_MED_ID | ENDOSCOPY_METRICS | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_MED_ID | EXTERNAL_ORDER_INFO | ORDER_ID | No | Unknown | No |  |
| 1 | ORDER_MED_ID | F_IMG_STUDY | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_MED_ID | F_IP_HSP_SUM_ORDER | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_MED_ID | F_LAB_ORDERS | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_MED_ID | F_MU_OBJ_EH_PLACED_ORDER | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_MED_ID | F_MU_OBJ_EH_RESULTD_ORDER | ORDER_PROC_ID | Unknown | Unknown | No |  |
| 1 | ORDER_MED_ID | F_ONC_PRIOR_AUTH_ORDERS | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_MED_ID | F_OPIOID_ORDERS | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_MED_ID | HH_MED_ORD_IN_POC_DETAIL | ORDER_MED_ID | No | Unknown | No |  |
| 1 | ORDER_MED_ID | HV_ORDER_PROC | ORDER_PROC_ID | Unknown | Unknown | No |  |
| 1 | ORDER_MED_ID | MED_DETAILS_EXT_ORD | ORDER_ID | No | Unknown | No |  |
| 1 | ORDER_MED_ID | MERCHANDISE_ORDER_INFO | ORDER_ID | Yes | Unknown | No |  |
| 1 | ORDER_MED_ID | MU_EH_QRDA_I_ORDER | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_MED_ID | ORDERS | ORDER_ID | No | Unknown | No |  |
| 1 | ORDER_MED_ID | ORDER_AUTH_INFO | ORDER_ID | No | Unknown | No |  |
| 1 | ORDER_MED_ID | ORDER_MED | ORDER_MED_ID | Unknown | Unknown | No |  |
| 1 | ORDER_MED_ID | ORDER_MEDINFO | ORDER_MED_ID | Unknown | Unknown | No |  |
| 1 | ORDER_MED_ID | ORDER_MED_2 | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_MED_ID | ORDER_MED_3 | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_MED_ID | ORDER_MED_4 | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_MED_ID | ORDER_MED_5 | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_MED_ID | ORDER_MED_6 | ORDER_MED_ID | Unknown | Unknown | No |  |
| 1 | ORDER_MED_ID | ORDER_MED_7 | ORDER_ID | No | Unknown | No |  |

_(90 total; showing first 30)_
