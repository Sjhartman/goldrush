# OR_LOG_ALL_PROC

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=OR_LOG_ALL_PROC

## Description

The OR_LOG_ALL_PROC table contains OR management system log procedures.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | ORL |
| Release Version | MU1 - MAY 2001 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| LOG_ID | VARCHAR (18) | The unique ID of the log referred to by this procedure. |
| LINE | No | The number of the line of procedure in the surgical log. |
| OR_PROC_ID | VARCHAR (254) | The unique ID of the procedure. |
| POS_C | INTEGER |  |
| ANES_TYPE_C | INTEGER |  |
| LRB_C | INTEGER |  |
| OP_REG_C | INTEGER |  |
| WND_CLS_C | INTEGER |  |
| WND_LOC_C | INTEGER |  |
| ALL_APPROACH_C | INTEGER |  |
| ALL_PROCS_TOT_TIME | INTEGER | The total time of all procedures in the log. |
| ALL_PROCS_PANEL | INTEGER | The number of the panel in which this procedure was performed. |
| COMMENTS | VARCHAR (500) | The free text comments for this procedure. |
| ORDINAL | INTEGER | The ordinal number of the positioning within the procedure. |
| CM_PHY_OWNER_ID | VARCHAR (25) | ID of the physical deployment owner for this record.  Physical owners will be where the data is hosted, either on the cross-over server or the owner deployment. |
| CM_LOG_OWNER_ID | VARCHAR (25) | ID of the logical deployment owner for this record.  Logical owners show the deployment where the record was created but doesn't represent if the record is a part of version skew. |
| RESOURCE_PREF_ID | VARCHAR (254) | Stores the procedure/preference id which was used to default resources (staff, equipment, etc.) corresponding to this procedure. |
| PICKLIST_PREF_ID | VARCHAR (254) | Stores the procedure/preference id whose pick list was copied to create the corresponding pick list for this procedure in the case. |
| MATCHED_PREF_ID | VARCHAR (254) | Stores the preference card that has been selected to override the defaulted preference card. NOTE: Starting in the Epic 2012 release, this column will display the ID of the selected preference card even though the column name says Matched Pref. The ID of the preference card that is matched or defaulted will be stored in I ORL 2018. |
| DBC_EPISODE_ID | NUMERIC (18,0) | Stores the Diagnosis Behandling Combinatie (DBC) episode associated with the current procedure. Used in billing. |
| PROC_EAP_ID | NUMERIC (18,0) | Stores the ordered procedure (EAP) associated with the preference card. |
| ALL_PROC_AS_ORDERED | VARCHAR (500) | Denotes the procedure name as exactly ordered by the surgeon/provider. |
| ALL_DEF_OR_PROC_ID | VARCHAR (254) | Stores the defaulted preference card. |
| ALL_PROC_CODE_ID | NUMERIC (18,0) | Stores the procedure (EAP) id of the procedure code in the procedure (ORP) record. This column is only populated for older surgical logs which were created and last modified before upgrading to the Epic 2018 version. For newer surgical logs, codes are in OR_OPE_PROC_CODE.PROC_CODE_ID. OR_LOG_ALL_PROC joins directly from OR_LOG_ALL_PROC.ALL_PANEL_ADDL_ID to OR_OPE_PROC.OPE_ID. |
| PROC_DISPLAY_NAME | VARCHAR (500) | This stores the procedure display name for the performed procedure based on the settings on the Procedure/Preference Card form in System Definitions. |
| ALL_PROCS_INCISION_CLOSURE_C | INTEGER |  |
| ALL_NHSN_CLOSURE_C | INTEGER |  |
| ALL_PANEL_ADDL_ID | NUMERIC (18,0) | Stores the pointer to the procedure additional data record for all panels. |
| ALL_PANEL_ORDER_ID | NUMERIC (18,0) | This item stores the order ID for the procedure request associated with the log created for the procedure plan case. |
| PROC_NAME | VARCHAR (200) | Free-text procedure name. This is only populated on the Cosmos host. |
| EXT_PROC_REF_IDENT | VARCHAR (174) | This stores the reference ID of the external data used to generate the procedure associated with this panel. |
| ASSOC_PROC_ID | NUMERIC (18,0) | This item contains the mapped procedure (EAP) ID for the associated panel. |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| B-TREE INDEX | EIX_OR_LOG_ALL_PROC_ANTYC | ANES_TYPE_C | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_OR_LOG_ALL_PROC_DBC_ID | DBC_EPISODE_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_OR_LOG_ALL_PROC_EAP_ID | PROC_EAP_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_OR_LOG_ALL_PROC_MAT_PRF_ID | MATCHED_PREF_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_OR_LOG_ALL_PROC_ORPRID | OR_PROC_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_OR_LOG_ALL_PROC_PCK_PRF_ID | PICKLIST_PREF_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_OR_LOG_ALL_PROC_RES_PRF_ID | RESOURCE_PREF_ID | 1 | Yes | Yes |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | LOG_ID | F_LOG_BASED | LOG_ID | Unknown | Unknown | No |  |
| 1 | LOG_ID | OR_LOG | LOG_ID | Unknown | No | No |  |
| 1 | LOG_ID | OR_LOG_2 | LOG_ID | Unknown | No | No |  |
| 1 | LOG_ID | OR_LOG_3 | LOG_ID | No | No | No |  |
| 1 | LOG_ID | OR_LOG_METRIC_DETAILS | LOG_ID | No | No | No |  |
| 1 | LOG_ID | OR_LOG_PRECEDING | LOG_ID | No | No | No |  |
| 1 | LOG_ID | OR_LOG_VIRTUAL | LOG_ID | No | No | No |  |
| 1 | LOG_ID | UK_CRM_PACEMKR_PROC | LOG_ID | No | No | No |  |
| 1 | LOG_ID | V_CASE_CHARGES | LOG_ID | Unknown | Unknown | No |  |
| 1 | LOG_ID | V_CASE_COSTS | LOG_ID | Unknown | Unknown | No |  |
| 1 | LOG_ID | V_CASE_ON_TIME_START | LOG_ID | Unknown | Unknown | No |  |
| 1 | LOG_ID | V_CASE_PHYS_TURNOVER | LOG_ID | Unknown | Unknown | No |  |
| 1 | LOG_ID | V_CASE_ROOM_TURNOVER | LOG_ID | Unknown | Unknown | No |  |
| 1 | LOG_ID | V_CASE_VOLUME | LOG_ID | Unknown | Unknown | No |  |
| 1 | LOG_ID | V_DECISION_TO_INCISION | LOG_ID | Unknown | Unknown | No |  |
| 1 | LOG_ID | V_LOG_BASED | LOG_ID | Unknown | Unknown | No |  |
| 1 | LOG_ID | V_LOG_TIMING_EVENTS | LOG_ID | Unknown | Unknown | No |  |
| 3 | OR_PROC_ID | OR_PROC_2 | OR_PROC_ID | No | No | No |  |
| 3 | OR_PROC_ID | OR_PROC_CONSENT_CONFIG | PROC_ID | No | No | No |  |
| 4 | POS_C | ZC_OR_POSITION | POSITION_C | No | No | No |  |
| 4 | POS_C | ZC_OR_POS_BODY | OR_POS_BODY_C | No | No | No |  |
| 5 | ANES_TYPE_C | ZC_OR_ANESTH_TYPE | ANESTHESIA_TYPE_C | No | No | No |  |
| 6 | LRB_C | ZC_OR_LRB | LRB_C | No | No | No |  |
| 7 | OP_REG_C | ZC_OR_OP_REGION | OPERATING_REGION_C | No | No | No |  |
| 8 | WND_CLS_C | ZC_OR_WOUND_CLASS | WND_CLS_C | No | No | No |  |
| 9 | WND_LOC_C | ZC_OR_OP_REGION | OPERATING_REGION_C | No | No | No |  |
| 10 | ALL_APPROACH_C | ZC_OR_APPROACH | ALL_APPROACH_C | No | No | No |  |
| 15 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 15 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 15 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |

_(183 total; showing first 30)_
