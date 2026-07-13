"""
Epic Clarity Data Dictionary scraper.

Reads table names from schemas/clarity_tables.txt and saves each schema
as markdown to schemas/raw_schemas/.

Usage:
    venv/bin/python tools/scrape_clarity.py              # scrape all tables
    venv/bin/python tools/scrape_clarity.py PAT_ENC ...  # scrape specific tables

Requires Playwright (install once with: venv/bin/playwright install chromium).
On first run, a headed browser window opens for SSO login. The session is saved
to schemas/auth_state.json and reused headlessly on subsequent runs.
"""

import asyncio
import re
import sys
from pathlib import Path

from playwright.async_api import async_playwright
from bs4 import BeautifulSoup

GOLDRUSH_DIR = Path(__file__).parent.parent
SCHEMAS_ROOT = GOLDRUSH_DIR / "schemas"
AUTH_FILE    = SCHEMAS_ROOT / "auth_state.json"
OUT_DIR      = SCHEMAS_ROOT / "raw_schemas"
OUT_DIR.mkdir(parents=True, exist_ok=True)

BASE_URL   = "https://datahandbook.epic.com"
DETAIL_URL = f"{BASE_URL}/ClarityDictionary/Details"


# ---------------------------------------------------------------------------
# Login
# ---------------------------------------------------------------------------

async def login_and_save(playwright):
    browser = await playwright.chromium.launch(headless=False)
    ctx     = await browser.new_context()
    page    = await ctx.new_page()
    await page.goto(f"{BASE_URL}/ClarityDictionary")
    print("\n>>> Browser is open. Log in via SSO, then press Enter here to continue...", flush=True)
    input()
    await ctx.storage_state(path=str(AUTH_FILE))
    await browser.close()
    print("Session saved.")


# ---------------------------------------------------------------------------
# Table list
# ---------------------------------------------------------------------------

def load_table_names() -> list:
    table_file = SCHEMAS_ROOT / "clarity_tables.txt"
    if not table_file.exists():
        print(f"Table list not found: {table_file}")
        print("Create it with one table name per line (uppercase).")
        print("Generate it in Databricks with:")
        print("  names = [row.tableName.upper() for row in spark.sql('SHOW TABLES IN curated.epic_clarity').collect()]")
        print("  print('\\n'.join(names))")
        sys.exit(1)

    for encoding in ("utf-16", "utf-8-sig", "utf-8"):
        try:
            lines = table_file.read_text(encoding=encoding).splitlines()
            return [l.strip().upper() for l in lines if l.strip()]
        except (UnicodeDecodeError, UnicodeError):
            continue

    print(f"Could not read {table_file} -- try saving it as UTF-8.")
    sys.exit(1)


# ---------------------------------------------------------------------------
# Scrape a single table page
# ---------------------------------------------------------------------------

async def scrape_table(ctx, table_name: str) -> str:
    url  = f"{DETAIL_URL}?tblName={table_name}"
    page = await ctx.new_page()
    try:
        await page.goto(url, wait_until="networkidle", timeout=30_000)
        html = await page.content()
    except Exception as e:
        await page.close()
        return f"# {table_name}\n\n_Error loading page: {e}_\n"
    await page.close()
    return _parse_page(html, table_name, url)


def _parse_page(html: str, table_name: str, url: str) -> str:
    soup  = BeautifulSoup(html, "html.parser")
    parts = [f"# {table_name}\n\n**Source:** {url}\n"]

    desc = _find_description(soup)
    if desc:
        parts.append(f"## Description\n\n{desc}\n")

    col_md = _best_table(soup, prefer_headers=["name", "type", "column"])
    if col_md:
        parts.append(f"## Columns\n\n{col_md}\n")

    idx_md = _section_after_heading(soup, ["index", "indexes"])
    if idx_md:
        parts.append(f"## Indexes\n\n{idx_md}\n")

    fk_md = _section_after_heading(soup, ["foreign key", "foreign keys"])
    if fk_md:
        parts.append(f"## Foreign Keys\n\n{fk_md}\n")

    meta_md = _section_after_heading(soup, ["type:", "load type", "chronicles"])
    if not meta_md:
        meta_md = _remaining_tables(soup)
    if meta_md:
        parts.append(f"## Additional Metadata\n\n{meta_md}\n")

    return "\n".join(parts)


def _find_description(soup) -> str:
    for tag in soup.find_all(["p", "div", "span"]):
        if tag.find("table"):
            continue
        text    = tag.get_text(strip=True)
        classes = " ".join(tag.get("class", []))
        if len(text) > 50 and any(k in classes.lower()
                                  for k in ["desc", "summary", "detail", "info", "comment"]):
            return text
    return ""


def _table_to_md(tbl) -> str:
    rows, header_done = [], False
    for tr in tbl.find_all("tr"):
        cells = [td.get_text(separator=" ", strip=True) for td in tr.find_all(["th", "td"])]
        if not cells:
            continue
        rows.append("| " + " | ".join(cells) + " |")
        if not header_done:
            rows.append("| " + " | ".join(["---"] * len(cells)) + " |")
            header_done = True
    return "\n".join(rows)


def _best_table(soup, prefer_headers: list) -> str:
    tables = soup.find_all("table")
    for tbl in tables:
        headers = [th.get_text(strip=True).lower() for th in tbl.find_all("th")]
        if any(kw in h for kw in prefer_headers for h in headers):
            return _table_to_md(tbl)
    if tables:
        biggest = max(tables, key=lambda t: len(t.find_all("tr")))
        return _table_to_md(biggest)
    return ""


def _section_after_heading(soup, keywords: list) -> str:
    for tag in soup.find_all(["h1", "h2", "h3", "h4", "caption", "th"]):
        if any(kw in tag.get_text(strip=True).lower() for kw in keywords):
            sibling = tag.find_next_sibling()
            while sibling:
                if sibling.name == "table":
                    return _table_to_md(sibling)
                if sibling.name in ["h1", "h2", "h3", "h4"]:
                    break
                sibling = sibling.find_next_sibling()
    return ""


def _remaining_tables(soup) -> str:
    tables = soup.find_all("table")
    if len(tables) <= 1:
        return ""
    parts = []
    for tbl in tables[1:]:
        heading = tbl.find_previous(["h2", "h3", "h4", "caption"])
        label   = heading.get_text(strip=True) if heading else ""
        md      = _table_to_md(tbl)
        if md:
            parts.append((f"### {label}\n\n" if label else "") + md)
    return "\n\n".join(parts)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

async def main():
    async with async_playwright() as pw:
        if not AUTH_FILE.exists():
            print("No saved session. Opening browser for login...")
            await login_and_save(pw)
        else:
            reuse = input(f"Saved session found at {AUTH_FILE.name}. Re-login? (y/N): ").strip().lower()
            if reuse == "y":
                AUTH_FILE.unlink()
                await login_and_save(pw)

        table_names = load_table_names()

        if len(sys.argv) > 1:
            requested   = {a.upper() for a in sys.argv[1:]}
            table_names = [t for t in table_names if t in requested]
            print(f"Filtered to {len(table_names)} requested tables.")

        browser = await pw.chromium.launch(headless=True)
        ctx     = await browser.new_context(storage_state=str(AUTH_FILE))

        total = len(table_names)
        for i, name in enumerate(table_names, start=1):
            out_path = OUT_DIR / f"{name}.md"
            if out_path.exists():
                print(f"[{i}/{total}] {name} -- skipping (already exists)")
                continue
            print(f"[{i}/{total}] {name}...", end=" ", flush=True)
            md = await scrape_table(ctx, name)
            out_path.write_text(md, encoding="utf-8")
            print("done")

        await browser.close()
        print(f"\nDone. {total} tables -> {OUT_DIR}/")
        print(f"Run: venv/bin/python tools/postprocess.py")


if __name__ == "__main__":
    asyncio.run(main())
