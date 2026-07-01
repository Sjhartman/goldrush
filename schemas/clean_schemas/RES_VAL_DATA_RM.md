# RES_VAL_DATA_RM

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=RES_VAL_DATA_RM

## Description

Stores data for multi-line value item. For a given line data may be spread across multiple lines.

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
| RESULT_ID | VARCHAR (18) | The unique ID of the result record for this row. This column is frequently used to link to the RES_COMPONENTS table through the RES_VAL_PTR_RM table.  For component repeats, link from RES_REPEAT_COMP through the RES_RPT_VAL_PTR_RM table. |
| GROUP_LINE | No | Stores a link from the RES_VAL_PTR_RM.CMP_MULTILINE_VALUE column. |
| VALUE_LINE | No | The line number of one of the multiple values that are associated with the result and the component/organism from the RES_VAL_PTR_RM or RES_RPT_VAL_PTR_RM table. This column can be ignored - it is here for completeness. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| MULT_LN_VAL_STORAGE | VARCHAR (254) | The value entered for a given component. Each component can list multiple lines in Component Multiline Value (OVR-51201) (RES_VAL_PTR_RM.CMP_MULTILINE_VALUE) or Repeat Component Multiline Value (OVR-53201) (RES_RPT_VAL_PTR_RM.RPT_MULTILINE_VALUE), which are the lines of this item. If the value is a category number, this column contains the category title, not the category number, at the time of extract. If the category title is changed after the extract, this data could get out of sync. Note that the category number is also extracted to RES_VAL_DATA_RM.MULT_LN_VAL_STG_RAW, so you could look up the category title based on the category number from the corresponding category ZC table. To find out which category table to use, check the columns LAB_CAT_INI and LAB_CAT_ITEM in table CLARITY_COMPONENT for the component associated with this row. |
| MULT_LN_VAL_STG_RAW | VARCHAR (254) | Stores the values for a given component. For a category value this would be the identifier. |

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

_(86 total; showing first 30)_
