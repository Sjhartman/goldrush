# LINKED_CHARGEABLES

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=LINKED_CHARGEABLES

## Description

This table contains information about chargeable records linked to orderable or performable procedure records. An orderable or performable procedure record may be linked to one or more chargeable records to indicate the possible charges in which an order or performed service might result.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | EAP |
| Release Version | SPRING 2008 |
| May contain EHI? | No |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| PROC_ID | NUMERIC (18,0) | The unique ID of a procedure record in your system. This is referring to the internal ID, not the industry standard procedure code. |
| CONTACT_DATE_REAL | No | This is a numeric representation of the date of this encounter in your system. The integer portion of the number specifies the date of the encounter. The digits after the decimal point indicate multiple visits on one day. |
| LINE | No | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| CONTACT_DATE | DATETIME | The contact date for the procedure, in standard date format. |
| CM_CT_OWNER_ID | VARCHAR (25) | This is the deployment that owns this contact. |
| LINKED_CHRG_ID | NUMERIC (18,0) | This column shows the chargeable procedure record or records to which an orderable or performable procedure record may be linked. This indicates the possible charges in which an order or performed service might result. |
| CHRG_LINK_TYPE_C | INTEGER |  |
| CHARGE_TYPE_C | INTEGER |  |
| LNK_CHARGE_MODS | VARCHAR (192) | Modifiers for when this linked charge is used. |
| CHG_RULE_ID | VARCHAR (18) | Condition under which to include a charge. |
| CHG_OVRIDE_LPP_ID | NUMERIC (18,0) | Extension to override charge values for this linked charge. |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | PROC_ID | CLARITY_EAP | PROC_ID | No | No | No |  |
| 1 | PROC_ID | CLARITY_EAP_2 | PROC_ID | No | No | No |  |
| 1 | PROC_ID | CLARITY_EAP_3 | PROC_ID | No | No | No |  |
| 1 | PROC_ID | CLARITY_EAP_4 | PROC_ID | No | No | No |  |
| 1 | PROC_ID | CLARITY_EAP_5 | PROC_ID | No | No | No |  |
| 1 | PROC_ID | CLARITY_EAP_IMM | PROC_ID | Unknown | No | No |  |
| 1 | PROC_ID | CLARITY_EAP_OT | PROC_ID | Unknown | Unknown | Yes |  |
| 1 | PROC_ID | PROC_CONSENT_CONFIG | PROC_ID | No | No | No |  |
| 1 | PROC_ID | PROC_UM | PROC_ID | No | No | No |  |
| 1 | PROC_ID | V_CUBE_D_PROCEDURE | PROCEDURE_ID | Unknown | Unknown | No |  |
| 1 | PROC_ID | CLARITY_EAP_HIST | PROC_ID | Unknown | No | No |  |
| 2 | CONTACT_DATE_REAL | CONTACT_DATE_REAL |  |  |  |  |  |
| 1 | PROC_ID | CLARITY_EAP_OT | PROC_ID | No | No | No |  |
| 2 | CONTACT_DATE_REAL | CONTACT_DATE_REAL |  |  |  |  |  |
| 1 | PROC_ID | CL_EAP_AP_RVU_NMOD | PROC_ID | No | No | No |  |
| 2 | CONTACT_DATE_REAL | CONTACT_DATE_REAL |  |  |  |  |  |
| 1 | PROC_ID | EAP_DBC_CONTACT | PROC_ID | No | No | No |  |
| 2 | CONTACT_DATE_REAL | CONTACT_DATE_REAL |  |  |  |  |  |
| 5 | CM_CT_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 5 | CM_CT_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 5 | CM_CT_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 6 | LINKED_CHRG_ID | CLARITY_EAP | PROC_ID | No | No | No |  |
| 6 | LINKED_CHRG_ID | CLARITY_EAP_2 | PROC_ID | No | No | No |  |
| 6 | LINKED_CHRG_ID | CLARITY_EAP_3 | PROC_ID | No | No | No |  |
| 6 | LINKED_CHRG_ID | CLARITY_EAP_4 | PROC_ID | No | No | No |  |
| 6 | LINKED_CHRG_ID | CLARITY_EAP_5 | PROC_ID | No | No | No |  |
| 6 | LINKED_CHRG_ID | CLARITY_EAP_IMM | PROC_ID | Unknown | No | No |  |
| 6 | LINKED_CHRG_ID | CLARITY_EAP_OT | PROC_ID | Unknown | Unknown | Yes |  |
| 6 | LINKED_CHRG_ID | PROC_CONSENT_CONFIG | PROC_ID | No | No | No |  |
| 6 | LINKED_CHRG_ID | PROC_UM | PROC_ID | No | No | No |  |

_(36 total; showing first 30)_
