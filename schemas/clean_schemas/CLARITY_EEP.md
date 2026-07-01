# CLARITY_EEP

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=CLARITY_EEP

## Description

This table contains information about employer records from the EEP master file.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | FULL |
| Load Frequency | WEEKLY - FULL |
| Chronicles INI | EEP |
| Release Version | EPIC 2000 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| EMPLOYER_ID | VARCHAR (254) | The unique ID for the employer record. |
| EMPLOYER_NAME | VARCHAR (200) | The name of the employer. |
| ADDRESS1 | VARCHAR (254) | The first line of the street address for the employer. Use the EEP_STREET_ADDRESS table instead to get all lines of this unlimited-line item. |
| ADDRESS2 | VARCHAR (254) | The second line of the street address for the employer. Use the EEP_STREET_ADDRESS table instead to get all lines of this unlimited-line item. |
| CITY | VARCHAR (254) | The city for the employer address. |
| STATE_C | VARCHAR (66) |  |
| ZIP | VARCHAR (50) | The ZIP code for the employer address. |
| PHONE | VARCHAR (50) | The employer contact person's phone number. |
| FAX | VARCHAR (50) | The employer contact person's fax number. |
| CONTACT | VARCHAR (192) | The employer contact person's name. |
| CONTRACT_ID | NUMERIC (18,0) | The unique ID of the pricing contract you have set up with the employer. |
| ACCT_MGR_USER_ID | VARCHAR (18) | The user responsible for this client. |
| IS_VERIFIED | VARCHAR (1) |  |
| STATUS | VARCHAR (12) |  |
| SIC_CODE | VARCHAR (30) |  |
| PRIMARY_LOC_ID | NUMERIC (18,0) | For reporting purposes, ID of the location with which this employer is associated. |
| NUM_EMPLOYEES | INTEGER | For reference, the number of people employed by the employer. |
| CM_PHY_OWNER_ID | VARCHAR (25) | ID of the physical deployment owner for this record. Physical owners will be where the data is hosted, either on the cross-over server or the owner deployment. |
| CM_LOG_OWNER_ID | VARCHAR (25) | ID of the logical deployment owner for this record. Logical owners show the deployment where the record was created but doesn't represent if the record is a part of version skew. |
| COUNTY_C | VARCHAR (66) |  |
| COUNTRY_C | VARCHAR (66) |  |
| HOUSE_NUM | VARCHAR (20) | The house number for the employer address. |
| DISTRICT_C | INTEGER |  |
| EMPLOYER_EIN | VARCHAR (254) | Employer's Federal Tax ID Number |
| REVIEW_DATE | DATETIME | The next review date for this client, only visible to administrators, representing when the employer information and configuration should next be confirmed or updated. |
| EMPLOYER_TYPE_C | INTEGER |  |
| ADMIN_INHERIT_STATUS_YN | VARCHAR (1) |  |
| EMPR_CONTACT_INHERIT_STATUS_C | INTEGER |  |
| WCDEF_INHERIT_STATUS_C | INTEGER |  |
| CVG_SEARCH_INHERIT_STATUS_C | INTEGER |  |
| PARENT_EMPLOYER_ID | VARCHAR (254) | The employer (EEP) record that is to be considered the parent of this employer. This association is meant to model business and institutional relationships such as: - Owner-subsidiary - Government-department - Entity-location  The following can be inherited from the parent employer: - Description - Documents - Billing contact name, address, phone, fax - Account manager - Review date - Admin comments - Workers' Comp coverage defaults - Coverage search options |
| SHARED_CONFIG_EMPLOYER_ID | VARCHAR (254) | The shared billing configuration override (EEP) record for this employer.  The following can be inherited from the shared billing configuration override: - Billing contact name, address, phone, fax - Workers' Comp coverage defaults - Coverage search options |
| CHILD_NAME_PREFIX | VARCHAR (200) | The prefix that should be prepended to the names of all immediate child employers of this employer. |
| INHERIT_NAME_PREFIX | VARCHAR (200) | The name prefix inherited from the parent employer. Used as the original value to identify which part of the child employer's name should be replaced when the parent employer updates the prefix. |
| GEN_INFO_INHERIT_STATUS_YN | VARCHAR (1) |  |
| DOC_INHERIT_STATUS_YN | VARCHAR (1) |  |
| ALLOW_CHILDREN_YN | VARCHAR (1) |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 6 | STATE_C | ZC_ALT_INVOICE_STA | ALT_INVOICE_STA_C | No | No | No |  |
| 6 | STATE_C | ZC_LLB_STATE | LLB_STATE_C | No | No | No |  |
| 6 | STATE_C | ZC_REFG_PROV_STATE | REFG_PROV_STATE_C | No | No | No |  |
| 6 | STATE_C | ZC_STATE | STATE_C | No | No | No |  |
| 6 | STATE_C | ZC_STATE_HISTORY | STATE_HISTORY_C | No | No | No |  |
| 6 | STATE_C | ZC_SUBSCR_EEP_STE | SUBSCR_EEP_STE_C | No | No | No |  |
| 6 | STATE_C | ZC_TAX_STATE | TAX_STATE_C | No | No | No |  |
| 11 | CONTRACT_ID | CLARITY_ECP | CONTRACT_ID | Unknown | No | No |  |
| 12 | ACCT_MGR_USER_ID | CLARITY_EMP | USER_ID | Unknown | No | No |  |
| 12 | ACCT_MGR_USER_ID | CLARITY_EMP_2 | USER_ID | Unknown | No | No |  |
| 12 | ACCT_MGR_USER_ID | CLARITY_EMP_3 | USER_ID | Unknown | No | No |  |
| 12 | ACCT_MGR_USER_ID | CLARITY_EMP_4 | USER_ID | No | No | No |  |
| 12 | ACCT_MGR_USER_ID | CLARITY_EMP_DEMO | USER_ID | No | No | No |  |
| 12 | ACCT_MGR_USER_ID | EMP_BASIC_INFO | USER_ID | No | No | No |  |
| 12 | ACCT_MGR_USER_ID | EMP_DOC_SETTINGS | USER_NUMBER_ID | No | No | No |  |
| 12 | ACCT_MGR_USER_ID | F_RX_USER | USER_ID | Unknown | Unknown | No |  |
| 12 | ACCT_MGR_USER_ID | IB_MESSAGE_SETTINGS | USER_ID | No | No | No |  |
| 12 | ACCT_MGR_USER_ID | LOGIN_INFO | USER_NUMBER_ID | No | No | No |  |
| 12 | ACCT_MGR_USER_ID | QC_RESULTS_REVIEW | USER_NUMBER_ID | No | No | No |  |
| 12 | ACCT_MGR_USER_ID | USER_SIDEBAR_RPT | USER_NUMBER_ID | Unknown | No | No |  |
| 12 | ACCT_MGR_USER_ID | V_CUBE_D_USER | USER_ID | Unknown | Unknown | No |  |
| 12 | ACCT_MGR_USER_ID | V_CUBE_RX_USER | USER_ID | Unknown | Unknown | No |  |
| 16 | PRIMARY_LOC_ID | ANALYTICS_SYSTEM_SETTINGS | FACILITY_ID | No | No | No |  |
| 16 | PRIMARY_LOC_ID | ARPB_SA_SETTINGS | FACILITY_ID | No | No | No |  |
| 16 | PRIMARY_LOC_ID | CLARITY_LOC | LOC_ID | Unknown | No | No |  |
| 16 | PRIMARY_LOC_ID | CLARITY_LOC_2 | LOC_ID | Unknown | No | No |  |
| 16 | PRIMARY_LOC_ID | CLARITY_POS | POS_ID | No | No | No |  |
| 16 | PRIMARY_LOC_ID | CLARITY_POS_2 | POS_ID | No | No | No |  |
| 16 | PRIMARY_LOC_ID | CLARITY_SA | SERV_AREA_ID | Unknown | No | No |  |
| 16 | PRIMARY_LOC_ID | CL_LOC_HIERARCHY | LOC_ID | Unknown | No | No |  |

_(71 total; showing first 30)_
