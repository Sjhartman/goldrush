# ORDER_PROC_3

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=ORDER_PROC_3

## Description

The ORDER_PROC_3 table enables you to report on the procedures ordered in the clinical system. This procedure table has the same basic structure as ORDER_PROC, but was created as a third table to prevent ORDER_PROC_2 from getting any larger.

**Overflow table** for ORDER_PROC (102 cols). Contains additional columns for the same records — join on the shared primary key column.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | ORD |
| Release Version | Summer 2009 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| ORDER_ID | NUMERIC (18,0) | The unique identifier for the order record. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| MAMMO_OUTCOME_C | INTEGER |  |
| OLD_RAD_STAT_C | INTEGER |  |
| TRANSCRIPTIONIST | VARCHAR (192) | The transcriptionist of an external order result coming through the transcription interface. |
| ORDERING_MODE_C | INTEGER |  |
| PROV_STATUS_C | INTEGER |  |
| RESULT_TYPE_C | INTEGER |  |
| RFL_PRIORITY_C | VARCHAR (66) |  |
| REFLEX_ORDER_ID | NUMERIC (18,0) | The order ID from which this reflex order was created. |
| PROTOCOL_PERF_CODE | VARCHAR (254) | Performed Protocol Code Sequence:  Meant to indicate the protocol that was actually performed on the ordered procedure (can differ from protocol that was ordered).  Sequence specified DICOM documentation for MPPS messages.   See IHE EYECARE transaction [EYECARE-6]. |
| PROTOCOL_PERF_NAME | VARCHAR (254) | Name/description for the protocol that was actually performed on the ordered procedure (can differ from protocol that was ordered).  Correlates with Protocol Performed Code.  See IHE EYECARE transaction [EYECARE-6] |
| ORD_TRANS_METHOD_C | INTEGER |  |
| ORD_OSQ_ID | NUMERIC (18,0) | The unique ID of the Orderable OSQ that this order was created from. |
| ORD_OSQ_DATE | VARCHAR (254) | The date corresponding to the version of the parent Orderable OSQ used to place this order. |
| ORD_OSQ_OV_CTX | VARCHAR (254) | A descriptor that can be used to identify the override record used for the parent Orderable OSQ. |
| ORD_OSQ_ORDER_SRC_C | INTEGER |  |
| NUM_SIG_REQ | INTEGER | The number of physician signatures required to move the study status to final within the procedural applications. |
| RES_BY_EXT_LAB_YN | VARCHAR (1) |  |
| SPECIMEN_COUNT | INTEGER | Stores the number of specimens that will be created from this order. |
| FREQ_UNSCHEDULED_C | INTEGER |  |
| DURATION | INTEGER | Duration for this procedure. |
| FREQUENCY *(deprecated)* | VARCHAR (254) |  |
| INTERVENTION | VARCHAR (254) | Intervention for this procedure. |
| SUMM_UPDATE_DTTM | DATETIME (Local) | Instant that the summary sentence was generated for a signed order. |
| NEEDS_TRANSMITTAL_C | INTEGER |  |
| NEEDS_CHARGE_DROP_C | INTEGER |  |
| ORD_TRANSMTL_COM_YN | VARCHAR (1) |  |
| SS_PRL_ORD_SRC_C | INTEGER |  |
| CROSS_ENC_ORD_C | INTEGER |  |
| SIGN_ACTION_PEND_C | INTEGER |  |
| STAT_COMP_USER_ID | VARCHAR (18) | The ID of the user who marked an inpatient procedure as 'Complete' |
| STAT_COMP_DTTM | DATETIME (Local) | The time and date that an inpatient procedure was marked as 'Complete' |
| IS_EXT_READ_YN | VARCHAR (1) |  |
| PENDDC_STATUS_C | INTEGER |  |
| AUTOINTK_COMPL_YN | VARCHAR (1) |  |
| RESULT_LOCATION_C | INTEGER |  |
| STAND_EOW_ID | VARCHAR (18) | Holds the ID number of the Standing Status In Basket message associated with this Order.  The In Basket message informs the user that a standing order exists. |
| EXPIRING_EOW_ID | VARCHAR (18) | Holds the ID number of the Expiring Order In Basket message (EOW) associated with this Order.  The In Basket message informs the user that a future order is about to expire. |
| NEXT_PASS_NUM | INTEGER | Holds the next pass number that Order Transmittal needs to take on this Order. |
| OK_TO_CONTINUE_YN | VARCHAR (1) |  |
| INPAT_DISC_INTER_ID | VARCHAR (18) | This item stores the interval at which a standing order should be released for inpatient orders. |
| INPAT_AUTO_RLSE_YN | VARCHAR (1) |  |
| VERB_ORD_MESSAGE_ID *(deprecated)* | VARCHAR (18) | This column is no longer used.  Refer to tables ORDER_SIGNED_MED and ORDER_SIGNED_PROC for verbal information.  The deprecated column's content/data is no longer available since it is no longer populated in Chronicles. |
| ORD_PATHWAY_GRP_ID | NUMERIC (18,0) | The unique ID of the orderable OSQ's Pathway group record that contains this record. |
| ORD_PATHWAY_GRP_CSN | NUMERIC (18,0) | The CSN of the contact of orderable OSQ's Pathway group record that contains this record. |
| PENDING_RTX_YN | VARCHAR (1) |  |
| LAB_CRT_CNCT_CSN_ID | NUMERIC (18,0) | The unique contact serial number for the contact that was created from this order. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| LAB_SPCL_RES_TYPE_C | INTEGER |  |
| INSTANT_MET_DTTM | DATETIME (Local) | Stores the instant when the condition was marked as "met/satisfied" (ORD-1401) for an inpatient conditional order. |
| LAST_OVERALL_ASMT_C | VARCHAR (66) |  |
| REVENUE_CODE_ID | NUMERIC (18,0) | The revenue code associated with the service. |
| UNITS_REQUESTED | INTEGER | The number of units requested for the service. |
| UNITS_APPROVED | INTEGER | The number of units approved for the service. |
| TOTAL_PRICE | NUMERIC (18,2) | The total price of the service. |
| PATIENT_PORTION | NUMERIC (18,2) | The amount or portion the patient will have to pay for the service they are being referred for. |
| AUTH_REQUIRED | VARCHAR (1) | This column stores whether or not authorization is required for the service. |
| NET_PAYABLE | NUMERIC (18,2) | The net payable of the service. |
| NOT_COVERED | VARCHAR (24) | This item indicates whether or not the service is covered. |
| PROVIDING_PROV_ID | VARCHAR (18) | The provider on the service. |
| COMMENT_WITH_CANCEL | VARCHAR (2044) | Comment entered while cancelling an order. |
| SCHED_ORD_EXT_ID | VARCHAR (254) | Schedule orders external id used for CS and EDI |
| AUTO_GENERATED_YN | VARCHAR (1) |  |
| SOFT_DEL_FLAG | VARCHAR (254) | Soft deletion flag for order records associated with order-based transcriptions, which were deleted by the transcription soft-deletion utility. |
| IS_CHRG_READY_C | VARCHAR (254) |  |
| CHARGE_TRIG_RSLT_C | INTEGER |  |
| PATH_NARR_NOTE_ID *(deprecated)* | VARCHAR (254) |  |
| RESULT_TRACK_STS_C | INTEGER |  |
| ORD_PHASE_OF_CARE_C | INTEGER |  |
| WORKSTN_OVERRIDE_ID | VARCHAR (18) | This item stores the override workstation ID (LWS .1). |
| REQUESTED_DEPT | VARCHAR (254) | This column contains the requested department. The item is populated by the Cadence Orders Interface. |
| REQUESTED_DATETIME | 171 | The requested date and time. The items extracted to this column are populated by the Cadence Orders Interface. |
| PRINT_LOCAL_COPY_YN | VARCHAR (1) |  |
| ORX_ID | NUMERIC (18,0) | Contains an ID from Order Lookup Index. This may be populated if an order originates from an Order Panel. |
| RELEASED_INSTA_DTTM | DATETIME (Local) | Stores the scheduled instant of the child order. |
| HQID | VARCHAR (254) | Stores the queue ID when an order release is scheduled for a later instant. This ID corresponds to the ^HGEN("QITEM",###) node. |
| LAST_SCHE_INST_DTTM | DATETIME (UTC) | This item stores the inpatient order's last scheduled instant. |
| AR_INTERFACE_STAT_C | INTEGER |  |
| INTERACT_COMMENT | VARCHAR (254) | Interaction override comment. |
| COPY_POINTER_ID | NUMERIC (18,0) | This object tracks order record links created when using the inpatient or ambulatory order mover utilities to move an order record. This item is populated on the source order record and points to the target order record(s) created. |
| AFTER_ORDER_ID | VARCHAR (254) | This column contains the After Order ID for an order after Order Transmittal. |
| BEFORE_ORDER_ID | VARCHAR (254) | This column contains the Before Order ID for an order before Order Transmittal. |
| DIET_COMMENTS | VARCHAR (508) | This column contains the Diet Comments entered for an order. |
| ORD_CONDITION_FLAG | INTEGER | This column contains the a Condition Flag if this is an order created from certain condition. |
| PREV_POC_C | INTEGER |  |
| COR_AFTR_FINAL_DTTM | DATETIME (Local) | The date and time when the study was corrected and finalized. |
| OVERRIDE_RRRECP_C | INTEGER |  |
| IS_HELD_ORDER_C | INTEGER |  |
| NOCHRG_EXT_RSLT_YN | VARCHAR (1) |  |
| PROC_PERF_LOC_ID | NUMERIC (18,0) | Stores the location (EAF) at which the procedure will take place. |
| PROTOCOL_STATUS_C | INTEGER |  |
| PROTCL_ASGN_POOL_ID | VARCHAR (18) | If an order's protocol has been assigned to a pool, this item contains the pool ID of the assigned pool. |
| PROTCL_ASGN_PROV_ID | VARCHAR (18) | If an order's protocol has been assigned to a provider, this item contains the provider ID of the assigned provider. |
| EXCL_FROM_MQSA_YN | VARCHAR (1) |  |
| ORDER_CONTEXT_ID | NUMERIC (18,0) | Pointer to the order context record. |
| PREV_ORD_CONTEXT_ID | NUMERIC (18,0) | This item stores the context the order was linked to prior to being released. |
| CONTEXT_CREATED_ID | NUMERIC (18,0) | Stores the context (ODC) ID that was created by the order. |
| COLLECT_PPID_REQ_C | INTEGER |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ORDER_ID | ADT_ORDERS_ERRORS | ORDER_ID | No | No | No |  |
| 1 | ORDER_ID | ADT_ORDER_INFORMATION | ORDER_ID | No | No | No |  |
| 1 | ORDER_ID | APPT_REQUEST | REQUEST_ID | No | No | No |  |
| 1 | ORDER_ID | CL_ORD_FST_LST_SCH | ORDER_ID | No | No | No |  |
| 1 | ORDER_ID | DENT_ORD_NOADD | ORDER_ID | No | No | No |  |
| 1 | ORDER_ID | DUPMED_DISMISS_HH_INFO | ORDER_ID | No | No | No |  |
| 1 | ORDER_ID | ENDOSCOPY_METRICS | ORDER_ID | Unknown | No | No |  |
| 1 | ORDER_ID | EXTERNAL_ORDER_INFO | ORDER_ID | No | No | No |  |
| 1 | ORDER_ID | F_IMG_STUDY | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_ID | F_IP_HSP_SUM_ORDER | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_ID | F_LAB_ORDERS | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_ID | F_MU_OBJ_EH_PLACED_ORDER | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_ID | F_MU_OBJ_EH_RESULTD_ORDER | ORDER_PROC_ID | Unknown | Unknown | No |  |
| 1 | ORDER_ID | F_ONC_PRIOR_AUTH_ORDERS | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_ID | F_OPIOID_ORDERS | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_ID | F_RX_ORDER | ORDER_MED_ID | Unknown | Unknown | No |  |
| 1 | ORDER_ID | HH_MED_ORD_IN_POC_DETAIL | ORDER_MED_ID | No | No | No |  |
| 1 | ORDER_ID | HV_ORDER_PROC | ORDER_PROC_ID | Unknown | No | No |  |
| 1 | ORDER_ID | MED_DETAILS_EXT_ORD | ORDER_ID | No | No | No |  |
| 1 | ORDER_ID | MERCHANDISE_ORDER_INFO | ORDER_ID | Yes | No | No |  |
| 1 | ORDER_ID | MU_EH_QRDA_I_ORDER | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_ID | ORDERS | ORDER_ID | No | No | No |  |
| 1 | ORDER_ID | ORDER_AUTH_INFO | ORDER_ID | No | No | No |  |
| 1 | ORDER_ID | ORDER_MED | ORDER_MED_ID | Unknown | No | No |  |
| 1 | ORDER_ID | ORDER_MEDINFO | ORDER_MED_ID | Unknown | No | No |  |
| 1 | ORDER_ID | ORDER_MED_2 | ORDER_ID | Unknown | No | No |  |
| 1 | ORDER_ID | ORDER_MED_3 | ORDER_ID | Unknown | No | No |  |
| 1 | ORDER_ID | ORDER_MED_4 | ORDER_ID | Unknown | No | No |  |
| 1 | ORDER_ID | ORDER_MED_5 | ORDER_ID | Unknown | No | No |  |
| 1 | ORDER_ID | ORDER_MED_6 | ORDER_MED_ID | Unknown | No | No |  |

_(484 total; showing first 30)_
