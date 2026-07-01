# OB_HSB_DEL_RP_DTTM

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=OB_HSB_DEL_RP_DTTM

## Description

The OB_HSB_DEL_RP_DTTM table contains membrane rupture date and time information recorded from the OB Delivery Summary. It uses the list of rupture dates and times stored in the patient's delivery record and combines them to create a list of date/time values. If a rupture time was recorded with no corresponding date, it is considered incomplete documentation and the line is thrown out.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | HSB |
| Release Version | Summer 2009 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| SUMMARY_BLOCK_ID | NUMERIC (18,0) | The unique ID assigned to the episode record (HSB .1). |
| LINE | No | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| OB_DEL_RUP_DTTM | 35151 | This column extracts the date and time of rupture for a delivery record. It uses the list of rupture dates and times stored in the patient's delivery record and concatenates them to create a list of correlated date/time values.  If no time value was recorded, the default is midnight (use RUPT_TM_PRESENT_YN to determine if a midnight value is entered by the user or defaulted in). |
| RUPT_TM_PRESENT_YN | No | This column denotes whether a rupture time was present in HSB 35151.  If there was no rupture time present, OB_DEL_RUP_DTTM stores midnight as a default time. |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | SUMMARY_BLOCK_ID | ADMIN_PATHWAY_PERIOD | ADMIN_PWY_PERIOD_ID | Unknown | No | No |  |
| 1 | SUMMARY_BLOCK_ID | ADMIN_PATHWAY_PERIOD_2 | ADMIN_PWY_PERIOD_ID | No | No | No |  |
| 1 | SUMMARY_BLOCK_ID | AN_HSB_LINK_INFO | SUMMARY_BLOCK_ID | Unknown | No | No |  |
| 1 | SUMMARY_BLOCK_ID | BMT_INFO | SUMMARY_BLOCK_ID | Unknown | No | No |  |
| 1 | SUMMARY_BLOCK_ID | BND_EPSD_INFO | EPISODE_ID | No | No | No |  |
| 1 | SUMMARY_BLOCK_ID | CARE_PATH | SUMMARY_BLOCK_ID | No | No | No |  |
| 1 | SUMMARY_BLOCK_ID | CATARACT_PLANNING_GOALS | SUMMARY_BLOCK_ID | No | No | No |  |
| 1 | SUMMARY_BLOCK_ID | CATARACT_PLANNING_INFO | SUMMARY_BLOCK_ID | No | No | No |  |
| 1 | SUMMARY_BLOCK_ID | EPISODE | EPISODE_ID | Unknown | No | No |  |
| 1 | SUMMARY_BLOCK_ID | EPISODE_2 | EPISODE_ID | Unknown | No | No |  |
| 1 | SUMMARY_BLOCK_ID | EPISODE_ALL | EPISODE_ID | No | No | No |  |
| 1 | SUMMARY_BLOCK_ID | EPISODE_AUTH | SUMMARY_BLOCK_ID | No | No | No |  |
| 1 | SUMMARY_BLOCK_ID | EPI_ANTICOAG | SUMMARY_BLOCK_ID | Unknown | No | No |  |
| 1 | SUMMARY_BLOCK_ID | F_AN_RECORD_SUMMARY | AN_EPISODE_ID | Unknown | Unknown | No |  |
| 1 | SUMMARY_BLOCK_ID | HH_EPSD_INFO | SUMMARY_BLOCK_ID | Unknown | No | No |  |
| 1 | SUMMARY_BLOCK_ID | HOME_INFUSION_EPSD | SUMMARY_BLOCK_ID | No | No | No |  |
| 1 | SUMMARY_BLOCK_ID | NEPHROLOGY_INFO | EPISODE_ID | No | No | No |  |
| 1 | SUMMARY_BLOCK_ID | NEPH_MODALITY_EPISODE | EPISODE_ID | Unknown | No | No |  |
| 1 | SUMMARY_BLOCK_ID | OB_HSB_DELIVERY | SUMMARY_BLOCK_ID | Unknown | No | No |  |
| 1 | SUMMARY_BLOCK_ID | OB_HSB_DELIVERY_2 | SUMMARY_BLOCK_ID | Unknown | No | No |  |
| 1 | SUMMARY_BLOCK_ID | OCCURRENCE_CODES | SUMMARY_BLOCK_ID | Unknown | No | No |  |
| 1 | SUMMARY_BLOCK_ID | PEF_NTFY_INSTR | EPISODE_ID | No | No | No |  |
| 1 | SUMMARY_BLOCK_ID | RAD_THERAPY_EPISODE_INFO | SUMMARY_BLOCK_ID | No | No | No |  |
| 1 | SUMMARY_BLOCK_ID | REHAB_PN_TRACKING | SUMMARY_BLOCK_ID | No | No | No |  |
| 1 | SUMMARY_BLOCK_ID | REHAB_REVIEW_CHOICE | SUMMARY_BLOCK_ID | No | No | No |  |
| 1 | SUMMARY_BLOCK_ID | RXMA_LOGISTICS | SUMMARY_BLOCK_ID | No | No | No |  |
| 1 | SUMMARY_BLOCK_ID | RXMA_RELATED_EPISODE | SUMMARY_BLOCK_ID | No | No | No |  |
| 1 | SUMMARY_BLOCK_ID | SOCIAL_CARE_EPISODE | EPISODE_ID | Unknown | No | No |  |
| 1 | SUMMARY_BLOCK_ID | TRANSPLANT_INFO | SUMMARY_BLOCK_ID | Unknown | No | No |  |
| 1 | SUMMARY_BLOCK_ID | V_EHI_HSB_FILTER_PAT | EPISODE_ID | Unknown | Unknown | No |  |

_(40 total; showing first 30)_
