# TPL_CYCLES

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=TPL_CYCLES

## Description

The cycle information for the treatment plan.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | TPL |
| Release Version | SPRING 2008 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| TREATMENT_PLAN_ID | NUMERIC (18,0) | The treatment plan ID. |
| LINE | No | The line number that corresponds to each cycle in the treatment plan in this row. |
| CM_PHY_OWNER_ID | VARCHAR (25) | ID of the physical deployment owner for this record.  Physical owners will be where the data is hosted, either on the cross-over server or the owner deployment. |
| CM_LOG_OWNER_ID | VARCHAR (25) | ID of the logical deployment owner for this record.  Logical owners show the deployment where the record was created but doesn't represent if the record is a part of version skew. |
| CYCLE_ID | VARCHAR (100) | The treatment plan level ID for the cycle in this row. |
| CYCLE_NAME | VARCHAR (254) | The cycle name of the cycle in this row. |
| CYCLE_STATUS_C | INTEGER |  |
| CYCLE_START_DATE | DATETIME | The start date of the cycle in this row, in calendar format. |
| CYCLE_WAIT_AFTER | NUMERIC (18,0) | The number of days to wait after the cycle in this row. |
| CYCLE_MAX_LEAD | NUMERIC (18,0) | The max lead for the cycle in this row. |
| CYCLE_MAX_LAG | NUMERIC (18,0) | The max lag for the cycle in this row. |
| ANCHOR_DAY | NUMERIC (18,0) | The treatment plan level ID of the anchor day for the cycle in this row. |
| CYCLE_CREATED_BY_ID | VARCHAR (18) | The user ID of the person who created the cycle in this row. |
| CYCLE_CREATED_ON_TM | DATETIME (Local) | The date and time of creation in external format for the cycle in this row. |
| CYCLE_COMMENT | VARCHAR (254) | The cycle creation comment for the cycle in this row. |
| CYCLE_NUM | INTEGER | The cycle number of this cycle for this treatment plan. |
| CYC_STAT_CHG_USR_ID | VARCHAR (18) | Stores the user who changed the cycle status. |
| CYC_STAT_CHG_DTTM | DATETIME (Local) | Stores the instant at which the cycle status changed. |
| CYC_STAT_CHG_COMM | VARCHAR (254) | Stores comment entered by user when changing the status. |
| CYC_SOURCE_UID | VARCHAR (100) | Stores the unique ID of the cycle from which it was created. |
| PRL_CYCLE_SRC_ID | VARCHAR (25) | If this treatment plan cycle was created from a protocol, this item will be set to the Cycle ID (I PRL 200) that created this treatment plan cycle. This column will match the CL_PRL_CYCLES__PRL_CYCLE_ID column. |
| CONVERSION_CYC_SRC | INTEGER | If this cycle is created for conversion, this will be the line number in SI TPL 1000 of the source cycle. |
| CONVERSION_CYC_TRGT | INTEGER | If this cycle was replaced by another cycle when conversion is accepted or discarded, this will be the line of the cycle that replaced it (SI TPL 1000). |
| CYCLE_PATTERN_SOURCE_LINE | INTEGER | For this cycle, if it was created from a pattern cycle, this item will store the source line in SI TPL 12000 it was created from. |
| CYCLE_CREATION_METHOD_C | INTEGER |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | TREATMENT_PLAN_ID | DENT_TREATMENT | TREATMENT_ID | No | No | No |  |
| 1 | TREATMENT_PLAN_ID | TPL_HSB_EPT_LINK | TREATMENT_PLAN_ID | Unknown | No | No |  |
| 1 | TREATMENT_PLAN_ID | TPL_INFO | TREATMENT_PLAN_ID | No | No | No |  |
| 3 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 4 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 4 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 4 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 7 | CYCLE_STATUS_C | ZC_CYCLE_STATUS | CYCLE_STATUS_C | No | No | No |  |
| 13 | CYCLE_CREATED_BY_ID | CLARITY_EMP | USER_ID | Unknown | No | No |  |
| 13 | CYCLE_CREATED_BY_ID | CLARITY_EMP_2 | USER_ID | Unknown | No | No |  |
| 13 | CYCLE_CREATED_BY_ID | CLARITY_EMP_3 | USER_ID | Unknown | No | No |  |
| 13 | CYCLE_CREATED_BY_ID | CLARITY_EMP_4 | USER_ID | No | No | No |  |
| 13 | CYCLE_CREATED_BY_ID | CLARITY_EMP_DEMO | USER_ID | No | No | No |  |
| 13 | CYCLE_CREATED_BY_ID | EMP_BASIC_INFO | USER_ID | No | No | No |  |
| 13 | CYCLE_CREATED_BY_ID | EMP_DOC_SETTINGS | USER_NUMBER_ID | No | No | No |  |
| 13 | CYCLE_CREATED_BY_ID | F_RX_USER | USER_ID | Unknown | Unknown | No |  |
| 13 | CYCLE_CREATED_BY_ID | IB_MESSAGE_SETTINGS | USER_ID | No | No | No |  |
| 13 | CYCLE_CREATED_BY_ID | LOGIN_INFO | USER_NUMBER_ID | No | No | No |  |
| 13 | CYCLE_CREATED_BY_ID | QC_RESULTS_REVIEW | USER_NUMBER_ID | No | No | No |  |
| 13 | CYCLE_CREATED_BY_ID | USER_SIDEBAR_RPT | USER_NUMBER_ID | Unknown | No | No |  |
| 13 | CYCLE_CREATED_BY_ID | V_CUBE_D_USER | USER_ID | Unknown | Unknown | No |  |
| 13 | CYCLE_CREATED_BY_ID | V_CUBE_RX_USER | USER_ID | Unknown | Unknown | No |  |
| 17 | CYC_STAT_CHG_USR_ID | CLARITY_EMP | USER_ID | Unknown | No | No |  |
| 17 | CYC_STAT_CHG_USR_ID | CLARITY_EMP_2 | USER_ID | Unknown | No | No |  |
| 17 | CYC_STAT_CHG_USR_ID | CLARITY_EMP_3 | USER_ID | Unknown | No | No |  |
| 17 | CYC_STAT_CHG_USR_ID | CLARITY_EMP_4 | USER_ID | No | No | No |  |
| 17 | CYC_STAT_CHG_USR_ID | CLARITY_EMP_DEMO | USER_ID | No | No | No |  |
| 17 | CYC_STAT_CHG_USR_ID | EMP_BASIC_INFO | USER_ID | No | No | No |  |

_(39 total; showing first 30)_
