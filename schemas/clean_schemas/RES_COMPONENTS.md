# RES_COMPONENTS

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=RES_COMPONENTS

## Description

Primary table for result component information.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | OVR |
| Release Version | FALL 2004 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| RESULT_ID | VARCHAR (18) | The unique identifier of the result record. |
| RES_TYPE_ID *(deprecated)* | VARCHAR (18) |  |
| LINE | No | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| LAB_ID *(deprecated)* | VARCHAR (18) |  |
| RES_SPECIMEN_ID *(deprecated)* | VARCHAR (18) |  |
| COMPONENT_ID | NUMERIC (18,0) | Internal component ID |
| COMPONENT_GRP_C | INTEGER |  |
| COMPONENT_RESULT | VARCHAR (254) | Component result interpreted value |
| COMPONENT_VALUE | VARCHAR (254) | Component result value |
| COMPONENT_UNITS | VARCHAR (254) | Component result units |
| COMPONENT_ABN_C | VARCHAR (66) |  |
| COMPONENT_DELTA_YN | VARCHAR (254) |  |
| COMPONENT_NRML_LO | VARCHAR (254) | This item specifies the lowest "normal" value for this component if applicable. |
| COMPONENT_NRML_HI | VARCHAR (254) | This item specifies the highest "normal" value for this component, if applicable. |
| COMPONENT_CMT | VARCHAR (1000) | This item allows entry of a free-text comment related specifically to this component. |
| COMPONENT_MTHD_ID | VARCHAR (18) | The testing method for this component. |
| COMPONENT_RANGE | VARCHAR (254) | The normal range for the component or a list of values that are considered normal. |
| COMPONENT_INST | DATETIME (Local) | The instant the component was resulted. |
| COMPONENT_LAB_ID | VARCHAR (18) | Resulting lab ID for this component. |
| COMPONENT_REPORT_YN | VARCHAR (254) |  |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| COMP_SMRTXT_COMM_ID *(deprecated)* | VARCHAR (254) | In table RES_COMPONENTS, the column COMP_SMRTXT_COMM_ID (OVR/51051) has been deprecated. The deprecated column's content/data is no longer available since it is no longer populated in Chronicles. |
| COMPON_ST_VALUE_ID *(deprecated)* | VARCHAR (254) | In table RES_COMPONENTS, the column COMPON_ST_VALUE_ID (OVR/51012) has been deprecated. The deprecated column's content/data is no longer available since it is no longer populated in Chronicles. |
| COMPON_DILUTION | VARCHAR (254) | The factor by which the value is diluted |
| COMPON_LINEAR_YN | VARCHAR (1) |  |
| COMPON_DATA_REQ_C | INTEGER |  |
| COMPON_RPT_SET_BY_C | INTEGER |  |
| COMPON_REPORTABLE_C | INTEGER |  |
| CMP_REVIEW_TYPE_C | INTEGER |  |
| CMP_RSCRN_SELMETH_C | INTEGER |  |
| CMP_SCREEN_DT *(deprecated)* | DATETIME | In table RES_COMPONENTS, the column CMP_SCREEN_DT (OVR/51284) has been deprecated. The deprecated column's content/data is no longer available since it is no longer populated in Chronicles. |
| COMP_CSRVWR_USER_ID *(deprecated)* | VARCHAR (18) | In table RES_COMPONENTS, the column COMP_CSRVWR_USER_ID (OVR/51285) has been deprecated. The deprecated column's content/data is no longer available since it is no longer populated in Chronicles. |
| COM_REPORT_SYSTEM_C | INTEGER |  |
| COM_REPORT_RULE_ID | VARCHAR (18) | This will copy and store component reported rule from test when result record is created |
| COM_RPT_FIELD_C | INTEGER |  |
| CMP_EDITING_USER_ID | VARCHAR (18) | The user that resulted the related component. |
| COMP_INSTR_VERFLG_C *(deprecated)* | INTEGER | In table RES_COMPONENTS, column COMP_INSTR_VERFLG_C has been deprecated.  This column has been replaced by column COMP_INSTR_VERFLG (OVR/51062) in table RES_COMPONENTS.  This column has been changed from a category to a string item. Data previously stored as a category (1 - 5) now appears as the former category number and has the following interpretation: 1 - Pass 2 - Failed & Held 3 - Failed & Not Held 4 - Not Evaluated & Held 5 - Not Evaluated & Not Held Customers may send their own verification flags and interpret them as they see fit. |
| COMP_VAL_STAT_C | INTEGER |  |
| COMP_VERIF_STATUS_C | INTEGER |  |
| COMP_VERIF_DTTM | DATETIME (Local) | The instant the component was verified. |
| COMP_VERIF_LAB_ID | VARCHAR (18) | The unique ID of the lab that verified the component. |
| COMP_VERIF_USER_ID | VARCHAR (18) | The unique ID of the user who verified the component. |
| COMP_INTERP_SET_C *(deprecated)* | INTEGER |  |
| COMP_VALUE_NUM | NUMERIC (18,10) | The component result value for the result. This column is only populated if the component result value is numeric. This includes numeric results as well as category ID's for category results. |
| USR_OVRD_ABNRML_ID | VARCHAR (18) | The unique ID associated with the user record responsible for overriding abnormality or reference range. This column is frequently used to link to the CLARITY_EMP table. |
| USR_OVRD_REP_FLG_ID | VARCHAR (18) | The unique ID associated with the user record responsible for overriding the reportable flag. This column is frequently used to link to the CLARITY_EMP table. |
| OVRIDE_ABNRML_YN | VARCHAR (1) |  |
| OVRIDE_REP_FLAG_YN | VARCHAR (1) |  |
| COMP_RES_UTC_DTTM | DATETIME (UTC) | The instant when the component was resulted in UTC. |
| COMP_DELTA_RES_ID | VARCHAR (18) | The unique ID of the result that triggered the delta flag for this result component. |
| COMP_INSTR_VERFLG | VARCHAR (24) | This item is the verification flag received from the middle tier. |
| CMP_VERIF_UTC_DTTM | DATETIME (UTC) | Stores the instant in UTC at which the component on the corresponding line was verified. |
| COMP_METH_SET_BY_C | INTEGER |  |
| COMP_PO_LAB_ID | NUMERIC (18,0) | The unique ID of the actual resulting agency for this component. This could be populated for interfaced results to indicate which resulting agency actually performed the test (as opposed to the lab or section in which verification occurred). |
| COMP_LNC_RECORD_ID | NUMERIC (18,0) | The unique ID associated with the LOINC record for this row as populated by the interface when results are received from an external resulting agency. |
| COMP_ACCREDITED_YN | VARCHAR (1) |  |
| USR_OVRD_ACCR_ST_USER_ID | VARCHAR (18) | The unique ID associated with the user record. This column is frequently used to link to the CLARITY_EMP table. Records the user responsible for overriding the accreditation status for this component. |
| OVRIDE_ACCR_STAT_YN | VARCHAR (1) |  |
| COMP_UNCERTAIN_MEAS | VARCHAR (50) | The extent to which a given value is uncertain (e.g. if the uncertainty percentage is 5%, then the component uncertainty value for a result of 1.00 will be +/- 0.05). NOTE:  This is how the data is stored in the database; as string format. This field stores numeric in M internal format, using a period as the decimal separator irrespective of locale. |
| COMP_NETWORK_CONCEPT_IDENT | VARCHAR (50) | Stores the network concept identifier associated with this component at the time of resulting. |
| COMP_DISP_RANGE_SET_BY_C | INTEGER |  |
| COMP_INSTR_PROF_IDENT | VARCHAR (50) | Stores the network concept identifier associated with the component's resulting method at the time of resulting or verification. |
| CMP_LINEARITY_SET_BY_C | INTEGER |  |
| COMPON_TAG_LN | INTEGER | Line number for the tested against group relevant to this row, indicating that all component lines pointing to the same line should be grouped together logically. |
| CMP_ADD_USER_ID | VARCHAR (18) | User who added the component to the test |
| CMP_ADD_DTTM | DATETIME (Attached) | Stores the local instant of when the component was originally added to the test. |
| CMP_ADD_UTC_DTTM | DATETIME (UTC) | Stores the UTC instant of when the component was originally added to the test. |
| COMP_NORM_LO_INEQ_C | INTEGER |  |
| COMP_NORM_HI_INEQ_C | INTEGER |  |

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

_(288 total; showing first 30)_
