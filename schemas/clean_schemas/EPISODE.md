# EPISODE

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=EPISODE

## Description

This table contains high-level information on the episodes recorded in the clinical system for your patients. When a provider sees a patient several times for an ongoing condition, such as prenatal care, these encounters can be linked to a single Episode of Care. It does not contain episodes linked to an inpatient encounter.

**Primary table** in this group (101 cols). Overflow siblings joined on shared key: EPISODE_2 (57 cols), OCCURRENCE_CODES (10 cols). Prefer this table for most queries.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | HSB |
| Release Version | EPIC 2000 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| EPISODE_ID | NUMERIC (18,0) | The unique ID of the episode of care record. |
| NAME | VARCHAR (500) | The name of the episode. |
| STATUS *(deprecated)* | VARCHAR (10) |  |
| SUM_BLK_TYPE_ID | NUMERIC (18,0) | The episode type. |
| PAT_ID *(deprecated)* | VARCHAR (18) | DEPRECATED: This column is deprecated.  To link to patient encounters, use the PAT_ENC_CSN_ID column of the EPISODE_LINK table.  The unique ID assigned to the patient record. This ID may be encrypted if you have elected to use enterprise reporting?s encryption utility.  NOTE: Gets the patient ID by looking up the CSN_ID associated with this episode record, and then using the EPIC_CSN_TO_ID to look up the patient ID from the CSN_ID.  There is an issue with merged patients as this column will not update to the new patient id. |
| START_DATE | DATETIME | The date the episode was initiated. |
| END_DATE | DATETIME | The date the episode was resolved in calendar format. This field is called "Resolved" on the clinical system screen. |
| COMMENTS | VARCHAR (255) | Any free text comments about the episode. |
| CM_PHY_OWNER_ID | VARCHAR (25) | ID of the physical deployment owner for this record.  Physical owners will be where the data is hosted, either on the cross-over server or the owner deployment. |
| CM_LOG_OWNER_ID | VARCHAR (25) | ID of the logical deployment owner for this record.  Logical owners show the deployment where the record was created but doesn't represent if the record is a part of version skew. |
| PAT_ID_1900 | No | DEPRECATED: Look at the PAT_EPISODE table for linking non-inpatient episodes to patient IDs.   Original Description: The unique patient ID associated with an episode. Links the patient ID to the episode ID by associating item 1900 in the EPT master file with the episode ID. |
| STICKY_NOTE_TEXT | VARCHAR (500) | This item is used to hold text entered in the sticky note activity. |
| PROVIDERS_COMMENT | VARCHAR (254) | Comments for the Episodic Care providers. |
| PREGRAVID_WEIGHT | NUMERIC (18,1) | This field contains the pre-pregnancy weight maintained before this episode. |
| NUMBER_OF_BABIES | INTEGER | Prior to delivery, this column is expected to contain the number of fetuses that the patient is carrying. This can be manually documented, such as in the Prenatal Vitals section, or the value can be automatically set by creating or removing fetal result tabs in the ultrasound activity.  If your organization documents on the Delivery Summary then after the Delivery Summary is signed, this column is expected to contain the number of viable deliveries associated with the pregnancy. Specifically, this is the number of delivery records attached to the pregnancy. This expectation is based on Epic's recommendation that only viable deliveries should be documented on the Delivery Summary. Your organization may follow a different policy for when to create a delivery record. The behavior of this column containing the number of delivery records may be overridden at the profile level in system definitions, in which case it will continue to contain the number of fetuses that were being carried unless the number of deliveries is manually documented in its place. |
| DBC_EPISODE_YN | VARCHAR (1) |  |
| PRIMARY_LPL_ID | NUMERIC (18,0) | The primary problem linked to the episode. |
| SPECIALTY_C | VARCHAR (66) |  |
| HSB_DEF_NAME | VARCHAR (500) | This item will store the defaulted name of the episode if the episode was created automatically for a case. |
| STATUS_C | INTEGER |  |
| OB_DEL_PREG_EPI_ID | NUMERIC (18,0) | The value for this column is mom's pregnancy episode ID. This can be used to link from the delivery record to the corresponding pregnancy episode. Link EPISODE.OB_DEL_PREG_EPI_ID to EPISODE.EPISODE_ID, where the first table represents the delivery record and the second is the pregnancy episode. |
| OB_DELIVERY_BABY_ID | VARCHAR (18) | This column displays the baby's patient ID. For environments that are not IntraConnect-enabled, this column will be populated with the baby's patient ID in the row containing the delivery record.   IntraConnect - enabled environments: Delivery records are created on the mother record and ?mirrored? on the baby record. This column uses the ?mirrored" delivery record on the baby and thus will not display on a row from the mother delivery record. Follow the link EPISODE.OB_DEL_REC_COPY_ID to EPISODE.EPISODE_ID if you are using the mother record.  This column can be used to link to the PATIENT table via the column PAT_ID. |
| PAT_LINK_ID | VARCHAR (18) | Virtual item that checks HSB items linked to EPT and returns the first EPT ID it finds. |
| L_UPDATE_INST_DTTM | DATETIME (Local) | The date and time that the episode of care record was last updated. |
| L_UPDATE_USER_ID | VARCHAR (18) | The ID of the last user that updated the episode of care record. |
| OB_DEL_REC_COPY_ID | NUMERIC (18,0) | This item points to the delivery record that is attached directly to the pregnancy episode. This record's information is kept identical between the delivery records. The record with this item set is a child record of the baby's chart, and the record this item points to is a child record of the mother's chart.  This item is only populated in IntraConnect-enabled evironments. |
| PEF_LTST_INST_DTTM *(deprecated)* | DATETIME (Local) |  |
| REC_ARCHIVED_YN | No | Indicates whether the Episode record is archived at the record level. |
| PEF_MYC_STATUS_C *(deprecated)* | INTEGER |  |
| FATHER_NAME | VARCHAR (200) | The current legal name of the second parent. There was formerly an expectation this person was the father, but we now refer to this person as the second parent. There has not been a change to the business logic. |
| FATHER_BIRTHPLACE | VARCHAR (254) | The birthplace (state, territory, or country) of the second parent. There was formerly an expectation this person was the father, but we now refer to this person as the second parent. There has not been a change to the business logic. |
| FATHER_SSN | VARCHAR (192) | The social security number of the second parent. There was formerly an expectation this person was the father, but we now refer to this person as the second parent. There has not been a change to the business logic. |
| FATHER_EDU | VARCHAR (80) | The education level (in years) of the second parent. There was formerly an expectation this person was the father, but we now refer to this person as the second parent. There has not been a change to the business logic. |
| FATHER_ETHNICTY_C | INTEGER |  |
| FATHER_CITY | VARCHAR (50) | The city of the mailing address of the second parent. There was formerly an expectation this person was the father, but we now refer to this person as the second parent. There has not been a change to the business logic. |
| FATHER_STATE_C | VARCHAR (66) |  |
| FATHER_ZIP | VARCHAR (254) | The zip code of the mailing address of the second parent. There was formerly an expectation this person was the father, but we now refer to this person as the second parent. There has not been a change to the business logic. |
| PATERNITY_ACK_C | INTEGER |  |
| SMOKE_3_MO_BEF | INTEGER | The number of cigarettes/packs smoked per day 3 months before the pregnancy by the mother. |
| SMOKE_3_MO_BEF_C | INTEGER |  |
| SMOKE_1ST_3_MO | INTEGER | The number of cigarettes/packs smoked per day in the first 3 months of the pregnancy by the mother. |
| SMOKE_1ST_3_MO_C | INTEGER |  |
| SMOKE_2ND_3_MO | INTEGER | The number of cigarettes/packs smoked per day in the second 3 months of the pregnancy by the mother. |
| SMOKE_2ND_3_MO_C | INTEGER |  |
| SMOKE_3RD_TRI | INTEGER | The number of cigarettes/packs smoked per day in the third trimester of the pregnancy by the mother. |
| SMOKE_3RD_TRI_C | INTEGER |  |
| DRINK_3_MO_BEF | INTEGER | The number of alcoholic drinks consumed per week 3 months before the pregnancy by the mother. |
| DRINK_1ST_3_MO | INTEGER | The number of alcoholic drinks consumed per week in the first three months of the pregnancy by the mother. |
| DRINK_2ND_3_MO | INTEGER | The number of alcoholic drinks consumed per week in the second three months of the pregnancy by the mother. |
| DRINK_3RD_TRI | INTEGER | The number of alcoholic drinks consumed per week in the third trimester of the pregnancy by the mother. |
| IN_CITY_LIMITS_YN | VARCHAR (1) |  |
| WIC_FOODS_YN | VARCHAR (1) |  |
| FIRST_PNC_DT | DATETIME | Override value to be used in situations where not all prenatal care was given at the same Epic provider and so the first date of prenatal care is not in the system. |
| LAST_PNC_DT | DATETIME | Override value to be used in situations where not all prenatal care was given at the same Epic provider and so last date of prenatal care is not in the system. |
| TOTAL_PNC | INTEGER | Override value to be used in situations where not all prenatal care was given at the same Epic provider and so not all prenatal care visits are in the system. |
| MONTH_1ST_PNC | INTEGER | Override value to be used in situations where not all prenatal care was given at the same Epic provider and so first date of prenatal care is not in the system and the month of the pregnancy when prenatal care began cannot be calculated. |
| LIVE_BIRTHS_LIVING | INTEGER | Override value to be used in situations where not all prenatal care was given at the same Epic provider, and consequently, other pregnancy information is not available. The number of children born alive which are still living not including children born at this birth. |
| LIVE_BIRTHS_DEAD | INTEGER | Override value to be used in situations where not all prenatal care was given at the same Epic provider, and consequently, other pregnancy information is not available. The number of other children born alive which are now deceased not including any born alive and deceased at this birth. |
| MOTHER_BIRTHPLACE | VARCHAR (254) | The birthplace (state, territory, or country) of the mother of the baby. |
| MOTHER_MARRIED_YN | VARCHAR (1) |  |
| FATHER_DOB_DT | DATETIME | The date of birth of the second parent. There was formerly an expectation this person was the father, but we now refer to this person as the second parent. There has not been a change to the business logic. |
| OB_PREGRAVID_BMI | NUMERIC (18,1) | The patient's pre-pregnancy BMI for this pregnancy episode. |
| EPIS_GRAVIDA_COUNT | No |  |
| EPIS_PARA_COUNT | No |  |
| EPIS_TERM_COUNT | No |  |
| EPIS_PRETERM_COUNT | No |  |
| EPIS_ABORT_COUNT | No |  |
| EPIS_TAB_COUNT | No |  |
| EPIS_SAB_COUNT | No |  |
| EPIS_ECTOPIC_COUNT | No |  |
| FIRST_PNT_LOC_C | INTEGER |  |
| SERV_AREA_ID | NUMERIC (18,0) | The unique ID of the episode's service area. This column is used for DBC episodes, which are specific to a service area. |
| OB_WRK_EDD_DT | DATETIME | The estimated date of delivery for a pregnancy episode. |
| EDD_INITIAL_DT *(deprecated)* | DATETIME | *** Deprecated *** The data this column extracts is not useful for reporting.  Finds the initial EDD for a pregnancy as documented during the first prenatal visit. The first prenatal visit is determined by the contact with the earliest date attached to the pregnancy episode. |
| OB_HIGHEST_BP *(deprecated)* | INTEGER | *** Deprecated *** The data this column extracts is not useful for reporting.  The value of the highest diastolic blood pressure documented during a pregnancy episode. |
| EXPECTED_DEL_LOC_C | INTEGER |  |
| DEL_LOC_CHANGE_C | INTEGER |  |
| FATHER_BRTHCNTRY_C | VARCHAR (66) |  |
| EDD_DELIVERY_DT *(deprecated)* | DATETIME | *** Deprecated *** The data this column extracts is not useful for reporting.  Calculates the EDD at the start of labor. |
| OB_HIGHEST_BP_DT *(deprecated)* | DATETIME | *** Deprecated *** The data this column extracts is not useful for reporting.  Date of highest diastolic blood pressure during an episode. |
| HIGHEST_SYST_BP *(deprecated)* | INTEGER | *** Deprecated *** The data this column extracts is not useful for reporting.  Systolic blood pressure when the highest diastolic blood pressure value is recorded during an episode. |
| PREG_HT_DIAST_BP *(deprecated)* | INTEGER | *** Deprecated *** The data this column extracts is not useful for reporting.  Diastolic blood pressure when pregnancy-induced hypertension is noted for an episode via the configured flowsheet row. |
| PREG_HT_SYST_BP *(deprecated)* | INTEGER | *** Deprecated *** The data this column extracts is not useful for reporting.  Systolic blood pressure when pregnancy-induced hypertension is noted for an episode via the configured flowsheet row. |
| PREG_HT_DT *(deprecated)* | DATETIME | *** Deprecated *** The data this column extracts is not useful for reporting.  The date when pregnancy-induced hypertension is noted for an episode, in the configured flowsheet row. |
| OB_FEEDING_INTENTIONS_C | INTEGER |  |
| FATHER_BRTHCONT_C | INTEGER |  |
| OB_HX_ORDER | INTEGER | The order in which a given pregnancy occurred in relation to all documented pregnancies. |
| INTENT_TREAT_C | INTEGER |  |
| INTENT_TREAT_OTHR | VARCHAR (254) | The free text intended treatment for an implanted Mechanical Circulatory Device. |
| MCS_DISCHARGE_DT | DATETIME | Date a Mechanical Circulatory Device patient is discharged. |
| MCS_EVAL_DT | DATETIME | The start date of the Mechanical Circulatory Device evaluation. |
| MCS_REV_DT | DATETIME | The date when the Mechanical Circulatory Device case was reviewed by the evaluation committee. |
| MCS_ADMISSION_DT | DATETIME | Date of the admission for the Mechanical Circulatory Device procedure. |
| MCS_SURG_DT | DATETIME | The date of the Mechanical Circulatory Device surgery. |
| MCS_IS_HISTORIC_YN | VARCHAR (1) |  |
| MCS_EVAL_END_DT | DATETIME | The date on which the Mechanical Circulatory Device evaluation was completed. |
| MCS_NEXT_REVIEW_DT | DATETIME | The date on which both the Mechanical Circulatory Device episode and the patient chart should be reviewed. |
| MCS_REFERRAL_DT | DATETIME | The date the patient was referred for the Mechanical Circulatory Device. |
| MCS_TXPORT_MTHD_C | INTEGER |  |
| FATHER_OCCUPAT | VARCHAR (254) | Occupation of the father of the baby in the pregnancy episode |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| B-TREE INDEX | EIX_EPISODE_PAID | PAT_ID | 1 | Yes | Yes |  |

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

_(256 total; showing first 30)_
