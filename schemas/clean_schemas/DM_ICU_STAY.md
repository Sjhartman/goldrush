# DM_ICU_STAY

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=DM_ICU_STAY

## Description

DM_ICU_STAY is a data mart table that stores information related to ICU stays. This table consolidates patient information from many subject areas including medications, procedures, LDAs, ventilators, physiological data, and stays. Only patients that had an ICU stay have their information stored in this table.

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
| ICU_STAY_BLOCK_ID | NUMERIC (18,0) | The ID for the Block of Time record for this ICU Stay. This column is commonly used to join to the BLOCKS_OF_TIME table. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| ICU_LENGTH_OF_STAY_DAYS | No | The duration, in days, between the start and end of a patient's ICU stay.  Rule: DM ICU STAY LENGTH OF STAY (36128) |
| NEXT_DEPARTMENT_ID | No | The ID of the department that a patient was in immediately after the patient?s ICU stay. It will be blank if the block of time record was not created using Patient Location events or if there is no subsequent department.  Rule: DM ICU STAY NEXT DEPARTMENT (36001) |
| PREV_DEPARTMENT_ID | No | The ID of the department that a patient was in immediately before the patient?s ICU stay. It will be blank if the block of time record was not created using Patient Location events or if there is no previous department.  Rule: DM ICU STAY PREVIOUS DEPARTMENT (36002) |
| PREV_ICU_DEPARTMENT_ID | No | The ID of the most recent ICU department that a patient was in prior to the current ICU stay that is within the same encounter. The last department will either be the ICU stay?s initial department if there are no interrupts, or the last resume department if the ICU stay has one or more interrupts. It will be blank if the patient has only had one ICU stay during this encounter.  Rule: DM ICU STAY PREVIOUS ICU (36003) |
| METHOD_OF_VENTILATION | No | The most recent Method of Ventilation value documented between the start and end instants of an ICU stay.  Rule: DM VENTILATOR METHOD OF VENTILATION (36004) |
| DVT_PROPHYLAXIS_BOOL | No | Indicates whether a patient underwent deep vein thrombosis (DVT) prophylaxis during an ICU stay. It contains 1 if DVT was documented as having occurred during an ICU stay, or 0 otherwise.  Rule: DM FLOWSHEET RECEIVED DVT PROPHYLAXIS (36005) |
| DELIRIUM_PRESENT_BOOL | No | Indicates whether a patient experienced delirium during an ICU stay. It contains 1 if delirium was documented as having been present during an ICU stay, or 0 otherwise.  Rule: DM FLOWSHEET DELIRIUM PRESENT (36006) |
| BED_AT_30_DEGREES_BOOL | No | Indicates whether the head of a patient?s bed was at 30? during an ICU stay. It contains 1 if the head of the patient?s bed was documented as being at 30? during an ICU stay, or 0 otherwise.  Rule: DM FLOWSHEET HEAD OF BED AT 30 DEGREES (36007) |
| HAD_ILEUS_BOOL | No | Indicates whether ileus was documented for a patient during an ICU stay. It contains 1 if ileus was documented as having occurred during an ICU stay, or 0 otherwise.  Rule: DM FLOWSHEET ILEUS DOCUMENTED (36008) |
| RECEIVED_HEMODIALYSIS_BOOL | No | Indicates whether a patient underwent hemodialysis during an ICU stay. It contains 1 if hemodialysis was documented as having occurred during an ICU stay, or 0 otherwise.  Rule: DM FLOWSHEET RECEIVED HEMODIALYSIS (36009) |
| RECEIVED_ORAL_CARE_BOOL | No | Indicates whether a patient received oral care during an ICU stay. It contains 1 if oral care was documented as having been received during an ICU stay, or 0 otherwise.  Rule: DM FLOWSHEET RECEIVED ORAL CARE (36010) |
| SBT_PASSED_BOOL | No | Indicates whether a patient passed a spontaneous breathing trial (SBT) during an ICU stay. It contains 1 if a patient was documented as having passed an SBT during an ICU stay, or 0 otherwise.  Rule: DM FLOWSHEET PASSED SPONTANEOUS BREATHING TRIAL (36011) |
| SBT_PERFORMED_BOOL | No | Indicates whether a patient underwent a spontaneous breathing trial (SBT) during an ICU stay. It contains 1 if an SBT was documented as having occurred during an ICU stay, or 0 otherwise.  Rule: DM FLOWSHEET SPONTANEOUS BREATHING TRIAL PERFORMED (36012) |
| SAT_PASSED_BOOL | No | Indicates whether a patient passed a sedation awakening trial (SAT) during an ICU stay. It contains 1 if a patient was documented as having passed an SAT during an ICU stay, or 0 otherwise.  Rule: DM FLOWSHEET PASSED SEDATION AWAKENING TRIAL (36013) |
| SAT_PERFORMED_BOOL | No | Indicates whether a patient underwent a sedation awakening trial (SAT) during an ICU stay. It contains 1 if an SAT was documented as having occurred during an ICU stay, or 0 otherwise.  Rule: DM FLOWSHEET SEDATION AWAKENING TRIAL PERFORMED (36014) |
| SIG_EDEMA_OR_POS_FLUID_BOOL | No | Indicates whether a patient had a significant edema or positive fluid balance during an ICU stay. This is primarily relevant for NICU patients. It contains 1 if a significant edema or positive fluid balance (greater than 20 ml/kg over 24 hours) was documented as having occurred during an ICU stay, or 0 otherwise.  Rule: DM SEPSIS HAD SIGNIFICANT EDEMA OR POSITIVE FLUID BALANCE (36015) |
| FIRST_FEEDING_DTTM | DATETIME (Local) | The instant of a patient?s first feeding during an ICU stay. This is primarily relevant for NICU patients.  Rule: DEPRECATED DM FLOWSHEET TIME OF FIRST FEEDING (36016) Rule: DM FLOWSHEET TIME OF FIRST FEEDING (36129) |
| TISSUE_HYPOPERFUSION_BOOL | No | Indicates whether tissue hypoperfusion was present for a patient during an ICU stay. This is intended to help identify and treat sepsis. It contains 1 if tissue hypoperfusion was documented as having been present during an ICU stay, or 0 otherwise.  Rule: DM FLOWSHEET HAD TISSUE HYPOPERFUSION (36017) |
| TISSUE_HYPERPERFUSION_BOOL | No | Indicates whether tissue hyperperfusion was present for a patient during an ICU stay. This is intended to help identify and treat sepsis. It contains 1 if tissue hyperperfusion was documented as having been present during an ICU stay, or 0 otherwise.  Rule: DM FLOWSHEET HAD TISSUE HYPERPERFUSION (36018) |
| TRANSCUTANEOUS_PACG_TREAT_BOOL | No | Indicates whether a patient received transcutaneous pacing treatment during an ICU stay. It contains 1 if transcutaneous pacing treatment was documented as having occurred during an ICU stay, or 0 otherwise.  Rule: DM FLOWSHEET RECEIVED TRANSCUTANEOUS PACING TREATMENT (36019) |
| TRANSCUTANEOUS_PACG_TREAT_HRS | No | The number of hours of transcutaneous pacing treatment a patient has received during an ICU stay.  Rule: DM FLOWSHEET HOURS OF TRANSCUTANEOUS PACING TREATMENT (36090) |
| APACHE_II_DX | No | The primary APACHE II diagnosis documented for a patient during an ICU stay.  Rule: DM DIAGNOSIS APACHE II PRIMARY DIAGNOSIS (36020) |
| APACHE_IV_DX | No | The primary APACHE IV diagnosis documented for a patient during an ICU stay.  Rule: DM DIAGNOSIS APACHE IV PRIMARY DIAGNOSIS (36021) |
| DEC_CAP_REFILL_OR_MOTTLG_BOOL | No | Indicates whether a patient experienced decreased capillary refill or mottling during an ICU stay. It contains 1 if decreased capillary refill or mottling was documented as having occurred during an ICU stay, or 0 otherwise.  Rule: DM SEPSIS EXPERIENCED DECREASED CAPILLARY REFILL OR MOTTLING (36022) |
| ANTIBIOTIC_GIVEN_BOOL | No | Indicates whether antibiotics were administered to a patient during an ICU stay. It contains 1 if any of the medications in the antibiotic groupers were administered between the start and end instants of an ICU stay, or 0 if none of the medications in the groupers were administered between the start and end instants.  Rule: DM MED GIVEN ANTIBIOTIC (36023) |
| VASODILATORS_GIVEN_BOOL | No | Indicates whether vasodilators were administered to a patient during an ICU stay. It contains 1 if any of the medications in the vasodilator groupers were administered between the start and end instants of an ICU stay, or 0 if none of the medications in the groupers were administered between the start and end instants.  Rule: DM MED GIVEN VASODILATORS (36024) |
| VASOPRESSORS_GIVEN_BOOL | No | Indicates whether vasopressors were administered to a patient during an ICU stay. It contains 1 if any of the medications in the vasopressor groupers were administered between the start and end instants of an ICU stay, or 0 if none of the medications in the groupers were administered between the start and end instants.  Rule: DM MED GIVEN VASOPRESSORS (36025) |
| CONTINUOUS_SEDATION_BOOL | No | Indicates whether a patient received continuous sedation during an ICU stay. It contains 1 if sedation medications were administered between the start and end instants of an ICU stay, or 0 otherwise.  Rule: DM MED RECEIVED CONTINUOUS SEDATION (36026) |
| IS_ICU_READMISSION_BOOL | No | Indicates whether the associated ICU Stay is an ICU readmission. It contains 1 if the following are true: The patient was previously in an ICU in the same location in the same inpatient encounter and the patient was bedded in a non-ICU department between a previous ICU Stay and the current ICU Stay. Otherwise, it contains 0.  Rule: DM ICU STAY HAD ICU READMISSION (36027) |
| COMFORT_OR_PALLIATIVE_BOOL | No | Indicates whether comfort measures or palliative care were provided for a patient during an ICU stay. It contains 1 if a patient had orders for one or more of the comfort measures or palliative care groupers active between the start and end instants of an ICU stay, or 0 if no orders for the procedures in the groupers were active between the start and end instants.  Rule: DM ORDER COMFORT MEASURES/PALLIATIVE CARE PROVIDED (36028) |
| C_REACTIVE_PROTEIN_LAST_VALUE | No | The last C-reactive protein lab value that was collected during an ICU stay.  Rule: DM LAB LAST C-REACTIVE PROTEIN (36029) |
| C_REACTIVE_PROTEIN_MAX_VALUE | No | The maximum C-reactive protein lab value that was collected during an ICU stay.  Rule: DM LAB MAX C-REACTIVE PROTEIN (36030) |
| CREATININE_MAX_COLL_VALUE | No | The maximum creatinine lab value that was collected during an ICU stay.  Rule: DM LAB MAX CREATININE (36031) |
| CREATININE_MIN_COLL_VALUE | No | The minimum creatinine lab value that was collected during an ICU stay.  Rule: DM LAB MIN CREATININE (36032) |
| HEMATOCRIT_LAST_COLL_VALUE | No | The last hematocrit lab value that was collected during an ICU stay.  Rule: DM LAB LAST HEMATOCRIT (36033) |
| HEMATOCRIT_MAX_COLL_VALUE | No | The maximum hematocrit lab value that was collected during an ICU stay.  Rule: DM LAB MAX HEMATOCRIT (36034) |
| HEMATOCRIT_MIN_COLL_VALUE | No | The minimum hematocrit lab value that was collected during an ICU stay.  Rule: DM LAB MIN HEMATOCRIT (36035) |
| INR_LAST_COLL_VALUE | No | The last INR lab value that was collected during an ICU stay.  Rule: DM LAB LAST INR (36036) |
| INR_MAX_COLL_VALUE | No | The maximum INR lab value that was collected during an ICU stay.  Rule: DM LAB MAX INR (36037) |
| INR_MIN_COLL_VALUE | No | The minimum INR lab value that was collected during an ICU stay.  Rule: DM LAB MIN INR (36038) |
| PARTIAL_THROMBOPLASTIN_TM_LAST | No | The last partial thromboplastin time lab value that was collected during an ICU stay.  Rule: DM LAB LAST PARTIAL THROMBOPLASTIN TIME (36039) |
| PARTIAL_THROMBOPLASTIN_TM_MAX | No | The maximum partial thromboplastin time lab value that was collected during an ICU stay.  Rule: DM LAB MAX PARTIAL THROMBOPLASTIN TIME (36040) |
| PROTHROMBIN_TIME_LAST_COLL_VAL | No | The last prothrombin time lab value that was collected during an ICU stay.  Rule: DM LAB LAST PROTHROMBIN TIME (36041) |
| PROTHROMBIN_TIME_MAX_COLL_VAL | No | The maximum prothrombin time lab value that was collected during an ICU stay.  Rule: DM LAB MAX PROTHROMBIN TIME (36042) |
| EXP_IN_HOSPITAL_BOOL | No | Indicates whether a patient died during a hospital stay. It contains 1 if a patient has been marked as deceased during an encounter that included an ICU stay, or 0 otherwise.  Rule: DM GENERAL EXPIRED IN HOSPITAL (36043) |
| EXP_IN_ICU_BOOL | No | Indicates whether a patient died during an ICU stay. It contains 1 if a patient has been marked as deceased and his date and time of death occurred during an ICU stay, or 0 otherwise.  Rule: DM GENERAL EXPIRED IN ICU (36044) |
| EXPECTED_DEATH_BOOL | No | Indicates whether a patient?s passing was an expected death. It contains 1 if a patient?s passing during an ICU stay was expected, based on a procedure order and if a patient was discharged as deceased, or 0 otherwise.  Rule: DM GENERAL EXPECTED DEATH (36126) |
| UNEXPECTED_DEATH_BOOL | No | Indicates whether a patient?s passing was an unexpected death. It contains 1 if a patient?s passing during an ICU stay was unexpected, based on a procedure order and if a patient was discharged as deceased, or 0 otherwise.  Rule: DM GENERAL UNEXPECTED DEATH (36127) |
| RASS_LAST_RECORDED_SCORE | No | The last Richmond Agitation Sedation Scale (RASS) score that was documented during an ICU stay.  Rule: DM SCORE LAST RASS SCORE (36045) |
| RASS_MAX_RECORDED_SCORE | No | The maximum Richmond Agitation Sedation Scale (RASS) score that was documented during an ICU stay.   Rule: DM SCORE MAX RASS SCORE (36046) |
| POSITIVE_CAM_ICU_SCORE_BOOL | No | Indicates whether a patient has a positive Confusion Assessment Method for the ICU (CAM-ICU) score documented during an ICU stay. It contains 1 if a patient has a positive CAM-ICU score documented during an ICU stay, or 0 otherwise.  Rule: DM SCORE HAD POSITIVE CAM-ICU SCORE (36047) |
| CENTRAL_VENOUS_PRESSURE_LAST | No | The last central venous pressure value that was documented during an ICU stay.  Rule: DM VITALS LAST CENTRAL VENOUS PRESSURE (36048) |
| CENTRAL_VENOUS_PRESSURE_MAX | No | The maximum central venous pressure value that was documented during an ICU stay.  Rule: DM VITALS MAX CENTRAL VENOUS PRESSURE (36049) |
| CORE_TEMPERATURE_MAX_VALUE | No | The maximum core temperature value that was documented during an ICU stay.  Rule: DM VITALS MAX CORE TEMP (36050) |
| CORE_TEMPERATURE_MIN_VALUE | No | The minimum core temperature value that was documented during an ICU stay.  Rule: DM VITALS MIN CORE TEMP (36051) |
| FIO2_LAST_RECORDED_VALUE | No | The last FIO2 value that was documented during an ICU stay.  Rule: DM VENTILATOR LAST FIO2 (36052) |
| FIO2_MAX_RECORDED_VALUE | No | The maximum FIO2 value that was documented during an ICU stay.  Rule: DM VENTILATOR MAX FIO2 (36053) |
| GCS_24_HOURS_AFTER_ADMISSION | No | The Glasgow Coma Scale (GCS) score that was documented after the first 24 hours of an ICU stay.  Rule: DM SCORE GCS 24H AFTER ADMISSION (36054) |
| GCS_LAST_RECORDED_SCORE | No | The last Glasgow Coma Scale (GCS) score that was documented during an ICU stay.  Rule: DM SCORE LAST GCS (36055) |
| GCS_MIN_RECORDED_SCORE | No | The minimum Glasgow Coma Scale (GCS) score that was documented during an ICU stay.  Rule: DM SCORE MIN GCS (36056) |
| ICDSC_LAST_RECORDED_SCORE | No | The last Intensive Care Delirium Screening Checklist (ICDSC) score that was documented during an ICU stay.  Rule: DM SCORE LAST ICDSC SCORE (36057) |
| ICDSC_MAX_RECORDED_SCORE | No | The maximum Intensive Care Delirium Screening Checklist (ICDSC) score that was documented during an ICU stay.  Rule: DM SCORE MAX ICDSC SCORE (36058) |
| MEAN_ARTERIAL_PRESSURE_LAST | No | The last mean arterial pressure (MAP) value that was documented during an ICU stay.  Rule: DM VITALS LAST MEAN ARTERIAL PRESSURE (36059) |
| MEAN_ARTERIAL_PRESSURE_MIN | No | The minimum mean arterial pressure (MAP) value that was documented during an ICU stay.  Rule: DM VITALS MIN MEAN ARTERIAL PRESSURE (36060) |
| PEEP_MIN_RECORDED_VALUE | No | The minimum positive end-expiratory pressure (PEEP) value that was documented during an ICU stay.  Rule: DM VENTILATOR MIN PEEP (36061) |
| PULSE_MAX_RECORDED_VALUE | No | The maximum pulse value that was documented during an ICU stay.  Rule: DM VITALS MAX PULSE (36062) |
| PULSE_MIN_RECORDED_VALUE | No | The minimum pulse value that was documented during an ICU stay.  Rule: DM VITALS MIN PULSE (36063) |
| SAPS_II_LAST_RECORDED_SCORE | No | The last Simplified Acute Physiology Score (SAPS) II score that was documented during an ICU stay.  Rule: DM SCORE LAST SAPS II SCORE (36064) |
| SAPS_II_MAX_RECORDED_SCORE | No | The maximum Simplified Acute Physiology Score (SAPS) II score that was documented during an ICU stay.  Rule: DM SCORE MAX SAPS II SCORE (36065) |
| SOFA_LAST_RECORDED_SCORE | No | The last Sequential Organ Failure Assessment (SOFA) score that was documented during an ICU stay.  Rule: DM SCORE LAST SOFA SCORE (36066) |
| SOFA_MAX_RECORDED_SCORE | No | The maximum Sequential Organ Failure Assessment (SOFA) score that was documented during an ICU stay.  Rule: DM SCORE MAX SOFA SCORE (36067) |
| SYSTOLIC_BP_MAX_RECORDED_VALUE | No | The maximum systolic blood pressure value that was documented during an ICU stay.  Rule: DM VITALS MAX SYSTOLIC BP (36068) |
| SYSTOLIC_BP_MIN_RECORDED_VALUE | No | The minimum systolic blood pressure value that was documented during an ICU stay.  Rule: DM VITALS MIN SYSTOLIC BP (36069) |
| TEMPERATURE_FIRST_VALUE | No | The first temperature value that was documented during an ICU stay.  Rule: DM VITALS FIRST TEMPERATURE (36070) |
| TEMPERATURE_MAX_VALUE | No | The maximum temperature value that was documented during an ICU stay.  Rule: DM VITALS MAX TEMPERATURE (36071) |
| TEMPERATURE_MIN_VALUE | No | The minimum temperature value that was documented during an ICU stay.  Rule: DM VITALS MIN TEMPERATURE (36072) |
| URINE_OUTPUT_LAST_VALUE | No | The last urine output value that was documented during an ICU stay.  Rule: DM I/O LAST URINE OUTPUT (36073) |
| URINE_OUTPUT_MAX_VALUE | No | The maximum urine output value that was documented during an ICU stay.  Rule: DM I/O MAX URINE OUTPUT (36074) |
| URINE_OUTPUT_MIN_VALUE | No | The minimum urine output that was documented during an ICU stay.  Rule: DM I/O MIN URINE OUTPUT (36075) |
| NUM_REINTUBATIONS_WITHIN_24_HR | No | The number of times a patient was reintubated less than 24 hours post-extubation during an ICU stay, or 0 if the patient was not reintubated during an ICU stay.  Rule: DM LDA NUMBER OF REINTUBATIONS <24 HOURS POST-EXTUBATION (36076) |
| REINTUBATION_WITHIN_24_HR_BOOL | No | Indicates whether a patient has been reintubated less than 24 hours post-extubation. It contains 1 if a patient had a reintubation less than 24 hours post-extubation during an ICU stay, or 0 if the patient was not reintubated during an ICU stay.  Rule: DM LDA REINTUBATION OCCURRED <24 HOURS POST-EXTUBATION (36077) |
| NUM_REINTUBATIONS_WITHIN_48_HR | No | The number of times a patient was reintubated less than 48 hours post-extubation during an ICU stay, or 0 if the patient was not reintubated during an ICU stay.  Rule: DM LDA NUMBER OF REINTUBATIONS <48 HOURS POST-EXTUBATION (36124) |
| REINTUBATION_WITHIN_48_HR_BOOL | No | Indicates whether a patient has been reintubated less than 48 hours post-extubation. It contains 1 if a patient had a reintubation less than 48 hours post-extubation during an ICU stay, or 0 if the patient was not reintubated during an ICU stay.  Rule: DM LDA REINTUBATION OCCURRED <48 HOURS POST-EXTUBATION (36125) |
| ALBUMIN_LAST_COLL_VALUE | No | The last albumin lab value that was collected during an ICU stay.  Rule: DM LAB LAST ALBUMIN (36078) |
| ALBUMIN_MAX_COLL_VALUE | No | The maximum albumin lab value that was collected during an ICU stay.  Rule: DM LAB MAX ALBUMIN (36079) |
| BILIRUBIN_LAST_COLL_VALUE | No | The last bilirubin lab value that was collected during an ICU stay.  Rule: DM LAB LAST BILIRUBIN (36080) |
| BILIRUBIN_MAX_COLL_VALUE | No | The maximum bilirubin lab value that was collected during an ICU stay.  Rule: DM LAB MAX BILIRUBIN (36081) |
| BLOOD_GLUCOSE_MAX_COLL_VALUE | No | The maximum blood glucose lab value that was collected during an ICU stay.  Rule: DM LAB MAX BLOOD GLUCOSE (36082) |
| BLOOD_GLUCOSE_MIN_COLL_VALUE | No | The minimum blood glucose lab value that was collected during an ICU stay.  Rule: DM LAB MIN BLOOD GLUCOSE (36083) |
| CLB_COMP_BARRIER_PRECAUTIONS | No | Indicates central line bundle compliance for the barrier precautions criterion. It contains 1 if a patient had one or more central lines placed during an ICU stay and the documentation was compliant for barrier precautions for all lines, or 0 if a patient had one or more central lines placed and the documentation for one or more of those central lines was not compliant for barrier precautions. It will be blank if there was no central line placed or if it's not possible to determine if all central lines that were placed were compliant for barrier precautions.  Rule: DM CLB BARRIER PRECAUTIONS (36084) |
| CLB_COMP_HAND_HYGIENE | No | Indicates central line bundle compliance for the hand hygiene criterion. It contains 1 if a patient had one or more central lines placed during an ICU stay and the documentation was compliant for hand hygiene for all lines, or 0 if a patient had one or more central lines placed and the documentation for one or more of those central lines was not compliant for hand hygiene. It will be blank if there was no central line placed or if it's not possible to determine if all central lines that were placed were compliant for hand hygiene.  Rule: DM CLB HAND HYGIENE (36085) |
| CLB_COMP_DAILY_REVIEW | No | Indicates central line bundle compliance for the daily review criterion. Contains the number of days that a patient was missing daily review documentation if she had a central line during an ICU stay. It will be blank if a patient did not have a central line, or 0 if the daily review documentation was completed for every day that a patient had a central line.  Rule: DM CLB DAILY LINE REVIEW (36086) |
| CLB_COMP_SITE_SELECTION | No | Indicates central line bundle compliance for the optimal site selection criterion. It contains 1 if a patient had one or more central lines placed during an ICU stay and the documentation was compliant for optimal site selection for all lines, or 0 if a patient had one or more central lines placed and the documentation for one or more of those central lines was not compliant for optimal site selection. It will be blank if there was no central line placed or if it's not possible to determine if all central lines that were placed were compliant for optimal site selection.  Rule: DM CLB OPTIMAL SITE SELECTION (36087) |
| CLB_COMP_SKIN_ANTISEPSIS | No | Indicates central line bundle compliance for the skin antisepsis precautions criterion. It contains 1 if a patient had one or more central lines placed during an ICU stay and the documentation was compliant for skin antisepsis precautions for all lines, or 0 if a patient had one or more central lines placed and the documentation for one or more of those central lines was not compliant for skin antisepsis precautions. It will be blank if there was no central line placed or if it's not possible to determine if all central lines that were placed were compliant for skin antisepsis precautions.  Rule: DM CLB SKIN ANTISEPSIS (36088) |
| VENTILATOR_DURATION_DAYS | No | The duration, in days, between the start and end documentation for a ventilator episode which occurred during an ICU stay.  Rule: DM VENTILATOR DAYS ON VENTILATOR (36089) |
| IABP_DURATION_HOURS | No | The number of hours of intra-aortic balloon pump (IABP) treatment a patient has received during an ICU stay.  Rule: DM FLOWSHEET HOURS ON IABP (36091) |
| HAD_RESTRAINTS_BOOL | No | Indicates whether a patient has been placed in restraints. It contains 1 if at least one episode overlaps with an ICU stay, or 0 if no episodes exist or no episodes overlap with an ICU stay.  Rule: DM FLOWSHEET PATIENT ON RESTRAINTS (36092) |
| HAD_VENTILATOR_EPISODE_BOOL | No | Indicates whether a patient had a ventilator episode. It contains 1 if at least one ventilator episode overlaps with an ICU stay, or 0 if no episodes exist or no episodes overlap with an ICU stay.  Rule: DM VENTILATOR PATIENT ON VENTILATOR (36093) |
| CULTURE_BEFORE_ANTIBIOTIC_BOOL | No | Indicates whether a patient had a culture obtained prior to giving antibiotics. It contains 1 if a patient had a culture obtained prior to giving antibiotics, or 0 otherwise.  Rule: DM SEPSIS CULTURE OBTAINED PRIOR TO GIVING ANTIBIOTICS (36094) |
| CENTRAL_LINE_DURATION_DAYS | No | The duration, in days, between the placement and removal of a central line during an ICU stay, or 0 if no central line was in place.  Rule: DM LDA CENTRAL LINE DAYS (36095) |
| FOLEY_CATHETER_DURATION_DAYS | No | The duration, in days, between the placement and removal of a Foley during an ICU stay, or 0 if no Foley was in place.  Rule: DM LDA FOLEY CATHETER DAYS (36096) |
| INTUBATION_DURATION_DAYS | No | The duration, in days, between the placement and removal of an intubation during an ICU stay, or 0 if no intubation occurred.  Rule: DM LDA INTUBATION DAYS (36097) |
| HAD_EXTUBATION_BOOL | No | Indicates whether a patient had an extubation during an ICU stay. It contains 1 if a patient had an extubation during an ICU stay, or 0 if no extubation occurred.  Rule: DM LDA PATIENT EXTUBATED (36098) |
| HAD_CENTRAL_LINE_BOOL | No | Indicates whether a patient had a central line during an ICU stay. It contains 1 if a patient had an active central line during an ICU stay, or 0 if no central lines were active.  Rule: DM LDA HAD CENTRAL LINE (36099) |
| HAD_FOLEY_CATHETER_BOOL | No | Indicates whether a patient had a Foley in place during an ICU stay. It contains 1 if a patient had a Foley in place during an ICU stay, or 0 if no Foleys were in place.  Rule: DM LDA HAD FOLEY CATHETER (36100) |
| INTUBATED_BOOL | No | Indicates whether a patient was intubated during an ICU stay. It contains 1 if a patient was intubated during an ICU stay, or 0 if no intubations occurred.  Rule: DM LDA PATIENT INTUBATED (36101) |
| HAD_PRESSURE_ULCER_BOOL | No | Indicates whether a patient had a pressure ulcer during an ICU stay. It contains 1 if a patient had a pressure ulcer during an ICU stay, or 0 if there were no pressure ulcers.  Rule: DM LDA HAD PRESSURE ULCER (36102) |
| APACHE_II_24_HR_AFTER_ADMSN | No | The APACHE II score that was documented 24 hours after an ICU admission.  Rule: DM SCORE APACHE II SCORE 24H AFTER ADMISSION (36103) |
| APACHE_II_FIRST_RECORDED_SCORE | No | The first APACHE II score that was documented during an ICU stay.  Rule: DM SCORE FIRST APACHE II SCORE (36104) |
| APACHE_IV_24_HR_AFTER_ADMSN | No |  |
| APACHE_IV_FIRST_RECORDED_SCORE | No |  |
| PREDICTED_LENGTH_OF_STAY_DAYS | No | The patient?s predicted length of stay.  Rule: DM SCORE PREDICTED LENGTH OF STAY (DAYS) (36107) |
| PREDICTED_MORTALITY | No | The patient's predicted mortality. This score is assumed to be a percentage score measuring the likelihood that a patient will die during a visit. If you are using a score that is not measured from 0 to 100, then you should convert the score to that scale in the attached rule.  Rule: DM SCORE PREDICTED MORTALITY (36108) |
| LACTATE_LAST_COLL_VALUE | No | The last lactate lab value that was collected during an ICU stay.  Rule: DM LAB LAST LACTATE (36109) |
| LACTATE_MAX_COLL_VALUE | No | The maximum lactate lab value that was collected during an ICU stay.  Rule: DM LAB MAX LACTATE (36110) |
| PLASMA_PROCALCITONIN_LAST_VAL | No | The last plasma procalcitonin lab value that was collected during an ICU stay.  Rule: DM LAB LAST PLASMA PROCALCITONIN (36111) |
| PLASMA_PROCALCITONIN_MAX_VAL | No | The maximum plasma procalcitonin lab value that was collected during an ICU stay.  Rule: DM LAB MAX PLASMA PROCALCITONIN (36112) |
| PLATELET_COUNT_LAST_COLL_VALUE | No | The last platelet count lab value that was collected during an ICU stay.  Rule: DM LAB LAST PLATELET COUNT (36113) |
| PLATELET_COUNT_MAX_COLL_VALUE | No | The maximum platelet count lab value that was collected during an ICU stay.  Rule: DM LAB MAX PLATELET COUNT (36114) |
| PLATELET_COUNT_MIN_COLL_VALUE | No | The minimum platelet count lab value that was collected during an ICU stay.  Rule: DM LAB MIN PLATELET COUNT (36115) |
| WBC_COUNT_LAST_COLL_VALUE | No | The last white blood cell (WBC) count lab value that was collected during an ICU stay.  Rule: DM LAB LAST WBC (36116) |
| WBC_COUNT_MAX_COLL_VALUE | No | The maximum white blood cell (WBC) count lab value that was collected during an ICU stay.  Rule: DM LAB MAX WBC (36117) |
| WBC_COUNT_MIN_COLL_VALUE | No | The minimum white blood cell (WBC) count lab value that was collected during an ICU stay.  Rule: DM LAB MIN WBC (36118) |
| HAD_POSITIVE_CULTURE_BOOL | No | Indicates whether a patient has a positive culture result. It contains 1 if a patient has a positive culture result that was collected during an ICU stay, or 0 otherwise.  Rule: DM SEPSIS HAD POSITIVE CULTURE (36119) |
| PAO2_FIO2_RATIO_LAST_VALUE | No | The last calculated PaO2/FiO2 ratio, based on the last (most recent) PaO2 value with a corresponding FiO2 value.  Rule: DM VITALS LAST PAO2/FIO2 (36135) |
| PAO2_FIO2_RATIO_MIN_VALUE | No | The minimum calculated PaO2/FiO2 ratio, using the minimum of the ratio between the PaO2 value and the corresponding FiO2 value.  Rule: DM VITALS MIN PAO2/FIO2 (36136) |
| PAT_AGE_YEARS_AT_ADMISSION | No | The patient?s age in years at the time of ICU admission.  Rule: DM GENERAL PATIENT AGE (36122) |
| PRIMARY_ADMISSION_DX_ID | No | The unique diagnosis ID for the principal problem associated with a patient's admission.  Rule: DM DIAGNOSIS ADMISSION PRIMARY DIAGNOSIS (36123) |
| APACHE_IV_NON_CABG_LOS | No | The APACHE IV Non-CABG length of stay score that was documented during the ICU stay.  Rule: DM SCORE APACHE IV NON-CABG LENGTH OF STAY (36133) |
| APACHE_IV_CABG_LOS | No | The APACHE IV CABG length of stay score that was documented during the ICU stay.  Rule: DM SCORE APACHE IV CABG LENGTH OF STAY (36134) |
| APACHE_IV_NON_CABG_MORTALITY | No | The APACHE IV Non-CABG mortality score that was documented during the ICU stay. This score is assumed to be a percentage score measuring the likelihood that a patient will die during a visit. If you are using a score that is not measured from 0 to 100, then you should convert the score to that scale in the attached rule.  Rule: DM SCORE APACHE IV NON-CABG MORTALITY (36131) |
| APACHE_IV_CABG_MORTALITY | No | The APACHE IV CABG mortality score that was documented during the ICU stay. This score is assumed to be a percentage score measuring the likelihood that a patient will die during a visit. If you are using a score that is not measured from 0 to 100, then you should convert the score to that scale in the attached rule.  Rule: DM SCORE APACHE IV CABG MORTALITY (36132) |
| APACHE_II_DX_PATIENT_TYPE | No | The patient type documented for APACHE II during the patient's ICU Stay, indicating whether the reason for the stay was operative or non-operative.  Rule: DM DIAGNOSIS APACHE II PATIENT TYPE (36130) |
| TEMPERATURE_FIRST_VAL_CELSIUS | No | The first temperature value that was documented during an ICU stay in degrees Celsius.  Rule: DM VITALS FIRST TEMPERATURE (36170) |
| TEMPERATURE_MAX_CELSIUS | No | The maximum temperature value that was documented during an ICU stay in degrees Celsius.  Rule: DM VITALS MAX TEMPERATURE (36171) |
| TEMPERATURE_MIN_CELSIUS | No | The minimum temperature value that was documented during an ICU stay in degrees Celsius.  Rule: DM VITALS MIN TEMPERATURE (36172) |
| CORE_TEMP_MAX_CELSIUS | No | The maximum core temperature value that was documented during an ICU stay in degrees Celsius.  Rule: DM VITALS MAX CORE TEMP (36150) |
| CORE_TEMP_MIN_CELSIUS | No | The minimum core temperature value that was documented during an ICU stay in degrees Celsius.  Rule: DM VITALS MIN CORE TEMP (36151) |
| ICU_STAY_START_DTTM | DATETIME (Local) | The instant, in the patient's local time zone, this ICU stay began.  Rule: DM ICU STAY START (36137) |
| ICU_STAY_END_DTTM | DATETIME (Local) | The instant, in the patient's local time zone, this ICU stay ended.  Rule: DM ICU STAY END (36138) |
| DEPARTMENT_ID | NUMERIC (18,0) | The department the patient was in when this ICU stay began.  Rule: DM ICU STAY INITIAL DEPARTMENT (36139) |
| PAT_ENC_CSN_ID | NUMERIC (18,0) | The unique contact serial number for the patient admission during which this ICU stay occurred. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI).  Rule: DM ICU STAY PATIENT HOSPITAL ADMISSION (36140) |
| EPIC_ICU_EXPECT_LENGTH_OF_STAY | NUMERIC (18,2) | The most recently filed score for the ICU LENGTH OF STAY (RETROSPECTIVE) (34504) predictive model associated with this ICU stay.  Rule: DM SCORE EPIC ICU EXPECTED LENGTH OF STAY (36141) |
| EPIC_ICU_RISK_OF_MORTALITY | NUMERIC (18,2) | The most recently filed score for the ICU IN-HOSPITAL MORTALITY RISK (RETROSPECTIVE) (34505) predictive model associated with this ICU stay.  Rule: DM SCORE EPIC ICU RISK OF HOSPITAL MORTALITY (36142) |
| ICU_LAST_READMIT_RISK_SCORE | NUMERIC (18,2) | The most recently filed ICU readmission risk score for the Risk of ICU Readmission or Mortality (34507) predictive model associated with this cross-ICU stay.  Rule: DM Score Last ICU Readmission Risk Score (36145) |
| ICU_LAST_MORTALITY_RISK_SCORE | NUMERIC (18,2) | The most recently filed mortality risk score for the Risk of ICU Readmission or Mortality (34507) predictive model associated with this cross-ICU stay.  Rule: DM Score Last ICU Readmission Risk Score (36146) |
| READMIT_IN_5_DAYS_BOOL | NUMERIC (1,0) | Indicates whether a patient was readmitted to the ICU within five days of this cross-ICU stay. It contains 1 if a patient was readmitted within five days or 0 if not readmitted within five days.  Rule: DM ICU Stay Readmitted Within 5 Days (36144) |
| EXPIRED_IN_5_DAYS_BOOL | NUMERIC (1,0) | Indicates whether a patient expired within five days of this cross-ICU stay. It contains 1 if a patient expired within five days or 0 if a patient did not expire within five days.  Rule: DM General Expired Within 5 Days (36143) |
| CROSS_ICU_STAY_START_DTTM | DATETIME (Local) | The instant, in the patient's local time zone, this cross-ICU stay began.  Rule: DM ICU Stay Cross-ICU Stay Start (36147) |
| CROSS_ICU_STAY_END_DTTM | DATETIME (Local) | The instant, in the patient's local time zone, this cross-ICU stay ended.  Rule: DM ICU Stay Cross-ICU Stay End (36148) |
| DVT_PROPHYLAXIS_DAYS | NUMERIC (18,0) | The number of days that have documentation for deep vein thrombosis (DVT) prophylaxis in the specified flowsheet rows during an ICU stay.  Rule: DM Flowsheet Days Receiving DVT Prophylaxis (36152) |
| BED_AT_30_DEGREES_DAYS | NUMERIC (18,0) | The number of days that have documentation of the head of a patient's bed being at 30? in the specified flowsheet rows during an ICU stay.  Rule: DM Flowsheet Days with Head of Bed at 30 Degrees (36153) |
| RECEIVED_ORAL_CARE_DAYS | NUMERIC (18,0) | The number of days that oral care was documented in the specified flowsheet rows as having been received during an ICU stay.  Rule: DM Flowsheet Days Receiving Oral Care (36154) |
| SBT_PERFORMED_DAYS | NUMERIC (18,0) | The number of days that a spontaneous breathing trial (SBT) documented in the specified flowsheet rows as having occurred during an ICU stay.  Rule: DM Flowsheet Days with Spontaneous Breathing Trial Performed (36155) |
| SAT_PERFORMED_DAYS | NUMERIC (18,0) | The number of days that a sedation awakening trial (SAT) was documented in the specified flowsheet rows as having occurred during an ICU stay.  Rule: DM Flowsheet Days with Sedation Awakening Trial Performed (36156) |
| ICU_PAT_AGE_CLASS_C | INTEGER | Indicates patient age classification for ICU stay.  Rule: DM ICU STAY PATIENT AGE CLASSIFICATION (90034421) |

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

_(424 total; showing first 30)_
