# CUST_SERV_ATCHMENT

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=CUST_SERV_ATCHMENT

## Description

Extracts the attachments for this NCS (customer service) record.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | NCS |
| Release Version | SPRING 2008 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| COMM_ID | NUMERIC (18,0) | The unique ID of the customer service communication record for this row. |
| LINE | No | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| ATCHMENT_USER_ID | VARCHAR (18) | The unique ID associated with the user record for this row. This column is frequently used to link to the CLARITY_EMP table. |
| ATCHMENT_INSTANT | DATETIME (UTC) | The instant that this attachment line was added to the customer service communication record. |
| ATCHMENT_TYPE_C | INTEGER |  |
| ATCHMENT_PAT_ID | VARCHAR (18) | The unique ID of the patient record that is attached to this customer service communication line. |
| ATCHMENT_PT_CSN_ID | NUMERIC (18,0) | The unique contact serial number for the patient encounter that is attached to the customer service communication.  This number is unique across all patient encounters in your system. If you use IntraConnect this is the Unique Contact Identifier (UCI). |
| ATCHMENT_SER_ID | VARCHAR (18) | The unique ID of the provider record that is attached to the customer service communication. |
| ATCHMENT_EMP_GRP_ID | VARCHAR (35) | The unique ID of the employer group record that is attached to the customer service communication. |
| ATCHMENT_VEN_ID | VARCHAR (18) | The unique ID of the vendor record that is attached to the customer service communication. |
| ATCHMENT_MCR_ID | VARCHAR (18) | The unique ID of the carrier record that is attached to the customer service communication. |
| ATCHMENT_REF_ID | NUMERIC (18,0) | The unique ID of the referral record that is attached to the customer service communication. |
| ATCHMENT_CLM_ID | NUMERIC (18,0) | The unique ID of the AP Claim record that is attached to the customer service communication. |
| ATCHMENT_NET_ID | VARCHAR (18) | The unique ID of the network record that is attached to the customer service communication. |
| ATCHMENT_LOC_ID | NUMERIC (18,0) | The unique ID of the location record that is attached to the customer service communication. |
| ATCHMENT_POS_ID | NUMERIC (18,0) | The unique ID of the place of service record that is attached to the customer service communication. |
| ATCHMENT_DEP_ID | NUMERIC (18,0) | The unique ID of the department record that is attached to the customer service communication. |
| ATCHMENT_PBA_ID | VARCHAR (18) | The unique ID of the premium billing account record that is attached to the customer service communication. |
| ATCHMENT_EAR_ID | NUMERIC (18,0) | The unique ID of the account record that is attached to the customer service communication. |
| ATCHMENT_NCS_ID | NUMERIC (18,0) | The unique ID of the customer service communication record that is attached to the customer service communication. |
| ATCHMENT_RSN_C | INTEGER |  |
| ATCHMENT_RSN_CMT | No | The attachment reason comment for the customer service communication attachment. |
| ATCHMENT_HAR_ID | NUMERIC (18,0) | The unique ID of the hospital account record that is attached to the customer service communication. |
| ATCHMENT_CVG_ID | NUMERIC (18,0) | The unique ID of the coverage record that is attached to the customer service communication. |
| ATCHMENT_PROG_ID | VARCHAR (18) | The unique ID of the program record that is attached to the customer service communication. |
| ATCHMENT_ZIP | VARCHAR (50) | The ZIP code that was associated with the attachment when it was added to the customer service communication. |
| ATCHMENT_PROSPECT_ID | NUMERIC (18,0) | The unique ID of the prospective patient record that is attached to the customer service communication. |
| ATCHMENT_CAMPAIGN_ID | NUMERIC (18,0) | The unique ID of the campaign record that is attached to a customer service communication. |
| ATCHMENT_ORDER_ID | NUMERIC (18,0) | Stores relevant order records for this NCS record. |
| ATCHMENT_ESTIMATE_ID | NUMERIC (18,0) | The unique ID of the estimate record that is attached to the customer service communication. |
| ATCHMENT_DOCUMENT_ID | VARCHAR (18) | The unique ID of the document record that is attached to this customer service communication line. |
| ATCHMENT_CLAIM_RECON_ID | VARCHAR (18) | The unique ID of the rejected claim record that is attached to the customer service communication. |
| ATCHMENT_RESEARCH_ID | VARCHAR (18) | The unique ID of the research study record that is attached to the customer service communication. |
| ATCHMENT_STAGING_RECORD_ID | NUMERIC (18,0) | The unique ID of the member transaction record that is attached to the customer service communication. |
| ATCHMENT_APPEAL_GRV_ID | NUMERIC (18,0) | Stores relevant appeal or grievance record for this row. |
| ATCHMENT_AUTH_REQUEST_ID | NUMERIC (18,0) | Stores relevant authorization requests for CRM |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | COMM_ID | CUST_SERVICE | COMM_ID | Unknown | No | No |  |
| 1 | COMM_ID | CUST_SERVICE_2 | COMM_ID | No | No | No |  |
| 1 | COMM_ID | CUST_SERVICE_TRANSFER | COMM_ID | No | No | No |  |
| 1 | COMM_ID | CUST_SERV_ORG_FILTER_SA | COMM_ID | No | No | No |  |
| 1 | COMM_ID | V_ADT_TC_DEST | COMM_ID | Unknown | Unknown | No |  |
| 1 | COMM_ID | V_ADT_TRANSFER_CENTER | COMM_ID | Unknown | Unknown | No |  |
| 3 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 4 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 4 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 4 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 5 | ATCHMENT_USER_ID | CLARITY_EMP | USER_ID | Unknown | No | No |  |
| 5 | ATCHMENT_USER_ID | CLARITY_EMP_2 | USER_ID | Unknown | No | No |  |
| 5 | ATCHMENT_USER_ID | CLARITY_EMP_3 | USER_ID | Unknown | No | No |  |
| 5 | ATCHMENT_USER_ID | CLARITY_EMP_4 | USER_ID | No | No | No |  |
| 5 | ATCHMENT_USER_ID | CLARITY_EMP_DEMO | USER_ID | No | No | No |  |
| 5 | ATCHMENT_USER_ID | EMP_BASIC_INFO | USER_ID | No | No | No |  |
| 5 | ATCHMENT_USER_ID | EMP_DOC_SETTINGS | USER_NUMBER_ID | No | No | No |  |
| 5 | ATCHMENT_USER_ID | F_RX_USER | USER_ID | Unknown | Unknown | No |  |
| 5 | ATCHMENT_USER_ID | IB_MESSAGE_SETTINGS | USER_ID | No | No | No |  |
| 5 | ATCHMENT_USER_ID | LOGIN_INFO | USER_NUMBER_ID | No | No | No |  |
| 5 | ATCHMENT_USER_ID | QC_RESULTS_REVIEW | USER_NUMBER_ID | No | No | No |  |
| 5 | ATCHMENT_USER_ID | USER_SIDEBAR_RPT | USER_NUMBER_ID | Unknown | No | No |  |
| 5 | ATCHMENT_USER_ID | V_CUBE_D_USER | USER_ID | Unknown | Unknown | No |  |
| 5 | ATCHMENT_USER_ID | V_CUBE_RX_USER | USER_ID | Unknown | Unknown | No |  |
| 7 | ATCHMENT_TYPE_C | ZC_ATCHMENT_REC_TY | ATCHMENT_REC_TY_C | No | No | No |  |
| 8 | ATCHMENT_PAT_ID | ANTICOAG_SELF_REGULATING | PAT_ID | No | No | No |  |
| 8 | ATCHMENT_PAT_ID | CARE_COORDINATION | PAT_ID | Unknown | No | No |  |
| 8 | ATCHMENT_PAT_ID | CLAIMS_DERIVE_PAT_FLAGS | PAT_ID | No | No | No |  |

_(500 total; showing first 30)_
