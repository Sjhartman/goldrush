# F_SCHED_APPT_STATS

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=F_SCHED_APPT_STATS

## Description

Basic appointment statistics broken down by provider, department, and date. Note: if your organization uses joint appointments and can have the same department or same provider listed multiple times for an appointment, summaries at the department or provider level will double count those appointments.

## Metadata

| Property | Value |
| --- | --- |
| Type | Derived Table |
| Load Frequency | INCREMENTAL |
| Release Version | Summer 2009 |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| STATISTICS_DATE | No | The date for which the statistics were compiled. |
| PROV_ID | No | The unique ID associated with the provider record for this row. This column is frequently used to link to the CLARITY_SER table. |
| DEPARTMENT_ID | No | The unique ID associated with the department for this row. This column is frequently used to link to the CLARITY_DEP table. |
| UPDATE_DATE | No | The date and time when this row was created or last updated. |
| MASTER_SCHEDULABLE_HRS | No | The total number of hours in the schedule for this provider in this department. This includes time and days set as unavailable. |
| SCHEDULABLE_HRS | No | The total number of hours in the schedule for this provider in this department open for scheduling with patients. This does not include time and days unavailable. |
| BOOKED_HRS | No | The total number of hours in the schedule for this provider in this department scheduled with patients. |
| AVAIL_OPENINGS_ON_DAY_CNT | No | The count of both regular and overbook openings for this date that were available for scheduling on this date for this provider in this department.  This count will be the number of openings available at the very start of the day plus any openings made available by same day cancellations. |
| REG_OPENINGS_CNT | No | The number of regular openings for this provider in this department for this date. |
| SAME_DAY_REG_OPENINGS_USED_CNT | No | The number of openings with appointments scheduled for this provider in this department where the appointment was made the same day it occurred and did not cause the number of appointments for this slot to exceed the number of regular openings available. |
| PREVIOUS_REG_OPENINGS_USED_CNT | No | The number of openings with appointments scheduled for this provider in this department where the appointment was made prior to the day it occurred and did not exceed the number of regular openings available for that slot. |
| OVERBOOK_OPENINGS_CNT | No | The number of overbook openings for this provider in this department for this date. |
| SAME_DAY_OVRBK_OPENGS_USED_CNT | No | The number of openings with appointments scheduled for this provider in this department beyond the number of regular openings for the slot where the appointment was made the same day it occurred. |
| PREVIOUS_OVRBK_OPENGS_USED_CNT | No | The number of openings with appointments scheduled for this provider in this department beyond the number of regular openings for the slot where the appointment was made prior to the day it occurred. |
| ARRIVED_CNT | No | The number of appointments at a status of arrived for this date, this provider and this department. |
| NO_SHOW_CNT | No | The number of appointments at a status of no show for this date, this provider and this department. |
| LEFT_WO_SEEN_CNT | No | The number of appointments at a status of left without seen for this date, this provider and this department. |
| COMPLETED_CNT | No | The number of appointments at a status of completed for this date, this provider and this department. |
| SCHEDULED_CNT | No | The number of appointments at a status of scheduled for this date, this provider and this department. |
| CANCELED_CNT | No | The number of appointments at a status of canceled for this date, this provider and this department. |
| PATIENT_CANCELED_CNT | No | The number of appointments at a status of canceled for this date, this provider and this department where the cancellation was initiated by the patient. |
| SAME_DAY_CANCELED_CNT | No | The number of appointments at a status of canceled for this date, this provider and this department where the cancellation was entered the day of the appointment. |
| LATE_CANCELED_CNT | No | The number of appointments at a status of canceled for this date, this provider and this department where the cancellation was entered within the organization's late time frame. |
| LATE_PROV_CANCELED_CNT | No | The number of appointments at a status of canceled for this date, this provider and this department where the cancellation was initiated by a provider and was within the organization's late time frame for providers. Note:  for joint appointments, a late cancellation from one provider will count for all providers scheduled. |
| RESCHEDULED_APPT_CNT | No | The number of appointments at a status of canceled for this date, this provider and this department where the cancellation was initiated by the patient and another appointment was rescheduled in its place. |
| SAME_DAY_APPT_CNT | No | The number of same-day appointments scheduled for this date, this provider and this department. |
| APPT_WITH_PCP_CNT | No | The number of appointments for this date, this provider and this department where the provider is listed as any type of primary care provider for the patient. |
| APPT_FOR_TODAY_LEAD_DAYS | No | The sum of days between when an appointment was made and when it occurred for appointments scheduled for this date, this provider and this department.  Divide this by the APPT_FOR_TODAY_CNT to determine the average lead time for appointments occurring today.  This statistic can be rolled up to other time groupings such as week or month. |
| APPT_FOR_TODAY_CNT | No | The number of appointments for this date, this provider and this department. |
| APPT_MADE_TODAY_LEAD_DAYS | No | The sum of days between when an appointment was made and when it occurred for appointments scheduled on this date for this provider and this department.  Divide this by the APPT_MADE_TODAY_CNT to determine the average lead time for appointments made today.  This statistic can be rolled up to other time groupings such as week or month. |
| APPT_MADE_TODAY_CNT | No | The number of appointments made on this date for this provider and this department. |
| REG_AVAILABLE_HRS | No | The total number of hours in the schedule for this provider in this department open for scheduling with patients in regular openings. Slots with multiple regular openings are counted multiple times. Note that this excludes overbook openings and slots marked unavailable via time or day unavailable exceptions. It also excludes slots marked as held if the P_INCLUDE_HELD_AS_SCHEDULABLE property is set to No. |
| OVERBOOK_AVAILABLE_HRS | No | The total number of hours in the schedule for this provider in this department open for scheduling with patients in overbook openings. Slots with multiple overbook openings are counted multiple times. Note that this does not include time and days unavailable, nor does it include slots marked as held if the P_INCLUDE_HELD_AS_SCHEDULABLE property is set to No |
| UNAVAILABLE_OPENINGS_USED_CNT | No | The number of openings with appointments scheduled for this provider in this department in slots marked unavailable. Appointments in slots that are marked both held and unavailable will contribute to this count, but not to the HELD_OPENINGS_USED_CNT column. |
| HELD_OPENINGS_USED_CNT | No | The number of openings with appointments scheduled for this provider in this department in slots marked as held. Note that the value in this column does not depend on the P_INCLUDE_HELD_AS_SCHEDULABLE property. Appointments in slots that are marked both held and unavailable will contribute only to the UNAVAILABLE_OPENINGS_USED_CNT column, and not to this column. |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | PROV_ID | CLARITY_SER | PROV_ID | Unknown | Unknown | No |  |
| 2 | PROV_ID | CLARITY_SER_2 | PROV_ID | Unknown | Unknown | No |  |
| 2 | PROV_ID | CLARITY_SER_3 | PROV_ID | Unknown | Unknown | No |  |
| 2 | PROV_ID | CLARITY_SER_4 | PROV_ID | No | Unknown | No |  |
| 2 | PROV_ID | CLARITY_SER_MYC | PROV_ID | Unknown | Unknown | No |  |
| 2 | PROV_ID | D_PROV_PRIMARY_HIERARCHY | PROV_ID | Unknown | Unknown | No |  |
| 2 | PROV_ID | ED_SER_SETTINGS | PROV_ID | Unknown | Unknown | No |  |
| 2 | PROV_ID | EXT_CAL_PROV_CONFIG | PROV_ID | No | Unknown | No |  |
| 2 | PROV_ID | OR_SER_EQUIPMENT | PROV_ID | Unknown | Unknown | No |  |
| 2 | PROV_ID | OR_SER_ROOM | PROV_ID | Unknown | Unknown | No |  |
| 2 | PROV_ID | PROV_BATCH_LTR_GEN | PROV_ID | Unknown | Unknown | No |  |
| 2 | PROV_ID | PROV_GROUP | PROV_ID | No | Unknown | No |  |
| 2 | PROV_ID | V_CUBE_D_PROVIDER | PROVIDER_ID | Unknown | Unknown | No |  |
| 3 | DEPARTMENT_ID | BH_DEP | DEPARTMENT_ID | No | Unknown | No |  |
| 3 | DEPARTMENT_ID | CLARITY_DEP | DEPARTMENT_ID | No | Unknown | No |  |
| 3 | DEPARTMENT_ID | CLARITY_DEP_2 | DEPARTMENT_ID | No | Unknown | No |  |
| 3 | DEPARTMENT_ID | CLARITY_DEP_3 | DEPARTMENT_ID | No | Unknown | No |  |
| 3 | DEPARTMENT_ID | CLARITY_DEP_4 | DEPARTMENT_ID | No | Unknown | No |  |
| 3 | DEPARTMENT_ID | CLARITY_DEP_5 | DEPARTMENT_ID | No | Unknown | No |  |
| 3 | DEPARTMENT_ID | CLARITY_DEP_MYC | DEPARTMENT_ID | No | Unknown | No |  |
| 3 | DEPARTMENT_ID | DEPT_QUEUE_MSG_SETTINGS | DEPARTMENT_ID | No | Unknown | No |  |
| 3 | DEPARTMENT_ID | DEPT_VERIFIED_INFO | DEPARTMENT_ID | No | Unknown | No |  |
| 3 | DEPARTMENT_ID | DEP_BATCH_LTR_GEN | DEPARTMENT_ID | No | Unknown | No |  |
| 3 | DEPARTMENT_ID | DEP_CE_SETTINGS | DEPARTMENT_ID | No | Unknown | No |  |
| 3 | DEPARTMENT_ID | DP_HIDE_SENSITIVE_CONFIG | DEPARTMENT_ID | No | Unknown | No |  |
| 3 | DEPARTMENT_ID | ED_ALRT_DFLT | DEPARTMENT_ID | No | Unknown | No |  |
| 3 | DEPARTMENT_ID | ED_DEP_SETTINGS | DEP_ID | No | Unknown | No |  |
| 3 | DEPARTMENT_ID | EXT_CAL_DEPT_CONFIG | DEPARTMENT_ID | No | Unknown | No |  |
| 3 | DEPARTMENT_ID | VISIT_MODE_CONFIG_DEP | DEPARTMENT_ID | No | Unknown | No |  |
| 3 | DEPARTMENT_ID | V_CUBE_D_DEPARTMENT | DEPARTMENT_ID | Unknown | Unknown | No |  |

_(31 total; showing first 30)_
