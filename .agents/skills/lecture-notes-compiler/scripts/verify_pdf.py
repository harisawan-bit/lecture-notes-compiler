"""
verify_pdf.py - Spatial collision detector, column separation verifier, and density calculator.
Supports US Legal, US Letter, and ISO A4 page sizes.

Usage:
    python verify_pdf.py <path_to_pdf> [target_page_count] [--page-size=legal|letter|a4]
"""

import sys
import argparse
import fitz

PAGE_HEIGHTS = {
    "legal": 1008.0,
    "letter": 792.0,
    "a4": 842.0
}

PAGE_MIDPOINTS = {
    "legal": 306.0,
    "letter": 306.0,
    "a4": 297.5
}

def verify_pdf(pdf_path, target_pages=None, page_size="legal"):
    doc = fitz.open(pdf_path)
    total_pages = len(doc)
    page_height = PAGE_HEIGHTS.get(page_size, 1008.0)
    mid_x = PAGE_MIDPOINTS.get(page_size, 306.0)

    print("=" * 60)
    print(f"VERIFYING PDF: {pdf_path}")
    print(f"Format: {page_size.upper()} (Page Height: {page_height:.1f} pt)")
    print(f"Total Pages Detected: {total_pages}")
    if target_pages is not None:
        target_pages = int(target_pages)
        if total_pages == target_pages:
            print(f"  [PASS] Page count matches target ({target_pages} pages).")
        else:
            print(f"  [FAIL] Page count mismatch: got {total_pages}, expected {target_pages}!")
    print("=" * 60)

    total_collisions = 0
    total_words = 0

    for pno, page in enumerate(doc):
        words = page.get_text("words")
        total_words += len(words)
        blocks = page.get_text("blocks")
        max_y = max(b[3] for b in blocks) if blocks else 0

        # Column bounds check around midpoint
        c1 = [w for w in words if w[0] < mid_x]
        c2 = [w for w in words if w[0] >= mid_x]
        max_x1 = max(w[2] for w in c1) if c1 else 0
        min_x2 = min(w[0] for w in c2) if c2 else mid_x * 2
        gap = min_x2 - max_x1

        # Check for column bleed
        bleed_fail = gap < 7.0
        bleed_status = "[FAIL - COLUMN BLEED DETECTED]" if bleed_fail else "[PASS - CLEAN COLUMN GAP]"

        fullness_pct = (max_y / page_height) * 100
        print(f"\n--- Page {pno + 1} ---")
        print(f"  Words: {len(words)} | Vertical Extent: {max_y:.1f}/{page_height:.1f} pt ({fullness_pct:.1f}%)")
        print(f"  Col 1 Max X: {max_x1:.1f} pt | Col 2 Min X: {min_x2:.1f} pt | Column Gap: {gap:.1f} pt {bleed_status}")

        # Collision detector using 20pt spatial bins
        buckets = {}
        for w in words:
            col = 0 if w[0] < mid_x else 1
            y_bin = int(w[1] // 20)
            key = (col, y_bin)
            if key not in buckets:
                buckets[key] = []
            buckets[key].append(w)

        page_collisions = 0
        for (col, y_bin), bwords in buckets.items():
            candidates = bwords + buckets.get((col, y_bin + 1), [])
            for i in range(len(bwords)):
                w1 = bwords[i]
                r1 = fitz.Rect(w1[:4])
                for w2 in candidates:
                    if w1 == w2:
                        continue
                    r2 = fitz.Rect(w2[:4])
                    inter = r1 & r2
                    if inter.is_valid and not inter.is_empty and inter.width > 2.5 and inter.height > 2.5:
                        if w1[0] <= w2[0]:
                            print(f"    [COLLISION] '{w1[4]}' <--> '{w2[4]}' at y={inter.y0:.1f}-{inter.y1:.1f}, x={inter.x0:.1f}-{inter.x1:.1f}")
                            page_collisions += 1

        print(f"  Collisions on Page {pno + 1}: {page_collisions}")
        total_collisions += page_collisions

    print("\n" + "=" * 60)
    print(f"SUMMARY REPORT:")
    print(f"  Total Document Words: {total_words}")
    print(f"  Total Text Collisions: {total_collisions}")
    if total_collisions == 0:
        print("  VERIFICATION RESULT: [PASSED] 100% Zero-Collision Clarity.")
    else:
        print(f"  VERIFICATION RESULT: [FAILED] {total_collisions} text collision(s) detected!")
    print("=" * 60)

    return total_collisions == 0 and (target_pages is None or total_pages == target_pages)

def main():
    parser = argparse.ArgumentParser(description="Verify PDF layout, page density, and text collision metrics.")
    parser.add_argument("pdf_path", help="Path to PDF file to verify")
    parser.add_argument("target_pages", nargs="?", default=None, type=int, help="Optional expected page count")
    parser.add_argument("--page-size", choices=["legal", "letter", "a4"], default="legal", help="Page size standard")
    args = parser.parse_args()

    success = verify_pdf(args.pdf_path, args.target_pages, args.page_size)
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
