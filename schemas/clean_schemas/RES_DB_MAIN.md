# RES_DB_MAIN

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=RES_DB_MAIN

## Description

The RES_DB_MAIN is the primary table for storing results data.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | OVR |
| Release Version | FALL 2004 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| RESULT_ID | VARCHAR (18) | The unique ID of the result record. |
| RES_TYPE_ID | VARCHAR (18) | The unique ID of the result type record that is associated with this result record. |
| LAB_ID *(deprecated)* | VARCHAR (18) |  |
| RES_VAL_STATUS_C | INTEGER |  |
| RES_TEST_ID | 10036 76 36 | The unique ID of the test that is associated with the result record. It gets the ID through OVR 10036 which in turn checks OVR 76 (test for the result) and then, if OVR 76 is not available, OVS 36 (tests for the specimen associated with the result) for the first specimen associated with the result. |
| RES_SPECIMEN_ID | VARCHAR (18) | The unique ID of the specimen that is associated with the result record. |
| RES_SPEC_NO_REL | 10026 | The related external specimen ID number for the given result. It gets the specimen ID through related externa ID number (I OVR 10026), which in turn uses the specimen related external ID number (I OVS 26) for the first specimen associated with the result. |
| RES_EPT_PAT_ID | VARCHAR (18) | The unique ID of the patient (EPT) associated with the result record. |
| RES_TYP_OF_RES_C | INTEGER |  |
| RES_GW_RESULT_ID | VARCHAR (18) | The unique ID of the result record for a general workcard associated with this result record. |
| RES_OW_RESULT_ID | VARCHAR (18) | The unique ID of the organism workcard result record associated with this result record. |
| RES_TECH_ID | VARCHAR (18) | The unique ID of the user who last resulted the test. |
| RES_ABNORMAL_C | VARCHAR (66) |  |
| RES_NRPT_FLG_C *(deprecated)* | INTEGER |  |
| RES_BATCH_AUDIT | VARCHAR (254) | Batch audit trail for result (batch ID and relative position in the batch) |
| RES_INST_ORDERED_TM | 10106 | The instant the result's test was added to the specimen. It gets the instant through I OVR 10106, which in turn uses I OVS 106 for the first specimen associated with the result. |
| RES_INST_VALIDTD_TM | DATETIME (Local) | For results in status prelim, pend prelim, pend final, cosign, and final, the column is the instant the result attained that status. If the result is in status corrected the column instead stores the time of final verification. For results in other statuses the column is not populated. This column gets the instant from OVR 10170, which itself uses the audit trail for the result record. |
| RES_INST_UNVAL_TM | DATETIME (Local) | This column is only populated for results of status "Corrected". It stores the instant the result correction was authorized and gets the instant from OVR 10172, which itself uses the audit trail for the current result record. |
| RES_NUM_REPEAT *(deprecated)* | INTEGER | In table RES_DB_MAIN, the column RES_NUM_REPEAT (OVS/34) has been deprecated. The deprecated column is no longer available since it is no longer populated in Chronicles by Epic's laboratory information system. To report on repeats, use table RES_REPEAT_COMP. |
| RES_EPIC_PROV_ID *(deprecated)* | VARCHAR (18) | In table RES_DB_MAIN, the column RES_EPIC_PROV_ID (OVS/86) has been deprecated. The deprecated column is no longer available since it is no longer extracted to Clarity. In order to avoid data consistency issues, when reporting on the provider who placed the order associated with the specimen for this result, use the column SPEC_TST_PROV_ID in table SPEC_TEST_REL. |
| RES_ORDER_ID | 10085 | The order ID associated with the result's test. It gets the order ID through the related external ID number (I OVR 10026) , which in turn uses order ID (I OVS 85) for the first specimen associated with the result. |
| RES_TEST_MTHD_ID | VARCHAR (18) | The unique ID of the test method. |
| RES_VERIFY_LAB_ID | VARCHAR (18) | Lab where result was verified |
| RES_RQG_PAT_ID | NUMERIC (18,0) | The unique ID of the non-participating submitter's patient (RQG) associated with the result record. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| CURRENT_ACTION_ID | NUMERIC (18,0) | The action which is currently in progress for the workcard. |
| RES_SMART_TEXT_ID *(deprecated)* | VARCHAR (254) | In table RES_DB_MAIN, the column RES_SMART_TEXT_ID (OVR/51200) has been deprecated.The deprecated column's content/data is no longer available since it is no longer populated in Chronicles. |
| SLIDE_REVIEW_RPT_YN | VARCHAR (1) |  |
| DIFF_REPORTED_C | INTEGER |  |
| REPORTABLE_C | INTEGER |  |
| REPORT_TO_HU_YN | VARCHAR (1) |  |
| DIFF_COUNT_RSTRC_C | INTEGER |  |
| RPT_PER_100_CELL_YN | VARCHAR (1) |  |
| SCALE_FACTOR_WBCS | INTEGER | Stores the scale factor used for calculating WBCs components. |
| DIFF_CELL_COUNT_EVT | INTEGER | Stores the number of cells to count before which an action will be triggered. This value is used when a manual cell count is being performed such as a CBC Differential. |
| MAIN_RPTD_YN | VARCHAR (1) |  |
| AUTO_RES_START_DTTM | DATETIME (Local) | The start time for auto resulting. |
| MULTI_COMP_COM_DT_C | INTEGER |  |
| CAT_INI | VARCHAR (254) | Stores the master file from which to select a category list for multiline component level category comments. |
| CAT_ITEM | NUMERIC (18,0) | Stores the item from which to select a category list for multiline component level category comments. |
| CAT_DISCRIMINATION | VARCHAR (254) | Stores the custom code to limit the categories from which to select a category list for multiline component level catgeory comments. |
| CULTURE_GROWTH_C *(deprecated)* | INTEGER |  |
| RES_BY_EXT_LAB_YN | VARCHAR (1) |  |
| STAIN_BILL_YN | VARCHAR (1) |  |
| SCI_NOTATN_FMT_C | INTEGER |  |
| SCI_NOTATN_ORD_MAG | INTEGER | Stores the minimum order of magnitude for formatting culture quantity in scientific notation for a result. |
| RESULTING_LAB_ID | VARCHAR (18) | The unique ID of the resulting lab for the result record. |
| TEST_LINE | No | The test line number for the information associated with the specimen of this result. Along with RES_SPECIMEN_ID, this forms the foreign key to the SPEC_TEST_REL table. |
| QC_OUT_OF_CTRL_YN | VARCHAR (1) |  |
| DIFF_TYPE_RPTD_C | INTEGER |  |
| DONT_REPORT_TEST_YN | VARCHAR (1) |  |
| COSIGN_MINOR_EDT_YN | VARCHAR (1) |  |
| COSIGN_MAJOR_EDT_YN | VARCHAR (1) |  |
| AUTO_START_UTC_DTTM | DATETIME (UTC) | The instant when auto-resulting was started for a test in UTC. |
| INST_ORD_UTC_DTTM | 10126 | The instant (UTC) the result's test was added to the specimen. Gets the instant through I OVR 10126, which in turn uses I OVS 126 for the first specimen associated with the result. |
| LINKED_CBC_TEST_ID | VARCHAR (18) | The unique ID of the hemogram/auto diff test linked to a manual diff test. If there is no linked test, the unique ID of the manual diff test is stored. |
| EXT_VER_UTC_DTTM | DATETIME (UTC) | The UTC result report instant specified by a reference lab or POCT result message. |
| RAND_REFX_FIRED_YN | VARCHAR (1) |  |
| TYPE_OF_DATA_C | INTEGER |  |
| RES_EXCL_CDS_FLAG_C | INTEGER |  |
| RES_EXCL_CDS_SRC_C | INTEGER |  |
| RES_EXCL_CDS_USER_ID | VARCHAR (18) | The Exclude From Decision Support user ID for the result. |
| PERF_ORG_LAB_ID | NUMERIC (18,0) | The unique ID of the actual resulting agency for this result. This could be populated for interfaced results to indicate which resulting agency actually performed the test (as opposed to the lab or section in which verification occurred). |
| REQ_COSIGNER_USER_ID | VARCHAR (18) | Stores the unique ID of the user record requested to cosign this result. If blank, any user can cosign this result. |
| VALIDATION_DATE | DATETIME | The date when the result was validated. |
| SPEC_TYPE_CONTAINER_TYPE_ID | VARCHAR (18) | The unique ID for the container type of the specimen for this result. |
| VAR_UPDATE_UTC_DTTM | DATETIME (UTC) | The date and time when the variant associated with this result was added, updated, or deleted. |
| CRIT_PUSH_OUTCOME_C | INTEGER |  |
| TEST_INSTRUMENT_PROF_IDENT | VARCHAR (50) | Stores the network concept identifier associated with the test's resulting method at the time of resulting or verification. |
| COMP_CMT_C | INTEGER |  |
| SUS_CATALOG_ENTRY_CSN_ID | NUMERIC (18,0) | The unique contact serial number of the Network Catalog Entry (NCE) that is associated with the susceptibility test. |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| B-TREE INDEX | EIX_RES_DB_MAIN_RES_STATUS_C | RES_VAL_STATUS_C | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_RES_DB_MAIN_SPEC_TEST_REL | RES_SPECIMEN_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_RES_DB_MAIN_SPEC_TEST_REL | TEST_LINE | 2 | Yes | Yes |  |
| B-TREE INDEX | EIX_RES_DB_MAIN_VALIDATED_TM | RES_INST_VALIDTD_TM | 1 | Yes | Yes |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | RESULT_ID | ADRENAL_GLAND_BIOP | RESULT_ID | No | No | No |  |
| 1 | RESULT_ID | AMPULLA_OF_VATER | RESULT_ID | No | No | No |  |
| 1 | RESULT_ID | ANUS_ABDOMIN_RESEC | RESULT_ID | No | No | No |  |
| 1 | RESULT_ID | ANUS_EXCISION_BIOP | RESULT_ID | No | No | No |  |
| 1 | RESULT_ID | APPENDIX_RESECTION | RESULT_ID | No | No | No |  |
| 1 | RESULT_ID | BONE_BIOPSY | RESULT_ID | No | No | No |  |
| 1 | RESULT_ID | BONE_MARROW_ASPIR | RESULT_ID | No | No | No |  |
| 1 | RESULT_ID | BONE_RESECTION | RESULT_ID | No | No | No |  |
| 1 | RESULT_ID | BRAIN_SPINAL_BIOP | RESULT_ID | No | No | No |  |
| 1 | RESULT_ID | BRAIN_SPINAL_BIO_2 | RESULT_ID | No | No | No |  |
| 1 | RESULT_ID | COLON_RECTUM_BIOP | RESULT_ID | No | No | No |  |
| 1 | RESULT_ID | COLON_RECTUM_RESEC | RESULT_ID | No | No | No |  |
| 1 | RESULT_ID | DCIS_BREAST_EXCIS | RESULT_ID | No | No | No |  |
| 1 | RESULT_ID | DIST_EXTRAHEP_BILE | RESULT_ID | No | No | No |  |
| 1 | RESULT_ID | EMBRYOLOGY_RESULT | RESULT_ID | No | No | No |  |
| 1 | RESULT_ID | ENDOMETRIUM_HYSTER | RESULT_ID | No | No | No |  |
| 1 | RESULT_ID | ESOPHAGUS_RESEC | RESULT_ID | No | No | No |  |
| 1 | RESULT_ID | EWING_SARCOMA_BIOP | RESULT_ID | No | No | No |  |
| 1 | RESULT_ID | EWING_SARCOM_RESEC | RESULT_ID | No | No | No |  |
| 1 | RESULT_ID | FALLOP_TUB_SALPING | RESULT_ID | No | No | No |  |
| 1 | RESULT_ID | GALLBLADDER_RESEC | RESULT_ID | No | No | No |  |
| 1 | RESULT_ID | HEART_RESECTION | RESULT_ID | No | No | No |  |
| 1 | RESULT_ID | HEPATOBLAST_RESEC | RESULT_ID | No | No | No |  |
| 1 | RESULT_ID | HEPATOCELL_CARC | RESULT_ID | No | No | No |  |
| 1 | RESULT_ID | HODGKIN_LYMPHOMA | RESULT_ID | No | No | No |  |
| 1 | RESULT_ID | INTRAH_BILE_RESEC | RESULT_ID | No | No | No |  |
| 1 | RESULT_ID | INVAS_CARC_BREAST | RESULT_ID | No | No | No |  |
| 1 | RESULT_ID | INVAS_CARC_BREAS_2 | RESULT_ID | No | No | No |  |
| 1 | RESULT_ID | INVAS_CARC_BREAS_3 | RESULT_ID | No | No | No |  |
| 1 | RESULT_ID | KIDNEY_BIOPSY | RESULT_ID | No | No | No |  |

_(446 total; showing first 30)_
