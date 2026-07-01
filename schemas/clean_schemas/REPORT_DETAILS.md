# REPORT_DETAILS

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=REPORT_DETAILS

## Description

This table contains information about general characteristics of reports containing print groups.  This table includes whether it is an HTML report or time sensitive, the stylesheet used, setup extensions, print class, and content type.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | LRP |
| Release Version | SPRING 2008 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| LRP_ID | VARCHAR (18) | The unique ID of the report. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| REPORT_NAME | VARCHAR (254) | The name of the report |
| RECORD_STATE_C | INTEGER |  |
| TEMP_NAME_EDIT *(deprecated)* | VARCHAR (254) |  |
| HTML_REPORT_YN | VARCHAR (1) |  |
| STYLESHEET_C | INTEGER |  |
| PAGE_SUPPRESS_YN | VARCHAR (1) |  |
| GEN_SETUP_PPT_ID | NUMERIC (18,0) | The unique ID of the programming point that is used for general setup. |
| RPT_COMP_PPT_ID | NUMERIC (18,0) | The unique ID of the programming point that is used for report completion. |
| ALIGN_LEFT_RIGHT_YN | VARCHAR (1) |  |
| TIME_SENSITIVE_YN | VARCHAR (1) |  |
| SYNOPSIS_DEPT_C | INTEGER |  |
| SYNOPSIS_VIEW_TITLE | VARCHAR (75) | Synopsis view title. |
| DEFAULT_REPORT | VARCHAR (18) | The default report to use if the redirector doesn't find any matches. |
| PRINTER_CLASS_C | VARCHAR (66) |  |
| BEFORE_RUN_SETUP_ID | NUMERIC (18,0) | This item contains a programming point that runs before initial processing of the report begins.  This programming point will run before report engine initialization routine is called. |
| RPT_CONTENT_TYPE_C | INTEGER |  |
| SYNOPSIS_HIDE_MR_YN | VARCHAR (1) |  |
| SYNOP_SHOW_GRID_YN *(deprecated)* | VARCHAR (1) |  |
| SYNOPSIS_HEADER_ID | NUMERIC (18,0) | Programming point to specify custom OP Synopsis headers. |
| LRP_BASE_TEMPLATE_ID | VARCHAR (18) | A template off of which a report will be based. |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 2 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 2 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 3 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 5 | RECORD_STATE_C | ZC_DEL_STATUS | DEL_STATUS_C | No | No | No |  |
| 5 | RECORD_STATE_C | ZC_EDG_REC_STAT | EDG_REC_STAT_C | No | No | No |  |
| 5 | RECORD_STATE_C | ZC_ERS_REC_STAT | RECORD_STATUS_C | No | No | No |  |
| 5 | RECORD_STATE_C | ZC_HCD_REC_STATE | HCD_REC_STATE_C | No | No | No |  |
| 5 | RECORD_STATE_C | ZC_HFL_RECORD_STAT | HFL_RECORD_STAT_C | No | No | No |  |
| 5 | RECORD_STATE_C | ZC_IMM_REC_STATUS | IMM_REC_STATUS_C | No | No | No |  |
| 5 | RECORD_STATE_C | ZC_LLB_STATUS | LLB_STATUS_C | No | No | No |  |
| 5 | RECORD_STATE_C | ZC_LMA_RECORD_STAT | LMA_RECORD_STAT_C | No | No | No |  |
| 5 | RECORD_STATE_C | ZC_MEM_REC_STATUS | MEM_REC_STATUS_C | No | No | No |  |
| 5 | RECORD_STATE_C | ZC_OR_REC_STATUS | OR_REC_STATUS_C | No | No | No |  |
| 5 | RECORD_STATE_C | ZC_PBA_REC_STAT | PBA_REC_STAT_C | No | No | No |  |
| 5 | RECORD_STATE_C | ZC_PROV_REC_STATE | PROV_REC_STATE_C | No | No | No |  |
| 5 | RECORD_STATE_C | ZC_RECORD_STATE_2 | RECORD_STATE_2_C | No | No | No |  |
| 5 | RECORD_STATE_C | ZC_RECORD_STATE_3 | RECORD_STATE_3_C | No | No | No |  |
| 5 | RECORD_STATE_C | ZC_RECORD_STATE_4 | RECORD_STATE_4_C | No | No | No |  |
| 5 | RECORD_STATE_C | ZC_RECORD_STATE_6 | RECORD_STATE_6_C | No | No | No |  |
| 5 | RECORD_STATE_C | ZC_RECORD_STATE_7 | RECORD_STATE_7_C | No | No | No |  |
| 5 | RECORD_STATE_C | ZC_RECORD_STAT_EPM | RECORD_STAT_EPM_C | No | No | No |  |
| 5 | RECORD_STATE_C | ZC_RECORD_STAT_EPP | RECORD_STAT_EPP_C | No | No | No |  |
| 5 | RECORD_STATE_C | ZC_RECORD_STAT_ETX | RECORD_STAT_ETX_C | No | No | No |  |
| 5 | RECORD_STATE_C | ZC_RECORD_STAT_HRV | RECORD_STAT_HRV_C | No | No | No |  |
| 5 | RECORD_STATE_C | ZC_RECORD_STAT_RMC | RECORD_STAT_RMC_C | No | No | No |  |
| 8 | STYLESHEET_C | ZC_STYLESHEET | STYLESHEET_C | No | No | No |  |
| 10 | GEN_SETUP_PPT_ID | CLARITY_LPP | LPP_ID | Unknown | No | No |  |

_(37 total; showing first 30)_
