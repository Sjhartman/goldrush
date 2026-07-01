# V_OB_DEL_RECORDS

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=V_OB_DEL_RECORDS

## Description

This view is used to display information relevant to a baby's delivery record on one row. Note that babies that are unlinked from their mother will not appear in this view.

## Metadata

| Property | Value |
| --- | --- |
| Type | View |
| Release Version | Rel 2012 |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| BABY_ID | VARCHAR (18) | Virtual column containing the patient ID of the baby. Can be linked to the column PAT_ID in the PATIENT table. |
| MOM_ID | VARCHAR (18) | Virtual column containing the patient ID of the mother. Can be linked to the column PAT_ID in the PATIENT table. |
| DELREC_ID | NUMERIC (18,0) | Virtual column containing the baby's delivery record ID. This can be linked to the EPISODE_ID in the EPISODE table or SUMMARY_BLOCK_ID in the OB_HSB_DELIVERY table. |
| DELMETH_C | VARCHAR (66) |  |
| GA | VARCHAR (30) | Virtual column containing the gestational age at birth in weeks and days. Ex. '39w 3d'. |
| PROV_NAME | VARCHAR (200) | Virtual column containing the name of the provider who delivered the baby. |
| DEL_DTTM | DATETIME (Local) | Virtual column containing the date and time of delivery, converted to local time. For values that are not fully confident (for example, if just the year was documented), the confidence is stored in the OB_HSB_DELIVERY.OB_HX_OUTC_FUZZY_C. For those values, this column contains midnight in the time zone the delivery was documented on the earliest date that the value could represent, converted to the local time zone. |
| LIVING_C | INTEGER |  |
| APGAR1 | VARCHAR (10) |  |
| APGAR5 | VARCHAR (10) |  |
| APGAR10 | VARCHAR (10) |  |
| BIRTHWT | VARCHAR (10) | Virtual column containing the baby's birth weight in grams (converted from ounces). |
| ANESTH_CONC | No | Virtual column containing a comma delimeted list of all anesthesia methods for the baby on one row. Ex. 'Epidural, Spinal, General'. |
| INDUCT_CONC | No | Virtual column containing a comma delimeted list of all induction methods for the baby on one row. Ex. 'Cervidil, Foley/EASI'. |
| LACER_CONC | No | Virtual column containing a comma delimeted list of all laceration methods for the baby on one row. Ex. '1st, Vaginal'. |
| EPISIO_CONC | No | Virtual column containing a comma delimeted list of all episiotomy methods for the baby on one row. Ex. 'Median, Left Mediolateral' |
| AUGMENT_CONC | No | Virtual column containing a comma delimeted list of all augmentation methods for the baby on one row. Ex. 'AROM, Oxytocin'. |
| CERVRIPE_CONC | No | Virtual column containing a comma delimeted list of all cervical ripening methods for the baby on one row. Ex. 'Gel, Misoprostol' |
| DEPT_ID | NUMERIC (18,0) | Virtual column containing the ID of the department where the birth occurred. This can be used to link to the CLARITY_DEP table. |
| BABY_NAME | VARCHAR (200) | Virtual column containing the baby's name. |
| MOM_NAME | VARCHAR (200) | Virtual column containing the mom's name. |
| OB_DEL_DELIV_MD_ID | VARCHAR (18) | Stores the unique ID of the provider (SER) who was responsible for delivering this infant. The data in this column are entered in the Delivery Summary activity and stored in the delivery record. |
| PREG_EPISODE_ID | NUMERIC (18,0) | The value for this column is mom's pregnancy episode ID. This can be used to link from the delivery record to the corresponding pregnancy episode. Link EPISODE.OB_DEL_PREG_EPI_ID to EPISODE.EPISODE_ID, where the first table represents the delivery record and the second is the pregnancy episode. |
| MOM_CSN | NUMERIC (18,0) | This item stores the contact serial number of the admission date in the mother's record during which the delivery occurred. |
| BABY_CSN | NUMERIC (18,0) | This item stores the contact serial number in the baby's record for the birth encounter. |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | BABY_ID | ANTICOAG_SELF_REGULATING | PAT_ID | No | Unknown | No |  |
| 1 | BABY_ID | CARE_COORDINATION | PAT_ID | Unknown | Unknown | No |  |
| 1 | BABY_ID | CLAIMS_DERIVE_PAT_FLAGS | PAT_ID | No | Unknown | No |  |
| 1 | BABY_ID | COMMUNITY_RESRC_REVIEWED | PAT_ID | No | Unknown | No |  |
| 1 | BABY_ID | D_PAT_GEOGRAPHIC_CLASS | PAT_ID | Unknown | Unknown | No |  |
| 1 | BABY_ID | EPT_MEM_INFO | PAT_ID | No | Unknown | No |  |
| 1 | BABY_ID | EXT_DATA_LAST_DONE | PAT_ID | No | Unknown | No |  |
| 1 | BABY_ID | F_IBD_ADULT_FORM_PAT | PAT_ID | Unknown | Unknown | No |  |
| 1 | BABY_ID | HH_PAT_INFO | PAT_ID | Unknown | Unknown | No |  |
| 1 | BABY_ID | HM_STATUS_UPD | PAT_ID | No | Unknown | No |  |
| 1 | BABY_ID | IMMNZTN_LAST_REVIEW | PAT_ID | No | Unknown | No |  |
| 1 | BABY_ID | PATIENT | PAT_ID | No | Unknown | No |  |
| 1 | BABY_ID | PATIENT_2 | PAT_ID | No | Unknown | No |  |
| 1 | BABY_ID | PATIENT_3 | PAT_ID | No | Unknown | No |  |
| 1 | BABY_ID | PATIENT_4 | PAT_ID | No | Unknown | No |  |
| 1 | BABY_ID | PATIENT_5 | PAT_ID | No | Unknown | No |  |
| 1 | BABY_ID | PATIENT_6 | PAT_ID | No | Unknown | No |  |
| 1 | BABY_ID | PATIENT_CONF_ADDR | PAT_ID | No | Unknown | No |  |
| 1 | BABY_ID | PATIENT_MISC_COMMENTS | PAT_ID | No | Unknown | No |  |
| 1 | BABY_ID | PATIENT_MYC | PAT_ID | Unknown | Unknown | No |  |
| 1 | BABY_ID | PATIENT_OPT | PAT_ID | No | Unknown | No |  |
| 1 | BABY_ID | PAT_ENC_LAST_HX_CT | PAT_ID | Unknown | Unknown | No |  |
| 1 | BABY_ID | PAT_RES_CODE | PAT_ID | No | Unknown | No |  |
| 1 | BABY_ID | PROB_LIST_REVIEWED | PAT_ID | No | Unknown | No |  |
| 1 | BABY_ID | REGADDL_PAT | PAT_ID | No | Unknown | No |  |
| 1 | BABY_ID | SCF_FHIR_MAP | PAT_ID | No | Unknown | No |  |
| 1 | BABY_ID | TEETH_REVIEWED | PAT_ID | No | Unknown | No |  |
| 1 | BABY_ID | VALID_PATIENT | PAT_ID | No | Unknown | No |  |
| 1 | BABY_ID | V_PAT_ABO | PAT_ID | Unknown | Unknown | No |  |
| 1 | BABY_ID | V_PAT_FACT | PAT_ID | Unknown | Unknown | No |  |

_(406 total; showing first 30)_
