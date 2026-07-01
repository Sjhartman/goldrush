# CLARITY_EAP_OT

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=CLARITY_EAP_OT

## Description

The CLARITY_EAP_OT table contains over time information from the procedure master file.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | EAP |
| Release Version | EPIC 2002 |
| May contain EHI? | No |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| PROC_ID | NUMERIC (18,0) | The unique ID of each procedure record in your system. This is referring to the internal ID, not the industry standard procedure code. |
| CONTACT_DATE_REAL | No | A unique, internal contact date in decimal format. The integer portion of the number indicates the date of the contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| CONTACT_DATE | DATETIME | The contact date for the procedure, in standard date format. |
| CONTACT_TYPE_C | INTEGER |  |
| CONTACT_COMMENT | VARCHAR (255) | The contact comment of the EAP record. |
| RVU_WORK_COMPON | NUMERIC (12,2) | The relative value units work component for this procedure (with no modifier applying). |
| RVU_OVERHD_COMPON | NUMERIC (12,2) | The relative value units overhead component for this procedure (with no modifier applying). |
| RVU_MALPRAC_COMPON | NUMERIC (12,2) | The relative value units malpractice component for this procedure (with no modifier applying). |
| RVU_TOTAL_NO_MOD | NUMERIC (12,2) | The total relative value unit (no modifier). |
| RVU_ALT | NUMERIC (12,2) | The alternate RVU for this procedure. This is date sensitive and will be used relative to the service date of charges entered. |
| RVU_BASE_UNITS_NM | NUMERIC (12,2) | The base unit's component value for the combination of procedure and no modifiers. |
| RVU_ADDL_UNITS_NM | NUMERIC (12,2) | The additional unit's component value for the combination of procedure and no modifiers. |
| RVU_TOTAL_UNITS_NM | NUMERIC (12,2) | The total unit's component value for the combination of procedure and no modifiers. |
| UNIT_PRICE | NUMERIC (12,2) | The unit charge for this procedure. This price is date sensitive and will be used relative to the service date of charges entered into the system. |
| CPT_CODE | VARCHAR (20) | The CPT? Code associated with the ordered procedure. |
| CODE_TYPE_C | INTEGER |  |
| SHOW_HCPCS_YN | VARCHAR (1) |  |
| LMRP_CODE | VARCHAR (50) | The LCD code used for LCD edits. |
| IS_ORD_SPC_QUS_YN | VARCHAR (1) |  |
| END_CONT_DATE_REAL | No | In table CLARITY_EAP_OT, the column END_CONT_DATE_REAL has been deprecated.  This column has been replaced by column END_CONT_DATE_REAL in table CLARITY_EAP_2.  This column stores the most recent contact date in internal, decimal format.  To look up the deprecated column's value after the Clarity Compass upgrade, join column CLARITY_EAP_OT.PROC_ID to table CLARITY_EAP_2 column PROC_ID to get the END_CONT_DATE_REAL value. |
| CM_PHY_OWNER_ID | VARCHAR (25) | ID of the physical deployment owner for this record.  Physical owners will be where the data is hosted, either on the cross-over server or the owner deployment. |
| CM_LOG_OWNER_ID | VARCHAR (25) | ID of the logical deployment owner for this record.  Logical owners show the deployment where the record was created but doesn't represent if the record is a part of version skew. |
| NAME_HISTORY | VARCHAR (254) | Stores the procedure name over time. |
| ORDERABLE_YN | VARCHAR (1) |  |
| PERFORMABLE_YN | VARCHAR (1) |  |
| CHARGEABLE_YN | VARCHAR (1) |  |
| HISTORICAL_YN | VARCHAR (1) |  |
| BASE_DOSAGE | NUMERIC (18,2) | Base dosage for charge procedures. |
| DOSAGE_UNIT_C | INTEGER |  |
| BASE_CHARGE | VARCHAR (254) | Estimated price for an Advanced Beneficiary Notice. |
| RVU_OVERHEAD_FAC | NUMERIC (18,2) | The RVU overhead (or practice expense) component for this procedure. |
| RVU_TTL_NO_MOD_FAC | NUMERIC (18,2) | The total facility RVU (or practice expense) component for this procedure with no modifier applying. |
| RVU_PER_UNIT | NUMERIC (4,2) | The Relative Value Units to credit the provider for each Unit of this procedure charged. |
| PRICE_PER_RVU | NUMERIC (15,2) | The procedure price that is equivalent to 1 RVU. |
| BASE_RVU | INTEGER | The Base RVUs to credit the performing provider with. |
| IP_QUES_OVRD_YN | VARCHAR (1) |  |
| CONTACT_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this contact. This is only populated if you use IntraConnect. |
| IS_TAXABLE_CHARGE_YN | VARCHAR (1) |  |
| TAX_CLASS_C | INTEGER |  |
| SELF_PAY_PROC_YN | VARCHAR (1) |  |
| DECISION_SERVICE_YN | VARCHAR (1) |  |
| RECURRING_BILLING_SERVICE_YN | VARCHAR (1) |  |
| ALT_FNT_CHARGE_PROC_ID | NUMERIC (18,0) | An alternate chargeable procedure that can be used, for example, for daily charging, or whenever the primary chargeable is not applicable. This is only used for procedures used as a chargeable for a decision service procedure. |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | PROC_ID | CLARITY_EAP | PROC_ID | No | No | No |  |
| 1 | PROC_ID | CLARITY_EAP_2 | PROC_ID | No | No | No |  |
| 1 | PROC_ID | CLARITY_EAP_3 | PROC_ID | No | No | No |  |
| 1 | PROC_ID | CLARITY_EAP_4 | PROC_ID | No | No | No |  |
| 1 | PROC_ID | CLARITY_EAP_5 | PROC_ID | No | No | No |  |
| 1 | PROC_ID | CLARITY_EAP_IMM | PROC_ID | Unknown | No | No |  |
| 1 | PROC_ID | PROC_CONSENT_CONFIG | PROC_ID | No | No | No |  |
| 1 | PROC_ID | PROC_UM | PROC_ID | No | No | No |  |
| 1 | PROC_ID | V_CUBE_D_PROCEDURE | PROCEDURE_ID | Unknown | Unknown | No |  |
| 4 | CONTACT_TYPE_C | ZC_EAP_CONT_TYPE | CONTACT_TYPE_C | No | No | No |  |
| 16 | CODE_TYPE_C | ZC_CODE_TYPE | CODE_TYPE_C | No | No | No |  |
| 21 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 21 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 21 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 22 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 22 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 22 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 29 | DOSAGE_UNIT_C | ZC_MED_UNIT | DISP_QTYUNIT_C | No | No | No |  |
| 37 | CONTACT_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 37 | CONTACT_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 37 | CONTACT_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 39 | TAX_CLASS_C | ZC_TAX_CLASSES | CLASS_C | No | No | No |  |
| 43 | ALT_FNT_CHARGE_PROC_ID | CLARITY_EAP | PROC_ID | No | No | No |  |
| 43 | ALT_FNT_CHARGE_PROC_ID | CLARITY_EAP_2 | PROC_ID | No | No | No |  |
| 43 | ALT_FNT_CHARGE_PROC_ID | CLARITY_EAP_3 | PROC_ID | No | No | No |  |
| 43 | ALT_FNT_CHARGE_PROC_ID | CLARITY_EAP_4 | PROC_ID | No | No | No |  |
| 43 | ALT_FNT_CHARGE_PROC_ID | CLARITY_EAP_5 | PROC_ID | No | No | No |  |
| 43 | ALT_FNT_CHARGE_PROC_ID | CLARITY_EAP_IMM | PROC_ID | Unknown | No | No |  |
| 43 | ALT_FNT_CHARGE_PROC_ID | PROC_CONSENT_CONFIG | PROC_ID | No | No | No |  |
| 43 | ALT_FNT_CHARGE_PROC_ID | PROC_UM | PROC_ID | No | No | No |  |

_(31 total; showing first 30)_
