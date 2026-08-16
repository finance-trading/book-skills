#!/usr/bin/env python3
"""OCR extract text from the scanned PDF book 量化交易"""
import os
import sys
import time
import fitz  # PyMuPDF
import pytesseract
from PIL import Image

PDF_PATH = "./.library/量化交易：如何建立自己的算法交易事业 (（加）欧内斯特·陈) (z-library.sk, 1lib.sk, z-lib.sk).pdf"
OUTPUT_DIR = "./output/量化交易-欧内斯特·陈-OCR分页"
OUTPUT_TXT = "./output/量化交易-欧内斯特·陈-OCR提取全文.txt"
LANG = "chi_sim+eng"  # 中英混合
DPI = 300  # 扫描书 300 DPI 足够清晰

os.makedirs(OUTPUT_DIR, exist_ok=True)

doc = fitz.open(PDF_PATH)
total_pages = len(doc)
print(f"📖 书籍: 量化交易：如何建立自己的算法交易事业")
print(f"📄 总页数: {total_pages}")
print(f"🌐 OCR 语言: {LANG}")
print(f"🎯 DPI: {DPI}")
print()

all_text = []
start = time.time()
char_total = 0

for page_num in range(total_pages):
    page_start = time.time()
    page = doc[page_num]

    # 渲染页面为高分辨率图像
    mat = fitz.Matrix(DPI / 72, DPI / 72)
    pix = page.get_pixmap(matrix=mat)

    # 转换为 PIL Image
    img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

    # OCR
    text = pytesseract.image_to_string(img, lang=LANG)
    char_count = len(text.strip())
    char_total += char_count

    # 保存每页文本（便于调试和断点续传）
    page_txt_path = f"{OUTPUT_DIR}/量化交易-欧内斯特·陈_Page{page_num+1:03d}.txt"
    with open(page_txt_path, "w", encoding="utf-8") as f:
        f.write(f"===== Page {page_num+1} =====\n")
        f.write(text)

    all_text.append(text)

    elapsed = time.time() - start
    page_elapsed = time.time() - page_start
    pages_done = page_num + 1
    eta = (elapsed / pages_done) * (total_pages - pages_done)
    print(f"[{pages_done}/{total_pages}] Page {page_num+1:3d}: {char_count:5d} chars "
          f"({page_elapsed:.1f}s) | elapsed {elapsed:.0f}s | ETA {eta:.0f}s")

doc.close()

# 合并到单个文本文件
with open(OUTPUT_TXT, "w", encoding="utf-8") as f:
    f.write("=" * 60 + "\n")
    f.write("量化交易：如何建立自己的算法交易事业\n")
    f.write("作者：（加）欧内斯特·陈 (Ernest Chan)\n")
    f.write("=" * 60 + "\n\n")
    for i, text in enumerate(all_text):
        f.write(f"\n{'='*40} Page {i+1} {'='*40}\n")
        f.write(text)

total_time = time.time() - start
print()
print("=" * 60)
print(f"✅ OCR 完成")
print(f"⏱  总耗时: {total_time:.1f}s ({total_time/60:.1f}min)")
print(f"📊 总字符数: {char_total}")
print(f"📁 分页目录: {OUTPUT_DIR}")
print(f"📄 合并文件: {OUTPUT_TXT}")
print("=" * 60)
