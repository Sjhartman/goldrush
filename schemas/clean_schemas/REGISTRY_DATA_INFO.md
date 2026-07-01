# REGISTRY_DATA_INFO

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=REGISTRY_DATA_INFO

## Description

This table contains basic information about registry data, including what type of registry data it is.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | RDT |
| Release Version | Summer 2009 |
| May contain EHI? | No |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| RECORD_ID | NUMERIC (18,0) | The unique identifier (.1 item) for the record. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| RECORD_STATUS_C | INTEGER |  |
| NETWORKED_ID | VARCHAR (60) | The unique identifier of the record that is linked to by this registry data record. |
| RECORD_CREATION_DT | DATETIME | Stores the date the record was created |
| INSTANT_OF_UPD_TM *(deprecated)* | DATETIME (Local) | *** Deprecated *** In table REGISTRY_DATA_INFO, the column INSTANT_OF_UPD_TM (RDT/95000) has been deprecated.  The deprecated column's content/data is no longer available since it is no longer populated in Chronicles.  Stores the instant the record was last locked/unlocked |
| RELATED_INI | VARCHAR (3) | The base INI this registry data comes from. |
| NETWORKED_CSN | NUMERIC (18,0) | The networked CSN for the RDT record (e.g. the relevant EPT CSN). |
| RDT_TYPE_C | INTEGER |  |
| LINKED_INI | VARCHAR (3) | This is the linked INI for the registrant, if the registrant qualifies for a patient linked registry. |
| LINKED_ID | VARCHAR (60) | The record ID from the linked INI for this RDT record. |
| DATA_PERIOD_DATE | DATETIME | The date from which relevant data was drawn for this RDT record. The date falls in the time range associated with the record represented by the Networked INI and Networked ID for the RDT record. For example, a date between a Block of Time (BOT) record's start and end. |
| EXTERNAL_DEDUP_DOCUMENT_ID | NUMERIC (22,0) | The deduplicated document (DXR) ID for this registry data. |
| LINKED_PAT_ID | VARCHAR (18) | The linked patient ID. This is only populated on the Cosmos host. |
| PAT_ENC_REF_IDENT | VARCHAR (174) | Deduplicated document reference ID for the external encounter. |
| EXT_ANESTHESIA_DATA_REF_IDENT | VARCHAR (174) | The reference ID of the external data used to generate these anesthesia registry metrics. |
| EXT_SURGERY_REG_MET_REF_IDENT | VARCHAR (174) | Unique reference identifier for the surgery registry metric record. |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | RECORD_ID | DM_ACG_RISK | RECORD_ID | Unknown | No | No |  |
| 1 | RECORD_ID | DM_ACO | RECORD_ID | Unknown | No | No |  |
| 1 | RECORD_ID | DM_ACO_EXT | RECORD_ID | Unknown | No | No |  |
| 1 | RECORD_ID | DM_ACTIVE_PAT | RECORD_ID | Unknown | No | No |  |
| 1 | RECORD_ID | DM_ADHD | RECORD_ID | Unknown | No | No |  |
| 1 | RECORD_ID | DM_ADHD_EXT | RECORD_ID | Unknown | No | No |  |
| 1 | RECORD_ID | DM_ADOL_TRANS | RECORD_ID | Unknown | No | No |  |
| 1 | RECORD_ID | DM_ADOL_TRANS_EXT | RECORD_ID | Unknown | No | No |  |
| 1 | RECORD_ID | DM_ADULT_ADHD | RECORD_ID | Unknown | No | No |  |
| 1 | RECORD_ID | DM_ADULT_ASTHMA | RECORD_ID | Unknown | No | No |  |
| 1 | RECORD_ID | DM_ADULT_DIABETES | RECORD_ID | Unknown | No | No |  |
| 1 | RECORD_ID | DM_ADULT_FTM | RECORD_ID | Unknown | No | No |  |
| 1 | RECORD_ID | DM_ADULT_FTM_EXT | RECORD_ID | Unknown | No | No |  |
| 1 | RECORD_ID | DM_ADULT_HIV | RECORD_ID | Unknown | No | No |  |
| 1 | RECORD_ID | DM_ADULT_HYPERTENSION | RECORD_ID | Unknown | No | No |  |
| 1 | RECORD_ID | DM_ADULT_MTF | RECORD_ID | Unknown | No | No |  |
| 1 | RECORD_ID | DM_ADULT_MTF_EXT | RECORD_ID | Unknown | No | No |  |
| 1 | RECORD_ID | DM_ADULT_OBESITY | RECORD_ID | Unknown | No | No |  |
| 1 | RECORD_ID | DM_ALS | RECORD_ID | Unknown | No | No |  |
| 1 | RECORD_ID | DM_ANESTHESIA | RECORD_ID | Unknown | No | No |  |
| 1 | RECORD_ID | DM_ANESTHESIA_2 | RECORD_ID | Unknown | No | No |  |
| 1 | RECORD_ID | DM_ASTHMA | RECORD_ID | Unknown | No | No |  |
| 1 | RECORD_ID | DM_ASTHMA_EXT | RECORD_ID | Unknown | No | No |  |
| 1 | RECORD_ID | DM_ATRIAL_FIBRILLATION | RECORD_ID | Unknown | No | No |  |
| 1 | RECORD_ID | DM_BREAST_HEALTH | RECORD_ID | Unknown | No | No |  |
| 1 | RECORD_ID | DM_CAD | RECORD_ID | Unknown | No | No |  |
| 1 | RECORD_ID | DM_CAD_DIABETES | RECORD_ID | Unknown | No | No |  |
| 1 | RECORD_ID | DM_CAD_EXT | RECORD_ID | Unknown | No | No |  |
| 1 | RECORD_ID | DM_CANCER_PATIENT | RECORD_ID | Unknown | No | No |  |
| 1 | RECORD_ID | DM_CANCER_PROBLEM | RECORD_ID | Unknown | No | No |  |

_(350 total; showing first 30)_
