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
    "greenwald-competition-demystified": ".library/financial/Competition Demystified A Radically Simplified Approach to Business Strategy (Bruce C. Greenwald, Judd Kahn) (z-library.sk, 1lib.sk, z-lib.sk).epub",
    "higgins-financial-management": ".library/Analysis for Financial Management, 13e ISE (Robert Higgins, Jennifer Koski) (z-library.sk, 1lib.sk, z-lib.sk).pdf",
    "mankiw-principles-of-economics": ".library/financial/Principles of Economics 10th Edition (N. Gregory Mankiw) (z-library.sk, 1lib.sk, z-lib.sk).pdf",
    "marks-most-important-thing": ".library/financial/The Most Important Thing Illuminated= Uncommon Sense for the Thoughtful Investor (Howard Marks) (z-library.sk, 1lib.sk, z-lib.sk).pdf",
    "mishkin-money-banking": ".library/financial/货币金融学_第12版 ([美] 弗雷德里克·S.米什金) (z-library.sk, 1lib.sk, z-lib.sk).pdf",
    "penman-financial-statement-analysis": ".library/financial/Financial Statement Analysis for Value Investing (Stephen Penman and Peter F. Pope) (z-library.sk, 1lib.sk, z-lib.sk).epub",
    "schilit-financial-shenanigans": ".library/financial/Financial Shenanigans, Fourth Edition How to Detect Accounting Gimmicks  Fraud in Financial Reports ( etc.) (z-library.sk, 1lib.sk, z-lib.sk).epub",
    "thorndike-outsiders": ".library/financial/The Outsiders Eight Unconventional CEOs and Their Radically Rational Blueprint for Success (William N. Thorndike Jr.) (z-library.sk, 1lib.sk, z-lib.sk).epub",
    "xiaoxing-financial-statements": ".library/Financial_freedom/《一本书读懂财报（全新修订版）》.pdf",
    "thiel-zero-to-one": ".library/从0到1  开启商业与未来的秘密 = Zero to One Notes on Startups, or How to Build the Future ([美] 彼得・蒂尔 (Peter Thiel) etc.).epub",
    "graham-hackers-and-painters": ".library/Hackers  Painters Big Ideas from the Computer Age (Paul Graham).epub",
    "beinhocker-origin-of-wealth": ".library/财富的起源 = The Origin of Wealth Evolution, Complexity, and the Radical Remaking of Economics ([英] 埃里克・拜因霍克 (Eric Beinhocker) 著  俸绪娴, 刘玮琦 etc.).epub",
    "fanbing-growth-hacking": ".library/增长黑客：创业公司的用户与收入增长秘籍 (范冰).epub",
    "davidson-sovereign-individual": ".library/The Sovereign Individual - 主权个人（中文版） (James Dale Davidson, Lord William Rees-Mogg).pdf",
    "ries-lean-startup": ".library/The Lean Startup How Todays Entrepreneurs Use Continuous Innovation to Create Radically Successful Businesses (Eric Ries).epub",
    "fangyan-day-two": ".library/第二天金钱进化论 (方言).epub",
    "sandel-tyranny-of-merit": ".library/精英的傲慢：好的社会该如何定义成功？= The Tyranny of Merit Whats Become of the Common Good ([美] 迈克尔 · 桑德尔 (Michael J. Sandel) 著  曾纪茂 译).mobi",
    "durant-lessons-of-history": ".library/历史的教训 = The Lessons of History ([美] 威尔・杜兰特 (Will Durant) etc.).epub",
    "deutsch-beginning-of-infinity": ".library/无穷的开始  世界进步的本源 = The Beginning of Infinity Explanations That Transform the World ([英] 戴维・多伊奇 (David Deutsch) 著  王艳红, 张韵 译).epub",
    "hawkins-thousand-brains": ".library/千脑智能 = A Thousand Brains A New Theory of Intelligence ([美] 杰夫・霍金斯 (Jeff Hawkins) 著  廖璐, 熊宇轩, 马雷 译).epub",
    "carse-finite-infinite-games": ".library/有限与无限的游戏：一个哲学家眼中的竞技世界 (James P.Carse, 马小悟, 余倩).epub",
    "lewis-liars-poker": ".library/Liars Poker (Michael Lewis).epub",
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
