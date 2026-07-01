# OR_ROOM_TEMPLATE_AUDIT

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=OR_ROOM_TEMPLATE_AUDIT

## Description

The OR_ROOM_TEMPLATE_AUDIT table stores the audit trail for OR templates.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | APPEND |
| Load Frequency | INCREMENTAL |
| Chronicles INI | SCH |
| Release Version | Rel 2015 |
| May contain EHI? | No |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| DEPARTMENT_ID | No | The unique ID of the department of the room template that was modified. |
| ROOM_ID | No | The unique ID of the room associated to the template that was modified. |
| AUDIT_DTTM | No | The date and time that the template was modified. |
| LINE | No | The line number for the information associated with the audit action. If the value is 0, this indicates that the template was deleted for that combination of room, date range and day of week. |
| AUDIT_ACTION_C | No | The audit action category ID for the template modification. |
| AUDIT_USER_ID | No | The unique ID of the user who modified the template. |
| TEMPLATE_START_DATE | No | The start of the date range that was altered by the associated audit action. |
| TEMPLATE_END_DATE | No | The end of the date range that was altered by the associated audit action. For indefinite templates, this column will be null. |
| DAY_OF_WEEK_C | No | The day of week category ID for day that was modified. |
| TEMPLATE_START_TIME | No | The start time of the slot length. |
| TEMPLATE_END_TIME | No | The end time of the slot length. |
| SLOT_LENGTH | No | The slot length (in minutes). |
| BLOCK_TYPE_C | No | The type of slot defined for the pattern. For open slots (blocks) the values are 0 for unblocked, 1 for service, 2 for physician, 3 for surgeon/physician group. For closed slots the values are 101 for on hold and 102 for time off. |
| BLOCK_ID | No | The associated category or record ID for the block. For service blocks, this is the surgical service category ID. For surgeon blocks, this is the surgeon ID. For surgeon group blocks, this is the group ID. This column will be null for time on the schedule that corresponds to unblocked, on hold, or time off.  This column should not be used in an IntraConnect setting. Instead, use SERVICE_C, SURGEON_ID and GROUP_ID to get the block owner. |
| BLOCK_KEY | No | The generated block key for this block. The string consists of a three letter acronym for the block type (SVC for service, SRG for surgeon, and GRP for surgeon group) and the category ID, if service, or the record ID, if surgeon or surgeon group. In an IntraConnect setting, the ID will be the Community ID (CID). For unblocked time, this will be "UNBLOCKED." Null will be returned for on hold and time off. |
| PUBLIC_YN | No | Indicates whether the slot is public. Y indicates that the slot is public. N indicates that the time is not public. |
| TIME_TYPE_C | No | The time type category ID for the slot on the template. The options are Open (1), On Hold (2), or Time Off (3). |
| TIME_OFF_REASON_C | No | The time off reason category ID for slots on the template that are marked as time off. |
| TEMPLATE_COMMENT | No | The comment associated with the slot on the template. |
| DEPLOYMENT_ID | No | The unique ID of the deployment from which the room template audit history was taken. |
| SERVICE_C | No | When the open slot type (block type) is 1 for service this is the service category ID. |
| SURGEON_ID | No | When the open slot type (block type) is 2 for surgeon/physician, this is the surgeon/physician ID. |
| GROUP_ID | No | When the open slot type (block type) is 3 for surgeon/physician group, this is the surgeon/physician group ID. |
| RESPONSIBLE_PROV_ID | No | The surgeon/physician responsible for the block, if any. |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | DEPARTMENT_ID | BH_DEP | DEPARTMENT_ID | No | Yes | No |  |
| 1 | DEPARTMENT_ID | CLARITY_DEP | DEPARTMENT_ID | No | Yes | No |  |
| 1 | DEPARTMENT_ID | CLARITY_DEP_2 | DEPARTMENT_ID | No | Yes | No |  |
| 1 | DEPARTMENT_ID | CLARITY_DEP_3 | DEPARTMENT_ID | No | Yes | No |  |
| 1 | DEPARTMENT_ID | CLARITY_DEP_4 | DEPARTMENT_ID | No | Yes | No |  |
| 1 | DEPARTMENT_ID | CLARITY_DEP_5 | DEPARTMENT_ID | No | Yes | No |  |
| 1 | DEPARTMENT_ID | CLARITY_DEP_MYC | DEPARTMENT_ID | No | Yes | No |  |
| 1 | DEPARTMENT_ID | DEPT_QUEUE_MSG_SETTINGS | DEPARTMENT_ID | No | Yes | No |  |
| 1 | DEPARTMENT_ID | DEPT_VERIFIED_INFO | DEPARTMENT_ID | No | Yes | No |  |
| 1 | DEPARTMENT_ID | DEP_BATCH_LTR_GEN | DEPARTMENT_ID | No | Yes | No |  |
| 1 | DEPARTMENT_ID | DEP_CE_SETTINGS | DEPARTMENT_ID | No | Yes | No |  |
| 1 | DEPARTMENT_ID | DP_HIDE_SENSITIVE_CONFIG | DEPARTMENT_ID | No | Yes | No |  |
| 1 | DEPARTMENT_ID | ED_ALRT_DFLT | DEPARTMENT_ID | No | Yes | No |  |
| 1 | DEPARTMENT_ID | ED_DEP_SETTINGS | DEP_ID | No | Yes | No |  |
| 1 | DEPARTMENT_ID | EXT_CAL_DEPT_CONFIG | DEPARTMENT_ID | No | Yes | No |  |
| 1 | DEPARTMENT_ID | VISIT_MODE_CONFIG_DEP | DEPARTMENT_ID | No | Yes | No |  |
| 1 | DEPARTMENT_ID | V_CUBE_D_DEPARTMENT | DEPARTMENT_ID | Unknown | Unknown | No |  |
| 1 | DEPARTMENT_ID | V_CUBE_D_DEP_LOC | DEPARTMENT_ID | Unknown | Unknown | No |  |
| 2 | ROOM_ID | CLARITY_SER | PROV_ID | Unknown | Yes | No |  |
| 2 | ROOM_ID | CLARITY_SER_2 | PROV_ID | Unknown | Yes | No |  |
| 2 | ROOM_ID | CLARITY_SER_3 | PROV_ID | Unknown | Yes | No |  |
| 2 | ROOM_ID | CLARITY_SER_4 | PROV_ID | No | Yes | No |  |
| 2 | ROOM_ID | CLARITY_SER_MYC | PROV_ID | Unknown | Yes | No |  |
| 2 | ROOM_ID | D_PROV_PRIMARY_HIERARCHY | PROV_ID | Unknown | Unknown | No |  |
| 2 | ROOM_ID | ED_SER_SETTINGS | PROV_ID | Unknown | Yes | No |  |
| 2 | ROOM_ID | EXT_CAL_PROV_CONFIG | PROV_ID | No | Yes | No |  |
| 2 | ROOM_ID | OR_SER_EQUIPMENT | PROV_ID | Unknown | Yes | No |  |
| 2 | ROOM_ID | OR_SER_ROOM | PROV_ID | Unknown | Yes | No |  |
| 2 | ROOM_ID | PROV_BATCH_LTR_GEN | PROV_ID | Unknown | Yes | No |  |
| 2 | ROOM_ID | PROV_GROUP | PROV_ID | No | Yes | No |  |

_(78 total; showing first 30)_
