# IP_LDA_NOADDSINGLE

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=IP_LDA_NOADDSINGLE

## Description

This table stores LDA information for a patient. A record is created in LDA for insertion of every line, drain, airway, or wound for a patient, as well as entering a trip into a patient's travel history. The no-add information for this LDA is stored in the table.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | LDA |
| Release Version | SUMMER 2005 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| IP_LDA_ID | VARCHAR (18) | The internal ID of the Lines/Drains/Airways (LDA) record. |
| CM_PHY_OWNER_ID | VARCHAR (25) | Stroes Physical Owner's ID |
| CM_LOG_OWNER_ID | VARCHAR (25) | Stores the logical owner for the record |
| PAT_ID | VARCHAR (18) | This item stores the ID of the patient to which this line record was added. |
| PAT_ENC_CSN_ID | NUMERIC (18,0) | This item stores the contact serial number of the encounter in which the record was created. |
| FLO_MEAS_ID | VARCHAR (18) | This item stores the Flowsheet ID that defines the structure of this record. It is the flowsheet group that is used to define the set of rows for the Line/Drain/Airway (LDA). |
| REMOVAL_INSTANT | DATETIME (Local) | This item stores the instant at which the line/drain was removed. If the line or drain has not been removed, it will store 11/19/2157 17:46:39 as the end instant. |
| PLACEMENT_INSTANT | DATETIME (Local) | This item stores the placement instant of the record. |
| FSD_ID | VARCHAR (18) | This item stores the flowsheet data (FSD) ID of the record that has information about the properties of the line/drain/airway (LDA). |
| DESCRIPTION | VARCHAR (254) | This item stores the name/description of the line/drain. |
| PROPERTIES_DISPLAY | VARCHAR (254) | Stores the properties display string to be displayed in Doc Flowsheets and Reports. |
| SITE | VARCHAR (254) | This item stores site information for the inserted Line/Drain/Airway. |
| LDA_GROUP_CDR | FLOAT | This column stores the contact date real of the Line/Drain/Airway (LDA) Group contact that created this LDA.  This column is stored in Epic's datetime (DTE) format. |
| LINKED_SUPPLY_ID | VARCHAR (18) | The unique ID of the supply record that is associated with this Line/Drain/Airway. |
| REMOVAL_DTTM | DATETIME (Local) | This item stores the date and time at which the line/drain was removed. Unlike REMOVAL_INSTANT, if the line or drain has not been removed, it will store null. |
| REC_ARCHIVED_YN | No | Record archived status for LDA. |
| TRIP_REGION_ID | NUMERIC (18,0) | Represents where the patient traveled for this trip |
| TRIP_BEGIN_DATE | DATETIME | Represents when a patient began their trip |
| TRIP_END_DATE | DATETIME | Represents the end of this patient trip |
| TRIP_DATE_APPROX_C | INTEGER |  |
| TRIP_PAT_ENTERED_YN | VARCHAR (1) |  |
| AVATAR_PROPERTY_OVERRIDE_YN | VARCHAR (1) |  |
| AVATAR_RECORD_ID | NUMERIC (18,0) | The unique ID of the Anatomy record associated with the region in which this Line/Drain/Airway (LDA) is located on the LDA Avatar activity. |
| AVATAR_CALCULATED_RECORD_ID | NUMERIC (18,0) | Used to store the current region (VEL) record calculated from the Lines/Drains/Airways (LDA) properties and the Avatar LDA Mapping Configuration. |
| RECORDED_DTTM | DATETIME (Local) | The recorded time used in IP_FLWSHT_MEAS for storing the property data for this LDA. |
| AVATAR_X_COORDINATE | NUMERIC (18,12) | The x-coordinate for this LDA on the patient's Avatar. |
| AVATAR_Y_COORDINATE | NUMERIC (18,12) | The y-coordinate for this LDA on the patient's Avatar. |
| ADDED_TO_BACKGROUND_AVATAR_C | INTEGER |  |
| AVATAR_ORIENT_C | INTEGER | Surrogate key used to uniquely identify rows in this (and only this) table on Cogito Cloud only, do not assume the surrogate key in this table will correspond to the surrogate key in another table |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| B-TREE INDEX | EIX_LDA_NOADDSINGLE_FLO_MES_ID | FLO_MEAS_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_LDA_NOADDSINGLE_PL_RM_INST | PLACEMENT_INSTANT | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_LDA_NOADDSINGLE_PL_RM_INST | REMOVAL_INSTANT | 2 | Yes | Yes |  |
| B-TREE INDEX | EIX_LDA_NOADDSINGLE_RM_INST | REMOVAL_INSTANT | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_LDA_NOADDSING_PAT_PL_INST | PAT_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_LDA_NOADDSING_PAT_PL_INST | PLACEMENT_INSTANT | 2 | Yes | Yes |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | IP_LDA_ID | LDA_SHARE_WITH_PAT | IP_LDA_ID | No | No | No |  |
| 1 | IP_LDA_ID | V_IP_PAT_CENT_LINE | IP_LDA_ID | Unknown | Unknown | No |  |
| 1 | IP_LDA_ID | V_IP_PAT_UMB_LINE | IP_LDA_ID | Unknown | Unknown | No |  |
| 1 | IP_LDA_ID | V_IP_PAT_URIN_CATH | IP_LDA_ID | Unknown | Unknown | No |  |
| 2 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 2 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 2 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 3 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 4 | PAT_ID | ANTICOAG_SELF_REGULATING | PAT_ID | No | No | No |  |
| 4 | PAT_ID | CARE_COORDINATION | PAT_ID | Unknown | No | No |  |
| 4 | PAT_ID | CLAIMS_DERIVE_PAT_FLAGS | PAT_ID | No | No | No |  |
| 4 | PAT_ID | COMMUNITY_RESRC_REVIEWED | PAT_ID | No | No | No |  |
| 4 | PAT_ID | D_PAT_GEOGRAPHIC_CLASS | PAT_ID | Unknown | Unknown | No |  |
| 4 | PAT_ID | EPT_MEM_INFO | PAT_ID | No | No | No |  |
| 4 | PAT_ID | EXT_DATA_LAST_DONE | PAT_ID | No | No | No |  |
| 4 | PAT_ID | F_IBD_ADULT_FORM_PAT | PAT_ID | Unknown | Unknown | No |  |
| 4 | PAT_ID | HH_PAT_INFO | PAT_ID | Unknown | No | No |  |
| 4 | PAT_ID | HM_STATUS_UPD | PAT_ID | No | No | No |  |
| 4 | PAT_ID | IMMNZTN_LAST_REVIEW | PAT_ID | No | No | No |  |
| 4 | PAT_ID | PATIENT | PAT_ID | No | No | No |  |
| 4 | PAT_ID | PATIENT_2 | PAT_ID | No | No | No |  |
| 4 | PAT_ID | PATIENT_3 | PAT_ID | No | No | No |  |
| 4 | PAT_ID | PATIENT_4 | PAT_ID | No | No | No |  |
| 4 | PAT_ID | PATIENT_5 | PAT_ID | No | No | No |  |
| 4 | PAT_ID | PATIENT_6 | PAT_ID | No | No | No |  |
| 4 | PAT_ID | PATIENT_CONF_ADDR | PAT_ID | No | No | No |  |
| 4 | PAT_ID | PATIENT_MISC_COMMENTS | PAT_ID | No | No | No |  |
| 4 | PAT_ID | PATIENT_MYC | PAT_ID | Unknown | No | No |  |

_(176 total; showing first 30)_
