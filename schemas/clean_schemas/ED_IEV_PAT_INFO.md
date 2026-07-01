# ED_IEV_PAT_INFO

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=ED_IEV_PAT_INFO

## Description

This table contains information that is useful for linking records (patient, department, etc.) to their appropriate events.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | IEV |
| Release Version | EPIC 2002 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| EVENT_ID | VARCHAR (18) | The unique ID of the event record. This column is frequently used to link to the ED_IEV_EVENT_INFO table. |
| RECORD_STATE_NAME *(deprecated)* | VARCHAR (8) |  |
| PAT_ID | VARCHAR (18) | The unique ID of the patient record for this line. This column is frequently used to link to the PATIENT table. |
| EPT_DAT *(deprecated)* | FLOAT | This column is deprecated and does not extract any data. The column previously extracted a unique, internal patient contact date in decimal format. Note: the format of this internal date is not the same as PAT_ENC_DATE_REAL. This column will not be useful as a link to any other table. |
| ITEMS_EDITED_TIME | DATETIME | The date and time when this event record was last edited. |
| UPDATE_DATE | No | The last date and time the event record was extracted. |
| PAT_DATE_REAL | No | A unique, internal contact date in decimal format. The integer portion of the number indicates the date of the contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| DTE_EXTERNAL | No | The date of this contact in calendar format. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| PAT_ENC_CSN_ID | NUMERIC (18,0) | The unique contact serial number for this contact. This number is unique across patients and encounters in your system. If you use IntraConnect this is the Unique Contact Identifier (UCI). |
| PAT_ENC_DATE_REAL | No | A unique, internal patient contact date in decimal format. The integer portion of the number indicates the date of the contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| CONTACT_DATE | No | The date of this contact in calendar format. |
| DEPT_EVENT_DEP_ID | NUMERIC (18,0) | The unique ID of the department that is associated with this event record. Note: this item is populated only for department-level events. |
| RECORD_STATE_C | INTEGER |  |
| TRANSFER_STATUS_C | INTEGER |  |
| TYPE_ID | VARCHAR (18) | The unique ID of the event that indicates the type of events stored on this event record. Common examples would be 50-ED Arrived for ED related events or 35000-IP Admission Reconciliation for some medication reconciliation events. This column should be used to link to the ED_EVENT_TMPL_INFO table. |
| CREATE_DTTM | DATETIME (Local) | The instant when the event record was created. |
| CREATE_USER_ID | VARCHAR (18) | The unique ID of the user who created the event record. |
| EVENT_DATE | DATETIME | The date the event record was created. |
| PAT_CSN | NUMERIC (18,0) | The unique contact serial number for this contact. This number is unique across patients and encounters in your system. If you use IntraConnect this is the Unique Contact Identifier (UCI). |
| ADT_TRANSFER_LINK | INTEGER | Virtual item for the Admission, Transfer, Discharge, or Leave of Absence (ADT) event link for a medication reconciliation transfer. |
| REG_CLIP_FREETEXT | VARCHAR (508) | User-entered patient name for patient added to clipboard. User-entered text is necessary for users without security to select real patients or for new patients. |
| REG_CLIP_LWS_ID | VARCHAR (18) | Workstation that was used to add the patient to the Patients Waiting Registration clipboard. |
| REG_CLIP_COMMENTS | VARCHAR (508) | Comments for the patient added to the Patients Waiting Registration Clipboard |
| IP_ORDREC_SORT_DTTM | DATETIME (Local) | This is the instant that all the orders in the event should be sorted by, instead of using their individual ordering session keys or ordering instants. |
| REG_WAIT_STATE_C | INTEGER |  |
| REG_WAIT_PAT_NAME | VARCHAR (160) | Holds the user-entered patient name for a patient who is waiting but has not yet been identified. |
| REG_WAIT_IS_PRI_YN | VARCHAR (1) |  |
| REG_WAIT_PAGER_ID | VARCHAR (40) | Holds the patient pager number when the Patient Paging functionality is being used. |
| REG_WAIT_PAGER_NUM | VARCHAR (40) | Holds a simple patient pager number when the Patient Paging functionality is not being used. |
| REG_WAIT_ARRV_DTTM | DATETIME (Local) | Holds the earliest event instant, which will indicate the time the patient arrived for the encounter this event list is associated with. |
| ORD_REC_ADT_EVENT_ID | NUMERIC (18,0) | Contains a pointer to the Admission, Transfer, Discharge, or Leave of Absence (ADT) event that is most relevant for this medication reconciliation action. An admission medication reconciliation record will point to the admission (ADT)event; a discharge or discharge/readmit (also known as inter-facility transfer) record will point to the discharge ADT event; and a transfer record will point to the most recent transfer-in ADT event that took place before reconciliation was completed. |
| ORD_REC_SUMMARY_UPDT_DTTM | DATETIME (UTC) | This contains the instant (in UTC) that the summary data for this record in the ORDER_REC_SUMMARY table was last updated. |
| ORD_REC_DISCHARGE_DISP_C | VARCHAR (66) |  |
| AVS_COPY_FORWARD_DTTM | DATETIME (UTC) | The date and time that a user copied After Visit Summary documentation from another encounter into this one. |
| AVS_COPY_FORWARD_USER_ID | VARCHAR (18) | The unique ID of the user who copied After Visit Summary documentation from another encounter into this one. |
| EVENT_LOCATION_EAF_ID | NUMERIC (18,0) | For hospital area level IEV records, this holds the hospital area that the events are associated with. |
| EVENT_YEAR | INTEGER | The calendar year the event applies to if the type of event is tracked over multiple years. |
| OR_ADMISSION_GROUP_C | INTEGER |  |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| B-TREE INDEX | EIX_IEV_PAT_INFO_CSN | PAT_CSN | 1 | Yes | Yes |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | EVENT_ID | IP_MAR_BARCODE_ITM | EVENT_ID | Unknown | No | No |  |
| 3 | PAT_ID | ANTICOAG_SELF_REGULATING | PAT_ID | No | No | No |  |
| 3 | PAT_ID | CARE_COORDINATION | PAT_ID | Unknown | No | No |  |
| 3 | PAT_ID | CLAIMS_DERIVE_PAT_FLAGS | PAT_ID | No | No | No |  |
| 3 | PAT_ID | COMMUNITY_RESRC_REVIEWED | PAT_ID | No | No | No |  |
| 3 | PAT_ID | D_PAT_GEOGRAPHIC_CLASS | PAT_ID | Unknown | Unknown | No |  |
| 3 | PAT_ID | EPT_MEM_INFO | PAT_ID | No | No | No |  |
| 3 | PAT_ID | EXT_DATA_LAST_DONE | PAT_ID | No | No | No |  |
| 3 | PAT_ID | F_IBD_ADULT_FORM_PAT | PAT_ID | Unknown | Unknown | No |  |
| 3 | PAT_ID | HH_PAT_INFO | PAT_ID | Unknown | No | No |  |
| 3 | PAT_ID | HM_STATUS_UPD | PAT_ID | No | No | No |  |
| 3 | PAT_ID | IMMNZTN_LAST_REVIEW | PAT_ID | No | No | No |  |
| 3 | PAT_ID | PATIENT | PAT_ID | No | No | No |  |
| 3 | PAT_ID | PATIENT_2 | PAT_ID | No | No | No |  |
| 3 | PAT_ID | PATIENT_3 | PAT_ID | No | No | No |  |
| 3 | PAT_ID | PATIENT_4 | PAT_ID | No | No | No |  |
| 3 | PAT_ID | PATIENT_5 | PAT_ID | No | No | No |  |
| 3 | PAT_ID | PATIENT_6 | PAT_ID | No | No | No |  |
| 3 | PAT_ID | PATIENT_CONF_ADDR | PAT_ID | No | No | No |  |
| 3 | PAT_ID | PATIENT_MISC_COMMENTS | PAT_ID | No | No | No |  |
| 3 | PAT_ID | PATIENT_MYC | PAT_ID | Unknown | No | No |  |
| 3 | PAT_ID | PATIENT_OPT | PAT_ID | No | No | No |  |
| 3 | PAT_ID | PAT_ENC_LAST_HX_CT | PAT_ID | Unknown | Unknown | No |  |
| 3 | PAT_ID | PAT_RES_CODE | PAT_ID | No | No | No |  |
| 3 | PAT_ID | PROB_LIST_REVIEWED | PAT_ID | No | No | No |  |
| 3 | PAT_ID | REGADDL_PAT | PAT_ID | No | No | No |  |
| 3 | PAT_ID | SCF_FHIR_MAP | PAT_ID | No | No | No |  |
| 3 | PAT_ID | TEETH_REVIEWED | PAT_ID | No | No | No |  |
| 3 | PAT_ID | VALID_PATIENT | PAT_ID | No | No | No |  |
| 3 | PAT_ID | V_PAT_ABO | PAT_ID | Unknown | Unknown | No |  |

_(394 total; showing first 30)_
