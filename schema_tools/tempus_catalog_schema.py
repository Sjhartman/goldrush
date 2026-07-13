"""
catalog_schema.py

Scans all TSV files in the Tempus catalog data_explorer directory and writes
a human-readable schema to tempus_catalog_schema.txt in the working directory.

For each file reports:
  - Row count (fast, via DuckDB)
  - Per-column: dtype, null %, unique count
"""

import pandas as pd
import duckdb
from pathlib import Path

# ---------------------------------------------------------------------------
# CONFIG
# ---------------------------------------------------------------------------

CATALOG_DIR = (
    "/mnt/citadel3/clinical/data/Tempus/dashboard_inventory_files"
    "/tempus_catalog_260616_v2.0_git72cf943/tempus-catalog/backend/data_explorer"
)
OUTPUT_PATH = Path("tempus_catalog_schema.txt")
SAMPLE_ROWS = 5_000  # rows used for dtype / null inference

# ---------------------------------------------------------------------------
# HELPERS
# ---------------------------------------------------------------------------

def row_count(path: Path, con: duckdb.DuckDBPyConnection):
    try:
        return con.execute(
            f"SELECT COUNT(*) FROM read_csv_auto('{path}', delim='\t', header=true, ignore_errors=true)"
        ).fetchone()[0]
    except Exception as e:
        return None, str(e)

def schema_block(path: Path, con: duckdb.DuckDBPyConnection) -> list[str]:
    lines = []
    sep = "=" * 72

    lines.append(f"\n{sep}")
    lines.append(f"FILE: {path.name}")
    lines.append(sep)

    n = row_count(path, con)
    if isinstance(n, tuple):
        lines.append(f"  ERROR counting rows: {n[1]}")
        return lines

    try:
        sample = pd.read_csv(path, sep="\t", nrows=SAMPLE_ROWS, low_memory=False)
    except Exception as e:
        lines.append(f"  ERROR reading sample: {e}")
        return lines

    n_sample = min(SAMPLE_ROWS, n)
    lines.append(f"  Rows: {n:,}  |  Columns: {len(sample.columns)}")
    lines.append(f"  (dtype / null stats from first {n_sample:,} rows)")
    lines.append("")

    col_w = max((len(c) for c in sample.columns), default=6)
    lines.append(f"  {'Column':<{col_w}}  {'Dtype':<12}  {'Null%':>6}  {'Uniq':>8}")
    lines.append("  " + "-" * (col_w + 32))

    for col in sample.columns:
        s        = sample[col]
        null_pct = s.isna().mean() * 100
        n_uniq   = s.nunique(dropna=True)
        lines.append(
            f"  {col:<{col_w}}  {str(s.dtype):<12}  {null_pct:>5.1f}%  {n_uniq:>8,}"
        )

    return lines

# ---------------------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------------------

def main():
    tsv_files = sorted(Path(CATALOG_DIR).glob("*.tsv"))
    print(f"Found {len(tsv_files)} TSV files in data_explorer/")

    con = duckdb.connect()
    all_lines = [
        f"Tempus Catalog Schema",
        f"Directory: {CATALOG_DIR}",
        f"Files scanned: {len(tsv_files)}",
        f"Sample size for inference: {SAMPLE_ROWS:,} rows",
    ]

    for f in tsv_files:
        print(f"  Processing {f.name}...")
        all_lines.extend(schema_block(f, con))

    con.close()

    OUTPUT_PATH.write_text("\n".join(all_lines) + "\n")
    print(f"\nDone. Schema written to: {OUTPUT_PATH.resolve()}")

if __name__ == "__main__":
    main()
