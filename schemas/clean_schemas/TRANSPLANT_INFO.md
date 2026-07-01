# TRANSPLANT_INFO

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=TRANSPLANT_INFO

## Description

This table contains information regarding the transplant episode. Only episodes whose Episode Type Class (I HBD 130) is 4 - Transplant will be included.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | HSB |
| Release Version | SPRING 2007 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| SUMMARY_BLOCK_ID | NUMERIC (18,0) | The unique ID of the episode of care record. |
| CM_PHY_OWNER_ID | VARCHAR (25) | ID of the physical deployment owner for this record.  Physical owners will be where the data is hosted, either on the cross-over server or the owner deployment. |
| CM_LOG_OWNER_ID | VARCHAR (25) | ID of the logical deployment owner for this record.  Logical owners show the deployment where the record was created but doesn't represent if the record is a part of version skew. |
| TX_REV_DT | DATETIME | Date on which the patient's information was presented at a multi-disciplinary committee meeting to determine whether to list the patient for transplant. |
| TX_EPSD_TYPE_C | INTEGER |  |
| TX_NUM | INTEGER | Stores the transplant number |
| TX_HIST_LOCATION | VARCHAR (254) | This item stores the location where a historic transplant occurred |
| TX_SURG_DT | DATETIME | Date on which the transplant surgery took place. |
| TX_IS_HISTORIC_YN | VARCHAR (1) |  |
| TX_EPSD_NOTE_HNO_ID | VARCHAR (254) | The transplant episode note record ID. |
| TX_HIST_STATE_C | VARCHAR (66) |  |
| TX_HIST_COUNTY_C | VARCHAR (66) |  |
| TX_WAITLIST_DT | DATETIME | Date on which the patient was placed on the waitlist |
| TX_DNR_POS_C | INTEGER |  |
| TX_DISCHARGE_DT | DATETIME | Date on which the patient was discharged after the transplant surgery. |
| TX_CURRENT_STAGE_C | INTEGER |  |
| TX_CURRENT_STAGE_DT | DATETIME | Effective date for the current phase, status, and reason of the transplant episode. |
| TX_CURRENT_STATUS_C | INTEGER |  |
| TX_CURRENT_REASON_C | INTEGER |  |
| TXP_EXTERNAL_CITY | VARCHAR (254) | City where the external transplant procedure was performed. |
| ADMISSION_DT | DATETIME | Date on which the patient was admitted for the transplant procedure. |
| BW_UNACCEPT_AG_C | INTEGER |  |
| TXP_NEXT_REVIEW_DT | DATETIME | Date on which the transplant episode and the patient chart should be reviewed. |
| TXP_ADMIT_CSN | NUMERIC (18,0) | The contact serial number (CSN) for the hospital admission when the transplant surgery was performed. |
| IN_TPN_DEPENDENT_YN | VARCHAR (1) |  |
| IN_IV_DEPENDENT_YN | VARCHAR (1) |  |
| IN_ORAL_FEEDING_YN | VARCHAR (1) |  |
| IN_TUBE_FEEDING_YN | VARCHAR (1) |  |
| LISTED_ELSEWHERE | VARCHAR (70) | Non-United Network for Organ Sharing (UNOS) center where the patient is listed. |
| TIME_TO_CENTER | NUMERIC (18,1) | The patient's travel time in hours to the transplant center. |
| EXHAUST_VASC_HEM_YN | VARCHAR (1) |  |
| EXHAUST_PERITON_YN | VARCHAR (1) |  |
| EXHAUST_IN_VASC_YN | VARCHAR (1) |  |
| LOSS_VASC_SITES_YN | VARCHAR (1) |  |
| FLUID_ELEC_LOSS_YN | VARCHAR (1) |  |
| NONRECON_GITRACT_YN | VARCHAR (1) |  |
| TXP_REFERRAL_DT | DATETIME | Date on which the patient was referred to transplant-related specialty care. |
| TX_HIST_PHONE | VARCHAR (31) | Phone number of the facility where the historic transplant took place. |
| TX_HIST_FAX | VARCHAR (31) | Fax for the facility where the historic transplant took place. |
| TX_HIST_COORD | VARCHAR (254) | The coordinator for the historic transplant. |
| TX_HIST_CENTER_C | INTEGER |  |
| TX_EVAL_DT | DATETIME | Date on which transplant evaluation began for the patient. |
| TX_DNR_WILLING_YN | VARCHAR (1) |  |
| TXP_CALC_RFL_DATE | DATETIME | Computed referral date for a transplant episode.  The following fields are checked, in this order, to obtain the referral date: 1. Transplant Referral Date (I HSB 30113). 2. From the transplant status history, the first time the episode reached the Pre-Evaluation phase in the system (I HSB 30056). 3. From the transplant status history, the first time the episode reached the Evaluation phase in the system (I HSB 30056). 4. Episode Start Date (I HSB 70). |
| TXP_CALC_EVAL_DATE | DATETIME | Computed evaluation date for a transplant episode.  The following fields are checked, in this order, to obtain the evaluation date: 1. Transplant Evaluation Date (I HSB 30007). 2. From the transplant status history, the first time the episode reached the Evaluation phase in the system (I HSB 30056). |
| TXP_CALC_CR_DATE | DATETIME | Computed committee review date for a transplant episode.  The following fields are checked, in this order, to obtain the committee review date: 1. Transplant Committee Review Date (I HSB 30025). 2. The earliest review date from Committee Review encounters linked to the episode (I EPT 98025). |
| TXP_CALC_ADMIT_DATE | DATETIME | Computed admission date for a transplant episode.  The following fields are checked, in this order, to obtain the admission date: 1. Transplant Admission Date (I HSB 30048). 2. The admission date from the encounter linked to the episode as the admission encounter (I EPT 18850), as stored in item TX ADMISSION CONTACT SERIAL NUMBER (I HSB 30185). |
| TXP_CALC_DISCHRG_DT | DATETIME | Computed discharge date for a transplant episode.  The following fields are checked, in this order, to obtain the discharge date: 1. Transplant Discharge Date (I HSB 30006). 2. The discharge date from the encounter linked to the episode as the admission encounter (I EPT 18855), as stored in item TX ADMISSION CONTACT SERIAL NUMBER (I HSB 30185). |
| TXPORT_MTHD_C | INTEGER |  |
| UNOS_ACCEPT | VARCHAR (20) | The United Network for Organ Sharing (UNOS) waitlist acceptance code. |
| DONOR_MIN_WT | NUMERIC (18,2) | The minimum acceptable donor weight. |
| DONOR_MAX_WT | NUMERIC (18,2) | The maximum acceptable donor weight |
| TX_CENTER_WL_DT | DATETIME | Date on which the patient was added to the center waitlist. |
| EPISODE_STATUS_C | INTEGER |  |
| PAT_ID | VARCHAR (18) | The patient associated with the episode. |
| TXP_REF_PROV_ID | VARCHAR (18) | The referring provider specified in the transplant care team. |
| TXP_SURGEON_ID | VARCHAR (18) | The surgeon specified in the transplant care team. If surgeon is not specified in the care team, it will be looked up from the associated surgical log. |
| TXP_CALC_EVAL_END_DT | DATETIME | Computed evaluation end date for a transplant episode.  The following fields are checked, in this order, to obtain the evaluation date: 1. Transplant Evaluation End Date (I HSB 30081). 2. If the episode is declined for transplant, use the status date 3. if the patient is waitlisted or above, use the center waitlist date(I HSB 30074), if empty, use waitlist date(I HSB 30061)  4. if patient died during referral/evaluation then return patient death date(I EPT 115) |
| UNOS_LIVER_SCORE | VARCHAR (254) | The most recent United Network for Organ Sharing (UNOS) liver score. |
| UNOS_LIVER_SCORE_DT | DATETIME | The date of the most recent United Network for Organ Sharing (UNOS) liver score update. |
| UNOS_LIVER_IS_PELD_YN | VARCHAR (1) |  |
| UNOS_LIVER_IS_STATUS_YN | VARCHAR (1) |  |
| UNOS_HEART_STATUS | VARCHAR (254) | The most recent United Network for Organ Sharing (UNOS) heart status. |
| UNOS_HEART_STATUS_DT | DATETIME | The date of the most recent United Network for Organ Sharing (UNOS) heart status. |
| UNOS_LAS | NUMERIC (18,4) | The most recent United Network for Organ Sharing (UNOS) lung allocation score. |
| UNOS_LAS_DT | DATETIME | The date of the most recent United Network for Organ Sharing (UNOS) lung allocation score. |
| UNOS_CPRA | INTEGER | The most recent United Network for Organ Sharing (UNOS) Calculated Panel Reactive Antibodies (CPRA) score. |
| UNOS_CPRA_DT | DATETIME | The most recent United Network for Organ Sharing (UNOS) Calculated Panel Reactive Antibodies (CPRA) score update date. |
| TXP_EVAL_END_DT | DATETIME | Date on which the transplant evaluation was completed for the patient. |
| UNOS_IN_STATUS | VARCHAR (254) | The most recent United Network for Organ Sharing (UNOS) intestine status. |
| UNOS_IN_STATUS_DT | DATETIME | The date of the most recent United Network for Organ Sharing (UNOS) intestine status. |
| TXP_CENTER_C | INTEGER |  |
| TXP_SURG_DTTM | DATETIME (UTC) | Contains the earliest clamp time from organs associated with the transplant episode. If there are no clamp times for any associated organs, this will be null. |
| HEIGHT_AT_TXP | NUMERIC (18,3) | The donor or recipient's height at transplant, in cm. |
| WEIGHT_AT_TXP | NUMERIC (18,2) | The donor or recipient's weight at transplant, in kg. |
| TOBACCO_USE_AT_TXP_C | INTEGER |  |
| ALCOHOL_USE_AT_TXP_C | INTEGER |  |
| DRUG_USE_AT_TXP_C | INTEGER |  |
| TXP_CENTER_AT_REFERRAL_C | INTEGER |  |
| TXP_CENTER_AT_EVALUATION_C | INTEGER |  |
| TXP_CENTER_AT_WAITLIST_C | INTEGER |  |
| TXP_CENTER_AT_COMMITTEE_C | INTEGER |  |
| TXP_CENTER_AT_TRANSPLANT_C | INTEGER |  |
| TXP_CALC_SURG_DATE | DATETIME | Computed transplant date for a transplant episode. The following fields are checked, in this order, to obtain the transplant date: 1. Transplant Date (I HSB 30050). 2. From the transplant status history, the first time the episode reached the Transplanted phase in the system (I HSB 30056). |
| TXP_CALC_WAITLIST_DATE | DATETIME | Computed waitlist date for a transplant episode. The following fields are checked, in this order, to obtain the waitlist date: 1. Transplant Center Waitlist Date (I HSB 30074). 2. Transplant Waitlist Qualifying Date (I HSB 30061). 3. From the transplant status history, the first time the episode reached the Waitlist phase in the system (I HSB 30056). |
| UNOS_CAS | NUMERIC (18,4) | Most recent lung composite allocation score |
| UNOS_CAS_DATE | DATETIME | The date of the most recent CAS subscore. |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| B-TREE INDEX | EIX_TRANSPLANT_INFO_EPSD_STAT | EPISODE_STATUS_C | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_TRANSPLANT_INFO_PAT_ID | PAT_ID | 1 | Yes | Yes |  |

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
| 1 | SUMMARY_BLOCK_ID | V_EHI_HSB_FILTER_PAT | EPISODE_ID | Unknown | Unknown | No |  |
| 1 | SUMMARY_BLOCK_ID | V_EHI_HSB_LINKED_PATS | EPISODE_ID | Unknown | Unknown | No |  |

_(272 total; showing first 30)_
