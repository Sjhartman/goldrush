# RES_VLD_AUDIT

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=RES_VLD_AUDIT

## Description

Result audit information for verification and unverification (result correction).

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | OVR |
| Release Version | SPRING 2007 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| RESULT_ID | VARCHAR (18) | The unique ID of the result record. |
| RES_TYPE_ID | VARCHAR (18) | The unique ID of the result type record for this result. |
| LINE | No | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| LAB_ID *(deprecated)* | VARCHAR (18) |  |
| RES_SPECIMEN_ID | VARCHAR (18) | Internal specimen identifier associated with result |
| RES_VLD_STATUS_C | INTEGER |  |
| RES_UNVLD_RSN_C | INTEGER |  |
| RES_VLD_USER | VARCHAR (18) | The unique ID associated with the user record for this row. This column is frequently used to link to the CLARITY_EMP table. |
| RES_VLD_INSTANT | DATETIME (Local) | The instant when the result is validated. |
| RES_UNVLD_RSLT *(deprecated)* | VARCHAR (18) | *** Deprecated *** In table RES_VLD_AUDIT, the column RES_UNVLD_RSLT (OVR/90080) has been deprecated.   This column has been replaced by column RES_UNVLD_RESULT_ID (OVR/90080) in table RES_VLD_AUDIT.   Validation audit result record pointer |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| RES_UNVLD_RSN_COM | VARCHAR (254) |  |
| RES_VERIFY_UTC_DTTM | DATETIME (UTC) | The instant when verification occurred in UTC. |
| RES_UNVLD_RESULT_ID | VARCHAR (18) | The unique identifier of the validation audit result record that is associated with this result record. |
| UNVALIDATION_TYPE_C | INTEGER |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | RESULT_ID | ADRENAL_GLAND_BIOP | RESULT_ID | No | No | No |  |
| 1 | RESULT_ID | AMPULLA_OF_VATER | RESULT_ID | No | No | No |  |
| 1 | RESULT_ID | ANUS_ABDOMIN_RESEC | RESULT_ID | No | No | No |  |
| 1 | RESULT_ID | ANUS_EXCISION_BIOP | RESULT_ID | No | No | No |  |
| 1 | RESULT_ID | APPENDIX_RESECTION | RESULT_ID | No | No | No |  |
| 1 | RESULT_ID | BONE_BIOPSY | RESULT_ID | No | No | No |  |
| 1 | RESULT_ID | BONE_MARROW_ASPIR | RESULT_ID | No | No | No |  |
| 1 | RESULT_ID | BONE_RESECTION | RESULT_ID | No | No | No |  |
| 1 | RESULT_ID | BRAIN_SPINAL_BIOP | RESULT_ID | No | No | No |  |
| 1 | RESULT_ID | BRAIN_SPINAL_BIO_2 | RESULT_ID | No | No | No |  |
| 1 | RESULT_ID | COLON_RECTUM_BIOP | RESULT_ID | No | No | No |  |
| 1 | RESULT_ID | COLON_RECTUM_RESEC | RESULT_ID | No | No | No |  |
| 1 | RESULT_ID | DCIS_BREAST_EXCIS | RESULT_ID | No | No | No |  |
| 1 | RESULT_ID | DIST_EXTRAHEP_BILE | RESULT_ID | No | No | No |  |
| 1 | RESULT_ID | EMBRYOLOGY_RESULT | RESULT_ID | No | No | No |  |
| 1 | RESULT_ID | ENDOMETRIUM_HYSTER | RESULT_ID | No | No | No |  |
| 1 | RESULT_ID | ESOPHAGUS_RESEC | RESULT_ID | No | No | No |  |
| 1 | RESULT_ID | EWING_SARCOMA_BIOP | RESULT_ID | No | No | No |  |
| 1 | RESULT_ID | EWING_SARCOM_RESEC | RESULT_ID | No | No | No |  |
| 1 | RESULT_ID | FALLOP_TUB_SALPING | RESULT_ID | No | No | No |  |
| 1 | RESULT_ID | GALLBLADDER_RESEC | RESULT_ID | No | No | No |  |
| 1 | RESULT_ID | HEART_RESECTION | RESULT_ID | No | No | No |  |
| 1 | RESULT_ID | HEPATOBLAST_RESEC | RESULT_ID | No | No | No |  |
| 1 | RESULT_ID | HEPATOCELL_CARC | RESULT_ID | No | No | No |  |
| 1 | RESULT_ID | HODGKIN_LYMPHOMA | RESULT_ID | No | No | No |  |
| 1 | RESULT_ID | INTRAH_BILE_RESEC | RESULT_ID | No | No | No |  |
| 1 | RESULT_ID | INVAS_CARC_BREAST | RESULT_ID | No | No | No |  |
| 1 | RESULT_ID | INVAS_CARC_BREAS_2 | RESULT_ID | No | No | No |  |
| 1 | RESULT_ID | INVAS_CARC_BREAS_3 | RESULT_ID | No | No | No |  |
| 1 | RESULT_ID | KIDNEY_BIOPSY | RESULT_ID | No | No | No |  |

_(188 total; showing first 30)_
