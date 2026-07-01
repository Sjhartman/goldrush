# QM_GEN_INFO

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=QM_GEN_INFO

## Description

This table contains general information about the quality measure associated with registry data records.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | RDI |
| Release Version | Summer 2009 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| REGISTRY_DATA_ID | NUMERIC (18,0) | The unique ID of the registry data record. |
| REGISTRY_TYPE_C | INTEGER |  |
| PAT_ID | VARCHAR (18) | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| PAT_DATE | DATETIME | The patient encounter date for this registry data record. Each registry data record in this table will correspond to only one encounter. To link to that encounter, use the first line of RDI_PAT_CSN.PAT_CSN. |
| QM_SUM_MEASURE_CSN *(deprecated)* | NUMERIC (18,0) | In table QM_GEN_INFO the column QUALITY_SUM MEASURE_CSN (RDI 3200) has been deprecated.  The deprecated column's content/data is no longer available since it is no longer populated in Chronicles. |
| QM_YEAR | INTEGER | The reporting year to which this registry data applies. |
| QM_PROV_AND_TIN | VARCHAR (62) | A concatenation of the encounter provider ID and the reporting entity's TIN for the registry data. |
| QM_ENC_PROV_ID | VARCHAR (18) | The unique ID associated with the provider record for this row. This column is frequently used to link to the CLARITY_SER table. |
| QM_TIN | VARCHAR (254) | The tax identification number (TIN) associated with the revenue location in this row. |
| QM_EHR_RECORD_YN | VARCHAR (1) |  |
| QM_SUM_MSR_VER_ID | NUMERIC (18,0) | The unique ID of the quality measure record for this row. This column is frequently used to link to the QM_QUAL_MEASURES table. |
| SUM_QM_CNCT_NUM | INTEGER | The contact number for the quality measure in the row. |
| ED_ARRIVAL_DTTM | DATETIME (Local) | Records the instant of the patient's arrival to the ED. Used by Meaningful Use reporting. |
| ED_DEPARTURE_DTTM | DATETIME (Local) | Records the instant of the patient's departure from the ED. Used by Meaningful Use reporting. |
| ED_DECISION_DTTM | DATETIME (Local) | Records the instant of the decision to admit from the ED. Used by Meaningful Use reporting. |
| ED_ADMIT_DEP_ID | NUMERIC (18,0) | Records the emergency department from which the patient was admitted. Used by Meaningful Use reporting. |
| OM_PROV_ID | VARCHAR (18) | The unique ID of the provider linked to this registry data record. This column is frequently used to link to the CLARITY_SER table. |
| OM_MEASURE_ID | NUMERIC (18,0) | The unique ID of the measure associated with this registry data record. This column is frequently used to link to the QM_QUAL_MEASURES table. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| UDS_GRANTEE_C | INTEGER |  |
| UDS_GRANT_C | INTEGER |  |
| OM_DEPARTMENT_ID | NUMERIC (18,0) | The unique ID of the department for which this registry data record contains data. |
| OM_FACT_DATE | DATETIME | The date for which this registry data record contains data. |
| OM_REV_LOC_ID | NUMERIC (18,0) | The unique ID of the revenue location for which this registry data record contains data. |
| LOG_ID | VARCHAR (18) | This item stores ORL ID if the RDI record is associated with a surgery. The item is used to enable clarity report for SCIP quality measures. |
| QM_ENC_END_TIM_DTTM | DATETIME (Local) | End instant for the patient encounter, only set for QRDA |
| REPORTING_REV_LOC_ID | NUMERIC (18,0) | The revenue location in which the patient encounter occurred. |
| ED_DEPART_DEP_ID | NUMERIC (18,0) | Stores the ED that the patient departed from for Meaningful Use Quality Measures |
| LAST_UPDATE_DTTM | No | The extract date/time for the row. |
| ED_ARRIVAL_DEP_ID | NUMERIC (18,0) | This item stores the ED arrival department as determined by the Meaningful Use Quality Measures batch job. |
| ED_ARR_REV_LOC_ID | NUMERIC (18,0) | This item stores the ED arrival revenue location as determined by the Meaningful Use Quality Measures batch job. |
| EH_QM_DISCH_DEP_ID | NUMERIC (18,0) | Discharge department set by the Meaningful Use quality measures batch job. |
| ACUITY_SYSTEM_ID | NUMERIC (18,0) | This item stores the scoring system record ID from which the scores are calculated and stored, if applicable. This item is populated when the RDI record is created. |
| EH_QM_ARR_DEP_ID | NUMERIC (18,0) | Arrival department set by the Meaningful Use Quality Measure batch. |
| OR_LOC_ID | NUMERIC (18,0) | This item stores the OR location ID of the principal surgery performed during the admission in this RDI record. |
| CM_ED_ARRIVAL_DTTM | DATETIME (Local) | The date and time of the patient's arrival to the ED. It is used for Inpatient Core Measures reporting. |
| CM_ED_DEPART_DTTM | DATETIME (Local) | The date and time of the patient's departure from the ED. It is used for Inpatient Core Measures reporting. |
| CM_ED_DECISION_DTTM | DATETIME (Local) | The date and time of the decision to admit the patient from the ED. It is used for Inpatient Core Measures reporting. |
| CM_ED_DEPART_DEP_ID | NUMERIC (18,0) | The unique ID for the ED from which the patient departed. It is used for Inpatient Core Measures reporting. |
| QM_ATTR_TYPE_C | INTEGER |  |
| QM_ATTR_RECORD_ID | VARCHAR (30) | This item specifies the record identifier on which the outcomes are evaluated. Its attribution type is determined by the item RDI 3231. |
| QM_GEN_ATTR_SRC | VARCHAR (100) | This item indicates how a patient or encounter was associated to the attribution record listed in I RDI 3232. |
| QRDA_SEX_C | VARCHAR (66) |  |
| QRDA_RACE_C | VARCHAR (66) |  |
| QRDA_ETHNICITY_C | VARCHAR (66) |  |
| QRDA_PAYER_C | VARCHAR (66) |  |
| BLOCK_ID | NUMERIC (18,0) | This item stores the ID of the Block of Time record that is linked to this Registry Data record. |
| QM_ENC_DEPT_ID | NUMERIC (18,0) | The unique ID of the department in which the encounter took place. |
| OM_SUM_STAGE_C | INTEGER |  |
| ORDER_ID | NUMERIC (18,0) | The associated order ID. |
| PRED_DEPARTMENT_ID | NUMERIC (18,0) | Links department record to predictive model score for department based models. |
| NOTE_ID | VARCHAR (254) | Associates this record's predictive model score with an HNO record such as a clinical note. |
| EPISODE_ID | NUMERIC (18,0) | The episode associated with the registry data record. |
| CURRENT_STATUS_C | INTEGER |  |
| RECORD_STATUS_2_C | INTEGER |  |
| REGISTRY_ID | NUMERIC (18,0) | The registry associated with this data record. |
| REGISTRY_OVRIDE_CONTEXT | VARCHAR (62) | Stores the override context string to identify the correct override record for the registry settings record (HFR). |
| IB_MSG_ID | VARCHAR (18) | Associates this row's predictive model score with a specific In Basket message |
| PB_FOL_ID | NUMERIC (18,0) | Associates this record's predictive model score with a follow-up record. |
| BUCKET_ID | NUMERIC (18,0) | Associates this record's predictive model score with a hospital liability bucket record. |
| RELEVANT_DATE | DATETIME | This is a registry specific date which will be filled upon submission of registry record. |
| ANCHOR_HSP_ACCOUNT_ID | NUMERIC (18,0) | The hospital account record associated with the abstraction if it uses a hospital account-based co-anchor. |
| ANCHOR_PROV_ID | VARCHAR (18) | The provider record associated with the abstraction if it uses provider co-anchoring. |
| ANCHOR_POC_ID | NUMERIC (18,0) | The plan of care record associated with the abstraction if it uses plan of care co-anchoring. |
| ANCHOR_REFERRAL_ID | NUMERIC (18,0) | The referral record associated with the abstraction if it uses referral co-anchoring. |
| ANCHOR_NOTE_ID | VARCHAR (254) | The note associated with the abstraction if it uses note co-anchoring. |
| ANCHOR_FIN_ASST_TRACKER_ID | NUMERIC (18,0) | The decision record associated with the abstraction if it uses decision co-anchoring. |
| ANCHOR_DEPARTMENT_ID | NUMERIC (18,0) | The department associated with the abstraction if it uses department co-anchoring. |
| ANCHOR_ORDER_ID | NUMERIC (18,0) | The order associated with the abstraction if it uses order co-anchoring. |
| CURRENT_STATUS_USER_ID | VARCHAR (18) | The user who set the current status. |
| CURRENT_STATUS_DTTM | DATETIME (UTC) | The instant the current status was set. |
| ANCHOR_EPISODE_ID | NUMERIC (18,0) | The episode associated with the abstraction if it uses episode co-anchoring. |
| IS_FORM_IN_EDITABLE_STATUS_YN | VARCHAR (1) |  |
| HSP_ACCOUNT_ID | NUMERIC (18,0) | Associates this record's predictive model score with a hospital account record. |
| REFERRAL_ID | NUMERIC (18,0) | The unique identifier of the referral record associated with the predictive model score. |
| AUTH_REQUEST_ID | NUMERIC (18,0) | The unique identifier of the authorization request record associated with the predictive model score. |
| AUTH_REQUEST_CSN_ID | NUMERIC (18,0) | The unique contact serial number of the authorization request associated with the predictive model score. |
| PARENT_REGISTRY_DATA_ID | NUMERIC (18,0) | Parent registry data record. Only populated if this is a repeating group record. |
| CRITERIA_REVIEW_ID | NUMERIC (18,0) | The unique identifier of the criteria review record associated with the predictive model score. |
| EXTERNAL_STATUS_RDI_C | INTEGER |  |
| EXTERNAL_STATUS_LOCAL_DTTM | DATETIME (Local) | Instant the most recent external status (EXTERNAL_STATUS_RDI_C) was set |
| EXTERNAL_STATUS_ERROR_MESSAGE | VARCHAR (550) | Contains the associated error message when External_STATUS_RDI_C has a status of "error" |
| IDENTITY_EVENT_RECORD_ID | VARCHAR (18) | Associates this record's predictive model score with an Identity Event record. |
| CHILD_RDI_PAT_ID | VARCHAR (18) | The .1 ID of the context patient for the child abstraction record. This will not necessarily be the patient defined in the root abstraction record. |
| CHILD_RDI_PAT_ENC_CSN_ID | NUMERIC (18,0) | The CSN of the context patient for the child abstraction record. This will not necessarily be the patient defined in the root abstraction record. |
| LAB_CASE_ID | NUMERIC (18,0) | A unique lab case identifier that consists of the name and the REQ ID. This column is often used for grouping, sorting, and display purposes in reports. |
| LAB_SPECIMEN_ID | VARCHAR (18) | A unique lab specimen identifier that consists of the name and the OVS ID. This column is often used for grouping, sorting, and display purposes in reports. |
| LAB_RESULT_ID | VARCHAR (18) | A unique lab result identifier that consists of the name and the OVR ID. This column is often used for grouping, sorting, and display purposes in reports. |
| QM_EXT_IDENT_BUNDLE_ID | NUMERIC (18,0) | The associated QRDA-I external ID bundle's RQG .1 |
| COSMOS_DEDUP_DOCUMENT_ID | NUMERIC (22,0) | Stores the deduplicated DXR for an RDI record in Cosmos. |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| B-TREE INDEX | EIX_QM_GEN_INFO_REGISTRY_TYPE | REGISTRY_TYPE_C | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_QM_GEN_INFO_UPD_TYPE_REG | LAST_UPDATE_DTTM | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_QM_GEN_INFO_UPD_TYPE_REG | REGISTRY_TYPE_C | 2 | Yes | Yes |  |
| B-TREE INDEX | EIX_QM_GEN_INFO_UPD_TYPE_REG | REGISTRY_DATA_ID | 3 | Yes | Yes |  |

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

_(1341 total; showing first 30)_
