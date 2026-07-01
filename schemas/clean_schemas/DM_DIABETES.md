# DM_DIABETES

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=DM_DIABETES

## Description

DM_DIABETES is a data mart table that stores information related to the topic of diabetes. This table consolidates patient information from many subject areas including lab values, encounters, vitals, medications, diagnoses, and social history.  Only patients that meet specific inclusion criteria have information stored in this table.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | RDT |
| Release Version | Summer 2009 |
| May contain EHI? | No |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| RECORD_ID | NUMERIC (18,0) | The unique identifier (.1 item) for the registry data record. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| REGISTRY_STATUS_C | INTEGER |  |
| PAT_ID | VARCHAR (18) | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| CUR_PCP_PROV_ID | No | The unique ID of the patient's primary care physician.  Rule: DM General Current PCP (82000) |
| CUR_PRIM_LOC_ID | No | The unique ID of the patient's primary location.   Rule: DM General Primary Location (82001) |
| CONTACT_LAST_DT | No | The date of the patient's last encounter.  Rule: DM Encounter Last Encounter Date (82025) |
| CONTACT_LAST_TYPE_C | No | The encounter type category value of the patient's last encounter.  Rule: DM Encounter Last Encounter Type (82026) |
| OFF_VIS_LAST_DT | No | Date of the patient's last office visit.  Rule: DM Encounter Last Office Visit Date (82027) |
| INPAT_ADMIT_LAST_DT | No | The date of the patient's last inpatient admission.   Rule: DM Encounter Last Inpatient Admission Date (82028) |
| NUM_CONTACT | No | The total number of encounters the patient has had.  Rule: DM Encounter Number of Encounters (82030) |
| NUM_HOSP_ADMIT | No | The total number of times the patient was admitted to a hospital.  Rule: DM Encounter Number Of Hospital Admissions (82031) |
| ENDO_VIS_LAST_DT | No | The date of the patient's last visit to an endocrinologist.  Rule: DM Encounter Last Visit to an Endocrinologist (82032) |
| NEPH_VIS_LAST_DT | No | The date of the patient's last visit to a nephrologist.  Rule: DM Encounter Last Visit to a Nephrologist (82033) |
| OPHTH_VIS_LAST_DT | No | The date of the patient's last visit to an ophthalmologist.  Rule: DM Encounter Last Visit to an Ophthalmologist (82034) |
| POD_VIS_LAST_DT | No | The date of the patient's last visit to a podiatrist.  Rule: DM Encounter Last Visit to a Podiatrist (82036) |
| NUTR_VIS_LAST_DT | No | The date of the patient's last visit to a nutritionist.  Rule: DM Encounter Last Visit to a Nutritionist (82035) |
| OFF_VIS_PROV_ID | No | The unique ID of the visit provider for the patient's last office visit.  Rule: DM Encounter Last Visit Provider (82029) |
| CARDIO_VIS_LAST_DT | No | The date of the patient's last visit to a cardiologist.  Rule: DM Encounter Last Visit to a Cardiologist (82037) |
| WEIGHT_LAST | No | The patient's most recent weight.  Rule: DM Vitals Last Weight (82100) |
| WEIGHT_LAST_DT | No | The date the patient's most recent weight was recorded.  Rule: DM Vitals Last Weight (82100) |
| WEIGHT_FIRST | No | The patient's first recorded weight in a given time period.  Rule: DM Vitals First Weight (82102) |
| WEIGHT_FIRST_DT | No | The date the patient's first weight in a given time period was recorded.  Rule: DM Vitals First Weight (82102) |
| HEIGHT_LAST | No | The patient's most recent height.  Rule: DM Vitals Last Height (82101) |
| HEIGHT_LAST_DT | No | The date the patient's most recent height was recorded.  Rule: DM Vitals Last Height (82101) |
| BP_SYS_LAST | No | The patient's most recent systolic blood pressure.  Rule: DM Vitals Last Systolic BP (82103) |
| BP_SYS_LAST_DT | No | The date the patient's most recent systolic blood pressure was recorded.  Rule: DM Vitals Last Systolic BP (82103) |
| BP_DIA_LAST | No | The patient's most recent diastolic blood pressure.  Rule: DM Vitals Last Diastolic BP (82104) |
| BP_DIA_LAST_DT | No | The date the patient's most recent diastolic blood pressure was recorded.  Rule: DM Vitals Last Diastolic BP (82104) |
| BP_SYS_FIRST | No | The patient's first recorded systolic blood pressure in a given time period.  Rule: DM Vitals First Systolic BP (82105) |
| BP_SYS_FIRST_DT | No | The date the patient's first systolic blood pressure in a given time period was recorded.  Rule: DM Vitals First Systolic BP (82105) |
| BP_DIA_FIRST | No | The patient's first recorded diastolic blood pressure in a given time period.  Rule: DM Vitals First Diastolic BP (82106) |
| BP_DIA_FIRST_DT | No | The date the patient's first diastolic blood pressure in a given time period was recorded.  Rule: DM Vitals First Diastolic BP (82106) |
| BMI_LAST | No | The patient's most recent  body mass index.  Rule: DM Vitals Last BMI (82108) |
| BMI_FIRST | No | The patient's first recorded body mass index in a given time period.  Rule: DM Vitals First BMI (82107) |
| TOBAC_USE_STATUS_C | No | It is recommended that you use SMOKING_STATUS_C for Meaningful Use.  The category value of the patient's last recorded tobacco use status.  Rule: DM History Last Tobacco Use Status (82150) |
| TOBAC_USER_HX_YN | No | It is recommended that you use SMOKING_USER_HX_YN for Meaningful Use.  Indicates whether a patient was ever identified as a tobacco user.  Rule: DM History Is Previous Tobacco User (82151) |
| TOBAC_DX_ID | No | The unique diagnosis ID of the most recent diagnosis that identified the patient as a tobacco user.  Rule: DM Diagnosis Tobacco Use Diagnosis ID (82152) |
| TOBAC_NUM_PACK | No | The most recently reported quantity of tobacco consumed by the patient in packs/day.  Rule: DM History Last Tobacco Packs (82154) |
| TOBAC_QUIT_LAST_DT | No | It is recommended that you use SMOKING_QUIT_L_DT for Meaningful Use.  Contains the patient's most recently recorded tobacco quit date if the patient has previously quit using tobacco and does not currently use tobacco.  Rule: DM History Last Tobacco Quit Date (82155) |
| TOBAC_NUM_PACK_HX | No | If the patient has previously quit using tobacco and does not currently use tobacco, stores the most recently reported quantity of tobacco consumed by the patient in packs/day when the patient was using tobacco.  Rule: DM History Previous Tobacco Packs (82156) |
| TOBAC_DX_DT | No | The most recent date a diagnosis was assigned to the patient that identified the patient as a tobacco user.  Rule: DM Diagnosis Tobacco Use Diagnosis ID (82152) |
| ALCOHOL_DX_ID | No | The unique diagnosis ID of the most recent diagnosis that identified the patient as an alcohol user.  Rule: DM Diagnosis Alcohol Use Diagnosis ID (82157) |
| ALCOHOL_DX_DT | No | The most recent date a diagnosis was assigned to the patient that identified the patient as an alcohol user.  Rule: DM Diagnosis Alcohol Use Diagnosis ID (82157) |
| HBA1C_LAST | No | The patient's most recent hemoglobin A1C (HbA1C) value.  Only numeric lab values are stored in this column.  Non-numeric lab values entered are displayed as null.  If the data is an inequality sign followed by a number, then an estimate value is returned instead. If the inequality is > or >=, then the number plus 10% is returned (e.g. ?>10? becomes ?11?). If the inequality is < or <=, then the number minus 10% is returned (e.g. ?<10? becomes ?9?). Other non-numeric data is not returned.  Rule: DM Lab Last Hemoglobin A1C (82200) |
| HBA1C_LAST_DT | No | The date as per the prioritized instant of the patient's most recent hemoglobin A1C (HbA1C) lab.  Rule: DM Lab Last Hemoglobin A1C (82200) |
| LDL_DIR_LAST | No | The patient's most recent low-density lipoprotein (LDL) direct value.  Only numeric lab values are stored in this column.  Non-numeric lab values entered are displayed as null.  Rule: DM Lab Last LDL Direct (82201) |
| LDL_DIR_LAST_DT | No | The date as per the prioritized instant of the patient's most recent low-density lipoprotein (LDL) direct lab.  Rule: DM Lab Last LDL Direct (82201) |
| LDL_CALC_LAST | No | The patient's most recent calculated low-density lipoprotein (LDL) value.  Only numeric lab values are stored in this column.  Non-numeric lab values entered are displayed as null.  Rule: DM Lab Last LDL Calculated (82213) |
| LDL_CALC_LAST_DT | No | The date as per the prioritized instant of the patient's most recent calculated low-density lipoprotein (LDL) lab.  Rule: DM Lab Last LDL Calculated (82213) |
| HDL_LAST | No | The patient's most recent high-density lipoprotein (HDL) value.  Only numeric lab values are stored in this column.  Non-numeric lab values entered are displayed as null.  Rule: DM Lab Last HDL (82202) |
| HDL_LAST_DT | No | The date as per the prioritized instant of the patient's most recent high-density lipoprotein (HDL) lab.  Rule: DM Lab Last HDL (82202) |
| VLDL_LAST | No | The patient's most recent very low density lipoprotein  (VLDL) value.  Only numeric lab values are stored in this column.  Non-numeric lab values entered are displayed as null.   Rule: DM Lab Last VLDL (82203) |
| VLDL_LAST_DT | No | The date as per the prioritized instant of the patient's most recent very low density lipoprotein (VLDL) lab.  Rule: DM Lab Last VLDL (82203) |
| LDL_HDL_RT_LAST | No | The patient's most recent LDL:HDL ratio value.  Only numeric lab values are stored in this column.  Non-numeric lab values entered are displayed as null.  If the data is an inequality sign followed by a number, then an estimate value is returned instead. If the inequality is > or >=, then the number plus 10% is returned (e.g. ?>10? becomes ?11?). If the inequality is < or <=, then the number minus 10% is returned (e.g. ?<10? becomes ?9?). Other non-numeric data is not returned.  Rule: DM Lab Last LDL:HDL Ratio (82204) |
| LDL_HDL_RT_LAST_DT | No | The date as per the prioritized instant of the patient's most recent LDL:HDL ratio lab.  Rule: DM Lab Last LDL:HDL Ratio (82204) |
| TTL_CHL_LAST | No | The patient's most recent total cholesterol value.  Only numeric lab values are stored in this column.  Non-numeric lab values entered are displayed as null.  Rule: DM Lab Last Total Cholesterol (82205) |
| TTL_CHL_LAST_DT | No | The date as per the prioritized instant of the patient's most recent total cholesterol lab.  Rule: DM Lab Last Total Cholesterol (82205) |
| TRIGLY_LAST | No | The patient's most recent triglycerides value. Only numeric lab values are stored in this column.  Non-numeric lab values entered are displayed as null.  Rule: DM Lab Last Triglycerides (82206) |
| TRIGLY_LAST_DT | No | The date as per the prioritized instant of the patient's most recent triglycerides lab.  Rule: DM Lab Last Triglycerides (82206) |
| BUN_LAST | No | The patient's most recent blood urea nitrogen value.  Only numeric lab values are stored in this column.  Non-numeric lab values entered are displayed as null.  Rule: DM Lab Last Blood Urea Nitrogen (82207) |
| BUN_LAST_DT | No | The date as per the prioritized instant of the patient's most recent blood urea nitrogen lab.  Rule: DM Lab Last Blood Urea Nitrogen (82207) |
| UR_MALB_LAST | No | The patient's most recent urine microalbumin value.  Only numeric lab values are stored in this column.  Non-numeric lab values entered are displayed as null.  If the data is an inequality sign followed by a number, then an estimate value is returned instead. If the inequality is > or >=, then the number plus 10% is returned (e.g. ?>10? becomes ?11?). If the inequality is < or <=, then the number minus 10% is returned (e.g. ?<10? becomes ?9?). Other non-numeric data is not returned.  Rule: DM Lab Last Urine Microalbumin (82208) |
| UR_MALB_LAST_DT | No | The date as per the prioritized instant of the patient's most recent urine microalbumin lab.  Rule: DM Lab Last Urine Microalbumin (82208) |
| UR_PROT_LAST | No | The patient's most recent urine protein value. Only numeric lab values are stored in this column.  Non-numeric lab values entered are displayed as null.  If the data is an inequality sign followed by a number, then an estimate value is returned instead. If the inequality is > or >=, then the number plus 10% is returned (e.g. ?>10? becomes ?11?). If the inequality is < or <=, then the number minus 10% is returned (e.g. ?<10? becomes ?9?). Other non-numeric data is not returned.  Rule: DM Lab Last Urine Protein (82212) |
| UR_PROT_LAST_DT | No | The date as per the prioritized instant of the patient's most recent urine protein lab.  Rule: DM Lab Last Urine Protein (82212) |
| PROT_CR_RT_LAST | No | The patient's most recent protein:creatinine ratio value. Only numeric lab values are stored in this column.  Non-numeric lab values entered are displayed as null.  If the data is an inequality sign followed by a number, then an estimate value is returned instead. If the inequality is > or >=, then the number plus 10% is returned (e.g. ?>10? becomes ?11?). If the inequality is < or <=, then the number minus 10% is returned (e.g. ?<10? becomes ?9?). Other non-numeric data is not returned.  Rule: DM Lab Last Protein:Creatinine Ratio (82214) |
| PROT_CR_RT_LAST_DT | No | The date as per the prioritized instant of the patient's most recent protein:creatinine ratio lab.  Rule: DM Lab Last Protein:Creatinine Ratio (82214) |
| CREAT_LAST | No | The patient's most recent creatinine value. Only numeric lab values are stored in this column.  Non-numeric lab values entered are displayed as null.  Rule: DM Lab Last Creatinine (82209) |
| CREAT_LAST_DT | No | The date as per the prioritized instant of the patient's last creatinine lab.  Rule: DM Lab Last Creatinine (82209) |
| CREAT_CLR_LAST | No | The patient's most recent creatinine clearance value. Only numeric lab values are stored in this column.  Non-numeric lab values entered are displayed as null.  If the data is an inequality sign followed by a number, then an estimate value is returned instead. If the inequality is > or >=, then the number plus 10% is returned (e.g. ?>10? becomes ?11?). If the inequality is < or <=, then the number minus 10% is returned (e.g. ?<10? becomes ?9?). Other non-numeric data is not returned.  Rule: DM Lab Last Creatinine Clearance (82210) |
| CREAT_CLR_LAST_DT | No | The date as per the prioritized instant of the patient's most recent creatinine clearance lab.  Rule: DM Lab Last Creatinine Clearance (82210) |
| IMMNZTN_PNEUM_YN | No | Indicates whether a patient was administered the pneumonia vaccine. "Y" indicates the patient has been administered this vaccine. "N" indicates the patient has not been administered this vaccine.  Rule: DM Imm is Pneumonia Vaccine Administered (82352) |
| IMMNZTN_FLU_DT | No | The date the patient's most recent flu vaccine was administered.  Rule: DM Imm Flu Vaccine Administration Date (82351) |
| IMMNZTN_FLU_YN | No | Indicates whether a patient was administered the flu vaccine. "Y" indicates the patient has been administered this vaccine. "N" indicates the patient has not been administered this vaccine.  Rule: DM Imm is Flu Vaccine Administered (82350) |
| ON_STATIN_YN | No | Indicates whether a statin medication is on the patient's current medication list. "Y" indicates a statin medication is on the patient's current medication list. "N" indicates a statin medication is not on the patient's current medication list.  Rule: DM Med Is Prescribed Statins (82375) |
| STATIN_ORD_ID | No | The unique ID of the last medication order for any statin medication which is also on the patient's current medication list.   Rule: DM Med Last Current Statin (82382) |
| STATIN_ORD_DT | No | The ordering date of the last medication order for any statin medication which is also on the patient's current medication list.  Rule: DM Med Last Current Statin (82382) |
| ON_ANTHYPERT_YN | No | Indicates whether an antihypertensive medication is on the patient's current medication list. "Y" indicates an antihypertensive medication is on the patient's current medication list. "N" indicates an antihypertensive medication is not on the patient's current medication list.  Rule: DM Med Is Prescribed Antihypertensives (82376) |
| ANTIHYPERT_ORD_ID | No | The unique ID of the last medication order for any antihypertensive medication which is also on the patient's current medication list.   Rule: DM Med Last Current Antihypertensive (82383) |
| ANTIHYPERT_ORD_DT | No | The ordering date of the last medication order for any antihypertensive medication which is also on the patient's current medication list.  Rule: DM Med Last Current Antihypertensive (82383) |
| ON_SALICYLATE_YN | No | Indicates whether a salicylate medication is on the patient's current medication list. "Y" indicates a salicylate  medication is on the patient's current medication list. "N" indicates a salicylate medication is not on the patient's current medication list.  Rule: DM Med Is Prescribed Salicylates (82377) |
| SALICYLATE_ORD_ID | No | The unique ID of the last medication order for any salicylate medication which is also on the patient's current medication list.   Rule: DM Med Last Current Salicylate (82384) |
| SALICYLATE_ORD_DT | No | The ordering date of the last medication order for any salicylate medication which is also on the patient's current medication list.   Rule: DM Med Last Current Salicylate (82384) |
| ON_ANTIPLAT_YN | No | Indicates whether an antiplatelet medication is on the patient's current medication list. "Y" indicates an antiplatelet medication is on the patient's current medication list. "N" indicates an antiplatelet medication is not on the patient's current medication list.  Rule: DM Med Is Prescribed Antiplatelets (82378) |
| ANTIPLAT_ORD_ID | No | The unique ID of the last medication order for any antiplatelet medication which is also on the patient's current medication list.   Rule: DM Med Last Current Antiplatelet (82385) |
| ANTIPLAT_ORD_DT | No | The ordering date of the last medication order for any antiplatelet medication which is also on the patient's current medication list.  Rule: DM Med Last Current Antiplatelet (82385) |
| ON_OR_ANTIDIAB_YN | No | Indicates whether an oral antidiabetic agent is on the patient's current medication list. "Y" indicates an oral antidiabetic agent is on the patient's current medication list. "N" indicates an oral antidiabetic agent is not on the patient's current medication list.  Rule: DM Med Is Prescribed Oral Antidiabetics (82379) |
| OR_ANTIDIAB_ORD_ID | No | The unique ID of the last medication order for any oral antidiabetic agent which is also on the patient's current medication list.   Rule: DM Med Last Current Oral Antidiabetic (82386) |
| OR_ANTIDIAB_ORD_DT | No | The ordering date of the last medication order for any oral antidiabetic medication which is also on the patient's current medication list.  Rule: DM Med Last Current Oral Antidiabetic (82386) |
| ON_INSULIN_YN | No | Indicates whether insulin is on the patient's current medication list. "Y" indicates insulin is on the patient's current medication list. "N" indicates insulin is not on the patient's current medication list.  Rule: DM Med Is Prescribed Insulins (82380) |
| INSULIN_ORD_ID | No | The unique ID of the last medication order for insulin which is also on the patient's current medication list.   Rule: DM Med Last Current Insulin (82387) |
| INSULIN_ORD_DT | No | The ordering date of the last medication order for any insulin medication which is also on the patient's current medication list.  Rule: DM Med Last Current Insulin (82387) |
| ON_INJ_ANTIDIAB_YN | No | Indicates whether an injectable antidiabetic is on the patient's current medication list. "Y" indicates an injectable antidiabetic is on the patient's current medication list. "N" indicates an injectable antidiabetic  is not on the patient's current medication list.  Rule: DM Med Is Prescribed Injectable Antidiabetics (82381) |
| INJ_ANTIDIAB_ORD_ID | No | The unique ID of the last medication order for an injectable antidiabetic agent which is also on the patient's current medication list.   Rule: DM Med Last Current Injectable Antidiabetic (82388) |
| INJ_ANTIDIAB_ORD_DT | No | The ordering date of the last medication order for any injectable antidiabetic medication which is also on the patient's current medication list.  Rule: DM Med Last Current Injectable Antidiabetic (82388) |
| IS_PREGNANT_YN | No | Indicates whether the patient is pregnant.  "Y" indicates the patient is pregnant. "N" indicates the patient is not pregnant.  Rule: DM Diagnosis Is Patient Pregnant (82475) |
| HAS_HYPERTEN_YN | No | Indicates whether the patient has hypertension.  "Y" indicates the patient has hypertension. "N" indicates the patient does not have hypertension.  Rule: DM Diagnosis Does Patient Have Hypertension (82490) |
| HAS_CAD_YN | No | Indicates whether the patient has coronary artery disease (CAD.)  "Y" indicates the patient has CAD. "N" indicates the patient does not have CAD.  Rule: DM Diagnosis Does Patient Have Coronary Artery Disease (82476) |
| HAS_DIAB_REN_DIS_YN | No | Indicates whether the patient has diabetic renal disease.  "Y" indicates the patient has diabetic renal disease. "N" indicates the patient does not have diabetic renal disease.  Rule: DM Diagnosis Does Patient Have Diabetic Renal Disease (82491) |
| HAS_DIAB_RET_YN | No | Indicates whether the patient has diabetic retinopathy.  "Y" indicates the patient has diabetic retinopathy. "N" indicates the patient does not have diabetic retinopathy.  Rule: DM Diagnosis Does Patient Have Diabetic Retinopathy (82492) |
| HAS_PERI_VAS_DIS_YN | No | Indicates whether the patient has peripheral vascular disease.  "Y" indicates the patient has peripheral vascular disease. "N" indicates the patient does not have peripheral vascular disease.  Rule: DM Diagnosis Does Patient Have Peripheral Vascular Disease (82493) |
| HBA1C_L_ORD_ID | No | The unique ID of the procedure order associated with the patient's most recent hemoglobin A1C (HbA1C) value.    Rule: DM Lab Last Hemoglobin A1C (82200) |
| LDL_DIR_L_ORD_ID | No | The unique ID of the procedure order associated with the patient's most recent low-density lipoprotein (LDL) direct value.    Rule: DM Lab Last LDL Direct (82201) |
| HDL_L_ORD_ID | No | The unique ID of the procedure order associated with the patient's most recent high-density lipoprotein (HDL) value.   Rule: DM Lab Last HDL (82202) |
| VLDL_L_ORD_ID | No | The unique ID of the procedure order associated with the patient's most recent very low density lipoprotein (VLDL) value.    Rule: DM Lab Last VLDL (82203) |
| LDL_HDL_RT_L_ORD_ID | No | The unique ID of the procedure order associated with the patient's most recent LDL:HDL ratio value.    Rule: DM Lab Last LDL:HDL Ratio (82204) |
| TTL_CHL_L_ORD_ID | No | The unique ID of the procedure order associated with the patient's most recent total cholesterol value.    Rule: DM Lab Last Total Cholesterol (82205) |
| TRIGLY_L_ORD_ID | No | The unique ID of the procedure order associated with the patient's most recent triglycerides value.   Rule: DM Lab Last Triglycerides (82206) |
| BUN_L_ORD_ID | No | The unique ID of the procedure order associated with the patient's most recent blood urea nitrogen value.  Rule: DM Lab Last Blood Urea Nitrogen (82207) |
| UR_MALB_L_ORD_ID | No | The unique ID of the procedure order associated with the patient's most recent urine microalbumin value.    Rule: DM Lab Last Urine Microalbumin (82208) |
| UR_PROT_L_ORD_ID | No | The unique ID of the procedure order associated with the patient's most recent urine protein value.   Rule: DM Lab Last Urine Protein (82212) |
| PROT_CR_RT_L_ORD_ID | No | The unique ID of the procedure order associated with the patient's most recent protein:creatinine ratio value.   Rule: DM Lab Last Protein:Creatinine Ratio (82214) |
| CREAT_L_ORD_ID | No | The unique ID of the procedure order associated with the patient's most recent creatinine value.   Rule: DM Lab Last Creatinine (82209) |
| CREAT_CLR_L_ORD_ID | No | The unique ID of the procedure order associated with the patient's most recent creatinine clearance value.   Rule: DM Lab Last Creatinine Clearance (82210) |
| LDL_CALC_L_ORD_ID | No | The unique ID of the procedure order associated with the patient's most recent calculated low-density lipoprotein (LDL) value.  Rule: DM Lab Last LDL Calculated (82213) |
| HBA1C_L_LRR_ID | No | The unique ID of the component associated with the patient's most recent hemoglobin A1C (HbA1C) value.     Rule: DM Lab Last Hemoglobin A1C (82200) |
| LDL_DIR_L_LRR_ID | No | The unique ID of the component associated with the patient's most recent low-density lipoprotein (LDL) direct value.    Rule: DM Lab Last LDL Direct (82201) |
| HDL_L_LRR_ID | No | The unique ID of the component associated with the patient's most recent high-density lipoprotein (HDL) value.   Rule: DM Lab Last HDL (82202) |
| VLDL_L_LRR_ID | No | The unique ID of the component associated with the patient's most recent very low density lipoprotein (VLDL) value.   Rule: DM Lab Last VLDL (82203) |
| LDL_HDL_RT_L_LRR_ID | No | The unique ID of the component associated with the patient's most recent  LDL:HDL ratio value.    Rule: DM Lab Last LDL:HDL Ratio (82204) |
| TTL_CHL_L_LRR_ID | No | The unique ID of the component associated with the patient's most recent total cholesterol value.   Rule: DM Lab Last Total Cholesterol (82205) |
| TRIGLY_L_LRR_ID | No | The unique ID of the component associated with the patient's most recent triglycerides value.   Rule: DM Lab Last Triglycerides (82206) |
| BUN_L_LRR_ID | No | The unique ID of the component associated with the patient's most recent blood urea nitrogen value.  Rule: DM Lab Last Blood Urea Nitrogen (82207) |
| UR_MALB_L_LRR_ID | No | The unique ID of the component associated with the patient's most recent urine microalbumin value.    Rule: DM Lab Last Urine Microalbumin (82208) |
| UR_PROT_L_LRR_ID | No | The unique ID of the component associated with the patient's most recent urine protein value.   Rule: DM Lab Last Urine Protein (82212) |
| PROT_CR_RT_L_LRR_ID | No | The unique ID of the component associated with the patient's most recent protein:creatinine ratio value.   Rule: DM Lab Last Protein:Creatinine Ratio (82214) |
| CREAT_L_LRR_ID | No | The unique ID of the component associated with the patient's most recent creatinine value.   Rule: DM Lab Last Creatinine (82209) |
| CREAT_CLR_L_LRR_ID | No | The unique ID of the component associated with the patient's most recent creatinine clearance value.   Rule: DM Lab Last Creatinine Clearance (82210) |
| LDL_CALC_L_LRR_ID | No | The unique ID of the component associated with the patient's most recent calculated low-density lipoprotein (LDL) value.  Rule: DM Lab Last LDL Calculated (82213) |
| HBA1C_L_UNIT | No | The unit of the patient's most recent hemoglobin A1C (HbA1C) value.  Rule: DM Lab Last Hemoglobin A1C (82200) |
| LDL_DIR_L_UNIT | No | The unit of the patient's most recent low-density lipoprotein (LDL) direct value.  Rule: DM Lab Last LDL Direct (82201) |
| LDL_CALC_L_UNIT | No | The unit of the patient's most recent calculated low-density lipoprotein (LDL) value.  Rule: DM Lab Last LDL Calculated (82213) |
| HDL_L_UNIT | No | The unit of the patient's most recent high-density lipoprotein (HDL) value.  Rule: DM Lab Last HDL (82202) |
| VLDL_L_UNIT | No | The unit of the patient's most recent very low density lipoprotein (VLDL) value.  Rule: DM Lab Last VLDL (82203) |
| LDL_HDL_RT_L_UNIT | No | The unit of the patient's most recent LDL:HDL ratio value.  Rule: DM Lab Last LDL:HDL Ratio (82204) |
| TTL_CHL_L_UNIT | No | The unit of the patient's most recent total cholesterol value.  Rule: DM Lab Last Total Cholesterol (82205) |
| TRIGLY_L_UNIT | No | The unit of the patient's most recent triglycerides value.  Rule: DM Lab Last Triglycerides (82206) |
| BUN_L_UNIT | No | The unit of the patient's most recent blood urea nitrogen value.  Rule: DM Lab Last Blood Urea Nitrogen (82207) |
| UR_MALB_L_UNIT | No | The unit of the patient's most recent urine microalbumin value.  Rule: DM Lab Last Urine Microalbumin (82208) |
| UR_PROT_L_UNIT | No | The unit of the patient's most recent urine protein value.  Rule: DM Lab Last Urine Protein (82212) |
| PROT_CR_RT_L_UNIT | No | The unit of the patient's most recent protein:creatinine ratio value.  Rule: DM Lab Last Protein:Creatinine Ratio (82214) |
| CREAT_L_UNIT | No | The unit of the patient's most recent creatinine value.  Rule: DM Lab Last Creatinine (82209) |
| CREAT_CLR_L_UNIT | No | The unit of the patient's most recent creatinine clearance value.  Rule: DM Lab Last Creatinine Clearance (82210) |
| HAS_CELIAC_DIS_YN | No | Indicates whether the patient has celiac disease.  "Y" indicates the patient has celiac disease. "N" indicates the patient does not have celiac disease.  Rule: DM Diagnosis Does Patient Have Celiac Disease (82507) |
| TSH_LAST | No | The patient's most recent thyroid-stimulating hormone (TSH) value. Only numeric lab values are stored in this column.  Non-numeric lab values entered are displayed as null.  Rule: DM Lab Last TSH (82251) |
| TSH_LAST_DT | No | The date as per the prioritized instant of the patient's most recent thyroid-stimulating hormone (TSH) lab.  Rule: DM Lab Last TSH (82251) |
| TSH_L_ORD_ID | No | The unique ID of the procedure order associated with the patient's most recent thyroid-stimulating hormone (TSH) value.    Rule: DM Lab Last TSH (82251) |
| TSH_L_LRR_ID | No | The unique ID of the component associated with the patient's most recent thyroid-stimulating hormone (TSH) value.  Rule: DM Lab Last TSH (82251) |
| TSH_L_UNIT | No | The unit of the patient's most recent thyroid-stimulating hormone (TSH) value.  Rule: DM Lab Last TSH (82251) |
| TOBAC_PACK_YEAR | No | The most recently reported pack years for the patient.  Rule: DM History Last Pack Years (82158) |
| T3_LAST | No | The patient's most recent triiodothyronine (T3) value. Only numeric lab values are stored in this column.  Non-numeric lab values entered are displayed as null.  Rule: DM Lab Last T3 (82258) |
| T3_LAST_DT | No | The date as per the prioritized instant of the patient's most recent triiodothyronine (T3) lab.  Rule: DM Lab Last T3 (82258) |
| T3_L_ORD_ID | No | The unique ID of the procedure order associated with the patient's most recent triiodothyronine (T3) value.    Rule: DM Lab Last T3 (82258) |
| T3_L_LRR_ID | No | The unique ID of the component associated with the patient's most recent triiodothyronine (T3) value.    Rule: DM Lab Last T3 (82258) |
| T3_L_UNIT | No | The unit of the patient's most recent triiodothyronine (T3) value.  Rule: DM Lab Last T3 (82258) |
| T4_LAST | No | The patient's most recent thyroxine (T4) value. Only numeric lab values are stored in this column.  Non-numeric lab values entered are displayed as null.  Rule: DM Lab Last T4 (82257) |
| T4_LAST_DT | No | The date as per the prioritized instant of the patient's most recent thyroxine (T4) lab.  Rule: DM Lab Last T4 (82257) |
| T4_L_ORD_ID | No | The unique ID of the procedure order associated with the patient's most recent thyroxine (T4) value.    Rule: DM Lab Last T4 (82257) |
| T4_L_LRR_ID | No | The unique ID of the component associated with the patient's most recent thyroxine (T4) value.    Rule: DM Lab Last T4 (82257) |
| T4_L_UNIT | No | The unit of the patient's most recent thyroxine (T4) value.  Rule: DM Lab Last T4 (82257) |
| BMI_LAST_DT | No | The date the patient's most recent body mass index was recorded.  Rule: DM Vitals Last BMI (82108) |
| HAD_STROKE_YN | No | Indicates whether the patient has had a stroke in the specified timeframe. "Y" indicates the patient has had a stroke and "N" indicates the patient has not had a stroke.  Rule: DM Diagnosis Did Patient Have Stroke (82488) |
| HAD_HEART_ATTACK_YN | No | Indicates whether the patient has had a heart attack in the specified timeframe. "Y" indicates the patient has had a heart attack and "N" indicates the patient has not had a heart attack.  Rule: DM Diagnosis Did Patient Have Heart Attack (82542) |
| SMOKING_STATUS_C | No | The category value of the patient's last recorded smoking tobacco use status.  Rule: DM History Last Smoking Tobacco Use Status (82153) |
| SMOKING_USER_HX_YN | No | Indicates whether a patient was ever identified as a tobacco smoker.  Rule: DM History Is Previous Tobacco Smoker (82159) |
| SMOKING_USER_YN | No | Indicates whether a patient is currently identified as a tobacco smoker.  Rule: DM History Is Currently a Tobacco Smoker (82164) |
| SMOKING_QUIT_L_DT | No | Contains the patient's most recently recorded smoking tobacco quit date if the patient has previously quit smoking and does not currently smoke tobacco.  Rule: DM History Last Smoking Tobacco Quit Date (82165) |
| NUM_ED_VIS_DIABETES | No | The total number of times the patient visited the ED with a diabetes related diagnosis.  Rule: DM Encounter Number Of ED Visits For Diabetes (82055) |
| NUM_ED_VIS | No | The total number of times the patient visited ED.  Rule: DM Encounter Number Of ED Visits (82040) |
| FOOT_EXAM_HM_C | No | Indicates whether the patient is overdue for a foot exam.  Rule: DM Result Is Overdue For Foot Exam (82323) |
| ON_ACE_INHB_YN | No | Indicates whether an ACE inhibitor is on the patient's current medication list. "Y" indicates an ACE inhibitor is on the patient's current medication list. "N" indicates an ACE inhibitor is not on the patient's current medication list.  Rule: DM Med Is Prescribed ACE Inhibitors (82391) |
| ACE_INHB_ORD_ID | No | The unique ID of the last medication order for an ACE inhibitor which is also on the patient's current medication list.   Rule: DM Med Last Current ACE Inhibitor (82393) |
| ACE_INHB_ORD_DT | No | The ordering date of the last medication order for any ACE inhibitor medication which is also on the patient's current medication list.  Rule: DM Med Last Current ACE Inhibitor (82393) |
| ON_ARB_YN | No | Indicates whether an angiotensin II receptor blocker is on the patient's current medication list. "Y" indicates that the medication is on the patient's current medication list. "N" indicates it is not.  Rule: DM Med Is Prescribed Angiotensin II Receptor Blocker (82435) |
| ARB_ORD_ID | No | The unique ID of the last medication order for any angiotensin II receptor blocker medication which is also on the patient's current medication list.   Rule: DM Med Last Current Angiotensin II Receptor Blockers (82436) |
| ARB_ORD_DT | No | The ordering date of the last medication order for any angiotensin II receptor blocker medication which is also on the patient's current medication list.  Rule: DM Med Last Current Angiotensin II Receptor Blockers (82436) |
| FOOT_EXAM_L_DT | No |  |
| IMMNZTN_PNEUM_DT | No | The date the patient's most recent pneumonia vaccine was administered.  Rule: DM Imm Pneumonia Vaccine Administration Date (82371) |
| BMI_FIRST_DT | No | The date the patient's first recorded BMI in a given time period was recorded.  Rule: DM Vitals First BMI (82107) |
| AGE | No | Age of the patient.  Rule: DM GENERAL AGE [82005] |
| SEX_C | No | Sex of the patient.  Rule: DM GENERAL SEX [82006] |
| HEIGHT_FIRST | No | The patient's first recorded height in a given time period.  Rule: DM Vitals First Height (82109) |
| SC_DIAB_COMP | No | The current diabetes composite score for a patient.  Rule: DM Score Diabetes Composite [84350] |
| SC_DIAB_BP | No | The blood pressure component of the Diabetes Composite score.  Rule: DM Score Diabetes Composite Bp [84351] |
| SC_DIAB_LDL | FLOAT | The LDL treatment level for use in the statin component of the diabetes composite score. This is a number indicating the range in which the LDL value falls.  Rule: DM SCORE Diabetes Composite LDL Treatment Level (84352) |
| SC_DIAB_A1C | No | The A1c component of the Diabetes Composite score.  Rule: DM Score Diabetes Composite A1c [84353] |
| SC_DIAB_TOBAC_FREE | No | The smoking tobacco component of the Diabetes Composite score.  Rule: DM Score Diabetes Composite Tobacco-Free [84354] |
| SC_DIAB_ASPIRIN_USE | No | The Aspirin use component of the Diabetes Composite score.  Rule: DM Score Diabetes Composite Aspirin-Use [84355] |
| ASPIRIN_PRESCR_YN | No | Indicates whether any aspirin medication in the given grouper is on the patient's current medication list. "Y" indicates that an aspirin medication in the given grouper is found on the patient's current medication list. "N" indicates that no aspirin medication in the given grouper is found on the patient's current medication list.  Rule: DM Med Is Prescribed Aspirin [83279] |
| ASPIRIN_ORD_ID | No | The unique ID of the medication order associated with the patient's most recent aspirin medication.  Rule: DM Med Last Current Aspirin [83280] |
| ASPIRIN_ORD_DT | No | The date of the medication order associated with the patient's most recent aspirin medication.  Rule: DM Med Last Current Aspirin [83280] |
| HEIGHT_FIRST_DT | No | The date the patient's first recorded height in a given time period was recorded.  Rule: DM Vitals First Height (82109) |
| HAS_DYSLIPIDEMA_YN | No | Indicates whether the patient has dyslipidemia. "Y" indicates the patient has dyslipidemia and "N" indicates the patient doesn't have dyslipidemia.  Rule: DM Diagnosis Does Patient Have Dyslipidemia [82512] |
| HAS_NAFLD_YN | No | Indicates whether the patient has NAFLD (Non-Alcoholic Fatty Liver Disease). "Y" indicates the patient has NAFLD. "N" indicates the patient does not have NAFLD.  Rule: DM Diagnosis Does Patient Have NAFLD (84117) |
| HAS_OBESITY_YN | No | Indicates whether the patient has obesity. "Y" indicates the patient has obesity. "N" indicates the patient does not have obesity.  Rule: DM Diagnosis Does Patient Have Obesity (84123) |
| CUR_PRIM_PAYER_ID | No | The unique ID of the patient's primary payer.  Rule: PRIMARY PAYER (CER 19238) |
| CUR_PRIM_BEN_PLAN_ID | No | The unique ID of the patient's primary benefit plan.  Rule: PRIMARY BENEFIT PLAN (CER 19239) |
| CUR_PRIM_FIN_CLASS_C | No | The category value of the financial class of the patient's primary payer.  Rule: PRIMARY PAYER'S FINANCIAL CLASS (CER 19240) |
| CUR_PRIM_PROD_TYPE_C | No | The category value of the product type of the patient's primary payer.  Rule: PRIMARY PAYER'S PRODUCT TYPE (CER 19241) |
| SMOKELESS_STATUS_C | INTEGER | The category value of the patient's last recorded smokeless tobacco use status.  Datasource: I EPT 19219  Rule: DM HISTORY LAST SMOKELESS TOBACCO USE STATUS (CER 19188) |
| HAS_ASA_ALLERGY_YN | No | Indicates whether the patient has is allergic to ASA. "Y" indicates the patient is allergic and "N" indicates the patient is not allergic.  Rule: MR DOES PATIENT HAVE ASA ALLERGY (CER 19041) |
| ON_ANTICOAG_YN | No | Indicates whether an anticoagulant is on the patient's current medication list. "Y" indicates an anticoagulant is on the patient's current medication list. "N" indicates an anticoagulant is not on the patient's current medication list.  Rule: DM MED IS PRESCRIBED ANTICOAGULANTS (CER 19042) |
| HAS_IVD_YN | No | Indicates whether the patient has Ischemic Vascular Disease (IVD). "Y" indicates the patient has IVD and "N" indicates the patient doesn't have IVD.  Rule: DM DIAGNOSIS DOES PATIENT HAVE ISCHEMIC VASCULAR DISEASE (IVD) (CER 19046) |
| HBA1C_LAST_STR | VARCHAR (254) | The patient's most recent hemoglobin A1C (HbA1C) value.  Rule: DM Lab Last Hemoglobin A1C (82200) |
| LDL_HDL_RT_LAST_STR | VARCHAR (254) | The patient's most recent LDL:HDL ratio value.  Rule: DM Lab Last LDL:HDL Ratio (82204) |
| UR_MALB_LAST_STR | VARCHAR (254) | The patient's most recent urine microalbumin value.  Rule: DM Lab Last Urine Microalbumin (82208) |
| CREAT_CLR_LAST_STR | VARCHAR (254) | The patient's most recent creatinine clearance value.  Rule: DM Lab Last Creatinine Clearance (82210) |
| UR_PROT_LAST_STR | VARCHAR (254) | The patient's most recent urine protein value.  Rule: DM Lab Last Urine Protein (82212) |
| PROT_CR_RT_LAST_STR | VARCHAR (254) | The patient's most recent protein:creatinine ratio value.  Rule: DM Lab Last Protein:Creatinine Ratio (82214) |
| LIPID_PANEL_LAST_DT | DATETIME | The specimen collection date of the patient's most recent lipid panel.   Rule: DM LAB LAST LIPID PANEL SPECIMEN DATE (82302) |
| HAS_CVD_YN | VARCHAR (1) | This rule evaluates various inclusion criteria to determine whether a patient has cardiovascular disease (CVD) or a history of CVD.    Rule: DM DIAGNOSIS DOES PATIENT HAVE CARDIOVASCULAR DISEASE (19047) |
| ASCVD_10_YR_SCORE | FLOAT | The estimated risk of having an atherosclerotic cardiovascular disease (ASCVD) event in the next 10 years, displayed as a percentage. ASCVD events are defined as myocardial infarction, CHD death, or stroke.  Rule: DM Score 10 Year ASCVD Risk (19535) |
| ASCVD_10_YR_SC_MISSING_C | INTEGER | Category value to explain why the patient's ASCVD 10-year score is missing. "1" indicates the patient is not eligible. "2" indicates the patient's risk score is missing components. "3" indicates that the patient's risk score is invalid.  Rule: DM Score 10-Year ASCVD Risk (19535) |
| NONHISP_AFRICAN_AMER_YN | VARCHAR (1) | Indicates if the patient is a non-Hispanic African American.  Rule: DM General Is Patient A Non-Hispanic African American (19532) |
| PRIOR_ASCVD_EVENT_YN | VARCHAR (1) | Indicates whether or not the patient has had a prior Atherosclerotic Cardiovascular Disease (ASCVD) event. ASCVD events are defined as myocardial infarction, CHD death, or stroke.  Rule: DM Score Diagnosis Prior ASCVD Event (19534) |
| ASPIRIN_APPROPRIATE_YN | VARCHAR (1) | Indicates whether or not daily aspirin is appropriate for the patient.  Rule: DM SCORE DIABETES IS ASPIRIN APPROPRIATE (84388) |
| IS_BP_TREATED_YN | VARCHAR (1) | Indicates whether the patient's blood pressure is treated. Used by the ASCVD and CVD risk scores.  Rule: DM Is Treated For BP (19850) |
| HAS_HYPTN_PROB_YN | VARCHAR (1) | Indicates whether the patient has hypertension or a related blood pressure problem.  Rule: DM Diagnosis Does Patient Have Hypertension Or Related BP Problems (19852) |
| ON_BP_MED_YN | VARCHAR (1) | Indicates whether the patient is on antihypertensives specifically related to blood pressure treatment.  Rule: DM Med Is Prescribed Antihypertensive For BP (19851) |
| HAS_CLIN_ASCVD_YN | VARCHAR (1) | Indicates whether the patient has clinical atherosclerotic cardiovascular disease (ASCVD).  Rule: DM Diagnosis Does Patient Have Clinical ASCVD (19417) |
| SC_DIAB_STATIN_USE | FLOAT | The statin use component of the diabetes composite score.  Rule: DM SCORE Diabetes Composite Statin Use Score (19419) |
| SC_DIAB_STATIN_USE_CMT_C | INTEGER | Category value to help explain the statin use component of the diabetes composite score.  Rule: DM SCORE Diabetes Composite Statin Use Data (19420) |
| STATIN_RECOMMENDED_YN | VARCHAR (1) | Indicates whether statin use is recommended for the diabetic patient.  Rule: DM SCORE Diabetes Composite Is Statin Use Recommended (19418) |
| ENDOCRIN_ON_CARE_TEAM_YN | VARCHAR (1) | Indicates whether the patient has an endocrinologist on their care team.  Rule: DM General Has Endocrinologist On Care Team (83717) |
| GFR_L_DT | DATETIME | The date associated with the patient's most recent glomerular filtration rate (GFR) value.  Rule: DM Lab Last Glomerular Filtration Rate (CER 82248) |
| GFR_L_LRR_ID | NUMERIC (18,0) | The unique ID of the component associated with the patient's most recent glomerular filtration rate (GFR) value.  Rule: DM Lab Last Glomerular Filtration Rate (CER 82248) |
| GFR_L_ORD_ID | NUMERIC (18,0) | The unique ID of the procedure order associated with the patient's most recent glomerular filtration rate (GFR) value.  Rule: DM Lab Last Glomerular Filtration Rate (CER 82248) |
| GFR_L_STR | VARCHAR (254) | The patient's most recent glomerular filtration rate (GFR) value.  Rule: DM Lab Last Glomerular Filtration Rate (CER 82248) |
| GFR_L_UNIT | VARCHAR (100) | The unit associated with the patient's most recent glomerular filtration rate (GFR) value.  Rule: DM Lab Last Glomerular Filtration Rate (CER 82248) |
| GFR_LAST | FLOAT | The patient's most recent glomerular filtration rate (GFR) value. Only numeric lab values are stored in this column. Non-numeric lab values entered are displayed as null.  Rule: DM Lab Last Glomerular Filtration Rate (CER 82248) |
| HAD_KIDNEY_COMPLICATIONS_YN | VARCHAR (1) | Indicates whether the patient had kidney complications.  Rule: DM Surgery Did Patient Have Kidney Complications (83702) |
| HAD_LOWER_EXTREM_AMPUTATION_YN | VARCHAR (1) | Indicates whether the patient has had an amputation of the lower extremities.  Rule: DM Surgery Has Patient Had Amputation of Lower Extremities (CER 84511) |
| HAS_AFIB_YN | VARCHAR (1) | Indicates whether the patient has atrial fibrillation.   Rule: DM Diagnosis Does Patient Have Atrial Fibrillation (CER 82598) |
| HAS_ANEMIA_YN | VARCHAR (1) | Indicates whether the patient has anemia.  Rule: DM Diagnosis Does Patient Have Anemia (82481) |
| HAS_BRONCHIECTASIS_YN | VARCHAR (1) | Indicates whether the patient has bronchiectasis.  Rule: DM Diagnosis Does Patient Have Bronchiectasis (82503) |
| HAS_COPD_YN | VARCHAR (1) | Indicates whether the patient has chronic obstructive pulmonary disease (COPD).  Rule: DM Diagnosis Does Patient Have Chronic Obstructive Pulmonary Disease (84421) |
| HAS_EYE_COMPLICATIONS_YN | VARCHAR (1) | Indicates whether the patient has eye complications.  Rule: DM Diagnosis Does Patient Have Eye Complications (83706) |
| HAS_GASTROPARESIS_YN | VARCHAR (1) | Indicates whether the patient has gastroparesis.  Rule: DM Diagnosis Does Patient Have Gastroparesis (83703) |
| HAS_ISCHEMIC_HEART_DIS_YN | VARCHAR (1) | Indicates whether the patient has ischemic heart disease.  Rule: DM Diagnosis Does Patient Have Ischemic Heart Disease (CER 84513) |
| HAS_KETOACIDOSIS_YN | VARCHAR (1) |  |
| HAS_LYMPHOMAS_YN | VARCHAR (1) | Indicates whether the patient has lymphomas.  Rule: DM Diagnosis Does Patient Have Lymphomas (82537) |
| HAS_MEDICAID_COVERAGE_YN | VARCHAR (1) |  |
| HAS_MEDICARE_COVERAGE_YN | VARCHAR (1) |  |
| HAS_PERIP_NEURO_YN | VARCHAR (1) | Indicates whether the patient has peripheral neuropathy.  Rule: DM Diagnosis Does Patient Have Peripheral Neuropathy (82540) |
| HAS_SKIN_COMPLICATIONS_YN | VARCHAR (1) | Indicates whether the patient has skin complications.  Rule: DM Diagnosis Does Patient Have Skin Complications (83705) |
| HAS_TYPE_2_DIABETES_YN | VARCHAR (1) | Indicates whether the patient has type 2 diabetes.  Rule: DM Diagnosis Does Patient Have Type 2 Diabetes (CER 84126) |
| ON_ANESTHETIC_YN | VARCHAR (1) | Indicates whether an anesthetic is on the patient's current medication list.  Rule: DM Med Is Prescribed Anesthetics (83714) |
| ON_ANTI_ULCERS_YN | VARCHAR (1) | Indicates whether an anti-ulcer is on the patient's current medication list.  Rule: DM Med Is Prescribed Anti-Ulcers (83726) |
| ON_ANTISEIZURE_YN | VARCHAR (1) | Indicates whether an antiseizure is on the patient's current medication list.  Rule: DM Med Is Prescribed Antiseizures (82473) |
| ON_BETA_BLOCK_YN | VARCHAR (1) | Indicates whether a beta blocker is on the patient's current medication list.  Rule: DM Med Is Prescribed Beta Blockers (82390) |
| ON_CA_BLOCK_YN | VARCHAR (1) |  |
| ON_IMM_SUPPR_YN | VARCHAR (1) | Indicates whether an immunosuppressive drug is on the patient's current medication list.  Rule: DM Med Is Prescribed Immunosuppressive Drugs (83277) |
| ON_NON_OPIOID_ANALGESIC_YN | VARCHAR (1) | Indicates whether a non-opioid analgesic is on the patient's current medication list.  Rule: DM Med Is Prescribed Non-Opioid Analgesics (83713) |
| ON_OPIOID_ANALGESIC_YN | VARCHAR (1) |  |
| OPHTHALMOLOGY_REFERRAL_LAST_DT | DATETIME |  |
| PHY_THR_REFERRAL_LAST_DT | DATETIME |  |
| PODIATRY_REFERRAL_LAST_DT | DATETIME |  |
| RISK_NEG_OUT_TYPE_2_SCORE | FLOAT | The 2-year risk of negative outcomes for type 2 diabetes, displayed as the expected number of outcomes. Patients under 18 and those without type 2 diabetes will not be evaluated. If the score definition has not been clinically reviewed, the column will return null.  Rule: DM Score Risk of Negative Outcomes of Type 2 Diabetes (CER 84499) |
| SPEC_ON_CARE_TEAM_YN | VARCHAR (1) | Indicates whether the patient has a specialist on their care team.  Rule: DM General Has Specialist On Care Team (83716) |
| BP_SYS_LAST_REP | FLOAT | The lowest systolic blood pressure value from the day of the patient's most recent blood pressure reading.  Rule: DM Vitals Last Representative Systolic BP (82143) |
| BP_DIA_LAST_REP | FLOAT | The lowest diastolic blood pressure value from the day of the patient's most recent blood pressure reading.  Rule: DM Vitals Last Representative Diastolic BP (82144) |
| EYE_EXAM_L_DT | DATETIME | The date the patient last had an eye exam performed.  Rule: DM Score Last Eye Exam Date (84978) |
| NEG_EYE_EXAM_L_DT | DATETIME | The date the patient last had a negative (no evidence of retinopathy) eye exam performed.  Rule: DM Score Last Negative Eye Exam Date (84956) |
| HAD_KIDNEY_TRANSPLANT_YN | VARCHAR (1) | Indicates whether the patient has had a kidney transplant. "Y" indicates the patient had a kidney transplant, "N" indicates the patient did not have kidney transplant.  Rule: DM Surgery Has Patient Had Kidney Transplant (82569) |
| HAS_FOOT_ULCER_YN | VARCHAR (1) | Indicates whether the patient has a foot ulcer.  Rule: DM Diagnosis Does Patient Have Foot Ulcer (84944) |
| HAS_FEET_YN | VARCHAR (1) | Indicates whether the patient has feet.  Rule: DM General Has Feet (84988) |
| FOOT_EXAM_LAST_DT | DATETIME | The date the patient last had a foot exam performed.  Rule: DM Score Last Foot Exam Date (82510) |
| GFR_L_2_DT | DATETIME | Rule: DM LAB LAST GLOMERULAR FILTRATION RATE (90083483) |
| GFR_L_2_LRR_ID | NUMERIC (18,0) | Rule: DM LAB LAST GLOMERULAR FILTRATION RATE (90083483) |
| GFR_L_2_ORD_ID | NUMERIC (18,0) | Rule: DM LAB LAST GLOMERULAR FILTRATION RATE (90083483) |
| GFR_L_2_STR | VARCHAR (254) | Rule: DM LAB LAST GLOMERULAR FILTRATION RATE (90083483) |
| GFR_L_2_UNIT | VARCHAR (100) | Rule: DM LAB LAST GLOMERULAR FILTRATION RATE (90083483) |
| GFR_LAST_2 | FLOAT | Rule: DM LAB LAST GLOMERULAR FILTRATION RATE (90083483) |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| B-TREE INDEX | EIX_DM_DIABETES_PATID | PAT_ID | 1 | Yes | Yes |  |

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

_(2459 total; showing first 30)_
