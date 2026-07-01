# ALT_HISTORY_2

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=ALT_HISTORY_2

## Description

This table contains general history information for each type of medication warning or advisory. Since each warning could be triggered in different activities at different times, it contains general warning information for each time the warning was triggered. This table is an extension of ALT_HISTORY table.

**Overflow table** for ALT_HISTORY (101 cols). Contains additional columns for the same records — join on the shared primary key column.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | ALT |
| Release Version | Rel 2014 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| ALT_ID | NUMERIC (18,0) | The unique identifier for the med alert record. |
| ALT_CSN_ID | NUMERIC (18,0) | A unique serial number for this contact. This number is unique across all alerts in the system. |
| FILTEROUT_REASON_C | INTEGER |  |
| DUP_ALERT_ING_C | INTEGER |  |
| DUP_ALERT_GROUP_C | INTEGER |  |
| VENDOR_EXTERNAL_ID | VARCHAR (50) | Indicates the corresponding vendor external ID of the warning. |
| BPA_ACK_LPP_ID *(deprecated)* | NUMERIC (18,0) |  |
| PAT_COND_CHK_SEV_C | INTEGER |  |
| TPN_VOL_INFUSED | NUMERIC (18,2) | It is possible to calculate warnings for total parenteral nutrition (TPN) based on the total volume present in the bag or the volume based upon how much the patient will actually receive. If the volume to be infused to the patient is being calculated, then this item will store the volume to be infused at the time that a TPN alert fired. If the warning is based on the volume in the TPN bag, then this item will not be set. |
| ACT_TKN_INST_DTTM | DATETIME (Attached) | This item records the instant that an advisory follow-up action was taken. |
| INGREDIENT_LINE *(deprecated)* | INTEGER |  |
| STUDY_CONTAINER_ID | NUMERIC (18,0) | The unique ID of the container used for investigational medications that is associated with alert record. |
| BPA_TRGR_DV_DT_YN | VARCHAR (1) |  |
| PREG_ALRT_SEV_DK_C | INTEGER |  |
| LACT_ALRT_SEV_DK_C | INTEGER |  |
| CONTACT_DATE_REAL | FLOAT | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| COMPLETE_BPA_ORIGINAL_CSN_ID | NUMERIC (18,0) | When completing an advisory in In Basket, this column stores the CSN of the advisory firing that originally sent the In Basket message. |
| CRIT_DOSE_POPUP_YN | VARCHAR (1) |  |
| LOCATOR_FAILED_YN | VARCHAR (1) |  |
| DUP_ALT_COMBINED_YN | VARCHAR (1) |  |
| BPA_ACK_LOCKOUT_TM_FLOAT | FLOAT | The lockout time associated with the acknowledge reason chosen in the advisory. |
| HARD_STOP_YN | VARCHAR (1) |  |
| DRUGSTUDY_SEVERITY_C | INTEGER |  |
| MEDBASE_DRUG_DRUG_SEVERITY_C | INTEGER |  |
| MEDBASE_DRUG_DRUG_DOC_LEVEL_C | INTEGER |  |
| BPA_DISPLAY_MODE_C | INTEGER |  |
| USER_PLATFORM_C | INTEGER |  |
| FI_LACTATION_SEVERITY_C | INTEGER |  |
| FI_PREGNANCY_SEVERITY_C | INTEGER |  |
| FI_GERIATRIC_SEVERITY_C | INTEGER |  |
| ALLERGY_CERTAINTY_C | INTEGER |  |
| NET_BPA_SAVINGS | NUMERIC (18,2) | The estimated net savings to the organization for this OurPractice Advisory. |
| HCI_SEVERITY_LEVEL_C | INTEGER |  |
| BPA_ACT_FSD_ID *(deprecated)* | VARCHAR (18) |  |
| BPA_ACT_FLO_DISP *(deprecated)* | VARCHAR (254) |  |
| BPA_ACT_FLO_FREQ_C *(deprecated)* | INTEGER |  |
| BPA_ACT_TEMPLATE_ID *(deprecated)* | VARCHAR (18) |  |
| WAS_FORCED_SCROLL_YN | VARCHAR (1) |  |
| DD_INT_NUMERIC_SEV | INTEGER | Stores the numeric severity level of the interaction at the time it fired. |
| ATAH_WARNING_IDNT | VARCHAR (254) | This item stores the warning ID for a medication warning that appeared based on warning response data from the ATAH decision support service provided by Trifork. |
| ATAH_DRUG_DRUG_TYPE_C | INTEGER |  |
| ATAH_RENAL_TYPE_C | INTEGER |  |
| ATAH_PEDIATRIC_TYPE_C | INTEGER |  |
| ATAH_DRUG_DISEASE_TYPE_C | INTEGER |  |
| ATAH_SPECIFIC_WARNING_IDNT | VARCHAR (180) | This item contains the specific portion of the warning ID from a warning provided by the ATAH decision support that represents the nature of the specific warning. It does not contain the information from the full warning ID that describes the module type, specific warning type, and API version, and can be used to identify a specific warning and assist with managing medication warnings. |
| ATAH_SEVERITY_C | INTEGER |  |
| ATAH_DUPLICATE_TYPE_C | INTEGER |  |
| ATAH_DRUG_ALLERGY_TYPE_C | INTEGER |  |
| BPA_CARD_ID | VARCHAR (254) | This item contains the card ID which is used to distinguish between those cards or sub advisories. |
| ACK_BTN_CAPTION | VARCHAR (254) | The acknowledge reason button caption. This item is populated from LGL  4015 at the time the ALT contact is created. |
| BPA_DEF_TRIGGER_C | INTEGER |  |
| CDSHKS_FB_STAT_C | INTEGER |  |
| ATAH_DOSE_TYPE_C | INTEGER |  |
| NBA_ACTION_UTC_DTTM | DATETIME (UTC) | The instant of an next best action event. |
| NBA_USER_ID | VARCHAR (18) | The user correlated with this next best action event. |
| NBA_DEPARTMENT_ID | NUMERIC (18,0) | The department correlated with this next best action event. |
| NBA_RESULT_C | INTEGER |  |
| NBA_DFR_REASON_C | INTEGER |  |
| NBA_DFR_DAYS_NUM | INTEGER | The defer days correlated with this next best action event. |
| NBA_DEC_REASON_C | INTEGER |  |
| NBA_COMM_ID | VARCHAR (45) | The contact correlated with this next best action event. |
| NBA_BUSINESS_SEG_ID | NUMERIC (18,0) | The next best action was performed in this business segment. |
| NBA_ACTION_DTTM | DATETIME (Local) | The instant of a next best action event in local time. |
| ATAH_PREGNANCY_TYPE_C | INTEGER |  |
| ATAH_LACTATION_TYPE_C | INTEGER |  |
| ACK_DYNAMIC_CODE | VARCHAR (100) | For an acknowledgement reason generated dynamically from a third party system, this item stores the code for the reason returned by the third party. |
| ACK_DYNAMIC_CODESYS | VARCHAR (254) | For an acknowledgement reason generated dynamically from a third party system, this item stores the code system for the reason returned by the third party. |
| DRUG_INT_FEST_REL_C | INTEGER |  |
| DRUG_INT_FEST_SRC_C | INTEGER |  |
| BPA_FBK_IB_MSG_ID | VARCHAR (18) | The EOW ID of the feedback type In Basket message sent for this advisory's feedback. |
| BPA_FBK_C | INTEGER |  |
| BPA_FBK_CMT | VARCHAR (500) | Captures free text feedback comments on the advisory |
| ATAH_INDICATIONS_TYPE_C | INTEGER |  |
| MYC_TICKLER_AUDIT_CSN_ID | NUMERIC (18,0) | The CSN of the RCH record containing the auditing data of the tickler sent for this alert. |
| ACTION_IDENT | INTEGER | Action ID for the warning that fired. |
| BPA_ACT_PREG_STAT_C *(deprecated)* | INTEGER |  |
| BPA_ACT_PREG_FREQ_C *(deprecated)* | INTEGER |  |
| ATAH_SEVERITY_SUBTYPE_C | INTEGER |  |
| ATAH_SEVERITY_FREE_TEXT | VARCHAR (254) | This item contains a free-text representation of the severity of a medication warning from Trifork's medication decision support service. It contains text when the "free text" value is set in the corresponding discrete severity item. |
| ATAH_SEVERITY_SUBTYPE_FREETEXT | VARCHAR (254) | This item contains a free-text representation of the severity subtype of a medication warning from Trifork's medication decision support service. It contains text when the "free text" value is set in the corresponding discrete severity subtype item. |
| ATAH_MONITORING_TYPE_C | INTEGER |  |
| ERROR_MESSAGE | VARCHAR (500) | Error message, if any, that is associated with the warning. |
| ORD_VALID_WORKFLOW_C | INTEGER |  |
| ALT_ACTION_INST_LOCAL_DTTM | DATETIME (Attached) | The instant of alert, converted to local time |
| ORD_VALID_LPR_NAME | VARCHAR (100) | The name of the profile that the order validation came from. |
| ATAH_MESSAGE_IDENTIFIER | VARCHAR (100) | The message ID that was passed to the decision support service to check for medication warnings. |
| ST_STANDARD_C | INTEGER |  |
| ST_COMPREHENSIVE_C | INTEGER |  |
| BPA_ADDL_FACTORS_TEXT | VARCHAR (4000) | Snapshot of data relevant to the evaluation of the advisory, in the format of plain text. |
| BPA_ADDL_FACTORS_UTC_DTTM | DATETIME (UTC) | The instant that the additional contributing factors text (I ALT 2200) was created. |
| ALRGY_FROM_OUTSIDE_SRC_YN | VARCHAR (1) |  |
| OPA_SENT_ADVISORY_YN | VARCHAR (1) |  |
| LOG_HM_ACTION_C | INTEGER |  |
| LOG_HMT_PPN_RSN_C | INTEGER |  |
| LOG_HM_TYPE_C | INTEGER |  |
| LOG_HM_EDIT_RSN_C | INTEGER |  |
| LOG_HM_COMP_TYPE_C | INTEGER |  |
| NBA_ACT_IMPORTANCE_LVL_C | INTEGER |  |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| B-TREE INDEX | EIX_ALT_HISTORY_2__ALT_ID | ALT_ID | 1 | Yes | Yes |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ALT_ID | ALERT | ALT_ID | No | No | No |  |
| 2 | ALT_CSN_ID | ALT_DRUG_AGE | ALT_CSN_ID | Unknown | Unknown | No |  |
| 2 | ALT_CSN_ID | ALT_DRUG_ALLERGY | ALT_CSN_ID | Unknown | Unknown | No |  |
| 2 | ALT_CSN_ID | ALT_DRUG_DFALC | ALT_CSN_ID | Unknown | Unknown | No |  |
| 2 | ALT_CSN_ID | ALT_DRUG_DISEASE | ALT_CSN_ID | Unknown | Unknown | No |  |
| 2 | ALT_CSN_ID | ALT_DRUG_DUPTHERPY | ALT_CSN_ID | Unknown | Unknown | No |  |
| 2 | ALT_CSN_ID | ALT_DRUG_IV | ALT_CSN_ID | Unknown | Unknown | No |  |
| 2 | ALT_CSN_ID | ALT_DRUG_LACTATION | ALT_CSN_ID | Unknown | Unknown | No |  |
| 2 | ALT_CSN_ID | ALT_DRUG_PREGNANCY | ALT_CSN_ID | Unknown | Unknown | No |  |
| 2 | ALT_CSN_ID | ALT_DRUG_TPN | ALT_CSN_ID | Unknown | Unknown | No |  |
| 2 | ALT_CSN_ID | ALT_HISTORY | ALT_CSN_ID | No | No | No |  |
| 2 | ALT_CSN_ID | ALT_HISTORY_3 | ALT_CSN_ID | No | No | No |  |
| 2 | ALT_CSN_ID | F_IP_HSP_ALERT | ALERT_CSN_ID | Unknown | Unknown | No |  |
| 2 | ALT_CSN_ID | F_RX_OE_DRUG_WARNINGS | ALT_CSN_ID | Unknown | Unknown | No |  |
| 2 | ALT_CSN_ID | V_CUBE_F_ALERT | ALERT_CSN_ID | Unknown | Unknown | No |  |
| 2 | ALT_CSN_ID | V_DRUG_WARNINGS | ALT_CSN_ID | Unknown | Unknown | No |  |
| 3 | FILTEROUT_REASON_C | ZC_FILTEROUT_REASON | FILTEROUT_REASON_C | No | Yes | No |  |
| 4 | DUP_ALERT_ING_C | ZC_CHEMICAL | CHEMICAL_C | No | Yes | No |  |
| 5 | DUP_ALERT_GROUP_C | ZC_PHARM_SUBCLASS | PHARM_SUBCLASS_C | No | Yes | No |  |
| 8 | PAT_COND_CHK_SEV_C | ZC_PAT_COND_CHK_SEV | PAT_COND_CHK_SEV_C | No | Yes | No |  |
| 12 | STUDY_CONTAINER_ID | STUDY_CONTAINER | ID | No | Yes | No |  |
| 14 | PREG_ALRT_SEV_DK_C | ZC_DK_PREG_SEVERITY | DK_PREG_SEVERITY_C | No | Yes | No |  |
| 15 | LACT_ALRT_SEV_DK_C | ZC_DK_LACT_SEVERITY | DK_LACT_SEVERITY_C | No | Yes | No |  |
| 17 | COMPLETE_BPA_ORIGINAL_CSN_ID | ALT_DRUG_AGE | ALT_CSN_ID | Unknown | Unknown | No |  |
| 17 | COMPLETE_BPA_ORIGINAL_CSN_ID | ALT_DRUG_ALLERGY | ALT_CSN_ID | Unknown | Unknown | No |  |
| 17 | COMPLETE_BPA_ORIGINAL_CSN_ID | ALT_DRUG_DFALC | ALT_CSN_ID | Unknown | Unknown | No |  |
| 17 | COMPLETE_BPA_ORIGINAL_CSN_ID | ALT_DRUG_DISEASE | ALT_CSN_ID | Unknown | Unknown | No |  |
| 17 | COMPLETE_BPA_ORIGINAL_CSN_ID | ALT_DRUG_DUPTHERPY | ALT_CSN_ID | Unknown | Unknown | No |  |
| 17 | COMPLETE_BPA_ORIGINAL_CSN_ID | ALT_DRUG_IV | ALT_CSN_ID | Unknown | Unknown | No |  |
| 17 | COMPLETE_BPA_ORIGINAL_CSN_ID | ALT_DRUG_LACTATION | ALT_CSN_ID | Unknown | Unknown | No |  |

_(154 total; showing first 30)_
