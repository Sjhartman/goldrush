# ACUITY_RULE_SCORE

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=ACUITY_RULE_SCORE

## Description

Extracted table for rule-related data from scoring system data filed to RDI.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | RDI |
| Release Version | Rel 2015 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| REGISTRY_DATA_ID | NUMERIC (18,0) | The unique identifier (.1 item) for the registry data record. |
| CONTACT_DATE_REAL | FLOAT | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| LINE | INTEGER | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| CONTACT_DATE | DATETIME | The date of this contact in calendar format. |
| RULE_ID | VARCHAR (18) | The unique ID of the CER rule used in the scoring system. |
| RULE_SCORE | NUMERIC (18,5) | The score from the rule in RULE_ID. |
| RULE_TYPE_C | INTEGER |  |
| SCORE_CALC_UTC_DTTM | DATETIME (UTC) | The date and time when the rule score is filed in UTC. |
| ADV_MODEL_OPTIONS | VARCHAR (60) | Stores all output selections of an Advanced Model HDA. |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | REGISTRY_DATA_ID | ACCCATH3_ADMISSION | REGISTRY_DATA_ID | Unknown | No | No |  |
| 1 | REGISTRY_DATA_ID | C4_ADMISSION | REGISTRY_DATA_ID | Unknown | No | No |  |
| 1 | REGISTRY_DATA_ID | CASE_RPT_ABSTNS | REGISTRY_DATA_ID | Unknown | No | No |  |
| 1 | REGISTRY_DATA_ID | CMS_SEP1_ABSTN | REGISTRY_DATA_ID | No | No | No |  |
| 1 | REGISTRY_DATA_ID | COVID_19_HSP_INFECTIONS | REGISTRY_DATA_ID | Yes | No | No |  |
| 1 | REGISTRY_DATA_ID | CW_ABST_ANEMIA_MINERAL | REGISTRY_DATA_ID | Unknown | No | No |  |
| 1 | REGISTRY_DATA_ID | CW_ABST_DEMOGRAPHICS | REGISTRY_DATA_ID | Unknown | No | No |  |
| 1 | REGISTRY_DATA_ID | CW_ABST_HD_ADEQUACY | REGISTRY_DATA_ID | Unknown | No | No |  |
| 1 | REGISTRY_DATA_ID | CW_ABST_MED_REC | REGISTRY_DATA_ID | No | No | No |  |
| 1 | REGISTRY_DATA_ID | CW_ABST_PAT_ATTEST | REGISTRY_DATA_ID | Unknown | No | No |  |
| 1 | REGISTRY_DATA_ID | CW_ABST_PD_ADEQUACY | REGISTRY_DATA_ID | Unknown | No | No |  |
| 1 | REGISTRY_DATA_ID | CW_ABST_VACCINATIONS | REGISTRY_DATA_ID | Unknown | No | No |  |
| 1 | REGISTRY_DATA_ID | CW_ABST_VASCULAR_ACCESS | REGISTRY_DATA_ID | Unknown | No | No |  |
| 1 | REGISTRY_DATA_ID | DD_DIALYSIS_VACCINATION_G | REGISTRY_DATA_ID | No | No | No |  |
| 1 | REGISTRY_DATA_ID | DD_DIA_CMS_DEATH | REGISTRY_DATA_ID | No | No | No |  |
| 1 | REGISTRY_DATA_ID | DD_DIA_CMS_DISCONTINUED | REGISTRY_DATA_ID | No | No | No |  |
| 1 | REGISTRY_DATA_ID | DD_DIA_CMS_START | REGISTRY_DATA_ID | No | No | No |  |
| 1 | REGISTRY_DATA_ID | DD_DIA_CMS_START_2 | REGISTRY_DATA_ID | No | No | No |  |
| 1 | REGISTRY_DATA_ID | DD_DIA_CMS_TELEMEDICINE | REGISTRY_DATA_ID | No | No | No |  |
| 1 | REGISTRY_DATA_ID | DD_NHSE_CAN_RTT_PWY_DAY | REGISTRY_DATA_ID | No | No | No |  |
| 1 | REGISTRY_DATA_ID | DD_NHSE_CAN_RTT_PWY_MTH | REGISTRY_DATA_ID | No | No | No |  |
| 1 | REGISTRY_DATA_ID | DD_NHSE_CAN_RTT_PWY_WK | REGISTRY_DATA_ID | No | No | No |  |
| 1 | REGISTRY_DATA_ID | DD_NHSE_CAN_TREAT_PWY_DAY | REGISTRY_DATA_ID | No | No | No |  |
| 1 | REGISTRY_DATA_ID | DD_NHSE_CAN_TREAT_PWY_MTH | REGISTRY_DATA_ID | No | No | No |  |
| 1 | REGISTRY_DATA_ID | DD_NHSE_CAN_TREAT_PWY_WK | REGISTRY_DATA_ID | No | No | No |  |
| 1 | REGISTRY_DATA_ID | DD_NHSE_DX_ACTIVITY | REGISTRY_DATA_ID | No | No | No |  |
| 1 | REGISTRY_DATA_ID | DD_NHSE_DX_ACT_ORDERS | REGISTRY_DATA_ID | No | No | No |  |
| 1 | REGISTRY_DATA_ID | DD_NHSE_DX_ACT_SURG_CASES | REGISTRY_DATA_ID | No | No | No |  |
| 1 | REGISTRY_DATA_ID | DD_NHSE_DX_ACT_WAIT_LISTS | REGISTRY_DATA_ID | No | No | No |  |
| 1 | REGISTRY_DATA_ID | DD_NHSE_DX_PWY_DAY | REGISTRY_DATA_ID | No | No | No |  |

_(139 total; showing first 30)_
