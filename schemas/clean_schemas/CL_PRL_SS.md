# CL_PRL_SS

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=CL_PRL_SS

## Description

This table contains the SmartSet/Protocol/Pathway settings that do not change per contact for each SmartSet, Protocol, Pathway, or Dental Template.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | PRL |
| Release Version | SPRING 2007 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| PROTOCOL_ID | NUMERIC (18,0) | SmartSet/Protocol ID. |
| CM_PHY_OWNER_ID | VARCHAR (25) | ID of the physical deployment owner for this record.  Physical owners will be where the data is hosted, either on the cross-over server or the owner deployment. |
| CM_LOG_OWNER_ID | VARCHAR (25) | ID of the logical deployment owner for this record.  Logical owners show the deployment where the record was created but doesn't represent if the record is a part of version skew. |
| PROTOCOL_NAME | VARCHAR (200) | The SmartSet/Protocol record name.  This is different from the display name, which is stored in CL_PRL_SS_OT.DISPLAY_NAME. |
| RECORD_STATUS_2_C | INTEGER |  |
| SS_TYPE_C | INTEGER |  |
| PRL_STATUS_C | INTEGER |  |
| PROTOCOL_TYPE_C_ID | NUMERIC (18,0) | The primary episode type for this protocol. |
| PRL_RECORD_TYPE_C | INTEGER |  |
| RELEASED_CONTACT | FLOAT | Stores the current active released contact |
| TEST_TO_REL_CONTACT | FLOAT | Current active test released contact |
| ACCESS_LOGGING_YN | VARCHAR (1) |  |
| DENTAL_TREAT_NAME | VARCHAR (200) | This is the name of the dental treatment that is generated from this template. |
| DENT_TREAT_T_TYPE_C | INTEGER |  |
| DENT_PARENT_PRL_ID | NUMERIC (18,0) | This is the dental treatment template that this visit template belongs to. |
| DENT_VISIT_SPACING | INTEGER | This determines spacing in days between dental visits for treatments created from this template. |
| DENT_VISIT_LENGTH | INTEGER | This determines visit length in minutes for dental treatments created from this template. |
| DENTAL_SCHED_INST | VARCHAR (254) | This determines visit scheduling instructions for dental treatments created from this template. |
| DENT_VISIT_NUM | INTEGER | This determines the order of this visit in the treatment created from the dental template. |
| BLANK_TEMPLATE_YN | VARCHAR (1) |  |
| DENT_VISIT_NAME | VARCHAR (200) | Stores the visit name for a visit in a dental treatment template. |
| AUTO_DC_ENABLE_YN | VARCHAR (1) |  |
| AUTO_DC_INACTIVITY_THRESHOLD | INTEGER | The number of days of inactivity that must elapse before plans created from this protocol are considered inactive. |
| ALLOW_AUTO_DC_NO_REMAIN_TRT_YN | VARCHAR (1) |  |
| CREATED_BY_CRPC_INTERF_YN | VARCHAR (1) |  |
| ALLOW_SIGN_CYCLES_YN | VARCHAR (1) | Surrogate key used to uniquely identify rows in this (and only this) table on Cogito Cloud only, do not assume the surrogate key in this table will correspond to the surrogate key in another table |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 2 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 2 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 3 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 5 | RECORD_STATUS_2_C | ZC_RECORD_STATUS_2 | RECORD_STATUS_2_C | No | No | No |  |
| 5 | RECORD_STATUS_2_C | ZC_RECORD_STS | RECORD_STS_C | No | No | No |  |
| 6 | SS_TYPE_C | ZC_SS_TYPE | SS_TYPE_C | No | No | No |  |
| 7 | PRL_STATUS_C | ZC_OSQ_STATUS | OSQ_STATUS_C | No | No | No |  |
| 8 | PROTOCOL_TYPE_C_ID | EPISODE_DEF | EPISODE_DEF_ID | No | No | No |  |
| 9 | PRL_RECORD_TYPE_C | ZC_PRL_RECORD_TYPE | PRL_RECORD_TYPE_C | No | No | No |  |
| 14 | DENT_TREAT_T_TYPE_C | ZC_DENTAL_TYPE | DENTAL_TYPE_C | No | No | No |  |
| 15 | DENT_PARENT_PRL_ID | CL_PRL_SS | PROTOCOL_ID | No | No | No |  |
