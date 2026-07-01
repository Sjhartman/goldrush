# ORDER_SENSITIVITY

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=ORDER_SENSITIVITY

## Description

The ORDER_SENSITIVITY table contains information on the sensitivity of orders placed in clinical system.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | ORD |
| Release Version | EPIC 2000 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| ORDER_PROC_ID | NUMERIC (18,0) | The unique ID of the procedure order record. |
| LINE | No | The line number of the sensitivity data recorded within each procedure record. |
| PAT_ID *(deprecated)* | VARCHAR (18) |  |
| PAT_ENC_DATE_REAL | No |  |
| PAT_ENC_CSN_ID | 8 |  |
| ORD_DATE_REAL | No | This is a numeric representation of the date each order was placed in your system. The integer portion of the number specifies the date the order was placed. The digits after the decimal point indicate multiple orders on one day. |
| ORD_END_DATE_REAL | No | This is a numeric representation of the end date for each order in your system. The integer portion of the number specifies the date the order was placed. The digits after the decimal point indicate multiple orders on one day. |
| CONTACT_DATE | DATETIME | The date of this contact in calendar format. |
| RESULT_DATE | DATETIME | The date the technician ran the tests for each order |
| ORGANISM_ID | NUMERIC (18,0) | The ID of the organism that was cultured and tested for susceptibility. |
| ANTIBIOTIC_C | INTEGER |  |
| SUSCEPT_C | INTEGER |  |
| SENSITIVITY_VALUE | VARCHAR (255) | This item is not populated by the EMR. It may be populated with the sensitivity value from an interface. |
| LAB_STATUS_C | INTEGER |  |
| CM_CT_OWNER_ID | VARCHAR (25) | The contact owner deployment of this record, , used in Community Model record sharing. |
| SENS_ORGANISM_SID | VARCHAR (254) | This item will hold the sub ids for each organism helping the application to create a unique data structure for the display of microbiology results.  The unique data structure will use this item in conjunction with organism name or id as one of the key subscripts thus preventing errors with the display.   E.g. Salmonella typhi (Strain Ty2) and Salmonella typhi (Strain CT18) may have the same name (Salmonella typhi) but will have different sub ids depending on the external system sending the data. In order to display both of the above, a unique sub id is required. |
| SENS_COM_ORG_RES_ID | NUMERIC (18,0) | This item stores the RES (Results master file) record id which stores comments related to the organisms.  The item is related to the organisms stored in item ORD 2220 and the line number of this item will match directly to the organism line number. |
| SENS_OBS_INST_TM | DATETIME (Local) | Timestamp to track per micro result component when it was collected/observed. |
| SENS_ANL_INST_TM | DATETIME (Local) | Timestamp to track per micro result component when it was analyzed in lab. |
| SENS_START_LN | INTEGER | This columns contains the start line of ORD-2290 (extracted in SENS_LONG_VAL) where the long sensitivity value will begin. |
| SENS_END_LN | INTEGER | This column contains the end line of ORD-2290(extracted in SENS_LONG_VAL) where the long sensitivity value will terminate. |
| SENS_COMM | VARCHAR (254) | This column contains a short sensitivity note for ORD-2290 (extracted in SENS_LONG_VAL). |
| SENS_COMM_START_LN | INTEGER | This column contains the start line in ORD-2290(extracted in SENS_LONG_VAL) of a long sensitivity comment. |
| SENS_COMM_END_LN | INTEGER | This column contains the end line in ORD-2290(extracted in SENS_LONG_VAL) of a long sensitivity comment. |
| SENSITIVITY_UNITS | VARCHAR (254) | Indicates units applied for antibiotics on a sensitivity test. |
| SENS_STATUS_C | INTEGER |  |
| ANTIBIO_LNC_ID | NUMERIC (18,0) | The unique identifier of the LOINC record indicating the Logical Observation Identifiers Names and Codes (LOINC) code for the antibiotic associated with the sensitivity. |
| ANTIBIO_LNC_SRC_C | INTEGER |  |
| METHOD_LNC_ID | NUMERIC (18,0) | Microbiology method LOINC ID. |
| METHOD_LNC_SRC_C | INTEGER |  |
| SENS_REF_RANGE | VARCHAR (254) | Indicates the reference range for antibiotics on a sensitivity test. |
| HIDE_ANTIBIOTIC_YN | VARCHAR (1) |  |
| SENS_UNIT_UOM_ID | NUMERIC (18,0) | Pointer to the UOM (units of measure master file) record that represents the sensitivity's unit. |
| SENS_METHOD_ID | NUMERIC (18,0) | This column stores a procedure record ID that represents a method of testing an organism's sensitivity to an antibiotic. The value in this item is used to distinguish sensitivities obtained by different testing methods. |
| RESULTING_LAB_ID | NUMERIC (18,0) | The unique identifier of the resulting agency which is responsible for an antibiotic sensitivity. |
| KANTA_HYGIENE_SIGNIFICANCE_YN | VARCHAR (1) |  |
| SENS_ACCR_STAT_YN | VARCHAR (1) |  |
| SENS_METH_CATL_ENT_CSN_ID | NUMERIC (18,0) | This item stores the contact serial number of the Network Catalog Entry (NCE) record associated with the sensitivity method. |
| SENS_INSTR_CONCEPT_IDENT | VARCHAR (50) | Stores the network concept identifier associated with the sensitivity's resulting instrument at the time of verification. |
| LAB_SENS_KEY_IDENT | VARCHAR (254) | Stores a unique test key representing the lab susceptibility test associated with this sensitivity result. |
| SENS_ANT_CNCP_IDENT | VARCHAR (50) | Stores antibiotic network concept identifier used for Aura. |
| SENS_UNT_CNCP_IDENT | VARCHAR (50) | Stores sensitivity units network concept identifier used for Aura. |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| B-TREE INDEX | EIX_ORDER_SENSITIVITY_ORG_ORD | ORGANISM_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_ORDER_SENSITIVITY_ORG_ORD | ORDER_PROC_ID | 2 | Yes | Yes |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ORDER_PROC_ID | ADT_ORDERS_ERRORS | ORDER_ID | No | No | No |  |
| 1 | ORDER_PROC_ID | ADT_ORDER_INFORMATION | ORDER_ID | No | No | No |  |
| 1 | ORDER_PROC_ID | APPT_REQUEST | REQUEST_ID | No | No | No |  |
| 1 | ORDER_PROC_ID | CL_ORD_FST_LST_SCH | ORDER_ID | No | No | No |  |
| 1 | ORDER_PROC_ID | DENT_ORD_NOADD | ORDER_ID | No | No | No |  |
| 1 | ORDER_PROC_ID | DUPMED_DISMISS_HH_INFO | ORDER_ID | No | No | No |  |
| 1 | ORDER_PROC_ID | ENDOSCOPY_METRICS | ORDER_ID | Unknown | No | No |  |
| 1 | ORDER_PROC_ID | EXTERNAL_ORDER_INFO | ORDER_ID | No | No | No |  |
| 1 | ORDER_PROC_ID | F_IMG_STUDY | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_PROC_ID | F_IP_HSP_SUM_ORDER | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_PROC_ID | F_LAB_ORDERS | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_PROC_ID | F_MU_OBJ_EH_PLACED_ORDER | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_PROC_ID | F_MU_OBJ_EH_RESULTD_ORDER | ORDER_PROC_ID | Unknown | Unknown | No |  |
| 1 | ORDER_PROC_ID | F_ONC_PRIOR_AUTH_ORDERS | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_PROC_ID | F_OPIOID_ORDERS | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_PROC_ID | F_RX_ORDER | ORDER_MED_ID | Unknown | Unknown | No |  |
| 1 | ORDER_PROC_ID | HH_MED_ORD_IN_POC_DETAIL | ORDER_MED_ID | No | No | No |  |
| 1 | ORDER_PROC_ID | HV_ORDER_PROC | ORDER_PROC_ID | Unknown | No | No |  |
| 1 | ORDER_PROC_ID | MED_DETAILS_EXT_ORD | ORDER_ID | No | No | No |  |
| 1 | ORDER_PROC_ID | MERCHANDISE_ORDER_INFO | ORDER_ID | Yes | No | No |  |
| 1 | ORDER_PROC_ID | MU_EH_QRDA_I_ORDER | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_PROC_ID | ORDERS | ORDER_ID | No | No | No |  |
| 1 | ORDER_PROC_ID | ORDER_AUTH_INFO | ORDER_ID | No | No | No |  |
| 1 | ORDER_PROC_ID | ORDER_MED | ORDER_MED_ID | Unknown | No | No |  |
| 1 | ORDER_PROC_ID | ORDER_MEDINFO | ORDER_MED_ID | Unknown | No | No |  |
| 1 | ORDER_PROC_ID | ORDER_MED_2 | ORDER_ID | Unknown | No | No |  |
| 1 | ORDER_PROC_ID | ORDER_MED_3 | ORDER_ID | Unknown | No | No |  |
| 1 | ORDER_PROC_ID | ORDER_MED_4 | ORDER_ID | Unknown | No | No |  |
| 1 | ORDER_PROC_ID | ORDER_MED_5 | ORDER_ID | Unknown | No | No |  |
| 1 | ORDER_PROC_ID | ORDER_MED_6 | ORDER_MED_ID | Unknown | No | No |  |

_(155 total; showing first 30)_
