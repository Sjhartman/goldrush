# F_AN_RECORD_SUMMARY

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=F_AN_RECORD_SUMMARY

## Description

This derived fact table collects core information about anesthesia records into a standardized summary format. Each row uniquely represents an anesthesia record. Using this table, one can easily link to other important records and contacts linked to the anesthesia record for reporting purposes. Additionally, some important data for each anesthesia record, such as the procedure date and responsible anesthesiologist, is available in this table.

## Metadata

| Property | Value |
| --- | --- |
| Type | Derived Table |
| Load Frequency | INCREMENTAL |
| Release Version | Rel 2010 |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| AN_EPISODE_ID | NUMERIC (18,0) | The unique ID of the episode of care record. |
| UPDATE_DATE | No | The date and time when this row was extracted into enterprise reporting. |
| AN_PAT_ID | VARCHAR (18) | Stores the patient linked to this episode. |
| AN_53_ENC_CSN_ID | NUMERIC (18,0) | Stores the unique contact serial number for the 53-Anesthesia Event patient encounter associated with the anesthesia record. This number is unique across all patient encounters in your system. |
| AN_52_ENC_CSN_ID | NUMERIC (18,0) | Stores the unique contact serial number for the 52-Anesthesia patient encounter associated with the anesthesia record. This number is unique across all patient encounters in any given system. |
| AN_INPATIENT_DATA_ID | VARCHAR (18) | The unique ID of the Inpatient Data Store record. |
| AN_LOG_ID | VARCHAR (18) | The unique ID of the surgical case/log. |
| AN_PREOP_NOTE_ID *(deprecated)* | VARCHAR (254) | *** Deprecated *** In table F_AN_RECORD_SUMMARY, the column AN_PREOP_NOTE_ID has been deprecated.  Anesthesia Pre-op Evaluation notes can be found by joining from F_AN_RECORD_SUMMARY.AN_53_ENC_CSN_ID to HNO_INFO.PAT_ENC_CSN_ID and filtering by HNO_INFO.IP_NOTE_TYPE_C equalling 24. |
| AN_RESP_PROV_ID | VARCHAR (18) | Stores the overall responsible anesthesiologist for the anesthesia record. |
| AN_DATE | DATETIME | Stores the anesthesia procedure date for the anesthesia record. |
| AN_TIME | DATETIME (Local) | Stores the time when the procedure associated with the anesthesia record was performed. |
| AN_START_DATETIME | DATETIME (Local) | Stores the instant at which anesthesia started for the anesthesia record. |
| AN_STOP_DATETIME | DATETIME (Local) | Stores the instant at which anesthesia stopped for the anesthesia record. |
| AN_PROC_NAME | VARCHAR (500) | Stores the names of the procedures associated with the anesthesia record. If no procedure is specified, the free-text anesthesia record name will be used. |
| AN_BLOCK_NOTE_ID *(deprecated)* | VARCHAR (254) | *** Deprecated *** In table F_AN_RECORD_SUMMARY, the column AN_BLOCK_NOTE_ID has been deprecated.  Anesthesia Procedure notes can be found by joining from F_AN_RECORD_SUMMARY.AN_53_ENC_CSN_ID to HNO_INFO.PAT_ENC_CSN_ID and filtering by HNO_INFO.IP_NOTE_TYPE_C equalling 28. |
| CASE_ID | VARCHAR (18) | The unique ID of the case (ORC) that is associated with this anesthesia record. |
| LOG_ID | VARCHAR (18) | The unique ID of the log (ORL) that is associated with this anesthesia record. |
| CM_LOG_OWNER_ID | VARCHAR (25) | ID of the logical deployment owner for this record.  Logical owners show the deployment where the record was created but don't represent if the record is a part of version skew. |
| CM_PHY_OWNER_ID | VARCHAR (25) | ID of the physical deployment owner for this record.  Physical owners will be where the data is hosted, either on the cross-over server or the owner deployment. |
| AN_PRIMARY_NOTE_ID | VARCHAR (254) | Indicates which note record (HNO) to treat as the anesthesia preop note. |
| HAS_PERFUSION_YN | VARCHAR (1) |  |
| RPT_STATUS_C | INTEGER |  |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| B-TREE INDEX | EIX_FANRECSUM_LOG_ID | LOG_ID | 1 | Yes | Yes |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | AN_EPISODE_ID | ADMIN_PATHWAY_PERIOD | ADMIN_PWY_PERIOD_ID | Unknown | Unknown | No |  |
| 1 | AN_EPISODE_ID | ADMIN_PATHWAY_PERIOD_2 | ADMIN_PWY_PERIOD_ID | No | Unknown | No |  |
| 1 | AN_EPISODE_ID | AN_HSB_LINK_INFO | SUMMARY_BLOCK_ID | Unknown | Unknown | No |  |
| 1 | AN_EPISODE_ID | BMT_INFO | SUMMARY_BLOCK_ID | Unknown | Unknown | No |  |
| 1 | AN_EPISODE_ID | BND_EPSD_INFO | EPISODE_ID | No | Unknown | No |  |
| 1 | AN_EPISODE_ID | CARE_PATH | SUMMARY_BLOCK_ID | No | Unknown | No |  |
| 1 | AN_EPISODE_ID | CATARACT_PLANNING_GOALS | SUMMARY_BLOCK_ID | No | Unknown | No |  |
| 1 | AN_EPISODE_ID | CATARACT_PLANNING_INFO | SUMMARY_BLOCK_ID | No | Unknown | No |  |
| 1 | AN_EPISODE_ID | EPISODE | EPISODE_ID | Unknown | Unknown | No |  |
| 1 | AN_EPISODE_ID | EPISODE_2 | EPISODE_ID | Unknown | Unknown | No |  |
| 1 | AN_EPISODE_ID | EPISODE_ALL | EPISODE_ID | No | Unknown | No |  |
| 1 | AN_EPISODE_ID | EPISODE_AUTH | SUMMARY_BLOCK_ID | No | Unknown | No |  |
| 1 | AN_EPISODE_ID | EPI_ANTICOAG | SUMMARY_BLOCK_ID | Unknown | Unknown | No |  |
| 1 | AN_EPISODE_ID | HH_EPSD_INFO | SUMMARY_BLOCK_ID | Unknown | Unknown | No |  |
| 1 | AN_EPISODE_ID | HOME_INFUSION_EPSD | SUMMARY_BLOCK_ID | No | Unknown | No |  |
| 1 | AN_EPISODE_ID | NEPHROLOGY_INFO | EPISODE_ID | No | Unknown | No |  |
| 1 | AN_EPISODE_ID | NEPH_MODALITY_EPISODE | EPISODE_ID | Unknown | Unknown | No |  |
| 1 | AN_EPISODE_ID | OB_HSB_DELIVERY | SUMMARY_BLOCK_ID | Unknown | Unknown | No |  |
| 1 | AN_EPISODE_ID | OB_HSB_DELIVERY_2 | SUMMARY_BLOCK_ID | Unknown | Unknown | No |  |
| 1 | AN_EPISODE_ID | OCCURRENCE_CODES | SUMMARY_BLOCK_ID | Unknown | Unknown | No |  |
| 1 | AN_EPISODE_ID | PEF_NTFY_INSTR | EPISODE_ID | No | Unknown | No |  |
| 1 | AN_EPISODE_ID | RAD_THERAPY_EPISODE_INFO | SUMMARY_BLOCK_ID | No | Unknown | No |  |
| 1 | AN_EPISODE_ID | REHAB_PN_TRACKING | SUMMARY_BLOCK_ID | No | Unknown | No |  |
| 1 | AN_EPISODE_ID | REHAB_REVIEW_CHOICE | SUMMARY_BLOCK_ID | No | Unknown | No |  |
| 1 | AN_EPISODE_ID | RXMA_LOGISTICS | SUMMARY_BLOCK_ID | No | Unknown | No |  |
| 1 | AN_EPISODE_ID | RXMA_RELATED_EPISODE | SUMMARY_BLOCK_ID | No | Unknown | No |  |
| 1 | AN_EPISODE_ID | SOCIAL_CARE_EPISODE | EPISODE_ID | Unknown | Unknown | No |  |
| 1 | AN_EPISODE_ID | TRANSPLANT_INFO | SUMMARY_BLOCK_ID | Unknown | Unknown | No |  |
| 1 | AN_EPISODE_ID | V_EHI_HSB_FILTER_PAT | EPISODE_ID | Unknown | Unknown | No |  |
| 1 | AN_EPISODE_ID | V_EHI_HSB_LINKED_PATS | EPISODE_ID | Unknown | Unknown | No |  |

_(379 total; showing first 30)_
