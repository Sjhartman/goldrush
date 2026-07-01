# VERIFICATION

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=VERIFICATION

## Description

The VERIFICATION table contains information about your verification records. These records include verification information for patients, guarantors, coverages, coverage members, hospital accounts, and encounters.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | VRX |
| Release Version | Summer 2009 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| RECORD_ID | NUMERIC (18,0) | The unique identifier (.1 item) for the verification record. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| RECORD_NAME | VARCHAR (200) | The name (.2 item) of the verification record. This is not a meaningful identifier of the person or encounter being verified. |
| RECORD_STATUS_C | INTEGER |  |
| VERIF_RECORD_INI | VARCHAR (3) | INI of the verified record |
| VERIF_RECORD_IDNT | VARCHAR (18) | ID of the verified record. This item is not networked, because it can contain an EPT, EAR, CVG, or HAR ID, depending on the verification type. |
| VERIFICATION_TYPE_C | INTEGER |  |
| VERIF_STATUS_C | VARCHAR (66) |  |
| LAST_VERIF_DATETIME | DATETIME (UTC) | Date and time of the last successful verification |
| LAST_VERIF_USER_ID | VARCHAR (18) | User who performed the most recent verification |
| NEXT_REVIEW_DATE | DATETIME | The date on which the verification status needs review |
| VERIF_CONFRM_ID | VARCHAR (18) | Stores the confirmation record responsible for verifying this record. |
| LAST_STAT_CHNG_DTTM | DATETIME (UTC) | The date on which the status was last changed |
| LAST_CHANGE_USER_ID | VARCHAR (18) | The user who last changed the verification status |
| ENC_PAT_ID | VARCHAR (18) | ID for the patient of this encounter |
| ENC_PAT_VERIF_ID | NUMERIC (18,0) | Verification record for the encounter patient |
| ENC_CSN | NUMERIC (18,0) | Contact Serial Number (CSN) for the patient encounter associated with the verification. Applies to encounter and hospital account verification. |
| ENC_GUARANTOR_ID | NUMERIC (18,0) | Responsible guarantor for this encounter |
| ENC_GUAR_VERIF_ID | NUMERIC (18,0) | Verification record for the guarantor of this encounter |
| ENC_GUAR_SNAPSHOT_C | VARCHAR (66) |  |
| ENC_HOSP_ACCT_ID | NUMERIC (18,0) | Hospital account for this encounter |
| ENC_HAR_VERIF_ID | NUMERIC (18,0) | Verification record of the hospital account for this encounter |
| RECORD_CREATION_DT | DATETIME | Stores the date the record was created |
| INST_OF_UPDATE_DTTM | DATETIME | Stores the instant the record was last locked/unlocked |
| ENC_PAT_SNAPSHOT_C | VARCHAR (66) |  |
| VERIF_SUBTYPE_C | INTEGER |  |
| SUB_PARENT_VRX_ID | NUMERIC (18,0) | The parent verification record of the subtype verification record. |
| SUB_ORIGIN_EAF_ID | NUMERIC (18,0) | The origin EAF ID of the subtype verification record. This could be the location, service area, or facility where the subtypes are defined. |
| LAST_SELF_VERIF_DATE | DATETIME | The date on which the verification status was changed the last time by patient (using the Welcome kiosk). |
| VERIF_RECORD_IDNT_NUMERIC | NUMERIC (18,0) | ID of the verified record if the record's INI has a numeric ID type, or null if the verified record's ID is a string. |

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
| 8 | VERIFICATION_TYPE_C | ZC_VERIFICATION_TY | VERIFICATION_TY_C | No | No | No |  |
| 9 | VERIF_STATUS_C | ZC_CVG_REG_STATUS | CVG_REG_STATUS_C | No | No | No |  |
| 9 | VERIF_STATUS_C | ZC_GUAR_VERIF_STAT | GUAR_VERIF_STAT_C | No | No | No |  |
| 9 | VERIF_STATUS_C | ZC_REG_STATUS | REG_STATUS_C | No | No | No |  |
| 11 | LAST_VERIF_USER_ID | CLARITY_EMP | USER_ID | Unknown | No | No |  |
| 11 | LAST_VERIF_USER_ID | CLARITY_EMP_2 | USER_ID | Unknown | No | No |  |
| 11 | LAST_VERIF_USER_ID | CLARITY_EMP_3 | USER_ID | Unknown | No | No |  |
| 11 | LAST_VERIF_USER_ID | CLARITY_EMP_4 | USER_ID | No | No | No |  |
| 11 | LAST_VERIF_USER_ID | CLARITY_EMP_DEMO | USER_ID | No | No | No |  |
| 11 | LAST_VERIF_USER_ID | EMP_BASIC_INFO | USER_ID | No | No | No |  |
| 11 | LAST_VERIF_USER_ID | EMP_DOC_SETTINGS | USER_NUMBER_ID | No | No | No |  |
| 11 | LAST_VERIF_USER_ID | F_RX_USER | USER_ID | Unknown | Unknown | No |  |
| 11 | LAST_VERIF_USER_ID | IB_MESSAGE_SETTINGS | USER_ID | No | No | No |  |
| 11 | LAST_VERIF_USER_ID | LOGIN_INFO | USER_NUMBER_ID | No | No | No |  |
| 11 | LAST_VERIF_USER_ID | QC_RESULTS_REVIEW | USER_NUMBER_ID | No | No | No |  |
| 11 | LAST_VERIF_USER_ID | USER_SIDEBAR_RPT | USER_NUMBER_ID | Unknown | No | No |  |
| 11 | LAST_VERIF_USER_ID | V_CUBE_D_USER | USER_ID | Unknown | Unknown | No |  |
| 11 | LAST_VERIF_USER_ID | V_CUBE_RX_USER | USER_ID | Unknown | Unknown | No |  |
| 13 | VERIF_CONFRM_ID | CLARITY_HCF | CONFIRMATION_ID | No | No | No |  |
| 15 | LAST_CHANGE_USER_ID | CLARITY_EMP | USER_ID | Unknown | No | No |  |
| 15 | LAST_CHANGE_USER_ID | CLARITY_EMP_2 | USER_ID | Unknown | No | No |  |
| 15 | LAST_CHANGE_USER_ID | CLARITY_EMP_3 | USER_ID | Unknown | No | No |  |

_(280 total; showing first 30)_
