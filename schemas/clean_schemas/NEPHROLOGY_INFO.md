# NEPHROLOGY_INFO

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=NEPHROLOGY_INFO

## Description

The NEPHROLOGY_INFO table contains information about a patient's dialysis episode. The records included in this table are HSB records that are designated as dialysis episodes, where the episode type (HSB 35250) has a value of 35.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | HSB |
| Release Version | Rel February 2019 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| EPISODE_ID | NUMERIC (18,0) | The unique identifier for the dialysis episode record. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| CONTACT_TYPE_ID | NUMERIC (18,0) | The episode type. |
| EPISODE_STATUS_C | INTEGER |  |
| DEPARTMENT_ID | NUMERIC (18,0) | Stores the department primarily responsible for managing the episode. |
| COMMENTS | VARCHAR (255) | The episode comments. |
| PAT_ID | VARCHAR (18) | Virtual item that checks item linkages between HSB and EPT and returns the first EPT ID that it finds. |
| DIALYSIS_ADMISSION_REASON_C | INTEGER |  |
| TRANSIENT_YN | VARCHAR (1) |  |
| DIALYSIS_DISCHARGE_REASON_C | INTEGER |  |
| TRANSFER_DESTINATION_C | INTEGER |  |
| TREATMENT_TYPE_C | INTEGER |  |
| DIALYSIS_HISTORICAL_EPISODE_YN | VARCHAR (1) |  |
| DIALYSIS_DISCHARGE_OTHR | VARCHAR (254) | This item stores a free text comment if a patient's dialysis discharge reason is set to Other. |
| DIALYSIS_START_DATE | DATETIME | This item is used to store the start date of a patient's dialysis treatment episode. |
| DIALYSIS_END_DATE | DATETIME | This item is used to store the end date of a patient's dialysis treatment episode. |
| PLACE_OF_SERVICE_ID | NUMERIC (18,0) | The episode's service area. |
| MODALITY_START_DATE | DATETIME | This item stores a dialysis patient's start date of their current treatment details. |
| DIALYSIS_EPISODE_PURPOSE_C | INTEGER |  |
| NEPH_DLYS_TYPE_C | INTEGER |  |
| NEPH_TRANSIENT_RSN_C | INTEGER |  |
| TREATMENT_SESSIONS_PER_WEEK | NUMERIC (18,1) | This item stores the most recently prescribed sessions per week of the dialysis treatments. |
| TREATMENT_DURATION_MINUTES | INTEGER | This item stores the most recently prescribed duration of each dialysis treatment in minutes. |
| EXTERNAL_FACILITY_ID | NUMERIC (18,0) | This item is used to store a dialysis patient's external treatment facility. |
| DLYS_INT_EPISODE_YN | VARCHAR (1) |  |
| GEN_MODALITY_C | INTEGER |  |
| EXT_DEDUP_DOCUMENT_ID | NUMERIC (22,0) | The deduplicated document ID for this episode. |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | EPISODE_ID | ADMIN_PATHWAY_PERIOD | ADMIN_PWY_PERIOD_ID | Unknown | No | No |  |
| 1 | EPISODE_ID | ADMIN_PATHWAY_PERIOD_2 | ADMIN_PWY_PERIOD_ID | No | No | No |  |
| 1 | EPISODE_ID | AN_HSB_LINK_INFO | SUMMARY_BLOCK_ID | Unknown | No | No |  |
| 1 | EPISODE_ID | BMT_INFO | SUMMARY_BLOCK_ID | Unknown | No | No |  |
| 1 | EPISODE_ID | BND_EPSD_INFO | EPISODE_ID | No | No | No |  |
| 1 | EPISODE_ID | CARE_PATH | SUMMARY_BLOCK_ID | No | No | No |  |
| 1 | EPISODE_ID | CATARACT_PLANNING_GOALS | SUMMARY_BLOCK_ID | No | No | No |  |
| 1 | EPISODE_ID | CATARACT_PLANNING_INFO | SUMMARY_BLOCK_ID | No | No | No |  |
| 1 | EPISODE_ID | EPISODE | EPISODE_ID | Unknown | No | No |  |
| 1 | EPISODE_ID | EPISODE_2 | EPISODE_ID | Unknown | No | No |  |
| 1 | EPISODE_ID | EPISODE_ALL | EPISODE_ID | No | No | No |  |
| 1 | EPISODE_ID | EPISODE_AUTH | SUMMARY_BLOCK_ID | No | No | No |  |
| 1 | EPISODE_ID | EPI_ANTICOAG | SUMMARY_BLOCK_ID | Unknown | No | No |  |
| 1 | EPISODE_ID | F_AN_RECORD_SUMMARY | AN_EPISODE_ID | Unknown | Unknown | No |  |
| 1 | EPISODE_ID | HH_EPSD_INFO | SUMMARY_BLOCK_ID | Unknown | No | No |  |
| 1 | EPISODE_ID | HOME_INFUSION_EPSD | SUMMARY_BLOCK_ID | No | No | No |  |
| 1 | EPISODE_ID | NEPH_MODALITY_EPISODE | EPISODE_ID | Unknown | No | No |  |
| 1 | EPISODE_ID | OB_HSB_DELIVERY | SUMMARY_BLOCK_ID | Unknown | No | No |  |
| 1 | EPISODE_ID | OB_HSB_DELIVERY_2 | SUMMARY_BLOCK_ID | Unknown | No | No |  |
| 1 | EPISODE_ID | OCCURRENCE_CODES | SUMMARY_BLOCK_ID | Unknown | No | No |  |
| 1 | EPISODE_ID | PEF_NTFY_INSTR | EPISODE_ID | No | No | No |  |
| 1 | EPISODE_ID | RAD_THERAPY_EPISODE_INFO | SUMMARY_BLOCK_ID | No | No | No |  |
| 1 | EPISODE_ID | REHAB_PN_TRACKING | SUMMARY_BLOCK_ID | No | No | No |  |
| 1 | EPISODE_ID | REHAB_REVIEW_CHOICE | SUMMARY_BLOCK_ID | No | No | No |  |
| 1 | EPISODE_ID | RXMA_LOGISTICS | SUMMARY_BLOCK_ID | No | No | No |  |
| 1 | EPISODE_ID | RXMA_RELATED_EPISODE | SUMMARY_BLOCK_ID | No | No | No |  |
| 1 | EPISODE_ID | SOCIAL_CARE_EPISODE | EPISODE_ID | Unknown | No | No |  |
| 1 | EPISODE_ID | TRANSPLANT_INFO | SUMMARY_BLOCK_ID | Unknown | No | No |  |
| 1 | EPISODE_ID | V_EHI_HSB_FILTER_PAT | EPISODE_ID | Unknown | Unknown | No |  |
| 1 | EPISODE_ID | V_EHI_HSB_LINKED_PATS | EPISODE_ID | Unknown | Unknown | No |  |

_(162 total; showing first 30)_
