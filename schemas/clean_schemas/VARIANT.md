# VARIANT

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=VARIANT

## Description

Main variant result table.

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
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| RECORD_STATUS_C | INTEGER |  |
| VARIANT_TYPE_C | INTEGER |  |
| VARIANT_NAME | VARCHAR (192) | The name assigned to the variant. |
| HGVS_NAME | VARCHAR (192) | The HGVS name assigned to the variant. |
| PAT_ID | VARCHAR (18) | The unique identifier of the patient associated with the variant. |
| RQG_GROUPER_ID | NUMERIC (18,0) | The unique ID of the non-participating submitter's patient (RQG) associated with the variant. |
| GENOME_ASSEMBLY_C | INTEGER |  |
| CHROMOSOME_C | INTEGER |  |
| START_POSITION | INTEGER | The position where the variation starts. |
| STOP_POSITION | INTEGER | The position where the variation ends. |
| DNA_REGION | VARCHAR (100) | The region of a chromosome or gene where the variant is located. For example, this could be an exon, intron, regulatory region, or a functional domain. |
| GENE_C | INTEGER |  |
| GENE | VARCHAR (50) | The gene name. This column will be deprecated in the February 2027 release. It is being replaced by column REPORTED_GENE_NAME in table VARIANT_GENES. |
| GENE_SYSTEM_C | INTEGER |  |
| TRANSCRIPT_REF_SEQ | VARCHAR (20) | The external identifier defining the Transcript Reference Sequence. |
| TRANSCRIPT_SYSTEM_C | INTEGER |  |
| DNA_CHANGE | VARCHAR (140) | The change at the DNA level relative to the Transcript Reference Sequence. |
| DNA_VAR_TYPE_C | INTEGER |  |
| AMINO_ACID_CHANGE | VARCHAR (140) | The change at the amino acid (protein) level caused by the DNA change. |
| AA_VAR_TYPE_C *(deprecated)* | INTEGER |  |
| PROTEIN_REF_SEQ | VARCHAR (20) | The external identifier defining the Protein Reference Sequence. |
| CHROMOSOME_REF_SEQ *(deprecated)* | VARCHAR (20) |  |
| GENOMIC_REF_SEQ | VARCHAR (20) | The external ID defining the Genomic Reference Sequence. |
| GEN_SEQ_SYSTEM_C | INTEGER |  |
| REFERENCE_ALLELE | VARCHAR (1005) | The DNA string in the reference sequence (Ref Allele) with which the DNA string in the test sample differs. |
| OBSERVED_ALLELE | VARCHAR (1005) | The DNA sequence in the test sample (Ref Allele) that is different from the DNA sequence in the reference sequence (Ref Allele). |
| GENOMIC_DNA_CHANGE | VARCHAR (140) | The change at the DNA level relative to the Genomic Reference Sequence. |
| ALLELIC_STATE_C | INTEGER |  |
| ALLELIC_FREQUENCY | NUMERIC (18,5) | Reports the percentage of all of the reads at this genomic location that were represented by the given allele. For homozygotes it will be close to 100%; for heterozygotes it will be close to 50%. It can be a smaller number when there are mosaics or multiple chromosomes, or mixtures of tumor cells and normal cells. It is stored in the system as a decimal between 0 and 1 - this is calculated by dividing the percentage by 100. This field displays to end users as Variant Allele Fraction. |
| CYTOGENETIC_LOC | VARCHAR (100) | The cytogenetic location of the variant. |
| ALLELIC_READ_DEPTH | INTEGER | The read depth (or coverage) for the variant. |
| PENETRANCE | NUMERIC (18,5) | The penetrance for the variant. |
| GENOMIC_SOURCE_C | INTEGER |  |
| METHOD_TYPE_C | INTEGER |  |
| ALLELIC_PHASE_C | INTEGER |  |
| ALLELIC_BASIS_C | INTEGER |  |
| BOUNDARY_PRECISION | VARCHAR (100) | Structural variant narrative description of the boundary precision. |
| REPORTED_ACGH_RATIO | NUMERIC (18,5) | Structural variant reported aCGH Ratio. |
| ALLELE_LENGTH | INTEGER | Structural variant allele length. |
| INNER_START | INTEGER | Structural variant inner start position. |
| INNER_END | INTEGER | Structural variant inner end position. |
| OUTER_START | INTEGER | Structural variant outer start position. |
| OUTER_END | INTEGER | Structural variant outer end position. |
| COPY_NUMBER | INTEGER | Genomic structural variant copy number as an integer. To prepare for the future deprecation of this column, your content should use either the COPY_NUMBER_LOWER or the COPY_NUMBER_UPPER columns or both. |
| ASSESSMENT_C | INTEGER |  |
| CLINICAL_SIGNIF_C | INTEGER |  |
| GENOTYPE | VARCHAR (200) | Genotype Name, used in combination with the column GENE (VAR 1210) to describe a Pharmacogenomic Variant. |
| PGX_DRUG_METAB_C | INTEGER |  |
| PGX_DRUG_EFFICACY_C | INTEGER |  |
| PGX_HIGH_RISK_C | INTEGER |  |
| VARIANT_FUNC_EFFECT_C | INTEGER |  |
| VARIANT_MOLEC_CONSEQ_C | INTEGER |  |
| GENOTYPE_IDENT | VARCHAR (200) | Returns the genotype (VARIANT.GENOTYPE) converted to a standardized format. Use VARIANT.GENOTYPE for display and VARIANT.GENOTYPE_IDENT for identifying same genotypes regardless of formatting used in VARIANT.GENOTYPE |
| MOSAICISM_C | INTEGER |  |
| FRACTIONAL_COPY_NUMBER | NUMERIC (18,2) | Genomic structural variant copy number with two decimal places of precision. To prepare for the future deprecation of this column, your content should use either the COPY_NUMBER_LOWER or the COPY_NUMBER_UPPER columns or both. |
| IS_AMPLIFICATION_YN | VARCHAR (1) |  |
| GENE_ID | NUMERIC (18,0) | Gene where the variant is located. This column will be deprecated in the February 2027 release. It is being replaced by column GENE_ID in table VARIANT_GENES. |
| IS_EXTERNAL_YN | VARCHAR (1) |  |
| PERSISTENT_PAT_ID | VARCHAR (18) | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. While the ID in the PAT_ID column will get cleared out when its variant record is superseded, the value in this column will continue to indicate the patient. |
| PERSISTENT_RQG_GROUPER_ID | NUMERIC (18,0) | The historically maintained requisition grouper ID. While the requisition grouper ID in item 99 will be cleared out of a VAR record when a new VAR superscedes it, this will retain the grouper link. |
| PGX_DRUG_TXPORT_C | INTEGER |  |
| TOTAL_REPEAT_NUMBER *(deprecated)* | INTEGER |  |
| PGX_ACT_SCORE_LOWER | NUMERIC (18,3) | The lower bound of the activity score on the pharmacogenomic variant. If the activity score is a value and not a range, this will have the same value as PGX_ACT_SCORE_UPPER. If the activity score is a range without a lower bound specified, this column will contain 0. |
| PGX_ACT_SCORE_UPPER | NUMERIC (18,3) | The upper bound of the activity score on the pharmacogenomic variant. If the activity score is a value and not a range, this will have the same value as PGX_ACT_SCORE_LOWER. If the activity score is a range without an upper bound specified, this column will contain 99999. |
| DISPLAY_NAME | VARCHAR (300) | The name used when the variant is displayed |
| ISCN_NAME | VARCHAR (300) | The ISCN name assigned to the variant. |
| COPY_NUMBER_LOWER | NUMERIC (9,2) | Lower bound for the copy number of a variant. |
| COPY_NUMBER_UPPER | NUMERIC (9,2) | Upper bound for the copy number of a variant. |
| VARIANT_FINDING_TYPE_C | INTEGER |  |
| AFFECTED_EXON_START | INTEGER | The lowest exon number affected by the variant |
| AFFECTED_EXON_END | INTEGER | The highest exon number affected by the variant |
| AFFECTED_INTRON_START | INTEGER | The lowest intron number affected by the variant |
| AFFECTED_INTRON_END | INTEGER | The highest intron number affected by the variant |
| VARIANT_ENTRY_SRC_C | INTEGER |  |
| STDRD_AMINO_ACID_CHANGE | VARCHAR (140) | Parsed amino acid change based off of the original amino acid change string |
| CMPT_VARIANT_MOLEC_CONSEQ_C | INTEGER |  |
| CMPT_AMINO_ACID_START_CODON | INTEGER | Start position of amino acid change |
| CMPT_AMINO_ACID_END_CODON | INTEGER | End position of amino acid change |
| CMPT_AMINO_ACID_REFERENCE | VARCHAR (140) | Reference amino acid that the amino acid changed "from" |
| CMPT_AMINO_ACID_ALTERNATE | VARCHAR (140) | Alternate amino acid that the amino acid changed "to" |
| CLONAL_HEMAT_C | INTEGER |  |
| STDRD_TRANSCRIPT_REF_SEQ | VARCHAR (30) | The transcript reference sequence the system validates based off of the lab-provided transcript, protein, and genomic reference sequence values. Follows either the NCBI or EMBL standard. |
| STDRD_GENOMIC_REF_SEQ | VARCHAR (30) | The genomic reference sequence the system validates based off of the lab-provided transcript, protein, and genomic reference sequence values. Follows either the NCBI or EMBL standard. |
| STDRD_PROTEIN_REF_SEQ | VARCHAR (30) | The protein reference sequence the system validates based off of the lab-provided transcript, protein, and genomic reference sequence values. Follows either the NCBI or EMBL standard. |
| TOTAL_REPEAT_NUM_LOWER | INTEGER | The lower bound of the sum of all repeat numbers for a repeat expansion variant. |
| TOTAL_REPEAT_NUM_UPPER | INTEGER | The upper bound of the sum of all repeat numbers for a repeat expansion variant. |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| B-TREE INDEX | EIX_PATID_TYPE | PAT_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_PATID_TYPE | VARIANT_TYPE_C | 2 | Yes | Yes |  |
| B-TREE INDEX | EIX_VAR_PERSISTENT_PAT_ID | PERSISTENT_PAT_ID | 1 | Yes | Yes |  |
| B-TREE INDEX | EIX_VAR_RQG_ID | PERSISTENT_RQG_GROUPER_ID | 1 | Yes | Yes |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 2 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 2 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 3 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 4 | RECORD_STATUS_C | ZC_RECORD_STATUS_2 | RECORD_STATUS_2_C | No | No | No |  |
| 4 | RECORD_STATUS_C | ZC_RECORD_STS | RECORD_STS_C | No | No | No |  |
| 5 | VARIANT_TYPE_C | ZC_VARIANT_TYPE | VARIANT_TYPE_C | No | No | No |  |
| 8 | PAT_ID | ANTICOAG_SELF_REGULATING | PAT_ID | No | No | No |  |
| 8 | PAT_ID | CARE_COORDINATION | PAT_ID | Unknown | No | No |  |
| 8 | PAT_ID | CLAIMS_DERIVE_PAT_FLAGS | PAT_ID | No | No | No |  |
| 8 | PAT_ID | COMMUNITY_RESRC_REVIEWED | PAT_ID | No | No | No |  |
| 8 | PAT_ID | D_PAT_GEOGRAPHIC_CLASS | PAT_ID | Unknown | Unknown | No |  |
| 8 | PAT_ID | EPT_MEM_INFO | PAT_ID | No | No | No |  |
| 8 | PAT_ID | EXT_DATA_LAST_DONE | PAT_ID | No | No | No |  |
| 8 | PAT_ID | F_IBD_ADULT_FORM_PAT | PAT_ID | Unknown | Unknown | No |  |
| 8 | PAT_ID | HH_PAT_INFO | PAT_ID | Unknown | No | No |  |
| 8 | PAT_ID | HM_STATUS_UPD | PAT_ID | No | No | No |  |
| 8 | PAT_ID | IMMNZTN_LAST_REVIEW | PAT_ID | No | No | No |  |
| 8 | PAT_ID | PATIENT | PAT_ID | No | No | No |  |
| 8 | PAT_ID | PATIENT_2 | PAT_ID | No | No | No |  |
| 8 | PAT_ID | PATIENT_3 | PAT_ID | No | No | No |  |
| 8 | PAT_ID | PATIENT_4 | PAT_ID | No | No | No |  |
| 8 | PAT_ID | PATIENT_5 | PAT_ID | No | No | No |  |
| 8 | PAT_ID | PATIENT_6 | PAT_ID | No | No | No |  |
| 8 | PAT_ID | PATIENT_CONF_ADDR | PAT_ID | No | No | No |  |
| 8 | PAT_ID | PATIENT_MISC_COMMENTS | PAT_ID | No | No | No |  |
| 8 | PAT_ID | PATIENT_MYC | PAT_ID | Unknown | No | No |  |
| 8 | PAT_ID | PATIENT_OPT | PAT_ID | No | No | No |  |

_(115 total; showing first 30)_
