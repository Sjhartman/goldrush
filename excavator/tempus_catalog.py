"""
Specialist: Tempus catalog data extraction (Script 5b).

Generates a self-contained Python script (not SQL) that runs on the cluster
against Tempus catalog TSV files on the NFS mount. The generated script reads
cohort MRNs from the cohort SQL export (Databricks -> TSV), resolves them to
Tempus accession IDs via patient_clarity.tsv, and extracts approved elements.

Routing (what goes here vs tempus_databricks.py):
  CATALOG (this module):
    - Somatic DNA mutations      (accsn_variant_somatic.tsv)
    - Germline DNA mutations     (accsn_variant_germline_filtered.tsv)
    - Allelic fraction / VAF     (embedded in somatic variants)
    - RNA expression / TPM       (CPM_tables on NFS)
  DATABRICKS SQL (tempus_databricks.py):
    - CNV / copy number variants
    - MSI, TMB, HRD
    - RNA fusions
    - Clinically reported variant classifications
"""

from pathlib import Path
from datetime import datetime

# ---------------------------------------------------------------------------
# Element routing — keywords that map an approved element to a catalog step
# ---------------------------------------------------------------------------

_SOMATIC_KEYWORDS = {
    "somatic", "dna mutation", "snv", "indel", "variant", "genomic alteration",
    "allelic fraction", "vaf", "variant allele", "point mutation", "mutation",
}

_GERMLINE_KEYWORDS = {
    "germline", "inherited", "hereditary", "pathogenic variant",
}

_RNA_KEYWORDS = {
    "rna", "transcriptomic", "expression", "tpm", "cpm", "gene expression",
    "mrna", "transcript",
}


def _match(element_name: str, keywords: set) -> bool:
    name_lower = element_name.lower()
    return any(kw in name_lower for kw in keywords)


def _classify_elements(catalog_elements: list) -> dict:
    """Return dict of which catalog steps are needed."""
    want_somatic  = any(_match(e["element"], _SOMATIC_KEYWORDS)  for e in catalog_elements)
    want_germline = any(_match(e["element"], _GERMLINE_KEYWORDS) for e in catalog_elements)
    want_rna      = any(_match(e["element"], _RNA_KEYWORDS)      for e in catalog_elements)
    return {
        "somatic":  want_somatic,
        "germline": want_germline,
        "rna":      want_rna,
    }


# ---------------------------------------------------------------------------
# Script template
# ---------------------------------------------------------------------------

def generate(fields: dict, catalog_elements: list) -> str:
    """
    Generate a self-contained Python extraction script for Tempus catalog data.
    Returns the script as a string; the orchestrator writes it to a .py file.
    """
    irb   = fields.get("irb_summary", {})
    prot  = irb.get("protocol_number", "N/A")
    pi    = irb.get("pi_name", "Unknown PI")
    ts    = datetime.now().strftime("%Y-%m-%d")

    steps = _classify_elements(catalog_elements)
    need_variants = steps["somatic"] or steps["germline"]

    element_list = "\n".join(f"#   - {e['element']}" for e in catalog_elements)

    # Build step sections conditionally
    vcf_completion_fn = ""
    if need_variants:
        vcf_completion_fn = '''
def completion_label_two_callers(row, col_pindel, col_freebayes):
    pindel    = bool(row[col_pindel])
    freebayes = bool(row[col_freebayes])
    if pindel and freebayes:
        return "complete"
    elif pindel:
        return "pindel_only"
    elif freebayes:
        return "freebayes_only"
    else:
        return "missing"


def build_completion_maps(catalog: str) -> tuple:
    """Returns (somatic_map, germline_map) DataFrames with [accessionId, vcf_complete]."""
    print("Building VCF completion maps...")
    nonxf = pd.read_csv(os.path.join(catalog, "vcf_presence_nonxf.tsv"), sep="\\t")
    xf    = pd.read_csv(os.path.join(catalog, "vcf_presence_xf.tsv"),    sep="\\t")

    nonxf_som = nonxf[[ACCSN_COL]].copy()
    nonxf_som["vcf_complete"] = nonxf.apply(
        lambda r: completion_label_two_callers(r, "soma.pindel.vcf", "soma.freebayes.vcf"), axis=1)
    nonxf_ger = nonxf[[ACCSN_COL]].copy()
    nonxf_ger["vcf_complete"] = nonxf.apply(
        lambda r: completion_label_two_callers(r, "germ.pindel.vcf", "germ.freebayes.vcf"), axis=1)

    xf_som = xf[[ACCSN_COL]].copy()
    xf_som["vcf_complete"] = xf["soma.vardict.vcf"].apply(lambda x: "complete" if bool(x) else "missing")
    xf_ger = xf[[ACCSN_COL]].copy()
    xf_ger["vcf_complete"] = xf["germ.vardict.vcf"].apply(lambda x: "complete" if bool(x) else "missing")

    somatic_map  = pd.concat([nonxf_som, xf_som], ignore_index=True).drop_duplicates(ACCSN_COL)
    germline_map = pd.concat([nonxf_ger, xf_ger], ignore_index=True).drop_duplicates(ACCSN_COL)
    return somatic_map, germline_map
'''

    somatic_step = ""
    if steps["somatic"]:
        somatic_step = '''
def extract_somatic_variants(cohort_accsns: set, somatic_map, catalog: str, out_dir: Path):
    print("Extracting somatic variants (DNA mutations + allelic fraction)...")
    df = pd.read_csv(os.path.join(catalog, "accsn_variant_somatic.tsv"), sep="\\t")
    df = df.merge(somatic_map, on=ACCSN_COL, how="left")
    df = df[df[ACCSN_COL].astype(str).isin(cohort_accsns)]
    df.to_csv(out_dir / "somatic_variants.tsv", sep="\\t", index=False)
    print(f"  somatic_variants.tsv: {len(df)} rows")
    print(f"  vcf_complete: {df['vcf_complete'].value_counts().to_dict()}")
'''

    germline_step = ""
    if steps["germline"]:
        germline_step = '''
def extract_germline_variants(cohort_accsns: set, germline_map, catalog: str, out_dir: Path):
    print("Extracting germline variants (DuckDB -- large file)...")
    germline_path = os.path.join(catalog, "accsn_variant_germline_filtered.tsv")
    con = duckdb.connect()
    con.register("germline_map", germline_map)
    placeholders = ", ".join(f"'{a}'" for a in cohort_accsns)
    result = con.execute(f"""
        SELECT g.*, m.vcf_complete
        FROM read_csv_auto('{germline_path}', delim='\\t', header=true) AS g
        LEFT JOIN germline_map AS m ON g.accessionId = m.accessionId
        WHERE g.accessionId IN ({placeholders})
    """).df()
    con.close()
    result.to_csv(out_dir / "germline_variants.tsv", sep="\\t", index=False)
    print(f"  germline_variants.tsv: {len(result)} rows")
    print(f"  vcf_complete: {result['vcf_complete'].value_counts().to_dict()}")
'''

    rna_step = ""
    rna_dir_config = "# RNA_CPM_DIR not needed for this request" if not steps["rna"] else ""
    if steps["rna"]:
        rna_dir_config = 'RNA_CPM_DIR = "/mnt/citadel3/clinical/data/Tempus/RNAseq/<YYYYMMDD_HHMMSS>"  # update to current pipeline run dir'
        rna_step = '''
def extract_rna_tpm(cohort_accsns: set, out_dir: Path):
    print("Extracting RNA TPM tables...")
    batches = {
        "RSv1_paired": "tpm_RSv1.tsv",
        "RSv2_split":  "tpm_RSv2_split.tsv",
        "RSv2_paired": "tpm_RSv2_paired.tsv",
    }
    for batch_name, filename in batches.items():
        tpm_path = os.path.join(RNA_CPM_DIR, filename)
        if not os.path.exists(tpm_path):
            print(f"  WARNING: {tpm_path} not found, skipping {batch_name}")
            continue
        tpm = pd.read_csv(tpm_path, sep="\\t", index_col=0)
        cohort_cols = [c for c in tpm.columns if str(c).removesuffix("_bam") in cohort_accsns]
        tpm[cohort_cols].rename(columns=lambda c: str(c).removesuffix("_bam")).to_csv(
            out_dir / f"rna_tpm_{batch_name}.tsv", sep="\\t"
        )
        print(f"  rna_tpm_{batch_name}.tsv: {len(tpm)} genes x {len(cohort_cols)} samples")
'''

    # Build call block
    variant_map_call = ""
    if need_variants:
        variant_map_call = "    somatic_map, germline_map = build_completion_maps(CATALOG_DIR)\n"

    somatic_call  = "    extract_somatic_variants(cohort_accsns, somatic_map, CATALOG_DIR, OUTPUT_DIR)\n" if steps["somatic"] else ""
    germline_call = "    extract_germline_variants(cohort_accsns, germline_map, CATALOG_DIR, OUTPUT_DIR)\n" if steps["germline"] else ""
    rna_call      = "    extract_rna_tpm(cohort_accsns, OUTPUT_DIR)\n" if steps["rna"] else ""

    script = f'''\
# =============================================================================
# Script 5b: Tempus Catalog Extraction
# IRB Protocol : {prot}
# PI           : {pi}
# Generated    : {ts}
# Generated by : goldrush excavator / tempus_catalog.py
#
# Run on the cluster. Update CONFIG below before running.
# Requirements : pandas, duckdb
#
# Approved catalog elements:
{element_list}
# =============================================================================

import os
import pandas as pd
import duckdb
from pathlib import Path

# =============================================================================
# CONFIG -- update before running
# =============================================================================

# Export of cohort SQL from Databricks. Must contain an 'mrn' column.
COHORT_TSV  = "cohort.tsv"

# Tempus catalog data_explorer directory (NFS mount on cluster).
# Update to the current catalog version path.
CATALOG_DIR = "/mnt/citadel3/clinical/data/Tempus/dashboard_inventory_files/<catalog_version>/tempus-catalog/backend/data_explorer"

{rna_dir_config}

OUTPUT_DIR  = Path("tempus_catalog_output")

# Accession ID column name (consistent across all catalog files)
ACCSN_COL   = "accessionId"

# =============================================================================
# STEP 1: Load cohort MRNs from Databricks cohort export
# =============================================================================

def load_cohort_mrns() -> set:
    print("Step 1: Loading cohort MRNs from", COHORT_TSV)
    df = pd.read_csv(COHORT_TSV, sep="\\t")
    if "mrn" not in df.columns:
        raise ValueError(f"cohort TSV must have an 'mrn' column. Found: {{list(df.columns)}}")
    mrns = set(df["mrn"].dropna().astype(str))
    print(f"  {{len(mrns)}} unique MRNs in cohort")
    return mrns

# =============================================================================
# STEP 2: Resolve MRNs to Tempus accession IDs via patient_clarity.tsv
# =============================================================================

def resolve_accession_ids(cohort_mrns: set) -> set:
    print("Step 2: Resolving accession IDs via patient_clarity.tsv...")
    clarity = pd.read_csv(os.path.join(CATALOG_DIR, "patient_clarity.tsv"), sep="\\t")
    matched = clarity[clarity["emrid"].astype(str).isin(cohort_mrns)]
    accsns  = set(matched["tempus_accession"].dropna().astype(str))

    inventory = pd.read_csv(os.path.join(CATALOG_DIR, "bam_fq_inventory_plusMissing.tsv"), sep="\\t")
    inventory = inventory[inventory["omic"].notna()]
    accsns    = accsns & set(inventory[ACCSN_COL].dropna().astype(str))
    print(f"  {{len(accsns)}} accession IDs after intersect with bam inventory")
    return accsns
{vcf_completion_fn}{somatic_step}{germline_step}{rna_step}
# =============================================================================
# STEP 7: Specimen-level metadata
# =============================================================================

def extract_specimen(cohort_accsns: set, catalog: str, out_dir: Path):
    print("Extracting specimen-diagnosis table...")
    specimen = pd.read_csv(os.path.join(catalog, "collectionDateDiagnosis.tsv"), sep="\\t")
    specimen["sampleSite"] = specimen["primarySampleSite"].combine_first(specimen["sampleSite"])
    drop = [c for c in ["primarySampleSite", "Unnamed: 0", "diagnosis",
                         "diagnosisDate", "originPathLabDiagnosis"] if c in specimen.columns]
    specimen = specimen.drop(columns=drop).dropna(subset=["tempusId"])
    specimen = specimen[specimen["sampleCategory"] != "normal"]
    specimen = specimen[specimen[ACCSN_COL].astype(str).isin(cohort_accsns)]

    clarity = pd.read_csv(os.path.join(catalog, "patient_clarity.tsv"), sep="\\t")
    diag_cols = [c for c in ["tempus_accession", "emrid", "current_icd10_list",
                              "tempus_returned_diagnosis", "DX_NAME"] if c in clarity.columns]
    specimen = specimen.merge(clarity[diag_cols].drop_duplicates(),
                              left_on=ACCSN_COL, right_on="tempus_accession", how="left")
    if "tempus_accession" in specimen.columns:
        specimen = specimen.drop(columns=["tempus_accession"])
    specimen.to_csv(out_dir / "specimen_diagnosis.tsv", sep="\\t", index=False)
    print(f"  specimen_diagnosis.tsv: {{len(specimen)}} rows")

# =============================================================================
# MAIN
# =============================================================================

def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    cohort_mrns  = load_cohort_mrns()
    cohort_accsns = resolve_accession_ids(cohort_mrns)

{variant_map_call}{somatic_call}{germline_call}{rna_call}    extract_specimen(cohort_accsns, CATALOG_DIR, OUTPUT_DIR)

    print("\\nDone. Outputs written to:", OUTPUT_DIR.resolve())


if __name__ == "__main__":
    main()
'''
    return script
