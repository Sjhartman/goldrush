# REFERRAL_ORDER_ID

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=REFERRAL_ORDER_ID

## Description

This table holds the Order ID for orders which EpicCare fills when dropping this referral.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | RFL |
| Release Version | SPRING 2006 |
| May contain EHI? | No |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| REFERRAL_ID | NUMERIC (18,0) | The unique ID of the referral in database. |
| LINE | No | The line number of the change to the referral. For example, if the referral is changed twice, the first change will have a line value of 1, while the second change will have a line value of 2. |
| CM_PHY_OWNER_ID | VARCHAR (25) | ID of the physical deployment owner for this record.  Physical owners will be where the data is hosted, either on the cross-over server or the owner deployment. |
| CM_LOG_OWNER_ID | VARCHAR (25) | ID of the logical deployment owner for this record.  Logical owners show the deployment where the record was created but doesn't represent if the record is a part of version skew. |
| ORDER_ID | NUMERIC (18,0) | Order ID for this referral |

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
| 3 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 4 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 4 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 4 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 5 | ORDER_ID | ADT_ORDERS_ERRORS | ORDER_ID | No | No | No |  |
| 5 | ORDER_ID | ADT_ORDER_INFORMATION | ORDER_ID | No | No | No |  |
| 5 | ORDER_ID | APPT_REQUEST | REQUEST_ID | No | No | No |  |
| 5 | ORDER_ID | CL_ORD_FST_LST_SCH | ORDER_ID | No | No | No |  |
| 5 | ORDER_ID | DENT_ORD_NOADD | ORDER_ID | No | No | No |  |
| 5 | ORDER_ID | DUPMED_DISMISS_HH_INFO | ORDER_ID | No | No | No |  |
| 5 | ORDER_ID | ENDOSCOPY_METRICS | ORDER_ID | Unknown | No | No |  |
| 5 | ORDER_ID | EXTERNAL_ORDER_INFO | ORDER_ID | No | No | No |  |
| 5 | ORDER_ID | F_IMG_STUDY | ORDER_ID | Unknown | Unknown | No |  |

_(94 total; showing first 30)_
