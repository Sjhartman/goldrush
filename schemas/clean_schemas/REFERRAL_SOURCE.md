# REFERRAL_SOURCE

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=REFERRAL_SOURCE

## Description

The REFERRAL_SOURCE table contains information about referral sources. Referral sources can be physicians who write medical referrals for patients, or they can be marketing sources by which you acquire new patients.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | REF |
| Release Version | EPIC 2000 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| REFERRING_PROV_ID | VARCHAR (18) | The referral ID for the referral record. |
| REFERRING_PROV_NAM | VARCHAR (200) | The name of the referral source. |
| PROV_TYPE *(deprecated)* | VARCHAR (66) |  |
| FIRST_PROV_SPEC *(deprecated)* | VARCHAR (66) |  |
| FIRST_SERV_AREA_ID | NUMERIC (18,0) | The ID of the service area in which this referral source is available. |
| SSN | VARCHAR (12) | The Social Security Number of the referral source. |
| OFFICE_PHONE | VARCHAR (50) | The phone number for the referral source. |
| DOCTOR_DEGREE | VARCHAR (254) | The referral source?s medical degree. |
| VERIFIED_YN | VARCHAR (1) |  |
| EPIC_REF_SOURCE_ID *(deprecated)* | VARCHAR (18) | The unique ID of the referral source record. This ID may be hidden.  This column has been deprecated. It extracted information identical to the REFERRING_PROV_ID column in the same table. You should use the REFERRING_PROV_ID column instead of this one. |
| REF_PROVIDER_ID | VARCHAR (18) | The unique ID of the provider associated with this referral source. |
| CM_PHY_OWNER_ID | VARCHAR (25) | ID of the physical deployment owner for this record.  Physical owners will be where the data is hosted, either on the cross-over server or the owner deployment. |
| CM_LOG_OWNER_ID | VARCHAR (25) | ID of the logical deployment owner for this record.  Logical owners show the deployment where the record was created but doesn't represent if the record is a part of version skew. |
| CITY | VARCHAR (508) | The city field of the address of the referral source. |
| STATE_C | VARCHAR (66) |  |
| ZIP_CODE | VARCHAR (508) | The ZIP code of the address of the referral source. |
| COUNTY_C | VARCHAR (66) |  |
| COUNTRY_C | VARCHAR (66) |  |
| HOUSE_NUM | VARCHAR (254) | The house number of the address of the referral source. |
| DISTRICT_C | INTEGER |  |
| UPIN_NUM | VARCHAR (254) | The UPIN number for the referring provider |
| REF_PROV_TYPE_C | VARCHAR (66) |  |
| PROVIDER_TYPE_C | INTEGER |  |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| B-TREE INDEX | EIX_REFERRAL_SOURCE_EPRESOID | EPIC_REF_SOURCE_ID | 1 | Yes | Yes |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 5 | FIRST_SERV_AREA_ID | ANALYTICS_SYSTEM_SETTINGS | FACILITY_ID | No | No | No |  |
| 5 | FIRST_SERV_AREA_ID | ARPB_SA_SETTINGS | FACILITY_ID | No | No | No |  |
| 5 | FIRST_SERV_AREA_ID | CLARITY_LOC | LOC_ID | Unknown | No | No |  |
| 5 | FIRST_SERV_AREA_ID | CLARITY_LOC_2 | LOC_ID | Unknown | No | No |  |
| 5 | FIRST_SERV_AREA_ID | CLARITY_POS | POS_ID | No | No | No |  |
| 5 | FIRST_SERV_AREA_ID | CLARITY_POS_2 | POS_ID | No | No | No |  |
| 5 | FIRST_SERV_AREA_ID | CLARITY_SA | SERV_AREA_ID | Unknown | No | No |  |
| 5 | FIRST_SERV_AREA_ID | CL_LOC_HIERARCHY | LOC_ID | Unknown | No | No |  |
| 5 | FIRST_SERV_AREA_ID | CV_PCI_D2B_SETTINGS | FACILITY_ID | No | No | No |  |
| 5 | FIRST_SERV_AREA_ID | EAF_CLM_ALTADR_INF | FACILITY_ID | No | No | No |  |
| 5 | FIRST_SERV_AREA_ID | EAF_CLM_RMT_SETUP | FACILITY_ID | No | No | No |  |
| 5 | FIRST_SERV_AREA_ID | EAF_EXP_APPT_LOG | FACILITY_ID | No | No | No |  |
| 5 | FIRST_SERV_AREA_ID | EAF_SEARCH_TERMS | FACILITY_ID | No | No | No |  |
| 5 | FIRST_SERV_AREA_ID | ESCALATION_THRESH_SGL | FACILITY_ID | No | No | No |  |
| 5 | FIRST_SERV_AREA_ID | FAC_CONNECT | FACILITY_ID | No | No | No |  |
| 5 | FIRST_SERV_AREA_ID | FAC_DIRECT_ADDR | FACILITY_ID | Unknown | No | No |  |
| 5 | FIRST_SERV_AREA_ID | HH_FAC_INFO | FACILITY_ID | No | No | No |  |
| 5 | FIRST_SERV_AREA_ID | MC_FACILITY_GL_SEGMENTS | FACILITY_ID | No | No | No |  |
| 5 | FIRST_SERV_AREA_ID | MYC_INFO | FACILITY_ID | No | No | No |  |
| 5 | FIRST_SERV_AREA_ID | OR_LOC | LOC_ID | Unknown | No | No |  |
| 5 | FIRST_SERV_AREA_ID | PDMD_FILE_CONFIG | FACILITY_ID | No | No | No |  |
| 5 | FIRST_SERV_AREA_ID | RX_LOC | LOC_ID | Unknown | No | No |  |
| 5 | FIRST_SERV_AREA_ID | SD_FILTER_CONFIG_SETTING | FACILITY_ID | Yes | No | No |  |
| 5 | FIRST_SERV_AREA_ID | SERVICE_PROV | FACILITY_ID | No | No | No |  |
| 5 | FIRST_SERV_AREA_ID | SMS_SETTINGS_SNGL | FACILITY_ID | No | No | No |  |
| 5 | FIRST_SERV_AREA_ID | SYS_RSH_RPT_GRP_OVRIDE | FACILITY_ID | No | No | No |  |
| 5 | FIRST_SERV_AREA_ID | V_CMS_MU_LOC | LOC_ID | Unknown | Unknown | No |  |
| 5 | FIRST_SERV_AREA_ID | V_CUBE_D_LOCATION | LOCATION_ID | Unknown | Unknown | No |  |
| 5 | FIRST_SERV_AREA_ID | V_CUBE_D_SERVICE_AREA | SERVICE_AREA_ID | Unknown | Unknown | No |  |
| 5 | FIRST_SERV_AREA_ID | V_OR_LOC_STRUCTURE | OR_LOC_ID | Unknown | Unknown | No |  |

_(65 total; showing first 30)_
