# V_CUBE_D_DEP_LOC

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=V_CUBE_D_DEP_LOC

## Description

This view contains data from the CLARITY_DEP and CLARITY_POS table, optimized for use in SSAS Cubes. This data contains basic information about a department, and links it to its corresponding location.

## Metadata

| Property | Value |
| --- | --- |
| Type | View |
| Release Version | Rel 2015 |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| DEPARTMENT_ID | NUMERIC (18,0) | This column contains the unique ID number assigned to the department record. |
| DEPARTMENT_NAME | VARCHAR (254) | This column contains the name of the department. |
| DEPARTMENT_DISPLAY_NAME | VARCHAR (254) | This column contains the name of the department along with it's ID. The format is "DEPARTMENT_NAME [DEPARTMENT_ID]". |
| DEPARTMENT_SPECIALTY | No | This column contains the name of the medical specialty practiced in this department. |
| LOCATION_ID | NUMERIC (18,0) | This column contains just the ID of the Location. |
| LOCATION_NAME | VARCHAR (200) | This column contains just the name of the Location. |
| LOCATION_DISPLAY_NAME | .2 | This column contains the name of the Location with its ID. The format is "LOCATION_NAME [LOCATION_ID]". |
| LOCATION_TYPE | No | This column contains the type of location (i.e. facility, location, place of service, etc.) |
| POS_TYPE | No | This column contains the place of service's type. |
| SERVICE_AREA_ID | NUMERIC (18,0) | This column contains the unique ID for the service area to which this location is assigned. If this record's LOCATION_TYPE is Service Area, then this value will be the same as LOCATION_ID. |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | DEPARTMENT_ID | BH_DEP | DEPARTMENT_ID | No | Unknown | No |  |
| 1 | DEPARTMENT_ID | CLARITY_DEP | DEPARTMENT_ID | No | Unknown | No |  |
| 1 | DEPARTMENT_ID | CLARITY_DEP_2 | DEPARTMENT_ID | No | Unknown | No |  |
| 1 | DEPARTMENT_ID | CLARITY_DEP_3 | DEPARTMENT_ID | No | Unknown | No |  |
| 1 | DEPARTMENT_ID | CLARITY_DEP_4 | DEPARTMENT_ID | No | Unknown | No |  |
| 1 | DEPARTMENT_ID | CLARITY_DEP_5 | DEPARTMENT_ID | No | Unknown | No |  |
| 1 | DEPARTMENT_ID | CLARITY_DEP_MYC | DEPARTMENT_ID | No | Unknown | No |  |
| 1 | DEPARTMENT_ID | DEPT_QUEUE_MSG_SETTINGS | DEPARTMENT_ID | No | Unknown | No |  |
| 1 | DEPARTMENT_ID | DEPT_VERIFIED_INFO | DEPARTMENT_ID | No | Unknown | No |  |
| 1 | DEPARTMENT_ID | DEP_BATCH_LTR_GEN | DEPARTMENT_ID | No | Unknown | No |  |
| 1 | DEPARTMENT_ID | DEP_CE_SETTINGS | DEPARTMENT_ID | No | Unknown | No |  |
| 1 | DEPARTMENT_ID | DP_HIDE_SENSITIVE_CONFIG | DEPARTMENT_ID | No | Unknown | No |  |
| 1 | DEPARTMENT_ID | ED_ALRT_DFLT | DEPARTMENT_ID | No | Unknown | No |  |
| 1 | DEPARTMENT_ID | ED_DEP_SETTINGS | DEP_ID | No | Unknown | No |  |
| 1 | DEPARTMENT_ID | EXT_CAL_DEPT_CONFIG | DEPARTMENT_ID | No | Unknown | No |  |
| 1 | DEPARTMENT_ID | VISIT_MODE_CONFIG_DEP | DEPARTMENT_ID | No | Unknown | No |  |
| 1 | DEPARTMENT_ID | V_CUBE_D_DEPARTMENT | DEPARTMENT_ID | Unknown | Unknown | No |  |
| 5 | LOCATION_ID | ANALYTICS_SYSTEM_SETTINGS | FACILITY_ID | No | Unknown | No |  |
| 5 | LOCATION_ID | ARPB_SA_SETTINGS | FACILITY_ID | No | Unknown | No |  |
| 5 | LOCATION_ID | CLARITY_LOC | LOC_ID | Unknown | Unknown | No |  |
| 5 | LOCATION_ID | CLARITY_LOC_2 | LOC_ID | Unknown | Unknown | No |  |
| 5 | LOCATION_ID | CLARITY_POS | POS_ID | No | Unknown | No |  |
| 5 | LOCATION_ID | CLARITY_POS_2 | POS_ID | No | Unknown | No |  |
| 5 | LOCATION_ID | CLARITY_SA | SERV_AREA_ID | Unknown | Unknown | No |  |
| 5 | LOCATION_ID | CL_LOC_HIERARCHY | LOC_ID | Unknown | Unknown | No |  |
| 5 | LOCATION_ID | CV_PCI_D2B_SETTINGS | FACILITY_ID | No | Unknown | No |  |
| 5 | LOCATION_ID | EAF_CLM_ALTADR_INF | FACILITY_ID | No | Unknown | No |  |
| 5 | LOCATION_ID | EAF_CLM_RMT_SETUP | FACILITY_ID | No | Unknown | No |  |
| 5 | LOCATION_ID | EAF_EXP_APPT_LOG | FACILITY_ID | No | Unknown | No |  |
| 5 | LOCATION_ID | EAF_SEARCH_TERMS | FACILITY_ID | No | Unknown | No |  |

_(77 total; showing first 30)_
