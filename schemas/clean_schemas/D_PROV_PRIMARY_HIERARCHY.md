# D_PROV_PRIMARY_HIERARCHY

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=D_PROV_PRIMARY_HIERARCHY

## Description

This table gives provider-level information for use in reports. It includes, among other details, the provider's primary department, as well as that department's location and service area. It also calculates "name with id" columns for provider, department, location, and service area. Consider using this table when reporting on provider-level information. It is intended to improve performance and maintainability.

## Metadata

| Property | Value |
| --- | --- |
| Type | Derived Table |
| Load Frequency | INCREMENTAL |
| Release Version | Rel 2015 |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| PROV_ID | VARCHAR (18) | The unique ID assigned to the provider record. This ID can be encrypted. |
| PROV_NAME | VARCHAR (200) | The name of the service provider.   Will display "*Unnamed Provider" if no PROV_NAME is found in CLARITY_SER. |
| PROV_NM_WID | No | Provider name and id (e.g. "SMITH, JOHN [1001001]").  Will display "*Unnamed Provider [PROV_ID]" when PROV_NAME is NULL. |
| PROV_NM_CRED | No | Provider name and credentials (e.g. SMITH, JOHN, MD).  If no credentials are found, will be identical to PROV_NAME.  Otherwise, will be identical to PROV_NAME with credentials appended. |
| PROV_NM_CRED_WID | No | Provider name, credentials, and ID (e.g. "SMITH, JOHN, MD [1001001]").  Identical to PROV_NM_CRED, but with [PROV_ID] appended. |
| DEPARTMENT_ID | NUMERIC (18,0) | The unique ID of the department in which the provider can be scheduled, provided that the provider is active for scheduling in the department (i.e. that INACT_CAD_DEPT_YN is null or 'N'). |
| DEPARTMENT_NAME | VARCHAR (254) | The name of the department.  Will display "*Unspecified Department" when CLARITY_SER_DEP.DEPARTMENT_ID is NULL.  Otherwise, will display "*Unknown Department" when CLARITY_DEP.DEPARTMENT_ID is NULL.  Otherwise, will display "*Unnamed Department" when CLARITY_DEP.DEPARTMENT_NAME is NULL. |
| DEPARTMENT_NM_WID | No | Department name and id (e.g. "Family Clinic [1001001]").  Will display "*Unspecified Department" when CLARITY_SER_DEP.DEPARTMENT_ID is NULL.  Otherwise, identical to DEPARTMENT_NAME, but with [DEPARTMENT_ID] appended. |
| LOC_ID | NUMERIC (18,0) | The unique ID of the revenue location to which the department is linked. |
| LOC_NAME | VARCHAR (200) | The name of the revenue location.  Will display "*Unspecified Location" when CLARITY_DEP.REVENUE_LOCATION is NULL.  Otherwise, will display "*Unknown Location" when CLARITY_LOC.LOC_ID is NULL.  Otherwise, will display "*Unnamed Location" when CLARITY_LOC.LOC_NAME is NULL. |
| LOC_NM_WID | No | Location name and id (e.g. "Epic Model Location [1001001]").  Will display "*Unspecified Location" when CLARITY_DEP.REV_LOC_ID is NULL.  Otherwise, identical to LOC_NAME, but with [LOC_ID] appended. |
| SERV_AREA_ID | No | The unique ID of the service area in which this department is located. This is the service area for the department, calculated by the function EPIC_DEPTOSA; this function is needed because the service area is linked to the location record and not to the department record directly. |
| SERV_AREA_NAME | VARCHAR (200) | The name of the service area.  Will display "*Unspecified Service Area" when CLARITY_DEP.SERV_AREA_ID is NULL.  Otherwise, will display "*Unknown Service Area" when CLARITY_SA.SERV_AREA_ID is NULL.  Otherwise, will display "*Unnamed Service Area" when CLARITY_SA.SERV_AREA_NAME is NULL. |
| SERV_AREA_NM_WID | No | Service area and id (e.g. "Epic Model Service Area [1001001]").  Will display "*Unspecified Service Area" when CLARITY_DEP.SERV_AREA_ID is NULL.  Otherwise, identical to SERV_AREA_NAME, but with [SERV_AREA_ID] appended. |
| CREDENTIALS | No | Abbreviation of provider credentials (e.g. "MD"). |
| NPI | VARCHAR (10) | The provider's National Provider Identifier (NPI). This is a 10 digit numeric identifier issued to providers by the Centers for Medicare and Medicaid Services. |
| EPICCARE_PROV_YN | VARCHAR (1) |  |
| SPECIALTY_C | VARCHAR (66) |  |
| SPECIALTY_NAME | No | The provider's primary specialty.  Will display "*Unspecified Specialty" when CLARITY_SER_SPEC.SPECIALTY_C is NULL.  Otherwise, will display "*Unknown Specialty [CLARITY_SER_SPEC.SPECIALTY_C]" when ZC_SPECIALTY.SPECIALTY_C is NULL.  Otherwise, will display "*Unnamed Specialty [ZC_SPECIALTY_C.SPECIALTY_C]" when ZC_SPECIALTY.TITLE is NULL. |
| INTERNAL_ADDRESS_YN | VARCHAR (1) |  |
| EXTERNAL_NAME | VARCHAR (80) | The external name of the provider record. |
| ACTIVE_STATUS_C | INTEGER |  |
| ACTIVE_STATUS | No | The provider's active status.  Will display "*Unspecified Active Status" when CLARITY_SER.ACTIVE_STATUS_C is NULL.  Otherwise, will display "*Unknown Active Status [CLARITY_SER.ACTIVE_STATUS_C]" when ZC_ACTIVE_STATUS_2.ACTIVE_STATUS_2_C is NULL.  Otherwise, will display "*Unnamed Active Status [ZC_ACTIVE_STATUS_2.ACTIVE_STATUS_2_C]" when ZC_ACTIVE_STATUS_2.TITLE is NULL. |
| PROVIDER_TYPE_C | VARCHAR (66) |  |
| PROVIDER_TYPE | No | The provider's type.  Will display "*Unspecified Provider Type" when CLARITY_SER.PROVIDER_TYPE_C is NULL.  Otherwise, will display "*Unknown Provider Type [CLARITY_SER.PROVIDER_TYPE_C]" when ZC_NOTE_SER.SERVICE_TYPE_C is NULL.  Otherwise, will display "*Unnamed Provider Type [ZC_NOTE_SER.SERVICE_TYPE_C]" when ZC_NOTE_SER.TITLE is NULL. |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| B-TREE INDEX | EIX_PROV_HIERARCHY__DID | DEPARTMENT_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_PROV_HIERARCHY__LID | LOC_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_PROV_HIERARCHY__SID | SERV_AREA_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_PROV_HIERARCHY__SPEC | SPECIALTY_C | 1 | Yes | Yes |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | PROV_ID | CLARITY_SER | PROV_ID | Unknown | Unknown | No |  |
| 1 | PROV_ID | CLARITY_SER_2 | PROV_ID | Unknown | Unknown | No |  |
| 1 | PROV_ID | CLARITY_SER_3 | PROV_ID | Unknown | Unknown | No |  |
| 1 | PROV_ID | CLARITY_SER_4 | PROV_ID | No | Unknown | No |  |
| 1 | PROV_ID | CLARITY_SER_MYC | PROV_ID | Unknown | Unknown | No |  |
| 1 | PROV_ID | ED_SER_SETTINGS | PROV_ID | Unknown | Unknown | No |  |
| 1 | PROV_ID | EXT_CAL_PROV_CONFIG | PROV_ID | No | Unknown | No |  |
| 1 | PROV_ID | OR_SER_EQUIPMENT | PROV_ID | Unknown | Unknown | No |  |
| 1 | PROV_ID | OR_SER_ROOM | PROV_ID | Unknown | Unknown | No |  |
| 1 | PROV_ID | PROV_BATCH_LTR_GEN | PROV_ID | Unknown | Unknown | No |  |
| 1 | PROV_ID | PROV_GROUP | PROV_ID | No | Unknown | No |  |
| 1 | PROV_ID | V_CUBE_D_PROVIDER | PROVIDER_ID | Unknown | Unknown | No |  |
| 6 | DEPARTMENT_ID | BH_DEP | DEPARTMENT_ID | No | Unknown | No |  |
| 6 | DEPARTMENT_ID | CLARITY_DEP | DEPARTMENT_ID | No | Unknown | No |  |
| 6 | DEPARTMENT_ID | CLARITY_DEP_2 | DEPARTMENT_ID | No | Unknown | No |  |
| 6 | DEPARTMENT_ID | CLARITY_DEP_3 | DEPARTMENT_ID | No | Unknown | No |  |
| 6 | DEPARTMENT_ID | CLARITY_DEP_4 | DEPARTMENT_ID | No | Unknown | No |  |
| 6 | DEPARTMENT_ID | CLARITY_DEP_5 | DEPARTMENT_ID | No | Unknown | No |  |
| 6 | DEPARTMENT_ID | CLARITY_DEP_MYC | DEPARTMENT_ID | No | Unknown | No |  |
| 6 | DEPARTMENT_ID | DEPT_QUEUE_MSG_SETTINGS | DEPARTMENT_ID | No | Unknown | No |  |
| 6 | DEPARTMENT_ID | DEPT_VERIFIED_INFO | DEPARTMENT_ID | No | Unknown | No |  |
| 6 | DEPARTMENT_ID | DEP_BATCH_LTR_GEN | DEPARTMENT_ID | No | Unknown | No |  |
| 6 | DEPARTMENT_ID | DEP_CE_SETTINGS | DEPARTMENT_ID | No | Unknown | No |  |
| 6 | DEPARTMENT_ID | DP_HIDE_SENSITIVE_CONFIG | DEPARTMENT_ID | No | Unknown | No |  |
| 6 | DEPARTMENT_ID | ED_ALRT_DFLT | DEPARTMENT_ID | No | Unknown | No |  |
| 6 | DEPARTMENT_ID | ED_DEP_SETTINGS | DEP_ID | No | Unknown | No |  |
| 6 | DEPARTMENT_ID | EXT_CAL_DEPT_CONFIG | DEPARTMENT_ID | No | Unknown | No |  |
| 6 | DEPARTMENT_ID | VISIT_MODE_CONFIG_DEP | DEPARTMENT_ID | No | Unknown | No |  |
| 6 | DEPARTMENT_ID | V_CUBE_D_DEPARTMENT | DEPARTMENT_ID | Unknown | Unknown | No |  |
| 6 | DEPARTMENT_ID | V_CUBE_D_DEP_LOC | DEPARTMENT_ID | Unknown | Unknown | No |  |

_(98 total; showing first 30)_
