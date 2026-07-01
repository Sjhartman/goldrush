# ENROLL_STAT_ACTV

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=ENROLL_STAT_ACTV

## Description

This table contains list of all enrollment statuses considered to be "active".

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | EAF |
| Release Version | Rel 2012 |
| May contain EHI? | No |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| FACILITY_ID | NUMERIC (18,0) | The unique identifier (.1 item) for the facility record. |
| LINE | INTEGER | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| RSH_ENR_STAT_ACT_C | INTEGER |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | FACILITY_ID | ANALYTICS_SYSTEM_SETTINGS | FACILITY_ID | No | No | No |  |
| 1 | FACILITY_ID | ARPB_SA_SETTINGS | FACILITY_ID | No | No | No |  |
| 1 | FACILITY_ID | CLARITY_LOC | LOC_ID | Unknown | No | No |  |
| 1 | FACILITY_ID | CLARITY_LOC_2 | LOC_ID | Unknown | No | No |  |
| 1 | FACILITY_ID | CLARITY_POS | POS_ID | No | No | No |  |
| 1 | FACILITY_ID | CLARITY_POS_2 | POS_ID | No | No | No |  |
| 1 | FACILITY_ID | CLARITY_SA | SERV_AREA_ID | Unknown | No | No |  |
| 1 | FACILITY_ID | CL_LOC_HIERARCHY | LOC_ID | Unknown | No | No |  |
| 1 | FACILITY_ID | CV_PCI_D2B_SETTINGS | FACILITY_ID | No | No | No |  |
| 1 | FACILITY_ID | EAF_CLM_ALTADR_INF | FACILITY_ID | No | No | No |  |
| 1 | FACILITY_ID | EAF_CLM_RMT_SETUP | FACILITY_ID | No | No | No |  |
| 1 | FACILITY_ID | EAF_EXP_APPT_LOG | FACILITY_ID | No | No | No |  |
| 1 | FACILITY_ID | EAF_SEARCH_TERMS | FACILITY_ID | No | No | No |  |
| 1 | FACILITY_ID | ESCALATION_THRESH_SGL | FACILITY_ID | No | No | No |  |
| 1 | FACILITY_ID | FAC_CONNECT | FACILITY_ID | No | No | No |  |
| 1 | FACILITY_ID | FAC_DIRECT_ADDR | FACILITY_ID | Unknown | No | No |  |
| 1 | FACILITY_ID | HH_FAC_INFO | FACILITY_ID | No | No | No |  |
| 1 | FACILITY_ID | MC_FACILITY_GL_SEGMENTS | FACILITY_ID | No | No | No |  |
| 1 | FACILITY_ID | MYC_INFO | FACILITY_ID | No | No | No |  |
| 1 | FACILITY_ID | OR_LOC | LOC_ID | Unknown | No | No |  |
| 1 | FACILITY_ID | PDMD_FILE_CONFIG | FACILITY_ID | No | No | No |  |
| 1 | FACILITY_ID | RX_LOC | LOC_ID | Unknown | No | No |  |
| 1 | FACILITY_ID | SD_FILTER_CONFIG_SETTING | FACILITY_ID | Yes | No | No |  |
| 1 | FACILITY_ID | SERVICE_PROV | FACILITY_ID | No | No | No |  |
| 1 | FACILITY_ID | SMS_SETTINGS_SNGL | FACILITY_ID | No | No | No |  |
| 1 | FACILITY_ID | SYS_RSH_RPT_GRP_OVRIDE | FACILITY_ID | No | No | No |  |
| 1 | FACILITY_ID | V_CMS_MU_LOC | LOC_ID | Unknown | Unknown | No |  |
| 1 | FACILITY_ID | V_CUBE_D_LOCATION | LOCATION_ID | Unknown | Unknown | No |  |
| 1 | FACILITY_ID | V_CUBE_D_SERVICE_AREA | SERVICE_AREA_ID | Unknown | Unknown | No |  |
| 1 | FACILITY_ID | V_OR_LOC_STRUCTURE | OR_LOC_ID | Unknown | Unknown | No |  |

_(37 total; showing first 30)_
