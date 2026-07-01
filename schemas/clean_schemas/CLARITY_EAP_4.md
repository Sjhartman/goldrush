# CLARITY_EAP_4

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=CLARITY_EAP_4

## Description

The CLARITY_EAP_4 table contains basic information about the procedure records in your system. This includes both A/R and clinical procedures. This is a continuation of Clarity table CLARITY_EAP.

**Overflow table** for CLARITY_EAP (149 cols). Contains additional columns for the same records — join on the shared primary key column.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | EAP |
| Release Version | Rel 2017 |
| May contain EHI? | No |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| PROC_ID | NUMERIC (18,0) | The unique identifier for the procedure record |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| DENTAL_SURF_LOGIC_C | INTEGER |  |
| DENTAL_TOOTH_SET_C | INTEGER |  |
| DENTAL_ARCH_C | INTEGER |  |
| DEFAULT_EXPECTED_DATE_CMT_C | INTEGER |  |
| DEFAULT_FASTING_DURATION | INTEGER | The default fasting duration in hours. If this procedure is linked to an appointment with a visit type that has a fasting duration, whichever duration is longer will be used. |
| BREAKS_FAST_YN | VARCHAR (1) |  |
| THIRD_PARTY_YN | VARCHAR (1) |  |
| MYC_TKT_GEN_RULE_ID | VARCHAR (18) | A rule which specifies the requirement to generate scheduling tickets for orders. If true for an order, a ticket will be generated. If false, a ticket will not be generated. |
| ALLOW_WOUND_LINK_YN | VARCHAR (1) |  |
| RAD_THP_CREATE_EPSD_QUEST_ID | VARCHAR (18) | Used to determine if a radiation therapy episode should be created when a radiation simulation procedure is signed and whether task templates should be applied. This item must be set to "Yes" if you want an episode to be created and task templates to be applied. If set to "No" nothing will happen. The default is "No". |
| RAD_THERAPY_SITE_QUEST_ID | VARCHAR (18) | This item specifies an order question to be looked at to determine the treatment site that will be treated. |
| RAD_THERAPY_TECHNIQUE_QUEST_ID | VARCHAR (18) | This item specifies the order question to be looked at to determine the treatment technique that will be used for treatment. |
| RAD_THP_DFLT_TASKTMP_RECORD_ID | VARCHAR (18) | This item defines the default task template to be applied. |
| PROSTHETIC_STRUCT_C | INTEGER |  |
| PARTIAL_DENT_TYP_C | INTEGER |  |
| DERM_PROC_TYPE_C | INTEGER |  |
| QUICK_PROC_YN | VARCHAR (1) |  |
| DERM_PROC_FORM_ID | VARCHAR (18) | Contains the SmartForm that will be used to document Dermatology Procedure. |
| RAD_THP_PLAN_START_DT_QUEST_ID | VARCHAR (18) | This item points to an LQL record that is used to ask about the planned start date of an episode of radiation therapy. |
| RAD_THP_LATERALITY_QUEST_ID | VARCHAR (18) | This item points to an LQL record that is used to ask about the lateralities of sites associated with an episode of radiation therapy. (This question works in tandem with EAP 53520 - Radiation Therapy Treatment Site Question; lateralities correspond to sites.) |
| RAD_THP_TREAT_GOAL_QUEST_ID | VARCHAR (18) | This item points to an LQL record that is used to ask about the goal of treatment in an episode of radiation therapy. |
| PURPOSE_MATERIAL_C | INTEGER |  |
| CONFIDENTIAL_YN | VARCHAR (1) |  |
| DENT_CHG_PER_TTH_YN | VARCHAR (1) |  |
| WOUND_PROC_TYPE_C | INTEGER |  |
| PROC_ABBR | VARCHAR (10) | The abbreviation (10 characters or fewer) of the procedure name. |
| SCHED_AVAIL_ALERT_YN | VARCHAR (1) |  |
| MATERIAL_IN_TOOTH_C | INTEGER |  |
| QLTY_ROOT_FILLING_C | INTEGER |  |
| TOOTH_PROS_STRUCT_C | INTEGER |  |
| IMPLNT_CROWN_TYPE_C | INTEGER |  |
| DEN_AVAIL_IN_WIS_YN | VARCHAR (1) |  |
| FUTURE_ORD_REQ_FIELD_C | INTEGER |  |
| GENOMICS_PROC_CLASS_C | INTEGER |  |
| REQUIRE_WOUND_QF_DATA_REQ_C | INTEGER |  |
| IS_RADIATION_THERAPY_PROC_YN | VARCHAR (1) |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | PROC_ID | CLARITY_EAP | PROC_ID | No | No | No |  |
| 1 | PROC_ID | CLARITY_EAP_2 | PROC_ID | No | No | No |  |
| 1 | PROC_ID | CLARITY_EAP_3 | PROC_ID | No | No | No |  |
| 1 | PROC_ID | CLARITY_EAP_5 | PROC_ID | No | No | No |  |
| 1 | PROC_ID | CLARITY_EAP_IMM | PROC_ID | Unknown | No | No |  |
| 1 | PROC_ID | PROC_CONSENT_CONFIG | PROC_ID | No | No | No |  |
| 1 | PROC_ID | PROC_UM | PROC_ID | No | No | No |  |
| 1 | PROC_ID | V_CUBE_D_PROCEDURE | PROCEDURE_ID | Unknown | Unknown | No |  |
| 2 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 2 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 2 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 3 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 4 | DENTAL_SURF_LOGIC_C | ZC_DENTAL_SURF_LOGIC | DENTAL_SURF_LOGIC_C | No | No | No |  |
| 5 | DENTAL_TOOTH_SET_C | ZC_DENTAL_TOOTH_SET | DENTAL_TOOTH_SET_C | No | No | No |  |
| 6 | DENTAL_ARCH_C | ZC_DENT_ARCH | ARCH_C | No | No | No |  |
| 7 | DEFAULT_EXPECTED_DATE_CMT_C | ZC_EXPECT_DT_BUTTON | EXPECT_DT_BUTTON_C | No | No | No |  |
| 11 | MYC_TKT_GEN_RULE_ID | CLARITY_CER | RULE_ID | No | No | No |  |
| 11 | MYC_TKT_GEN_RULE_ID | CL_CHRG_EDIT_RULE | RULE_ID | No | No | No |  |
| 13 | RAD_THP_CREATE_EPSD_QUEST_ID | CL_QQUEST | QUEST_ID | No | No | No |  |
| 14 | RAD_THERAPY_SITE_QUEST_ID | CL_QQUEST | QUEST_ID | No | No | No |  |
| 15 | RAD_THERAPY_TECHNIQUE_QUEST_ID | CL_QQUEST | QUEST_ID | No | No | No |  |
| 16 | RAD_THP_DFLT_TASKTMP_RECORD_ID | TASK_INFO | RECORD_ID | No | No | No |  |
| 17 | PROSTHETIC_STRUCT_C | ZC_PROSTHETIC_STRUCT | PROSTHETIC_STRUCT_C | No | No | No |  |
| 18 | PARTIAL_DENT_TYP_C | ZC_PARTIAL_DENT_TYP | PARTIAL_DENT_TYP_C | No | No | No |  |
| 19 | DERM_PROC_TYPE_C | ZC_DERM_PROC_TYPE | DERM_PROC_TYPE_C | No | No | No |  |
| 21 | DERM_PROC_FORM_ID | CL_QFORM | FORM_ID | No | No | No |  |
| 21 | DERM_PROC_FORM_ID | CL_QFORM1 | FORM_ID | Unknown | No | No |  |
| 21 | DERM_PROC_FORM_ID | DECISION_TREE_INFO | DTREE_ID | No | No | No |  |

_(43 total; showing first 30)_
