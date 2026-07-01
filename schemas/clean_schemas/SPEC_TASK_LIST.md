# SPEC_TASK_LIST

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=SPEC_TASK_LIST

## Description

This table contains task information for Microbiology specimens and Anatomic Pathology cases.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | OVS |
| Release Version | SPRING 2008 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| SPECIMEN_ID | VARCHAR (18) | The unique ID of the specimen record |
| LINE | No | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| TASK_TEST_ID | VARCHAR (18) | The unique identifier of the test that the task on the corresponding line applies to. |
| TASK_C | INTEGER |  |
| TASK_ACTION_C | INTEGER |  |
| TASK_PARAMS | VARCHAR (254) | Stores the parameters for the action associated with task on the corresponding line. For instance, this column may store the media type of the created container. |
| TASK_INSTANT | DATETIME (Local) | The instant when the task was completed. |
| TASK_PERSON_ID | VARCHAR (18) | The unique employee identifier of the person completing the task. |
| TASK_SYS_GEN_YN | VARCHAR (1) |  |
| TASK_LAB_ID | VARCHAR (18) | The unique identifier of the lab in which the task was completed. |
| TASK_INST | 51318 | The user-editable instant when the task was completed. |
| TASK_LINKED_CTNR_ID | VARCHAR (18) | The unique container identifier that might be created if the action associated with the task on the corresponding line is to create a media plate, a block or a slide that is related to a block. |
| TASK_GROUP | VARCHAR (254) | This item is used to group tasks together. This feature is most commonly used to link multiple slides to a block. |
| TASK_ACTION_QTY | INTEGER | Stores the number of times the action associated with this task must be performed. |
| TASK_CHARGE_ID | NUMERIC (18,0) | Stores a charge associated with this task. |
| TASK_CHARGE_QTY | INTEGER | Stores the number of times the billing code associated with this task must be charged. |
| TASK_INT_LAB_ID | VARCHAR (18) | Used to indicate the lab tasks must be performed in. If a lab is listed in this item, the task will be added to the specimen only when the specimen (any container or test on the specimen) is received in the listed lab for the first time. |
| TASK_LEVEL | INTEGER | Stores number of levels. |
| TASK_BLOCK_START_TM | DATETIME (Local) | Stores the block fixation start time. |
| TASK_BLOCK_END_TM | DATETIME (Local) | Stores the block fixation end time. |
| TASK_NOTES | VARCHAR (254) | Stores any free text notes describing the task. |
| TASK_DELETED_YN | VARCHAR (1) |  |
| TASK_AP_PART_ID | VARCHAR (254) | Returns the part ID for this anatomic pathology task, such as "A1". |
| TASK_PROTOCOL_ID | VARCHAR (18) | The unique identifier of the test which populated the associated task. |
| TASK_COMP_UTC_DTTM | 51336 | The instant that the user indicated the task was completed in UTC. |
| TASK_ORD_DTTM | DATETIME (UTC) | The instant that the user added or restored the task in UTC. |
| TASK_ORD_USER_ID | VARCHAR (18) | The unique employee ID of the person adding or restoring the task. |
| TASK_CHG_TR_STAT_C | INTEGER |  |
| TASK_UPD_LINE | INTEGER | The line in the tasks related table (SI 51310) that the current line is created to restore for when task was updated. |
| TASK_UPD_ALERT_ID | NUMERIC (18,0) | The unique alert record identifier created when the task was updated. |
| TEST_LINE | INTEGER | The line number of the associated test on the specimen. Together with SPECIMEN_ID, this forms the foreign key to the SPEC_TEST_REL table. |
| CHARGE_SS_PROC_ID | NUMERIC (18,0) | The unique ID of the last dropped charge for the associated specimen task. |
| CHARGE_QTY_SS | INTEGER | The quantity for the last dropped charge for the associated specimen task. |
| TASK_REFL_ORDER_ID | NUMERIC (18,0) | The unique ID of the order to use when this task is completed rather than reflexing a new one. |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | SPECIMEN_ID | AP_SPECIMEN_DESC | SPECIMEN_ID | No | No | No |  |
| 1 | SPECIMEN_ID | EMBRYOLOGY_SPECIMEN | SPECIMEN_ID | No | No | No |  |
| 1 | SPECIMEN_ID | SPEC_DB_MAIN | SPECIMEN_ID | No | No | No |  |
| 3 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 4 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 4 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 4 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 5 | TASK_TEST_ID | PROTOCOL_DB_MAIN | PROTOCOL_ID | Unknown | No | No |  |
| 5 | TASK_TEST_ID | TEST_MSTR_DB_MAIN | TEST_ID | Unknown | No | No |  |
| 5 | TASK_TEST_ID | ZC_QC_TEST_CAT_ID | QC_TEST_CAT_ID_C | Unknown | Unknown | No |  |
| 6 | TASK_C | ZC_TASK | TASK_C | No | No | No |  |
| 7 | TASK_ACTION_C | ZC_TASK_ACTION | TASK_ACTION_C | No | No | No |  |
| 10 | TASK_PERSON_ID | CLARITY_EMP | USER_ID | Unknown | No | No |  |
| 10 | TASK_PERSON_ID | CLARITY_EMP_2 | USER_ID | Unknown | No | No |  |
| 10 | TASK_PERSON_ID | CLARITY_EMP_3 | USER_ID | Unknown | No | No |  |
| 10 | TASK_PERSON_ID | CLARITY_EMP_4 | USER_ID | No | No | No |  |
| 10 | TASK_PERSON_ID | CLARITY_EMP_DEMO | USER_ID | No | No | No |  |
| 10 | TASK_PERSON_ID | EMP_BASIC_INFO | USER_ID | No | No | No |  |
| 10 | TASK_PERSON_ID | EMP_DOC_SETTINGS | USER_NUMBER_ID | No | No | No |  |
| 10 | TASK_PERSON_ID | F_RX_USER | USER_ID | Unknown | Unknown | No |  |
| 10 | TASK_PERSON_ID | IB_MESSAGE_SETTINGS | USER_ID | No | No | No |  |
| 10 | TASK_PERSON_ID | LOGIN_INFO | USER_NUMBER_ID | No | No | No |  |
| 10 | TASK_PERSON_ID | QC_RESULTS_REVIEW | USER_NUMBER_ID | No | No | No |  |
| 10 | TASK_PERSON_ID | USER_SIDEBAR_RPT | USER_NUMBER_ID | Unknown | No | No |  |
| 10 | TASK_PERSON_ID | V_CUBE_D_USER | USER_ID | Unknown | Unknown | No |  |
| 10 | TASK_PERSON_ID | V_CUBE_RX_USER | USER_ID | Unknown | Unknown | No |  |
| 12 | TASK_LAB_ID | AP_CASE_TYPES | LAB_ID | Unknown | No | No |  |
| 12 | TASK_LAB_ID | LAB_AP_LAB_SETUP | LAB_ID | Unknown | No | No |  |

_(153 total; showing first 30)_
