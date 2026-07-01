# VAR_PHENOTYPES

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=VAR_PHENOTYPES

## Description

The VAR_PHENOTYPES table contains the external phenotype identifier and the system that defined it.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | VAR |
| Release Version | Rel 2018 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| VARIANT_ID | NUMERIC (18,0) | The unique identifier for the variant record. |
| LINE | INTEGER | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| PHENOTYPE_SYSTEM_C | INTEGER |  |
| PHENOTYPE_CODE | VARCHAR (20) | The external phenotype code assigned by the phenotype coding system. |
| PHENOTYPE_NAME | VARCHAR (192) | Phenotype name of phenotypes associated with the variant |
| MODE_OF_INHERITANCE_C | INTEGER |  |
| PHENOTYPE_SPEC_PENETRANCE | NUMERIC (18,5) | The penetrance of a particular phenotype |
| PHENOTYPE_SPEC_DESC | VARCHAR (2046) | A free-text description of a particular phenotype |
| PHENOTYPE_SPEC_VAR_CLASS_C | INTEGER |  |
| PHENOTYPE_EFFECT_TYPE_C | INTEGER |  |
| PHENOTYPE_EFFECT_VAL_C | INTEGER |  |
| PHENOTYPE_ACTIVITY_SCORE_LOWER | NUMERIC (8,3) | The activity score of the pharmacogenomic variant, or the lowest value the activity score can be based on lab input |
| PHENOTYPE_ACTIVITY_SCORE_UPPER | NUMERIC (8,3) | The highest value the activity score can be based on lab input |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | VARIANT_ID | VARIANT | VARIANT_ID | No | No | No |  |
| 3 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 4 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 4 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 4 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 5 | PHENOTYPE_SYSTEM_C | ZC_PHENOTYPE_SYSTEM | PHENOTYPE_SYSTEM_C | No | No | No |  |
| 8 | MODE_OF_INHERITANCE_C | ZC_MODE_OF_INHERITANCE | MODE_OF_INHERITANCE_C | No | No | No |  |
| 11 | PHENOTYPE_SPEC_VAR_CLASS_C | ZC_CLINICAL_SIGNIF | CLINICAL_SIGNIF_C | No | No | No |  |
| 12 | PHENOTYPE_EFFECT_TYPE_C | ZC_PHENOTYPE_EFFECT_TYPE | PHENOTYPE_EFFECT_TYPE_C | No | No | No |  |
| 13 | PHENOTYPE_EFFECT_VAL_C | ZC_PHENOTYPE_EFFECT_VAL | PHENOTYPE_EFFECT_VAL_C | No | No | No |  |
