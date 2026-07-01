# F_VENT_EPISODES

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=F_VENT_EPISODES

## Description

This table contains a listing of all the mechanical ventilation episodes documented in Flowsheets. A ventilation episode begins when a ventilator start row is documented upon. That ventilation episode ends when a ventilator end row is documented upon, the patient is discharged, or the patient goes on a leave of absence. The inpatient data store ID, flowsheet data ID, and episode times are provided so you can look up more specific flowsheet information and link back to the patient's hospital records.

## Metadata

| Property | Value |
| --- | --- |
| Type | Derived Table |
| Load Frequency | INCREMENTAL |
| Release Version | Rel 2010 |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| VENT_START_FSD_ID | No | The unique ID for the flowsheet data record that contains the ventilation start cell for this ventilation episode. Combine this with VENT_START_FSD_LINE to get the cell that documents the start of this episode. |
| VENT_START_FSD_LINE | INTEGER | The line count for the row in IP_FLWSHT_MEAS that stores the ventilation start time for this ventilation episode. Combine this with VENT_START_FSD_ID to get the cell that documents the start of this episode. |
| UPDATE_DATE | No | The instant this ventilation episode was last updated. |
| INPATIENT_DATA_ID | VARCHAR (18) | The unique ID of the inpatient data record associated with the ventilation start documentation for this ventilation episode. |
| VENT_START_DTTM | No | The instant the ventilation start row was documented upon for this ventilation episode. Note that even if the row is a date or time row, the data mart will use the recorded time of the entry to signal the vent start time. |
| START_FLO_MEAS_ID | No | The unique ID for the flowsheet row in which the ventilation start instant was documented. |
| VENT_END_FSD_ID | No | The unique ID for the flowsheet data record that contains the ventilation end cell for this ventilation episode. Combine this with VENT_END_FSD_LINE to get the cell that documents the end of this episode. |
| VENT_END_FSD_LINE | No | The line count for the row in IP_FLWSHT_MEAS that stores the ventilation end time for this ventilation episode. Combine this with VENT_END_FSD_ID to get the cell that documents the end of this episode. |
| VENT_END_DTTM | No | The instant the stop row for this ventilation episode was documented upon. If the stop row was not documented after an episode began and before a leave of absence out or discharge event, then this instant will be updated to the leave of absence out time or discharge time, respectively. Note that even if the row is a date or time row, the data mart uses the recorded time of the documentation to determine the vent stop time. |
| END_FLO_MEAS_ID | No | The unique ID for the flowsheet row in which the ventilation end instant was documented. |
| DELETED_YN | No | In table F_VENT_EPISODES, the column DELETED_YN has been deprecated. This column offers no reporting value and is no longer needed for internal use.  If the value in the start cell for this row was later deleted, then this column will have the value 'Y'.  Otherwise, it will have the value 'N'.  This column is for internal use only and should not be referenced in reports. |
| PAT_ID | VARCHAR (18) | The unique ID of the patient record associated with this ventilation episode. This column is frequently used to link to the PATIENT table. |
| ASSUMED_VENT_START_DTTM | No | If the ventilator start row was documented upon without corresponding documentation in the ventilator end row prior to VENT_START_DTTM, then the earliest such documentation instant is stored in this column. Otherwise, this column stores the same instant as VENT_START_DTTM. This column can be used in conjunction with ASSUMED_VENT_END_DTTM to find overlapping ventilator documentation.  For example, if a ventilator is documented as starting at 0800, starting at 1200, and ending at 1600, there will be two episodes in this table with the following values: VENT_START_FSD_LINE = 1, VENT_START_DTTM = 0800, VENT_END_DTTM = 1600, ASSUMED_VENT_START_DTTM = 0800, ASSUMED_VENT_END_DTTM = 1600 VENT_START_FSD_LINE = 2, VENT_START_DTTM = 1200, VENT_END_DTTM = 1600, ASSUMED_VENT_START_DTTM = 0800, ASSUMED_VENT_END_DTTM = 1600 |
| ASSUMED_VENT_END_DTTM | No | This column will store the first instant after a ventilator start row was documented upon that a ventilator end row was documented upon. This column may differ from VENT_END_DTTM in the event that the patient left for a leave of absence or was discharged without the ventilator end row being documented upon. This column may not be populated if a ventilator start was documented during a leave of absence. This column can be used in conjunction with ASSUMED_VENT_START_DTTM to find overlapping ventilator documentation.  For example, if a ventilator is documented as starting at 0800, starting at 1200, ending at 1600, and the patient is on a leave of absence from 0900 to 1200, there will be two episodes in this table with the following values: VENT_START_FSD_LINE = 1, VENT_START_DTTM = 0800, VENT_END_DTTM = 0900, ASSUMED_VENT_START_DTTM = 0800, ASSUMED_VENT_END_DTTM = 1600 VENT_START_FSD_LINE = 2, VENT_START_DTTM = 1200, VENT_END_DTTM = 1600, ASSUMED_VENT_START_DTTM = 0800, ASSUMED_VENT_END_DTTM = 1600 |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| B-TREE INDEX | EIX_F_VENT_EPI_INP_ID | INPATIENT_DATA_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_F_VENT_PAT_ID_START | PAT_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_F_VENT_PAT_ID_START | VENT_START_DTTM | 2 | Yes | Yes |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | VENT_START_FSD_ID | IP_FLWSHT_REC | FSD_ID | No | Unknown | No |  |
| 1 | VENT_START_FSD_ID | V_EHI_FSD_FILTER | FSD_ID | Unknown | Unknown | No |  |
| 4 | INPATIENT_DATA_ID | IP_DATA_STORE | INPATIENT_DATA_ID | No | Unknown | No |  |
| 6 | START_FLO_MEAS_ID | FLO_CNTX_INFO | ID | No | Unknown | No |  |
| 6 | START_FLO_MEAS_ID | IP_FLO_GP_DATA | FLO_MEAS_ID | No | Unknown | No |  |
| 6 | START_FLO_MEAS_ID | IP_FLO_GP_DATA_2 | FLO_MEAS_ID | No | Unknown | No |  |
| 7 | VENT_END_FSD_ID | IP_FLWSHT_REC | FSD_ID | No | Unknown | No |  |
| 7 | VENT_END_FSD_ID | V_EHI_FSD_FILTER | FSD_ID | Unknown | Unknown | No |  |
| 10 | END_FLO_MEAS_ID | FLO_CNTX_INFO | ID | No | Unknown | No |  |
| 10 | END_FLO_MEAS_ID | IP_FLO_GP_DATA | FLO_MEAS_ID | No | Unknown | No |  |
| 10 | END_FLO_MEAS_ID | IP_FLO_GP_DATA_2 | FLO_MEAS_ID | No | Unknown | No |  |
| 12 | PAT_ID | ANTICOAG_SELF_REGULATING | PAT_ID | No | Unknown | No |  |
| 12 | PAT_ID | CARE_COORDINATION | PAT_ID | Unknown | Unknown | No |  |
| 12 | PAT_ID | CLAIMS_DERIVE_PAT_FLAGS | PAT_ID | No | Unknown | No |  |
| 12 | PAT_ID | COMMUNITY_RESRC_REVIEWED | PAT_ID | No | Unknown | No |  |
| 12 | PAT_ID | D_PAT_GEOGRAPHIC_CLASS | PAT_ID | Unknown | Unknown | No |  |
| 12 | PAT_ID | EPT_MEM_INFO | PAT_ID | No | Unknown | No |  |
| 12 | PAT_ID | EXT_DATA_LAST_DONE | PAT_ID | No | Unknown | No |  |
| 12 | PAT_ID | F_IBD_ADULT_FORM_PAT | PAT_ID | Unknown | Unknown | No |  |
| 12 | PAT_ID | HH_PAT_INFO | PAT_ID | Unknown | Unknown | No |  |
| 12 | PAT_ID | HM_STATUS_UPD | PAT_ID | No | Unknown | No |  |
| 12 | PAT_ID | IMMNZTN_LAST_REVIEW | PAT_ID | No | Unknown | No |  |
| 12 | PAT_ID | PATIENT | PAT_ID | No | Unknown | No |  |
| 12 | PAT_ID | PATIENT_2 | PAT_ID | No | Unknown | No |  |
| 12 | PAT_ID | PATIENT_3 | PAT_ID | No | Unknown | No |  |
| 12 | PAT_ID | PATIENT_4 | PAT_ID | No | Unknown | No |  |
| 12 | PAT_ID | PATIENT_5 | PAT_ID | No | Unknown | No |  |
| 12 | PAT_ID | PATIENT_6 | PAT_ID | No | Unknown | No |  |
| 12 | PAT_ID | PATIENT_CONF_ADDR | PAT_ID | No | Unknown | No |  |
| 12 | PAT_ID | PATIENT_MISC_COMMENTS | PAT_ID | No | Unknown | No |  |

_(43 total; showing first 30)_
