# CLARITY_POS

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=CLARITY_POS

## Description

The CLARITY_POS table contains information about your places of service. All EAF records are included in this table regardless of their type. That is, facilities, locations, service areas, and places of service are all included in this table.

**Primary table** in this group (101 cols). Overflow siblings joined on shared key: CLARITY_POS_2 (10 cols). Prefer this table for most queries.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | EAF |
| Release Version | EPIC 2000 |
| May contain EHI? | No |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| POS_ID | NUMERIC (18,0) | The unique ID number assigned to the place of service record. |
| POS_NAME | VARCHAR (200) | The name of the place of service. |
| POS_GROUP | INTEGER |  |
| POS_TYPE *(deprecated)* | VARCHAR (66) |  |
| POS_LOC_IS_OUTSIDE | VARCHAR (10) |  |
| POS_NAME_ABBR | VARCHAR (25) | The abbreviated name of the place of service. |
| GL_PREFIX | VARCHAR (128) | The code that billing system's General Ledger report uses to identify transactions belonging to a revenue location. |
| RPT_GRP_ONE | VARCHAR (80) | You can specify groupers for enterprise reporting, SQL, or report generator reporting. This is one of the free-text report groupers. |
| RPT_GRP_TWO | VARCHAR (80) | You can specify groupers for enterprise reporting, SQL, or report generator reporting. This is one of the free-text report groupers. |
| RPT_GRP_THREE | VARCHAR (80) | You can specify groupers for enterprise reporting, SQL, or report generator reporting. This is one of the free-text report groupers. |
| RPT_GRP_FOUR | VARCHAR (80) | You can specify groupers for enterprise reporting, SQL, or report generator reporting. This is one of the free-text report groupers. |
| RPT_GRP_FIVE | VARCHAR (80) | You can specify groupers for enterprise reporting, SQL, or report generator reporting. This is one of the free-text report groupers. |
| RPT_GRP_SIX | VARCHAR (66) |  |
| RPT_GRP_SEVEN | VARCHAR (66) |  |
| RPT_GRP_EIGHT | VARCHAR (66) |  |
| RPT_GRP_NINE | VARCHAR (66) |  |
| RPT_GRP_TEN | VARCHAR (66) |  |
| ADDRESS_LINE_1 | VARCHAR (80) | The first line of the street address for this place of service. |
| ADDRESS_LINE_2 | VARCHAR (80) | The second line of the street address for this place of service. |
| CITY | VARCHAR (60) | The city for this place of service. |
| STATE_C | VARCHAR (66) |  |
| ZIP | VARCHAR (50) | The ZIP Code for this place of service. |
| AREA_CODE | VARCHAR (5) | The area code for the place of service. |
| PHONE | VARCHAR (50) | The phone number for the place of service. |
| LOC_TYPE_C | INTEGER |  |
| CM_PHY_OWNER_ID | VARCHAR (25) | ID of the physical deployment owner for this record.  Physical owners will be where the data is hosted, either on the cross-over server or the owner deployment. |
| CM_LOG_OWNER_ID | VARCHAR (25) | ID of the logical deployment owner for this record.  Logical owners show the deployment where the record was created but doesn't represent if the record is a part of version skew. |
| RPT_GRP_ELEVEN_C | VARCHAR (66) |  |
| RPT_GRP_TWELVE_C | VARCHAR (66) |  |
| RPT_GRP_THIRTEEN_C | VARCHAR (66) |  |
| RPT_GRP_FOURTEEN_C | VARCHAR (66) |  |
| RPT_GRP_FIFTEEN_C | VARCHAR (66) |  |
| RPT_GRP_SIXTEEN_C | VARCHAR (66) |  |
| RPT_GRP_SEVNTEEN_C | VARCHAR (66) |  |
| RPT_GRP_EIGHTEEN_C | VARCHAR (66) |  |
| RPT_GRP_NINETEEN_C | VARCHAR (66) |  |
| RPT_GRP_TWENTY_C | VARCHAR (66) |  |
| RECORD_STATUS | INTEGER |  |
| BUILDING_NUMBER | VARCHAR (254) | Building number of a facility. Part of the facility's address in some countries. |
| DISTRICT_C | INTEGER |  |
| COUNTY_C | VARCHAR (66) |  |
| COUNTRY_C | VARCHAR (66) |  |
| LOGO_FILENAME | VARCHAR (260) | This column contains the filename of an image used for the logo of a particular location or service area. |
| POS_CODE | VARCHAR (25) | Code for Place of Service. |
| POS_TYPE_C | INTEGER |  |
| SERVICE_AREA_ID | NUMERIC (18,0) | Parent service area for this POS. |
| ORG_IDNT | VARCHAR (25) | The unique identifier for an external organization or place of service. |
| REGION_ID | NUMERIC (18,0) | The ID of the region to which this organization pertains. This can be used to group a number of different external organizations together into one logical group. For example: all external organizations in a certain geographical area could constitute a Region. |
| GROUP_ID | NUMERIC (18,0) | The ID for the group to which this organization pertains. This can be used to group a number of different external organizations together into one logical group. A group is generally part of a region. |
| OPEN_DT | DATETIME | The date when the organization opened. |
| CLOSE_DT | DATETIME | The date when the organization closed. |
| JOIN_DT | DATETIME | The date when the organization joined its parent organization. |
| LEAVE_DT | DATETIME | The date when the organization left its parent organization. |
| POS_SUBTYPE_C | INTEGER |  |
| ADT_PARENT_ID | NUMERIC (18,0) | Represents the parent for this hospital area or organization. This could be a service area or revenue location for revenue locations and hospital areas, or a place of service for other place of service records. |
| LOGO_PRINT_GROUP_ID | NUMERIC (18,0) | This item defines the print group that should be used as a logo at the top of reports printed from this location. This can be overridden at the Department level by populating item DEP 17018. |
| CLINIC_OR_BILLING_C | INTEGER |  |
| TECH_CONTACT_NAME | VARCHAR (60) | Technical contact name for the 835. |
| TECH_CONTACT_EMAIL | VARCHAR (254) | Technical contact e-mail address for the 835. |
| TECH_CONTACT_PHONE | VARCHAR (254) | Technical contact phone number for the 835. |
| TECH_CONTACT_URL | VARCHAR (254) | Technical contact website URL for the 835. |
| TECH_CONTACT_FAX | VARCHAR (254) | Technical contact fax number for the 835. |
| TECH_CONTACT_EXT | VARCHAR (254) | Technical contact phone extension for the 835. |
| FAX_NUM | VARCHAR (80) | This is the fax number corresponding to the location. |
| SD_RW_EXPORT_TEMPLATE_ID | NUMERIC (18,0) | This identifies the Reporting Workbench template to use when a user exports a patient population from SlicerDicer into Reporting Workbench. |
| PO_MEDICARE_NUM | VARCHAR (254) | The facility's Medicare provider number. |
| BOOK_ANYWHERE_CONFIG_ID *(deprecated)* | NUMERIC (18,0) | *** Deprecated *** In table CLARITY_POS, the column BOOK_ANYWHERE_CONFIG_ID (EAF/15500) has been deprecated  The deprecated column's content/data is no longer available since it is no longer populated in Chronicles. |
| NOT_LEAKED_DEMAND_YN | VARCHAR (1) |  |
| ADDRESS_CHECKSUM | VARCHAR (184) | This item is populated on external Place Of Service EAF records. It stores a unique value that corresponds to the physical address items: Address (400), City (410), State (420), Zip Code (430). |
| LINK_ORG_ID | NUMERIC (18,0) | Organization (DXO) that links to this location. |
| TC_ZONE_C | INTEGER |  |
| LEGAL_OPEN_DT | DATETIME | The date that this organization was legally opened. |
| LEGAL_CLOSE_DT | DATETIME | The date that this organization was legally closed. |
| ODS_LAST_CHANGE_DT | DATETIME | The date that this external organization's information was last updated by ODS file imports. |
| RECORD_CLASS_C | INTEGER |  |
| EMAIL_ADDRESS | VARCHAR (250) | This item contains the email address for the organization. |
| WEB_ADDRESS | VARCHAR (250) | This item contains the web address for the organization. |
| ALLOW_REFER_TO_YN | VARCHAR (1) |  |
| LEVEL_OF_CARE_MAP_TBL_ID | NUMERIC (18,0) | General Table ID for mapping patient level of care values to department level of care values. |
| SERVICE_MAP_TBL_ID | NUMERIC (18,0) | General Table ID for mapping patient service values to department service values. |
| CLAIM_SERV_FAC_NAME | VARCHAR (60) | String to use as the Service Facility Location name on claims. |
| POS_LOC_IS_OUTSIDE_YN | VARCHAR (1) |  |
| HL_IS_ON_C | INTEGER |  |
| FAC_ACTOR_TYPE_C | INTEGER |  |
| PERMIT_CLIN_DERIVATION_YN | VARCHAR (1) |  |
| CLM_SERV_FAC_ADDR_1 | VARCHAR (80) | Address line 1 to populate for the service facility location address on claims |
| CLM_SERV_FAC_ADDR_2 | VARCHAR (80) | Address line 2 to populate for the service facility location address on claims |
| CLM_SERV_FAC_CITY | VARCHAR (60) | City to populate for the service facility location address on claims |
| CLM_SRV_FAC_STATE_C | VARCHAR (66) |  |
| CLM_SERV_FAC_ZIP | VARCHAR (50) | ZIP code to populate for the service facility location address on claims |
| COMPILED_HL_IS_ON_C | INTEGER |  |
| IS_BUSINESS_SEGMENT_YN | VARCHAR (1) |  |
| IS_NON_BUS_SEG_SERV_AREA_YN | VARCHAR (1) |  |
| MAILING_ADDRESS_CITY | VARCHAR (254) | City in which the mailing address is located. |
| MAILING_ADDRESS_STATE_C | VARCHAR (66) |  |
| MAILING_ADDRESS_COUNTY_C | VARCHAR (66) |  |
| MAILING_ADDRESS_COUNTRY_C | VARCHAR (66) |  |
| MAILING_ADDRESS_ZIP | VARCHAR (50) | Zip Code in which the mailing address is located. |
| MAILING_ADDRESS_BUILDING_NUM | VARCHAR (254) | Building number of the mailing address. |
| MAILING_ADDRESS_DISTRICT_C | INTEGER | Surrogate key used to uniquely identify rows in this (and only this) table on Cogito Cloud only, do not assume the surrogate key in this table will correspond to the surrogate key in another table |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | POS_ID | ANALYTICS_SYSTEM_SETTINGS | FACILITY_ID | No | No | No |  |
| 1 | POS_ID | ARPB_SA_SETTINGS | FACILITY_ID | No | No | No |  |
| 1 | POS_ID | CLARITY_LOC | LOC_ID | Unknown | No | No |  |
| 1 | POS_ID | CLARITY_LOC_2 | LOC_ID | Unknown | No | No |  |
| 1 | POS_ID | CLARITY_POS_2 | POS_ID | No | No | No |  |
| 1 | POS_ID | CLARITY_SA | SERV_AREA_ID | Unknown | No | No |  |
| 1 | POS_ID | CL_LOC_HIERARCHY | LOC_ID | Unknown | No | No |  |
| 1 | POS_ID | CV_PCI_D2B_SETTINGS | FACILITY_ID | No | No | No |  |
| 1 | POS_ID | EAF_CLM_ALTADR_INF | FACILITY_ID | No | No | No |  |
| 1 | POS_ID | EAF_CLM_RMT_SETUP | FACILITY_ID | No | No | No |  |
| 1 | POS_ID | EAF_EXP_APPT_LOG | FACILITY_ID | No | No | No |  |
| 1 | POS_ID | EAF_SEARCH_TERMS | FACILITY_ID | No | No | No |  |
| 1 | POS_ID | ESCALATION_THRESH_SGL | FACILITY_ID | No | No | No |  |
| 1 | POS_ID | FAC_CONNECT | FACILITY_ID | No | No | No |  |
| 1 | POS_ID | FAC_DIRECT_ADDR | FACILITY_ID | Unknown | No | No |  |
| 1 | POS_ID | HH_FAC_INFO | FACILITY_ID | No | No | No |  |
| 1 | POS_ID | MC_FACILITY_GL_SEGMENTS | FACILITY_ID | No | No | No |  |
| 1 | POS_ID | MYC_INFO | FACILITY_ID | No | No | No |  |
| 1 | POS_ID | OR_LOC | LOC_ID | Unknown | No | No |  |
| 1 | POS_ID | PDMD_FILE_CONFIG | FACILITY_ID | No | No | No |  |
| 1 | POS_ID | RX_LOC | LOC_ID | Unknown | No | No |  |
| 1 | POS_ID | SD_FILTER_CONFIG_SETTING | FACILITY_ID | Yes | No | No |  |
| 1 | POS_ID | SERVICE_PROV | FACILITY_ID | No | No | No |  |
| 1 | POS_ID | SMS_SETTINGS_SNGL | FACILITY_ID | No | No | No |  |
| 1 | POS_ID | SYS_RSH_RPT_GRP_OVRIDE | FACILITY_ID | No | No | No |  |
| 1 | POS_ID | V_CMS_MU_LOC | LOC_ID | Unknown | Unknown | No |  |
| 1 | POS_ID | V_CUBE_D_LOCATION | LOCATION_ID | Unknown | Unknown | No |  |
| 1 | POS_ID | V_CUBE_D_SERVICE_AREA | SERVICE_AREA_ID | Unknown | Unknown | No |  |
| 1 | POS_ID | V_OR_LOC_STRUCTURE | OR_LOC_ID | Unknown | Unknown | No |  |
| 3 | POS_GROUP | ZC_POS_GROUP | POS_GROUP | No | No | No |  |

_(244 total; showing first 30)_
