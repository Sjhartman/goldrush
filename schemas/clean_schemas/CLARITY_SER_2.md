# CLARITY_SER_2

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=CLARITY_SER_2

## Description

This table contains high-level information about your provider records.

**Overflow table** for CLARITY_SER (127 cols). Contains additional columns for the same records — join on the shared primary key column.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | SER |
| Release Version | Summer 2009 |
| May contain EHI? | No |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| PROV_ID | VARCHAR (18) | The unique ID associated with the provider record for this row. This column is frequently used to link to the CLARITY_SER table. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| IP_ORD_PROV_YN | VARCHAR (1) |  |
| DEF_LETTER_PREF_C | INTEGER |  |
| DEF_CHART_STATN_ID | VARCHAR (18) | The unique ID of the deficiency chart station specified for the provider. |
| HOME_CITY | VARCHAR (254) | The city of the provider's home address. Lines of the provider's home address are found in the PROV_HOME_ADDR table. |
| HOME_STATE_C | VARCHAR (66) |  |
| HOME_ZIP | VARCHAR (50) | The ZIP code of the provider's home address. Lines of the provider's home address are found in the PROV_HOME_ADDR table. |
| PREVENT_REASGN_YN | VARCHAR (1) |  |
| LAB_PRINTER_ID | NUMERIC (18,0) | The unique ID of the printer that will be used to route paper result reports from the lab. |
| POS_DEV_TYP_C | VARCHAR (66) |  |
| CREATING_PATIENT_ID | VARCHAR (18) | The unique ID of the patient record that this record was created from. This column is frequently used to link to the PATIENT table. |
| REL_DT_OFST | INTEGER | This is a number that indicates how many days, weeks, or months in the future the provider's template will remain open for scheduling, in conjunction with REL_DT_OFST_TF_C. |
| REL_DT_OFST_TF_C | INTEGER |  |
| NON_PERSON_YN | VARCHAR (1) |  |
| RES_SUP_PROV_ID | VARCHAR (18) | The supervisor for a resident. |
| DICOM_AET_DEF_ID | NUMERIC (18,0) | The linked DICOM Definition (AE Title) record of the provider. This is used in Modality Worklist Queries by AE Title. |
| GRP_OR_SITE_C | VARCHAR (66) |  |
| TPL_PROV_YN | VARCHAR (1) |  |
| PANEL_FACTOR | NUMERIC (18,2) | The provider's panel factor. |
| PANEL_WEIGHT | NUMERIC (18,2) | The provider's panel weight. |
| PANEL_STATUS_C | VARCHAR (66) |  |
| AUTO_GEN_OR_TEMP_YN | VARCHAR (1) |  |
| OVRIDE_SYS_MEAS_YN | VARCHAR (1) |  |
| CREATED_ON_FLY_YN | VARCHAR (1) |  |
| OOO_POOL_HIP_ID | NUMERIC (18,0) | The ID of the InBasket pool that receives the provider's InBasket messages while the provider is out of the office. |
| PREFRD_COMM_MTHD_C | INTEGER |  |
| RECV_ENCREP_POOL_ID | NUMERIC (18,0) | When an encounter report is sent to a provider from the Communication Management section of your navigator or Managed Access, this setting determines who receives the In Basket message.  You can send the encounter report to In Basket pools in addition to or instead of the provider.  If  any Pools are specified here, you can omit the provider from the list of recipients by specifying "No" in the "Send to provider also?" field. |
| ENCREP_PROV_YN | VARCHAR (1) |  |
| MOD_CRT_FLMS_C | VARCHAR (66) |  |
| CREATING_USER_ID | VARCHAR (18) | The unique ID of the user who created this provider record. |
| SURG_AUTH_UPD_DTTM | DATETIME (Local) | This column will store the last instant that the surgeon's authorizations have been updated. It will be used by the batch that auto-creates user-specific preference lists based on the surgeons' authorizations to determine when the preference list will need to be updated. |
| RESIDENT_FOR_TRA_YN | VARCHAR (1) |  |
| IP_DEFAULT_TT_REL_C | VARCHAR (66) |  |
| INP_DISCIPLINE_ID | VARCHAR (18) | Inpatient provider discipline. |
| IGNORE_DEPT_ROUT_YN | VARCHAR (1) |  |
| EREFIL_MSG_POOL_ID | NUMERIC (18,0) | The Id of the message pool to receive ePrescription reports for medication orders that are sent through an ePrescription interface by this provider. |
| PLACE_OF_BIRTH | VARCHAR (254) | Specifies the place of birth in the provider database. |
| PAT_AGE_FROM | INTEGER | Specifies the youngest age of patients to which this provider would prefer to be assigned. |
| PAT_AGE_TO | INTEGER | Specifies the oldest age of patients to which this provider would prefer to be assigned. |
| AUTO_INT_RFL_APR_YN *(deprecated)* | VARCHAR (1) |  |
| AUTO_INT_RFL_AMT *(deprecated)* | NUMERIC (18,2) | *** Deprecated *** Discontinued item ****** In table CLARITY_SER_2, the column AUTO_INT_RFL_AMT (SER/18020) has been deprecated. Specifies the dollar amount up to which Tapestry will auto approve Internal referrals from this provider. |
| AUTO_EXT_RFL_APR_YN *(deprecated)* | VARCHAR (1) |  |
| AUTO_EXT_RFL_AMT *(deprecated)* | NUMERIC (18,2) | *** Deprecated *** Discontinued item ****** In table CLARITY_SER_2, the column AUTO_EXT_RFL_AMT (SER/18040) has been deprecated. Specifies the dollar amount up to which Tapestry will auto approve Outgoing referrals from this provider. |
| RECRUITMENT_SRC_C | INTEGER |  |
| UTILIZTN_METRIC_C | VARCHAR (66) |  |
| UTILIZTN_COMMENT | VARCHAR (254) | Specifies the utilization comment in the provider database. |
| DC_SENT_DATETIME | DATETIME (Local) | The instant when the provider record was sent using Data Courier to another deployment. |
| SURG_PRIMARY_SVC_C | VARCHAR (66) |  |
| COLL_RES_EXPR_YN | VARCHAR (1) |  |
| PAT_REVIEW_METRIC_C | VARCHAR (66) |  |
| PROV_GROUP_C | VARCHAR (66) |  |
| RECORD_CREATION_DT | DATETIME | The date the provider/resource was created |
| REPLACEMNT_PROV_ID | VARCHAR (18) | The replacement provider who will take care of this provider's duties in case of temporary or permanent absence. |
| ADMIN_ROLE_C | VARCHAR (66) |  |
| RESOURCE_TYPE_C | INTEGER |  |
| RSLT_ROUT_TYPE_C | INTEGER |  |
| NPI | VARCHAR (10) | The provider's National Provider Identifier (NPI). This is a 10 digit numeric identifier issued to providers by the Centers for Medicare and Medicaid Services. |
| INP_LICENSURE_C | INTEGER |  |
| EPRESC_CNTRLD_YN | VARCHAR (1) |  |
| EPCS_ALLOW_SSN_YN | VARCHAR (1) |  |
| TAP_CLMS_RESRC_YN | VARCHAR (1) |  |
| CUR_CRED_C | INTEGER |  |
| BRANCH_OF_SERVICE_C | INTEGER |  |
| ASGN_MIL_UNIT_ID | NUMERIC (18,0) | The unique ID of the military unit that is associated with the provider. |
| MILITARY_RANK_C | INTEGER |  |
| ALLOW_REFER_TO_YN | VARCHAR (1) |  |
| SERVICE_DEFAULT_C | VARCHAR (66) |  |
| IS_RESIDENT_C | INTEGER |  |
| REL_DT_PAST_TMPL_YN | VARCHAR (1) |  |
| PECOS_STATUS_YN *(deprecated)* | VARCHAR (3) |  |
| DBC_DFLT_RFL_SA_ID | NUMERIC (18,0) | The unique ID of the provider's default referring service area for DBCs. This is populated only for internal providers and only in the Netherlands. |
| ALT_ID | VARCHAR (192) | Alternate ID for the provider. |
| UNVERIFIED_REASON_C | INTEGER |  |
| A_PLACE_YN | VARCHAR (1) |  |
| DC_CAN_RESEND_YN | VARCHAR (1) |  |
| NOTE_SERVICE_DEFAULT_C | VARCHAR (66) |  |
| PRIMARY_DEPT_ID | NUMERIC (18,0) | The provider's primary department. This is equivalent to line 1 of CLARITY_SER_DEPT. |
| AUTH_ALL_LOCS_YN | VARCHAR (1) |  |
| GENERIC_YN | VARCHAR (1) |  |
| TR_SKIP_SAT_YN | VARCHAR (1) |  |
| TR_SKIP_SUN_YN | VARCHAR (1) |  |
| TR_SKIP_HOL_YN | VARCHAR (1) |  |
| RELEASE_TIME | DATETIME (Local) | The time of day in which block release settings using the day interval (from I SER 5353) will release. |
| INSTANT_OF_UPDATE_DTTM | DATETIME (Local) | The instant when the provider record was last locked or unlocked before this row was extracted. Changes to the instant of update do not trigger a Clarity extract, so values in this column may not represent the current value in Chronicles. |
| PALL_CARE_PROV_YN | VARCHAR (1) |  |
| PROFESSIONAL_GRP_C | INTEGER |  |
| DUTCH_AGB_CODE | VARCHAR (40) | The provider's Algemeen Gegevens Beheer (AGB) code. The AGB code is an 8-digit numeric identifier issued to providers as the Dutch national provider ID. |
| UDS_PROV_TYPE_C | INTEGER |  |
| APPT_TIME_TBD_YN | VARCHAR (1) |  |
| APPT_TBD_RECALC_YN | VARCHAR (1) |  |
| OFFICE_1_RAR_FAX | VARCHAR (192) | The refill authorization request fax number of the provider's primary office location. |
| ANES_SVC_PROV_GRP_C | VARCHAR (66) |  |
| MIPS_EC_YN | VARCHAR (1) |  |
| MIPS_IMG_ENC_C | INTEGER |  |
| MIPS_QM_METHOD_C | INTEGER |  |
| ADT_ADMT_PROVIDER_YN | VARCHAR (1) |  |
| ADT_ATTN_PROVIDER_YN | VARCHAR (1) |  |
| PROCEDURAL_ROOM_YN | VARCHAR (1) |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | PROV_ID | CLARITY_SER | PROV_ID | Unknown | No | No |  |
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
| 2 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 2 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 2 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 3 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 5 | DEF_LETTER_PREF_C | ZC_DEF_LETTER_PREF | DEF_LETTER_PREF_C | No | No | No |  |
| 6 | DEF_CHART_STATN_ID | CT_STATION | STATION_ID | Unknown | No | No |  |
| 8 | HOME_STATE_C | ZC_ALT_INVOICE_STA | ALT_INVOICE_STA_C | No | No | No |  |
| 8 | HOME_STATE_C | ZC_LLB_STATE | LLB_STATE_C | No | No | No |  |
| 8 | HOME_STATE_C | ZC_REFG_PROV_STATE | REFG_PROV_STATE_C | No | No | No |  |
| 8 | HOME_STATE_C | ZC_STATE | STATE_C | No | No | No |  |
| 8 | HOME_STATE_C | ZC_STATE_HISTORY | STATE_HISTORY_C | No | No | No |  |
| 8 | HOME_STATE_C | ZC_SUBSCR_EEP_STE | SUBSCR_EEP_STE_C | No | No | No |  |
| 8 | HOME_STATE_C | ZC_TAX_STATE | TAX_STATE_C | No | No | No |  |
| 11 | LAB_PRINTER_ID | PRINTERS | PRINT_DEVICE_ID | No | No | No |  |
| 11 | LAB_PRINTER_ID | PRINTERS_CE_OWNERS | PRINT_DEVICE_ID | No | No | No |  |
| 12 | POS_DEV_TYP_C | ZC_OR_PAT_POS_DEV_TYPE | OR_PAT_POS_DEV_TYPE_C | No | No | No |  |

_(190 total; showing first 30)_
