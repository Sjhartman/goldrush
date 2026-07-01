# REFERRAL_DX

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=REFERRAL_DX

## Description

The REFERRAL_DX table contains diagnosis information stored with referrals.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | RFL |
| Release Version | EPIC 2000 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| REFERRAL_ID | NUMERIC (18,0) | The referral ID for the referral record. |
| LINE | No | The line number of the diagnosis associated with the referral. For example, if a referral has two associated diagnoses, the first diagnosis will have a line value of 1, while the second diagnosis will have a line value of 2. |
| DX_ID | NUMERIC (18,0) | The ID number of the diagnosis associated with the referral. This is not the diagnosis code.  NOTE: Link to CLARITY_EDG to get the diagnosis code. |
| CM_PHY_OWNER_ID | VARCHAR (25) | ID of the physical deployment owner for this record.  Physical owners will be where the data is hosted, either on the cross-over server or the owner deployment. |
| CM_LOG_OWNER_ID | VARCHAR (25) | ID of the logical deployment owner for this record.  Logical owners show the deployment where the record was created but doesn't represent if the record is a part of version skew. |
| DX_TEXT | VARCHAR (254) | Free text associated with each additional diagnosis (I RFL 1000). |
| DX_CODE_TYPE_C | INTEGER |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | REFERRAL_ID | EPA_INFO | REFERRAL_ID | No | No | No |  |
| 1 | REFERRAL_ID | EPA_INFO_2 | REFERRAL_ID | No | No | No |  |
| 1 | REFERRAL_ID | F_REFERRAL_PRICE | REFERRAL_ID | Unknown | Unknown | No |  |
| 1 | REFERRAL_ID | REFERRAL | REFERRAL_ID | Unknown | No | No |  |
| 1 | REFERRAL_ID | REFERRAL_2 | REFERRAL_ID | Unknown | No | No |  |
| 1 | REFERRAL_ID | REFERRAL_3 | REFERRAL_ID | Unknown | No | No |  |
| 1 | REFERRAL_ID | REFERRAL_4 | REFERRAL_ID | Unknown | No | No |  |
| 1 | REFERRAL_ID | REFERRAL_5 | REFERRAL_ID | No | No | No |  |
| 1 | REFERRAL_ID | REFERRAL_6 | REFERRAL_ID | No | No | No |  |
| 1 | REFERRAL_ID | RFL_GROUP_INFO | REFERRAL_ID | No | No | No |  |
| 1 | REFERRAL_ID | V_ECL_REFERRALS | REFERRAL_ID | Unknown | Unknown | No |  |
| 1 | REFERRAL_ID | V_EPA_DATA | REFERRAL_ID | Unknown | Unknown | No |  |
| 1 | REFERRAL_ID | V_HH_REFERRALS | REFERRAL_ID | Unknown | Unknown | No |  |
| 1 | REFERRAL_ID | V_REFERRAL_CYCLE_TIME | REFERRAL_ID | Unknown | Unknown | No |  |
| 1 | REFERRAL_ID | V_VIC_ACCESS_POLICY_TARGETS | REFERRAL_ID | Unknown | Unknown | No |  |
| 3 | DX_ID | ADVERSE_EVENT_TERM_INFO | DX_ID | No | No | No |  |
| 3 | DX_ID | CLARITY_EDG | DX_ID | Unknown | No | No |  |
| 3 | DX_ID | EDG_DBC_INFO | DX_ID | No | No | No |  |
| 3 | DX_ID | V_CUBE_D_DIAGNOSIS | DIAGNOSIS_ID | Unknown | Unknown | No |  |
| 4 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 4 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 4 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 5 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 5 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 5 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 7 | DX_CODE_TYPE_C | ZC_DX_CODE_TYPE | DX_CODE_TYPE_C | No | No | No |  |
