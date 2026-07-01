# V_CANCER_STAGING

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=V_CANCER_STAGING

## Description

This view stores contact-specific information for a patient's cancer stage records. Each row in this table corresponds to a single set of edits that were all saved at the same time. Stages that were linked to more than one problem list entry prior to the 2014/2015 staging conversion will have a set of contacts for only one of those problems after the conversion, since the conversion included logic to choose a single problem to attach the converted stage(s) to. The contact date for stages created in the 2005 version and later edited in the 2007 version (before activating the over-time functionality in Spring 2007 special update client package C7503923 and server package E756910) will not reflect the actual date the 2007 contact was created. The contact date for the 2007 stage in this case will be the date on which the stage was signed (if the stage was signed), or will correspond to the same date as the 2005 stage (if the stage was not signed).

## Metadata

| Property | Value |
| --- | --- |
| Type | View |
| Release Version | Rel 2015 |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| STAGE_ID | NUMERIC (18,0) | The cancer stage ID. |
| CONTACT_DATE_REAL | No | A unique, internal contact date in decimal format. The integer portion of the number indicates the date of the contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc.  The contact date for stages created in the 2005 version and later edited in the 2007 version (before activating the over-time functionality in Spring 2007 special update client package C7503923 and server package E756910) will not reflect the actual date the 2007 contact was created. The contact date for the 2007 stage in this case will be the date on which the stage was signed (if the stage was signed) or will correspond to the same date as the 2005 stage (if the stage was not signed). |
| CONTACT_DATE | DATETIME | The date of this contact in calendar format.  The contact date for stages created in the 2005 version and later edited in the 2007 version (before activating the over-time functionality in Spring 2007 special update client package C7503923 and server package E756910) will not reflect the actual date the 2007 contact was created. The contact date for the 2007 stage in this case will be the date on which the stage was signed (if the stage was signed) or will correspond to the same date as the 2005 stage (if the stage was not signed). |
| CM_PHY_OWNER_ID | VARCHAR (25) | ID of the physical deployment owner for this record.  Physical owners will be where the data is hosted, either on the cross-over server or the owner deployment. |
| CM_LOG_OWNER_ID | VARCHAR (25) | ID of the logical deployment owner for this record.  Logical owners show the deployment where the record was created but doesn't represent if the record is a part of version skew. |
| CM_CT_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this contact. This is only populated if you use IntraConnect. |
| CONTACT_NUM | INTEGER | A sequential number to identify this contact uniquely within the cancer stage (STG) row. The first contact is number 1, the second is number 2, etc. |
| MOST_RECENT_CONTACT_YN | No | A yes/no flag indicating whether this contact is the most recent contact for the stage (i.e. is the most up-to-date information for the stage). |
| STG_CSN | NUMERIC (18,0) | A unique serial number for this contact. This number is unique across all stage (STG) contacts in your system. If you use IntraConnect this is the Unique Contact Identifier (UCI). |
| RECORD_STATUS_C | INTEGER |  |
| PAT_ID | VARCHAR (18) | The ID of the patient to which the stage in this row applies. |
| PAT_ENC_CSN_ID | NUMERIC (18,0) | The contact serial number (CSN) of the patient encounter in which this stage contact was edited. This column will be empty if the stage was edited in the patient's chart outside of an encounter context. |
| PAT_ENC_DEPT_ID | NUMERIC (18,0) | The ID of the department for the patient encounter in which this stage contact was edited. This column will be empty if the stage was edited in the patient's chart outside of an encounter context. |
| PAT_ENC_DEPT_NAME | .2 | The name of the department for the patient encounter in which this stage contact was edited. This column will be empty if the stage was edited in the patient's chart outside of an encounter context. |
| USER_LOGIN_DEPT_ID | NUMERIC (18,0) | The ID of the department to which the user was logged-in when this stage contact was edited. |
| USER_LOGIN_DEPT_NAME | .2 | The name of the department to which the user was logged-in when this stage contact was edited. |
| STAGE_EDIT_DATETIME | DATETIME (Local) | The instant in local time at which this contact was created in Chronicles. Note that once a contact has been created, it can no longer be edited in the cancer staging activity. Each time the user saves a cancer stage (STG) record, a new contact is created so that an edit history can be inferred by comparing data values across contacts. |
| STAGE_EDIT_USER_ID | VARCHAR (18) | The user ID of the person who created this contact. |
| STG_DEF_ID | NUMERIC (18,0) | The ID of the staging form definition (FCS) record which was used when entering the cancer staging information in this contact. |
| STG_DEF_CONTACT_DATE_REAL | NUMERIC (18,2) | The contact date real of the staging form definition (FCS) record which was used when entering the cancer staging information in this contact. |
| STG_DEF_CSN | NUMERIC (18,0) | The contact serial number (CSN) of the staging form definition (FCS) record that was used when entering the cancer staging information in this contact. |
| PROBLEM_LIST_ID | .1 | The unique ID of the Problem List entry for this cancer stage. |
| BODY_SITE_C | INTEGER |  |
| BODY_SITE_NAME | 77050 |  |
| UNCERTAIN_PRIMARY_SITE_YN | VARCHAR (1) | A yes/no flag indicating whether the primary tumor site is uncertain and therefore can only be suspected. |
| STAGE_METHOD_C | INTEGER |  |
| STAGE_METHOD_NAME | 60 |  |
| CLASSIFICATION_C | INTEGER |  |
| CLASSIFICATION_NAME | 400 |  |
| DATA_MODEL_VERSION_C | INTEGER |  |
| STAGING_DATE | DATETIME | The user-specified date associated with the staging information. |
| STAGE_STATUS_C | INTEGER |  |
| STAGE_STATUS_NAME | VARCHAR (254) |  |
| SIGN_USER_ID | VARCHAR (18) | If this stage has been signed, the ID of the user who signed the stage. |
| SIGN_DATETIME | DATETIME (Local) | If this stage is signed, the instant in local time at which the stage was signed. |
| CLINICAL_STAGED_BY_C | INTEGER | The category ID that corresponds to the person or people who assigned the clinical staging elements and stage group when staging a patient's cancer diagnosis. |
| CLINICAL_STAGED_BY_NAME | 55009 |  |
| FREE_TEXT_STAGE | VARCHAR (254) | The user-specified free text stage. |
| STAGE_GROUP_C | VARCHAR (66) | The category ID that corresponds to the stage grouping for this contact. |
| STAGE_GROUP_NAME | 100 |  |
| FIGO_STAGE_C | VARCHAR (66) | The category ID that corresponds to the FIGO stage for an incidence of gynecologic cancer. |
| FIGO_STAGE_NAME | 100 |  |
| STAGE_GROUP_SUMMARY | VARCHAR (254) | The stage group as an easily-accessible string. This will be either a FIGO or a general stage group, and may also include free text stage information. |
| STAGE_DESCRIPTION | VARCHAR (508) | A short description of this stage, typically including key values recorded by the user. |
| PRIMARY_TUMOR_C | VARCHAR (66) | The category ID that corresponds to the primary tumor (T) assessment. |
| PRIMARY_TUMOR_NAME | 105 |  |
| REGIONAL_LYMPH_NODES_C | VARCHAR (66) | The category ID that corresponds to the regional lymph nodes (N) assessment. |
| REGIONAL_LYMPH_NODES_NAME | 110 |  |
| DISTANT_METASTASIS_C | VARCHAR (66) | The category ID that corresponds to the distant metastasis (M) assessment. |
| DISTANT_METASTASIS_NAME | 115 |  |
| HISTOLOGIC_GRADE_C | VARCHAR (66) | The category ID that corresponds to the histologic grade (G) assessment. |
| HISTOLOGIC_GRADE_NAME | 90 |  |
| SERUM_TUMOR_MARKERS_C | VARCHAR (66) | The category ID that corresponds to the serum tumor markers (S) assessment. |
| SERUM_TUMOR_MARKERS_NAME | 906 |  |
| STAGE_PREFIX_C | INTEGER | The category ID that corresponds to the prefix used for the identification of special cases of TNM. Although a prefix does not affect the stage grouping, it does indicate cases needing separate analysis. |
| STAGE_PREFIX_NAME | 55010 |  |
| PERIPHERAL_BLOOD_INVOLVE_C | INTEGER | The category ID that corresponds to the field that denotes the level of peripheral blood involvement. |
| PERIPHERAL_BLOOD_INVOLVE_NAME | 55011 |  |
| HISTOLOGIC_GRADING_SYSTEM_C | INTEGER | The category ID that corresponds to the grading system used to determine the histologic grade, also known as the overall grade. |
| HISTOLOGIC_GRADING_SYSTEM_NAME | 55012 |  |
| LYMPHATIC_VASCULAR_INV_C | INTEGER | The category ID that corresponds to the field that was combined from the lymphatic vessel invasion (L) and venous invasion (V) into lymph-vascular invasion (LVI) for collection by cancer registrars. |
| LYMPHATIC_VASCULAR_INV_NAME | 55013 |  |
| LYMPHATIC_VESSEL_INV_C | INTEGER | The category ID that corresponds to the lymphatic vessel invasion (L) assessment. |
| LYMPHATIC_VESSEL_INV_NAME | 70 |  |
| VENOUS_INVASION_C | INTEGER | The category ID that corresponds to the venous invasion (V) assessment. |
| VENOUS_INVASION_NAME | 75 |  |
| RESIDUAL_TUMOR_C | INTEGER | The category ID that corresponds to the residual tumor (R) assessment. |
| RESIDUAL_TUMOR_NAME | 80 |  |
| RISK_SCORE_C | INTEGER | The category ID that corresponds to the risk factors assessment for this contact of the stage. |
| RISK_SCORE_NAME | 907 |  |
| RISK_SCORE | INTEGER | The numeric prognostic risk score associated with the cancer. |
| MULTIPLE_TUMORS_YN | VARCHAR (1) | A yes/no flag indicating whether the stage was documented based on the presence of multiple primary tumors. |
| NUMBER_OF_TUMORS | INTEGER | The number of tumors at this site. |
| LATERALITY_C | INTEGER | The category ID that corresponds to the laterality (left, right, or bilateral) of the cancer being staged, for a disease such as lung cancer or breast cancer which might affect one or both sides of the body. This column should be empty for a disease such as colon cancer which can only affect one area of the body. |
| LATERALITY_NAME | 500 |  |
| TUMOR_SIZE_MM | NUMERIC (18,1) | The size of the primary tumor. This value is always stored in millimeters, although the user may have documented this value in centimeters. |
| FIRST_TUMOR_SIZE_DIMENSION_MM | NUMERIC (18,1) | The first dimension of tumor size, in millimeters. |
| SECOND_TUMOR_SIZE_DIMENSION_MM | NUMERIC (18,1) | The second dimension of tumor size, in millimeters. |
| THIRD_TUMOR_SIZE_DIMENSION_MM | NUMERIC (18,1) | The third dimension of tumor size, in millimeters. |
| TUMOR_THICKNESS_MM | NUMERIC (18,1) | The thickness of the tumor, in millimeters. |
| LARGEST_REG_LYMPH_NODE_MM | NUMERIC (18,1) | The size of the largest regional lymph node, in millimeters. |
| LARGEST_LYMPH_TUMOR_DEP_MM | NUMERIC (18,1) | The size of the largest tumor deposit in the lymph nodes, in millimeters. |
| REG_LYMPH_NODE_TUMOR_NEST_MM | NUMERIC (18,1) | The size of the tumor nests in regional lymph nodes, in millimeters. |
| SPECIMEN_TYPE_C | INTEGER | The category ID that corresponds to the type of specimen that was collected to analyze the tumor. |
| SPECIMEN_TYPE_NAME | 505 |  |
| HISTOPATHOLOGIC_TYPE_C | VARCHAR (66) | The category ID that corresponds to the histopathologic type of the patient's cancer. |
| HISTOPATHOLOGIC_TYPE_NAME | 507 |  |
| DIAGNOSTIC_CONFIRMATION_C | INTEGER | The category ID that corresponds to the best method used to confirm the presence of a patient's cancer. |
| DIAGNOSTIC_CONFIRMATION_NAME | 55008 |  |
| METASTATIC_BIOPSY_PERFORMED_YN | VARCHAR (1) | A yes/no flag indicating whether a biopsy of the metastatic site was performed. |
| METASTATIC_SPEC_SOURCE_C | No |  |
| METASTATIC_SPEC_SOURCE_NAME | No |  |
| NODES_EXAMINED | INTEGER | The number of regional lymph nodes examined for staging. |
| POSITIVE_NODES | INTEGER | The number of regional lymph nodes that tested positive for cancer for staging. |
| GLEASON_PATTERN_PRIMARY | INTEGER | The primary Gleason pattern (1-5), entered as part of the stage for an incidence of prostate cancer. |
| GLEASON_PATTERN_SECONDARY | INTEGER | The secondary Gleason pattern (1-5), entered as part of the stage for an incidence of prostate cancer. |
| GLEASON_PATTERN_TERTIARY | INTEGER | The tertiary Gleason pattern (1-5), entered as part of the stage for an incidence of prostate cancer. |
| GLEASON_SCORE | INTEGER | The Gleason score, entered as part of the stage for an incidence of prostate cancer. |
| PSA_LEVEL | NUMERIC (18,1) | The patient's prostate-specific antigen (PSA) level, in ng/mL, entered as part of the stage for an incidence of prostate cancer. |
| PSA_RANGE_C | INTEGER | The category ID that corresponds to the patient's prostate-specific antigen (PSA) range entered as part of the stage for an incidence of prostate cancer. |
| PSA_RANGE_NAME | 55060 |  |
| FIBROSIS_C | INTEGER | The category ID that corresponds to the severity of fibrosis, entered as part of the stage for an incidence of liver cancer. |
| FIBROSIS_NAME | 551 |  |
| FIBROSIS_SCORE | INTEGER | A numeric score (0-6) indicating the severity of fibrosis, entered as part of the stage for an incidence of liver cancer. |
| VISUAL_ACUITY | VARCHAR (30) | A description of the patient's visual acuity, using Snellen shorthand or an equivalent system, entered as part of the stage for a malignant melanoma of the uvea. |
| HER2_STATUS_C | INTEGER | The category ID that corresponds to the patient's Human Epidermal Growth Factor Receptor 2 (HER2) amplification status (positive, negative, etc.). |
| HER2_STATUS_NAME | 55405 |  |
| PROG_RECEPTOR_STATUS_C | INTEGER | The category ID that corresponds to the progesterone receptor polymorphism status. |
| PROG_RECEPTOR_STATUS_NAME | 55034 |  |
| ESTROGEN_RECEPTOR_STATUS_C | INTEGER | The category ID that corresponds to the estrogen receptor over-expression status. |
| ESTROGEN_RECEPTOR_STATUS_NAME | 55034 |  |
| KRAS_GENE_ANALYSIS_C | INTEGER | The category ID that corresponds to the result of KRAS gene analysis (Normal, Abnormal, etc.). |
| KRAS_GENE_ANALYSIS_NAME | 55033 |  |
| CEA_LEVEL | NUMERIC (18,1) | The patient's carcinoembryonic antigen (CEA) level, in ng/mL, entered as part of the stage for an incidence of colorectal cancer. |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | STAGE_ID | STG_CS_INFO | STAGE_ID | Unknown | Unknown | No |  |
| 1 | STAGE_ID | STG_INFO | STAGE_ID | Unknown | Unknown | No |  |
| 1 | STAGE_ID | STG_PED_INFO | STAGE_ID | Unknown | Unknown | No |  |
| 4 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | Unknown | No |  |
| 4 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | Unknown | No |  |
| 4 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | Unknown | No |  |
| 5 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | Unknown | No |  |
| 5 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | Unknown | No |  |
| 5 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | Unknown | No |  |
| 6 | CM_CT_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | Unknown | No |  |
| 6 | CM_CT_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | Unknown | No |  |
| 6 | CM_CT_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | Unknown | No |  |
| 10 | RECORD_STATUS_C | ZC_RECORD_STATUS_2 | RECORD_STATUS_2_C | No | Unknown | No |  |
| 10 | RECORD_STATUS_C | ZC_RECORD_STS | RECORD_STS_C | No | Unknown | No |  |
| 11 | PAT_ID | ANTICOAG_SELF_REGULATING | PAT_ID | No | Unknown | No |  |
| 11 | PAT_ID | CARE_COORDINATION | PAT_ID | Unknown | Unknown | No |  |
| 11 | PAT_ID | CLAIMS_DERIVE_PAT_FLAGS | PAT_ID | No | Unknown | No |  |
| 11 | PAT_ID | COMMUNITY_RESRC_REVIEWED | PAT_ID | No | Unknown | No |  |
| 11 | PAT_ID | D_PAT_GEOGRAPHIC_CLASS | PAT_ID | Unknown | Unknown | No |  |
| 11 | PAT_ID | EPT_MEM_INFO | PAT_ID | No | Unknown | No |  |
| 11 | PAT_ID | EXT_DATA_LAST_DONE | PAT_ID | No | Unknown | No |  |
| 11 | PAT_ID | F_IBD_ADULT_FORM_PAT | PAT_ID | Unknown | Unknown | No |  |
| 11 | PAT_ID | HH_PAT_INFO | PAT_ID | Unknown | Unknown | No |  |
| 11 | PAT_ID | HM_STATUS_UPD | PAT_ID | No | Unknown | No |  |
| 11 | PAT_ID | IMMNZTN_LAST_REVIEW | PAT_ID | No | Unknown | No |  |
| 11 | PAT_ID | PATIENT | PAT_ID | No | Unknown | No |  |
| 11 | PAT_ID | PATIENT_2 | PAT_ID | No | Unknown | No |  |
| 11 | PAT_ID | PATIENT_3 | PAT_ID | No | Unknown | No |  |
| 11 | PAT_ID | PATIENT_4 | PAT_ID | No | Unknown | No |  |
| 11 | PAT_ID | PATIENT_5 | PAT_ID | No | Unknown | No |  |

_(273 total; showing first 30)_
