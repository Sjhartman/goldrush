# ORDER_RES

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=ORDER_RES

## Description

The ORDER_RES table contains result finding information for an order. Result findings include mammography pathology results, cardiovascular palette findings, and other result findings.

**Primary table** in this group (102 cols). Overflow siblings joined on shared key: ORDER_RES_2 (100 cols), ORDER_RES_3 (44 cols). Prefer this table for most queries.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | RES |
| Release Version | SUMMER 2005 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| FINDING_ID | NUMERIC (18,0) | The unique identifier of the finding record corresponding to the result. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this Chronicles record. This is populated only if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this Chronicles record was extracted. This is populated only if you use IntraConnect. |
| RESULT_TYPE_C | INTEGER |  |
| FINDING_SIDE_C | INTEGER |  |
| FNDG_HQA_ID *(deprecated)* | VARCHAR (18) | *** Deprecated *** In table ORDER_RES, the column FNDG_HQA_ID (RES/52105) has been deprecated. The deprecated column's content/data is no longer available since it is no longer populated in Chronicles. Support for Quick Forms has been dropped. Look for the corresponding SmartForm in SMRTDTA_ELEM_DATA.  HQA record ID that contains the questionnaire answers for a finding. |
| FINDING_TYPE_C | INTEGER |  |
| RECOMMENDATION_C | INTEGER |  |
| RECO_SIDE_C | INTEGER |  |
| CLASS_OF_LESION_C | INTEGER |  |
| SIZE_OF_TUMOR | NUMERIC (18,2) | The size of the tumor (mm) for pathology results of mammogram biopsies. |
| PATH_FND_SIDE_C | INTEGER |  |
| HISTOLOGY_GRADE_C | INTEGER |  |
| MARGIN_STATUS_C | INTEGER |  |
| NIPPLE_INVOLVED_YN | VARCHAR (1) |  |
| NODES_REMOVED | INTEGER | The number of nodes removed. |
| NODES_POSITIVE | INTEGER | The number of nodes positive in the pathology result. |
| STAGE_C | INTEGER |  |
| ESTROGEN_RECP_C | INTEGER |  |
| PROGESTERONE_RCP_C | INTEGER |  |
| S_PHASE | INTEGER | The S phase for a specific pathology result. |
| OB_ULTRASOUND_GA | VARCHAR (254) | The gestational age interpreted for the entire ultrasound, in days, for the result corresponding to ultrasound findings. |
| OB_US_AS_OF_DATE | DATETIME | The date the gestational age was recorded, if this is an ultrasound result. |
| NEEDS_FOLLOW_UP_C | INTEGER |  |
| MAMMO_DUE_DT | DATETIME | Due date for the recommendation. |
| MAMMO_FIND_FORM_ID | VARCHAR (18) | The unique ID of the SmartForm record of the mammography finding. This is populated using the enhanced drawing tools to document on breast diagrams within the radiology mammography module. |
| MAMMO_FIND_CTX_C | INTEGER |  |
| ORIGINAL_FINDING_ID | NUMERIC (18,0) | The unique ID of the original finding this finding record was copied from. |
| GRAFT_ID | VARCHAR (24) | The graft ID for this result. |
| DOMINANCE_C | INTEGER |  |
| ANNOTATION_TYPE_C | INTEGER |  |
| ANNOT_VESSEL_ID | NUMERIC (18,0) | The major vessel of the annotation. |
| ANNOT_SEGM_ID | NUMERIC (18,0) | The vessel segment ID. |
| ANNOT_END_SEGM_ID | NUMERIC (18,0) | The ending vessel segment ID. |
| COLLAT_END_VES_ID | NUMERIC (18,0) | The major vessel ID of the destination of a collateral. |
| COLLAT_END_SEGM_ID | NUMERIC (18,0) | The vessel segment of the destination of a collateral. |
| VESSEL_LOCATION_C | INTEGER |  |
| SEGMENT_LOC_C | INTEGER |  |
| LESION_PRE_STEN | INTEGER | The pre-stent stenosis percentage for this result. |
| LESION_POST_STEN | INTEGER | The post-stent stenosis percentage for this result. |
| INTERVENTION_TYPE_C | INTEGER |  |
| ATMOS_INFLATION | NUMERIC (4,2) | The measures of the balloon atmospheres inflation for the result. |
| SEC_OF_INFLATION | INTEGER | The number of seconds of balloon inflation measured for the result. |
| STENT_LENGTH | VARCHAR (254) | Indicates length of the stent. |
| STENT_DIAMETER | VARCHAR (254) | Indicates diameter of the stent. |
| INTERVENTIO_SEQ_NUM | INTEGER | The sequence of the intervention. |
| GRAFT_PROX_ANAST_ID | NUMERIC (18,0) | The proximal anastomosis for a graft. |
| GR_DIST_ANST_VEL_ID | NUMERIC (18,0) | The major vessel of the distal anastomosis for a graft. |
| GR_DIST_ANST_SEG_ID | NUMERIC (18,0) | The vessel segment of the distal anastomosis for a graft. |
| GRAFT_SEQ_NUM | INTEGER | The graft sequence number in a multi-vessel graft. |
| UPDATE_DATE | No | The date and time the finding record was extracted from the database. |
| CAST_BOOKMARK | VARCHAR (254) | This column contains the bookmark to be referenced on the Cast tool. |
| CONDITION_C | INTEGER |  |
| REC_ARCHIVED_YN | No | Indicates whether the Results Finding record is archived at the record level. |
| TECH_DOC_USER_ID | VARCHAR (18) | Stores the ID of the user that documented this finding in the procedure log. |
| TECH_DOC_DTTM | DATETIME (UTC) | The instant at which this finding was documented in the procedure log. |
| MAMMO_FIND_PULFW_YN | VARCHAR (1) |  |
| PAT_ID | VARCHAR (18) | The unique ID of the patient record with whom the result finding as associated. This column is frequently used to link to the PATIENT table. |
| MAMFND_SRC_FIND_ID | NUMERIC (18,0) | The result finding unique identifier for the source result finding from which the current result finding record was copied. Typically populated for permanent findings such as scars or tattoos. |
| MAMMO_BIOPSY_TYPE_C | INTEGER |  |
| MAMFND_PFWD_VERF_YN | VARCHAR (1) |  |
| PAT_CSN | NUMERIC (18,0) | The unique contact serial number (CSN) of the patient for whom the contact was moved. |
| LAST_FINDING_ID | NUMERIC (18,0) | The unique identifier for the most recent finding for a breast lesion. Use this column to join to another copy of ORDER_RES on the FINDING_ID column. This will only be populated for lesion records in ORDER_RES where RESULT_TYPE_C is equal to 52013 (Lesion). |
| LAST_LSN_STAT_C | INTEGER |  |
| NEEDLE_USED_C | INTEGER |  |
| CONF_OF_TARGET_C | INTEGER |  |
| IMG_DEVICE_USED_C | INTEGER |  |
| TECHNIQUE_USED_C | INTEGER |  |
| BIOPSY_REPEAT_TYP_C | INTEGER |  |
| MYOCARDIAL_TYPE_C | INTEGER |  |
| PATH_RESULT_DATE | DATETIME | The date on which a pathology result was returned from the lab after a breast biopsy was performed. |
| INVASIVE_SIZE_MM | NUMERIC (18,2) | The size (mm) of the invasive component of a breast lesion. |
| IN_SITU_SIZE_MM | NUMERIC (18,2) | The size (mm) of the in situ component of a breast legion. |
| NUM_OF_MARGINS | INTEGER | The number of margins that were identified anatomically and measured in metric units for a breast lesion. |
| SURG_LN_BIOPSY_YN | VARCHAR (1) |  |
| SPEC_COMP_SUBMTD_YN | VARCHAR (1) |  |
| MAM_SURGERY_TYPE_C | INTEGER |  |
| LN_EXTRA_EXTNSN_C | INTEGER |  |
| HER2_IHC_C | INTEGER |  |
| HER2_FISH_C | INTEGER |  |
| STATUS_C | INTEGER |  |
| GENERAL_RECOM_C | INTEGER |  |
| GEN_REC_ANAT_RGN_C | VARCHAR (66) |  |
| GEN_RECOM_MOD_TYP_C | INTEGER |  |
| GEN_RECOM_DUE_IN_C | INTEGER |  |
| GEN_RECOM_NOTE_ID | VARCHAR (254) | The comment entered for a follow-up recommendation for a non-mammography study. |
| REC_SRC_FINDING_ID | NUMERIC (18,0) | The finding record ID associated with a follow-up recommendation placed on a study. |
| RSLT_TRK_ACTY_C | INTEGER |  |
| RSLT_TRK_FINDING_C | INTEGER |  |
| RSLT_TRK_BGN_USR_ID | VARCHAR (18) | The user who documented a critical result. |
| RSLT_TRK_BEGIN_DTTM | DATETIME (UTC) | The instant at which a critical result was documented on a study. |
| RSLT_TRK_END_USR_ID | VARCHAR (18) | The user who completed the follow-up communication on a critical result. |
| RSLT_TRK_END_DTTM | DATETIME (UTC) | The instant at which a critical result follow-up communication was completed on a study. |
| PATH_LAB_ORDER_ID | NUMERIC (18,0) | The lab order that the pathology finding is documenting. |
| PATH_DOCUMENT_ID | VARCHAR (18) | The scanned document that the pathology finding is linked to. |
| PATH_BIOPSY_DATE | DATETIME | The biopsy date for the tissue sample that the pathology finding corresponds to.  This column will not include pre-upgrade data until after a specific workflow is done (ORD conversion 248404 has run to completion). If you are unsure whether this has happened yet, you can get the entire set of data if you COALESCE this column with the old column for the pathology biopsy date (ORDER_PROC_2.PATH_RSLT_DATE). |
| PATH_NOTE_ID | VARCHAR (254) | The unique ID of the user-entered, free-form text note that stores the comment/narrative text for the pathology finding as rich text format data. This column will not include pre-upgrade data until after a specific workflow is done (ORD conversion 248404 run to completion). If you are unsure whether this has happened yet, you can get the entire set of data if you COALESCE this column with the old column for pathology comment/narrative text (ORDER_PROC_4.PATH_NARR_NOTE_ID). |
| EXCL_FRM_CANCER_CNT_YN | VARCHAR (1) |  |
| CONCORDANT_YN | VARCHAR (1) |  |
| RSLT_TRK_FND_COMMNT | VARCHAR (200) | The comment associated with a critical result finding. |
| RESULT_NAME | VARCHAR (200) | Stores the result name. |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| B-TREE INDEX | EIX_ORDER_RES_PATH_RESULT_DT | PATH_RESULT_DATE | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_ORDER_RES_UPDATE_DT | UPDATE_DATE | 1 | Yes | Yes |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | FINDING_ID | ANATOMY_NOADD | FINDING_ID | No | No | No |  |
| 1 | FINDING_ID | AUDIOGRAM_METADATA | FINDING_ID | No | No | No |  |
| 1 | FINDING_ID | AUDIOLOGY_ORDER_LINK | FINDING_ID | No | No | No |  |
| 1 | FINDING_ID | DENTAL_FINDING_NOADD | FINDING_ID | No | No | No |  |
| 1 | FINDING_ID | DENTAL_HB_ESTIMATES | FINDING_ID | No | No | No |  |
| 1 | FINDING_ID | DENTAL_PROC_NOADD | FINDING_ID | No | No | No |  |
| 1 | FINDING_ID | DENTAL_VOUCHER_FEES | FINDING_ID | No | No | No |  |
| 1 | FINDING_ID | DERM_SKINEXAM_FINDING | FINDING_ID | No | No | No |  |
| 1 | FINDING_ID | HOMUNCULUS_INP_EXAM_DATA | FINDING_ID | No | No | No |  |
| 1 | FINDING_ID | ORDER_RES_2 | FINDING_ID | No | No | No |  |
| 1 | FINDING_ID | ORDER_RES_3 | FINDING_ID | No | No | No |  |
| 1 | FINDING_ID | ORDER_RES_CV_ORD | FINDING_ID | No | No | No |  |
| 1 | FINDING_ID | ORDER_RES_CV_RRT_ORDER | FINDING_ID | No | No | No |  |
| 1 | FINDING_ID | ORDER_RES_FOLLOWUP | FINDING_ID | Unknown | No | No |  |
| 1 | FINDING_ID | ORDER_RES_LOG | FINDING_ID | No | No | No |  |
| 1 | FINDING_ID | ORD_CV_FINDING | CV_FINDING_ID | Unknown | No | No |  |
| 1 | FINDING_ID | ORD_IOL | FINDING_ID | No | No | No |  |
| 1 | FINDING_ID | ORD_RES_BLOOD | FINDING_ID | Unknown | No | No |  |
| 1 | FINDING_ID | RES_FETALWEIGHT | FINDING_ID | No | No | No |  |
| 1 | FINDING_ID | RES_MAMMO_CUI_VALS | FINDING_ID | No | No | No |  |
| 1 | FINDING_ID | V_FINDINGS_ALL | FINDING_ID | Unknown | Unknown | No |  |
| 1 | FINDING_ID | V_ORDER_RES_IMG_STATUS | FINDING_ID | Unknown | Unknown | No |  |
| 1 | FINDING_ID | V_RIS_LESION | LESION_ID | Unknown | Unknown | No |  |
| 2 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 2 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 2 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 3 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 4 | RESULT_TYPE_C | ZC_RESULT_TYPE | RESULT_TYPE_C | No | No | No |  |

_(510 total; showing first 30)_
