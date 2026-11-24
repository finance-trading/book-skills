#!/usr/bin/env python3
"""Attach each book's original file in .library/ to website/books-index.json.

Stores `source` as a path relative to website/ so the reader can load the
original PDF/EPUB directly. Re-run after adding books or moving files.
"""

import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WEBSITE = os.path.join(ROOT, "website")
INDEX = os.path.join(WEBSITE, "books-index.json")

SOURCES = {
    "damodaran-investment-valuation": ".library/financial/Investment Valuation Tools and Techniques for Determining the Value of any Asset (4th edition) (Aswath Damodaran) (z-library.sk, 1lib.sk, z-lib.sk).pdf",
    "fisher-growth-stocks": ".library/Financial_freedom/《怎样选择成长股》.pdf",
    "graham-dodd-security-analysis": ".library/Financial_freedom/《证券分析》本杰明•格雷厄姆.pdf",
    "graham-intelligent-investor": ".library/Financial_freedom/《聪明的投资者》(美)本杰明·格雷厄姆.pdf",
    "greenwald-competition-demystified": ".library/financial/Competition Demystified A Radically Simplified Approach to Business Strategy (Bruce C. Greenwald, Judd Kahn) (z-library.sk, 1lib.sk, z-lib.sk).epub",
    "higgins-financial-management": ".library/Analysis for Financial Management, 13e ISE (Robert Higgins, Jennifer Koski) (z-library.sk, 1lib.sk, z-lib.sk).pdf",
    "mankiw-principles-of-economics": ".library/financial/Principles of Economics 10th Edition (N. Gregory Mankiw) (z-library.sk, 1lib.sk, z-lib.sk).pdf",
    "marks-most-important-thing": ".library/financial/The Most Important Thing Illuminated= Uncommon Sense for the Thoughtful Investor (Howard Marks) (z-library.sk, 1lib.sk, z-lib.sk).pdf",
    "mishkin-money-banking": ".library/financial/货币金融学_第12版 ([美] 弗雷德里克·S.米什金) (z-library.sk, 1lib.sk, z-lib.sk).pdf",
    "penman-financial-statement-analysis": ".library/financial/Financial Statement Analysis for Value Investing (Stephen Penman and Peter F. Pope) (z-library.sk, 1lib.sk, z-lib.sk).epub",
    "schilit-financial-shenanigans": ".library/financial/Financial Shenanigans, Fourth Edition How to Detect Accounting Gimmicks  Fraud in Financial Reports ( etc.) (z-library.sk, 1lib.sk, z-lib.sk).epub",
    "thorndike-outsiders": ".library/financial/The Outsiders Eight Unconventional CEOs and Their Radically Rational Blueprint for Success (William N. Thorndike Jr.) (z-library.sk, 1lib.sk, z-lib.sk).epub",
    "xiaoxing-financial-statements": ".library/Financial_freedom/《一本书读懂财报（全新修订版）》.pdf",
}


def main() -> int:
    with open(INDEX, encoding="utf-8") as fh:
        index = json.load(fh)

    missing = []
    for slug, rel in SOURCES.items():
        if slug not in index:
            missing.append(f"{slug}: not in books-index.json")
            continue
        abs_path = os.path.join(ROOT, rel)
        if not os.path.isfile(abs_path):
            missing.append(f"{slug}: missing {rel}")
            continue
        index[slug]["source"] = os.path.relpath(abs_path, WEBSITE).replace(os.sep, "/")

    with open(INDEX, "w", encoding="utf-8") as fh:
        json.dump(index, fh, ensure_ascii=False, indent=2)
        fh.write("\n")

    for book in index.values():
        print(f"{'✓' if book.get('source') else '·'} {book['title']} -> {book.get('source', '(none)')}")

    if missing:
        print("\nUnmapped:", file=sys.stderr)
        for entry in missing:
            print(f"  - {entry}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
