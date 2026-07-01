# OR_ROOM_TEMPLATE

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=OR_ROOM_TEMPLATE

## Description

The OR_ROOM_TEMPLATE table includes scheduling template slot patterns for operating rooms. A slot is an exclusive range of reserved scheduling time within a day. The pattern is a collection of slots that apply to one day of the week (e.g. Thursdays only) over a date range. Use V_OR_ROOM_TEMPLATE view to retrieve an operating room template for specific calendar days.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | FULL |
| Load Frequency | WEEKLY - FULL |
| Chronicles INI | N/A |
| Release Version | Rel 2015 |
| May contain EHI? | No |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| ROOM_ID | No | The unique record ID of the room resource. |
| DAY_OF_THE_WEEK_C | No | The category number of the day of the week (e.g. 0 is Thursday). |
| PATTERN_START_DATE | No | The start date for the pattern that applies to the room template. |
| PATTERN_END_DATE | No | The end date for the pattern that applies to the room template. |
| SLOT_TYPE_C | No | The type of slot defined for the pattern. For open slots (blocks) the values are 0 for unblocked, 1 for service, 2 for physician, 3 for surgeon/physician group. For closed slots the values are 101 for on hold and 102 for time off. |
| SLOT_START_TIME | No | The start time for the slot within the pattern. The value returned by this column will be between 12:00 AM January 1 1900 and 12:00 AM January 2 1900. |
| SLOT_END_TIME | No | The end time for the slot within the pattern. The value returned by this column will be between 12:00 AM January 1 1900 and 12:00 AM January 2 1900. |
| PUBLIC_SLOT_YN | No | Indicates whether the slot type is public. |
| SERVICE_C | No | When the open slot type (block type) is 1 for service, this is the service category ID value. |
| SURGEON_ID | No | When the open slot type (block type) is 2 for physician, this is the surgeon/physician ID value. |
| GROUP_ID | No | When the open slot type (block type) is 3 for surgeon/physician group, this is the surgeon/physician group ID. |
| BLOCK_KEY | No | For open slot types (0-4) this is the generated block key for the block that occupies the slot. The string consists of a three letter acronym for the block type (SVC for service, SRG for physician, and GRP for surgeon/physician group) and the category ID (if service) or the record ID (if physician or surgeon/physician group). In an IntraConnect setting, the ID will be the Community ID (CID). For unblocked time, this will be "UNBLOCKED."  For closed slot types (101 and 102) this value will be null. |
| TIME_OFF_REASON_C | No | If the slot type is time off (102), this is the time off reason category ID. |
| COMMENTS | No | When the slot type is 0 (unblocked), 1 (service), 2 (provider), 3 (provider/surgeon group) or 102 (time off), this is the comment stored with the slot. When the slot type is 101 (on hold), this is the on hold comments stored with the slot. |
| DEPLOYMENT_ID | No | The unique ID of the deployment that schedule template information was taken from. |
| RESPONSIBLE_PROV_ID | No | The surgeon/physician responsible for the block, if any. |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| B-TREE INDEX | EIX_OR_TEMPLATE_DOW_START_END | ROOM_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_OR_TEMPLATE_DOW_START_END | DAY_OF_THE_WEEK_C | 2 | Yes | Yes |  |
| B-TREE INDEX | EIX_OR_TEMPLATE_DOW_START_END | PATTERN_START_DATE | 3 | Yes | Yes |  |
| B-TREE INDEX | EIX_OR_TEMPLATE_DOW_START_END | PATTERN_END_DATE | 4 | Yes | Yes |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ROOM_ID | CLARITY_SER | PROV_ID | Unknown | Yes | No |  |
| 1 | ROOM_ID | CLARITY_SER_2 | PROV_ID | Unknown | Yes | No |  |
| 1 | ROOM_ID | CLARITY_SER_3 | PROV_ID | Unknown | Yes | No |  |
| 1 | ROOM_ID | CLARITY_SER_4 | PROV_ID | No | Yes | No |  |
| 1 | ROOM_ID | CLARITY_SER_MYC | PROV_ID | Unknown | Yes | No |  |
| 1 | ROOM_ID | D_PROV_PRIMARY_HIERARCHY | PROV_ID | Unknown | Unknown | No |  |
| 1 | ROOM_ID | ED_SER_SETTINGS | PROV_ID | Unknown | Yes | No |  |
| 1 | ROOM_ID | EXT_CAL_PROV_CONFIG | PROV_ID | No | Yes | No |  |
| 1 | ROOM_ID | OR_SER_EQUIPMENT | PROV_ID | Unknown | Yes | No |  |
| 1 | ROOM_ID | OR_SER_ROOM | PROV_ID | Unknown | Yes | No |  |
| 1 | ROOM_ID | PROV_BATCH_LTR_GEN | PROV_ID | Unknown | Yes | No |  |
| 1 | ROOM_ID | PROV_GROUP | PROV_ID | No | Yes | No |  |
| 1 | ROOM_ID | V_CUBE_D_PROVIDER | PROVIDER_ID | Unknown | Unknown | No |  |
| 2 | DAY_OF_THE_WEEK_C | ZC_DAY_OF_THE_WEEK | DAY_OF_THE_WEEK_C | No | Yes | No |  |
| 5 | SLOT_TYPE_C | ZC_OR_OLD_BLOCK | OLD_BLOCK_TYPE_C | No | Yes | No |  |
| 9 | SERVICE_C | ZC_OR_SERVICE | SERVICE_C | No | Yes | No |  |
| 10 | SURGEON_ID | CLARITY_SER | PROV_ID | Unknown | Yes | No |  |
| 10 | SURGEON_ID | CLARITY_SER_2 | PROV_ID | Unknown | Yes | No |  |
| 10 | SURGEON_ID | CLARITY_SER_3 | PROV_ID | Unknown | Yes | No |  |
| 10 | SURGEON_ID | CLARITY_SER_4 | PROV_ID | No | Yes | No |  |
| 10 | SURGEON_ID | CLARITY_SER_MYC | PROV_ID | Unknown | Yes | No |  |
| 10 | SURGEON_ID | D_PROV_PRIMARY_HIERARCHY | PROV_ID | Unknown | Unknown | No |  |
| 10 | SURGEON_ID | ED_SER_SETTINGS | PROV_ID | Unknown | Yes | No |  |
| 10 | SURGEON_ID | EXT_CAL_PROV_CONFIG | PROV_ID | No | Yes | No |  |
| 10 | SURGEON_ID | OR_SER_EQUIPMENT | PROV_ID | Unknown | Yes | No |  |
| 10 | SURGEON_ID | OR_SER_ROOM | PROV_ID | Unknown | Yes | No |  |
| 10 | SURGEON_ID | PROV_BATCH_LTR_GEN | PROV_ID | Unknown | Yes | No |  |
| 10 | SURGEON_ID | PROV_GROUP | PROV_ID | No | Yes | No |  |
| 10 | SURGEON_ID | V_CUBE_D_PROVIDER | PROVIDER_ID | Unknown | Unknown | No |  |
| 11 | GROUP_ID | OR_GRP | GROUP_ID | Unknown | Yes | No |  |

_(45 total; showing first 30)_
