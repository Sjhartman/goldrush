# OB_HSB_DELIVERY_2

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=OB_HSB_DELIVERY_2

## Description

This table contains information about the delivery for this pregnancy, as entered in Stork's Delivery Summary activity.

**Overflow table** for OB_HSB_DELIVERY (101 cols). Contains additional columns for the same records — join on the shared primary key column.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | HSB |
| Release Version | Rel 2015 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| SUMMARY_BLOCK_ID | NUMERIC (18,0) | The unique identifier (.1 item) for the summary block record. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| AUGMENTATION_DTTM | 35117 | Stores the date that augmentation of labor began. |
| DEL_LIVING_CMT | VARCHAR (254) | This provides users an opportunity to provide additional information about the living status in OB History. |
| DEL_ADDL_CMT | VARCHAR (254) | This provides users an opportunity to document information related to a delivery that is not captured elsewhere. |
| OB_HX_LIVING_STAT_C | INTEGER |  |
| OB_LAST_KNOWN_LIV_C | INTEGER |  |
| OB_DEL_PLCENTA_LOC_DTTM | DATETIME (Local) | Stores the date and time the placenta was delivered. This is the same value as in OB_HSB_DELIVERY.OB_DEL_PLCENTA_DTTM but converted to the local time of the delivery encounter. This column will be blank for deliveries documented directly in OB History. |
| PUSHING_START_LOC_DTTM | DATETIME (Local) | Stores the instant when the mother starts to push for the first time during a delivery.  This is the same value as in OB_HSB_DELIVERY.PUSHING_START_DTTM but converted to the local time of the delivery encounter. This column will be blank for deliveries documented directly in OB History. |
| CORD_CLAMP_LOC_DTTM | DATETIME (Local) | Stores the instant the umbilical cord was clamped.  This is the same value as in OB_HSB_DELIVERY.CORD_CLAMP_DTTM but converted to the local time of the delivery encounter. This column will be blank for deliveries documented directly in OB History. |
| DECISION_LOC_DTTM | DATETIME (Local) | Stores the instant the decision was made for an emergent c-section.  This is the same value as in OB_HSB_DELIVERY.DECISION_DTTM but converted to the local time of the delivery encounter. This column will be blank for deliveries documented directly in OB History. |
| BREAST_FEED_ST_LOC_DTTM | DATETIME (Local) | Stores the instant that breastfeeding was initiated. This is the same value as in OB_HSB_DELIVERY.BREAST_FEED_ST_DTTM but converted to the local time of the delivery encounter. This column will be blank for deliveries documented directly in OB History. |
| DEL_PLACENTAL_WT | NUMERIC (8,3) | This item stores the placental weight in ounces. This information is stored in the delivery records. |
| ESTAB_RESPIR_UTC_DTTM | DATETIME (UTC) | Stores the  instant respiration was established for the newborn. |
| OB_DEL_LABOR_TYPE_C | INTEGER |  |
| PRIMARY_INDUCTION_REASON_C | INTEGER |  |
| ETHNIC_GROUP_C | INTEGER |  |
| BIRTH_ATTEND_PROV_ID | VARCHAR (18) | The attending provider active as of birth. One provider with the earliest assignment end instant after the birth and who did not begin that assignment after the birth is specified. |

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
| 1 | SUMMARY_BLOCK_ID | V_EHI_HSB_LINKED_PATS | EPISODE_ID | Unknown | Unknown | No |  |

_(57 total; showing first 30)_
