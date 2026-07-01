# SOCIAL_HX

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=SOCIAL_HX

## Description

The SOCIAL_HX table contains social history data for each history encounter stored in your system. This table has one row per history encounter.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | EPT |
| Release Version | EPIC 2000 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| PAT_ID | VARCHAR (18) | The unique ID assigned to the patient record. |
| PAT_ENC_DATE_REAL | No | This is a numeric representation of the date of this encounter in your system. The integer portion of the number specifies the date of the encounter. The digits after the decimal point indicate multiple visits on one day. |
| CONTACT_DATE | DATETIME | The date of this contact in calendar format. |
| END_HIST_DATE_REAL | No | This column has been deprecated since it cannot be used with table-based tracking unless a full extract of EPT is run. This is very bad for performance. |
| IS_TOBACCO_USER *(deprecated)* | VARCHAR (10) |  |
| TOBACCO_PAK_PER_DY | VARCHAR (20) | *Partially Deprecated*. The number of packs of cigarettes the patient smokes per day, or null if the patient does not smoke. The tobacco data model has been updated and new data will no longer be saved to this item. It is recommended to use V_PAT_HX_TOB_USE->TOB_CURRENT_PPD instead. |
| TOBACCO_USED_YEARS | VARCHAR (20) | *Partially Deprecated*. The number of years a patient has smoked. The tobacco data model has been updated and new data will no longer be saved to this item. Though not a 1x1 equivalent it is recommended to use V_PAT_HX_TOB_USE->TOB_PACK_YEARS instead. |
| TOBACCO_COMMENT | VARCHAR (255) | Free-text comments regarding the patient?s use of tobacco. |
| SMOKING_QUIT_DATE | 19206 | *Partially Deprecated*. The date on which the patient quit smoking in calendar format. The tobacco data model has been updated and new data will no longer be saved to this item. It is recommended to use V_PAT_HX_TOB_USE->TOB_QUIT_DATE instead. |
| CIGARETTES_YN | VARCHAR (1) |  |
| PIPES_YN | VARCHAR (1) |  |
| CIGARS_YN | VARCHAR (1) |  |
| SNUFF_YN | VARCHAR (1) |  |
| CHEW_YN | VARCHAR (1) |  |
| IS_ALCOHOL_USER *(deprecated)* | VARCHAR (10) |  |
| ALCOHOL_OZ_PER_WK | VARCHAR (255) | The fluid ounces of alcohol the patient consumes per week. |
| ALCOHOL_COMMENT | VARCHAR (255) | Free-text comments regarding the patient?s use of alcohol. |
| IS_ILL_DRUG_USER *(deprecated)* | VARCHAR (10) |  |
| IV_DRUG_USER_YN | VARCHAR (1) |  |
| ILLICIT_DRUG_FREQ | VARCHAR (255) | The times per week the patient uses or used illicit drugs. |
| ILLICIT_DRUG_CMT | VARCHAR (255) | Free-text comments regarding the patient?s use of illicit drugs. |
| IS_SEXUALLY_ACTV *(deprecated)* | VARCHAR (15) |  |
| FEMALE_PARTNER_YN | VARCHAR (1) |  |
| MALE_PARTNER_YN | VARCHAR (1) |  |
| CONDOM_YN | VARCHAR (1) |  |
| PILL_YN | VARCHAR (1) |  |
| DIAPHRAGM_YN | VARCHAR (1) |  |
| IUD_YN | VARCHAR (1) |  |
| SURGICAL_YN | VARCHAR (1) |  |
| SPERMICIDE_YN | VARCHAR (1) |  |
| IMPLANT_YN | VARCHAR (1) |  |
| RHYTHM_YN | VARCHAR (1) |  |
| INJECTION_YN | VARCHAR (1) |  |
| SPONGE_YN | VARCHAR (1) |  |
| INSERTS_YN | VARCHAR (1) |  |
| ABSTINENCE_YN | VARCHAR (1) |  |
| SEX_COMMENT | VARCHAR (255) | Free-text comments regarding the patient?s sexual activity. |
| YEARS_EDUCATION | VARCHAR (80) | The number of years of education the patient has completed. Note: This is a free text field. |
| CM_CT_OWNER_ID | VARCHAR (25) | ID of the deployment owner for this contact. |
| PAT_ENC_CSN_ID | NUMERIC (18,0) | A unique serial number for this encounter. This number is unique across all patients and encounters in the system. |
| TOB_SRC_C | INTEGER |  |
| ALCOHOL_SRC_C | INTEGER |  |
| DRUG_SRC_C | INTEGER |  |
| SEX_SRC_C | INTEGER |  |
| HX_LNK_ENC_CSN | NUMERIC (18,0) | The Contact Serial Number of the encounter in which the history was created/edited. If the history was created/edited outside of the context of an encounter, then this column will be blank. |
| ALCOHOL_USE_C | INTEGER |  |
| ILL_DRUG_USER_C | INTEGER |  |
| SEXUALLY_ACTIVE_C | INTEGER |  |
| TOBACCO_USER_C | INTEGER |  |
| SMOKELESS_TOB_USE_C | 19219 | Stores the patient's usage of smokeless tobacco.  Data may include, Current User, Former User, Never Used or Unknown. |
| SMOKELESS_QUIT_DATE | 19216 | The date on which the patient quit using smokeless tobacco. |
| SMOKING_TOB_USE_C | 19218 | Stores the patient's usage of smoking tobacco.  Data may include, Current Everyday Smoker, Current Some Day Smoker, Former Smoker, Never Smoker, Unknown If Ever Smoked or Smoker, Current Status Unknown. |
| UNKNOWN_FAM_HX_YN | VARCHAR (1) |  |
| SMOKING_START_DATE | DATETIME | *Partially Deprecated*. The date on which the patient started smoking in calendar format. The tobacco data model has been updated and new data will no longer be saved to this item. It is recommended to use V_PAT_HX_TOB_USE->TOB_START_DATE instead. |
| EDU_LEVEL_C | INTEGER |  |
| FIN_RESOURCE_STRAIN_C | INTEGER |  |
| IPV_EMOTIONAL_ABUSE_C | INTEGER |  |
| IPV_FEAR_C | INTEGER |  |
| IPV_SEXUAL_ABUSE_C | INTEGER |  |
| IPV_PHYSICAL_ABUSE_C | INTEGER |  |
| ALCOHOL_FREQ_C | INTEGER |  |
| ALCOHOL_DRINKS_PER_DAY_C | INTEGER |  |
| ALCOHOL_BINGE_C | INTEGER |  |
| LIVING_W_SPOUSE_C | INTEGER |  |
| DAILY_STRESS_C | INTEGER |  |
| PHONE_COMMUNICATION_C | INTEGER |  |
| SOCIALIZATION_FREQ_C | INTEGER |  |
| CHURCH_ATTENDANCE_C | INTEGER |  |
| CLUBMTG_ATTENDANCE_C | INTEGER |  |
| CLUB_MEMBER_C | INTEGER |  |
| PHYS_ACT_DAYS_PER_WEEK_C | INTEGER |  |
| PHYS_ACT_MIN_PER_SESS_C | INTEGER |  |
| FOOD_INSECURITY_SCARCE_C | INTEGER |  |
| FOOD_INSECURITY_WORRY_C | INTEGER |  |
| MED_TRANSPORT_NEEDS_C | INTEGER |  |
| OTHER_TRANSPORT_NEEDS_C | INTEGER |  |
| SOC_PHONE_SRC_C | INTEGER |  |
| SOC_TOGETHER_SRC_C | INTEGER |  |
| SOC_CHURCH_SRC_C | INTEGER |  |
| SOC_MEETINGS_SRC_C | INTEGER |  |
| SOC_MEMBER_SRC_C | INTEGER |  |
| SOC_LIVING_SRC_C | INTEGER |  |
| PHYS_DPW_SRC_C | INTEGER |  |
| PHYS_MPS_SRC_C | INTEGER |  |
| STRESS_SRC_C | INTEGER |  |
| EDUCATION_SRC_C | INTEGER |  |
| FINANCIAL_SRC_C | INTEGER |  |
| IPV_EMOTIONAL_SRC_C | INTEGER |  |
| IPV_FEAR_SRC_C | INTEGER |  |
| IPV_SEXABUSE_SRC_C | INTEGER |  |
| IPV_PHYSABUSE_SRC_C | INTEGER |  |
| ALC_FREQ_SRC_C | INTEGER |  |
| ALC_STD_DRINK_SRC_C | INTEGER |  |
| ALC_BINGE_SRC_C | INTEGER |  |
| FOOD_WORRY_SRC_C | INTEGER |  |
| FOOD_SCARCITY_SRC_C | INTEGER |  |
| TRANS_MED_SRC_C | INTEGER |  |
| TRANS_NONMED_SRC_C | INTEGER |  |
| FAM_PAT_ADPT_PAR_1 | INTEGER | Stores the family history ID of the patient's adoptive parent. A patient can have two adoptive parents. The ID of the other parent is in FAM_PAT_ADPT_PAR_2. |
| FAM_PAT_ADPT_PAR_2 | INTEGER | Stores the family history ID of the patient's adoptive parent. A patient can have two adoptive parents. The ID of the other parent is in FAM_PAT_ADPT_PAR_1. |
| TOB_HX_ADDL_PACKYEARS | NUMERIC (18,2) | Number to add to the total number of pack years calculated for the patient's tobacco history. |
| TOB_HX_SMOKE_EXPOSURE_CMT | VARCHAR (255) | Store the comment for passive tobacco smoke exposure. |
| PASSIVE_SMOKE_EXPOSURE_C | INTEGER |  |
| FAMHX_PAT_IS_ADOPTED_C | INTEGER |  |
| TOBACCO_PCK_YRS_OLD | NUMERIC (18,2) | Virtual item for smoking tobacco pack year calculation using recorded values for packs per day, years smoked, and additional pack years. |
| TOBACCO_CUR_PPD | NUMERIC (18,2) | Virtual item for current tobacco packs per day which is deteremined by the current usage line in tobacco overtime documentation. If tobacco overtime documentation is not set will fall back to packs per day. |
| AVERAGE_PPD | NUMERIC (18,2) | Holds the average packs per day a patient has smoked from their earliest start date to their latest quit date. |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| B-TREE INDEX | EIX_SOCIAL_HXENC | PAT_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_SOCIAL_HXENC | PAT_ENC_DATE_REAL | 2 | Yes | Yes |  |
| B-TREE INDEX | EIX_SOC_DT_TOBACCO | CONTACT_DATE | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_SOC_DT_TOBACCO | TOBACCO_USER_C | 2 | Yes | Yes |  |
| B-TREE INDEX | EIX_SOC_DT_TOB_USE | PAT_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_SOC_DT_TOB_USE | CONTACT_DATE | 2 | Yes | Yes |  |
| B-TREE INDEX | EIX_SOC_DT_TOB_USE | SMOKING_TOB_USE_C | 3 | Yes | Yes |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | PAT_ID | ANTICOAG_SELF_REGULATING | PAT_ID | No | No | No |  |
| 1 | PAT_ID | CARE_COORDINATION | PAT_ID | Unknown | No | No |  |
| 1 | PAT_ID | CLAIMS_DERIVE_PAT_FLAGS | PAT_ID | No | No | No |  |
| 1 | PAT_ID | COMMUNITY_RESRC_REVIEWED | PAT_ID | No | No | No |  |
| 1 | PAT_ID | D_PAT_GEOGRAPHIC_CLASS | PAT_ID | Unknown | Unknown | No |  |
| 1 | PAT_ID | EPT_MEM_INFO | PAT_ID | No | No | No |  |
| 1 | PAT_ID | EXT_DATA_LAST_DONE | PAT_ID | No | No | No |  |
| 1 | PAT_ID | F_IBD_ADULT_FORM_PAT | PAT_ID | Unknown | Unknown | No |  |
| 1 | PAT_ID | HH_PAT_INFO | PAT_ID | Unknown | No | No |  |
| 1 | PAT_ID | HM_STATUS_UPD | PAT_ID | No | No | No |  |
| 1 | PAT_ID | IMMNZTN_LAST_REVIEW | PAT_ID | No | No | No |  |
| 1 | PAT_ID | PATIENT | PAT_ID | No | No | No |  |
| 1 | PAT_ID | PATIENT_2 | PAT_ID | No | No | No |  |
| 1 | PAT_ID | PATIENT_3 | PAT_ID | No | No | No |  |
| 1 | PAT_ID | PATIENT_4 | PAT_ID | No | No | No |  |
| 1 | PAT_ID | PATIENT_5 | PAT_ID | No | No | No |  |
| 1 | PAT_ID | PATIENT_6 | PAT_ID | No | No | No |  |
| 1 | PAT_ID | PATIENT_CONF_ADDR | PAT_ID | No | No | No |  |
| 1 | PAT_ID | PATIENT_MISC_COMMENTS | PAT_ID | No | No | No |  |
| 1 | PAT_ID | PATIENT_MYC | PAT_ID | Unknown | No | No |  |
| 1 | PAT_ID | PATIENT_OPT | PAT_ID | No | No | No |  |
| 1 | PAT_ID | PAT_ENC_LAST_HX_CT | PAT_ID | Unknown | Unknown | No |  |
| 1 | PAT_ID | PAT_RES_CODE | PAT_ID | No | No | No |  |
| 1 | PAT_ID | PROB_LIST_REVIEWED | PAT_ID | No | No | No |  |
| 1 | PAT_ID | REGADDL_PAT | PAT_ID | No | No | No |  |
| 1 | PAT_ID | SCF_FHIR_MAP | PAT_ID | No | No | No |  |
| 1 | PAT_ID | TEETH_REVIEWED | PAT_ID | No | No | No |  |
| 1 | PAT_ID | VALID_PATIENT | PAT_ID | No | No | No |  |
| 1 | PAT_ID | V_PAT_ABO | PAT_ID | Unknown | Unknown | No |  |
| 1 | PAT_ID | V_PAT_FACT | PAT_ID | Unknown | Unknown | No |  |

_(331 total; showing first 30)_
