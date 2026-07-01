# DM_WLL_ALL

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=DM_WLL_ALL

## Description

DM_WLL_ALL is a data mart table that stores information related to general patient health. This table consolidates patient information from many subject areas including lab values, encounters, vitals, medications, diagnoses, social history, and risk scores. If the patient is not deceased, then he/she is included in this wellness registry.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | RDT |
| Release Version | Rel 2015 |
| May contain EHI? | No |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| RECORD_ID | NUMERIC (18,0) | The unique identifier (.1 item) for the registry data record. |
| REGISTRY_STATUS_C | INTEGER |  |
| PAT_ID | VARCHAR (18) | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| NUM_ED_VIS | NUMERIC (18,0) | The total number of emergency department (ED) visits for a patient.  Rule: DM Encounter Number Of ED Visits (82040) |
| NUM_HOSP_ADMSNS | NUMERIC (18,0) | The total number of times the patient was admitted to a hospital.  Rule: DM Encounter Number Of Hospital Admissions (82031) |
| AGE | FLOAT | Age of the patient.  Rule: DM General Age (82005) |
| CUR_PCP_PROV_ID | VARCHAR (18) | The unique ID of the patient's primary care physician.  Rule: DM General Current PCP (82000) |
| DATE_OF_BIRTH | DATETIME | The patient's date of birth (EPT 110).   Rule: DM General Date of Birth (19828) |
| HAS_MEDICAID_COVERAGE_YN | VARCHAR (1) | Indicates if any of the patient's effective coverages is Medicaid.  Rule: DM General Has Medicaid Coverage (84422) |
| IS_ADULT_YN | VARCHAR (1) | Indicates if the patient's age in years is greater than or equal to the configured threshold (the default is 18).  Rule: DM General Is Adult (84423) |
| SEX_C | VARCHAR (66) | Sex of the patient.  Rule: DM General Sex (82006) |
| CUR_PRIM_BEN_PLAN_ID | NUMERIC (18,0) | The unique ID of the patient's primary benefit plan.  Rule: Primary Benefit Plan (19239) |
| CUR_PRIM_PAYER_ID | NUMERIC (18,0) | The unique ID of the patient's primary payer.  Rule: Primary Payer (19238) |
| CUR_PRIM_FIN_CLASS_C | VARCHAR (66) | The category value of the financial class of the patient's primary payer.  Rule: Primary Payer's Financial Class (19240) |
| CUR_PRIM_PROD_TYPE_C | VARCHAR (66) | The category value of the product type of the patient's primary payer.  Rule: Primary Payer's Product Type (19241) |
| NONHISP_AFRICAN_AMER_YN | VARCHAR (1) | Indicates if the patient is a non-Hispanic African American.  Rule: DM General Is Patient A Non-Hispanic African American (19532) |
| OFF_VIS_LAST_DT | DATETIME | Date of the patient's last office visit.  Rule: DM Encounter Last Office Visit Date (82027) |
| BMI_LAST | FLOAT | The patient's most recent body mass index.  Rule: DM Vitals Last BMI (82108) |
| BMI_LAST_DT | DATETIME | The date the patient's most recent body mass index was recorded.  Rule: DM Vitals Last BMI (82108) |
| BMI_LAST_PCT | FLOAT | The patient's last recorded BMI percentile in a given time period. By default, the rule only looks at height and weight measurements dated within the last year.  Rule: DM Vitals Last BMI Percentile (82115) |
| BMI_LAST_PCT_DT | DATETIME | The date the patient's last BMI percentile in a given time period was recorded. By default, the rule only looks at height and weight measurements dated within the last year.  Rule: DM Vitals Last BMI Percentile (82115) |
| BP_DIA_LAST | FLOAT | The patient's most recent diastolic blood pressure.  Rule: DM Vitals Last Diastolic BP (82104) |
| BP_DIA_LAST_DT | DATETIME | The date the patient's most recent diastolic blood pressure was recorded.  Rule: DM Vitals Last Diastolic BP (82104) |
| BP_SYS_LAST | FLOAT | The patient's most recent systolic blood pressure.  Rule: DM Vitals Last Systolic BP (82103) |
| BP_SYS_LAST_DT | DATETIME | The date the patient's most recent systolic blood pressure was recorded.  Rule: DM Vitals Last Systolic BP (82103) |
| SMOKING_USER_YN | VARCHAR (1) | Indicates whether the patient is currently identified as a tobacco smoker.  Rule: DM History Is Currently a Tobacco Smoker (82164) |
| TOBAC_PACK_YEAR | NUMERIC (18,2) | The most recently reported tobacco pack years for the patient. Pack years are calculated from the latest encounter containing a value for tobacco consumed in packs/day and the number of years a patient smoked.  Rule: DM History Last Pack Years (82158) |
| SMOKELESS_STATUS_C | INTEGER | The category value of the patient's last recorded smokeless tobacco use status.  Datasource: I EPT 19219  Rule: DM History Last Smokeless Tobacco Use Status (19188) |
| SMOKING_STATUS_C | INTEGER | The category value of the patient's last recorded smoking tobacco use status.  Datasource: I EPT 19208  Rule: DM History Last Smoking Tobacco Use Status (82153) |
| TOBAC_QUIT_LAST_DT | DATETIME | It is recommended that you use SMOKING_QUIT_L_DT for Meaningful Use.  Contains the patient's most recently recorded tobacco quit date if the patient has previously quit using tobacco and does not currently use tobacco.  Rule: DM History Last Tobacco Quit Date (82155) |
| SEXUALLY_ACTIVE_YN | VARCHAR (1) | Indicates whether the patient is sexually active.   Rule: DM Is Patient Sexually Active (19817) |
| CAD_RISK_FACTORS_YN | VARCHAR (1) | Indicates whether the patient is at risk for coronary artery disease (CAD). Returns null if the patient is missing documentation necessary to determine risk.  Rule: DM Score Does Patient Have CAD Risk Factors (19823) |
| CHLAMYDIA_RISK_ASSESSMENT_YN | VARCHAR (1) | Indicates whether the patient is at risk for chlamydia. Returns null if the patient has not been assessed.  Rule: DM SDE Chlamydia Risk Assessment (19818) |
| HEP_C_RISK_ASSESSMENT_YN | VARCHAR (1) | Indicates whether the patient is at risk for hepatitis C virus (HCV). Returns null if the patient has not been assessed.  Rule: DM SDE HCV Risk Assessment (19829) |
| HIV_RISK_ASSESSMENT_YN | VARCHAR (1) | Indicates whether the patient is at risk for human immunodeficiency virus (HIV). Returns null if the patient has not been assessed.  Rule: DM SDE HIV Risk Assessment (19821) |
| HAD_HEART_ATTACK_YN | VARCHAR (1) | Indicates whether a patient has had a heart attack.  Rule: DM Diagnosis Did Patient Have Heart Attack (82542) |
| HAD_STROKE_YN | VARCHAR (1) | Indicates whether the patient has had a stroke.  Rule: DM Diagnosis Did Patient Have Stroke (82488) |
| PRIOR_ASCVD_EVENT_YN | VARCHAR (1) | Indicates whether or not the patient has had a prior Atherosclerotic Cardiovascular Disease (ASCVD) event. ASCVD events are defined as myocardial infarction, CHD death, or stroke.  Rule: DM Score Diagnosis Prior ASCVD Event (19534) |
| HDL_LAST | FLOAT | The patient's most recent high-density lipoprotein (HDL) value. Only numeric lab values are stored in this column. Non-numeric lab values entered are displayed as null.  Rule: DM Lab Last HDL (82202) |
| HDL_LAST_DT | DATETIME | The date as per the prioritized instant of the patient's most recent high-density lipoprotein (HDL) lab.   Rule: DM Lab Last HDL (82202) |
| HDL_L_ORD_ID | NUMERIC (18,0) | The unique ID of the procedure order associated with the patient's most recent high-density lipoprotein (HDL) value.   Rule: DM Lab Last HDL (82202) |
| HDL_L_LRR_ID | NUMERIC (18,0) | The unique ID of the component associated with the patient's most recent high-density lipoprotein (HDL) value.   Rule: DM Lab Last HDL (82202) |
| HDL_L_UNIT | VARCHAR (100) | The unit of the patient's most recent high-density lipoprotein (HDL) value.  Rule: DM Lab Last HDL (82202) |
| TTL_CHL_LAST | FLOAT | The patient's most recent total cholesterol value.  Only numeric lab values are stored in this column.  Non-numeric lab values entered are displayed as null.  Rule: DM Lab Last Total Cholesterol (82205) |
| TTL_CHL_LAST_DT | DATETIME | The date as per the prioritized instant of the patient's most recent total cholesterol lab.  Rule: DM Lab Last Total Cholesterol (82205) |
| TTL_CHL_L_ORD_ID | NUMERIC (18,0) | The unique ID of the procedure order associated with the patient's most recent total cholesterol value.    Rule: DM Lab Last Total Cholesterol (82205) |
| TTL_CHL_L_LRR_ID | NUMERIC (18,0) | The unique ID of the component associated with the patient's most recent total cholesterol value.   Rule: DM Lab Last Total Cholesterol (82205) |
| TTL_CHL_L_UNIT | VARCHAR (100) | The unit of the patient's most recent total cholesterol value.  Rule: DM Lab Last Total Cholesterol (82205) |
| ABDOM_AORTIC_ANEURYSM_SCRN_DT | DATETIME | The date the last abdominal aortic aneurysm screening was performed.   Rule: DM Result Last Abdominal Aortic Aneurysm Screening Date (19826) |
| CHLAMYDIA_SCRN_DT | DATETIME | The date the last chlamydia screening was performed.   Rule: DM Result Last Chlamydia Screening Date (82799) |
| COLONOSCOPY_DT | DATETIME | The date the last colonoscopy was performed.   Rule: DM Result Last Colonoscopy Date (82798) |
| DIABETES_SCRN_DT | DATETIME | The date the last diabetes screening was performed.   Rule: DM Result Last Diabetes Screening Date (82803) |
| FECAL_OCCULT_BLOOD_DT | DATETIME | The date the last fecal occult blood test was performed.   Rule: DM Result Last Fecal Occult Blood Date (82795) |
| HEP_C_SCRN_DT | DATETIME | The date the last hepatitis C virus (HCV) screening was performed.   Rule: DM Result Last Hepatitis C Virus Screening Date (19830) |
| HIV_SCRN_DT | DATETIME | The date the last HIV screening was performed.   Rule: DM Result Last HIV Screening Date (82802) |
| HPV_SCRN_DT | DATETIME | The date the last human papillomavirus (HPV) screening was performed.   Rule: DM RESULT LAST HPV SCREENING DATE (19840) |
| LIPID_PROFILE_DT | DATETIME | The date the last lipid panel was performed.   Rule: DM LAB LAST LIPID PANEL SERVICE DATE (82800) |
| LUNG_CANCER_SCRN_DT | DATETIME | The date the last lung cancer screening was performed.  Rule: DM Result Last Lung Cancer Screening Date (19832) |
| MAMMOGRAM_DT | DATETIME | The date the last mammogram was performed.   Rule: DM Result Last Mammogram Date (82796) |
| OSTEOPOROSIS_SCRN_DT | DATETIME | The date the last osteoporosis screening was performed.  Rule: DM Result Last Osteoporosis Screening Date (19836) |
| PAP_SMEAR_DT | DATETIME | The date the last pap smear was performed.   Rule: DM Result Last Pap Smear Date (82784) |
| SIGMOIDOSCOPY_DT | DATETIME | The date the last sigmoidoscopy was performed.   Rule: DM Result Last Sigmoidoscopy Date (82797) |
| VISUAL_IMPAIRMENT_SCRN_DT | DATETIME | The date the last visual impairment screening was performed.   Rule: DM Result Last Visual Impairment Screening Date (19837) |
| ON_ANTHYPERT_YN | VARCHAR (1) | Indicates whether an antihypertensive medication is on the patient's current medication list.  Rule: DM Med Is Prescribed Antihypertensives (82376) |
| HAS_ABDOM_AORTIC_ANEURYSM_YN | VARCHAR (1) | Indicates whether the patient has an abdominal aortic aneurysm (AAA).  Rule: DM Diagnosis Does Patient Have Abdominal Aortic Aneurysm (19825) |
| HAS_BREAST_CANCER_YN | VARCHAR (1) | Indicates whether the patient has breast cancer.  Rule: DM Diagnosis Does Patient Have Breast Cancer (19827) |
| HAS_CERVI_CARCI_YN | VARCHAR (1) | Indicates whether the patient has cervical cell carcinoma.  Rule: DM Diagnosis Does Patient Have Cervical Cell Carcinoma (82541) |
| HAS_CHLAMYDIA_YN | VARCHAR (1) | Indicates whether the patient has chlamydia.  Rule: DM Diagnosis Does Patient Have Chlamydia (19816) |
| HAS_COPD_YN | VARCHAR (1) | Indicates whether the patient has COPD.   Rule: DM Diagnosis Does Patient Have Chronic Obstructive Pulmonary Disease (84421) |
| HAS_COLORECTAL_CANCER_YN | VARCHAR (1) | Indicates whether the patient has colorectal cancer.  Rule: DM Diagnosis Does Patient Have Colorectal Cancer (19820) |
| HAS_CHF_YN | VARCHAR (1) | Indicates whether the patient has congestive heart failure (CHF).  Rule: DM Diagnosis Does Patient Have Congestive Heart Failure (82495) |
| HAS_DEPRESSION_YN | VARCHAR (1) | Indicates whether the patient has depression.  Rule: DM Diagnosis Does Patient Have Depression (82504) |
| HAS_DIABETES_YN | VARCHAR (1) | Indicates whether the patient has diabetes.  Rule: DM Diagnosis Does Patient Have Diabetes (82479) |
| HAS_HEP_C_YN | VARCHAR (1) | Indicates whether the patient has hepatitis C.  Rule: DM Diagnosis Does Patient Have Hepatitis C (82522) |
| HAS_HIV_YN | VARCHAR (1) | Indicates whether the patient has human immunodeficiency virus (HIV).  Rule: DM Diagnosis Does Patient Have HIV (19815) |
| HAS_LIPID_DISORDER_YN | VARCHAR (1) | Indicates whether the patient has lipid disorders.  Rule: DM Diagnosis Does Patient Have Lipid Disorders (19822) |
| HAS_LIVER_DIS_YN | VARCHAR (1) | Indicates whether the patient has liver disease.  Rule: DM Diagnosis Does Patient Have Liver Disease (82544) |
| HAS_LUNG_CANCER_YN | VARCHAR (1) | Indicates whether the patient has lung cancer.  Rule: DM Diagnosis Does Patient Have Lung Cancer (19831) |
| HAS_OSTEOPOROSIS_YN | VARCHAR (1) | Indicates whether the patient has osteoporosis.  Rule: DM Diagnosis Does Patient Have Osteoporosis (19834) |
| HAS_PRECANC_CERV_LESION_YN | VARCHAR (1) | Indicates whether the patient has a precancerous cervical lesion.  Rule: DM Does Patient Have Precancerous Cervical Lesion (19813) |
| HAS_TYP_2_DIABETES_YN | VARCHAR (1) | Indicates whether the patient has type 2 diabetes.  Rule: DM Diagnosis Does Patient Have Type 2 Diabetes (84126) |
| HAD_UTERO_EXP_DIETHYL_YN | VARCHAR (1) | Indicates whether the patient has had in utero exposure to diethylstilbestrol.  Rule: DM Diagnosis Has Patient Had In Utero Exposure To Diethylstilbestrol (19814) |
| HAD_COLECTOMY_YN | VARCHAR (1) | Indicates whether the patient has had a colectomy by checking health maintenance modifiers and surgical history.  Rule: DM General Had Colectomy (19841) |
| HAD_HYSTERECTOMY_YN | VARCHAR (1) | Indicates whether the patient has had a hysterectomy.   Rule: DM General Had Hysterectomy (19839) |
| PREV_CARE_SC_ABD_AORTIC_ANEUR | FLOAT | The abdominal aortic aneurysm (AAA) component of the preventive care gap score. The AAA score ranges from 0-1, with lower values preferred.  Rule: DM Score Preventive Care Abdominal Aortic Aneurysm (19939) |
| PREV_CARE_SC_ABD_AOR_ANEUR_CMT | VARCHAR (254) | Comment to help explain the preventive care abdominal aortic aneurysm component.  Data Source: ECT 55510  Rule: DM Score Preventive Care Abdominal Aortic Aneurysm (19939) |
| PREV_CARE_SC_BREAST_CANCER | FLOAT | The breast cancer component of the preventive care gap score. The breast cancer score ranges from 0-1, with lower values preferred.   Rule: DM Score Preventive Care Breast Cancer (19942) |
| PREV_CARE_SC_BREAST_CANCER_CMT | VARCHAR (254) | Comment to help explain the preventive care breast cancer component.  Data Source: ECT 55510  Rule: DM Score Preventive Care Breast Cancer (19942) |
| PREV_CARE_SC_CERV_CANCER | FLOAT | The cervical cancer component of the preventive care gap score. The cervical cancer score ranges from 0-1, with lower values preferred.   Rule: DM Score Preventive Care Cervical Cancer (19921) |
| PREV_CARE_SC_CERV_CANCER_CMT | VARCHAR (254) | Comment to help explain the preventive care cervical cancer component.  Data Source: ECT 55510  Rule: DM Score Preventive Care Cervical Cancer (19921) |
| PREV_CARE_SC_CHLAMYDIA | FLOAT | The chlamydia component of the preventive care gap score. The chlamydia score ranges from 0-1, with lower values preferred.   Rule: DM Score Preventive Care Chlamydia (19924) |
| PREV_CARE_SC_CHLAMYDIA_CMT | VARCHAR (254) | Comment to help explain the preventive care chlamydia component.  Data Source: ECT 55510  Rule: DM Score Preventive Care Chlamydia (19924) |
| PREV_CARE_SC_COLORECTAL_CANCER | FLOAT | The colorectal cancer component of the preventive care gap score. The colorectal cancer score ranges from 0-1, with lower values preferred.   Rule: DM Score Preventive Care Colorectal Cancer (19927) |
| PREV_CARE_SC_COLORECT_CAN_CMT | VARCHAR (254) | Comment to help explain the preventive care colorectal cancer component.  Data Source: ECT 55510  Rule: DM Score Preventive Care Colorectal Cancer (19927) |
| PREV_CARE_GAP_SCORE | FLOAT | The preventive care gap score for a patient. This score is a count of the number of care gaps that a patient has; a lower score means fewer care gaps and is preferred. The maximum score varies based on the patient's age and sex.  Rule: DM Score Preventive Care Gap (19920) |
| PREV_CARE_GAP_SC_MISSING_C | INTEGER | Category value to explain why the patient's preventive care gap score is missing. "1" indicates the patient is not eligible. "2" indicates the patient's score is missing components. "3" indicates that the patient's score is invalid.  Rule: DM Score Preventive Care Gap (19920) |
| PREV_CARE_SC_HEP_C | FLOAT | The hepatitis C virus (HCV) component of the preventive care gap score. The HCV score ranges from 0-1, with lower values preferred.   Rule: DM Score Preventive Care Hepatitis C Virus Infection (19945) |
| PREV_CARE_SC_HEP_C_CMT | VARCHAR (254) | Comment to help explain the preventive care hepatitis C virus infection component.  Data Source: ECT 55510  Rule: DM Score Preventive Care Hepatitis C Virus Infection (19945) |
| PREV_CARE_SC_HIGH_BP | FLOAT | The high blood pressure component of the preventive care gap score. The high blood pressure score ranges from 0-1, with lower values preferred.   Rule: DM Score Preventive Care High BP (19933) |
| PREV_CARE_SC_HIGH_BP_CMT | VARCHAR (254) | Comment to help explain the preventive care high blood pressure component.  Data Source: ECT 55510  Rule: DM Score Preventive Care High BP (19933) |
| PREV_CARE_SC_HIV | FLOAT | The human immunodeficiency virus (HIV) component of the preventive care gap score. The HIV score ranges from 0-1, with lower values preferred.   Rule: DM Score Preventive Care HIV (19930) |
| PREV_CARE_SC_HIV_CMT | VARCHAR (254) | Comment to help explain the preventive care HIV component.  Data Source: ECT 55510  Rule: DM Score Preventive Care HIV (19930) |
| PREV_CARE_SC_LIPID_DISORDERS | FLOAT | The lipid disorders component of the preventive care gap score. The lipid disorders score ranges from 0-1, with lower values preferred.   Rule: DM Score Preventive Care Lipid Disorders (19936) |
| PREV_CARE_SC_LIPID_DISORDS_CMT | VARCHAR (254) | Comment to help explain the preventive care lipid disorders component.  Data Source: ECT 55510  Rule: DM Score Preventive Care Lipid Disorders (19936) |
| PREV_CARE_SC_LUNG_CANCER | FLOAT | The lung cancer component of the preventive care gap score. The lung cancer score ranges from 0-1, with lower values preferred.   Rule: DM Score Preventive Care Lung Cancer (19948) |
| PREV_CARE_SC_LUNG_CANCER_CMT | VARCHAR (254) | Comment to help explain the preventive care lung cancer component.  Data Source: ECT 55510  Rule: DM Score Preventive Care Lung Cancer (19948) |
| PREV_CARE_SC_OBESITY | FLOAT | The obesity component of the preventive care gap score. The obesity score ranges from 0-1, with lower values preferred.  Rule: DM Score Preventive Care Obesity (19951) |
| PREV_CARE_SC_OBESITY_CMT | VARCHAR (254) | Comment to help explain the preventive care obesity component.  Data Source: ECT 55510  Rule: DM Score Preventive Care Obesity (19951) |
| PREV_CARE_SC_OSTEOPOROSIS | FLOAT | The osteoporosis component of the preventive care gap score. The osteoporosis score ranges from 0-1, with lower values preferred.  Rule: DM Score Preventive Care Osteoporosis (19954) |
| PREV_CARE_SC_OSTEOPOROSIS_CMT | VARCHAR (254) | Comment to help explain the preventive care osteoporosis component.  Data Source: ECT 55510  Rule: DM Score Preventive Care Osteoporosis (19954) |
| PREV_CARE_SC_TYP_2_DIABETES | FLOAT | The type 2 diabetes mellitus component of the preventive care gap score. The type 2 diabetes score ranges from 0-1, with lower values preferred.  Rule: DM Score Preventive Care Type 2 Diabetes Mellitus (19957) |
| PREV_CARE_SC_TYP_2_DIAB_CMT | VARCHAR (254) | Comment to help explain the preventive care type 2 diabetes component.  Data Source: ECT 55510  Rule: DM Score Preventive Care Type 2 Diabetes Mellitus (19957) |
| PREV_CARE_SC_VISUAL_IMPAIR | FLOAT | The visual impairment component of the preventive care gap score. The visual impairment score ranges from 0-1, with lower values preferred.  Rule: DM Score Preventive Care Visual Impairment (19960) |
| PREV_CARE_SC_VISUAL_IMPAIR_CMT | VARCHAR (254) | Comment to help explain the preventive care visual impairment component.  Data Source: ECT 55510  Rule: DM Score Preventive Care Visual Impairment (19960) |
| PREV_CARE_SC_OBESITY_INTERV | FLOAT | The obesity intervention component of the preventive care gap score. The obesity intervention score ranges from 0-1, with lower values preferred.  Rule: DM Score Preventive Care Obesity Intervention (19963) |
| PREV_CARE_SC_OBES_INTERV_CMT | VARCHAR (254) | Comment to help explain the preventive care obesity intervention component.  Data Source: ECT 55510  Rule: DM Score Preventive Care Obesity Intervention (19963) |
| GEN_ADULT_SCORE | FLOAT | The current general risk score for an adult patient on a wellness registry. Patients under 18 years old will not be evaluated.  Rule: DM Score General Risk Adult (84410) |
| GEN_ADULT_SC_MISSING_C | INTEGER | Category value to explain why the patient's general risk score is missing. "1" indicates the patient is not eligible. "2" indicates the patient's risk score is missing components. "3" indicates that the patient's risk score is invalid. Patients under 18 years old will not be evaluated.  Rule: DM Score General Risk Adult (84410) |
| GEN_ADULT_SC_AGE | INTEGER | The age component of the general risk score.  Rule: DM Score General Risk Adult Age (84411) |
| GEN_ADULT_SC_ED_VISITS | INTEGER | The ED visits component of the general risk score.  Rule: DM Score General Risk Adult ED Visits (84413) |
| GEN_ADULT_SC_CHF | INTEGER | The CHF component of the general risk score.  Rule: DM Score General Risk Adult Has CHF (84416) |
| GEN_ADULT_SC_CHRON_LIVER_DIS | INTEGER | The chronic liver disease component of the general risk score.  Rule: DM Score General Risk Adult Has Chronic Liver Disease (84417) |
| GEN_ADULT_SC_COPD | INTEGER | The COPD component of the general risk score.  Rule: DM Score General Risk Adult Has COPD (84414) |
| GEN_ADULT_SC_DEPRESSION | INTEGER | The depression component of the general risk score.  Rule: DM Score General Risk Adult Has Depression (84418) |
| GEN_ADULT_SC_DIABETES | INTEGER | The diabetes component of the general risk score.  Rule: DM Score General Risk Adult Has Diabetes(84415) |
| GEN_ADULT_SC_MEDICAID | INTEGER | The Medicaid component of the general risk score.  Rule: DM Score General Risk Adult Has Medicaid (84420) |
| GEN_ADULT_SC_PCP | INTEGER | The PCP component of the general risk score.  Rule: DM Score General Risk Adult Has PCP (84419) |
| GEN_ADULT_SC_HOSP_ADMSNS | INTEGER | The acute admissions component of the general risk score.  Rule: DM Score General Risk Adult Hospital Admissions (84412) |
| FRACTURE_RISK_ASSESSMENT_YN | VARCHAR (1) | Indicates whether the patient is at risk for fracture. Returns null if the patient has not been assessed.  Rule: DM SDE Fracture Risk Assessment (19835) |
| LOW_LIFE_EXP_YN | VARCHAR (1) | Indicates whether the patient has a low life expectancy.  Rule: DM SDE Low Life Expectancy (19843) |
| MAMMO_EXCL_YN | VARCHAR (1) | Indicates whether the patient has had a mammogram performed for medical reasons.  Rule: DM SDE Mammogram Exclusion (19844) |
| OBESITY_FOL_UP_PLAN_YN | VARCHAR (1) | Indicates whether a patient has an obesity follow-up plan.  Rule: DM SDE Obesity Follow-Up Plan (19833) |
| OSTEO_SCRN_EXCL_YN | VARCHAR (1) | Indicates whether a patient is eligible for an osteoporosis screening exclusion.  Rule: DM SDE Osteoporosis Screening Exclusion (19842) |
| CVD_10_YR_SCORE | FLOAT | The 10-year percentage risk of developing a first Cardiovascular Disease (CVD) event. CVD events are defined as myocardial infarction, CHF, stroke, or peripheral vascular disease.  Rule: DM Score 10-Year CVD Risk (19000) |
| CVD_10_YR_SC_MISSING_C | INTEGER | Category value to explain why the patient's CVD 10-year score is missing. "1" indicates the patient is not eligible. "2" indicates the patient's risk score is missing components. "3" indicates that the patient's risk score is invalid.  Rule: DM Score 10-Year CVD Risk (19000) |
| ASCVD_10_YR_SCORE | FLOAT | The estimated risk of having an atherosclerotic cardiovascular disease (ASCVD) event in the next 10 years, displayed as a percentage. ASCVD events are defined as myocardial infarction, CHD death, or stroke.  Rule: DM Score 10-Year ASCVD Risk (19535) |
| ASCVD_10_YR_SC_MISSING_C | INTEGER | Category value to explain why the patient's ASCVD 10-year score is missing. "1" indicates the patient is not eligible. "2" indicates the patient's risk score is missing components. "3" indicates that the patient's risk score is invalid.  Rule: DM Score 10-Year ASCVD Risk (19535) |
| PRIOR_CVD_EVENT_YN | VARCHAR (1) | Indicates whether or not the patient has had a prior Cardiovascular Disease (CVD) event. CVD events are defined as stroke, myocardial infarction, CHF, or peripheral vascular disease.  Rule: DM Score Diagnosis Prior CVD Event (19001) |
| HAS_PERIPH_VASC_DIS_YN | VARCHAR (1) | Indicates whether the patient has peripheral vascular disease.  Rule: DM Diagnosis Does Patient Have Peripheral Vascular Disease (82493) |
| HAS_HYPERTENSION_YN | VARCHAR (1) | Indicates whether the patient has hypertension.  Rule: DM Diagnosis Does Patient Have Hypertension (82490) |
| HAS_OBESITY_YN | VARCHAR (1) | Indicates whether the patient has obesity.  Rule: DM Diagnosis Does Patient Have Obesity (84123) |
| HAS_CAD_YN | VARCHAR (1) | Indicates whether the patient has CAD.  Rule: DM Diagnosis Does Patient Have Coronary Artery Disease (82476) |
| HAS_NON_CAD_ATHERO_YN | VARCHAR (1) | Indicates whether the patient has non-CAD atherosclerosis.  Rule: DM Diagnosis Does Patient Have Non-CAD Atherosclerosis (82676) |
| HIST_CAD_YN | VARCHAR (1) | Indicates whether the patient has CAD in their medical history.  Rule: DM History Is CAD In Medical History (82178) |
| HIST_NON_CAD_ATHERO_YN | VARCHAR (1) | Indicates whether the patient has non-CAD atherosclerosis in their medical history.  Rule: DM History Is Non-CAD Atherosclerosis In Medical History (82179) |
| FAM_HIST_CVD_YN | VARCHAR (1) | Indicates whether the patient has a family history of cardiovascular disease.  Rule: DM History Does Patient Have Family History Of Cardiovascular Disease (82177) |
| USES_ANY_TOBAC_YN | VARCHAR (1) | Indicates whether the patient is using any kind of tobacco.  Rule: DM History Does Patient Use Any Kind Of Tobacco (82176) |
| HAS_ASTHMA_YN | VARCHAR (1) | Indicates whether the patient has asthma.  Rule: DM Diagnosis Does Patient Have Asthma (82571) |
| HAS_ANEMIA_YN | VARCHAR (1) | Indicates whether the patient has anemia.  Rule: DM Diagnosis Does Patient Have Anemia (82481) |
| HAS_AFIB_YN | VARCHAR (1) | Indicates whether the patient has atrial fibrillation.  Rule: DM Diagnosis Does Patient Have Atrial Fibrillation (82598) |
| HAS_CVD_YN | VARCHAR (1) | Indicates whether the patient has cardiovascular disease.  Rule: DM Diagnosis Does Patient Have Cardiovascular Disease (19047) |
| HAS_CKD_YN | VARCHAR (1) | Indicates whether the patient has chronic kidney disease.  Rule: DM Diagnosis Does Patient Have Chronic Kidney Disease (82511) |
| HAS_CONNECT_TISSUE_DISORDER_YN | VARCHAR (1) | Indicates whether the patient has a connective tissue disorder.  Rule: DM Diagnosis Does Patient Have A Connective Tissue Disorder (82305) |
| HAS_MEDICARE_COVERAGE_YN | VARCHAR (1) | Indicates if any of the patient's effective coverages is Medicare.  Rule: DM General Has Medicare Coverage (82303) |
| IS_IN_RELATIONSHIP_YN | VARCHAR (1) | Indicates whether the patient is in a relationship.  Rule: DM General Is In Relationship (82306) |
| HOSP_OR_ED_RISK_SCORE | FLOAT | The 1-year risk of a hospital admission or ED visit for an adult patient, displayed as a percentage. If the score definition has not been clinically reviewed, the column will return null.  Rule: DM Score Risk Of Hospital Admission Or ED Visit (82307) |
| HOSP_OR_ED_RISK_SC_MISSING_C | INTEGER | Category value to explain why the patient's hospital admission or ED visit risk score is missing.  Rule: DM Score Risk Of Hospital Admission Or ED Visit (82307) |
| HAS_CHRONIC_HEART_DISEASE_YN | VARCHAR (1) | Indicates whether the patient has chronic heart disease.  Rule: DM Diagnosis Does Patient Have Chronic Heart Disease (82616) |
| HAS_CHRONIC_LUNG_DISEASE_YN | VARCHAR (1) | Indicates whether the patient has chronic lung disease.  Rule: DM Diagnosis Does Patient Have Chronic Lung Disease (82617) |
| HAS_ALCOHOLISM_YN | VARCHAR (1) | Indicates whether the patient has alcoholism.  Rule: DM Diagnosis Does Patient Have Alcoholism (82618) |
| HAS_CHRONIC_LIVER_DISEASE_YN | VARCHAR (1) | Indicates whether the patient has chronic liver disease.  Rule: DM Diagnosis Does Patient Have Chronic Liver Disease (82668) |
| HAS_CSF_LEAKS_YN | VARCHAR (1) | Indicates whether the patient has CSF leaks.  Rule: DM Diagnosis Does Patient Have CSF Leaks (82669) |
| HAS_COCHLEAR_IMPLANTS_YN | VARCHAR (1) | Indicates whether the patient has cochlear implants.  Rule: DM Surgery Does Patient Have Cochlear Implants (82670) |
| HAS_HEMOGLOBINOPATHIES_YN | VARCHAR (1) | Indicates whether the patient has hemoglobinopathies.  Rule: DM Diagnosis Does Patient Have Hemoglobinopathies (82671) |
| HAS_CONG_OR_ACQ_ASPLENIA_YN | VARCHAR (1) | Indicates whether the patient has congenital or acquired asplenia.  Rule: DM Diagnosis Does Patient Have Congenital or Acquired Asplenia (82672) |
| HAS_CONG_OR_ACQ_IMMUNODEF_YN | VARCHAR (1) | Indicates whether the patient has congenital or acquired immunodeficiencies.  Rule: DM Diagnosis Does Patient Have Congenital or Acquired Immunodeficiencies (82673) |
| HAS_CHRONIC_RENAL_FAILURE_YN | VARCHAR (1) | Indicates whether the patient has chronic renal failure.  Rule: DM Diagnosis Does Patient Have Chronic Renal Failure (82674) |
| HAS_NEPHROTIC_SYNDROME_YN | VARCHAR (1) | Indicates whether the patient has nephrotic syndrome.  Rule: DM Diagnosis Does Patient Have Nephrotic Syndrome (82675) |
| HAS_LEUKEMIA_YN | VARCHAR (1) | Indicates whether the patient has leukemia.  Rule: DM Diagnosis Does Patient Have Leukemia (82677) |
| HAS_LYMPHOMAS_YN | VARCHAR (1) | Indicates whether the patient has lymphomas.  Rule: DM Diagnosis Does Patient Have Lymphomas (82537) |
| HAS_HODGKIN_DISEASE_YN | VARCHAR (1) | Indicates whether the patient has Hodgkin disease.  Rule: DM Diagnosis Does Patient Have Hodgkin Disease (82678) |
| HAS_GENERALIZED_MALIGNANCY_YN | VARCHAR (1) | Indicates whether the patient has generalized malignancy.  Rule: DM Diagnosis Does Patient Have Generalized Malignancy (82679) |
| HAS_IATRO_IMMUNOSUPP_YN | VARCHAR (1) | Indicates whether the patient has iatrogenic immunosuppression.  Rule: DM Diagnosis Does Patient Have Iatrogenic Immunosuppression (82680) |
| HAD_SOLID_ORGAN_TRANSPLANT_YN | VARCHAR (1) | Indicates whether the patient has had a solid organ transplant.  Rule: DM Surgery Has Patient Had Solid Organ Transplant (82681) |
| HAS_MULTIPLE_MYELOMA_YN | VARCHAR (1) | Indicates whether the patient has multiple myeloma.  Rule: DM Diagnosis Does Patient Have Multiple Myeloma (82682) |
| PNEUMO_HM_MODIFIER_C | INTEGER | The patient's pneumococcal risk category value as indicated by the patient's Health Maintenance modifiers.  Rule: DM Imm Pneumococcal HM Modifier (82684) |
| PNEUMOCOCCAL_RISK_SCORE_C | INTEGER | The patient's pneumococcal risk score category value.  Rule: DM Imm Pneumococcal Risk Score (82683) |
| IS_BP_TREATED_YN | VARCHAR (1) | Indicates whether the patient's blood pressure is treated. Used by the ASCVD and CVD risk scores.  Rule: DM Is Treated For BP (19850) |
| HAS_HYPTN_PROB_YN | VARCHAR (1) | Indicates whether the patient has hypertension or a related blood pressure problem.  Rule: DM Diagnosis Does Patient Have Hypertension Or Related BP Problems (19852) |
| ON_BP_MED_YN | VARCHAR (1) | Indicates whether the patient is on antihypertensives specifically related to blood pressure treatment.  Rule: DM Med Is Prescribed Antihypertensive For BP (19851) |
| EVALUATE_AS_MALE_YN | VARCHAR (1) | Indicates whether the patient should be considered male for preventive screenings, etc.  Rule: DM General Evaluate as Male (CER 19386) |
| EVALUATE_AS_FEMALE_YN | VARCHAR (1) | Indicates whether the patient should be considered female for preventive screenings, etc.  Rule: DM General Evaluate as Female (CER 19385) |
| HAS_CERVIX_YN *(deprecated)* | VARCHAR (1) |  |
| HAS_BREASTS_YN *(deprecated)* | VARCHAR (1) |  |
| EDU_LEVEL_C | INTEGER | Patient's highest level of educational attainment.  Rule: DM Social Drivers: Education Level (CER 97039) |
| FIN_RESOURCE_STRAIN_C | INTEGER | Patient's reported financial resource strain.  Rule: DM Social Drivers: Financial Resource Strain (CER 97040) |
| IPV_EMOTIONAL_ABUSE_C | INTEGER | Indicates whether the patient reported being emotionally abused by a current or former partner.  Rule: DM Social Drivers: Intimate Partner Violence - Emotional Abuse (CER 97041) |
| PHONE_COMMUNICATION_C | INTEGER | How often patient communicates with friends or family over the phone in a week.  Rule: DM Social Drivers: Social Connections - Phone Communication Frequency (CER 97030) |
| CHURCH_ATTENDANCE_C | INTEGER | How often the patient reports attending religious services.  Rule: DM Social Drivers: Social Connections - Religious Services Attendance (CER 97031) |
| SOCIALIZATION_FREQ_C | INTEGER | How often the patients reports they spend time with friends or family in a given week.  Rule: DM Social Drivers: Social Connections - Socialization Frequency (CER 97032) |
| CLUBMTG_ATTENDANCE_C | INTEGER | How often patient attends club or organization meetings in a year.  Rule: DM Social Drivers: Social Connections - Club Meeting Attendance (CER 97033) |
| CLUB_MEMBER_C | INTEGER | Indicates whether the patient reports being a member of a club or organization.  Rule: DM Social Drivers: Social Connections - Club Membership (CER 97034) |
| LIVING_W_SPOUSE_C | INTEGER | Indicates whether patient reports living with spouse or partner  Rule: DM Social Drivers: Social Connections - Living with Spouse or Partner (CER 97035) |
| PHYS_ACT_DAYS_PER_WEEK_C | INTEGER | Number of days in a week in which the patient reports that they engage in strenuous activity.  Rule: DM Social Drivers: Physical Activity - Days Per Week (CER 97036) |
| PHYS_ACT_MIN_PER_SESS_C | INTEGER | How long (in minutes) patient reports that they exercise on days in which they exercise.  Rule: DM Social Drivers: Physical Activity - Minutes Per Session (CER 97037) |
| DAILY_STRESS_C | INTEGER | Patient's reported daily stress level.  Rule: DM Social Drivers: Daily Stress (CER 97038) |
| IPV_FEAR_C | INTEGER | Indicates whether the patient reported being afraid of a current or former partner.  Rule: DM Social Drivers: Intimate Partner Violence - Fear (CER 97042) |
| IPV_SEXUAL_ABUSE_C | INTEGER | Indicates whether the patient reported as having been sexually assaulted by a current or former partner.  Rule: DM Social Drivers: Intimate Partner Violence - Forced Sexual Contact (CER 97044) |
| IPV_PHYSICAL_ABUSE_C | INTEGER | Indicates whether the patient reported as having been physically abused by a current or former partner.  Rule: DM Social Drivers: Intimate Partner Violence - Physical Abuse (CER 97043) |
| ALCOHOL_FREQ_C | INTEGER | How frequently the patient reports consuming alcohol.  Rule: DM Social Drivers: Alcohol Frequency (CER 97045) |
| ALCOHOL_DRINKS_PER_DAY_C | INTEGER | How many standard drinks a patient reports having on a typical day.  Rule: DM Social Drivers: Alcohol Standard Drinks (CER 97046) |
| ALCOHOL_BINGE_C | INTEGER | How often the patient engages in binge drinking.  Rule: DM Social Drivers: Alcohol Binge Drinking (CER 97047) |
| FIN_RESOURCE_RISK_C | INTEGER | The current financial resource strain risk for the patient.  Rule: DM Social Drivers: Financial Resource Strain Risk Classification (CER 97057) |
| SOCIAL_ISOLATION_RISK_C | INTEGER | Most recent social isolation risk classification for the patient.  Rule: DM Social Drivers: Social Connections Risk Classification (CER 97059) |
| PHYS_INACTIVITY_RISK_C | INTEGER | Most recent physical inactivity risk classification.  Rule: DM Social Drivers: Physical Activity Risk Classification (CER 97060) |
| STRESS_RISK_C | INTEGER | Most recent stress risk classification for the patient.  Rule: DM Social Drivers: Daily Stress Risk Classification (CER 97058) |
| IPV_RISK_C | INTEGER | Most recent intimate partner violence risk classification for the patient.  Rule: DM Social Drivers: Intimate Partner Violence Risk Classification (CER 97062) |
| ALCOHOL_RISK_C | INTEGER | Most recent risky alcohol use risk classification for the patient.  Rule: DM Social Drivers: Alcohol Risk Classification (CER 97064) |
| HIB_1DOSE_HM_MODIFIER | INTEGER | Indicates whether the patient has hib 1-dose risk Health Maintenance modifiers.  Rule: DM IMM Hib 1-Dose HM Modifier (84964) |
| HIB_3DOSE_HM_MODIFIER | INTEGER | Indicates whether the patient has hib 3-dose risk Health Maintenance modifiers.  Rule: DM IMM Hib 3-Dose HM Modifier (84965) |
| HPV_3DOSE_HM_MODIFIER | INTEGER | Indicates whether the patient has hpv 3-dose risk Health Maintenance modifiers.  Rule: DM IMM HPV 3-Dose HM Modifier (16061) |
| MENACWY_2DOSE_HM_MODIFIER | INTEGER | Indicates whether the patient has meningococcal 2-dose risk Health Maintenance modifiers.  Rule: DM IMM Meningococcal 2-Dose HM Modifier (84973) |
| MENACWY_HM_MODIFIER | INTEGER | Indicates whether the patient has meningococcal risk Health Maintenance modifiers.  Rule: DM IMM Meningococcal HM Modifier (84970) |
| MENB_HM_MODIFIER | INTEGER | Indicates whether the patient has meningococcal b risk Health Maintenance modifiers.  Rule: DM IMM Meningococcal B HM Modifier (16044) |
| RABIES_RESEARCH_HM_MODIFIER | INTEGER | Indicates whether the patient has rabies researchers risk Health Maintenance modifiers.  Rule: DM IMM Rabies 3-Dose Continuous HM Modifier (84967) |
| YF_HM_MODIFIER | INTEGER | Indicates whether the patient has yellow fever risk Health Maintenance modifiers.  Rule: DM IMM Yellow Fever HM Modifier (84949) |
| JE_HM_MODIFIER | INTEGER | Indicates whether the patient has Japanese encephalitis risk Health Maintenance modifiers.  Rule: DM IMM JE HM Modifier (84948) |
| TYPHOID_HM_MODIFIER | INTEGER | Indicates whether the patient has typhoid risk Health Maintenance modifiers.  Rule: DM IMM Typhoid HM Modifier (16059) |
| HAS_COMPLEMENT_DEFICIENCY_YN | VARCHAR (1) | Indicates whether the patient has complement deficiency disorder.  Rule: DM Diagnosis Does Patient Have Complement Deficiency Disorder (84953) |
| HAS_FACTORB_DEFICIENCY_YN | VARCHAR (1) | Indicates whether the patient has factor B deficiency disease.  Rule: DM Diagnosis Does Patient Have Factor B Deficiency Disease (84955) |
| HAS_PROPERDIN_DEFICIENCY_YN | VARCHAR (1) | Indicates whether the patient has properdin deficiency disorder.  Rule: DM Diagnosis Does Patient Have Properdin Deficiency Disorder (84954) |
| HAD_STEMCELL_TRANSPLANT_YN | VARCHAR (1) | Indicates whether the patient had a stem cell transplant.  Rule: DM Surgery Has Patient Had Hemopoietic Stem Cell Transplant (84962) |
| STEMCELL_TRANSPLANT_DATE | DATETIME | Patient's stem cell transplant service date.  Rule: DM SURGERY LAST STEM CELL TRANSPLANT SERVICE DATE (16067) |
| DEPRESSION_RISK_C | INTEGER | Most recent depression PHQ-2 risk classification for the patient.  Rule: DM Social Drivers: Depression PHQ-2 Risk Classification (CER 97063) |
| LAST_PHQ_2_SCORE | No | Most recent PHQ-2 score.  Rule: DM Social Drivers: PHQ-2 Most Recent Result (CER 97051) |
| FOOD_INSECURITY_WORRY_C | INTEGER | The most recent response to the social drivers of health question about whether the patient worried about food running out in the past year or not.  Rule: DM Social Drivers: Food Insecurity - Worry (CER 97070) |
| FOOD_INSECURITY_SCARCE_C | INTEGER | The most recent response to the social drivers of health question about whether or not the patient had run out of food and was not able to buy more in the past year.  Rule: DM Social Drivers: Food Insecurity - Inability (CER 97071) |
| FOOD_INSECURITY_RISK_C | INTEGER | Most recent food insecurity risk classification for the patient.  Rule: DM Social Drivers: Food Insecurity Risk Classification (CER 97073) |
| MED_TRANSPORT_NEEDS_C | INTEGER | This item stores responses to the social drivers of health question about whether the patient had difficulty regarding transportation for medical appointments and medicine.  Rule: DM Social Drivers: Transportation Needs - Medical (CER 97074) |
| OTHER_TRANSPORT_NEEDS_C | INTEGER | This item stores responses to the social drivers of health question about whether the patient had difficulty regarding transportation for things other than medical appointments and medicine.  Rule: DM Social Drivers: Transportation Needs - Non-Medical (CER 97075) |
| TRANSPORT_NEEDS_RISK_C | INTEGER | Most recent transportation needs risk classification for the patient.  Rule: DM Social Drivers: Transportation Needs Risk Classification (CER 97077) |
| RABIES_HM_MODIFIER | INTEGER | Indicates whether the patient has rabies risk Health Maintenance modifiers.  Rule: DM IMM Rabies 3-Dose Frequent HM Modifier (84968) |
| MENCY_HM_MODIFIER | INTEGER | Indicates whether the patient has meningococcal C/Y risk Health Maintenance modifiers.  Rule: DM IMM Meningococcal C/Y HM Modifier (84971) |
| MENACWY_1DOSE_HM_MODIFIER | INTEGER | Indicates whether the patient has meningococcal 1-dose risk Health Maintenance modifiers.  Rule: DM IMM Meningococcal 1-Dose HM Modifier (84972) |
| HAS_CERVIX_2_YN | VARCHAR (1) | Indicates whether the patient should be considered as having a cervix.  Rule: DM General Has Cervix (CER 83364) |
| HAS_BREASTS_2_YN | VARCHAR (1) | Indicates whether the patient should be considered as having breasts.  Rule: DM General Has Breasts (CER 83362) |
| MENB_2DOSE_HM_MODIFIER | INTEGER | Indicates whether the patient has Meningococcal B 2-dose risk Health Maintenance modifiers.  Rule: DM IMM MenB 2-Dose Risk HM Modifier (16100) |
| TOBACCO_RISK_C | INTEGER | Most recent tobacco use risk classification for the patient.  Rule: DM Social Drivers: Tobacco Risk Classification (CER 97026) |
| MMR_2DOSE_ART_HM_MODIFIER | INTEGER | Indicates whether the patient has the MMR risk 2-dose ART Health Maintenance modifiers.  Rule: DM IMM MMR 2-Dose ART HM Modifier (CER 84999) |
| FIRST_ART_DATE | DATETIME | Returns the date the patient began antiviral therapy.  Rule: DM MED BEGIN DATE OF ANTIVIRAL THERAPY (CER 16983) |
| HAS_COMPLEMENT_INHIBITOR_YN | VARCHAR (1) | Indicates whether the patient is taking a drug that is a type of complement inhibitor.  Rule: DM Medication Is Patient Taking a Complement Inhibitor (97788) |
| SDOH_SMOKING_STATUS_C | INTEGER | The category value of the patient's last recorded smoking tobacco use status. This value pulls from the rule used in the Social Drivers tobacco risk score.  Rule: DM Social Drivers: Smoking Tobacco Use Status (CER 97028) |
| SDOH_SMOKELESS_STATUS_C | INTEGER | The category value of the patient's last recorded smokeless tobacco use status. This value pulls from the rule used in the Social Drivers tobacco risk score.  Rule: DM Social Drivers: Smokeless Tobacco Use Status (CER 97078) |
| IN_LONG_TERM_CARE_YN | VARCHAR (1) | Indicates whether the patient has an episode with a type of Long Term Care.  Rule: DM IMM Is Patient in Long Term Care (84544) |
| NEEDS_COVID_BOOSTER_YN *(deprecated)* | VARCHAR (1) | *** Deprecated *** In table DM_WLL_ALL, the column NEEDS_COVID_BOOSTER_YN has been deprecated. The deprecated column's content/data is no longer available since it is no longer populated in Chronicles.  Indicates whether the patient has a medical need for a booster dose of COVID-19 vaccine.  Rule: DM IMM COVID-19 Patient Has Medical Need for Booster (84545) |
| HAS_HAD_DENGUE_YN | VARCHAR (1) | Indicates whether a patient has had evidence of dengue fever.  Rule: DM Has Patient Had Evidence of Dengue Fever (97175) |
| LAST_EPDS_TOTAL_SCORE | NUMERIC (2,0) | Most recent Edinburgh Postnatal Depression Scale total score.  Rule: DM Social Drivers: Edinburgh Postnatal Depression Scale Total Last Flowsheet Data (CER 97080) |
| LAST_EPDS_SELF_HARM_C | INTEGER | The most recent response to a question on the Edinburgh Postnatal Depression Scale about self harm.  Rule: DM Social Drivers: Edinburgh Postnatal Depression Scale Self-Harm Last Flowsheet Data  (CER 97081) |
| EPDS_RISK_C | INTEGER | Most recent Edinburgh Postnatal Depression Scale risk classification for the patient.  Rule: DM Social Drivers: Edinburgh Postnatal Depression Scale Risk Classification (CER 97084) |
| HOUSING_UNABLE_TO_PAY_C | INTEGER | The most recent response to a question on the Children's Healthwatch Housing screener about unable to pay for housing in the last year.  Rule: DM Social Drivers: Children's HealthWatch Housing Mortgage Last Flowsheet Value (CER 97085) |
| HOUSING_NUMBER_OF_PLACES_LIVED | NUMERIC (15,0) | This column is replaced by HOUSING_NUMBER_OF_TIMES_MOVED.  The most recent response to a question on the Children's Healthwatch Housing screener about number of places lived in the last year.  Rule: DM Social Drivers: Children's HealthWatch Housing Places Lived Last Flowsheet Value (CER 97088) |
| HOUSING_STEADY_LOC_TO_SLEEP_C | INTEGER | This column is replaced by HOUSING_HOMELESS_C.  The most recent response to a question on the Children's Healthwatch Housing screener about unstable housing in the last year.  Rule: DM Social Drivers: Children's HealthWatch Housing Steady Place to Sleep Last Flowsheet Value (CER 97090) |
| HOUSING_STABILITY_RISK_C | INTEGER | This column is replaced by HOUSING_STABILITY_RISK_CLAS_C  Most recent Children's HealthWatch Housing risk classification for the patient.  Rule: DM Social Drivers: Children's HealthWatch Housing Risk Classification (CER 97087) |
| OASIS_HEALTH_LITERACY_LAST_C | INTEGER | Most recent OASIS Health Literacy Assessment  Rule: DM Social Drivers: Home Health OASIS B1300 - Health Literacy Last SmartData Element Data (93033) |
| OASIS_HEALTH_LITERACY_RISK_C | INTEGER | Most recent OASIS Health Literacy Risk Classification  Rule: DM Social Drivers: Home Health OASIS B1300 - Health Literacy Risk Classification (93034) |
| OASIS_TRANSPORT_MED_LAST_C | INTEGER | Most recent OASIS Transportation Medical Assessment  Rule: DM Social Drivers: Home Health OASIS A1250A - Transportation Medical Last SmartData Element Data (93030) |
| OASIS_TRANSPORT_NONMED_LAST_C | INTEGER | Most recent OASIS Transportation Non-Medical Assessment  Rule: DM Social Drivers: Home Health OASIS A1250B - Transportation Non-Medical Last SmartData Element Data (93031) |
| OASIS_TRANSPORT_RISK_C | INTEGER | Most recent OASIS Transportation Risk Classification  Rule: DM Social Drivers: Home Health OASIS A1250 - Transportation Risk Classification (93032) |
| OASIS_FEEL_SOC_ISO_LAST_C | INTEGER | Most recent OASIS Social Isolation Assessment  Rule: DM Social Drivers: Home Health OASIS D0700 - Social Isolation Last SmartData Emelent Data (93029) |
| OASIS_FEEL_SOC_ISO_RISK_C | INTEGER | Most recent OASIS Social Isolation Risk Classification  Rule: DM Social Drivers: Home Health OASIS D0700 - Social Isolation Risk Classification (93028) |
| OASIS_TRANSPORT_UNK_LAST_C | INTEGER | Most recent OASIS Transportation Unknown Assessment  Rule: DM Social Drivers: Home Health OASIS A1250X/Y - Transportation Unknown Last SmartData Element Data (93035) |
| LAST_PHQ_9_SCORE | NUMERIC (2,0) | Most recent PHQ-9 score.  Rule: DM Social Drivers: PHQ-9 Most Recent Result (CER 97142) |
| DEPRESSION_PHQ_9_RISK_C | INTEGER | Most recent depression PHQ-9 risk classification for the patient.  Rule: DM Social Drivers: Depression PHQ-9 Risk Classification (CER 97143) |
| HAS_LESS_SEV_BCELL_DEFICNCY_YN | VARCHAR (1) | Indicates whether the patient has less severe B cell deficiency disorders. "Y" indicates there is such a diagnosis. "N" indicates there is not.  Rule: DM Diagnosis Does Patient Have Less Severe B Cell Deficiency Disorder (83476) |
| HAS_ANTIBODY_DEFICNCY_YN | VARCHAR (1) | Indicates whether the patient has antibody deficiencies. "Y" indicates there is such a diagnosis. "N" indicates there is not.  Rule: DM Diagnosis Does Patient Have Antibody Deficiencies (83478) |
| HEALTH_LITERACY_INSTRUCTIONS_C | INTEGER | The last assessment recorded for B1300 Health Literacy Screener.  Rule: DM Social Drivers: Health Literacy (97155) |
| HEALTH_LITERACY_RISK_C | INTEGER | The patient's most recent risk classification for Health Literacy.    Rule: DM Social Drivers: Health Literacy Risk Classification (97156) |
| UTILITIES_SHUT_OFF_C | INTEGER | The last assessment recorded for the AHC HRSN Utilities screener.   Rule: DM Social Drivers: Utilities (97157) |
| UTILITIES_RISK_C | INTEGER | The patient's most recent risk classification for Utilities.  Rule: DM Social Drivers: Utilities Risk Classification (97158) |
| HOUSING_STABILITY_RISK_CLAS_C | INTEGER | This column replaces HOUSING_STABILITY_RISK_C.   Most recent Children's HealthWatch Housing risk classification for the patient.  Rule: DM Social Drivers: Children's HealthWatch Housing Risk Classification (90097173) |
| HOUSING_NUMBER_OF_TIMES_MOVED | VARCHAR (50) | This column replaces HOUSING_NUMBER_OF_PLACES_LIVED.  The most recent response to a question on the Children's Healthwatch Housing screener about number of times moved in the last year.  Rule: DM Social Drivers: Children's HealthWatch Housing Times Moved Last Flowsheet Value (90097172) |
| SMOKING_QUIT_L_DT | DATETIME | Rule: DM HISTORY LAST SMOKING TOBACCO QUIT DATE (90082165) |
| HOUSING_HOMELESS_C | INTEGER | The most recent response to a question on the Children's Healthwatch Housing screener about being homeless or living in a shaler in the last year.  Rule: DM Social Drivers: Children's HealthWatch Housing Homelessness Last Flowsheet Value (90097174) |
| AHC_INADEQUATE_HOUSING_RISK_C | INTEGER | Most recent AHC Inadequate Housing risk classification for the patient.  Rule: DM Social Drivers: AHC Inadequate Housing Risk Classification (90083870) |
| AHC_TXPORT_RISK_C | INTEGER | Most recent AHC Transportation Needs risk classification for the patient.  Rule: DM Social Drivers: AHC Transportation Risk Classification (90083871) |
| AHC_PERSONAL_SAFETY_RISK_C | INTEGER | Most recent AHC Personal Safety risk classification for the patient.  Rule: DM Social Drivers: AHC Personal Safety Risk Classification (90083872) |
| AHC_HOUSING_PROBLEMS | VARCHAR (250) | Most recent response to the AHC Housing Problems question.  Rule: DM Social Drivers: AHC Housing Problems (90083783) |
| AHC_LIVING_SITUATION | INTEGER | Most recent response to the AHC Living Situation question.  Rule: DM Social Drivers: AHC Living Situation (90083782) |
| AHC_TXPORT | INTEGER | Most recent response to the AHC Transportation question for the Transportation Needs domain.  Rule: DM Social Drivers: AHC Transportation (90083784) |
| AHC_THREATEN_YOU | INTEGER | Most recent response to the AHC Threaten You question for the Personal Safety domain.  Rule: DM Social Drivers: AHC Threaten You (90083787) |
| AHC_INSULT_YOU | INTEGER | Most recent response to the AHC Insult You question for the Personal Safety domain.  Rule: DM Social Drivers: AHC Insult You (90083786) |
| AHC_SCREAM_AT_YOU | INTEGER | Most recent response to the AHC Scream at You question for the Personal Safety domain.  Rule: DM Social Drivers: AHC Scream at You (90083788) |
| AHC_PHYSICALLY_HURT_YOU | INTEGER | Most recent response to the AHC Physically Hurt You question for the Personal Safety domain.  Rule: DM Social Drivers: AHC Physically Hurt You (90083785) |
| AHC_SOCIAL_CONNECTIONS_RISK_C | INTEGER | Most recent AHC Social Connections risk classification for the patient.  Rule: DM Social Drivers: AHC Social Connections Risk Classification (90083875) |
| AHC_NEED_HELP_ACTIVITIES | INTEGER | Most recent response to the AHC Need Help Activities question for the Social Connections domain.  Rule: DM Social Drivers: AHC Need Help Activities (90083791) |
| AHC_LONELY_ISOLATED | INTEGER | Most recent response to the AHC Lonely Isolated question for the Social Connections domain.  Rule: DM Social Drivers: AHC Lonely Isolated (90083792) |
| OASIS_A1255_RISK_C | INTEGER | Rule: DM Social Drivers: Home Health OASIS A1255 - Transportation Risk Classification (90093041) |
| OASIS_A1255_LAST_C | INTEGER | Rule: DM Social Drivers: Home Health OASIS A1255 - Transportation Last SmartData Element Data (90093025) |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| B-TREE INDEX | EIX_DM_WELL_ALL_PATID | PAT_ID | 1 | Yes | Yes |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | RECORD_ID | DM_ACG_RISK | RECORD_ID | Unknown | No | No |  |
| 1 | RECORD_ID | DM_ACO | RECORD_ID | Unknown | No | No |  |
| 1 | RECORD_ID | DM_ACO_EXT | RECORD_ID | Unknown | No | No |  |
| 1 | RECORD_ID | DM_ACTIVE_PAT | RECORD_ID | Unknown | No | No |  |
| 1 | RECORD_ID | DM_ADHD | RECORD_ID | Unknown | No | No |  |
| 1 | RECORD_ID | DM_ADHD_EXT | RECORD_ID | Unknown | No | No |  |
| 1 | RECORD_ID | DM_ADOL_TRANS | RECORD_ID | Unknown | No | No |  |
| 1 | RECORD_ID | DM_ADOL_TRANS_EXT | RECORD_ID | Unknown | No | No |  |
| 1 | RECORD_ID | DM_ADULT_ADHD | RECORD_ID | Unknown | No | No |  |
| 1 | RECORD_ID | DM_ADULT_ASTHMA | RECORD_ID | Unknown | No | No |  |
| 1 | RECORD_ID | DM_ADULT_DIABETES | RECORD_ID | Unknown | No | No |  |
| 1 | RECORD_ID | DM_ADULT_FTM | RECORD_ID | Unknown | No | No |  |
| 1 | RECORD_ID | DM_ADULT_FTM_EXT | RECORD_ID | Unknown | No | No |  |
| 1 | RECORD_ID | DM_ADULT_HIV | RECORD_ID | Unknown | No | No |  |
| 1 | RECORD_ID | DM_ADULT_HYPERTENSION | RECORD_ID | Unknown | No | No |  |
| 1 | RECORD_ID | DM_ADULT_MTF | RECORD_ID | Unknown | No | No |  |
| 1 | RECORD_ID | DM_ADULT_MTF_EXT | RECORD_ID | Unknown | No | No |  |
| 1 | RECORD_ID | DM_ADULT_OBESITY | RECORD_ID | Unknown | No | No |  |
| 1 | RECORD_ID | DM_ALS | RECORD_ID | Unknown | No | No |  |
| 1 | RECORD_ID | DM_ANESTHESIA | RECORD_ID | Unknown | No | No |  |
| 1 | RECORD_ID | DM_ANESTHESIA_2 | RECORD_ID | Unknown | No | No |  |
| 1 | RECORD_ID | DM_ASTHMA | RECORD_ID | Unknown | No | No |  |
| 1 | RECORD_ID | DM_ASTHMA_EXT | RECORD_ID | Unknown | No | No |  |
| 1 | RECORD_ID | DM_ATRIAL_FIBRILLATION | RECORD_ID | Unknown | No | No |  |
| 1 | RECORD_ID | DM_BREAST_HEALTH | RECORD_ID | Unknown | No | No |  |
| 1 | RECORD_ID | DM_CAD | RECORD_ID | Unknown | No | No |  |
| 1 | RECORD_ID | DM_CAD_DIABETES | RECORD_ID | Unknown | No | No |  |
| 1 | RECORD_ID | DM_CAD_EXT | RECORD_ID | Unknown | No | No |  |
| 1 | RECORD_ID | DM_CANCER_PATIENT | RECORD_ID | Unknown | No | No |  |
| 1 | RECORD_ID | DM_CANCER_PROBLEM | RECORD_ID | Unknown | No | No |  |

_(500 total; showing first 30)_
