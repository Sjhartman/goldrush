# BND_EPSD_INFO

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=BND_EPSD_INFO

## Description

This table contains information about bundled episodes. A bundled episode is used to link related encounters and services that can be billed together using a pre-defined agreement with a payor or guarantor.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | HSB |
| Release Version | Rel 2014 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| EPISODE_ID | NUMERIC (18,0) | This column stores the unique identifier for the bundled episode record. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| BND_EPSD_BILL_STS_C | INTEGER |  |
| COVERAGE_ID | NUMERIC (18,0) | This column stores the unique identifier for the coverage that will be billed for the bundled episode. |
| PAYOR_ID | NUMERIC (18,0) | This column stores the unique identifier for the payer responsible for the bundled episode's expected payment. |
| SELF_PAY_YN | VARCHAR (1) |  |
| BPC_ID | NUMERIC (18,0) | This column stores the unique identifier for the bundled episode terms associated with the bundled episode. The terms are used to define various reimbursement related attributes for a bundled episode. |
| BPC_CSN | NUMERIC (18,0) | The contact serial number of the bundled episode terms associated with the bundled episode. The terms are used to define various reimbursement related attributes for a bundled episode. |
| BILLING_START_DT | DATETIME | The start date from which the services are covered in the bundled episode. |
| BILLING_END_DT | DATETIME | The end date until which the services are covered in the bundled episode. |
| EXP_TOTAL_PMT | NUMERIC (18,2) | The amount of the total expected payment/target price from the responsible party of a bundled episode. |
| EXP_HOSP_PMT | NUMERIC (18,2) | The amount of the total hospital expected payment from the responsible party of a bundled episode. |
| EXP_PROF_PMT | NUMERIC (18,2) | The amount of the total professional expected payment from the responsible party of a bundled episode. This will only be used when a separate  professional payment is expected. |
| MAIN_EVENT_CSN | NUMERIC (18,0) | The contact serial number of the patient encounter that is the main encounter for this bundled episode. |
| MAIN_EVENT_USER_ID | VARCHAR (18) | This column stores the unique identifier for the user who set the main event for this bundled episode. |
| MAIN_EVENT_SET_DTTM | DATETIME (UTC) | The date and time that the main event was last set for this bundled episode. |
| CLOSE_OR_VOID_DATE | DATETIME | The closed or voided date of the bundled episode. |
| BND_EPSD_VOID_RSN_C | INTEGER |  |
| BND_EPSD_SYS_BILL_STS_C | INTEGER |  |
| LAST_LINK_UNLINK_DATE | DATETIME | The most recent date when a record was either linked or unlinked from the bundled episode. This will be updated when a hospital transaction, professional transaction, or hospital billing account is linked or unlinked. |
| LAST_ORIG_PMT_DATE | DATETIME | The most recent date when a global payment or refund was posted on the anchor hospital account. |
| LAST_BILL_LINK_UNLINK_DT | DATETIME | The most recent date when a record was either linked or unlinked from the bundled episode within the date range of a non-tracking phase. This will be updated when a hospital transaction, professional transaction, or hospital billing account is linked or unlinked. |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| B-TREE INDEX | EIX_BND_EPSD_INFO_BILLSTS | BND_EPSD_BILL_STS_C | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_BND_EPSD_INFO_CLOSEDT | CLOSE_OR_VOID_DATE | 1 | Yes | Yes |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | EPISODE_ID | ADMIN_PATHWAY_PERIOD | ADMIN_PWY_PERIOD_ID | Unknown | No | No |  |
| 1 | EPISODE_ID | ADMIN_PATHWAY_PERIOD_2 | ADMIN_PWY_PERIOD_ID | No | No | No |  |
| 1 | EPISODE_ID | AN_HSB_LINK_INFO | SUMMARY_BLOCK_ID | Unknown | No | No |  |
| 1 | EPISODE_ID | BMT_INFO | SUMMARY_BLOCK_ID | Unknown | No | No |  |
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
| 1 | EPISODE_ID | V_EHI_HSB_LINKED_PATS | EPISODE_ID | Unknown | Unknown | No |  |

_(194 total; showing first 30)_
