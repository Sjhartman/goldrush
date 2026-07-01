# CLARITY_SER_DEPT

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=CLARITY_SER_DEPT

## Description

The CLARITY_SER_DEPT table contains the departments in which each of your providers will be scheduled. A provider can be scheduled in multiple departments; therefore, the primary key for this table is a combination of provider ID and line number of the department in the provider's record.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | SER |
| Release Version | EPIC 2000 |
| May contain EHI? | No |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| PROV_ID | VARCHAR (18) | The unique ID of the provider record. This ID may be encrypted. |
| LINE | No | The line number of the associated department in the provider's record. |
| DEPARTMENT_ID | NUMERIC (18,0) | The unique ID of the department in which the provider can be scheduled, provided that the provider is active for scheduling in the department (i.e. that INACT_CAD_DEPT_YN is null or 'N'). |
| CM_PHY_OWNER_ID | VARCHAR (25) | ID of the physical deployment owner for this record.  Physical owners will be where the data is hosted, either on the cross-over server or the owner deployment. |
| CM_LOG_OWNER_ID | VARCHAR (25) | ID of the logical deployment owner for this record.  Logical owners show the deployment where the record was created but doesn't represent if the record is a part of version skew. |
| INACT_CAD_DEPT_YN | VARCHAR (1) |  |
| OUTLOOK_DEPT_YN *(deprecated)* | VARCHAR (1) |  |
| SUBGROUP_C *(deprecated)* | INTEGER | This column has been deprecated.  Use column TEAM_SUBGROUP_ID instead, which links to the SUBGROUP table. |
| TEAM_SUBGROUP_ID | NUMERIC (18,0) | The unique ID of the team subgroup for this row. This column is frequently used to link to the SUBGROUP table.  This subgroup will be added to the search provider list in appointment entry when the user selects the provider and clicks on the "Team" button. Note that if the subgroup entered is not used by the associated department, the "Team" button will not be enabled for the provider. |
| DEPT_VT_LMT_DEPT_YN | VARCHAR (1) |  |
| PUBLISH_SLOTS_YN | VARCHAR (1) |  |
| PUBLISH_CLINICIAN_C | INTEGER |  |
| DFLT_ACCT_CLASS_C | INTEGER |  |
| DEFAULT_ARRIVAL_PAT_LOC_ID *(deprecated)* | NUMERIC (18,0) |  |
| REMOVE_UNAVAIL_DAYS | INTEGER | The number of days before a batch job (using template 82) removes the "day unavailable" restriction from a provider's schedule. This numeric value has a default of zero and must be a non-negative integer. |
| EXCLUDE_UTIL_OVERRIDE_C | INTEGER |  |
| TAKE_NEW_PAT_DEPT_YN | VARCHAR (1) |  |
| ACTIVE_UNTIL_DATE | DATETIME | Indicates the date on which the provider will become inactive in this department. |
| PF_SHOW_PROV_DEPT_YN | VARCHAR (1) |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | PROV_ID | CLARITY_SER | PROV_ID | Unknown | No | No |  |
| 1 | PROV_ID | CLARITY_SER_2 | PROV_ID | Unknown | No | No |  |
| 1 | PROV_ID | CLARITY_SER_3 | PROV_ID | Unknown | No | No |  |
| 1 | PROV_ID | CLARITY_SER_4 | PROV_ID | No | No | No |  |
| 1 | PROV_ID | CLARITY_SER_MYC | PROV_ID | Unknown | No | No |  |
| 1 | PROV_ID | D_PROV_PRIMARY_HIERARCHY | PROV_ID | Unknown | Unknown | No |  |
| 1 | PROV_ID | ED_SER_SETTINGS | PROV_ID | Unknown | No | No |  |
| 1 | PROV_ID | EXT_CAL_PROV_CONFIG | PROV_ID | No | No | No |  |
| 1 | PROV_ID | OR_SER_EQUIPMENT | PROV_ID | Unknown | No | No |  |
| 1 | PROV_ID | OR_SER_ROOM | PROV_ID | Unknown | No | No |  |
| 1 | PROV_ID | PROV_BATCH_LTR_GEN | PROV_ID | Unknown | No | No |  |
| 1 | PROV_ID | PROV_GROUP | PROV_ID | No | No | No |  |
| 1 | PROV_ID | V_CUBE_D_PROVIDER | PROVIDER_ID | Unknown | Unknown | No |  |
| 3 | DEPARTMENT_ID | BH_DEP | DEPARTMENT_ID | No | No | No |  |
| 3 | DEPARTMENT_ID | CLARITY_DEP | DEPARTMENT_ID | No | No | No |  |
| 3 | DEPARTMENT_ID | CLARITY_DEP_2 | DEPARTMENT_ID | No | No | No |  |
| 3 | DEPARTMENT_ID | CLARITY_DEP_3 | DEPARTMENT_ID | No | No | No |  |
| 3 | DEPARTMENT_ID | CLARITY_DEP_4 | DEPARTMENT_ID | No | No | No |  |
| 3 | DEPARTMENT_ID | CLARITY_DEP_5 | DEPARTMENT_ID | No | No | No |  |
| 3 | DEPARTMENT_ID | CLARITY_DEP_MYC | DEPARTMENT_ID | No | No | No |  |
| 3 | DEPARTMENT_ID | DEPT_QUEUE_MSG_SETTINGS | DEPARTMENT_ID | No | No | No |  |
| 3 | DEPARTMENT_ID | DEPT_VERIFIED_INFO | DEPARTMENT_ID | No | No | No |  |
| 3 | DEPARTMENT_ID | DEP_BATCH_LTR_GEN | DEPARTMENT_ID | No | No | No |  |
| 3 | DEPARTMENT_ID | DEP_CE_SETTINGS | DEPARTMENT_ID | No | No | No |  |
| 3 | DEPARTMENT_ID | DP_HIDE_SENSITIVE_CONFIG | DEPARTMENT_ID | No | No | No |  |
| 3 | DEPARTMENT_ID | ED_ALRT_DFLT | DEPARTMENT_ID | No | No | No |  |
| 3 | DEPARTMENT_ID | ED_DEP_SETTINGS | DEP_ID | No | No | No |  |
| 3 | DEPARTMENT_ID | EXT_CAL_DEPT_CONFIG | DEPARTMENT_ID | No | No | No |  |
| 3 | DEPARTMENT_ID | VISIT_MODE_CONFIG_DEP | DEPARTMENT_ID | No | No | No |  |
| 3 | DEPARTMENT_ID | V_CUBE_D_DEPARTMENT | DEPARTMENT_ID | Unknown | Unknown | No |  |

_(41 total; showing first 30)_
