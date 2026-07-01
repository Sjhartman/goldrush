# ORDER_MEDMIXINFO

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=ORDER_MEDMIXINFO

## Description

This table is used to extract ingredient medication information for mixture orders.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | ORD |
| Release Version | MU6 - EPIC 2002 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| ORDER_MED_ID | NUMERIC (18,0) | The unique ID of the medication order (prescription) record. |
| LINE | No | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. Each line represents an ingredient of the mixture. |
| MEDICATION_ID | NUMERIC (18,0) | The unique identifier of a medication record used as an ingredient in the mixture. |
| INGREDIENT_TYPE_C | INTEGER |  |
| MIN_DOSE_AMOUNT | NUMERIC (13,3) | The minimum ordered dose amount of the ingredient. |
| MAX_DOSE_AMOUNT | NUMERIC (13,3) | The maximum ordered dose amount of the ingredient. |
| DOSE_UNIT_C | INTEGER |  |
| FREQUENCY_ID | VARCHAR (18) | The unique identifier of the frequency record associated with the mixture ingredient. |
| MIN_INFUSION_RATE | NUMERIC (13,3) | The minimum infusion rate amount of the ingredient. |
| MAX_INFUSION_RATE | NUMERIC (13,3) | The maximum infusion rate amount of the ingredient. |
| RATE_UNIT_C | INTEGER |  |
| SEPARATE_BAG_YN | VARCHAR (254) |  |
| NONFORMULARY_YN | VARCHAR (254) |  |
| SELECTION | VARCHAR (254) | Indicates the selection status of the ingredient. |
| MIN_CALC_DOSE_AMT | NUMERIC (16,3) | Indicates the minimum calculated dose amount for the ingredient. |
| MAX_CALC_DOSE_AMT | NUMERIC (16,3) | Indicates the maximum calculated dose amount for the ingredient. |
| CALC_DOSE_UNIT_C | INTEGER |  |
| DOSE_CALC_INFO | VARCHAR (1000) | Indicates the calculated steps to get the calculated minimum or maximum calculated dose. |
| CM_PHY_OWNER_ID | VARCHAR (25) | ID of the physical deployment owner for this record.  Physical owners will be where the data is hosted, either on the cross-over server or the owner deployment. |
| CM_LOG_OWNER_ID | VARCHAR (25) | ID of the logical deployment owner for this record.  Logical owners show the deployment where the record was created but doesn't represent if the record is a part of version skew. |
| CALCDOSAMT_PDAY | NUMERIC (13,3) | Calculated dose amount per day. |
| RXM_CALC_AMTUNTPD_C | INTEGER |  |
| RXM_ADDS_VOLUME_YN | VARCHAR (1) |  |
| DOSE_CALC_WARNING | VARCHAR (500) | A warning about whether a medication mixture's final dose was rounded by more than a specified percentage. |
| RXM_ADDS_WT_YN | VARCHAR (1) |  |
| RXM_DISP_QTY | NUMERIC (12,2) | Stores the ordered dispense quantity. |
| RXM_DISP_UNIT_C | INTEGER |  |
| RXM_RATIO | NUMERIC (18,2) | Stores ingredient ratio. |
| RXM_RATIO_UNIT_C | INTEGER |  |
| RXM_DOSE_RND_ACK_C | INTEGER |  |
| COMP_RX_NUM_RAW | VARCHAR (192) | The unformatted prescription numbers for each component in a medication that should be administered with multiple tablets of different strengths. |
| COMP_RX_NUM_FMT | VARCHAR (184) | The formatted prescription numbers for each component in a medication that should be administered with multiple tablets of different strengths. |
| RX_APPLY_OVERFILL_YN | VARCHAR (1) |  |
| COMP_SIG | VARCHAR (3000) | The medication instructions for a single component of a mixture comprised of multiple medications with different tablet strengths. |
| COMP_DISPENSE_TEXT | VARCHAR (50) | This column stores the dispense amount added by a user. |
| MED_MIXTURE_TEXT_TYPE_C | INTEGER |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ORDER_MED_ID | ADT_ORDERS_ERRORS | ORDER_ID | No | No | No |  |
| 1 | ORDER_MED_ID | ADT_ORDER_INFORMATION | ORDER_ID | No | No | No |  |
| 1 | ORDER_MED_ID | APPT_REQUEST | REQUEST_ID | No | No | No |  |
| 1 | ORDER_MED_ID | CL_ORD_FST_LST_SCH | ORDER_ID | No | No | No |  |
| 1 | ORDER_MED_ID | DENT_ORD_NOADD | ORDER_ID | No | No | No |  |
| 1 | ORDER_MED_ID | DUPMED_DISMISS_HH_INFO | ORDER_ID | No | No | No |  |
| 1 | ORDER_MED_ID | ENDOSCOPY_METRICS | ORDER_ID | Unknown | No | No |  |
| 1 | ORDER_MED_ID | EXTERNAL_ORDER_INFO | ORDER_ID | No | No | No |  |
| 1 | ORDER_MED_ID | F_IMG_STUDY | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_MED_ID | F_IP_HSP_SUM_ORDER | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_MED_ID | F_LAB_ORDERS | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_MED_ID | F_MU_OBJ_EH_PLACED_ORDER | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_MED_ID | F_MU_OBJ_EH_RESULTD_ORDER | ORDER_PROC_ID | Unknown | Unknown | No |  |
| 1 | ORDER_MED_ID | F_ONC_PRIOR_AUTH_ORDERS | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_MED_ID | F_OPIOID_ORDERS | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_MED_ID | F_RX_ORDER | ORDER_MED_ID | Unknown | Unknown | No |  |
| 1 | ORDER_MED_ID | HH_MED_ORD_IN_POC_DETAIL | ORDER_MED_ID | No | No | No |  |
| 1 | ORDER_MED_ID | HV_ORDER_PROC | ORDER_PROC_ID | Unknown | No | No |  |
| 1 | ORDER_MED_ID | MED_DETAILS_EXT_ORD | ORDER_ID | No | No | No |  |
| 1 | ORDER_MED_ID | MERCHANDISE_ORDER_INFO | ORDER_ID | Yes | No | No |  |
| 1 | ORDER_MED_ID | MU_EH_QRDA_I_ORDER | ORDER_ID | Unknown | Unknown | No |  |
| 1 | ORDER_MED_ID | ORDERS | ORDER_ID | No | No | No |  |
| 1 | ORDER_MED_ID | ORDER_AUTH_INFO | ORDER_ID | No | No | No |  |
| 1 | ORDER_MED_ID | ORDER_MED | ORDER_MED_ID | Unknown | No | No |  |
| 1 | ORDER_MED_ID | ORDER_MEDINFO | ORDER_MED_ID | Unknown | No | No |  |
| 1 | ORDER_MED_ID | ORDER_MED_2 | ORDER_ID | Unknown | No | No |  |
| 1 | ORDER_MED_ID | ORDER_MED_3 | ORDER_ID | Unknown | No | No |  |
| 1 | ORDER_MED_ID | ORDER_MED_4 | ORDER_ID | Unknown | No | No |  |
| 1 | ORDER_MED_ID | ORDER_MED_5 | ORDER_ID | Unknown | No | No |  |
| 1 | ORDER_MED_ID | ORDER_MED_6 | ORDER_MED_ID | Unknown | No | No |  |

_(101 total; showing first 30)_
