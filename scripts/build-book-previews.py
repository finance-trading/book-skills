#!/usr/bin/env python3
"""Convert non-PDF originals into cached PDF previews for the website reader.

Browsers cannot embed EPUB/MOBI/AZW3, so each such source is rendered to
.library/.previews/<slug>.pdf with Calibre's `ebook-convert`, and recorded as
`preview` (relative to website/) in website/books-index.json. The original
`source` is untouched, so "查看原书" still opens the real file.

Requires Calibre (ebook-convert). The cache lives under .library/ (gitignored).
"""

import json
import os
import shutil
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WEBSITE = os.path.join(ROOT, "website")
INDEX = os.path.join(WEBSITE, "books-index.json")
CACHE = os.path.join(ROOT, ".library", ".previews")
PDF_EXT = {".pdf"}
EBOOK_EXT = {".epub", ".mobi", ".azw", ".azw3", ".fb2", ".htmlz"}
WORKERS = 2


def convert(slug: str, src_abs: str):
    out = os.path.join(CACHE, f"{slug}.pdf")
    if os.path.isfile(out) and os.path.getmtime(out) >= os.path.getmtime(src_abs):
        return slug, out, None
    proc = subprocess.run(
        ["ebook-convert", src_abs, out],
        capture_output=True,
        text=True,
    )
    if proc.returncode != 0 or not os.path.isfile(out):
        detail = (proc.stderr or proc.stdout).strip().splitlines()
        return slug, None, detail[-1] if detail else f"exit {proc.returncode}"
    return slug, out, None


def main() -> int:
    if not shutil.which("ebook-convert"):
        print("ebook-convert not found; install Calibre first.", file=sys.stderr)
        return 1

    with open(INDEX, encoding="utf-8") as fh:
        index = json.load(fh)

    jobs = []
    for slug, book in index.items():
        source = book.get("source", "")
        ext = os.path.splitext(source)[1].lower()
        if not source or ext in PDF_EXT or ext not in EBOOK_EXT:
            book.pop("preview", None)
            continue
        source_abs = os.path.join(WEBSITE, source)
        if not os.path.isfile(source_abs):
            book.pop("preview", None)
            continue
        jobs.append((slug, source_abs))

    os.makedirs(CACHE, exist_ok=True)
    with ThreadPoolExecutor(max_workers=WORKERS) as pool:
        results = list(pool.map(lambda job: convert(*job), jobs))

    errors = []
    for slug, out, error in results:
        if out:
            index[slug]["preview"] = os.path.relpath(out, WEBSITE).replace(os.sep, "/")
            print(f"✓ {slug} -> {index[slug]['preview']}")
        else:
            index[slug].pop("preview", None)
            errors.append(f"{slug}: {error}")

    with open(INDEX, "w", encoding="utf-8") as fh:
        json.dump(index, fh, ensure_ascii=False, indent=2)
        fh.write("\n")

    if errors:
        print("\nFailed:", file=sys.stderr)
        for entry in errors:
            print(f"  - {entry}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
