# MDS_RECS

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=MDS_RECS

## Description

This table contains data on Minimum Data Set (MDS) assessments. An MDS assessment is represented by a Registry Data (RDI) record with a Registry Type (I RDI 26) value of Minimum Data Set.

**Primary table** in this group (101 cols). Overflow siblings joined on shared key: MDS_RECS_2 (7 cols). Prefer this table for most queries.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | RDI |
| Release Version | Rel 2014 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| REGISTRY_DATA_ID | NUMERIC (18,0) | The unique identifier (.1 item) for the registry data record. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| RECORD_STATUS_C | INTEGER |  |
| REGISTRY_ID | NUMERIC (18,0) | This column contains the ID of the registry definition (HFR) that configures the MDS abstraction. |
| REGISTRY_TYPE_C | INTEGER |  |
| PAT_ID | VARCHAR (18) | This column contains the associated patient's ID (EPT .1). |
| ARD_TARGET_DATE | DATETIME | This column contains the Target Date or Assessment Reference Date. |
| CUR_STAT_C | INTEGER |  |
| CUR_STAT_USER_ID | VARCHAR (18) | This items stores the ID of the user who set the current status (RDI-10024).  RDI-40011 stores the instant the item was set. |
| CUR_STAT_DTTM | DATETIME (UTC) | This item stores the instant the current status (RDI-10024) was set.  RDI-40010 stores the user who set it. |
| MDS_REC_TYPE_C | VARCHAR (66) |  |
| ARD_USER_ID | VARCHAR (18) | Stores the user who most recently documented the target date for the assessment - ARD, discharge date, or entry date (RDI 101) - MDS A2300. |
| ARD_DTTM | DATETIME (UTC) | Stores the most recent instant that the target date (ARD, entry date or discharge date) was documented - MDS A2300. |
| MDS_REC_TYPE_USER_ID | VARCHAR (18) | Stores the most recent user to document RDI 35000 (MDS A0050) |
| MDS_REC_TYPE_DTTM | DATETIME (UTC) | Stores the most recent instant that RDI 35000 (MDS A0050) was documented |
| OBRA_TYPE_C | VARCHAR (66) |  |
| OBRA_TYPE_USER_ID | VARCHAR (18) | Stores the last user to document the MDS Federal OBRA Reason for Assessment (RDI 35010) - A0310A. |
| OBRA_TYPE_DTTM | DATETIME (UTC) | Most recent instant of documentation for Federal OBRA Reason for Assessment (RDI 35010) - MDS A0310A. |
| PPS_TYPE_C | VARCHAR (66) |  |
| PPS_TYPE_USER_ID | VARCHAR (18) | Stores the most recent user to document the type of PPS Assessment (RDI 35011) - MDS A0310B. |
| PPS_TYPE_DTTM | DATETIME (UTC) | Stores the most recent instant that the federal submission requirement was documented (RDI 35011) - MDS A0310B. |
| OMRA_TYPE_C | VARCHAR (66) |  |
| OMRA_TYPE_USER_ID | VARCHAR (18) | Inidcates the user who last documented PPS OMRA reason for assessment (RDI 35012) - A0310C. |
| OMRA_TYPE_DTTM | DATETIME (UTC) | Most recent instant of documentation for PPS OMRA reason for assessment (RDI 35012) - A0310C. |
| MDS_REQT_C | VARCHAR (66) |  |
| MDS_REQT_USER_ID | VARCHAR (18) | Stores the most recent user to document the federal submission requirement (RDI 35015) - MDS A0410. |
| MDS_REQT_DTTM | DATETIME (UTC) | Stores the most recent instant that the federal submission requirement was  documented (RDI 35015) - MDS A0410. |
| ENTRY_DISCHRG_C | VARCHAR (66) |  |
| ENTRY_DISCHRG_USER_ID | VARCHAR (18) | Stores the most recent user to document the type of entry/discharge reporting for the assessment (RDI 35020) - MDS A0310F. |
| ENTRY_DISCHRG_DTTM | DATETIME (UTC) | Stores the most recent instant the type of entry/discharge reporting was documented for the assessment (RDI 35020) - MDS A0310F. |
| PREV_CORR_ARD_DT | DATETIME | This column indicates the ARD of the assessment to be corrected. |
| PREV_CORR_ARD_USER_ID | VARCHAR (18) | Current user to document the previous ARD for a significant correction. |
| PREV_CORR_ARD_DTTM | DATETIME (UTC) | This column contains the instant that the A2200 value (RDI 35048) was documented. |
| PART_A_HIPPS | VARCHAR (63) | This column contains the HIPPS code for Medicare Part A. |
| PART_A_HIPPS_USER_ID | VARCHAR (18) | Current user to document Z0100A (RDI 35060) |
| PART_A_HIPPS_DTTM | DATETIME (UTC) | The current instant that MDS item Z0100A (RDI 35060) was documented. |
| PART_A_RUG_VER | VARCHAR (63) | This column contains the version code used for MDS Z0100A. |
| PART_A_RUG_VER_USER_ID | VARCHAR (18) | Current user to document MDS item Z0100B (RDI 35061). |
| PART_A_RUG_VER_DTTM | DATETIME (UTC) | Current instant that Z0100B was documented (RDI 35061). |
| PART_A_SHORT_STAY_YN | VARCHAR (1) |  |
| PART_A_SHORT_STAY_USER_ID | VARCHAR (18) | Current user to document MDS item Z0100C (RDI 35062). |
| PART_A_SHORT_STAY_DTTM | DATETIME (UTC) | This column contains the instant that MDS item Z0100C was documented (RDI 35062). |
| PART_A_NT_HIPPS | VARCHAR (63) | This column contains the HIPPS code for Medicare Part A non-therapy. |
| PART_A_NT_HIPPS_USER_ID | VARCHAR (18) | This column contains the ID of the user who documented the current value of MDS item Z0150A (RDI 35063). |
| PART_A_NT_HIPPS_DTTM | DATETIME (UTC) | This column contains the current instant that MDS item Z0150A was documented (RDI 35063). |
| PART_A_NT_RUG_VER | VARCHAR (63) | This column contains the version code used for MDS Z0150A. |
| PART_A_NT_RUG_VER_USER_ID | VARCHAR (18) | This column contains the ID of the current user to document MDS item Z0150B (RDI 35064). |
| PART_A_NT_RUG_VER_DTTM | DATETIME (UTC) | This column contains the current instant that MDS item Z0150B (RDI 35064) was documented. |
| STATE_RUG_CASE_GRP | VARCHAR (63) | This column contains the RUG Case Mix group for state Medicaid billing. |
| STATE_RUG_CASE_GRP_USER_ID | VARCHAR (18) | This column contains the ID of the current user to document MDS item Z0200A (RDI 35070). |
| STATE_RUG_CASE_GRP_DTTM | DATETIME (UTC) | This column contains the instant that MDS item Z0200A (RDI 35070) was last documented. |
| STATE_RUG_VER | VARCHAR (63) | This column contains the Version code used for MDS Z0200A. |
| STATE_RUG_VER_USER_ID | VARCHAR (18) | This column contains the ID of the current user to document MDS item Z0200B (RDI 35071). |
| STATE_RUG_VER_DTTM | DATETIME (UTC) | This column contains the current instant that Z0200B (RDI 35071) was documented. |
| ALT_STATE_RUG_GRP | VARCHAR (63) | This column contains the RUG Case Mix group for alternate state Medicaid billing on an MDS assessment. |
| ALT_STATE_RUG_GRP_USER_ID | VARCHAR (18) | This column contains the ID of the current user to document MDS item Z0250A (RDI 35072). |
| ALT_STATE_RUG_GRP_DTTM | DATETIME (UTC) | This column contains the current instant that MDS Item Z0250A was documented (RDI 35072). |
| ALT_STATE_RUG_VER | VARCHAR (63) | This column contains the version code used for MDS Z0250A. |
| ALT_STATE_RUG_VER_USER_ID | VARCHAR (18) | This column contains the ID of the current user to document MDS item Z0250B (RDI 35073). |
| ALT_STATE_RUG_VER_DTTM | DATETIME (UTC) | This column contains the current instant that Z0250B was documented (RDI 35073). |
| INSURANCE_RUG_CODE | VARCHAR (63) | This column contains the RUG billing code used for a private payor. |
| INSURANCE_RUG_USER_ID | VARCHAR (18) | This column indicates the user who last documented MDS item Z0300 (RDI 35080). |
| INSURANCE_RUG_DTTM | DATETIME (UTC) | This column contains the current instant that MDS item Z0300 was documented (RDI 35083). |
| INSURANCE_RUG_VER | VARCHAR (63) | This column contains the version code used for MDS Z0300A. |
| INSURANCE_RUG_VER_USER_ID | VARCHAR (18) | This column contains the ID of the current user to document MDS item Z0300B (RDI 35081). |
| INSURANCE_RUG_VER_DTTM | DATETIME (UTC) | This column contains the current instant that MDS item Z0300B was documented (RDI 35081). |
| MOD_PREV_ASMT_ID | NUMERIC (18,0) | This column indicates the record which holds the previous version of the current abstraction record. |
| CAA_SIG_USER_ID | VARCHAR (18) | This column contains the ID of the RN coordinator who signed for the Care Area Assessment process. |
| CAA_SIG_DTTM | DATETIME (Attached) | This column contains the date of the signature in MDS V0200B1. |
| CARE_PLAN_SIG_USER_ID | VARCHAR (18) | This column contains the ID of the individual who signed for completing care plan decisions. |
| CARE_PLAN_SIG_DTTM | DATETIME (Attached) | This column contains the instant of the signature in MDS V0200C1. |
| CORR_RN_AC_SIG_USER_ID | VARCHAR (18) | This column contains the ID of the RN assessment coordinator attesting to the completion of the correction record. |
| CORR_RN_AC_SIG_DTTM | DATETIME (Attached) | This column contains the instant of the signature in MDS X1100D. |
| MDS_STATE_C *(deprecated)* | VARCHAR (66) |  |
| MDS_DAYS_LATE | INTEGER | This column contains the number of days the assessment is late or early. |
| MDS_ASSESS_INDIC_C | VARCHAR (66) |  |
| BILLING_START_DATE | DATETIME | This column stores the date that an MDS record becomes applicable for billing purposes. |
| BILLING_END_DATE | DATETIME | This column stores the known or expected effective end date after which an MDS should no longer be used for billing purposes. |
| RN_AC_COMP_SIG_DTTM | DATETIME (Attached) | This column contains the date of the signature in MDS Z0500A. |
| RN_AC_COMP_SIG_USER_ID | VARCHAR (18) | This column contains the ID of the RN assessment coordinator verifying assessment completion. |
| MDS_EXP_INST_DTTM | DATETIME (UTC) | The instant the export batch with which the assessment was exported from Epic was started. |
| MDS_EXP_LOC | VARCHAR (508) | The location the assessment was exported to. |
| MDS_ACC_REJ_DT | DATETIME | The user-entered date for when the assessment was accepted or rejected by CMS. |
| MDS_REJ_RSN_C | INTEGER |  |
| MDS_REGION_C | INTEGER |  |
| MDS_REGION_USER_ID | VARCHAR (18) | Stores the most recent user to document MDS resident state item RDI 35092. |
| MDS_REGION_INST_DTTM | DATETIME (UTC) | Stores the most recent instant that MDS resident state item (RDI 35092) was documented. |
| ORIG_ABSTN_ID | NUMERIC (18,0) | Indicates the original record whose data was copied to create the current record. |
| PPS_DISCHRG_YN | VARCHAR (1) |  |
| PPS_DISCHRG_USER_ID | VARCHAR (18) | Stores the ID of the most recent user to document MDS item A0310H |
| PPS_DISCHRG_UTC_DTTM | DATETIME (UTC) | Stores the most recent instant that MDS item A0310H was documented |
| MDS_OPT_STATE_ASMT_YN | VARCHAR (1) |  |
| MDS_OPT_STATE_ASMT_USER_ID | VARCHAR (18) | User who documented the current value of A0300A. |
| MDS_OPT_STATE_ASMT_UTC_DTTM | DATETIME (UTC) | Instant at which the current value of A0300A was documented. |
| MDS_STATE_ASMT_TYPE_C | INTEGER |  |
| MDS_STATE_ASMT_TYPE_USER_ID | VARCHAR (18) | User who documented the current value of A0300B |
| MDS_STATE_ASMT_TYPE_UTC_DTTM | DATETIME (UTC) | Instant at which the current value of A0300B was documented |
| MDS_VERSION_DAT | NUMERIC (18,2) | Contains the internally formated date of the custom HFR contact containing the MDS version information. |
| MDS_VERSION_USER_ID | VARCHAR (18) | Contains the user which set the current version value. |
| MDS_VERSION_UTC_DTTM | DATETIME (UTC) | Contains the UTC instant when the current version value was set. |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | REGISTRY_DATA_ID | ACCCATH3_ADMISSION | REGISTRY_DATA_ID | Unknown | No | No |  |
| 1 | REGISTRY_DATA_ID | C4_ADMISSION | REGISTRY_DATA_ID | Unknown | No | No |  |
| 1 | REGISTRY_DATA_ID | CASE_RPT_ABSTNS | REGISTRY_DATA_ID | Unknown | No | No |  |
| 1 | REGISTRY_DATA_ID | CMS_SEP1_ABSTN | REGISTRY_DATA_ID | No | No | No |  |
| 1 | REGISTRY_DATA_ID | COVID_19_HSP_INFECTIONS | REGISTRY_DATA_ID | Yes | No | No |  |
| 1 | REGISTRY_DATA_ID | CW_ABST_ANEMIA_MINERAL | REGISTRY_DATA_ID | Unknown | No | No |  |
| 1 | REGISTRY_DATA_ID | CW_ABST_DEMOGRAPHICS | REGISTRY_DATA_ID | Unknown | No | No |  |
| 1 | REGISTRY_DATA_ID | CW_ABST_HD_ADEQUACY | REGISTRY_DATA_ID | Unknown | No | No |  |
| 1 | REGISTRY_DATA_ID | CW_ABST_MED_REC | REGISTRY_DATA_ID | No | No | No |  |
| 1 | REGISTRY_DATA_ID | CW_ABST_PAT_ATTEST | REGISTRY_DATA_ID | Unknown | No | No |  |
| 1 | REGISTRY_DATA_ID | CW_ABST_PD_ADEQUACY | REGISTRY_DATA_ID | Unknown | No | No |  |
| 1 | REGISTRY_DATA_ID | CW_ABST_VACCINATIONS | REGISTRY_DATA_ID | Unknown | No | No |  |
| 1 | REGISTRY_DATA_ID | CW_ABST_VASCULAR_ACCESS | REGISTRY_DATA_ID | Unknown | No | No |  |
| 1 | REGISTRY_DATA_ID | DD_DIALYSIS_VACCINATION_G | REGISTRY_DATA_ID | No | No | No |  |
| 1 | REGISTRY_DATA_ID | DD_DIA_CMS_DEATH | REGISTRY_DATA_ID | No | No | No |  |
| 1 | REGISTRY_DATA_ID | DD_DIA_CMS_DISCONTINUED | REGISTRY_DATA_ID | No | No | No |  |
| 1 | REGISTRY_DATA_ID | DD_DIA_CMS_START | REGISTRY_DATA_ID | No | No | No |  |
| 1 | REGISTRY_DATA_ID | DD_DIA_CMS_START_2 | REGISTRY_DATA_ID | No | No | No |  |
| 1 | REGISTRY_DATA_ID | DD_DIA_CMS_TELEMEDICINE | REGISTRY_DATA_ID | No | No | No |  |
| 1 | REGISTRY_DATA_ID | DD_NHSE_CAN_RTT_PWY_DAY | REGISTRY_DATA_ID | No | No | No |  |
| 1 | REGISTRY_DATA_ID | DD_NHSE_CAN_RTT_PWY_MTH | REGISTRY_DATA_ID | No | No | No |  |
| 1 | REGISTRY_DATA_ID | DD_NHSE_CAN_RTT_PWY_WK | REGISTRY_DATA_ID | No | No | No |  |
| 1 | REGISTRY_DATA_ID | DD_NHSE_CAN_TREAT_PWY_DAY | REGISTRY_DATA_ID | No | No | No |  |
| 1 | REGISTRY_DATA_ID | DD_NHSE_CAN_TREAT_PWY_MTH | REGISTRY_DATA_ID | No | No | No |  |
| 1 | REGISTRY_DATA_ID | DD_NHSE_CAN_TREAT_PWY_WK | REGISTRY_DATA_ID | No | No | No |  |
| 1 | REGISTRY_DATA_ID | DD_NHSE_DX_ACTIVITY | REGISTRY_DATA_ID | No | No | No |  |
| 1 | REGISTRY_DATA_ID | DD_NHSE_DX_ACT_ORDERS | REGISTRY_DATA_ID | No | No | No |  |
| 1 | REGISTRY_DATA_ID | DD_NHSE_DX_ACT_SURG_CASES | REGISTRY_DATA_ID | No | No | No |  |
| 1 | REGISTRY_DATA_ID | DD_NHSE_DX_ACT_WAIT_LISTS | REGISTRY_DATA_ID | No | No | No |  |
| 1 | REGISTRY_DATA_ID | DD_NHSE_DX_PWY_DAY | REGISTRY_DATA_ID | No | No | No |  |

_(850 total; showing first 30)_
