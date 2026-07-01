# ORDER_STATUS

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=ORDER_STATUS

## Description

The ORDER_STATUS table contains overtime single response orders information.

**Primary table** in this group (100 cols). Overflow siblings joined on shared key: ORDER_STATUS_2 (7 cols). Prefer this table for most queries.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | ORD |
| Release Version | MU2 - EPIC 2002 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| ORDER_ID | NUMERIC (18,0) | Unique ID for this order record |
| ORD_DATE_REAL | No | This is a numeric representation of the date of this encounter in your system. The integer portion of the number specifies the date of the encounter. The digits after the decimal point indicate multiple visits on one day. |
| CONTACT_DATE | DATETIME | The date of this contact in calendar format. |
| CONTACT_NUMBER | INTEGER | The contact number of the orders record. |
| CONTACT_TYPE_C | INTEGER |  |
| ABNORMAL_YN | VARCHAR (1) |  |
| ORDER_CREATOR_ID | VARCHAR (18) | The unique ID of the person creating the order. |
| RESULTING_PROV | VARCHAR (255) | The name of the provider signing off on the results. |
| LAB_TECHNICIAN | VARCHAR (255) | The technician responsible for the order tests. |
| RESULTING_LAB_ID | NUMERIC (18,0) | The unique ID of the lab running the test. |
| MED_HX_OLD_VALUE *(deprecated)* | VARCHAR (255) | *** Deprecated *** In table ORDER_STATUS, the column MED_HX_OLD_VALUE (ORD 7180) has been deprecated.  The deprecated column's content/data is no longer available since it is no longer populated in Chronicles.  Medication history - old value. |
| CONTACT_COMMENT | VARCHAR (255) | Comment associated with this contact. |
| INSTANT_OF_ENTRY | DATETIME (Local) | The instant the record was last entered. |
| INSTANT_OF_EDIT | DATETIME | The instant the record was last edited. |
| ITEMS_EDITED | VARCHAR (1024) | The items that were edited with this contact. |
| DATA_ENTRY_PERSON | VARCHAR (50) | The user who created/edited this contact. |
| RX_DISPENSE_CODE_C | INTEGER |  |
| RX_CART_GROUP_C *(deprecated)* | INTEGER |  |
| RX_PAR_DOSES | INTEGER | PRN par level number of doses |
| CM_CT_OWNER_ID | VARCHAR (25) | ID of the deployment owner for this contact. |
| CSN_FOR_ADD_REFILL | NUMERIC (18,0) | This item only applies to refill orders. It stores the contact serial numbers of the patient visits where the refill order was modified. |
| SCHEDULED_DATE | DATETIME | The date a standard ambulatory order is scheduled for. |
| SCHEDULED_TIME | DATETIME (Local) | The time a standard ambulatory order is scheduled for. |
| PROCEDURE_NOTE_ID | VARCHAR (254) | This column contains the unique notes record identifier of the note that resulted the narrative for the order. |
| PROCEDURE_NOTE_DT | DATETIME | This is the date for the procedure note that resulted the order. |
| ERFLL_REQ_RFL_PRN_C | INTEGER |  |
| ERFLL_APP_RFL_PRN_C | INTEGER |  |
| EREFILL_TO_PHM_ID | VARCHAR (254) | Stores the link to the general use notes record containing the action message to the pharmacy. |
| WET_READS_C | INTEGER |  |
| ROUTING_OUTCOME_C | INTEGER |  |
| ROUTING_RULE_ID | NUMERIC (18,0) | The unique ID of the results routing rule that was used to determine recipients for this result. |
| ROUTING_RULE_LEVEL | VARCHAR (50) | The level at which the results routing rule used to determine recipients was specified. The possible levels are: Auth Prov, Auth Prov Primary Dept, Enc Dept, or System |
| ROUTING_SCHEME_ID | NUMERIC (18,0) | The unique ID of the results routing scheme that was used to determine recipients for this result. |
| ROUTING_SCHEME_LINE | VARCHAR (40) | The line of the results routing scheme that was executed to determine recipients for this result. If no line was executed, the value of the column will be the string "DEFAULT". |
| ROUTING_INST_TM | DATETIME (Local) | The date and time the order was resulted and routed. |
| ROUTING_USER_ID | VARCHAR (18) | The unique ID of the user the result was routed to for this row. |
| RIS_LET_TEMPLT_ID | VARCHAR (18) | The unique ID of the SmartText record for a mammography result letter associated with this order. |
| ROUTING_CURSTATUS_C | INTEGER |  |
| PROC_NOTE_DATE_REAL | FLOAT | A unique, internal contact date of the associated note record in decimal format. The integer portion of the number indicates the date of the note record contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. Along with PROCEDURE_NOTE_ID, this forms the foreign key to overtime note tables (e.g. HNO_NOTE_TEXT). |
| MAM_5_YEAR_RISK | NUMERIC (6,2) | Patient's probability of getting breast cancer in the next 5 years.  Calculated using external formula. |
| MAM_LIFETIME_RISK | NUMERIC (6,2) | Patient's probability of getting breast cancer in a lifetime. Calculated using external formula. |
| LAB_STATUS_C | INTEGER |  |
| OVRL_BREAST_DENS_C | INTEGER |  |
| RIGHT_BREAST_DENS_C | INTEGER |  |
| LEFT_BREAST_DENS_C | INTEGER |  |
| MOST_SIG_MAM_FIND_C | INTEGER |  |
| IMG_DOUBLE_READ_C | INTEGER |  |
| CAD_USAGE_C | INTEGER |  |
| LAB_PATHOLOGIST_ID | VARCHAR (18) | The unique user ID of the pathologist that has responsibility for the current Anatomic Pathology order. |
| RSLT_CNCT_INSTANT_DTTM | DATETIME (UTC) | The instant in which a result contact is modified/filed to the system. Not to be confused with Result Date/Time, which is when the result was actually generated. |
| RSLT_CNCT_USER_ID | VARCHAR (18) | The user filing the result contact. For interfaces or Beaker Result Filing background job, this might be a generic user. |
| RSLT_CNCT_SOURCE_C | INTEGER |  |
| IPROC_NOTE_ID | VARCHAR (254) | Stores the ID to the general use notes record of the Imaging and Procedures Resulting Note. |
| IPROC_NOTE_CSN | NUMERIC (18,0) | Stores the contact serial number to the general use notes record of the Imaging and Procedures Resulting Note. |
| RES_INTERPRETER_ID | VARCHAR (18) | The unique ID of the user who is the interpreter of the results for this order. |
| RX_DSP_CPY_FROM_ID | NUMERIC (18,0) | This item contains the order ID from which a dispense was copied. |
| RX_DSP_CPY_FROM_DTE_REAL | FLOAT | This item contains the order DAT from which a dispense was copied. |
| RESPONS_AP_USER_ID | VARCHAR (18) | The unique ID of the lab user that has responsibility for the current anatomic pathology order. |
| OVRL_TISSUE_COMP_C | INTEGER |  |
| RIGHT_TISSUE_COMP_C | INTEGER |  |
| LEFT_TISSUE_COMP_C | INTEGER |  |
| OVRL_FGT_C | INTEGER |  |
| RIGHT_FGT_C | INTEGER |  |
| LEFT_FGT_C | INTEGER |  |
| OVRL_BPE_C | INTEGER |  |
| RIGHT_BPE_C | INTEGER |  |
| LEFT_BPE_C | INTEGER |  |
| SYMMETRIC_BPE_C | INTEGER |  |
| READACK_BY_WHEN_UTC_DTTM | DATETIME (UTC) | This item stores when the result needs to be acted on by a user |
| LAB_CORR_TYPE_C | INTEGER |  |
| RESULT_DTTM | 26 | The date and time the technician ran the tests for each order in calendar format. NOTE: Concatenates the result date (ORD 26) and result time (ORD 28) into a datetime format. If the time value is null, the query will return 12:00 AM for a time. |
| LEFT_OVARY_SMALL_FOLLICLE_CNT | INTEGER | The number of follicles in the left ovary at or below the minimum threshold as defined in system definitions (I LSD 53002). |
| RIGHT_OVARY_SMALL_FOLLICLE_CNT | INTEGER | The number of follicles in the right ovary at or below the minimum threshold as defined in system definitions (I LSD 53002). |
| ENDOMETRIAL_STRIPE | NUMERIC (18,1) | The measurement of the endometrial stripe. |
| OV_CYST_PRESENCE_C | INTEGER |  |
| UTERINE_FIBROID_PRESENCE_C | INTEGER |  |
| UTERINE_POLYP_PRESENCE_C | INTEGER |  |
| REPORTABLE_LAB_RESULT_YN | VARCHAR (1) |  |
| NARRATIVE_PERF_ORG_INFO | INTEGER | This item stores the line number of the performing organization related group (ORD 1220) and acts as a pointer to the performing organization information of narrative of the result. |
| IMPRESSION_PERF_ORG_INFO | INTEGER | This item stores the line number of the preforming organization related group (ORD 1220) and acts as a pointer to the performing organization information of impression of the result. |
| WET_READS_SHARED_C | INTEGER |  |
| MSG_EXT_SYS_WHEN_RSLT_ACK_YN | VARCHAR (1) |  |
| EXT_DISP_FILL_IDENT | VARCHAR (184) | Holds the unique identifier for a given fill used to identify the external dispense |
| ORD_PROC_LABEL | VARCHAR (254) | This item stores additional information from MedCom interfaces for Results Review display. Required for MedCom certification in Denmark. |
| SR_VALID_STATUS_C | INTEGER |  |
| IMPR_SEPARATOR | VARCHAR (508) | Stores the impression separator for imaging result reports. |
| LAB_PDF_GEN_DCSN_C | INTEGER |  |
| RESULT_PERF_ORG | INTEGER | This item stores the line number of related group 1220 and acts as a pointer to the performing organization information of the result. |
| LAB_RESULTING_METHOD | VARCHAR (254) | The main resulting method (either manual or a specific interface) that was used to result the order |
| NLP_RESULT_ACTION_C | INTEGER |  |
| ROUTING_MOPS_ORDER_ID | NUMERIC (18,0) | The ID of the MOPS grouper order this order was routed with. |
| ROUTING_MOPS_ORDER_DAT | INTEGER | The DAT of the MOPS grouper order this order was routed with. |
| NLP_UNVERIFIED_IB_ONLY_YN | VARCHAR (1) |  |
| LAB_PLAIN_TEXT_GEN_DCS_C | INTEGER |  |
| OVRL_AVG_VOL_BREAST_DENS | NUMERIC (6,3) | Overall average volumetric breast density. Stored as a percentage. |
| RIGHT_VOL_BREAST_DENS | NUMERIC (6,3) | Right volumetric breast density. Stored as a percentage. |
| LEFT_VOL_BREAST_DENS | NUMERIC (6,3) | Left Volumetric Breast Density. Stored as a percentage. |
| BREAST_DENS_ALG | VARCHAR (254) | The algorithm used to determine breast composition and volumetric breast density |
| BREAST_DENS_ALG_VER | VARCHAR (254) | The algorithm version used to determine breast composition and volumetric breast density |
| OVRL_VOL_ASSOC_BREAST_DENS_C | INTEGER |  |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| B-TREE INDEX | EIX_ORDER_STATUS_LAB_PATH | LAB_PATHOLOGIST_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_ORDER_STATUS_PROC_NOTE_ID | PROCEDURE_NOTE_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_ORDER_STATUS_RX_CPY_ID_DTE | RX_DSP_CPY_FROM_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_ORDER_STATUS_RX_CPY_ID_DTE | RX_DSP_CPY_FROM_DTE_REAL | 2 | Yes | No |  |

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

_(426 total; showing first 30)_
