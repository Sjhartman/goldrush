# ORGAN

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=ORGAN

## Description

Table for general organ information about transplanted and native organs.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | ORG |
| Release Version | SPRING 2007 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| ORG_RECORD_ID | NUMERIC (18,0) | The unique identifier for the organ record. |
| CM_PHY_OWNER_ID | VARCHAR (25) | ID of the physical deployment owner for this record.  Physical owners will be  where the data is hosted, either on the cross-over server or the owner  deployment. |
| CM_LOG_OWNER_ID | VARCHAR (25) | ID of the logical deployment owner for this record.  Logical owners show the  deployment where the record was created but doesn't represent if the record is a  part of version skew. |
| TX_DNR_ID | VARCHAR (18) | The unique identifier for the organ donor. |
| TX_RCP_ID | VARCHAR (18) | The unique identifier for the organ recipient. |
| TX_ORG_SRC_C | INTEGER |  |
| TX_DNR_REL_C | INTEGER |  |
| ORG_DEATH_ID | NUMERIC (18,0) | Reasons for organ graft death |
| ORG_NOTE_ID | VARCHAR (254) | Note about the organ |
| ORG_STAT_C | INTEGER |  |
| ORG_WT | NUMERIC (18,2) | Organ's weight in ounces. |
| ANTIGEN_MATCHES | NUMERIC (18,0) | Number of antigen matches 0 - 6 |
| ORG_PROCUREMENT_DT | DATETIME | Procurement date of organ from donor |
| ORG_PERFUSION_MIN | NUMERIC (18,0) | Perfusion time of organ minutes component |
| ORG_WISCHEMIA_MIN | NUMERIC (18,0) | Time in warm ischemia minutes component |
| ORG_CISCHEMIA_MIN | NUMERIC (18,0) | Time spent in cold ischemia minute component |
| CLAMP_INST_ON_TM | DATETIME (Local) | Instant when clamp was put on |
| CLAMP_INST_OFF_TM | DATETIME (Local) | Instant clamp taken off |
| ORG_DONATION_CRIT_C | INTEGER |  |
| PRIMARY_WARM_ISCH | NUMERIC (18,0) | Minutes organ is in primary warm ischemia |
| ORG_FAIL_DT | DATETIME | Date which the transplanted organ failed |
| ORG_FAIL_METHOD_C | INTEGER |  |
| ORG_MATCHTYPE_C | INTEGER |  |
| ORG_PRESERVE_C | INTEGER |  |
| ORG_PROCEDURE_TYP_C | INTEGER |  |
| FINAL_RESISTANCE | NUMERIC (18,2) | Final resistance at transplant if organ was on a pump |
| FINAL_FLOW_RATE | NUMERIC (18,0) | Final flow rate at transplant if organ was on a pump |
| ORGAN_REMOVAL_DT | DATETIME | Date the organ was removed after it failed. |
| UNOS_PRIMARY_FAIL_C | INTEGER |  |
| UNOS_PRIMARY_OTHER | VARCHAR (254) | Free text entry listing the primary reason for organ failure. If no entry exists in the category list, this explains the reason for organ failure. |
| ORGAN_NUM | NUMERIC (18,0) | The sequential number of the organ transplanted. |
| ORGAN_SIZE | NUMERIC (18,2) | The volume of the organ in mL. |
| UNOS_CONTRIB_OTHER | VARCHAR (254) | Free text entry listing a contributory cause of organ failure. If no entry exists in the category list, this explains the reason for organ failure. |
| NATIVE_ORGAN_YN | VARCHAR (1) |  |
| NAT_PRIMARY_FAIL_C | INTEGER |  |
| NAT_PRIMARY_OTHER | VARCHAR (254) | Other primary reason for native organ failure |
| NAT_CONTRIB_OTHER | VARCHAR (254) | Other contributory reason for native organ failure |
| ORG_RECEIVED_ON_C | INTEGER |  |
| ORGAN_STAYED_ON_C | INTEGER |  |
| INDUCTION_USED_C | INTEGER |  |
| KIDNEY_BIOPSY_YN | VARCHAR (1) |  |
| PERIOP_TRANSFUSION | NUMERIC (18,0) | Number of perioperative blood transfusions. |
| INTRA_OP_TRANSFUSN | NUMERIC (18,0) | Number of intra-operative blood transfusions |
| RECORD_STATUS_C | INTEGER |  |
| PREOP_BLOOD_TRANS | NUMERIC (18,0) | The number of pre-operative blood transfusions. |
| ANASTOMOSIS_ST_DTTM | DATETIME (Local) | Indicates the anastomosis start time for the transplant. |
| PORT_CLAMP_OFF_DTTM | DATETIME (Local) | Indicates the portal clamp off time for the transplant. |
| CDC_YN | VARCHAR (1) |  |
| MATCH_RUN | VARCHAR (192) | The match run ID for the organ. |
| OPO_C | INTEGER |  |
| OPO_RISK_YN | VARCHAR (1) |  |
| LINKED_ORGAN_ID | NUMERIC (18,0) | If the current organ is linked to another organ, this stores the ID of the linked organ. This linked organ provides the donor information for the current organ. |
| EXT_TEAM_RECOVER_YN | VARCHAR (1) |  |
| RECOVERY_FAC_ID | NUMERIC (18,0) | The facility where the organ was recovered. |
| REC_FAC_OTHER | VARCHAR (192) | The facility where the organ was recovered, if none is listed in the organ recovery facility. |
| ORG_TISCHEMIA_MIN | INTEGER | Total ischemia time in minutes. |
| FAILURE_DT_EST_C | INTEGER |  |
| NAT_DX_RVW_USER_ID *(deprecated)* | VARCHAR (18) | *** Deprecated *** This functionality was removed in the August 2020 Release  Native organ diagnosis review user. |
| NAT_DX_RVW_DATE *(deprecated)* | DATETIME | *** Deprecated *** This functionality was removed in the August 2020 Release  Native organ diagnosis review date. |
| DNR_RISK_PRF_PCT | INTEGER | The percentage score of donor risk profile index. |
| DNR_KI_EXTRACT_INST_DTTM | DATETIME (UTC) | Indicates the donor organ extraction time. |
| ORGAN_CLASS_C | INTEGER |  |
| A_MISMATCHES_NUM | INTEGER | Indicate the number of A mismatches between the donor and the recipient. |
| B_MISMATCHES_NUM | INTEGER | Indicate the number of B mismatches between the donor and the recipient. |
| DR_MISMATCHES_NUM | INTEGER | Indicate the number of DR mismatches between the donor and the recipient. |
| POSTOP_BLOOD_TRANS | INTEGER | The number of post-operative blood transfusions. |
| SPEC_DONOR_REL | VARCHAR (50) | Indicates a specific free-text donor relation when the donor relation category list is insufficient. |
| MACHINE_PERFUSION_ST_UTC_DTTM | DATETIME (UTC) | The instant at which the organ perfusion started. |
| MACHINE_PERFUSION_END_UTC_DTTM | DATETIME (UTC) | The instant at which the organ perfusion ended during the transplant surgery. |
| MACHINE_PERFUSION_TOTAL_MIN | NUMERIC (18,2) | The number of minutes the organ was perfused using a machine. |
| ORGAN_RECORD_TYPE_C | INTEGER |  |
| RAD_THP_VOL_DESCRIPTION | VARCHAR (4000) | Description of the radiotherapy volume |
| RAD_THP_PAT_ID | VARCHAR (18) | Radiotherapy patient ID from EPT |
| RAD_THP_VOL_VERSION | VARCHAR (50) | Version of the radiotherapy volume resource |
| RT_VOL_VER_INST_UTC_DTTM | DATETIME (UTC) | This item stores the last update instant of the record. |
| ALLOC_DNR_ABO_C | INTEGER | Surrogate key used to uniquely identify rows in this (and only this) table on Cogito Cloud only, do not assume the surrogate key in this table will correspond to the surrogate key in another table |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ORG_RECORD_ID | ISLET_PROC_INFO | ORG_RECORD_ID | No | No | No |  |
| 1 | ORG_RECORD_ID | ORGAN_OFFERS | ORG_RECORD_ID | No | No | No |  |
| 1 | ORG_RECORD_ID | ORGAN_RELATION | ORG_RECORD_ID | No | No | No |  |
| 1 | ORG_RECORD_ID | ORG_SURGICAL_INFO | ORG_RECORD_ID | Unknown | No | No |  |
| 1 | ORG_RECORD_ID | ORG_SURGICAL_INFO2 | ORG_RECORD_ID | No | No | No |  |
| 1 | ORG_RECORD_ID | V_EHI_AUDIT_ORG_RT_ITEMS | ORG_RECORD_ID | Unknown | Unknown | No |  |
| 2 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 2 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 2 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 3 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 4 | TX_DNR_ID | ANTICOAG_SELF_REGULATING | PAT_ID | No | No | No |  |
| 4 | TX_DNR_ID | CARE_COORDINATION | PAT_ID | Unknown | No | No |  |
| 4 | TX_DNR_ID | CLAIMS_DERIVE_PAT_FLAGS | PAT_ID | No | No | No |  |
| 4 | TX_DNR_ID | COMMUNITY_RESRC_REVIEWED | PAT_ID | No | No | No |  |
| 4 | TX_DNR_ID | D_PAT_GEOGRAPHIC_CLASS | PAT_ID | Unknown | Unknown | No |  |
| 4 | TX_DNR_ID | EPT_MEM_INFO | PAT_ID | No | No | No |  |
| 4 | TX_DNR_ID | EXT_DATA_LAST_DONE | PAT_ID | No | No | No |  |
| 4 | TX_DNR_ID | F_IBD_ADULT_FORM_PAT | PAT_ID | Unknown | Unknown | No |  |
| 4 | TX_DNR_ID | HH_PAT_INFO | PAT_ID | Unknown | No | No |  |
| 4 | TX_DNR_ID | HM_STATUS_UPD | PAT_ID | No | No | No |  |
| 4 | TX_DNR_ID | IMMNZTN_LAST_REVIEW | PAT_ID | No | No | No |  |
| 4 | TX_DNR_ID | PATIENT | PAT_ID | No | No | No |  |
| 4 | TX_DNR_ID | PATIENT_2 | PAT_ID | No | No | No |  |
| 4 | TX_DNR_ID | PATIENT_3 | PAT_ID | No | No | No |  |
| 4 | TX_DNR_ID | PATIENT_4 | PAT_ID | No | No | No |  |
| 4 | TX_DNR_ID | PATIENT_5 | PAT_ID | No | No | No |  |
| 4 | TX_DNR_ID | PATIENT_6 | PAT_ID | No | No | No |  |
| 4 | TX_DNR_ID | PATIENT_CONF_ADDR | PAT_ID | No | No | No |  |

_(201 total; showing first 30)_
