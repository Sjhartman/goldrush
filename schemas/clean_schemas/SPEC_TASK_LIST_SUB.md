# SPEC_TASK_LIST_SUB

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=SPEC_TASK_LIST_SUB

## Description

This is sub container information for Anatomic Pathology specimens.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | OVS |
| Release Version | Summer 2009 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| SPECIMEN_ID | VARCHAR (18) | The unique ID of the specimen record |
| GROUP_LINE | No | The line number of the sub container information for anatomic pathology (AP) specimens. Together with SPECIMEN_ID, this forms the foreign key for this table, SPEC_TASK_LIST. |
| VALUE_LINE | No | The line number of specific sub container information for anatomic pathology (AP) specimens associated with the different tasks on the specimen from the SPEC_TASK_LIST table. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| TASK_LINKED_SCTR_ID | VARCHAR (18) | Stores a container designation that may be created in association with a specific container and task, as in a slide for a given block designation with a specific stain. |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | SPECIMEN_ID | AP_SPECIMEN_DESC | SPECIMEN_ID | No | No | No |  |
| 1 | SPECIMEN_ID | EMBRYOLOGY_SPECIMEN | SPECIMEN_ID | No | No | No |  |
| 1 | SPECIMEN_ID | SPEC_DB_MAIN | SPECIMEN_ID | No | No | No |  |
| 1 | SPECIMEN_ID | SPEC_TASK_LIST | SPECIMEN_ID | No | No | No |  |
| 2 | GROUP_LINE | LINE |  |  |  |  |  |
| 4 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 4 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 4 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 5 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 5 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 5 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 6 | TASK_LINKED_SCTR_ID | OVC_DB_MAIN | CONTAINER_ID | No | No | No |  |
