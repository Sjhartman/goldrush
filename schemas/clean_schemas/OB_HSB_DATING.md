# OB_HSB_DATING

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=OB_HSB_DATING

## Description

This table contains the associated information about the criteria for determining the estimated date of delivery for this pregnancy.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | HSB |
| Release Version | SPRING 2008 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| SUMMARY_BLOCK_ID | NUMERIC (18,0) | The unique ID assigned to the episode record (HSB .1). |
| LINE | No |  |
| CM_PHY_OWNER_ID | VARCHAR (25) | ID of the physical deployment owner for this record.  Physical owners will be where the data is hosted, either on the cross-over server or the owner deployment. |
| CM_LOG_OWNER_ID | VARCHAR (25) | ID of the logical deployment owner for this record.  Logical owners show the deployment where the record was created but doesn't represent if the record is a part of version skew. |
| OB_DT_EVENT_C | INTEGER |  |
| OB_DT_DTESYS_DT | DATETIME | The system-calculated date when this event occurred. |
| OB_DT_DTEUSR_DT | DATETIME | The date when this event occurred, as entered by the user. |
| OB_DT_GA_SYS | INTEGER | The gestational age at which this event is expected to occur, as calculated by the system. This value represents the gestational age in days. |
| OB_DT_GA_USR | INTEGER | The gestational age at which this criterion did occur, as specified by the user. This value represents the gestational age in days. |
| OB_DT_EDDSYS_DT | DATETIME | The estimated date of delivery based on this criterion, as calculated by the system. |
| OB_DT_EDDUSR_DT | DATETIME | The estimated date of delivery based on this criterion, as entered by the user. |
| OB_DT_WRKEDD_YN | VARCHAR (1) |  |
| OB_DT_ROWIDX | INTEGER | Currently, this column contains the line count and is analogous to the LINE column in this table. |
| OB_DT_RPLROW | INTEGER | The dating table represents all calculations, entries, and documentation on dating criteria. If a given row is changed by the user, it is not changed in the system. Instead, a new row representing the changes is added, and it is considered to replace the old row. This column indicates the line number of the row that this line deprecates. |
| OB_DT_ENTINS_TM | DATETIME (Local) | The instant this row was entered and saved. |
| OB_DT_ENTUSR_ID | VARCHAR (18) | The user who has entered the information for this specific dating event. |
| OB_DT_ENT_PT_C | INTEGER |  |
| OB_DT_CYC_LN | INTEGER | The patient's average menstrual cycle length. |
| OB_DT_LUT_LN | INTEGER | The average length of the menstrual cycle's luteal phase. |
| OB_DT_AFTOVU | INTEGER | The number of days after ovulation that conception occurred. |
| OB_DT_ENT_CMT | VARCHAR (2000) | A comment for this event. |
| OB_DT_BTHCTL_YN | VARCHAR (1) |  |
| OB_DT_UTZID_C_ID | NUMERIC (18,0) | If the entry in the dating table came from an ultrasound resulted in Epic, this item contains the source ORD ID. |
| OB_DT_DTEPREC_C | INTEGER |  |
| OB_DT_REASONCHNG_C | INTEGER |  |

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

_(131 total; showing first 30)_
