#!/usr/bin/env python3
"""
Filter the full CMS ICD-10-CM order file to oncology-relevant codes.

Run once (or when the annual ICD-10 file updates):
    venv/bin/python tools/filter_icd10.py

Outputs ICD10_codes/icd10cm-oncology-<year>.csv covering:
    C       -- all malignant neoplasms
    D00-D49 -- in situ and benign neoplasms
    Z15, Z17, Z19, Z80, Z85, Z86 -- genetic susceptibility, receptor status,
              family/personal history

Options:
    --prefixes C D0 D1 Z17   # custom prefix list (replaces defaults)
    --billable-only           # exclude header/category codes
"""

import argparse
import csv
import glob
import os
import sys
from pathlib import Path

DEFAULT_PREFIXES = [
    "C",
    "D0", "D1", "D2", "D3", "D4",
    "Z15", "Z17", "Z19", "Z80", "Z85", "Z86",
]

SCRIPT_DIR = Path(__file__).parent.parent
ICD10_DIR  = SCRIPT_DIR / "ICD10_codes"


def dot_code(code: str) -> str:
    return f"{code[:3]}.{code[3:]}" if len(code) > 3 else code


def main():
    parser = argparse.ArgumentParser(
        description="Filter CMS ICD-10-CM order file to oncology codes."
    )
    parser.add_argument(
        "--prefixes", nargs="+", default=DEFAULT_PREFIXES,
        metavar="PREFIX", help="Code prefixes to include (default: oncology set)",
    )
    parser.add_argument(
        "--billable-only", action="store_true",
        help="Exclude header/category codes (billable flag = 0)",
    )
    args = parser.parse_args()

    pattern = str(ICD10_DIR / "icd10cm-order-*.txt")
    matches = sorted(glob.glob(pattern))
    if not matches:
        sys.exit(f"No input file found matching {pattern}")
    if len(matches) > 1:
        print(f"Warning: multiple order files found, using {matches[-1]}", file=sys.stderr)
    input_path = matches[-1]

    year = os.path.basename(input_path).replace("icd10cm-order-", "").replace(".txt", "")
    output_path = ICD10_DIR / f"icd10cm-oncology-{year}.csv"

    prefixes = tuple(args.prefixes)
    rows_written = 0

    with open(input_path, encoding="utf-8", errors="replace") as f, \
         open(output_path, "w", newline="", encoding="utf-8") as out:
        writer = csv.writer(out)
        writer.writerow(["code", "description"])
        for line in f:
            line = line.rstrip("\r\n")
            if len(line) < 17:
                continue
            code = line[6:13].strip()
            if not code:
                continue
            billable = line[14]
            if args.billable_only and billable != "1":
                continue
            if not code.startswith(prefixes):
                continue
            description = line[16:76].strip()
            writer.writerow([dot_code(code), description])
            rows_written += 1

    print(f"Wrote {rows_written} codes to {output_path}")


if __name__ == "__main__":
    main()
