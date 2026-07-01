# TRG_BLOCK_INFO

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=TRG_BLOCK_INFO

## Description

This table contains information about certain types of planned orders, including orders from treatment days in treatment plans and therapy plans, and orders from clinical pathways steps.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | TRG |
| Release Version | SPRING 2008 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| REGIMEN_ID | NUMERIC (18,0) | The treatment day ID. |
| CONTACT_DATE_REAL | No | This is a numeric representation of the date of this encounter in your system. The integer portion of the number specifies the date of the encounter. The digits after the decimal point indicate multiple visits on one day. |
| LINE | No | The line number that corresponds to each order block in the treatment day in this row. |
| CONTACT_DT | DATETIME | The contact date in external format of the treatment day in this row. |
| CM_CT_OWNER_ID | VARCHAR (25) | ID of the deployment owner for this contact. |
| BLOCK_ID | VARCHAR (100) | The ID of an order block in the treatment day in this row. In an IntraConnect environment this column contains the community ID (CID). |
| BLOCK_DAT | VARCHAR (50) | The contact date (DAT) of an order block in the treatment day in this row. |
| BLOCK_INI | VARCHAR (50) | The master file (INI) of an order block in the treatment day in this row. For example, "OTP". |
| BLOCK_DURATION | NUMERIC (18,0) | The duration of an order block in the treatment day in this row. |
| BLOCK_CAT_C | VARCHAR (66) |  |
| BLOCK_WAIT_AFTER | NUMERIC (18,0) | The number of days to wait after an order block in the treatment day in this row. |
| BLOCK_WAIT_FROM_C | INTEGER |  |
| BLOCK_MAX_LEAD | NUMERIC (18,0) | The max lead of an order block in the treatment day in this row. |
| BLOCK_MAX_LAG | NUMERIC (18,0) | The max lag of an order block in the treatment day in this row. |
| BLOCK_SOURCE | VARCHAR (254) | The source ID of an order block in the treatment day in this row. |
| BLOCK_OTP_ID | NUMERIC (18,0) | The unique ID of the order block (patient order template) in the treatment day in this record. |
| CHILD_DISPLAY_NAME | VARCHAR (254) | The display name of an order block in the treatment day in this record. |
| CHILD_SSC_ID | NUMERIC (18,0) | The unique ID of a non-order block in the treatment day in this record. |
| TMPL_SELECTED_YN | VARCHAR (1) |  |
| CHILD_RECOMMEND_YN | VARCHAR (1) |  |
| CHILD_REC_OVR_RSN_C | INTEGER |  |
| CHILD_RECOM_OVR_CMT | VARCHAR (254) | The comments for deselecting the recommended item |
| BLOCK_SRC_DAY_UID | VARCHAR (100) | Stores the unique ID of the day from which it was created. |
| SRC_AOG_ORDER_ID | NUMERIC (18,0) | If this order was added from an advanced order group (AOG), this item will hold the OTP ID of the AOG order  from which it was added. |
| ORDER_RANK | INTEGER | Stores the position of this order in the treatment day from the source protocol. If this order was added manually to the treatment plan after it was created, then this item will be empty. |
| CONVERSION_STATUS_C | INTEGER |  |
| CONVERSION_SRC_ID | NUMERIC (18,0) | For an order in a plan that is being converted for transition of treatment, this will be the ID of the actual order from the plan this is a duplicate of. While the plan is being converted the user will actually be editing this duplicate, until they are done, then the changes will be applied to the source order. |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | REGIMEN_ID | DENTAL_VISIT_INFO | REGIMEN_ID | No | No | No |  |
| 1 | REGIMEN_ID | TRG_INFO | REGIMEN_ID | Unknown | No | No |  |
| 1 | REGIMEN_ID | V_EHI_TRG_FILTER | REGIMEN_ID | Unknown | Unknown | No |  |
| 1 | REGIMEN_ID | TRG_UPDATE_INFO | REGIMEN_ID | Unknown | No | No |  |
| 2 | CONTACT_DATE_REAL | CONTACT_DATE_REAL |  |  |  |  |  |
| 5 | CM_CT_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 5 | CM_CT_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 5 | CM_CT_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 10 | BLOCK_CAT_C | ZC_REGIMEN_CAT | REGIMEN_CAT_C | No | No | No |  |
| 12 | BLOCK_WAIT_FROM_C | ZC_BLOCK_WAITFROM | BLOCK_WAITFROM_C | No | No | No |  |
| 16 | BLOCK_OTP_ID | ADT_PAT_ORDER_TEMPLATE | OTP_ID | No | No | No |  |
| 16 | BLOCK_OTP_ID | CL_OTP_FST_LST_SCH | OTP_ID | Unknown | No | No |  |
| 16 | BLOCK_OTP_ID | OTP_DOSE_PARAMS | OTP_ID | Unknown | No | No |  |
| 16 | BLOCK_OTP_ID | OTP_INFO | OTP_ID | Unknown | No | No |  |
| 16 | BLOCK_OTP_ID | OTP_INFO_1 | OTP_ID | Unknown | No | No |  |
| 16 | BLOCK_OTP_ID | OTP_INFO_2 | OTP_ID | Unknown | No | No |  |
| 16 | BLOCK_OTP_ID | OTP_INFO_3 | OTP_ID | Unknown | No | No |  |
| 16 | BLOCK_OTP_ID | OTP_INFO_4 | OTP_ID | Unknown | No | No |  |
| 16 | BLOCK_OTP_ID | OTP_INFO_5 | OTP_ID | No | No | No |  |
| 16 | BLOCK_OTP_ID | OTP_ROUTING | OTP_ID | Unknown | No | No |  |
| 18 | CHILD_SSC_ID | SSC_GEN_REC_INFO | RECORD_ID | No | No | No |  |
| 21 | CHILD_REC_OVR_RSN_C | ZC_CHILD_REC_OVR_R | CHILD_REC_OVR_R_C | No | No | No |  |
| 24 | SRC_AOG_ORDER_ID | ADT_PAT_ORDER_TEMPLATE | OTP_ID | No | No | No |  |
| 24 | SRC_AOG_ORDER_ID | CL_OTP_FST_LST_SCH | OTP_ID | Unknown | No | No |  |
| 24 | SRC_AOG_ORDER_ID | OTP_DOSE_PARAMS | OTP_ID | Unknown | No | No |  |
| 24 | SRC_AOG_ORDER_ID | OTP_INFO | OTP_ID | Unknown | No | No |  |
| 24 | SRC_AOG_ORDER_ID | OTP_INFO_1 | OTP_ID | Unknown | No | No |  |
| 24 | SRC_AOG_ORDER_ID | OTP_INFO_2 | OTP_ID | Unknown | No | No |  |
| 24 | SRC_AOG_ORDER_ID | OTP_INFO_3 | OTP_ID | Unknown | No | No |  |
| 24 | SRC_AOG_ORDER_ID | OTP_INFO_4 | OTP_ID | Unknown | No | No |  |

_(43 total; showing first 30)_
