# ACUITY_CONFIG

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=ACUITY_CONFIG

## Description

This table contains the configuration information for the acuity systems.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | HDA |
| Release Version | Summer 2009 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| ACUITY_SYSTEM_ID | NUMERIC (18,0) | The unique identifier (.1 item) for the acuity system record. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| ACUITY_SYSTEM_NAME | VARCHAR (200) | The name of this HDA record. |
| RECORD_STATUS_C | INTEGER |  |
| DISPLAY_NAME | VARCHAR (250) | This string determines how the acuity system's name will be displayed throughout the system.  For Acuity Systems with ACUITY_REC_TYPE_C (HDA/40) equal to 3-Advanced Model, this column has been replaced by column MODEL_DISP_NAME (HDA/1150) in table ACUITY_OVERTIME_SETTINGS. |
| DISPLAY_COLUMN_ID | NUMERIC (18,0) | This item links into a PAF column which will be synched to display the acuity score for this system. |
| DISCOL_ID_STOCK_TI | NUMERIC (18,0) | This item links to a PAF column which will be synched to display the stock ticker for this system. |
| DISID_TM_SINC_REVI | NUMERIC (18,0) | This item links to a PAF column which will be synched to display the time since last reviewed for this system. |
| SCORING_SYS_PG_ID | NUMERIC (18,0) | This column stores the print group ID associated with this scoring system. |
| INST_NOADD_EDT_DTTM | DATETIME | The instant at which no-add data in the record was last edited. |
| INST_REC_UPDT_DTTM | DATETIME (Attached) | The instant at which record was last updated. |
| METRIC_TEMPLATE_C | INTEGER |  |
| METRIC_DESC | VARCHAR (508) | This item contains the description displayed to the user when more information about a metric is requested. |
| GRP_CAT_C | INTEGER |  |
| FORMAT_TYPE_C | INTEGER |  |
| DIRECTION_C | INTEGER |  |
| GOAL | INTEGER | The goal for the metric. For percents, use whole numbers without the percent symbol, such as 80 if the goal is 80%.  For times, specify the goal in number of seconds, so if the goal is 20 minutes, enter 1200. |
| GOAL_TEXT | VARCHAR (254) | The text shown to the end user describing the goal expectations. |
| METRIC_DATA_TYPE_C | INTEGER |  |
| BACKGROUND_ONLY_YN | VARCHAR (1) |  |
| SCALE_MIN | INTEGER | The minimum value displayed in a numeric scale Pulse metric. |
| SCALE_MAX | INTEGER | The maximum value displayed in a numeric scale Pulse metric. |
| RADAR_DEFINITION | NUMERIC (18,0) | Link to IDN record used by Pulse to populate CSF data. |
| METRIC_APP_C | INTEGER |  |
| ACUITY_REC_TYPE_C | INTEGER |  |
| MODEL_ALGORITHM_C *(deprecated)* | INTEGER |  |
| FLO_MEAS_ID | VARCHAR (18) | The unique ID of the Flowsheet Row into which this scoring system should file its score. |
| TEMPLATE_ID | VARCHAR (18) | The unique ID of the Flowsheet Template which this scoring system should use when filing a score to a Flowsheet Row. |
| DATA_TO_RDI_YN | VARCHAR (1) |  |
| DATA_VALID_TIME | INTEGER | Store the time (in seconds) that this score should be considered valid. |
| SCR_FILTER_RULE_ID | VARCHAR (18) | This item determines whether a score is assigned to a patient based on the results of the rule set in this field. When the conditions of the rule are not met, no score is assigned. If no rule is set, all patients will receive scores. |
| MODEL_USAGE_DATE | DATETIME | The last date the predictive model was used to score a record. This is only tracked for predictive analytics models. |
| MODEL_PARENT_ID | NUMERIC (18,0) | The ID of the original parent model used in duplication. |
| MODEL_EXTERNAL_ENDPOINT_ID | NUMERIC (18,0) | This item stores the E0A record ID to be used for this predictive model. |
| MODEL_OVERRIDE_YN | VARCHAR (1) |  |
| MODEL_MAJOR_TRAIN | VARCHAR (200) | This item stores which major version to use for retrains. |
| BATCH_SIMPLE_ACTION_ID | NUMERIC (18,0) | This item stores the batch simple report action which will recalculate scores and file them to RDI. |
| MODEL_DATABASE | VARCHAR (3) | This item stores the model's database context. |
| NO_DATABASE_YN | VARCHAR (1) |  |
| DISPLAY_NULL_AS_HYPHEN_YN | VARCHAR (1) |  |
| BATCH_RESUB_FREQ_C | INTEGER |  |
| BATCH_RESUB_PERIOD_LOW_NUM | INTEGER | The lower bound on how often to run (in minutes). Used for batch job build inspector check. |
| BATCH_RESUB_PERIOD_HIGH_NUM | INTEGER | The upper bound on how often to run (in minutes). Used for batch job build inspector check. |
| BATCH_RESUB_INTERVAL_NUM | INTEGER | Number of days between recurrences (1 is typical). Used for batch job build inspector check. |
| BATCH_RESUB_START_TIME | DATETIME (Local) | The earliest time a customer can configure a run (00:00 is typical). Used for batch job build inspector check. |
| BATCH_RESUB_END_TIME | DATETIME (Local) | The latest time a customer can configure a run (23:59 is typical). Used for batch job build inspector check. |
| MODEL_REG_SCORE_RULE_ID | VARCHAR (18) | The unique ID associated with the released registry metric scoring rule corresponding to this model. This column will only be populated for rows of released Acuity Systems that represent registry-based predictive models. |
| MODEL_DATABASE_ITEM | INTEGER | Records the item number for an INI that the model uses for prediction. Category based recommender systems use this to look up the the category list options. |
| AISERVICES_TYPE_C | INTEGER |  |
| CLOUD_ARCHIVE_YN | VARCHAR (1) |  |
| PRIMARY_MODEL_RES_TYPE_C | INTEGER |  |
| NL_PLATFORM_IDENT | VARCHAR (2) | The unique identifier used for workflows within the NL Platform, including chatbot and assistant models. |
| MODEL_MAX_ENTY_NUM | INTEGER | Determines the maximum number of records that can be sent to Nebula in one batched scoring request for the model. |
| MODEL_ENSEMBLE_CNT | INTEGER | The number of models participating in an ensemble prediction. For prompt-based classifiers, this is the number of times the language model is queried with the prompt. |
| FEEDBACK_YN | VARCHAR (1) |  |
| WORKLOAD_TRTMNT_TEAM_REL_C | VARCHAR (66) |  |
| POINTS_PER_HOUR | NUMERIC (15,4) | The number of points scored for an hour of work |
| USAGE_TRACKING_YN | VARCHAR (1) |  |
| MODEL_DASHBOARD_ID | NUMERIC (18,0) | This contains the dashboard (IDM) ID that can be used to track reporting data for this generative AI feature. |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ACUITY_SYSTEM_ID | DISEASE_RISK_MODEL | ACUITY_SYSTEM_ID | No | No | No |  |
| 1 | ACUITY_SYSTEM_ID | PM_TRANSFER_CONFIG | ACUITY_SYSTEM_ID | No | No | No |  |
| 2 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 2 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 2 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 3 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 5 | RECORD_STATUS_C | ZC_DEL_STATUS | DEL_STATUS_C | No | No | No |  |
| 5 | RECORD_STATUS_C | ZC_EDG_REC_STAT | EDG_REC_STAT_C | No | No | No |  |
| 5 | RECORD_STATUS_C | ZC_ERS_REC_STAT | RECORD_STATUS_C | No | No | No |  |
| 5 | RECORD_STATUS_C | ZC_HCD_REC_STATE | HCD_REC_STATE_C | No | No | No |  |
| 5 | RECORD_STATUS_C | ZC_HFL_RECORD_STAT | HFL_RECORD_STAT_C | No | No | No |  |
| 5 | RECORD_STATUS_C | ZC_IMM_REC_STATUS | IMM_REC_STATUS_C | No | No | No |  |
| 5 | RECORD_STATUS_C | ZC_LLB_STATUS | LLB_STATUS_C | No | No | No |  |
| 5 | RECORD_STATUS_C | ZC_LMA_RECORD_STAT | LMA_RECORD_STAT_C | No | No | No |  |
| 5 | RECORD_STATUS_C | ZC_MEM_REC_STATUS | MEM_REC_STATUS_C | No | No | No |  |
| 5 | RECORD_STATUS_C | ZC_OR_REC_STATUS | OR_REC_STATUS_C | No | No | No |  |
| 5 | RECORD_STATUS_C | ZC_PBA_REC_STAT | PBA_REC_STAT_C | No | No | No |  |
| 5 | RECORD_STATUS_C | ZC_PROV_REC_STATE | PROV_REC_STATE_C | No | No | No |  |
| 5 | RECORD_STATUS_C | ZC_RECORD_STATE_2 | RECORD_STATE_2_C | No | No | No |  |
| 5 | RECORD_STATUS_C | ZC_RECORD_STATE_3 | RECORD_STATE_3_C | No | No | No |  |
| 5 | RECORD_STATUS_C | ZC_RECORD_STATE_4 | RECORD_STATE_4_C | No | No | No |  |
| 5 | RECORD_STATUS_C | ZC_RECORD_STATE_6 | RECORD_STATE_6_C | No | No | No |  |
| 5 | RECORD_STATUS_C | ZC_RECORD_STATE_7 | RECORD_STATE_7_C | No | No | No |  |
| 5 | RECORD_STATUS_C | ZC_RECORD_STAT_EPM | RECORD_STAT_EPM_C | No | No | No |  |
| 5 | RECORD_STATUS_C | ZC_RECORD_STAT_EPP | RECORD_STAT_EPP_C | No | No | No |  |
| 5 | RECORD_STATUS_C | ZC_RECORD_STAT_ETX | RECORD_STAT_ETX_C | No | No | No |  |
| 5 | RECORD_STATUS_C | ZC_RECORD_STAT_HRV | RECORD_STAT_HRV_C | No | No | No |  |
| 5 | RECORD_STATUS_C | ZC_RECORD_STAT_RMC | RECORD_STAT_RMC_C | No | No | No |  |

_(67 total; showing first 30)_
