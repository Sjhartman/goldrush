# CLARITY_LLB

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=CLARITY_LLB

## Description

Interface laboratory general information.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | FULL |
| Load Frequency | WEEKLY - FULL |
| Chronicles INI | LLB |
| Release Version | SPRING 2006 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| RESULTING_LAB_ID | NUMERIC (18,0) | The unique ID of the interface laboratory record. |
| LLB_NAME | VARCHAR (254) | Interface laboratory name. |
| LLB_ABBR | VARCHAR (254) | Interface laboratory name abbreviated. |
| LLB_STATUS_C | INTEGER |  |
| LLB_ADDR_LN1 | VARCHAR (254) | Interface laboratory address line 1. |
| LLB_ADDR_LN2 | VARCHAR (254) | Interface laboratory address line 2. |
| LLB_CITY | VARCHAR (254) | Interface laboratory address city. |
| LLB_STATE_C | VARCHAR (66) |  |
| LLB_ZIP | VARCHAR (254) | Interface laboratory address zip code. |
| LLB_BILL_DEPT_ID | NUMERIC (18,0) | Interface laboratory billing department. |
| LLB_CONTACT | VARCHAR (254) | Interface laboratory contact name. |
| LLB_CONTACT_PH | VARCHAR (254) | Interface laboratory contact phone number. |
| LLB_CONTACT_FAX | VARCHAR (254) | Interface laboratory contact fax number. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this Chronicles record. This is populated only if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this Chronicles record was extracted. This is populated only if you use IntraConnect. |
| LLB_DIRECTOR | VARCHAR (254) | Interface laboratory director name. |
| LLB_DFLT_RES_PROV | VARCHAR (254) | Interface laboratory default result provider name. |
| LLB_ORDER_CLASS_C | INTEGER |  |
| HOUSE_NUM | VARCHAR (254) | Stores the house number of the laboratory. |
| DISTRICT_C | INTEGER |  |
| COUNTY_C | VARCHAR (66) |  |
| COUNTRY_C | VARCHAR (66) |  |
| LLB_INT_ROUTE_CODE | VARCHAR (254) | Stores the internal routing code that the lab interface should use for this lab. |
| LLB_EXT_ROUTE_CODE | VARCHAR (254) | Stores the external routing code that the lab interface should use for this  lab. |
| DIS_CHRG_TRIGGER_YN | VARCHAR (1) |  |
| LLB_DIR_SER_ID | VARCHAR (18) | The Medical Lab Director of the lab. This is the discrete version, which is linked to the Provider (SER) master file. |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 4 | LLB_STATUS_C | ZC_DEL_STATUS | DEL_STATUS_C | No | No | No |  |
| 4 | LLB_STATUS_C | ZC_EDG_REC_STAT | EDG_REC_STAT_C | No | No | No |  |
| 4 | LLB_STATUS_C | ZC_ERS_REC_STAT | RECORD_STATUS_C | No | No | No |  |
| 4 | LLB_STATUS_C | ZC_HCD_REC_STATE | HCD_REC_STATE_C | No | No | No |  |
| 4 | LLB_STATUS_C | ZC_HFL_RECORD_STAT | HFL_RECORD_STAT_C | No | No | No |  |
| 4 | LLB_STATUS_C | ZC_IMM_REC_STATUS | IMM_REC_STATUS_C | No | No | No |  |
| 4 | LLB_STATUS_C | ZC_LLB_STATUS | LLB_STATUS_C | No | No | No |  |
| 4 | LLB_STATUS_C | ZC_LMA_RECORD_STAT | LMA_RECORD_STAT_C | No | No | No |  |
| 4 | LLB_STATUS_C | ZC_MEM_REC_STATUS | MEM_REC_STATUS_C | No | No | No |  |
| 4 | LLB_STATUS_C | ZC_OR_REC_STATUS | OR_REC_STATUS_C | No | No | No |  |
| 4 | LLB_STATUS_C | ZC_PBA_REC_STAT | PBA_REC_STAT_C | No | No | No |  |
| 4 | LLB_STATUS_C | ZC_PROV_REC_STATE | PROV_REC_STATE_C | No | No | No |  |
| 4 | LLB_STATUS_C | ZC_RECORD_STATE_2 | RECORD_STATE_2_C | No | No | No |  |
| 4 | LLB_STATUS_C | ZC_RECORD_STATE_3 | RECORD_STATE_3_C | No | No | No |  |
| 4 | LLB_STATUS_C | ZC_RECORD_STATE_4 | RECORD_STATE_4_C | No | No | No |  |
| 4 | LLB_STATUS_C | ZC_RECORD_STATE_6 | RECORD_STATE_6_C | No | No | No |  |
| 4 | LLB_STATUS_C | ZC_RECORD_STATE_7 | RECORD_STATE_7_C | No | No | No |  |
| 4 | LLB_STATUS_C | ZC_RECORD_STAT_EPM | RECORD_STAT_EPM_C | No | No | No |  |
| 4 | LLB_STATUS_C | ZC_RECORD_STAT_EPP | RECORD_STAT_EPP_C | No | No | No |  |
| 4 | LLB_STATUS_C | ZC_RECORD_STAT_ETX | RECORD_STAT_ETX_C | No | No | No |  |
| 4 | LLB_STATUS_C | ZC_RECORD_STAT_HRV | RECORD_STAT_HRV_C | No | No | No |  |
| 4 | LLB_STATUS_C | ZC_RECORD_STAT_RMC | RECORD_STAT_RMC_C | No | No | No |  |
| 8 | LLB_STATE_C | ZC_ALT_INVOICE_STA | ALT_INVOICE_STA_C | No | No | No |  |
| 8 | LLB_STATE_C | ZC_LLB_STATE | LLB_STATE_C | No | No | No |  |
| 8 | LLB_STATE_C | ZC_REFG_PROV_STATE | REFG_PROV_STATE_C | No | No | No |  |
| 8 | LLB_STATE_C | ZC_STATE | STATE_C | No | No | No |  |
| 8 | LLB_STATE_C | ZC_STATE_HISTORY | STATE_HISTORY_C | No | No | No |  |
| 8 | LLB_STATE_C | ZC_SUBSCR_EEP_STE | SUBSCR_EEP_STE_C | No | No | No |  |
| 8 | LLB_STATE_C | ZC_TAX_STATE | TAX_STATE_C | No | No | No |  |
| 10 | LLB_BILL_DEPT_ID | BH_DEP | DEPARTMENT_ID | No | No | No |  |

_(77 total; showing first 30)_
