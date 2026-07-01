# EMR_SYSTEM_DEFS

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=EMR_SYSTEM_DEFS

## Description

This table contains information from no-add, single-response items in EMR System Definitions.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | LSD |
| Release Version | Rel 2010 |
| May contain EHI? | No |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| FACILITY_ID | VARCHAR (18) | The unique identifier (.1 item) for the facility record. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| PREGNANCY_RATG_C | INTEGER |  |
| LACTATION_RATG_C | INTEGER |  |
| OB_CSECT_GRPER_ID | VARCHAR (18) | This item points to a grouper (VCG) record of surgical procedure (ORP) records that are considered to be c-sections. |
| MR_PSIST_STRTD_YN | VARCHAR (1) |  |
| CHK_SER_PHR_C | INTEGER |  |
| EPCS_SVC_LVL_C *(deprecated)* | INTEGER |  |
| NON_EPCS_PHARM_MSG | VARCHAR (254) | This text displays alongside an order if e-prescribing validation fails because the pharmacy does not support EPCS. |
| NON_EPCS_SER_MSG | VARCHAR (254) | This text displays alongside an order if e-prescribing validation fails because the provider does not support EPCS. |
| DIG_SIG_DOWN_MSG | VARCHAR (254) | This text displays alongside an order if e-prescribing validation fails because the digital signature server is down. |
| GENERIC_EPCS_MSG | VARCHAR (254) | The text that displays alongside an order if e-prescribing validations fail due to the medication not meeting DEA schedule regulations in order to be e-prescribed. |
| ELEC_FETAL_MON_ID | VARCHAR (18) | Configuration item to specify which flowsheet row to use for electronic fetal monitoring. If any value is documented in the associated flowsheet row for the patient for the encounter, we assume that electronic fetal monitoring was used for the patient during that encounter. |
| SURFACTANT_RPLACE_C | INTEGER |  |
| NO_INDUCTION_C | INTEGER |  |
| NO_AUGMENTATION_C | INTEGER |  |
| PROLAPSED_CORD_C | INTEGER |  |
| HEMOGLOBIN_COM_NAME | VARCHAR (254) | Configuration item to specify the common name for the result to use for determining hemoglobin. This column can be linked to CLARITY_COMPONENT.COMMON_NAME to determine which components are used for Hemoglobin results. |
| HEMATOCRIT_COM_NAME | VARCHAR (254) | Configuration item to specify the common name for the result to use for determining hematocrit. This column can be linked to CLARITY_COMPONENT.COMMON_NAME to determine which components are used for Hematocrit results. |
| MU_EH_DENOM_CALC_C | INTEGER |  |
| PRN_PROV_IIT_ID | NUMERIC (18,0) | For PRN configuration, this specifies what IIT record is being used by the organization, mapped from the provider's SER record |
| PRN_FAC_IIT_ID | NUMERIC (18,0) | The Identity Type (IIT) record being used by the organization to display the National Perinatal Registry (LVR) hospital number, mapped from the facility's EAF record. |
| ADM_TIMELY_REC_HR | INTEGER | This item gives the number of hours after a patient is admitted for admission med rec actions to be taken and considered "timely". Actions taken after this will not be considered timely by reports that show timely-reconciliation data. |
| AN_RESP_ANES_LOGIC_C | INTEGER |  |
| AN_MU_INCL_ADHOCS_YN | VARCHAR (1) |  |
| PREF_AUD_INSTALL_DTTM | DATETIME (UTC) | Stores the instant the SU or upgrade installed item EPT 20242, which corresponds to the earliest valid instant for item EPT 20242. |
| MAR_TIMEOUT_SCANS_YN | VARCHAR (1) |  |
| OR_DECISION_EVENT_C | VARCHAR (66) |  |
| OB_CSECT_PROC_ID | VARCHAR (254) | The procedure that will be used to create c-section cases in the C-Section Quick Case Creation activity. |
| IRIS_IDENTITY_ID | NUMERIC (18,0) | This is the Identity Type ID (IIT .1) that should be used to generate IDs for patients with encounters in the IRIS Registry. These IDs are only to be used when submitting data to the American Academy of Ophthalmology's IRIS Registry. |
| OB_EBL_FLO_MEAS_ID | VARCHAR (18) | This item stores the flowsheet row where estimated blood loss will be filed to at the signing of the delivery. |
| ORAL_ASSESS_WIN_START_MINUTES | INTEGER | The smallest number of minutes after an initial administration that a follow-up pain reassessment is considered timely. This threshold only applies to administrations with an oral administration route as defined by IP_ORAL_ADMIN_ROUTES. |
| ORAL_ASSESS_WIN_END_MINUTES | INTEGER | The greatest number of minutes after an initial administration that a follow-up pain reassessment is considered timely. This threshold only applies to administrations with an oral administration route as defined by IP_ORAL_ADMIN_ROUTES. |
| IV_ASSESS_WIN_START_MINUTES | INTEGER | The smallest number of minutes after an initial administration that a follow-up pain reassessment is considered timely. This threshold only applies to administrations with an IV administration route as defined by IP_IV_ADMIN_ROUTES. |
| IV_ASSESS_WIN_END_MINUTES | INTEGER | The greatest number of minutes after an initial administration that a follow-up pain reassessment is considered timely. This threshold only applies to administrations with an IV administration route as defined by IP_IV_ADMIN_ROUTES. |
| EXCL_PAIN_MEDS_GROUPER_ID | VARCHAR (18) | The unique ID of a grouper of medication (ERX) records that are part of a pharmaceutical class for pain medications but do not require follow-up pain reassessment. This column can be joined to GROUPER_COMPILED_REC_LIST.BASE_GROUPER_ID to get the medication records in the grouper. |
| REQUIRED_DOC_TASK_TEMPLATE_ID | VARCHAR (18) | Task template that contains required documentation configuration for system definitions. |
| OB_MOLAR_IS_ABORTION_YN | VARCHAR (1) |  |
| OPIOID_MED_GROUPER_ID | VARCHAR (18) | Medication grouper that identifies opioid medications. |
| NALOXONE_MED_GRP_ID | VARCHAR (18) | Medication grouper that identifies naloxone (opioid antagonist) medications. |
| IMM_ID_TYPE_ID | NUMERIC (18,0) | The internal ID type (IIT) used to map Immunizations (LIM) to Vaccine Administered (CVX) codes. |
| NO_EPISIOTOMY_C | INTEGER |  |
| NO_PERINLAC_C | INTEGER |  |
| OPIOID_OD_GROUPER_ID | VARCHAR (18) | The grouper that contains the diagnoses documented when a patient presents with an opioid overdose. |
| EMPR_RSLT_POOL_ID | NUMERIC (18,0) | The unique ID of the default In Basket pool which will receive Results Routing messages for confidential employer screening orders. |
| MED_RFL_TYPE_C | VARCHAR (66) |  |
| PED_BLOOD_GROUPER_ID | VARCHAR (18) | This grouper contains all transfuse and prepare blood procedures (EAP) for pediatric patients. This is used by reporting to present information correctly. This does not affect ordering or other ways EAP records are used. |
| SUSP_REACT_FLO_MEAS_ID | VARCHAR (18) | This flowsheet row is used to track suspected reactions to blood transfusions. |
| VV_SUCCESS_LEN_IN_SECONDS | INTEGER | The number of seconds that a video visit must last in order for it to be counted as successful in reporting content. Only time spent in a connection with two or more parties is counted. |
| PREGNANCY_LENGTH | INTEGER | How long a full term pregnancy lasts in days, from last menstrual period to estimated date of delivery. |
| WND_POST_PROC_ASMT_YN | VARCHAR (1) |  |
| FAM_HX_OTHER_COND_C | INTEGER |  |
| OB_ATTEND_ATTRIBUTION_C | INTEGER |  |
| OUD_EDG_GROUPER_ID | VARCHAR (18) | This item is meant to store a grouper containing opioid use disorder diagnoses to be used in MOUD metric calculation. |
| BUP_FOR_OUD_GROUPER_ID | VARCHAR (18) | Stores the ERX grouper associated with category value 12-Buprenorphine for Opioid Use Disorder in RG LSD 10715 for use in MOUD metrics for the executive packet. |
| ALRGY_RXN_TYP_LNK_TABLE_ID | NUMERIC (18,0) | AIF table ID that maps Allergy Reaction (I LPL 3008) to one or more allowed Allergy Reaction Types (I LPL 3060). This along with Reaction Type Acuity level AIF table in I LSD 3293 are used to determine allowed reaction types in the Allergies Reaction Type field for user-entered reactions. |
| ALRGY_RXN_TYP_ACUITY_TABLE_ID | NUMERIC (18,0) | AIF table ID that stores the acuity level for each Reaction Type (I LPL 3060). This along with Reaction and Reaction Type mapping AIF table in I LSD 3292 are used to determine allowed reaction types in the Allergies Reaction Type field for user-entered reactions. |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | FACILITY_ID | BMT_LSD_SETTINGS | FAC_ID | No | No | No |  |
| 1 | FACILITY_ID | COVID_19_SETTINGS | FAC_ID | No | No | No |  |
| 1 | FACILITY_ID | CPOE_REPORT_CONFIG | FAC_ID | No | No | No |  |
| 1 | FACILITY_ID | HEDIS_SOURCE_CONFIG | FAC_ID | No | No | No |  |
| 1 | FACILITY_ID | HP_CARE_MGMT_CONFIG | FAC_ID | No | No | No |  |
| 1 | FACILITY_ID | LSD_CAREPLAN | FAC_ID | No | No | No |  |
| 1 | FACILITY_ID | NOTE_TYPE_CUSTOM_MAPPING | FAC_ID | No | No | No |  |
| 1 | FACILITY_ID | ONC_SYSTEM_DEFS | FAC_ID | No | No | No |  |
| 1 | FACILITY_ID | RYAN_WHITE_CONFIG | FAC_ID | No | No | No |  |
| 1 | FACILITY_ID | SVI_CONFIG | FAC_ID | No | No | No |  |
| 1 | FACILITY_ID | SYSTEM_GENERIC_EXT_PROC | FAC_ID | No | No | No |  |
| 1 | FACILITY_ID | TXP_LSD_SETTINGS | FAC_ID | No | No | No |  |
| 1 | FACILITY_ID | TXP_SETTINGS | FAC_ID | No | No | No |  |
| 1 | FACILITY_ID | VBA_SYSTEM_SETTINGS | FAC_ID | No | No | No |  |
| 1 | FACILITY_ID | VBPM_DFLT_ATTRIBUTION | FAC_ID | No | No | No |  |
| 1 | FACILITY_ID | WOUND_LSD_NOADD_SINGLE | FAC_ID | No | No | No |  |
| 2 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 2 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 2 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 3 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 4 | PREGNANCY_RATG_C | ZC_PREGNANCY_RATG | PREGNANCY_RATG_C | No | No | No |  |
| 5 | LACTATION_RATG_C | ZC_LACTATION_RATG | LACTATION_RATG_C | No | No | No |  |
| 6 | OB_CSECT_GRPER_ID | GROUPER_ITEMS | GROUPER_ID | No | No | No |  |
| 6 | OB_CSECT_GRPER_ID | GROUPER_ITEMS_2 | GROUPER_ID | No | No | No |  |
| 8 | CHK_SER_PHR_C | ZC_CHK_SER_PHR | CHK_SER_PHR_C | No | No | No |  |
| 14 | ELEC_FETAL_MON_ID | FLO_CNTX_INFO | ID | No | No | No |  |
| 14 | ELEC_FETAL_MON_ID | IP_FLO_GP_DATA | FLO_MEAS_ID | No | No | No |  |
| 14 | ELEC_FETAL_MON_ID | IP_FLO_GP_DATA_2 | FLO_MEAS_ID | No | No | No |  |

_(79 total; showing first 30)_
