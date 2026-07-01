# OR_CASE_ALL_PROC

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=OR_CASE_ALL_PROC

## Description

The OR_CASE_ALL_PROC table contains OR management system case procedures.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | ORC |
| Release Version | MU1 - MAY 2001 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| OR_CASE_ID | VARCHAR (18) | The unique ID of the case record. |
| LINE | No | The number of the line of the procedure within the case. |
| OR_PROC_ID | VARCHAR (254) | The unique ID of the procedure record. |
| POS_C | INTEGER |  |
| LRB_C | INTEGER |  |
| ANES_TYPE_C | INTEGER |  |
| OP_REG_C | INTEGER |  |
| PICKLIST_GEN_C | INTEGER |  |
| TOTAL_LENGTH | INTEGER | The total amount of time required for the case. This includes all procedures in all panels as well as the setup and cleanup times for the case. |
| PANEL | INTEGER | The procedure panel within which this procedure is contained. This is a numeric value between 1 and 5. |
| COMMENTS | VARCHAR (500) | The free text comments for this procedure. |
| CM_PHY_OWNER_ID | VARCHAR (25) | ID of the physical deployment owner for this record.  Physical owners will be where the data is hosted, either on the cross-over server or the owner deployment. |
| CM_LOG_OWNER_ID | VARCHAR (25) | ID of the logical deployment owner for this record.  Logical owners show the deployment where the record was created but doesn't represent if the record is a part of version skew. |
| DEFAULTED_LENGTH | NUMERIC (18,2) | The length defaulted for this procedure by the system in minutes. |
| RESOURCE_PREF_ID | VARCHAR (254) | The procedure or preference card ID used to default the resources in the case for this procedure. |
| PICKLIST_PREF_ID | VARCHAR (254) | The procedure or preference card ID used to default the pick list in the case for this procedure. |
| LENGTH_MODIFIED_YN | VARCHAR (1) |  |
| MATCHED_PREF_ID | VARCHAR (254) | This item stores the preference card that has been selected to override the defaulted preference card. |
| POSSIBLE_PROC_YN | VARCHAR (1) |  |
| DBC_EPISODE_ID | NUMERIC (18,0) | Stores the Diagnose Behandel Combinatie (DBC) episode associated with the current procedure. Used in billing. |
| PROC_EAP_ID | NUMERIC (18,0) | Stores the ordered procedure (EAP) associated with the preference card. |
| ALL_PROC_AS_ORDERED | VARCHAR (500) | Specify the procedure name as exactly ordered by the surgeon/provider. |
| ALL_PROC_CODE_ID | NUMERIC (18,0) | This item stores the procedure (EAP) linked to the procedure code. This column is only populated for older surgical cases which were created and last modified before upgrading to the Epic Nov 2022 version. For newer surgical cases, codes are in OR_OPE_PROC_CODE.PROC_CODE_ID.  OR_CASE_ALL_PROC joins to OR_OPE_PROC_CODE on column ALL_PANEL_ADDL_OPE_ID. |
| ALL_DEF_OR_PROC_ID | VARCHAR (254) | This item stores the defaulted preference card. |
| PROC_DISPLAY_NAME | VARCHAR (500) | This stores the procedure display name for the scheduled procedure. |
| ALL_PANEL_ADDL_OPE_ID | NUMERIC (18,0) | Stores the pointer to the procedure additional data record for all panels. |
| ALL_PANEL_ORDER_ID | NUMERIC (18,0) | This item stores the order ID for the procedure request associated with the procedure plan case. |
| ORDINAL | INTEGER | This item stores the line number for this procedure request in the panel where the procedure is added. |
| EXTERNAL_PROC_NAME | VARCHAR (200) | Free-text procedure name for the external procedure. |
| EXT_PROC_REF_IDENT | VARCHAR (174) | Stores the reference ID of the external procedure associated with this panel. |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| B-TREE INDEX | EIX_OR_CASE_ALL_PROC_ANTYC | ANES_TYPE_C | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_OR_CASE_ALL_PROC_DBC_ID | DBC_EPISODE_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_OR_CASE_ALL_PROC_EAP_ID | PROC_EAP_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_OR_CASE_ALL_PROC_MATCH_PRF | MATCHED_PREF_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_OR_CASE_ALL_PROC_ORPRID | OR_PROC_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_OR_CASE_ALL_PROC_PICK_PREF | PICKLIST_PREF_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_OR_CASE_ALL_PROC_RES_PREF | RESOURCE_PREF_ID | 1 | Yes | Yes |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | OR_CASE_ID | OR_CASE | OR_CASE_ID | Unknown | No | No |  |
| 1 | OR_CASE_ID | OR_CASE_2 | CASE_ID | Unknown | No | No |  |
| 1 | OR_CASE_ID | OR_CASE_3 | CASE_ID | Unknown | No | No |  |
| 1 | OR_CASE_ID | OR_CASE_4 | OR_CASE_ID | No | No | No |  |
| 1 | OR_CASE_ID | OR_CASE_VIRTUAL | OR_CASE_ID | No | No | No |  |
| 1 | OR_CASE_ID | V_OR_CASE_ORR | CASE_ID | Unknown | Unknown | No |  |
| 3 | OR_PROC_ID | OR_PROC_2 | OR_PROC_ID | No | No | No |  |
| 3 | OR_PROC_ID | OR_PROC_CONSENT_CONFIG | PROC_ID | No | No | No |  |
| 4 | POS_C | ZC_OR_POSITION | POSITION_C | No | No | No |  |
| 4 | POS_C | ZC_OR_POS_BODY | OR_POS_BODY_C | No | No | No |  |
| 5 | LRB_C | ZC_OR_LRB | LRB_C | No | No | No |  |
| 6 | ANES_TYPE_C | ZC_OR_ANESTH_TYPE | ANESTHESIA_TYPE_C | No | No | No |  |
| 7 | OP_REG_C | ZC_OR_OP_REGION | OPERATING_REGION_C | No | No | No |  |
| 8 | PICKLIST_GEN_C | ZC_OR_PICKLIST_GEN | PICKLIST_GEN_C | No | No | No |  |
| 12 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 12 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 12 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 13 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 13 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 13 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 15 | RESOURCE_PREF_ID | OR_PROC | OR_PROC_ID | Unknown | No | No |  |
| 15 | RESOURCE_PREF_ID | OR_PROC_2 | OR_PROC_ID | No | No | No |  |
| 15 | RESOURCE_PREF_ID | OR_PROC_CONSENT_CONFIG | PROC_ID | No | No | No |  |
| 16 | PICKLIST_PREF_ID | OR_PROC | OR_PROC_ID | Unknown | No | No |  |
| 16 | PICKLIST_PREF_ID | OR_PROC_2 | OR_PROC_ID | No | No | No |  |
| 16 | PICKLIST_PREF_ID | OR_PROC_CONSENT_CONFIG | PROC_ID | No | No | No |  |
| 18 | MATCHED_PREF_ID | OR_PROC | OR_PROC_ID | Unknown | No | No |  |
| 18 | MATCHED_PREF_ID | OR_PROC_2 | OR_PROC_ID | No | No | No |  |
| 18 | MATCHED_PREF_ID | OR_PROC_CONSENT_CONFIG | PROC_ID | No | No | No |  |
| 20 | DBC_EPISODE_ID | ADMIN_PATHWAY_PERIOD | ADMIN_PWY_PERIOD_ID | Unknown | No | No |  |

_(159 total; showing first 30)_
