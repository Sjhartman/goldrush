"""
collect_schemas.py

Connects to the Databricks data lake and runs DESCRIBE TABLE for every table
in a given catalog.schema, writing a TSV of
table_name / col_name / data_type to schemas/<schema>_columns.tsv.

Usage:
    # Epic Clarity (default):
    venv/bin/python tools/collect_schemas.py -t YOUR_DATABRICKS_TOKEN

    # Any other catalog.schema:
    venv/bin/python tools/collect_schemas.py -t YOUR_DATABRICKS_TOKEN --catalog curated.tempus

    # Override the tables list file explicitly:
    venv/bin/python tools/collect_schemas.py -t YOUR_DATABRICKS_TOKEN --catalog curated.tempus --tables schemas/tempus_tables.txt

Tables list file:
    One table name per line (case-insensitive). Defaults to schemas/clarity_tables.txt for
    curated.epic_clarity, or schemas/<schema>_tables.txt for any other catalog.schema.
    To generate one from Databricks:
        names = [row.tableName.upper()
                 for row in spark.sql("SHOW TABLES IN curated.tempus").collect()]
        print("\\n".join(names))
    Paste the output into the tables file, or export as .txt and drop it in schemas/.

Output: schemas/<schema>_columns.tsv in the goldrush root.
"""

import argparse
import csv
from pathlib import Path

from databricks import sql

DATABRICKS_SERVER_HOSTNAME = 'adb-7423990253170059.19.azuredatabricks.net'
DATABRICKS_HTTP_PATH       = '/sql/1.0/warehouses/52433d0cfef3e650'

GOLDRUSH_DIR = Path(__file__).parent.parent
SCHEMAS_DIR  = GOLDRUSH_DIR / "schemas"


def _schema_name(catalog: str) -> str:
    parts = catalog.split(".")
    return parts[-1] if len(parts) > 1 else parts[0]


def default_tables_file(catalog: str) -> Path:
    schema = _schema_name(catalog)
    if schema == "epic_clarity":
        return SCHEMAS_DIR / "clarity_tables.txt"
    return SCHEMAS_DIR / f"{schema}_tables.txt"


def default_output_file(catalog: str) -> Path:
    schema = _schema_name(catalog)
    return Path(f"{schema}_columns.tsv")


def load_tables(tables_path: Path, catalog: str) -> list:
    if not tables_path.exists():
        raise FileNotFoundError(
            f"{tables_path} not found -- run SHOW TABLES IN {catalog} "
            f"in Databricks and paste the output into {tables_path.name}"
        )
    for encoding in ("utf-8-sig", "utf-16"):
        try:
            text = tables_path.read_text(encoding=encoding)
            tables = [t.strip().upper() for t in text.splitlines() if t.strip()]
            if tables:
                return tables
        except (UnicodeDecodeError, UnicodeError):
            continue
    raise ValueError(f"Could not decode {tables_path.name} -- try saving it as UTF-8")


def collect(token: str, catalog: str, tables: list) -> list:
    rows = []
    ok = 0
    skipped = 0

    connection = sql.connect(
        server_hostname=DATABRICKS_SERVER_HOSTNAME,
        http_path=DATABRICKS_HTTP_PATH,
        access_token=token,
    )
    cursor = connection.cursor()

    for i, table in enumerate(tables, 1):
        fqn = f"{catalog}.{table}"
        try:
            cursor.execute(f"DESCRIBE TABLE {fqn}")
            for row in cursor.fetchall():
                col_name, data_type = row[0], row[1]
                if col_name and not col_name.startswith("#"):
                    rows.append({
                        "table_name": table,
                        "col_name":   col_name,
                        "data_type":  data_type,
                    })
            ok += 1
            if i % 50 == 0 or i == len(tables):
                print(f"  {i}/{len(tables)} tables -- {ok} OK, {skipped} skipped")
        except Exception as e:
            skipped += 1
            if skipped <= 10:
                print(f"  SKIP {table}: {e}")

    cursor.close()
    connection.close()
    return rows


def main():
    parser = argparse.ArgumentParser(
        description="Collect column schemas from a Databricks catalog.schema via DESCRIBE TABLE"
    )
    parser.add_argument("-t", "--token", required=True,
                        help="Databricks personal access token")
    parser.add_argument("--catalog", default="curated.epic_clarity",
                        help="catalog.schema to collect (default: curated.epic_clarity)")
    parser.add_argument("--tables", default=None,
                        help="Path to tables list file (one name per line). "
                             "Defaults to schemas/clarity_tables.txt for epic_clarity, "
                             "schemas/<schema>_tables.txt for others.")
    args = parser.parse_args()

    tables_path = Path(args.tables) if args.tables else default_tables_file(args.catalog)
    out_path    = default_output_file(args.catalog)

    tables = load_tables(tables_path, args.catalog)
    print(f"Catalog : {args.catalog}")
    print(f"Tables  : {len(tables)} loaded from {tables_path.name}")
    print(f"Output  : {out_path}")
    print("Collecting column schemas via DESCRIBE TABLE...")

    rows = collect(args.token, args.catalog, tables)

    with open(out_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["table_name", "col_name", "data_type"],
                                delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)

    tables_seen = len({r["table_name"] for r in rows})
    print(f"\nDone. {len(rows)} columns across {tables_seen} tables -> {out_path.name}")


if __name__ == "__main__":
    main()
