#!/usr/bin/env python3
"""
Sequential OCR extraction script for scanned PDF
"""
import subprocess
import os
from pathlib import Path

def ocr_page(page_num):
    """OCR single page and return text"""
    img_path = f"temp_images/page-{page_num:03d}.ppm"
    if not os.path.exists(img_path):
        return None

    try:
        result = subprocess.run(
            ["tesseract", img_path, "stdout", "-l", "chi_sim+eng"],
            capture_output=True, text=True, timeout=30
        )
        if result.returncode == 0:
            return (page_num, result.stdout)
        else:
            return None
    except Exception as e:
        print(f"Page {page_num} error: {e}")
        return None

def main():
    # Get all pages
    pages = sorted([
        int(f.stem.split('-')[1])
        for f in Path("temp_images").glob("page-*.ppm")
    ])

    print(f"开始 OCR {len(pages)} 页...")

    results = []
    for i, page_num in enumerate(pages):
        result = ocr_page(page_num)
        if result:
            results.append(result)

        # Progress every 10 pages
        if (i + 1) % 10 == 0:
            print(f"进度: {i + 1}/{len(pages)}")

    # Sort by page number
    results.sort()

    # Write to file
    with open("extracted_text.txt", "w", encoding="utf-8") as f:
        for page_num, text in results:
            f.write(f"\n{'='*60}\n")
            f.write(f"第 {page_num} 页\n")
            f.write(f"{'='*60}\n")
            f.write(text)
            f.write("\n")

    print(f"\n完成！提取了 {len(results)}/{len(pages)} 页")
    print(f"保存到: extracted_text.txt")

    # Show stats
    file_size = os.path.getsize("extracted_text.txt")
    print(f"文件大小: {file_size / 1024:.1f} KB")

if __name__ == "__main__":
    main()
