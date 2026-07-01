# ORDER_RESULTS

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=ORDER_RESULTS

## Description

This table contains information on results from clinical system orders. This table extracts only the last Orders (ORD) contact for each ORD record.

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
| LINE | No | The line number of each result component within each ordered procedure. |
| ORD_DATE_REAL | No | This is a numeric representation of the date each order was placed in your system. The integer portion of the number specifies the date the order was placed. The digits after the decimal point indicate multiple orders on one day. |
| ORD_END_DATE_REAL | No | This is a numeric representation of the end date for each order in your system. The integer portion of the number specifies the date the order was placed. The digits after the decimal point indicate multiple orders on one day. |
| RESULT_DATE | DATETIME | The date the technician ran the tests for each order in calendar format. |
| COMPONENT_ID | NUMERIC (18,0) | The unique ID of each result component for each result. |
| PAT_ID *(deprecated)* | VARCHAR (18) |  |
| PAT_ENC_DATE_REAL | No |  |
| PAT_ENC_CSN_ID | NUMERIC (18,0) | A unique serial number for the associated patient encounter. This number is unique across all patients and encounters in the system. |
| ORD_VALUE | VARCHAR (254) | The value returned for each result component, in short free text format. NOTE:  This is how the data is stored in the database; as string format. Interface data may come in with alpha characters and this field is designed to store exactly what is stored in the database. This field stores numeric and structured numeric values in M internal format, using a period as the decimal separator irrespective of locale. |
| ORD_NUM_VALUE | No | A numeric representation of the value returned for each component where applicable. If the value contains any non-numeric characters, the value will display as 9999999. |
| RESULT_FLAG_C | VARCHAR (66) |  |
| REFERENCE_LOW | VARCHAR (50) | The lowest acceptable value for each result component. If the value in this column is a number or structured numeric, the numbers will be stored in M internal format, using a period as the decimal separator. |
| REFERENCE_HIGH | VARCHAR (50) | The highest acceptable value for each result component. If the value in this column is a number or structured numeric, the numbers will be stored in M internal format, using a period as the decimal separator. |
| REFERENCE_UNIT | VARCHAR (100) | The units for each result component value. |
| RESULT_STATUS_C | INTEGER |  |
| RESULT_SUB_IDN | VARCHAR (100) | This item is populated with the unique organism identifier (OVR 700 or interface) when the component of an order result is an organism and can be joined to ORDER_SENSITIVITY.SENS_ORGANISM_SID to identify details about this organism. |
| LAB_STATUS_C | INTEGER |  |
| INTERFACE_YN | VARCHAR (1) |  |
| SERV_AREA_ID | No | *** Deprecated *** In table ORDER_RESULTS, the column SERV_AREA_ID has been deprecated. This column has been replaced by column SERV_AREA_ID in table PAT_ENC. Please reference the replacement column to get the relevant values. |
| RESULT_TIME | 26 | The date and time the technician ran the tests for each order in calendar format. NOTE: Concatenates the result date  and result time  into a datetime format. If the time value is null, the query will return 12:00 AM for a time. |
| RESULTING_LAB_ID | NUMERIC (18,0) | The Unique ID of the Lab running the test. |
| CM_CT_OWNER_ID | VARCHAR (25) | The contact owner deployment of this record, , used in Community Model record sharing. |
| COMPONENT_COMMENT | VARCHAR (1000) | Contains the comments associated with a order COMPONENT_ID, i.e. this is the comments associated with a specific order component's results. If comment data is too long to fit in this item, then the comments will be found in the ORDER_RES_COMMENT table. |
| RESULT_IN_RANGE_YN | VARCHAR (1) |  |
| REF_NORMAL_VALS | VARCHAR (254) | This is a free-text item which allows you to enter a reference range without tying it to a "low" or "high" value. For example, it could be a string ("negative"), a list of choices ("Yellow, orange"), or a descriptive range ("Less than 20"). The values entered in this range should always represent the "normal" values. This item will be displayed in Results Review as the reference range, superseding any values in the low or high items. It may also be displayed in reports, if the print groups are configured to use it. Multiple responses are permitted (one per line). If the value in this column is a number or structured numeric, the numbers will be stored in M internal format using a period as the decimal separator. |
| LRR_BASED_ORGAN_ID | NUMERIC (18,0) | Used for storing discrete organisms. This item is used for storing isolated organisms at the component level. There may be cases where an isolated organism does not undergo sensitivity tests and therefore is only stored at the component level. Organisms with sensitivities are also stored in addition to this item. |
| COMP_RES_TECHNICIA | VARCHAR (254) | ID of the Resulting Lab Technician. |
| DATA_TYPE_C | INTEGER |  |
| VALUE_NORMALIZED | VARCHAR (254) | Will contain the structured numeric result value in a delimited structured numeric format. Numbers will be in M internal format. The delimited structured numeric value is the user entered structured numeric value converted to a delimited format. Valid structured numeric formats are range, operator followed by number, and number followed by operator the value stored in this item is of the format:    operator1_$c(16)_number1_$c(16)_operator2_$c(16)_number2. |
| NUMERIC_PRECISION | NUMERIC (18,0) | The number of decimal digits to the right of the decimal point. |
| COMP_OBS_INST_TM | DATETIME (Local) | Timestamp to track per non-micro result component when it was collected/observed. |
| COMP_ANL_INST_TM | DATETIME (Local) | Timestamp to track per non-micro result component when it was analyzed in lab. |
| RESULT_VAL_START_LN | INTEGER | For multi-line results holds the starting line number of RESULTS_CMT column from ORDER_RES_COMMENT table, where the result values begin.  This column is simply an indicator of the line number(s) where a result is stored. |
| RESULT_VAL_END_LN | INTEGER | For multi-line results holds the ending line number of RESULTS_CMT column from ORDER_RES_COMMENT table, where the result values begin.  This column is simply an indicator of the line number(s) where a result is stored. |
| RESULT_CMT_START_LN | INTEGER | For multi-line results holds the starting line number of RESULTS_CMT column from ORDER_RES_COMMENT table, where the result values begin.  This column is simply an indicator of the line number(s) where a result is stored. |
| RESULT_CMT_END_LN | INTEGER | For multi-line results holds the ending line number of RESULTS_CMT column from ORDER_RES_COMMENT table, where the result values begin.  This column is simply an indicator of the line number(s) where a result is stored. |
| ORD_RAW_VALUE | VARCHAR (254) | Stores the raw value of a numeric result as entered by the user. The value stored here and in column ORD_VALUE will be different in international locales for numeric data if the decimal separator used in that locale is a comma instead of a period. This is because ORD_VALUE will store numeric values in the M internal format. |
| RAW_LOW | VARCHAR (50) | Stores raw value of the minimum value of the result component mentioned in column REFERENCE_LOW. The value stored here and in REFERENCE_LOW will be different in international locales for numeric data if the decimal separator used in that locale is a comma instead of a period. This is because REFERENCE_LOW will store numeric data in M internal format. |
| RAW_HIGH | VARCHAR (50) | Stores raw value of the maximum value of the result component mentioned in column REFERENCE_HIGH. The value stored here and in REFERENCE_HIGH will be different in international locales for numeric data if the decimal separator used in that locale is a comma instead of a period. This is because REFERENCE_HIGH will store numeric data in M internal format. |
| RAW_REF_VALS | VARCHAR (254) | This column stores the raw value of REF_NORMAL_VALS (i.e. the reference normal values of the result component). Since REF_NORMAL_VALS will store numeric data in M internal format, the value stored here and in REF_NORMAL_VALS will be different in international locales if the decimal separator used in that locale is a comma instead of a period. |
| RSLT_REPORTABLE_YN | VARCHAR (1) |  |
| COMPONENT_TYPE_C | INTEGER |  |
| ORGANISM_QUANTITY | VARCHAR (254) | This item is used for storing isolated organisms at the component level. It contains the numeric or qualitative quantity of the organism that was observed. |
| ORGANISM_QUANTITY_UNIT | VARCHAR (100) | This item is used for storing isolated organisms at the component level. It contains the unit associated with the quantity of the organism that was observed. |
| COMPON_LNC_ID | NUMERIC (18,0) | Logical Observation Identifiers Names and Codes (LOINC) ID of the component. |
| COMPON_LNC_SRC_C | INTEGER |  |
| COMP_SNOMED_SRC_C | INTEGER |  |
| REF_UNIT_UOM_ID | NUMERIC (18,0) | Pointer to the record that represents the component's units of measure. |
| VERIFY_USER_ID | VARCHAR (18) | The unique ID of the user who verified each component result. |
| REF_RANGE_TYPE | VARCHAR (100) | Displays the type of the reference range. |
| ORGANISM_SNOMED_CT | VARCHAR (50) | The Systemized Nomenclature of Medicine ? Clinical Terms (SNOMED) code for the component's organism. |
| ORGANISM_QUANTITY_SNOMED_CT | VARCHAR (20) | The Systemized Nomenclature of Medicine ? Clinical Terms (SNOMED) code for the component's organism quantity. |
| PERFORMING_ORG_INFO_LINE | INTEGER | This is used to indicate the performing organization information for the component. This item stores the line number of the ORD related group which is used to save the performing organization information. |
| COMPON_EXCL_CDS_YN | VARCHAR (1) |  |
| COMPON_NETWORK_CONCEPT_IDENT | VARCHAR (50) | The network concept identifier associated with this component. |
| RTF_VAL_START_LINE | INTEGER | If the component result value is rich text, this column gives the first line of ORD_RTF_VAL_CMT that the value is stored in. |
| RTF_VAL_END_LINE | INTEGER | If the component result value is rich text, this column gives the last line of ORD_RTF_VAL_CMT that the value is stored in. |
| RTF_CMT_START_LINE | INTEGER | If the component comment is rich text, this column gives the first line of ORD_RTF_VAL_CMT that the component comment is stored in. |
| RTF_CMT_END_LINE | INTEGER | If the component comment is rich text, this column gives the last line of ORD_RTF_VAL_CMT that the component comment is stored in. |
| RSLT_ACCR_FLAG_YN | VARCHAR (1) |  |
| SIGNATURE_START_LN | INTEGER | Gives the first line of I ORD 2090 that signatures for the related component are stored in |
| SIGNATURE_END_LN | INTEGER | Gives the last line of I ORD 2090 that signatures for the related component are stored in |
| RES_INSTR_CONCEPT_IDENT | VARCHAR (50) | Stores the network concept identifier associated with the component's resulting instrument at the time of verification. |
| RESULT_TREND_C | INTEGER |  |
| RESULT_TREND_UTC_DTTM | DATETIME (UTC) | Instant trend status (I ORD 2056) was set. |
| RESULT_TREND_NAME | VARCHAR (192) | Common name for which trend status (I ORD 2056) was calculated. |
| CULT_GWTH_CNCP_IDENT | VARCHAR (50) | Stores culture growth network concept identifier used for Aura. |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| B-TREE INDEX | EIX_ORDER_RESULTS_CMCTOWID | CM_CT_OWNER_ID | 1 | No | Yes |  |
| B-TREE INDEX | EIX_ORDER_RESULTS_COID | COMPONENT_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_ORDER_RESULTS_CSN | PAT_ENC_CSN_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_ORDER_RESULTS_LRR_ORD_ID | LRR_BASED_ORGAN_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_ORDER_RESULTS_LRR_ORD_ID | ORDER_PROC_ID | 2 | Yes | Yes |  |
| B-TREE INDEX | EIX_ORDER_RESULTS_RESULT_DT | RESULT_DATE | 1 | Yes | Yes |  |

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

_(259 total; showing first 30)_
