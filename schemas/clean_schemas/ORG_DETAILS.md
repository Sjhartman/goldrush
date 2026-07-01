# ORG_DETAILS

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=ORG_DETAILS

## Description

Details about the organization. Includes external name, phone/e-mail, hours of operation, HSI, URL.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | DXO |
| Release Version | Summer 2009 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| ORGANIZATION_ID | NUMERIC (18,0) | The unique ID associated with the organization for this row. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| ORGANIZATION_NAME | VARCHAR (200) | Name of this organization. This name appears in all-caps. |
| RECORD_STATUS_C | INTEGER |  |
| ORG_TYPE_C | INTEGER |  |
| HEALTH_SYSTEM_ID | VARCHAR (192) | URI or other id for the health system. |
| ORG_URL | VARCHAR (254) | URL to which info requests are directed. |
| EXTERNAL_NAME | VARCHAR (192) | Organization's external name used as the display name on forms and user interfaces. |
| CITY | VARCHAR (80) | The home city of this organization. |
| STATE_C | VARCHAR (66) |  |
| ZIP | VARCHAR (20) | The zip code of this organization. |
| QUERY_PHONE *(deprecated)* | VARCHAR (20) | *** Deprecated *** In table ORG_DETAILS, the column QUERY_PHONE (DXO/240) has been deprecated. The deprecated column's content/data is no longer available since it is no longer populated in Chronicles.  Query assistance phone number |
| QUERY_EMAIL *(deprecated)* | VARCHAR (80) | *** Deprecated *** In table ORG_DETAILS, the column QUERY_EMAIL (DXO/250) has been deprecated. The deprecated column's content/data is no longer available since it is no longer populated in Chronicles.  Query assistance e-mail address. |
| QUERY_ASSTNCE_HRS *(deprecated)* | VARCHAR (254) | *** Deprecated *** In table ORG_DETAILS, the column QUERY_ASSTNCE_HRS (DXO/255) has been deprecated. The deprecated column's content/data is no longer available since it is no longer populated in Chronicles.  Hours of operation for the query assistance phone/e-mail. |
| AUDIT_PHONE *(deprecated)* | VARCHAR (20) | *** Deprecated *** In table ORG_DETAILS, the column AUDIT_PHONE (DXO/260) has been deprecated. The deprecated column's content/data is no longer available since it is no longer populated in Chronicles.  Phone number for audit assistance contact. |
| AUDIT_EMAIL *(deprecated)* | VARCHAR (80) | *** Deprecated *** In table ORG_DETAILS, the column AUDIT_EMAIL (DXO/270) has been deprecated. The deprecated column's content/data is no longer available since it is no longer populated in Chronicles.  E-mail address for audit assistance contact. |
| IT_PHONE *(deprecated)* | VARCHAR (20) | *** Deprecated *** In table ORG_DETAILS, the column IT_PHONE (DXO/280) has been deprecated. The deprecated column's content/data is no longer available since it is no longer populated in Chronicles.  IT assistance contact phone number. |
| IT_EMAIL *(deprecated)* | VARCHAR (80) | *** Deprecated *** In table ORG_DETAILS, the column IT_EMAIL (DXO/290) has been deprecated. The deprecated column's content/data is no longer available since it is no longer populated in Chronicles.  IT assistance contact e-mail address. |
| FAX_NUMBER *(deprecated)* | VARCHAR (20) | *** Deprecated *** In table ORG_DETAILS, the column FAX_NUMBER (DXO/300) has been deprecated. The deprecated column's content/data is no longer available since it is no longer populated in Chronicles.  Fax number for sending signed authorization documents. |
| ASSOC_WITH_ORG_ID | NUMERIC (18,0) | If this is an associated organization, this item links this record to the organization it is associated with. |
| CONSENT_TEXT_CODE | VARCHAR (10) | Code to group authorization text for organizations. |
| RECORD_CREATE_INST | DATETIME | Creation timestamp. |
| REC_CREATE_USR_ID | VARCHAR (18) | Record creation user identifier. |
| ASC_WITH_DEP_ID | NUMERIC (18,2) | If this is an associated organization, this item links this record to the deployment it is associated with. |
| REQ_WITHOUT_ENC_YN *(deprecated)* | VARCHAR (1) |  |
| DIRECT_ADDRESS | VARCHAR (192) | This item stores the Direct Address which is used to identify your organization when you send referrals or push other messages to outside organizations. This address will be used only if no more specific address can be found. |
| RFL_ENABLED_YN | VARCHAR (1) |  |
| HOME_COMMUNITY_ID | VARCHAR (128) | Specifies the NwHIN Home Community ID for this organization. |
| HIE_TYPE_C | INTEGER |  |
| TEMPLATE_ORG_ID | NUMERIC (18,0) | Specifies which Template DXO the organization inherits configuration from. This item can only be filled in with DXOs of type Template. |
| ALLOW_AUTO_QRY_YN | VARCHAR (1) |  |
| CAREQUALITY_YN | VARCHAR (1) |  |
| AUTOREC_NOTES_WITH_FHIR_YN | VARCHAR (1) |  |
| AUTOREC_NOTE_WO_SRC_ORG_YN | VARCHAR (1) |  |
| RESTR_EXT_CLM_EHI_YN | VARCHAR (1) |  |
| COUNTRY_2_C | VARCHAR (66) |  |
| LEGAL_LOCALITY_C | INTEGER |  |
| PAYER_PLATFORM_PAYER_YN | No | Yes/no column for whether this organization is a Payer Platform payer. |
| MYCC_AUTHORITY_HSI_ID | VARCHAR (192) | Health System Identifier (HSI) for the MyChart Central Authority this organization communicates with. |
| HEDIS_SOURCE_SYSTEM_C | INTEGER |  |
| IS_MULTIPLE_TIME_ZONE_YN | VARCHAR (1) | Surrogate key used to uniquely identify rows in this (and only this) table on Cogito Cloud only, do not assume the surrogate key in this table will correspond to the surrogate key in another table |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ORGANIZATION_ID | ORG_DETAILS_COSMOS | ORGANIZATION_ID | No | No | No |  |
| 1 | ORGANIZATION_ID | ORG_E_RX_NETWORK | ORGANIZATION_ID | No | No | No |  |
| 2 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 2 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 2 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 3 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 5 | RECORD_STATUS_C | ZC_DEL_STATUS | DEL_STATUS_C | No | No | No |  |
| 5 | RECORD_STATUS_C | ZC_EDG_REC_STAT | EDG_REC_STAT_C | No | No | No |  |
| 5 | RECORD_STATUS_C | ZC_ERS_REC_STAT | RECORD_STATUS_C | No | No | No |  |
| 5 | RECORD_STATUS_C | ZC_HCD_REC_STATE | HCD_REC_STATE_C | No | No | No |  |
| 5 | RECORD_STATUS_C | ZC_HFL_RECORD_STAT | HFL_RECORD_STAT_C | No | No | No |  |
| 5 | RECORD_STATUS_C | ZC_IMM_REC_STATUS | IMM_REC_STATUS_C | No | No | No |  |
| 5 | RECORD_STATUS_C | ZC_LLB_STATUS | LLB_STATUS_C | No | No | No |  |
| 5 | RECORD_STATUS_C | ZC_LMA_RECORD_STAT | LMA_RECORD_STAT_C | No | No | No |  |
| 5 | RECORD_STATUS_C | ZC_MEM_REC_STATUS | MEM_REC_STATUS_C | No | No | No |  |
| 5 | RECORD_STATUS_C | ZC_OR_REC_STATUS | OR_REC_STATUS_C | No | No | No |  |
| 5 | RECORD_STATUS_C | ZC_PBA_REC_STAT | PBA_REC_STAT_C | No | No | No |  |
| 5 | RECORD_STATUS_C | ZC_PROV_REC_STATE | PROV_REC_STATE_C | No | No | No |  |
| 5 | RECORD_STATUS_C | ZC_RECORD_STATE_2 | RECORD_STATE_2_C | No | No | No |  |
| 5 | RECORD_STATUS_C | ZC_RECORD_STATE_3 | RECORD_STATE_3_C | No | No | No |  |
| 5 | RECORD_STATUS_C | ZC_RECORD_STATE_4 | RECORD_STATE_4_C | No | No | No |  |
| 5 | RECORD_STATUS_C | ZC_RECORD_STATE_6 | RECORD_STATE_6_C | No | No | No |  |
| 5 | RECORD_STATUS_C | ZC_RECORD_STATE_7 | RECORD_STATE_7_C | No | No | No |  |
| 5 | RECORD_STATUS_C | ZC_RECORD_STAT_EPM | RECORD_STAT_EPM_C | No | No | No |  |
| 5 | RECORD_STATUS_C | ZC_RECORD_STAT_EPP | RECORD_STAT_EPP_C | No | No | No |  |
| 5 | RECORD_STATUS_C | ZC_RECORD_STAT_ETX | RECORD_STAT_ETX_C | No | No | No |  |
| 5 | RECORD_STATUS_C | ZC_RECORD_STAT_HRV | RECORD_STAT_HRV_C | No | No | No |  |
| 5 | RECORD_STATUS_C | ZC_RECORD_STAT_RMC | RECORD_STAT_RMC_C | No | No | No |  |

_(64 total; showing first 30)_
