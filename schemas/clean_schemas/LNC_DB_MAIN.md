# LNC_DB_MAIN

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=LNC_DB_MAIN

## Description

This is the primary table for Logical Observation Identifiers Names and Codes (LOINC?) information.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | FULL |
| Load Frequency | WEEKLY - FULL |
| Chronicles INI | LNC |
| Release Version | Summer 2009 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| RECORD_ID | NUMERIC (18,0) | The unique identifier for the Logical Observation Identifiers Names and Codes (LOINC?) code. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this Chronicles record. This is populated only if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this Chronicles record was extracted. This is populated only if you use IntraConnect. |
| LOINC_CODE_NM *(deprecated)* | VARCHAR (192) | In table LNC_DB_MAIN, the column LOINC_CODE_NM (LNC/.2) has been deprecated. The deprecated column's content/data is no longer available since it is no longer populated in Chronicles. If populated, this will contain name of the LOINC code. |
| RECORD_STATUS_C | INTEGER |  |
| LNC_REC_TYP_C | INTEGER |  |
| LNC_VER | VARCHAR (192) | The Logical Observation Identifiers Names and Codes (LOINC?) version number of either the definition or the individual code. |
| LNC_VER_DT | DATETIME | The date the version of the Logical Observation Identifiers Names and Codes (LOINC?) code was released by Regenstrief Institute, Inc. |
| LNC_FULL_NAM | VARCHAR (500) | The fully specified name of the Logical Observation Identifiers Names and Codes (LOINC?) code, stored as a virtual item for reporting. |
| LNC_CODE | VARCHAR (20) | The unique code for the Logical Observation Identifiers Names and Codes (LOINC?) code. |
| LNC_COMPON | VARCHAR (255) | The component/analyte value of the Logical Observation Identifiers Names and Codes (LOINC?) code. |
| LNC_PROPERTY_C | INTEGER |  |
| LNC_TM_ASPCT_C | INTEGER |  |
| LNC_TM_ASPCT_VAL_C | INTEGER |  |
| LNC_CALC_DURATN | INTEGER | The time duration (in seconds) of a Logical Observation Identifiers Names and Codes (LOINC?) code. |
| LNC_TM_ASPCT_MOD_C | INTEGER |  |
| LNC_SYS | VARCHAR (192) | The system for the Logical Observation Identifiers Names and Codes (LOINC?) code. |
| LNC_SUPER_SYS | VARCHAR (192) | The super system of the Logical Observation Identifiers Names and Codes (LOINC?); the second subpart of the System. |
| LNC_SCALE_C | INTEGER |  |
| LNC_MTHD | VARCHAR (192) | The method of the Logical Observation Identifiers Names and Codes (LOINC?) code. |
| LNC_CLASS | VARCHAR (20) | The class used to type the Logical Observation Identifiers Names and Codes (LOINC?) code. |
| LNC_LST_CHNG_DT | DATETIME | The date of the last update from Regenstrief Institute, Inc. |
| LNC_CHNG_TYP_C | INTEGER |  |
| LNC_STAT_C | INTEGER |  |
| LNC_MAP_LNC_ID | NUMERIC (18,0) | The Logical Observation Identifiers Names and Codes (LOINC?) code that replaces this LOINC code.  This will be set if this LOINC code has been deprecated and replaced. |
| LNC_SCOPE | VARCHAR (20) | The scope of the Logical Observation Identifiers Names and Codes (LOINC?) code. Not currently in use. |
| LNC_NORM_RANGE | VARCHAR (30) | Example normal range for the Logical Observation Identifiers Names and Codes (LOINC?) code. Not currently in use. |
| LNC_IPCC_UNIT | VARCHAR (30) | IPCC Units. Units for new Logical Observation Identifiers Names and Codes (LOINC?) codes will not be stored here and should be looked up in RELMA. |
| LNC_EXCT_COMPON_SYN | VARCHAR (50) | The exact component synonym of the Logical Observation Identifiers Names and Codes (LOINC?) code. |
| LNC_MOLAR_MASS | NUMERIC (18,2) | The molar mass provided by IUPAC for the Logical Observation Identifiers Names and Codes (LOINC?) code. |
| LNC_CLASS_TYP_C | INTEGER |  |
| LNC_FORMULA | VARCHAR (255) | Regression formula for many OB.US calculations that is used by the Logical Observation Identifiers Names and Codes (LOINC?) code. |
| LNC_BASE_NAM | VARCHAR (50) | The base name provided by the Chemical Abstract Society. |
| LNC_FINAL_YN | VARCHAR (1) |  |
| LNC_NAACCR | VARCHAR (20) | An example ID from NAACCR for the Logical Observation Identifiers Names and Codes (LOINC?) code. |
| LNC_CANCER_REG_ID | VARCHAR (10) | An example CR0050 Cancer Registry ID for the Logical Observation Identifiers Names and Codes (LOINC?) code. |
| LNC_SET_ROOT_YN | VARCHAR (1) |  |
| LNC_SRVY_QUESN_TXT | VARCHAR (1000) | The HIV Survey Question for the Logical Observation Identifiers Names and Codes (LOINC?) code. |
| LNC_SRVY_QUESN_SRC | VARCHAR (50) | The source of the HIV survey question (found in the column LNC_SRVY_QUESN_TXT) for the Logical Observation Identifiers Names and Codes (LOINC?) code. Exact name of the survey instrument and item/question number. |
| LNC_UNITS_REQ_YN | VARCHAR (1) |  |
| LNC_SUBMT_UNIT | VARCHAR (30) | Example units that were submitted. Units for new Logical Observation Identifiers Names and Codes (LOINC?) codes will not be stored here and should be looked up in RELMA. |
| LNC_SHORT_NAM | VARCHAR (192) | A concatenation of the six main components of the Logical Observation Identifiers Names and Codes (LOINC?) code, meant to be smaller than the full name. The size might change in the future. |
| LNC_ORD_OBSRVTN_C | INTEGER |  |
| LNC_CDISC_YN | VARCHAR (1) |  |
| LNC_HL7_FIELD | VARCHAR (50) | Indicates the HL7 field and subfield that this should be passed in when using this Logical Observation Identifiers Names and Codes (LOINC?) code. |
| LNC_EXAMPLE_UNIT | VARCHAR (255) | Example units that have been submitted. Units for new Logical Observation Identifiers Names and Codes (LOINC?) codes will not be stored here and should be looked up in RELMA. |
| RECORD_CREATION_DT | DATETIME | Stores the date the Logical Observation Identifiers Names and Codes (LOINC?) code was created. |
| INSTANT_OF_UPD_DTTM | DATETIME (Local) | Stores the instant the code was last locked/unlocked. |
| LNC_CONSUMER_NAME | VARCHAR (192) | An consumer friendly name stored in Logical Observation Identifiers Names and Codes (LOINC?) code. |
| LNC_INPC_PCENT | NUMERIC (15,12) | The INPC percentage of the Logical Observation Identifiers Names and Codes (LOINC?) code. Not currently in use. |
| LNC_LONG_NAME | VARCHAR (508) | The more readable format than the fully specified name in Logical Observation Identifiers Names and Codes (LOINC?) code. |
| LOINC_HL7_V2_TYPE | VARCHAR (10) | HL7 version 2.x data type that would be sent in OBX-2 when this data is delivered in an HL7 message with this Logical Observation Identifiers Names and Codes (LOINC?) code. |
| LNC_HL7_V3_TYPE_C *(deprecated)* | INTEGER |  |
| LNC_CURATED_UNIT | VARCHAR (50) | A curated list of normal ranges and associated units (expressed as near UCUM codes) for physical quantities and survey scores. |
| LNC_DOC_SEC_C *(deprecated)* | INTEGER |  |
| LNC_UCUM_UNIT | VARCHAR (50) | The Unified Code for Units of Measure (UCUM) is a code system intended to include all units of measures being contemporarily used in international science, engineering, and business. |
| LNC_SI_UCUM_UNIT | VARCHAR (50) | The Unified Code for Units of Measure (UCUM) is a code system intended to include all units of measures being contemporarily used in international science, engineering, and business. |
| LNC_STAT_REASN_C | INTEGER |  |
| LNC_STAT_TEXT | VARCHAR (508) | Explanation of concept status in narrative text in this Logical Observation Identifiers Names and Codes (LOINC?) code. |
| LNC_CHG_RSON_PUBLIC | VARCHAR (700) | Detailed explanation about special changes to the term over time. |
| LNC_CMN_TEST_RANK | INTEGER | Ranking of approximately 2000 common tests performed by laboratories in USA. |
| LNC_CMN_ORD_RANK | INTEGER | Ranking of approximately 300 common orders performed by laboratories in USA. |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 2 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 2 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 3 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 5 | RECORD_STATUS_C | ZC_RECORD_STATUS_2 | RECORD_STATUS_2_C | No | No | No |  |
| 5 | RECORD_STATUS_C | ZC_RECORD_STS | RECORD_STS_C | No | No | No |  |
| 6 | LNC_REC_TYP_C | ZC_LNC_REC_TYP | LNC_REC_TYP_C | No | No | No |  |
| 12 | LNC_PROPERTY_C | ZC_LNC_PROPERTY | LNC_PROPERTY_C | No | No | No |  |
| 13 | LNC_TM_ASPCT_C | ZC_LNC_TM_ASPCT | LNC_TM_ASPCT_C | No | No | No |  |
| 14 | LNC_TM_ASPCT_VAL_C | ZC_LNC_TM_ASPCT_VA | LNC_TM_ASPCT_VA_C | No | No | No |  |
| 16 | LNC_TM_ASPCT_MOD_C | ZC_LNC_TM_ASPCT_MO | LNC_TM_ASPCT_MO_C | No | No | No |  |
| 19 | LNC_SCALE_C | ZC_LNC_SCALE | LNC_SCALE_C | No | No | No |  |
| 23 | LNC_CHNG_TYP_C | ZC_LNC_CHNG_TYP | LNC_CHNG_TYP_C | No | No | No |  |
| 24 | LNC_STAT_C | ZC_LNC_STAT | LNC_STAT_C | No | No | No |  |
| 25 | LNC_MAP_LNC_ID | LNC_DB_MAIN | RECORD_ID | Unknown | No | No |  |
| 31 | LNC_CLASS_TYP_C | ZC_LNC_CLASS_TYP | LNC_CLASS_TYP_C | No | No | No |  |
| 43 | LNC_ORD_OBSRVTN_C | ZC_LNC_ORD_OBSRVTN | LNC_ORD_OBSRVTN_C | No | No | No |  |
| 58 | LNC_STAT_REASN_C | ZC_LNC_STAT_REASN | LNC_STAT_REASN_C | No | No | No |  |
