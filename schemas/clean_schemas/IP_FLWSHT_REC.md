# IP_FLWSHT_REC

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=IP_FLWSHT_REC

## Description

This table contains linking information associated with flowsheet records.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | FSD |
| Release Version | EPIC 2002 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| FSD_ID | VARCHAR (18) | The unique ID for the flowsheet data record. |
| INPATIENT_DATA_ID | VARCHAR (18) | The unique ID of the inpatient record associated with this flowsheet reading. |
| RECORD_DATE | DATETIME | The date these flowsheet readings were taken. |
| CM_PHY_OWNER_ID | VARCHAR (25) | ID of the physical deployment owner for this record.  Physical owners will be where the data is hosted, either on the cross-over server or the owner deployment. |
| CM_LOG_OWNER_ID | VARCHAR (25) | ID of the logical deployment owner for this record.  Logical owners show the deployment where the record was created but doesn't represent if the record is a part of version skew. |
| DAILY_NET | NUMERIC (18,5) | The daily net Intake/Output total for this date. |
| UPDATE_DATE | No | *** Deprecated *** In table IP_FLWSHT_REC, the column UPDATE_DATE has been deprecated.  This column should no longer be used to track updates to IP_FLWSHT_REC.  Flip "Track row updates?" to "Yes" in the Information Activity to enable capturing of row updates on IP_FLWSHT_REC using ESP_CR_ALTERED_ROWS.   The date and time this row was last updated (the last time it was extracted or this column was backfilled). |
| PAT_ID | VARCHAR (18) | The unique ID of the patient. |
| REC_ARCHIVED_YN | No | Indicates whether the Flowsheet record is archived at the record level. |
| UNVERIFIED_DAILY_NET | NUMERIC (18,5) | The unverified daily net Intake/Output total for this date. |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| B-TREE INDEX | EIX_IP_FLWSHT_REC__INP_ID | INPATIENT_DATA_ID | 1 | Yes | Yes |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | FSD_ID | V_EHI_FSD_FILTER | FSD_ID | Unknown | Unknown | No |  |
| 2 | INPATIENT_DATA_ID | IP_DATA_STORE | INPATIENT_DATA_ID | No | No | No |  |
| 4 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 4 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 4 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 5 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 5 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 5 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 8 | PAT_ID | ANTICOAG_SELF_REGULATING | PAT_ID | No | No | No |  |
| 8 | PAT_ID | CARE_COORDINATION | PAT_ID | Unknown | No | No |  |
| 8 | PAT_ID | CLAIMS_DERIVE_PAT_FLAGS | PAT_ID | No | No | No |  |
| 8 | PAT_ID | COMMUNITY_RESRC_REVIEWED | PAT_ID | No | No | No |  |
| 8 | PAT_ID | D_PAT_GEOGRAPHIC_CLASS | PAT_ID | Unknown | Unknown | No |  |
| 8 | PAT_ID | EPT_MEM_INFO | PAT_ID | No | No | No |  |
| 8 | PAT_ID | EXT_DATA_LAST_DONE | PAT_ID | No | No | No |  |
| 8 | PAT_ID | F_IBD_ADULT_FORM_PAT | PAT_ID | Unknown | Unknown | No |  |
| 8 | PAT_ID | HH_PAT_INFO | PAT_ID | Unknown | No | No |  |
| 8 | PAT_ID | HM_STATUS_UPD | PAT_ID | No | No | No |  |
| 8 | PAT_ID | IMMNZTN_LAST_REVIEW | PAT_ID | No | No | No |  |
| 8 | PAT_ID | PATIENT | PAT_ID | No | No | No |  |
| 8 | PAT_ID | PATIENT_2 | PAT_ID | No | No | No |  |
| 8 | PAT_ID | PATIENT_3 | PAT_ID | No | No | No |  |
| 8 | PAT_ID | PATIENT_4 | PAT_ID | No | No | No |  |
| 8 | PAT_ID | PATIENT_5 | PAT_ID | No | No | No |  |
| 8 | PAT_ID | PATIENT_6 | PAT_ID | No | No | No |  |
| 8 | PAT_ID | PATIENT_CONF_ADDR | PAT_ID | No | No | No |  |
| 8 | PAT_ID | PATIENT_MISC_COMMENTS | PAT_ID | No | No | No |  |
| 8 | PAT_ID | PATIENT_MYC | PAT_ID | Unknown | No | No |  |
| 8 | PAT_ID | PATIENT_OPT | PAT_ID | No | No | No |  |
| 8 | PAT_ID | PAT_ENC_LAST_HX_CT | PAT_ID | Unknown | Unknown | No |  |

_(40 total; showing first 30)_
