# EPISODE_LINK

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=EPISODE_LINK

## Description

The EPISODE_LINK table contains high-level information on the episodes recorded in the clinical system for your patients. It is intended to associate an encounter with its linked episode. It only contains episodes linked to EPT.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | HSB |
| Release Version | EPIC 2000 |
| May contain EHI? | No |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| EPISODE_ID | NUMERIC (18,0) | The unique ID of the episode of care record. |
| LINE | No | Identifies each patient encounter within one episode. |
| STATUS *(deprecated)* | VARCHAR (10) |  |
| SUM_BLK_TYPE_ID | NUMERIC (18,0) | The category value associated with the type of the episode. The episode type determines what SmartForms and/or flowsheets are available for a particular episode in clinical system. |
| PAT_ID | No | DEPRECATED: Use PAT_ENC_CSN_ID and match it with column:PAT_ENC_CSN_ID in table:PAT_ENC for linking inpatient episodes to patient IDs.  The unique ID assigned to the patient record. This ID may be encrypted if you have elected to use enterprise reporting?s encryption utility.  NOTE: Gets the patient ID by looking up the CSN_ID associated with this episode record, and then using the EPIC_CSN_TO_ID to look up the patient ID from the CSN_ID.  There is a limitation with merged patients as this column will not update to the new patient id.  To work around this, use the PAT_ENC_CSN_ID and link it to PAT_ENC__PAT_ENC_CSN_ID.  The table PAT_ENC will contain the correct PAT_ID. |
| PAT_ENC_DATE_REAL | No |  |
| PAT_ENC_CSN_ID | NUMERIC (18,0) | A unique serial number for this encounter. This number is unique across all patients and encounters in the system. |
| CM_PHY_OWNER_ID | VARCHAR (25) | ID of the physical deployment owner for this record.  Physical owners will be where the data is hosted, either on the cross-over server or the owner deployment. |
| CM_LOG_OWNER_ID | VARCHAR (25) | ID of the logical deployment owner for this record.  Logical owners show the deployment where the record was created but doesn't represent if the record is a part of version skew. |
| EPI_STATUS_C | INTEGER |  |
| EPISODE_LINK_INI | VARCHAR (91) | Indicates in which master file more information about this episode can be found. |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| B-TREE INDEX | EIX_EPISODE_LINK_PATCSN | PAT_ENC_CSN_ID | 1 | Yes | Yes |  |

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
| 1 | EPISODE_ID | NEPHROLOGY_INFO | EPISODE_ID | No | No | No |  |
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

_(162 total; showing first 30)_
