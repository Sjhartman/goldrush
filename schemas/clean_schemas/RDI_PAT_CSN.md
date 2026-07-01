# RDI_PAT_CSN

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=RDI_PAT_CSN

## Description

This table displays the contact information that is related to the report generated for the ACC Registry.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | RDI |
| Release Version | Summer 2009 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| REGISTRY_DATA_ID | NUMERIC (18,0) | The unique identifier for the registry data record. |
| LINE | No | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| PAT_CSN | NUMERIC (18,0) | The main patient CSNs that are associated with the record. |
| UPDATE_DATE | No | The date and time this row was inserted. |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| B-TREE INDEX | EIX_RDI_PAT_CSN_PAT_CSN | PAT_CSN | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_RDI_PAT_CSN_PAT_CSN | REGISTRY_DATA_ID | 2 | Yes | Yes |  |

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

_(255 total; showing first 30)_
