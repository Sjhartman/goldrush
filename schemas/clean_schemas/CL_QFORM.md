# CL_QFORM

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=CL_QFORM

## Description

The CL_QFORM table is the primary table for non-contact specific information related to questionnaire forms.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | LQF |
| Release Version | MU4 - MAY 2001 |
| May contain EHI? | No |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| FORM_ID | VARCHAR (18) | The unique ID of the questionnaire form record. |
| FORM_NAME | VARCHAR (250) | The name of the form record. |
| RECORD_STATE *(deprecated)* | INTEGER |  |
| FORM_TYPE_C | INTEGER |  |
| USE_OF_FORM | VARCHAR (80) | The description of how the form will be used. |
| REPORT_NAME *(deprecated)* | VARCHAR (80) | *** Deprecated *** In table CL_QFORM, the column REPORT_NAME (LRP/.2) has been deprecated. To look up the deprecated column's value after the Clarity Compass upgrade, join column CL_QFORM.REPORT_ID to table REPORT_DETAILS.REPORT_ID and get the REPORT_NAME value. |
| SORT_ORDER *(deprecated)* | INTEGER |  |
| VB_FORM_NAME *(deprecated)* | VARCHAR (80) | *** Deprecated *** In table CL_QFORM, the column VB_FORM_NAME (VBF/.2) has been deprecated. The deprecated column's content/data is no longer available since it is no longer extracted to Clarity. |
| COMMENTS | VARCHAR (255) | The comments printed when a graphic is sent to the printer. |
| CM_PHY_OWNER_ID | VARCHAR (25) | ID of the physical deployment owner for this record.  Physical owners will be where the data is hosted, either on the cross-over server or the owner deployment. |
| CM_LOG_OWNER_ID | VARCHAR (25) | ID of the logical deployment owner for this record.  Logical owners show the deployment where the record was created but doesn't represent if the record is a part of version skew. |
| PAT_FRNDLY_NAME | VARCHAR (400) | Stores a name for this questionnaire suitable for display to patient. |
| REPORT_ID | VARCHAR (18) | The ID of the report that displays when this questionnaire form is printed. |
| VB_FORM_ID | NUMERIC (18,0) | The ID of the VB form for this form record. |
| LISTED_YN | VARCHAR (1) |  |
| SOURCE_QUEST_ID | VARCHAR (18) | This item stores the LQL that was converted to create this LQF |
| FORM_CLASS_C | INTEGER |  |
| SOURCE_FORM | NUMERIC (18,0) | This item stores where the current form was copied from. |
| PG_FORM_LPG_ID | NUMERIC (18,0) | This item links a Print Group SmartForm to an actual LPG record. |
| QUESR_PRETEXT | VARCHAR (4000) | Holds the patient-entered questionnaire's pretext to display to patients. |
| QUESR_POSTTEXT | VARCHAR (1024) | Holds the patient-entered questionnaire's posttext to display to patients. |
| RECORD_STATE_C | INTEGER |  |
| SORT_ORDER_C | INTEGER |  |
| QUESR_ANS_VLD_DAYS | INTEGER | Stores the number of days the answers to this questionnaire will be considered valid. During this period of time after submission, duplicate questionnaires assigned from different contexts will look back to the valid answers. Note that this is not respected if the Responses are unique item is set to Yes. |
| THRD_PRTY_CNTNT_C | INTEGER |  |
| CAT_TYPE_C | INTEGER |  |
| QUESR_PRETXT_ETX_ID | VARCHAR (18) | Holds a SmartText record to be used as Questionnaire pre-text. |
| QUESR_POSTXT_ETX_ID | VARCHAR (18) | Holds a SmartText record to be used as Questionnaire post-text. |
| QUES_SCORING_C | INTEGER |  |
| CONV_FROM_HX_TEMPLATE_ID | VARCHAR (18) | Used to look up which LQH a given LQF was converted from, if any. |
| ALLOW_TKT_WO_ACCT_YN | VARCHAR (1) |  |
| OVERRIDE_STATUS_C | INTEGER |  |
| OVERRIDE_CONTEXT | VARCHAR (254) | Contains context for override. |
| ORIGINAL_FORM_ID | VARCHAR (18) | Contains original record for this override record. |
| PROM_CONCEPT_ID | 40 | Epic-released mapping concept to identify questionnaires used for the same Patient-Reported Outcome Measure across organizations. |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | FORM_ID | CL_QFORM1 | FORM_ID | Unknown | No | No |  |
| 1 | FORM_ID | DECISION_TREE_INFO | DTREE_ID | No | No | No |  |
| 1 | FORM_ID | QUESR_INSTRUCTIONS | FORM_ID | No | No | No |  |
| 4 | FORM_TYPE_C | ZC_FORM_TYPE | FORM_TYPE_C | No | No | No |  |
| 10 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 10 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 10 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 11 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 11 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 11 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 13 | REPORT_ID | REPORT_DETAILS | LRP_ID | No | No | No |  |
| 16 | SOURCE_QUEST_ID | CL_QQUEST | QUEST_ID | No | No | No |  |
| 17 | FORM_CLASS_C | ZC_FORM_CLASS | FORM_CLASS_C | No | No | No |  |
| 22 | RECORD_STATE_C | ZC_DEL_STATUS | DEL_STATUS_C | No | No | No |  |
| 22 | RECORD_STATE_C | ZC_EDG_REC_STAT | EDG_REC_STAT_C | No | No | No |  |
| 22 | RECORD_STATE_C | ZC_ERS_REC_STAT | RECORD_STATUS_C | No | No | No |  |
| 22 | RECORD_STATE_C | ZC_HCD_REC_STATE | HCD_REC_STATE_C | No | No | No |  |
| 22 | RECORD_STATE_C | ZC_HFL_RECORD_STAT | HFL_RECORD_STAT_C | No | No | No |  |
| 22 | RECORD_STATE_C | ZC_IMM_REC_STATUS | IMM_REC_STATUS_C | No | No | No |  |
| 22 | RECORD_STATE_C | ZC_LLB_STATUS | LLB_STATUS_C | No | No | No |  |
| 22 | RECORD_STATE_C | ZC_LMA_RECORD_STAT | LMA_RECORD_STAT_C | No | No | No |  |
| 22 | RECORD_STATE_C | ZC_MEM_REC_STATUS | MEM_REC_STATUS_C | No | No | No |  |
| 22 | RECORD_STATE_C | ZC_OR_REC_STATUS | OR_REC_STATUS_C | No | No | No |  |
| 22 | RECORD_STATE_C | ZC_PBA_REC_STAT | PBA_REC_STAT_C | No | No | No |  |
| 22 | RECORD_STATE_C | ZC_PROV_REC_STATE | PROV_REC_STATE_C | No | No | No |  |
| 22 | RECORD_STATE_C | ZC_RECORD_STATE_2 | RECORD_STATE_2_C | No | No | No |  |
| 22 | RECORD_STATE_C | ZC_RECORD_STATE_3 | RECORD_STATE_3_C | No | No | No |  |
| 22 | RECORD_STATE_C | ZC_RECORD_STATE_4 | RECORD_STATE_4_C | No | No | No |  |
| 22 | RECORD_STATE_C | ZC_RECORD_STATE_6 | RECORD_STATE_6_C | No | No | No |  |
| 22 | RECORD_STATE_C | ZC_RECORD_STATE_7 | RECORD_STATE_7_C | No | No | No |  |

_(48 total; showing first 30)_
