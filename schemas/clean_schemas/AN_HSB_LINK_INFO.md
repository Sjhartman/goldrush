# AN_HSB_LINK_INFO

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=AN_HSB_LINK_INFO

## Description

This table stores Anesthesia episode-level information.

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
| SUMMARY_BLOCK_ID | NUMERIC (18,0) | The unique ID of the Episode (HSB) record for this row. Episodes store information including the start and end dates, episode status and type, and any contacts associated with the episode. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| ANES_EPT_LINK_ID | VARCHAR (18) | Stores the patient linked to this episode. |
| ANES_EPT_CSN_LINK | NUMERIC (18,0) | Patient encounter linked to this episode, if one exists (true for surgical or scheduled reasons, false for order or other reasons). |
| AN_UNLINKED_FLAG_YN | VARCHAR (1) |  |
| ANES_PROC_ID | NUMERIC (18,0) | Stores the procedure that corresponds to this anesthesia episode. |
| ANES_PROC_DATE | DATETIME | Stores the date for the procedure of the anesthesia episode. |
| ANES_PRE_OP_DIAG_ID | NUMERIC (18,0) | The pre-op diagnosis for this anesthesia episode. |
| ANES_PROC_TIME | DATETIME (Local) | Stores the time when the procedure associated with the anesthesia episode was performed. |
| ANES_PROC_CMT | VARCHAR (254) | Comment for anesthesia procedure. |
| ANES_PREOP_COMP_YN | VARCHAR (1) |  |
| ANES_INTRAOP_COM_YN | VARCHAR (1) |  |
| ANES_PACU_COMP_YN | VARCHAR (1) |  |
| ANES_POSTOP_COMP_YN | VARCHAR (1) |  |
| ANES_DOC_COMP_YN | VARCHAR (1) |  |
| AN_DOC_COMP_INSTANT | DATETIME (Local) | The instant that all documentation for an anesthesia episode was marked as complete. |
| AN_BATCH_CLS_DON_YN | VARCHAR (1) |  |
| AN_RESP_PROV_ID | VARCHAR (18) | Stores the overall responsible anesthesiologist for the anesthesia record. |
| AN_DATE | DATETIME | Stores the anesthesia procedure date for the anesthesia record. |
| AN_TIME | DATETIME (Local) | Stores the time when the procedure associated with the anesthesia record was performed. |
| AN_START_DATETIME | DATETIME (Local) | Stores the instant at which anesthesia started for the anesthesia record. |
| AN_STOP_DATETIME | DATETIME (Local) | Stores the instant at which anesthesia stopped for the anesthesia record. |
| UPDATE_DATE | No | *** Deprecated *** This column is not reliably populated, row update tracking should be used instead. ****** The date and time when this row was extracted into enterprise reporting. |
| NAME | VARCHAR (500) | The name of the anesthesia episode. |
| AN_52_ENC_CSN_ID | NUMERIC (18,0) | Stores the unique contact serial number for the 52-Anesthesia patient encounter associated with the anesthesia record. This number is unique across all patient encounters in any given system. |
| AN_PROC_NAME | VARCHAR (500) | Stores the names of the procedures associated with the anesthesia record. If no procedure is specified, the free-text anesthesia record name will be used. |
| AN_RECORD_DATE | DATETIME | The date for this anesthesia record. |
| AN_BILLING_CSN_ID | NUMERIC (18,0) | The unique contact serial number for the Billing Encounter. This contains all the billing information needed to drop charges. |
| AN_MACRO_TRIED_YN | VARCHAR (1) |  |
| PRIMARY_LOG_ENC_CSN | NUMERIC (18,0) | Identifies the anesthesia record's primary log encounter contact serial number (CSN). |
| PRIMARY_PRC_ENC_CSN | NUMERIC (18,0) | Identifies the primary procedure's encounter contact serial number (CSN). |
| AN_BAT_PROCESS_DTTM | DATETIME (UTC) | The instant that a batch job processed the Anesthesia Record. |
| AN_PRIMARY_NOTE_ID | VARCHAR (254) | Indicates which note record (HNO) to treat as the anesthesia preop note. |
| RPT_STATUS_C | INTEGER |  |
| AN_ENC_REF_IDENT | VARCHAR (174) | Deduplicated document reference ID for the external anesthesia encounter. |
| BILLING_ENC_REF_IDENT | VARCHAR (174) | Deduplicated document reference ID for the external billing encounter. Typically, this encounter is the admission. |
| PRIMARY_LOG_ID | VARCHAR (18) | This column contains the primary procedure log from external data. This is only populated on the Cosmos host. |
| EXTERNAL_EPISODE_REF_IDENT | VARCHAR (174) | The reference ID of the external data used to generate this anesthesia episode. |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | SUMMARY_BLOCK_ID | ADMIN_PATHWAY_PERIOD | ADMIN_PWY_PERIOD_ID | Unknown | No | No |  |
| 1 | SUMMARY_BLOCK_ID | ADMIN_PATHWAY_PERIOD_2 | ADMIN_PWY_PERIOD_ID | No | No | No |  |
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
| 1 | SUMMARY_BLOCK_ID | V_EHI_HSB_LINKED_PATS | EPISODE_ID | Unknown | Unknown | No |  |

_(736 total; showing first 30)_
