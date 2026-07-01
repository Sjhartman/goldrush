# ALLERGY_REACTIONS

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=ALLERGY_REACTIONS

## Description

The ALLERGY_REACTIONS table contains the category values of the reactions associated with a given allergy. There may be multiple reactions associated with a single allergy. In this case, there will be multiple records in this table with the same ALLERGY_ID, but with different LINE values.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | LPL |
| Release Version | MU6 - EPIC 2002 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| ALLERGY_ID | NUMERIC (18,0) | The unique ID used to identify the allergy record. |
| LINE | INTEGER | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| REACTION_C | INTEGER |  |
| UPDATE_DATE | No | *** Deprecated *** This column is not reliably populated, row update tracking should be used instead. ****** The extract date and time of the record for this table. |
| CM_PHY_OWNER_ID | VARCHAR (25) | ID of the physical deployment owner for this record.  Physical owners will be where the data is hosted, either on the cross-over server or the owner deployment. |
| CM_LOG_OWNER_ID | VARCHAR (25) | ID of the logical deployment owner for this record.  Logical owners show the deployment where the record was created but doesn't represent if the record is a part of version skew. |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| B-TREE INDEX | EIX_ALLERGY_REACTION_REACT_C | REACTION_C | 1 | Yes | Yes |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ALLERGY_ID | ADVERSE_EVENT_INFO | ADVERSE_EVENT_ID | No | No | No |  |
| 1 | ALLERGY_ID | ALLERGY | ALLERGY_ID | Unknown | No | No |  |
| 1 | ALLERGY_ID | COMPLICATIONS | PROBLEM_LIST_ID | No | No | No |  |
| 1 | ALLERGY_ID | HH_PBLST_INFO | PROBLEM_LIST_ID | Unknown | No | No |  |
| 1 | ALLERGY_ID | IMMUNE | IMMUNE_ID | Unknown | No | No |  |
| 1 | ALLERGY_ID | PL_SYSTEMS | PROBLEM_LIST_ID | Unknown | No | No |  |
| 1 | ALLERGY_ID | PROBLEM_LIST | PROBLEM_LIST_ID | Unknown | No | No |  |
| 1 | ALLERGY_ID | PROBLEM_LIST_ALL | PROBLEM_LIST_ID | No | No | No |  |
| 1 | ALLERGY_ID | PROB_TXP_MODIFIERS | PROBLEM_LIST_ID | Unknown | No | No |  |
| 1 | ALLERGY_ID | V_IMMUNIZATION_ADMINS | IMMUNE_ID | Unknown | Unknown | No |  |
| 3 | REACTION_C | ZC_REACTION | REACTION_C | No | No | No |  |
| 5 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 5 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 5 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 6 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 6 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 6 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
