# CLARITY_SER_ADDR

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=CLARITY_SER_ADDR

## Description

The CLARITY_SER_ADDR table includes the office addresses for providers.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | SER |
| Release Version | MU2 - MAY 2001 |
| May contain EHI? | No |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| PROV_ID | VARCHAR (18) | The unique ID of the provider for the office address. |
| LINE | No | The line count of the office address for the provider. |
| ADDR_UNIQUE_ID | VARCHAR (120) | The unique ID of the office address for this provider. |
| ADDR_LINE_1 | VARCHAR (508) | The first line of the office street address for this provider. |
| ADDR_LINE_2 | VARCHAR (508) | The second line of the office street address for this provider. |
| ADDR_LINE_3 | VARCHAR (508) | The third line of the office street address for this provider. |
| CITY | VARCHAR (508) | The city for the provider's office mailing address. |
| STATE_C | VARCHAR (66) |  |
| ZIP | VARCHAR (508) | The ZIP Code for the provider's office mailing address. |
| COUNTY_C | VARCHAR (66) |  |
| COUNTRY_C | VARCHAR (66) |  |
| PRIMARY_ADDR_YN | VARCHAR (1) |  |
| PHONE | VARCHAR (508) | The phone number for the provider's office address. |
| FAX | VARCHAR (192) | The fax number for the provider's office address. |
| ACTIVE_YN | VARCHAR (1) |  |
| EMAIL | VARCHAR (508) | The e-mail for the provider's office address. |
| EXT_ADDR_ID | VARCHAR (15) | The external system ID for this office address. |
| CM_PHY_OWNER_ID | VARCHAR (25) | ID of the physical deployment owner for this record.  Physical owners will be where the data is hosted, either on the cross-over server or the owner deployment. |
| CM_LOG_OWNER_ID | VARCHAR (25) | ID of the logical deployment owner for this record.  Logical owners show the deployment where the record was created but doesn't represent if the record is a part of version skew. |
| PRACTICE_NAME_C | INTEGER |  |
| HOUSE_NUM | VARCHAR (254) | The house number for the provider's office mailing address. |
| DISTRICT_C | INTEGER |  |
| SEC_ADDR_FAX_DATE | DATETIME | Date on which the related fax number was registered. |
| CNTCT_MTHD_ADDR_C | INTEGER |  |
| SER_PRINTER_ID | NUMERIC (18,0) | The unique ID of the printer that is used to print results report at this office address for this provider. |
| ADDR_POS_ID | NUMERIC (18,0) | Links to a Facility Profile (EAF) record that represents the correct external location for the Transition of Care. |
| DIRECT_ADDR | VARCHAR (184) | Formatted like an email address, this is how Direct messaging knows where to send a message. This item is stored in mixed case to use in display in addressing. |
| ORG_ID | NUMERIC (18,0) | Organization the address is associated with. |
| SHARED_ADDRESS_YN | VARCHAR (1) |  |
| INTERNAL_ADDRESS_YN | VARCHAR (1) |  |
| SOURCE_OF_IMPORT | VARCHAR (32) | String identifying the imported external data source from which this address was created. |
| EXT_PRACTICE_NAME | VARCHAR (128) | String identifying the external place name of this address line. |
| ADDR_LOC_ID | NUMERIC (18,0) | Links to a Facility Profile (EAF) record that represents the secondary address in the related group. |
| CNTCT_MTHD_RULE_ID | NUMERIC (18,0) | The rule to determine the appropriate communication method for a given address. |
| SECONDARY_RAR_FAX | VARCHAR (192) | The refill authorization request fax number of the provider's office location. If nothing is specified here, then the provider's fax number is used. |
| DUPLICATE_EAF_ID | NUMERIC (18,0) | The ID of the EAF record that represents this address line. |
| ADDRESS_CHECKSUM | VARCHAR (184) | This item is populated on place-type SER records. It stores a unique value that corresponds to a line of secondary address items: Secondary Address Line 1-3 (21010,21020,21030), City (21040), State (21050), Zip Code (21060). |
| ADDR_CE_SET_IDENT | VARCHAR (184) | This item stores the Care Everywhere set ID. External EAF records and Place-type SER address lines with the same name and address checksum will have the same set ID. Recipients with the same set ID will be merged in Recipient Lookup if they have same direct address and phone number. |
| ADDR_LINK_LOC_ID | NUMERIC (18,0) | Location that this address links to. Determined by physical address, Direct Address, and source organization. |
| DIS_LOC_CALC_YN | VARCHAR (1) |  |
| ADDR_LINK_ORG_ID | NUMERIC (18,0) | Organization this address links to. Determined by Direct address, or overridden by SER-21170. |
| VENDOR_ID | VARCHAR (18) | The vendor of the provider's office location. |
| EFF_DATE | DATETIME | The date when the specific address line becomes effective for the provider. |
| TERM_DATE | DATETIME | The last date when the specific address line is effective for the provider. |
| DELETED_YN | VARCHAR (1) |  |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| B-TREE INDEX | EIX_CLARITY_SER_ADDR_ADUNID | ADDR_UNIQUE_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_CLARITY_SER_ADDR_PRID_CMP | PROV_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_CLARITY_SER_ADDR_PRID_CMP | EXT_ADDR_ID | 2 | Yes | Yes |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | PROV_ID | CLARITY_SER | PROV_ID | Unknown | No | No |  |
| 1 | PROV_ID | CLARITY_SER_2 | PROV_ID | Unknown | No | No |  |
| 1 | PROV_ID | CLARITY_SER_3 | PROV_ID | Unknown | No | No |  |
| 1 | PROV_ID | CLARITY_SER_4 | PROV_ID | No | No | No |  |
| 1 | PROV_ID | CLARITY_SER_MYC | PROV_ID | Unknown | No | No |  |
| 1 | PROV_ID | D_PROV_PRIMARY_HIERARCHY | PROV_ID | Unknown | Unknown | No |  |
| 1 | PROV_ID | ED_SER_SETTINGS | PROV_ID | Unknown | No | No |  |
| 1 | PROV_ID | EXT_CAL_PROV_CONFIG | PROV_ID | No | No | No |  |
| 1 | PROV_ID | OR_SER_EQUIPMENT | PROV_ID | Unknown | No | No |  |
| 1 | PROV_ID | OR_SER_ROOM | PROV_ID | Unknown | No | No |  |
| 1 | PROV_ID | PROV_BATCH_LTR_GEN | PROV_ID | Unknown | No | No |  |
| 1 | PROV_ID | PROV_GROUP | PROV_ID | No | No | No |  |
| 1 | PROV_ID | V_CUBE_D_PROVIDER | PROVIDER_ID | Unknown | Unknown | No |  |
| 8 | STATE_C | ZC_ALT_INVOICE_STA | ALT_INVOICE_STA_C | No | No | No |  |
| 8 | STATE_C | ZC_LLB_STATE | LLB_STATE_C | No | No | No |  |
| 8 | STATE_C | ZC_REFG_PROV_STATE | REFG_PROV_STATE_C | No | No | No |  |
| 8 | STATE_C | ZC_STATE | STATE_C | No | No | No |  |
| 8 | STATE_C | ZC_STATE_HISTORY | STATE_HISTORY_C | No | No | No |  |
| 8 | STATE_C | ZC_SUBSCR_EEP_STE | SUBSCR_EEP_STE_C | No | No | No |  |
| 8 | STATE_C | ZC_TAX_STATE | TAX_STATE_C | No | No | No |  |
| 10 | COUNTY_C | ZC_COUNTY | COUNTY_C | No | No | No |  |
| 10 | COUNTY_C | ZC_COUNTY_2 | COUNTY_2_C | No | No | No |  |
| 10 | COUNTY_C | ZC_COUNTY_OVERTIME | COUNTY_OVERTIME_C | No | No | No |  |
| 11 | COUNTRY_C | ZC_COUNTRY | COUNTRY_C | No | No | No |  |
| 11 | COUNTRY_C | ZC_COUNTRY_2 | COUNTRY_2_C | No | No | No |  |
| 11 | COUNTRY_C | ZC_COUNTRY_4 | COUNTRY_4_C | No | No | No |  |
| 15 | ACTIVE_YN | ZC_PROV_ADDR_ACTIVE | PROV_ADDR_ACTIVE_C | No | No | No |  |
| 18 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 18 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 18 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |

_(167 total; showing first 30)_
