# OR_IMP_IMPLANT

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=OR_IMP_IMPLANT

## Description

The OR_IMP_IMPLANT table contains implantation information for implants that were marked as being implanted for a surgery or invasive procedure .

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | IMP |
| Release Version | MU6 - MAY 2001 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| IMPLANT_ID | VARCHAR (18) | The unique ID of the implant record. |
| LINE | No | The number of the line of the implant information for the implant. |
| IMPLANTED_DATE | DATETIME | The date the implant was implanted. |
| IMPLANT_LOG_ID | VARCHAR (18) | The unique ID of the log in which the implant was implanted. |
| MANUF_NOTIFY_DATE | DATETIME | The date the manufacturer was notified of the implantation of the implant. |
| CM_PHY_OWNER_ID | VARCHAR (25) | ID of the physical deployment owner for this record.  Physical owners will be where the data is hosted, either on the cross-over server or the owner deployment. |
| CM_LOG_OWNER_ID | VARCHAR (25) | ID of the logical deployment owner for this record.  Logical owners show the deployment where the record was created but doesn't represent if the record is a part of version skew. |
| IMPLANTED_TIME | DATETIME (Local) | The time when the listed implant was marked as implanted. |
| IMP_STAFF_ID | VARCHAR (18) | The unique ID of the physician who implanted the listed implant. |
| NUM_IMPLANTED | INTEGER | The number of items implanted. |
| IMPLANT_LOG_REF_IDENT | VARCHAR (174) | This item stores the reference ID of the implant surgical log used to generate this data. |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| B-TREE INDEX | EIX_OR_IMP_IMPLANT_IMLOID | IMPLANT_LOG_ID | 1 | Yes | Yes |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | IMPLANT_ID | IMP_STENT_DIMENSIONS | IMPLANT_ID | No | No | No |  |
| 1 | IMPLANT_ID | OR_IMP | IMPLANT_ID | Unknown | No | No |  |
| 1 | IMPLANT_ID | OR_IMP_2 | IMPLANT_ID | Unknown | No | No |  |
| 1 | IMPLANT_ID | OR_IMP_3 | IMPLANT_ID | No | No | No |  |
| 1 | IMPLANT_ID | OR_IMP_SKNSUB | IMPLANT_ID | No | No | No |  |
| 1 | IMPLANT_ID | UK_CRM_LEAD_PLACMNT | IMPLANT_ID | No | No | No |  |
| 1 | IMPLANT_ID | V_CUBE_D_IMPLANT | IMPLANT_ID | Unknown | Unknown | No |  |
| 4 | IMPLANT_LOG_ID | F_LOG_BASED | LOG_ID | Unknown | Unknown | No |  |
| 4 | IMPLANT_LOG_ID | OR_LOG_2 | LOG_ID | Unknown | No | No |  |
| 4 | IMPLANT_LOG_ID | OR_LOG_3 | LOG_ID | No | No | No |  |
| 4 | IMPLANT_LOG_ID | OR_LOG_METRIC_DETAILS | LOG_ID | No | No | No |  |
| 4 | IMPLANT_LOG_ID | OR_LOG_PRECEDING | LOG_ID | No | No | No |  |
| 4 | IMPLANT_LOG_ID | OR_LOG_VIRTUAL | LOG_ID | No | No | No |  |
| 4 | IMPLANT_LOG_ID | UK_CRM_PACEMKR_PROC | LOG_ID | No | No | No |  |
| 4 | IMPLANT_LOG_ID | V_CASE_CHARGES | LOG_ID | Unknown | Unknown | No |  |
| 4 | IMPLANT_LOG_ID | V_CASE_COSTS | LOG_ID | Unknown | Unknown | No |  |
| 4 | IMPLANT_LOG_ID | V_CASE_ON_TIME_START | LOG_ID | Unknown | Unknown | No |  |
| 4 | IMPLANT_LOG_ID | V_CASE_PHYS_TURNOVER | LOG_ID | Unknown | Unknown | No |  |
| 4 | IMPLANT_LOG_ID | V_CASE_ROOM_TURNOVER | LOG_ID | Unknown | Unknown | No |  |
| 4 | IMPLANT_LOG_ID | V_CASE_VOLUME | LOG_ID | Unknown | Unknown | No |  |
| 4 | IMPLANT_LOG_ID | V_DECISION_TO_INCISION | LOG_ID | Unknown | Unknown | No |  |
| 4 | IMPLANT_LOG_ID | V_LOG_BASED | LOG_ID | Unknown | Unknown | No |  |
| 4 | IMPLANT_LOG_ID | V_LOG_TIMING_EVENTS | LOG_ID | Unknown | Unknown | No |  |
| 6 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 6 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 6 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 7 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 7 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 7 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 9 | IMP_STAFF_ID | CLARITY_SER | PROV_ID | Unknown | No | No |  |

_(42 total; showing first 30)_
