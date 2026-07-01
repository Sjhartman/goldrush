# OR_LOG_CHARGES

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=OR_LOG_CHARGES

## Description

This table contains the charge information for the surgical log (ORL) record.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | ORL |
| Release Version | SPRING 2008 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| LOG_ID | VARCHAR (18) | The unique ID of the log record. |
| LINE | No | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| CM_PHY_OWNER_ID | VARCHAR (25) | ID of the physical deployment owner for this record.  Physical owners will be where the data is hosted, either on the cross-over server or the owner deployment. |
| CM_LOG_OWNER_ID | VARCHAR (25) | ID of the logical deployment owner for this record.  Logical owners show the deployment where the record was created but doesn't represent if the record is a part of version skew. |
| UNIQUE_ID | VARCHAR (184) | This column stores the unique ID associated with the charge record. |
| CHARGE_SOURCE_C | VARCHAR (66) |  |
| UPDATE_ID | INTEGER | This column stores the update ID associated with the charge. |
| CHARGE_CANCELED_YN | VARCHAR (1) |  |
| PROCEDURE_CODE_ID | NUMERIC (18,0) | This column stores the charge code ID associated with the charge. |
| QUANTITY | INTEGER | This column stores the quantity associated with the charge. |
| AMOUNT | NUMERIC (18,2) | This column stores the charge amount associated with the charge. |
| PREVIOUS_LINE | INTEGER | This column stores the line number of the previous charge in this table associated with the charge. |
| SUPPLY_ID | VARCHAR (18) | This column stores the supply ID for which this charge was generated. |
| PICKLIST_TYPE_C | INTEGER |  |
| RESOURCE_ID | VARCHAR (18) | This column stores the staff/resource ID for which the charge was generated. |
| RESOURCE_TYPE_C | INTEGER |  |
| RESOURCE_SUB_TYPE | INTEGER | This column stores the sub type of the staff/resource for which this charge was generated. |
| COST | NUMERIC (18,2) | This column stores the cost associated with this line of charge. |
| CHARGE_IMPLANT_ID | VARCHAR (18) | This column stores the implant id for this line charge. |
| CANCEL_UPDATE_ID | INTEGER | This column stores the update id in which this charge was canceled |
| SURGICAL_PROC_ID | VARCHAR (254) | This column stores the surgical procedure assocaited with the charge. |
| CHRG_SVC_PROV_ID | VARCHAR (18) | This column stores the service provider for the charge. |
| CHRG_POS_ID | NUMERIC (18,0) | This column stores the place of service for the charge. |
| CHARGE_BILL_PROV_ID | VARCHAR (18) | This column stores the billing provider for the charge. |
| CHRG_REF_PROV_ID | VARCHAR (18) | This column stores the referring provider for the charge. |
| CHRG_ORM_ID | VARCHAR (18) | This column stores the ORM record ID which contains additional items for this  charge. |
| CHRG_SERVICE_DATE | DATETIME | This column stores the service date for the charge. |
| CHARGE_NAME | VARCHAR (254) | This column stores the name associated with the charge. |
| CHRG_SA_ID | NUMERIC (18,0) | This column stores the service area for the charge. |
| CHRG_REV_LOC_ID | NUMERIC (18,0) | This column stores the revenue location for the charge. |
| CHRG_DEP_ID | NUMERIC (18,0) | This column stores the department for the charge. |
| CHARGE_REFERRAL_ID | NUMERIC (18,0) | This column stores the referral ID for the surgery. |
| COST_CENTER_ID | NUMERIC (18,0) | This column stores the cost center for the charge. |
| EXT_CHRG_CODE | VARCHAR (40) | This column stores the external charge code. |
| CHARGE_PANEL | INTEGER | This column will store the panel number for the charge. |
| DBC_EPISODE_ID | NUMERIC (18,0) | This column stores the DBC Episode associated with the current charge. Used in the Dutch version. |
| CHRG_INV_LOC_ID | NUMERIC (18,0) | This item will store the inventory location for the charge |
| CHRG_REF_AMT | NUMERIC (18,2) | This item will store the reference amount of the inventory item. |
| CHRG_SUP_SWITCHED_YN | VARCHAR (1) |  |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| BITMAP INDEX | EIX_OR_LOG_CHARGES_OWNER1 | CM_PHY_OWNER_ID | 1 | No | Yes |  |
| BITMAP INDEX | EIX_OR_LOG_CHARGES_OWNER2 | CM_LOG_OWNER_ID | 1 | No | Yes |  |

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
| 3 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 4 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 4 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 4 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 6 | CHARGE_SOURCE_C | ZC_CHARGE_SOURCE | CHARGE_SOURCE_C | No | No | No |  |
| 9 | PROCEDURE_CODE_ID | CLARITY_EAP | PROC_ID | No | No | No |  |
| 9 | PROCEDURE_CODE_ID | CLARITY_EAP_2 | PROC_ID | No | No | No |  |
| 9 | PROCEDURE_CODE_ID | CLARITY_EAP_3 | PROC_ID | No | No | No |  |
| 9 | PROCEDURE_CODE_ID | CLARITY_EAP_4 | PROC_ID | No | No | No |  |
| 9 | PROCEDURE_CODE_ID | CLARITY_EAP_5 | PROC_ID | No | No | No |  |
| 9 | PROCEDURE_CODE_ID | CLARITY_EAP_IMM | PROC_ID | Unknown | No | No |  |

_(315 total; showing first 30)_
