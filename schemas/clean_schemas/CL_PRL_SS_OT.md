# CL_PRL_SS_OT

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=CL_PRL_SS_OT

## Description

This table contains the contact specific settings for each SmartSet or Protocol.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | PRL |
| Release Version | SPRING 2007 |
| May contain EHI? | No |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| PROTOCOL_ID | NUMERIC (18,0) | SmartSet/Protocol ID. |
| CONTACT_DATE_REAL | No | This is a numeric representation of the contact date of this record in your system. The integer portion of the number specifies the contact date of the record. The digits after the decimal point indicate multiple contacts created in one day. |
| CONTACT_DT | DATETIME | The date of this contact in calendar format. |
| CM_CT_OWNER_ID | VARCHAR (25) | ID of the deployment owner for this contact. |
| CONTACT_NUM | VARCHAR (5) | The contact number of this SmartSet/Protocol. |
| DISPLAY_NAME | VARCHAR (500) | This is the display name for this SmartSet/Protocol. |
| VERSION_STATUS_C | INTEGER |  |
| FILTER_LOCATOR_ID | NUMERIC (18,0) | The ID of the advisory record used to restrict the use of this SmartSet. This column is networked to LGL. |
| REL_DATE_C | INTEGER |  |
| SECTION_SELECTED_YN | VARCHAR (1) |  |
| DISALLOW_USER_OV_YN | VARCHAR (1) |  |
| DISCONT_ACTION_C | INTEGER |  |
| OSET_SEC_IN_PND_C | INTEGER |  |
| MERGE_SEQUENCE | INTEGER | This is the sequence that ordersets are merged in. |
| RESTRICTION_YN | VARCHAR (1) |  |
| ORDERSET_ID | NUMERIC (18,0) | The ID of the Treatment Day for this SmartSet.  It is networked to OSQ. If this PRL record is a Protocol, not a SmartSet, this will be the ID of the first Treatment Day in the Protocol. All of the Protocol Treatment Day information can be found in the table CL_PRL_TXDAYS. |
| RELEASE_TM | DATETIME (Local) | The date and time when the record was released in the SmartSet editor. |
| TEST_TM | DATETIME (Local) | The date and time when the record was released for testing in the SmartSet editor. |
| RETIRE_TM | DATETIME (Local) | The date and time when the record was retired in the SmartSet editor. |
| CLIN_REVIEWED_YN | VARCHAR (1) |  |
| FORM_ID | VARCHAR (18) | The questionnaire associated with this record. It is networked to LQF. |
| CNCT_STATUS_C | INTEGER |  |
| PRL_ABBREVIATION | VARCHAR (254) | The abbreviation of the protocol in this row. |
| PRL_DESCRIPTION | VARCHAR (254) | The description of the protocol in this row. This only extracts the first 254 characters. |
| RESEARCH_YN | VARCHAR (1) |  |
| ZERO_BASED_YN | VARCHAR (1) |  |
| PRL_AGE_FROM | NUMERIC (18,0) | The beginning of an age range associated with this protocol to aid lookups. |
| PRL_AGE_TO | NUMERIC (18,0) | The end of an age range associated with this protocol to aid lookups. |
| PRL_SEX_C | VARCHAR (66) |  |
| SUPPRESS_INTRCT_YN | VARCHAR (1) |  |
| DW_ALERT | NUMERIC (18,3) | The default weight change alert threshold for the protocol in this row. |
| DB_ALERT | NUMERIC (18,3) | The default change alert threshold for BSA (body surface area) for this protocol. |
| DEFAULT_AUC | NUMERIC (18,3) | The default target AUC (area under the curve) for the protocol in this row. |
| OT_DEFAULT_DOSING_C | INTEGER |  |
| PRL_DAT | No | The DAT of this contact in the protocol. |
| CM_PHY_OWNER_ID | VARCHAR (25) | ID of the physical deployment owner for this record.  Physical owners will be where the data is hosted, either on the cross-over server or the owner deployment. |
| CM_LOG_OWNER_ID | VARCHAR (25) | ID of the logical deployment owner for this record.  Logical owners show the deployment where the record was created but doesn't represent if the record is a part of version skew. |
| DFLT_ADJ_WT_CF | NUMERIC (18,4) | This item stores the default correction factor to use when calculating adjused weight in a TPL created from this PRL. |
| ALLOW_CF_CHANGE_YN | VARCHAR (1) |  |
| FIRST_CYCLE_NUM | INTEGER | This is the cycle number of the first cycle in the protocol. |
| PUBLISH_STATUS_C | INTEGER |  |
| PUBLISH_DTTM | DATETIME (Local) | The instant (date and time) when the protocol was published. |
| RELEASING_USER_ID | VARCHAR (18) | The unique ID of the user who released this contact. |
| TESTING_USER_ID | VARCHAR (18) | The unique ID of the user who released this contact for testing. |
| RETIRING_USER_ID | VARCHAR (18) | The unique ID of the user who retired this contact. |
| PUBLISHING_USER_ID | VARCHAR (18) | The unique ID of the user who published this contact. |
| START_CYCLE_NUM | INTEGER | This is the cycle number of the 'start cycle' in the protocol. |
| STARTING_CYCLE | INTEGER | The cycle that is marked as the 'start cycle' in the protocol. |
| STARTING_CYC_REP | INTEGER | For the 'start cycle' of the protocol, this is used to determine which repetition of that cycle is the actual start cycle. |
| START_DELTA_DATE | INTEGER | The number of days this protocol extends before its real start date as computed by items 192 and 194 (STARTING_CYCLE and STARTING_CYCLE_REP). |
| DEFAULT_CRCL_LPP_ID | NUMERIC (18,0) | The unique ID of the default programming point used when calculating creatinine clearance for orders in a treatment plan created from this protocol. |
| ALLOW_CRCL_CHG_YN | VARCHAR (1) |  |
| EW_ENABLED_YN | VARCHAR (1) |  |
| SORT_MERGE_ALPHA_YN | VARCHAR (1) |  |
| REV_SCHEME_C | INTEGER |  |
| REV_DUE | VARCHAR (254) | The length of the verification, the units depend on the chosen scheme (in REV_SCHEME_C). |
| REV_EXPIRES | INTEGER | The length of time before verification expiration to warn users. The units depend on the chosen scheme (in REV_SCHEME_C). |
| REV_BLOCK_EXP | INTEGER | The length of time after verification expiration to allow treatment. |
| REV_ACCEPT_EARLY_C | INTEGER |  |
| REV_DUE_MSG | VARCHAR (254) | The message shown in the plan section when the plan is due for review. |
| REV_EXP_MSG | VARCHAR (254) | The message shown in the plan section when a plan's review has expired. |
| CONTACT_SERIAL_NUM | NUMERIC (18,0) | The contact serial number (CSN) of the protocol contact. |
| PROTOCOL_CONTENTS_C | INTEGER |  |
| USE_ANCHOR_YN | VARCHAR (1) |  |
| ALLOW_MAXBSA_CHG_YN | VARCHAR (1) |  |
| INSTANT_OF_CREATION_DTTM | DATETIME (UTC) | The instant this contact was created |
| CREATING_USER_ID | VARCHAR (18) | The user who created this contact |
| EXPRESS_LANE_YN | VARCHAR (1) |  |
| BMT_PROTOCOL_YN | VARCHAR (1) |  |
| EXLN_SHOW_COMM_YN | VARCHAR (1) |  |
| EXLN_SHOW_CHARGE_CAPTURE_YN | VARCHAR (1) |  |
| EXLN_COMM_SECTION_ID | NUMERIC (18,0) | Stores the navigator section to use for Communication Management when the SmartSet is used in Express Lane. |
| EXLN_CHARGE_CAPTURE_SECTION_ID | NUMERIC (18,0) | Specify the Charge Capture section to use when launching this Express Lane. |
| EXLN_LRP_ID | VARCHAR (18) | Stores the report linked to an Express Lane SmartSet. |
| DISABLE_USE_AUC_YN | VARCHAR (1) |  |
| EXLN_KEEP_STRUCT_YN | VARCHAR (1) |  |
| DEFAULT_BSA_ID | NUMERIC (18,0) | The default formula to use when calculating body surface area in a treatment plan created from this protocol. Only programming points listed in LSD-4371 are allowed. If no programing points is listed in LSD-4371, this item will be empty. |
| ALLOW_BSA_FORMULA_CHANGE_YN | VARCHAR (1) |  |
| ESTIMATED_TOTAL_COST | NUMERIC (18,2) | The estimated total cost of this protocol. |
| COST_BUCKET_OVRD | INTEGER | The cost range this protocol should be in. This is usually inferred from the average cost of the protocol, but can be overridden with the value from this item. |
| PLAN_SCHEDULING_WINDOW_COUNT | INTEGER | Stores the numeric amount for the scheduling window. |
| PLAN_SCHEDULING_WINDOW_UNIT_C | INTEGER |  |
| EXLN_MOBILE_LRP_ID | VARCHAR (18) | The Report to show when opening the Express Lane in a Mobile platform |
| ALLOW_RECALC_EACH_TIME_YN | VARCHAR (1) |  |
| IS_WEIGHT_OPTIONAL_YN | VARCHAR (1) |  |
| RFL_ALWAYS_CREATE_YN | VARCHAR (1) |  |
| ALLOW_PATTERNS_YN | VARCHAR (1) |  |
| MIN_CYCLES_FOR_EXTENSION | INTEGER | The number of planned cycles at which the system will check to see if the plan has a pattern to automatically add cycles to the plan. Overrides item LSD 77390. |
| NUM_CYCLES_TO_ADD | INTEGER | The number of pattern instances to automatically add to a plan when the number of planned cycles is at or below the value specified in item PRL 2001. Overrides item LSD 77391. |
| TRIGGER_ADJUST_DUE_TIMES_YN | VARCHAR (1) |  |
| CAN_USE_FLEX_START_DT_C | INTEGER |  |
| MAX_DAYS_MULTIDAY_INTERVAL | INTEGER | The maximum number of days between treatments in the multi-day interval for therapy plan orders. |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| B-TREE INDEX | EIX_CL_PRL_SS_OT__CT_SERIAL_NM | CONTACT_SERIAL_NUM | 1 | Yes | Yes |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | PROTOCOL_ID | CL_PRL_SS | PROTOCOL_ID | No | No | No |  |
| 4 | CM_CT_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 4 | CM_CT_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 4 | CM_CT_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 7 | VERSION_STATUS_C | ZC_VERSION_STATUS | VERSION_STATUS_C | No | No | No |  |
| 8 | FILTER_LOCATOR_ID | CL_LGL_NOADD_SING | LOCATOR_ID | Unknown | No | No |  |
| 8 | FILTER_LOCATOR_ID | LGL_IB_SETTINGS | LOCATOR_ID | Unknown | No | No |  |
| 9 | REL_DATE_C | ZC_REL_DATE | REL_DATE_C | No | No | No |  |
| 12 | DISCONT_ACTION_C | ZC_DISCONT_ACTION | DISCONT_ACTION_C | No | No | No |  |
| 13 | OSET_SEC_IN_PND_C | ZC_ORDSETSHWSCTN | ORDSETSHWSCTN_C | No | No | No |  |
| 13 | OSET_SEC_IN_PND_C | ZC_OSET_SEC_IN_PND | OSET_SEC_IN_PND_C | No | No | No |  |
| 16 | ORDERSET_ID | CL_OSQ | ORDERSET_ID | No | No | No |  |
| 21 | FORM_ID | CL_QFORM | FORM_ID | No | No | No |  |
| 21 | FORM_ID | CL_QFORM1 | FORM_ID | Unknown | No | No |  |
| 21 | FORM_ID | DECISION_TREE_INFO | DTREE_ID | No | No | No |  |
| 21 | FORM_ID | QUESR_INSTRUCTIONS | FORM_ID | No | No | No |  |
| 22 | CNCT_STATUS_C | ZC_METRIC_STATUS | METRIC_STATUS_C | No | No | No |  |
| 29 | PRL_SEX_C | ZC_PREF_PCP_SEX | PREF_PCP_SEX_C | No | No | No |  |
| 29 | PRL_SEX_C | ZC_SEX | RCPT_MEM_SEX_C | No | No | No |  |
| 34 | OT_DEFAULT_DOSING_C | ZC_DFLT_DOSING_OPT | DFLT_DOSING_OPT_C | No | No | No |  |
| 36 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 36 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 36 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 37 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 37 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 37 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 41 | PUBLISH_STATUS_C | ZC_PUBLISH_STATUS | PUBLISH_STATUS_C | No | No | No |  |
| 43 | RELEASING_USER_ID | CLARITY_EMP | USER_ID | Unknown | No | No |  |
| 43 | RELEASING_USER_ID | CLARITY_EMP_2 | USER_ID | Unknown | No | No |  |
| 43 | RELEASING_USER_ID | CLARITY_EMP_3 | USER_ID | Unknown | No | No |  |

_(108 total; showing first 30)_
