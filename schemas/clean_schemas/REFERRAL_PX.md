# REFERRAL_PX

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=REFERRAL_PX

## Description

This table contains information on procedures associated with referrals. This table is related to the REFERRAL_ORDER_ID table. The REFERRAL_ORDER_ID table contains the list of procedures for the referral. The REFERRAL_PX table contains information on each of those procedures.

## Metadata

| Property | Value |
| --- | --- |
| Type | View |
| Release Version | EPIC 2000 |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| REFERRAL_ID | NUMERIC (18,0) | The unique ID of the referral in database. |
| LINE | No | The line number of the procedure associated with the referral. For example, if a referral has two associated procedures, the first procedure will have a line value of 1, while the second procedure will have a line value of 2. |
| PX_ID | NUMERIC (18,0) | The unique ID of the procedure associated with the referral. This is frequently used to join to the CLARITY_EAP table. |
| UNITS_REQUESTED | INTEGER | The number of units of this procedure that were requested |
| UNITS_APPROVED | INTEGER | The number of units of this procedure that were approved |
| TOTAL_PRICE | NUMERIC (12,2) | The total price calculated for this procedure using fee schedules or vendor contracts (for outgoing referrals) |
| NET_PAYABLE | NUMERIC (12,2) | The total net payable calculated for this procedure (the price - the patient portion). |
| PATIENT_PORTION | NUMERIC (12,2) | The total patient responsibility calculated for this procedure using the benefits engine |
| PROV_ID | VARCHAR (18) | The ID of the provider who will perform the service |
| AUTH_REQ_YN | VARCHAR (1) | A flag that indicates whether the member's benefits require a referral for this service. Yes=> a referral is required, No=> a referral is not required. |
| COVERED | VARCHAR (24) | A flag that indicates whether the procedure is not covered by the member's benefits or it is covered but by supplemental insurance |
| CM_PHY_OWNER_ID | VARCHAR (25) | The physical owner of the referral. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The logical owner of the referral. |
| REVENUE_CODE_ID | NUMERIC (18,0) | Stores the revenue billing code entered on the service. |
| MODIFIER1_ID | VARCHAR (20) | The unique ID of the modifier record.  This is the first modifier entered for the procedure and affects how the procedure is billed. |
| MODIFIER2_ID | VARCHAR (20) | The unique ID of the modifier record.  This is the second modifier entered for the procedure and affects how the procedure is billed. |
| MODIFIER3_ID | VARCHAR (20) | The unique ID of the modifier record.  This is the third modifier entered for the procedure and affects how the procedure is billed. |
| MODIFIER4_ID | VARCHAR (20) | The unique ID of the modifier record.  This is the fourth modifier entered for the procedure and affects how the procedure is billed. |
| REQ_PER_PERIOD | INTEGER | Requested units/visits per period.  This along with the Requested periods (REQ_PERIODS) determines the total 'requested units'. |
| REQ_FREQ_C | INTEGER |  |
| REQ_PERIODS | INTEGER | Requested periods. Requested units per period (REQ_PER_PERIOD) along with the requested periods determines the total 'requested units'. |
| APPR_PER_PERIOD | INTEGER | Approved units/visits per period. This along with the approved periods (APPR_PERIODS) determines the total 'approved units'. |
| APPR_FREQ_C | INTEGER |  |
| APPR_PERIODS | INTEGER | Approved periods.  Also known as duration. Approved units per period (APPR_PER_PERIOD) along with the approved periods determines the total 'approved units'. |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | REFERRAL_ID | EPA_INFO | REFERRAL_ID | No | Unknown | No |  |
| 1 | REFERRAL_ID | EPA_INFO_2 | REFERRAL_ID | No | Unknown | No |  |
| 1 | REFERRAL_ID | F_REFERRAL_PRICE | REFERRAL_ID | Unknown | Unknown | No |  |
| 1 | REFERRAL_ID | REFERRAL | REFERRAL_ID | Unknown | Unknown | No |  |
| 1 | REFERRAL_ID | REFERRAL_2 | REFERRAL_ID | Unknown | Unknown | No |  |
| 1 | REFERRAL_ID | REFERRAL_3 | REFERRAL_ID | Unknown | Unknown | No |  |
| 1 | REFERRAL_ID | REFERRAL_4 | REFERRAL_ID | Unknown | Unknown | No |  |
| 1 | REFERRAL_ID | REFERRAL_5 | REFERRAL_ID | No | Unknown | No |  |
| 1 | REFERRAL_ID | REFERRAL_6 | REFERRAL_ID | No | Unknown | No |  |
| 1 | REFERRAL_ID | RFL_GROUP_INFO | REFERRAL_ID | No | Unknown | No |  |
| 1 | REFERRAL_ID | V_ECL_REFERRALS | REFERRAL_ID | Unknown | Unknown | No |  |
| 1 | REFERRAL_ID | V_EPA_DATA | REFERRAL_ID | Unknown | Unknown | No |  |
| 1 | REFERRAL_ID | V_HH_REFERRALS | REFERRAL_ID | Unknown | Unknown | No |  |
| 1 | REFERRAL_ID | V_REFERRAL_CYCLE_TIME | REFERRAL_ID | Unknown | Unknown | No |  |
| 1 | REFERRAL_ID | V_VIC_ACCESS_POLICY_TARGETS | REFERRAL_ID | Unknown | Unknown | No |  |
| 3 | PX_ID | CLARITY_EAP | PROC_ID | No | Unknown | No |  |
| 3 | PX_ID | CLARITY_EAP_2 | PROC_ID | No | Unknown | No |  |
| 3 | PX_ID | CLARITY_EAP_3 | PROC_ID | No | Unknown | No |  |
| 3 | PX_ID | CLARITY_EAP_4 | PROC_ID | No | Unknown | No |  |
| 3 | PX_ID | CLARITY_EAP_5 | PROC_ID | No | Unknown | No |  |
| 3 | PX_ID | CLARITY_EAP_IMM | PROC_ID | Unknown | Unknown | No |  |
| 3 | PX_ID | PROC_CONSENT_CONFIG | PROC_ID | No | Unknown | No |  |
| 3 | PX_ID | PROC_UM | PROC_ID | No | Unknown | No |  |
| 3 | PX_ID | V_CUBE_D_PROCEDURE | PROCEDURE_ID | Unknown | Unknown | No |  |
| 9 | PROV_ID | CLARITY_SER | PROV_ID | Unknown | Unknown | No |  |
| 9 | PROV_ID | CLARITY_SER_2 | PROV_ID | Unknown | Unknown | No |  |
| 9 | PROV_ID | CLARITY_SER_3 | PROV_ID | Unknown | Unknown | No |  |
| 9 | PROV_ID | CLARITY_SER_4 | PROV_ID | No | Unknown | No |  |
| 9 | PROV_ID | CLARITY_SER_MYC | PROV_ID | Unknown | Unknown | No |  |
| 9 | PROV_ID | D_PROV_PRIMARY_HIERARCHY | PROV_ID | Unknown | Unknown | No |  |

_(122 total; showing first 30)_
