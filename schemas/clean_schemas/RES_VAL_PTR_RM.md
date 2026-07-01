# RES_VAL_PTR_RM

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=RES_VAL_PTR_RM

## Description

For a given component this holds all the pointers to the table that stores the multi line data.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | OVR |
| Release Version | Summer 2009 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| RESULT_ID | VARCHAR (18) | The unique ID of the result record for this row. This column is frequently used to link to the RES_COMPONENTS table. |
| GROUP_LINE | No | This is the component line number from the RES_COMPONENTS table. Use the RESULT_ID to link the RES_COMPONENTS table to this table in addition to the GROUP_LINE. |
| VALUE_LINE | No | The line number of one of the multiple values that is associated with the component and the result from the RES_VAL_DATA_RM table.  This column can be ignored - it is here for completeness. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| CMP_MULTILINE_VALUE | NUMERIC (18,0) | Stores a list of lines in OVR-52201 which stores data for this line in the component related group.  To link tables RES_VAL_PTR_RM to RES_VAL_DATA_RM link the following two sets of columns: - RES_VAL_PTR_RM.RESULT_ID to RES_VAL_DATA_RM.RESULT_ID, and - RES_VAL_PTR_RM.CMP_MULTILINE_VALUE to RES_VAL_DATA_RM.GROUP_LINE |

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

_(90 total; showing first 30)_
