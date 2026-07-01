# SPEC_DB_MAIN

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=SPEC_DB_MAIN

## Description

The SPEC_DB_MAIN table contains basic information about your specimen records. These include clinical pathology, anatomic pathology, and quality control specimens. One row in this table represents one specimen.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | OVS |
| Release Version | FALL 2004 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| SPECIMEN_ID | VARCHAR (18) | The unique ID of the specimen record |
| LAB_ID *(deprecated)* | VARCHAR (18) |  |
| SPEC_NUMBER_LN1 | VARCHAR (254) | The main external identifier of the specimen |
| SPEC_DTM_COLLECTED | 100 | The date and time when the specimen was collected. |
| SPEC_DTM_RECEIVED | 610 | The date and time when the specimen was received. |
| SPEC_CONTAINER_ID | VARCHAR (18) | The unique identifier of the container associated with this specimen |
| SPEC_SOURCE_C | INTEGER |  |
| SPEC_COLL_SITE_C | INTEGER |  |
| SPEC_COLLECT_BY | VARCHAR (254) | The name of the person who collected the specimen. |
| SPEC_EPT_PAT_ID | VARCHAR (18) | The unique identifier of the patient whom this specimen belongs to. |
| SPEC_PRE_DUP_C | INTEGER |  |
| SPEC_QC_FLAG_YN | VARCHAR (254) |  |
| SPEC_QC_MAT_ID | VARCHAR (36) | The unique ID of the quality control material associated with this specimen if it is a quality control specimen |
| SPEC_QC_MLOT_DAT | FLOAT | The DAT, an internal contact date identifier in decimal format, of the lot date of the quality control material associated with this specimen if it is a quality control specimen. |
| SPEC_SUB_SPEC_NO | VARCHAR (254) | The submitter's specimen number. |
| SPEC_VAL_STAT_C | INTEGER |  |
| SPEC_CLOSED_DT | DATETIME | The date on which the specimen was closed. |
| SPEC_COLL_BY_ID | VARCHAR (18) | The unique ID of the employee who collected the specimen |
| SPEC_COLL_DEPT_ID | NUMERIC (18,0) | The unique ID of the department in which this specimen was collected. |
| SPEC_DRAW_TYPE_C | INTEGER |  |
| SPEC_REQ_GRP_ID | NUMERIC (18,0) | The unique ID of the requisition grouper associated with this specimen if this is a non-EPT patient |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| SPEC_QC_MLOT_EX_DAT | No | The lot date the quality control material associated with this specimen. |
| TYPE_OF_QC_C | INTEGER |  |
| REQ_SMT_ID | NUMERIC (18,0) | The unique identifier of the submitter that collected this specimen. This is only populated for reference lab specimens. |
| REQ_ID | NUMERIC (18,0) | The unique identifier of the requisition this specimen is attached to. This is only populated for reference lab specimens. |
| ACUTE_CONVAL_C | INTEGER |  |
| CASE_ID | NUMERIC (18,0) | The unique identifier of the case this specimen is attached to. This is only populated for anatomic pathology specimens. |
| RECV_QUEUE_COMM_ID | VARCHAR (254) | The unique ID of the internal receiving comment that is associated with this specimen. |
| SPEC_DELETED_YN | VARCHAR (1) |  |
| SPEC_COLL_UTC_DTTM | 121 | The date and time when the specimen was collected in the UTC time zone. |
| SPEC_RCVD_UTC_DTTM | 123 | The date and time when the specimen was received in the UTC time zone. |
| SPEC_FROZEN_YN | VARCHAR (1) |  |
| SPECIMEN_COL_ID | NUMERIC (18,0) | The unique identifier of the specimen collection record which is associated with this specimen. |
| AP_RECEIVE_UTC_DTTM | DATETIME (UTC) | The date and time when the anatomic pathology specimen was received in the UTC time zone. This is only populated for anatomic pathology specimens. |
| AP_RECEIVED_BY_ID | VARCHAR (18) | The unique ID of the employee who received the anatomic pathology specimen. This is only populated for anatomic pathology specimens. |
| RECV_BY_BARCODE_YN | VARCHAR (1) |  |
| DRAW_SESS_UTC_DTTM | DATETIME (UTC) | The date and time when the draw session this specimen belongs to was started. It is stored in the UTC time zone. |
| SPECIMEN_TYPE_C | INTEGER |  |
| SPEC_FROM_DSL_YN | VARCHAR (1) |  |
| ONSET_DATE | DATETIME | The onset date that symptoms began for the associated specimen. This is a legacy item and this data is no longer populated in Chronicles. |
| BIOHAZARD_C | INTEGER |  |
| DRAW_CHGS_TRGRD_YN | VARCHAR (1) |  |
| SPEC_SOURCE | VARCHAR (192) | The specimen source for the specimen. This is legacy data that is no longer populated. |
| SPEC_ORIGIN_C | INTEGER |  |
| IMPORT_RUN_BATCH_NUMBER_ID | VARCHAR (18) | The batch ID associated to an imported specimen |
| CREATION_DEPARTMENT_ID | NUMERIC (18,0) | The unique ID of the department that the specimen was created in. |
| COLL_PPID_OVRIDE_YN | VARCHAR (1) |  |
| COLL_PSID_OVRIDE_YN | VARCHAR (1) |  |
| DRAW_SESS_DTTM | DATETIME (Local) | The date and time when the draw session this specimen belongs to was started in the time zone of the submitter or accessioning department. |
| REQ_OR_GEN_SUBMITTER_ID | NUMERIC (18,0) | The unique identifier of the submitter of the requisition that this specimen is attached to. This is only populated for reference lab specimens. This will include a generic submitter that is placed on orders that were placed at your organization and collected at an EpicCare Link site. |
| PRINT_TASK_ID | NUMERIC (18,0) | The unique ID of the print label task template (LTR) used to accession this specimen. |
| REDRAW_ABANDONED_COLL_YN | VARCHAR (1) |  |
| COLL_PRTR_OVRIDE_YN | VARCHAR (1) |  |
| COLL_PPID_REQ_YN | VARCHAR (1) |  |
| COLL_PSID_REQ_YN | VARCHAR (1) |  |
| DONATION_IDENTIFICATION_NUMBER | VARCHAR (15) | Stores the ISBT-128 donation identification number (DIN) for a donor product specimen. |
| ABORH_BLOOD_GROUPS | VARCHAR (4) | The barcoded string containing information about ABO and RhD blood groups for a blood product specimen, provided by the ISBT-128 specification. |
| SPECIAL_ABO_PHENOTYPE_C | INTEGER |  |
| INTENDED_USE_ATTRIBUTE_C | INTEGER |  |
| BLOOD_GROUP_SPEC_MSG_C | INTEGER |  |
| PRODUCT_CODE | VARCHAR (8) | Stores the barcoded string that represents the donor product specimen's product code, according to the ISBT-128 specification. |
| COLLECTION_TYPE_CODE_C | INTEGER |  |
| PRODUCT_COLLECTION_DATE | DATETIME | The date at which this blood product specimen was collected. This column is populated only for certain blood product types, according to the ISBT-128 specification. |
| PRODUCT_COLLECTION_UTC_DTTM | DATETIME (UTC) | The date and time at which this blood product specimen was collected. This column is populated only for certain blood product types, according to the ISBT-128 specification. |
| SPECIAL_TESTING_CODE_C | INTEGER |  |
| RBC_ANTIGEN_BARCODE | VARCHAR (18) | Stores a barcoded string containing antigen test info for RBC blood product specimens, according to the ISBT-128 specification. |
| PLATELET_ANTIGEN_BARCODE | VARCHAR (18) | Stores a barcoded string with information about platelet HLA and HPA testing for a blood product specimen, according to the ISBT-128 specification. |
| COLL_TIMER_EXPIRATIONS | INTEGER | Indicates how many times a scan workflow timer expired after accessioning for this specimen. |
| PROD_DESC_CODE_ID | NUMERIC (18,0) | The unique ID of the product description code corresonding to this donor product specimen, according to the ISBT-128 specification. |
| EXPIRATION_UTC_DTTM | DATETIME (UTC) | The UTC date and time at which this specimen expires. |
| FACILITY_IDENTIFIER_RECORD_ID | NUMERIC (18,0) | Unique ID of the submitter corresponding to the donor facility that prepared this product specimen. |
| EXPIRATION_LOCAL_DTTM | DATETIME (Local) | The date and time at which this specimen expires. |
| DESC_CODE_CSN_ID | NUMERIC (18,0) | Stores the CSN of the product description code for this row. |
| ABO_PHENOTYPE_C | INTEGER |  |
| RHD_LAB_ANTIGEN_RESULT_C | INTEGER |  |
| SPEC_EXP_STRING | VARCHAR (10) | The barcoded string corresponding to the expiration date and time found on the label for a donor product. |
| PRODUCT_STATUS_C | INTEGER |  |
| SPEC_CUMULATIVE_VOLUME | INTEGER | The cumulative volume of all containers on the specimen, in milliliters |
| DEST_EPT_PAT_ID | VARCHAR (18) | The unique ID of the patient record this product is destined to be administered to, regardless of whether or not the administration has happened yet |
| DEST_REQ_GROUPER_ID | NUMERIC (18,0) | The unique ID of the grouper this product is destined to be administered to, regardless of whether or not the administration has happened yet |
| SPEC_COLLECT_DTTM_BARCODE | VARCHAR (10) | Stores the barcoded string corresponding to the collection date and time found on the label for a donor product. |
| SPECIAL_TESTING_CODE_BARCODE | VARCHAR (5) | Stores the string corresponding to the Special Testing N-Code found on the label for a donor product. |
| SPECIAL_RHD_PHENOTYPE_C | INTEGER |  |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| BITMAP INDEX | EIX_SPEC_DB_MAIN_QC_YN | SPEC_QC_FLAG_YN | 1 | Yes | Yes |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | SPECIMEN_ID | AP_SPECIMEN_DESC | SPECIMEN_ID | No | No | No |  |
| 1 | SPECIMEN_ID | EMBRYOLOGY_SPECIMEN | SPECIMEN_ID | No | No | No |  |
| 6 | SPEC_CONTAINER_ID | CONTAINER_TYPE | CONTAINER_TYPE_ID | No | No | No |  |
| 7 | SPEC_SOURCE_C | ZC_SPECIMEN_SOURCE | SPECIMEN_SOURCE_C | No | No | No |  |
| 7 | SPEC_SOURCE_C | ZC_SPECIMEN_SRC_2 | SPECIMEN_SRC_2_C | No | No | No |  |
| 7 | SPEC_SOURCE_C | ZC_SPEC_SOURCE | SPEC_SOURCE_C | No | No | No |  |
| 8 | SPEC_COLL_SITE_C | ZC_SITE_OF_COLLECT | SITE_OF_COLLECT_C | No | No | No |  |
| 8 | SPEC_COLL_SITE_C | ZC_SPEC_COLL_SITE | SPEC_COLL_SITE_C | No | No | No |  |
| 10 | SPEC_EPT_PAT_ID | ANTICOAG_SELF_REGULATING | PAT_ID | No | No | No |  |
| 10 | SPEC_EPT_PAT_ID | CARE_COORDINATION | PAT_ID | Unknown | No | No |  |
| 10 | SPEC_EPT_PAT_ID | CLAIMS_DERIVE_PAT_FLAGS | PAT_ID | No | No | No |  |
| 10 | SPEC_EPT_PAT_ID | COMMUNITY_RESRC_REVIEWED | PAT_ID | No | No | No |  |
| 10 | SPEC_EPT_PAT_ID | D_PAT_GEOGRAPHIC_CLASS | PAT_ID | Unknown | Unknown | No |  |
| 10 | SPEC_EPT_PAT_ID | EPT_MEM_INFO | PAT_ID | No | No | No |  |
| 10 | SPEC_EPT_PAT_ID | EXT_DATA_LAST_DONE | PAT_ID | No | No | No |  |
| 10 | SPEC_EPT_PAT_ID | F_IBD_ADULT_FORM_PAT | PAT_ID | Unknown | Unknown | No |  |
| 10 | SPEC_EPT_PAT_ID | HH_PAT_INFO | PAT_ID | Unknown | No | No |  |
| 10 | SPEC_EPT_PAT_ID | HM_STATUS_UPD | PAT_ID | No | No | No |  |
| 10 | SPEC_EPT_PAT_ID | IMMNZTN_LAST_REVIEW | PAT_ID | No | No | No |  |
| 10 | SPEC_EPT_PAT_ID | PATIENT | PAT_ID | No | No | No |  |
| 10 | SPEC_EPT_PAT_ID | PATIENT_2 | PAT_ID | No | No | No |  |
| 10 | SPEC_EPT_PAT_ID | PATIENT_3 | PAT_ID | No | No | No |  |
| 10 | SPEC_EPT_PAT_ID | PATIENT_4 | PAT_ID | No | No | No |  |
| 10 | SPEC_EPT_PAT_ID | PATIENT_5 | PAT_ID | No | No | No |  |
| 10 | SPEC_EPT_PAT_ID | PATIENT_6 | PAT_ID | No | No | No |  |
| 10 | SPEC_EPT_PAT_ID | PATIENT_CONF_ADDR | PAT_ID | No | No | No |  |
| 10 | SPEC_EPT_PAT_ID | PATIENT_MISC_COMMENTS | PAT_ID | No | No | No |  |
| 10 | SPEC_EPT_PAT_ID | PATIENT_MYC | PAT_ID | Unknown | No | No |  |
| 10 | SPEC_EPT_PAT_ID | PATIENT_OPT | PAT_ID | No | No | No |  |
| 10 | SPEC_EPT_PAT_ID | PAT_ENC_LAST_HX_CT | PAT_ID | Unknown | Unknown | No |  |

_(221 total; showing first 30)_
