# Lecture Notes Compiler - Windsurf Cascade Rules

When processing lecture notes, slides, or generating consolidated PDF study documents:

1. Layout Standards:
   - Page sizes supported: US Legal (8.5x14in), US Letter (8.5x11in), ISO A4 (210x297mm).
   - Layout: Two-column flow (column-count: 2; column-gap: 8px) with 0.18in margins.
   - Body font: Arial 8.0px, line-height 1.13.
   - Monochrome palette: Black, white, and subtle grayscale backgrounds (#000, #fff, #e2e2e2, #f4f4f4).
2. Elimination of Wasted Space:
   - Remove all decorative header banners, slide numbers, and slide labels.
   - Group content into integrated clinical/scientific topic units.
   - Maintain 85% to 98% page fullness on all pages.
3. Table Architecture:
   - Apply table-layout: fixed; width: 100%;.
   - Consolidate multi-field entities into 3 clean columns (Disorder, Defect/Substrate, Clinical Hallmarks).
   - Define explicit colgroup percentage widths on every table.
   - Enforce overflow: hidden; on wrapping card divs.
4. QA Pipeline:
   - Run python scripts/verify_pdf.py to confirm zero word collisions and verify clean column boundaries.
