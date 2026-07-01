# CLARITY_IMMUNZATN

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=CLARITY_IMMUNZATN

## Description

The CLARITY_IMMUNZATN table contains high-level information about the immunizations providers can choose on the Immunization Administration window. These records should not be confused with the actual immunization procedures.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | FULL |
| Load Frequency | WEEKLY - FULL |
| Chronicles INI | LIM |
| Release Version | EPIC 2000 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| IMMUNZATN_ID | NUMERIC (18,0) | The unique ID of the immunization record. |
| NAME | VARCHAR (200) | The name of the immunization. |
| ABBREVIATION | VARCHAR (200) | An abbreviation to use for this immunization. |
| RECORD_STATUS | VARCHAR (10) |  |
| IMMUN_TYPE | INTEGER |  |
| CM_PHY_OWNER_ID | VARCHAR (25) | ID of the physical deployment owner for this record.  Physical owners will be where the data is hosted, either on the cross-over server or the owner deployment. |
| CM_LOG_OWNER_ID | VARCHAR (25) | ID of the logical deployment owner for this record.  Logical owners show the deployment where the record was created but doesn't represent if the record is a part of version skew. |
| NAME_MIXED_CASE | VARCHAR (200) | Item holds the immunization name in mixed case. A case of the various characters is an integral part of the name. |
| IMM_DOSE | VARCHAR (50) | The default dose for the immunization. Free text field. |
| ROUTE_C | INTEGER |  |
| SITE_C | INTEGER |  |
| MANUFACTURER_C | INTEGER |  |
| VIS_DATE | VARCHAR (254) | Default VIS date for the given immunization. |
| PRIMARY_FAMILY_ID | NUMERIC (18,0) | Primary family that the given immunization belongs to. |
| MED_ADMIN_TYPE_C | INTEGER |  |
| ACTIVE_STATUS_C | INTEGER |  |
| IMM_GROUP_C | VARCHAR (66) |  |
| BILLING_PROC_ID | NUMERIC (18,0) | The billing procedure that should be used when administering the immunization. If you want the immunization to drop the charge without depending on the order, please fill in this item. |
| ESIG_TEMPLATE_FILE | VARCHAR (254) | E-Sig template file. Gives the path to check for the file. |
| IMM_CVX_CODE | VARCHAR (254) | CVX code for the given immunization. This item is used by the interfaces. |
| SENS_IMMNZTN_YN | VARCHAR (1) |  |
| RECORD_STATUS_C | INTEGER |  |
| CVX_CODE | VARCHAR (30) | This contains the immunization's CVX code used by Ambulatory, as returned by getImmCode^LIMMLOAD. It is intended for CVX lookup in Clarity (say, for Caboodle). |
| MYC_DISPLAY_NAME | VARCHAR (254) | The patient-friendly name for the immunization. |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 5 | IMMUN_TYPE | ZC_IMM_TYPE | IMM_TYPE_C | No | No | No |  |
| 6 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 6 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 6 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 7 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 7 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 7 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 10 | ROUTE_C | ZC_ROUTE | ROUTE_C | No | No | No |  |
| 11 | SITE_C | ZC_SITE | SITE_C | No | No | No |  |
| 12 | MANUFACTURER_C | ZC_MFG | MFG_C | No | No | No |  |
| 14 | PRIMARY_FAMILY_ID | CLARITY_IMMUNZATN | IMMUNZATN_ID | Unknown | No | No |  |
| 15 | MED_ADMIN_TYPE_C | ZC_MED_ADMIN_TYPE | MED_ADMIN_TYPE_C | No | No | No |  |
| 16 | ACTIVE_STATUS_C | ZC_CNT_METRIC_EVNT | CNT_METRIC_EVNT_C | No | No | No |  |
| 16 | ACTIVE_STATUS_C | ZC_CONVERTED | CONVERTED_C | No | No | No |  |
| 16 | ACTIVE_STATUS_C | ZC_DATA_INDEXED | DATA_INDEXED_C | No | No | No |  |
| 16 | ACTIVE_STATUS_C | ZC_OP_MIXED_DEFAUL | OP_MIXED_DEFAUL_C | No | No | No |  |
| 16 | ACTIVE_STATUS_C | ZC_YES_NO | YES_NO_C | No | No | No |  |
| 17 | IMM_GROUP_C | ZC_IMM_GROUP | IMM_GROUP_C | No | No | No |  |
| 18 | BILLING_PROC_ID | CLARITY_EAP | PROC_ID | No | No | No |  |
| 18 | BILLING_PROC_ID | CLARITY_EAP_2 | PROC_ID | No | No | No |  |
| 18 | BILLING_PROC_ID | CLARITY_EAP_3 | PROC_ID | No | No | No |  |
| 18 | BILLING_PROC_ID | CLARITY_EAP_4 | PROC_ID | No | No | No |  |
| 18 | BILLING_PROC_ID | CLARITY_EAP_5 | PROC_ID | No | No | No |  |
| 18 | BILLING_PROC_ID | CLARITY_EAP_IMM | PROC_ID | Unknown | No | No |  |
| 18 | BILLING_PROC_ID | PROC_CONSENT_CONFIG | PROC_ID | No | No | No |  |
| 18 | BILLING_PROC_ID | PROC_UM | PROC_ID | No | No | No |  |
| 18 | BILLING_PROC_ID | V_CUBE_D_PROCEDURE | PROCEDURE_ID | Unknown | Unknown | No |  |
| 22 | RECORD_STATUS_C | ZC_DEL_STATUS | DEL_STATUS_C | No | No | No |  |
| 22 | RECORD_STATUS_C | ZC_EDG_REC_STAT | EDG_REC_STAT_C | No | No | No |  |
| 22 | RECORD_STATUS_C | ZC_ERS_REC_STAT | RECORD_STATUS_C | No | No | No |  |

_(49 total; showing first 30)_
