# SPEC_TEST_REL

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=SPEC_TEST_REL

## Description

The SPEC_TEST_REL table contains information stored on each specimen record that relates to the tests performed on the specimen. Each test appears as a distinct row in this table.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | OVS |
| Release Version | SPRING 2005 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| SPECIMEN_ID | VARCHAR (18) | The unique ID of the specimen record |
| LINE | No | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| LAB_ID *(deprecated)* | VARCHAR (18) |  |
| SPEC_NUMBER_RLTD | VARCHAR (254) | External specimen numbers related to this specimen. |
| SPEC_TST_ID | VARCHAR (18) | The unique ID of the test that is being run on this specimen |
| SPEC_TEST_PRI_C | VARCHAR (66) |  |
| SPEC_TST_LAB_ID | VARCHAR (18) | The unique ID of the lab that is running the test on the specimen |
| SPEC_TST_ORDER_ID | NUMERIC (18,0) | The unique identifier of the order that is associated with this specimen |
| SPEC_TST_PROV_ID | VARCHAR (18) | The unique ID of the provider who placed the order associated with this specimen. |
| SPEC_TST_CANC_ID | VARCHAR (18) | The unique ID of the employee who cancelled the test. |
| SPEC_TST_CANC_C | VARCHAR (66) |  |
| SPEC_TST_CANC_INST | DATETIME (Local) | The instant when a test on the specimen was cancelled. |
| SPEC_SUBM_TEST_NO | VARCHAR (254) | The submitter's external test number. |
| SPEC_UNVLD_RESULT | VARCHAR (18) | The unique ID of the result associated with a specimen that has been unvalidated. |
| SPEC_UNVLD_USER | VARCHAR (18) | The unique ID of the employee that unvalidated a specimen result. |
| SPEC_TST_OL_STS_C | INTEGER |  |
| SPEC_TST_ACC_LAB_ID | VARCHAR (18) | The unique identifier of the lab where the test was originally supposed to be performed. |
| TEST_DEST_LAB_ID | VARCHAR (18) | The unique identifier of the lab to which the specimen is being transferred. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| SPEC_TST_CANC_COM | VARCHAR (500) |  |
| TST_REASON_REDRAW_C | INTEGER |  |
| TST_REASON_REDR_COM | VARCHAR (500) |  |
| LAST_RECV_DTTM | DATETIME (Local) | The date and time this test was last received into the lab. This is used to calculate turnaround times if you have configured them to be based on the last receive instant. |
| REDRAWN_ORDERS_ID | NUMERIC (18,0) | Stores an order after a test has been marked as canceled but the order should be redrawn. |
| ORD_PERF_LINE | INTEGER | Stores the line number of the performable procedure linked to this test in the order record's superitem 51300. |
| TEST_METHOD_ID *(deprecated)* | VARCHAR (18) | In table SPEC_TEST_REL, the column TEST_METHOD_ID (OVS/95) has been deprecated.   The deprecated column's content/data is no longer available since it is no longer populated in Chronicles. |
| TIERED_TAT | INTEGER | The amount of time, in minutes, from when a specimen is received that can pass before its tests are considered overdue. |
| RESULT_TO_PRINT_ID | VARCHAR (18) | The unique ID of the result record to print for this specimen and test. |
| BATCH_NUMBER | VARCHAR (254) | A comma-delimited list of batch numbers for this specimen and test. |
| VERIF_STATUS_C | INTEGER |  |
| ORDER_GROUP_ID | NUMERIC (18,0) | The unique ID of the order group used to group together tests that were ordered as part of the same order or orderable panel.   Note: this item is only populated for orders placed through requisition entry.  Primarily used by lab billing to verify that all tests ordered as part of an order or panel are complete so that billing can be triggered at the order or panel level. For panels the first order ID in the panel will be used to group the tests together. |
| TST_CANCEL_USER_ID | VARCHAR (18) | The unique ID of the user who canceled the test.  This column is only populated for specimens without associated patients; other tests should have the ID of the user who canceled the test in the related order's item ORD 9500. |
| PENDING_RESULT_IDS | VARCHAR (508) | A comma-delimted list of pending result IDs for this specimen and test. |
| NOT_REPORT_FLAG_C | INTEGER |  |
| ACC_FROM_DEP_ID | NUMERIC (18,0) | The unique ID of the department from which this specimen was accessioned. If the user clicked "accession" in the client, this is the department the user was logged into when accessioning. If the test was accessioned by a background job or an interface, this is the encounter department. |
| CURRENT_RESULT_ID | VARCHAR (18) | This item stores a link to the most recent result record for each test on the specimen. |
| LAST_RECV_UTC_DTTM | DATETIME (UTC) | The date and time this test was last received into the lab in UTC. This is used to calculate turnaround times if you have configured them to be based on the last receive instant. |
| LAB_CHG_TRG_FLG | INTEGER | Bit flag to track charge triggering. The flag tracks whether different types of charges, such as primary charges and additional billing charges, have been triggered. |
| CHG_TRG_LVL_C | INTEGER |  |
| SPEC_TST_SEC_ID | VARCHAR (18) | Performing section. This is populated any time results are entered for the test, and represents the actual section that performed the test. |
| TEST_VAL_STATUS_C | INTEGER |  |
| TEST_STATUS_PERSON | VARCHAR (18) | The unique ID of the user associated with the validation status of the test.  In the case of multiple tests on a specimen, this column will store the validation status of each test in the corresponding row.  There are two other columns in the SPEC_TEST_REL table that store the status and instant associated with the user ID that is stored in this column.  Those columns are TEST_VAL_STATUS_C and TEST_STATUS_DTTM. |
| TEST_STATUS_DTTM | DATETIME (Local) | The instant associated with the validation status of the test. In the case of multiple tests on a specimen, this column will store the validation status of each test in the corresponding row.  There are two other columns in the SPEC_TEST_REL table that store the status and user ID associated with the instant that is stored in this column.  Those columns are TEST_VAL_STATUS_C and TEST_STATUS_PERSON. |
| TAT_OVERDUE_DTTM | DATETIME (UTC) | The calculated time this test is considered overdue. |
| TAT_NEARING_DTTM | DATETIME (UTC) | The calculated time this test is considered nearing overdue. |
| TST_CANCEL_UTC_DTTM | DATETIME (UTC) | The UTC date and time when the test was canceled or redrawn. |
| TEST_VER_UTC_DTTM | DATETIME (UTC) | Stores the verification instant of the test in the UTC format. The item is set/updated when the test is either prelim verified or final verified and is cleared when a result correction is done. |
| ORDERED_UTC_DTTM | DATETIME (UTC) | This stores the date the test was associated with the specimen in UTC. |
| ORDER_INST_DTTM | DATETIME (Local) | The instant the order associated with this test was placed or released. If this test is associated with the performable procedure of a panel, the instant is returned from the orderable procedure. |
| ORDER_INST_UTC_DTTM | DATETIME (UTC) | The instant the order associated with this test was placed or released in UTC. If this test is associated with the performable procedure of a panel, the instant is returned from the orderable procedure. |
| MISSING_REQ_DATA_C | INTEGER |  |
| REPORTABLE_YN | VARCHAR (1) |  |
| LEVEL_INTERACTION_C | INTEGER |  |
| AUTO_VERIFIED_YN | VARCHAR (1) |  |
| DELTA_YN | VARCHAR (1) |  |
| INSTRUMENT_ERROR_YN | VARCHAR (1) |  |
| TEST_RESULT_TYPE_ID | VARCHAR (18) | The unique identifier of the result type that is assigned to this test. |
| CHARGE_ID | VARCHAR (254) | The unique ID of the charge associated with the test. |
| TST_STAT_ABNORMS_C | VARCHAR (66) |  |
| GEN_WORKCARD_RESULT_TYPE_ID | VARCHAR (18) | The unique ID of the workcard result type which is associated with the test. |
| LNK_SPEC_TST_TOGETHER_YN | VARCHAR (1) |  |
| CHRG_METHOD_ID | VARCHAR (18) | The unique ID associated with the previous charge method used for this test. |
| CHG_UPD_FLAG | INTEGER | May only be populated for legacy records. A value in this column means the charges associated with the test require updating. |
| EXTRA_RESULT_CNT | INTEGER | The number of extra results remaining. |
| RESULT_CNT | INTEGER | The number of results needing to be performed for this test. |
| BATCH_QUEUE_IDENT | VARCHAR (254) | The position of this test in the batch queue. |
| VALIDATED_RESULT_ID | VARCHAR (18) | The unique ID of the finalized result for the test. |
| REPEAT_CNT | INTEGER | The number of repeats required for this test. |
| DEL_FROM_BATCH_QUEUE | VARCHAR (254) | May only be populated for legacy records. When a value is present in this column, this test was removed from the Batch Queue. |
| ORDER_PRIORITY_C | INTEGER |  |
| SHIPPING_NUMBER | INTEGER | Represents a unique ID associated with transferring this test to another lab. |
| PREV_RSLT_DISP_FLAG_C | INTEGER |  |
| RR_EXCEPT_LIST | VARCHAR (254) | May only be populated for legacy records. Contains flags for not reporting or sending result reports for this test to specific recipients. |
| CANCEL_RESULT_ID | VARCHAR (18) | The unique ID of a canceled result, if one exists, for each test on the specimen. |
| REFLEX_TRIGGERED_YN | VARCHAR (1) |  |
| SOURCE_ORDER_ID | NUMERIC (18,0) | The unique ID of the source order for the test. For tests that have been redrawn or moved, this is the removed order. For tests that have not be redrawn or removed, this is the order that results will file to. This is the culture order for susceptibility tests. |
| PERFORMING_METHOD_ID | VARCHAR (18) | The method that is intended to run the tests for this specimen. |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| B-TREE INDEX | EIX_SPECREL_ORDER | SPEC_TST_ORDER_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_SPECREL_TESTING_LAB | SPEC_TST_LAB_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_SPECREL_TEST_STATUS | TEST_STATUS_DTTM | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_SPECREL_TEST_STATUS | TEST_VAL_STATUS_C | 2 | Yes | Yes |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | SPECIMEN_ID | AP_SPECIMEN_DESC | SPECIMEN_ID | No | No | No |  |
| 1 | SPECIMEN_ID | EMBRYOLOGY_SPECIMEN | SPECIMEN_ID | No | No | No |  |
| 1 | SPECIMEN_ID | SPEC_DB_MAIN | SPECIMEN_ID | No | No | No |  |
| 5 | SPEC_TST_ID | PROTOCOL_DB_MAIN | PROTOCOL_ID | Unknown | No | No |  |
| 5 | SPEC_TST_ID | TEST_MSTR_DB_MAIN | TEST_ID | Unknown | No | No |  |
| 5 | SPEC_TST_ID | ZC_QC_TEST_CAT_ID | QC_TEST_CAT_ID_C | Unknown | Unknown | No |  |
| 6 | SPEC_TEST_PRI_C | ZC_SPEC_TEST_PRI | SPEC_TEST_PRI_C | No | No | No |  |
| 7 | SPEC_TST_LAB_ID | AP_CASE_TYPES | LAB_ID | Unknown | No | No |  |
| 7 | SPEC_TST_LAB_ID | LAB_AP_LAB_SETUP | LAB_ID | Unknown | No | No |  |
| 7 | SPEC_TST_LAB_ID | LAB_INFO | LAB_ID | Unknown | No | No |  |
| 7 | SPEC_TST_LAB_ID | LAB_PROFILE | LAB_ID | Unknown | No | No |  |
| 7 | SPEC_TST_LAB_ID | LAB_SECTION | SECTION_ID | Unknown | No | No |  |
| 7 | SPEC_TST_LAB_ID | LDF_REQ_SETUP | LAB_ID | Unknown | No | No |  |
| 7 | SPEC_TST_LAB_ID | WORKBENCH_PROFILE | WORKBENCH_ID | Unknown | No | No |  |
| 8 | SPEC_TST_ORDER_ID | ADT_ORDERS_ERRORS | ORDER_ID | No | No | No |  |
| 8 | SPEC_TST_ORDER_ID | ADT_ORDER_INFORMATION | ORDER_ID | No | No | No |  |
| 8 | SPEC_TST_ORDER_ID | APPT_REQUEST | REQUEST_ID | No | No | No |  |
| 8 | SPEC_TST_ORDER_ID | CL_ORD_FST_LST_SCH | ORDER_ID | No | No | No |  |
| 8 | SPEC_TST_ORDER_ID | DENT_ORD_NOADD | ORDER_ID | No | No | No |  |
| 8 | SPEC_TST_ORDER_ID | DUPMED_DISMISS_HH_INFO | ORDER_ID | No | No | No |  |
| 8 | SPEC_TST_ORDER_ID | ENDOSCOPY_METRICS | ORDER_ID | Unknown | No | No |  |
| 8 | SPEC_TST_ORDER_ID | EXTERNAL_ORDER_INFO | ORDER_ID | No | No | No |  |
| 8 | SPEC_TST_ORDER_ID | F_IMG_STUDY | ORDER_ID | Unknown | Unknown | No |  |
| 8 | SPEC_TST_ORDER_ID | F_IP_HSP_SUM_ORDER | ORDER_ID | Unknown | Unknown | No |  |
| 8 | SPEC_TST_ORDER_ID | F_LAB_ORDERS | ORDER_ID | Unknown | Unknown | No |  |
| 8 | SPEC_TST_ORDER_ID | F_MU_OBJ_EH_PLACED_ORDER | ORDER_ID | Unknown | Unknown | No |  |
| 8 | SPEC_TST_ORDER_ID | F_MU_OBJ_EH_RESULTD_ORDER | ORDER_PROC_ID | Unknown | Unknown | No |  |
| 8 | SPEC_TST_ORDER_ID | F_ONC_PRIOR_AUTH_ORDERS | ORDER_ID | Unknown | Unknown | No |  |
| 8 | SPEC_TST_ORDER_ID | F_OPIOID_ORDERS | ORDER_ID | Unknown | Unknown | No |  |
| 8 | SPEC_TST_ORDER_ID | F_RX_ORDER | ORDER_MED_ID | Unknown | Unknown | No |  |

_(844 total; showing first 30)_
