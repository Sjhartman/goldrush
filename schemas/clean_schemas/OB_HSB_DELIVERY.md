# OB_HSB_DELIVERY

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=OB_HSB_DELIVERY

## Description

This table contains information about the delivery for this pregnancy, as entered in Stork's Delivery Summary activity.

**Primary table** in this group (101 cols). Overflow siblings joined on shared key: OB_HSB_DELIVERY_2 (19 cols). Prefer this table for most queries.

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
| CM_PHY_OWNER_ID | VARCHAR (25) | ID of the physical deployment owner for this record.  Physical owners will be where the data is hosted, either on the cross-over server or the owner deployment. |
| CM_LOG_OWNER_ID | VARCHAR (25) | ID of the logical deployment owner for this record.  Logical owners show the deployment where the record was created but doesn't represent if the record is a part of version skew. |
| OB_DEL_2ND_STAGE_HR | INTEGER | This column stores the length of the second stage of labor in number of hours. |
| OB_DEL_1ST_STAGE_HR | INTEGER | This column stores the length of the first stage of labor in number of hours. |
| OB_DEL_1ST_STAGE_M | INTEGER | This column stores the length of the first stage of labor in the number of minutes, and is added to OB_DEL_1ST_STAGE_HR to produce the total time. |
| OB_DEL_2ND_STAGE_M | INTEGER | This column stores the length of the second stage of labor in the number of minutes, and is added to OB_DEL_2ND_STAGE_HR to produce the total time. |
| OB_DEL_3RD_STAGE_M | INTEGER | This column stores the length of the third stage of labor in the number of minutes, and is added to OB_DEL_3RD_STAGE_HR to produce the total time. |
| OB_DEL_BLOOD_LOSS | INTEGER | Stores the amount of blood lost in the delivery, in milliliters. |
| OB_DEL_CRV_RPE_DATE *(deprecated)* | DATETIME | The date when cervical ripening occurred. NOTE: This column has been deprecated.  Use OB_DEL_CRV_RPE_DTTM instead. |
| OB_DEL_CRV_RPE_TIME *(deprecated)* | DATETIME | The time when cervical ripening occurred. NOTE: This column has been deprecated.  Use OB_DEL_CRV_RPE_DTTM instead. |
| OB_DEL_COMPL_CMT | VARCHAR (508) | Stores the comments for any complications associated with this delivery. |
| OB_DEL_REP_PACKETS | INTEGER | Stores the number of suture packets used on a patient during laceration/episiotomy repair from delivery. |
| DELIVERY_DATE_CSN | NUMERIC (18,0) | This item stores the contact serial number of the admission date in the mother's record during which the delivery occurred. |
| OB_DELIVERY_DATE | DATETIME | This item holds the date when this pregnancy was completed. This is the latest date of delivery of all the newborns associated with the pregnancy.  This column should not be used to determine the birth date of the baby. |
| OB_DEL_DIL_CMP_DATE *(deprecated)* | DATETIME | The date that dilation was complete and/or the mother entered the second stage of labor for this pregnancy. NOTE: This column has been deprecated.  Use OB_DEL_DIL_CMP_DTTM instead. |
| OB_DEL_DIL_CMP_TIME *(deprecated)* | DATETIME | The time that dilation was complete and/or the mother entered the second stage of labor for this pregnancy. NOTE: This column has been deprecated.  Use OB_DEL_DIL_CMP_DTTM instead. |
| OB_DEL_ONSET_DATE *(deprecated)* | DATETIME | The date that labor began for this pregnancy. NOTE: This column has been deprecated.  Use OB_DEL_ONSET_DTTM instead. |
| OB_DEL_ONSET_TIME *(deprecated)* | DATETIME | The time that labor began for this pregnancy. NOTE: This column has been deprecated.  Use OB_DEL_ONSET_DTTM instead. |
| OB_DEL_3RD_STAGE_HR | INTEGER | This column stores the length of the third stage of labor in number of hours. |
| OB_DEL_CRV_RPE_DTTM | 35113 | Stores the date and time when cervical ripening occurred. |
| OB_DEL_DIL_CMP_DTTM | 35160 | Stores the date and time that dilation was complete and/or the mother entered the second stage of labor for this pregnancy. |
| OB_DEL_ONSET_DTTM | 35162 | Stores the date and time that labor began for this pregnancy. |
| UPDATE_DATE | No | *** Deprecated *** This column is not reliably populated, row update tracking should be used instead. ****** The date and time this row was last updated (the last time it was extracted or this column was backfilled). |
| OB_DEL_PRES_REF_C | INTEGER |  |
| OB_DEL_PRES_LR_C | INTEGER |  |
| OB_DEL_PRES_AP_C | INTEGER |  |
| OB_DEL_CHEST_CIRC | NUMERIC (8,3) | Stores the baby's chest circumference measurement at birth, in inches. |
| OB_DEL_ANALGES_CMNT | VARCHAR (254) | Stores the analgesia comments recorded in the Delivery Summary. This information is stored in the delivery records. |
| OB_DEL_PLCENTA_DTTM | DATETIME (UTC) | Stores the date and time the placenta was delivered. This data is stored in UTC time rather than local time. You may need to convert this data for display in reports. For deliveries documented in the Delivery Summary, the local time can be found in OB_HSB_DELIVERY_2.OB_DEL_PLCENTA_LOC_DTTM. |
| OB_DEL_DELIV_MD_ID | VARCHAR (18) | Stores the unique ID of the provider (SER) who was responsible for delivering this infant. The data in this column are entered in the Delivery Summary activity and stored in the delivery record. |
| OB_DEL_APGAR_SK_1_C | INTEGER |  |
| OB_DEL_APGAR_SK_5_C | INTEGER |  |
| OB_DEL_APGAR_SK10_C | INTEGER |  |
| OB_DEL_APGAR_HR_1_C | INTEGER |  |
| OB_DEL_APGAR_HR_5_C | INTEGER |  |
| OB_DEL_APGAR_HR10_C | INTEGER |  |
| OB_DEL_APGAR_GR_1_C | INTEGER |  |
| OB_DEL_APGAR_GR_5_C | INTEGER |  |
| OB_DEL_APGAR_GR10_C | INTEGER |  |
| OB_DEL_APGAR_MU_1_C | INTEGER |  |
| OB_DEL_APGAR_MU_5_C | INTEGER |  |
| OB_DEL_APGAR_MU10_C | INTEGER |  |
| OB_DEL_APGAR_BR_1_C | INTEGER |  |
| OB_DEL_APGAR_BR_5_C | INTEGER |  |
| OB_DEL_APGAR_BR10_C | INTEGER |  |
| OB_DEL_BIRTH_LENGTH | NUMERIC (8,3) | Stores the infant's length at birth, in inches. |
| OB_DEL_BIRTH_WT | NUMERIC (8,3) | Stores the infant's weight at birth in ounces. |
| OB_DEL_HEAD_CIRCUM | NUMERIC (8,3) | Stores the infant's head circumference at birth, in inches. This information is entered in the Delivery Summary activity and is stored in the delivery records. |
| OB_DEL_APGAR_1_C | INTEGER |  |
| OB_DEL_APGAR_5_C | INTEGER |  |
| OB_DEL_APGAR_10_C | INTEGER |  |
| OB_DEL_DELIV_METH_C | VARCHAR (66) |  |
| OB_DEL_ANOMALIES | VARCHAR (254) | Stores the observed fetal anomalies. This information is stored in the delivery records. |
| OB_DEL_BIRTH_DTTM | DATETIME (UTC) | Stores the date and time of delivery for a delivery record. For values that are not fully confident (for example, if just the year was documented), the confidence is stored in the OB_HX_OUTC_FUZZY_C column. For those values, this column contains the UTC representation of midnight on the earliest date that the value could represent, relative to the time zone where the delivery was documented. This data is stored in UTC time rather than local time. You may need to convert this data for display in reports. For deliveries documented in the Delivery Summary, the local time can be found in PATIENT.BIRTH_DATE. |
| OB_DEL_EPIS_TYPE_C | INTEGER |  |
| OB_DEL_DEPT | NUMERIC (18,0) | This column displays the department where the delivery was performed. |
| PUSHING_START_DTTM | DATETIME (UTC) | The instant when the mother starts to push for the first time.  This data is stored in UTC time rather than local time. You may need to convert this data for display in reports. For deliveries documented in the Delivery Summary, the local time can be found in OB_HSB_DELIVERY_2.PUSHING_START_LOC_DTTM. |
| ROM_TO_DELIVER | INTEGER | This item displays the amount of time (in seconds) from rupture of membranes until the patient delivers. For pregnancy episodes, if there are multiples, it will calculate the length of time from the earliest rupture instant documented on a delivery record through to the latest delivery instant. |
| OB_DEL_STEROIDS_C | INTEGER |  |
| MOTHER_ANTIBIO_YN | VARCHAR (1) |  |
| FORCEPS_DEL_ATT_YN | VARCHAR (1) |  |
| VACUUM_DEL_ATT_YN | VARCHAR (1) |  |
| LABOR_ATTEMPT_YN | VARCHAR (1) |  |
| OB_DEL_APGAR_15_C | INTEGER |  |
| OB_DEL_APGAR_20_C | INTEGER |  |
| OB_DEL_APGAR_SK15_C | INTEGER |  |
| OB_DEL_APGAR_HR15_C | INTEGER |  |
| OB_DEL_APGAR_GR15_C | INTEGER |  |
| OB_DEL_APGAR_MU15_C | INTEGER |  |
| OB_DEL_APGAR_BR15_C | INTEGER |  |
| OB_DEL_APGAR_SK20_C | INTEGER |  |
| OB_DEL_APGAR_HR20_C | INTEGER |  |
| OB_DEL_APGAR_GR20_C | INTEGER |  |
| OB_DEL_APGAR_MU20_C | INTEGER |  |
| OB_DEL_APGAR_BR20_C | INTEGER |  |
| OBOR_TOT_BLOOD_LOSS *(deprecated)* | INTEGER |  |
| ADDITIONAL_EBL *(deprecated)* | INTEGER |  |
| BIRTH_ORDER | INTEGER | Order in which the baby is delivered during birth. For example, the second baby born in a triplet delivery would have a value of 2 for this column. You may want to use this column along with EPISODE.NUMBER_OF_BABIES to determine the total number of babies for this delivery. |
| OB_HX_GEST_AGE | INTEGER | Stores the pregnancy gestational age (GA) in days for an outcome in OB history. |
| OB_HX_DEL_SITE_C | INTEGER |  |
| OB_HX_CLINICIAN_FT | VARCHAR (254) | Stores the delivering clinician for an outcome in OB history. This is free text. |
| OB_HX_INFANT_SEX_C | VARCHAR (66) |  |
| OB_HX_INFANT_NAME | VARCHAR (254) | The name of the patient that this delivery record represents. This is free text. |
| OB_HX_OUTC_FUZZY_C | INTEGER |  |
| OB_HX_DEL_SITE_CMT | VARCHAR (254) | This is the comment corresponding to the delivery site (I HSB 35803). |
| OB_HX_OUTCOME_C | INTEGER |  |
| OB_HX_TOTAL_LOL_HR | INTEGER | The hours of the total length of labor for a delivery. |
| OB_HX_TOTAL_LOL_M | INTEGER | The minutes of the total length of labor for a delivery. |
| CONT_START_PAT_DTTM | 35190 | This column stores the date and time the contractions started according to the patient. |
| DILATION_START_DTTM | 35192 | This column stores the date and time that active dilation started for the patient. |
| SKIN_TO_SKIN_DTTM | 35200 | Stores the date and time that skin to skin with the baby was initiated. |
| CORD_CLAMP_DTTM | DATETIME (UTC) | This column stores the instant the umbilical cord was clamped.  For deliveries documented in the Delivery Summary, the local time can be found in OB_HSB_DELIVERY_2.CORD_CLAMP_LOC_DTTM. |
| INDUCTION_DTTM | 35205 | This column stores date and time of induction for delivery. |
| LABOR_IDENTIFIER_C | INTEGER |  |
| BABY_BIRTH_CSN | NUMERIC (18,0) | This item stores the contact serial number in the baby's record for the birth encounter. |
| DECISION_DTTM | DATETIME (UTC) | This column stores the instant the decision was made for an emergent c-section.  For deliveries documented in the Delivery Summary, the local time can be found in OB_HSB_DELIVERY_2.DECISION_LOC_DTTM. |
| BREAST_FEED_ST_DTTM | DATETIME (UTC) | This column stores the instant that breastfeeding was initiated.  For deliveries documented in the Delivery Summary, the local time can be found in OB_HSB_DELIVERY_2.BREAST_FEED_ST_LOC_DTTM. |
| SKIN_TO_SKIN_END_DTTM | 35209 | Stores the date that skin to skin was completed. |
| ABDOMINAL_GIRTH | NUMERIC (18,2) | The measurement of the baby's abdominal girth. |

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

_(366 total; showing first 30)_
