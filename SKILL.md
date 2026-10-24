---
name: lecture-notes-compiler
description: >-
  Extracts, consolidates, and formats academic and medical lecture slides (PPT, PPTX, PDFs, images) into dense, high-yield, publication-grade study compendiums. Generates zero-waste, 2-column PDFs across US Legal, US Letter, and ISO A4 formats with 8px Arial typography, strictly black-and-white styling, diagram OCR extraction, anti-collision fixed tables, and automated spatial verification. Use when the user asks to summarize, compile, or format lecture slides into printable notes or high-density study PDFs.
---

# Lecture Notes Compiler: High-Density Study Compendium Runbook

This runbook guides AI agents across all IDEs (Antigravity, Claude Code, Cursor, Windsurf, Cline, Roo Code, Copilot) to extract, consolidate, style, compile, and spatially verify lecture slides into zero-waste, 2-column study PDFs.

## 1. Core Principles and Design Rules

1. Page Format Selection:
   - US Legal (8.5in x 14in / 612pt x 1008pt): Default for master comprehensive compendiums.
   - US Letter (8.5in x 11in / 612pt x 792pt): Standard North American printer paper.
   - ISO A4 (210mm x 297mm / 595pt x 842pt): Standard international printer paper.
2. Layout Architecture:
   - Continuous two-column flow (column-count: 2; column-gap: 8px).
   - Minimal printer margins: 0.18in (4.5mm).
   - Body font: Arial or Helvetica at 8.0px with 1.13 line-height.
   - Pure black-and-white / grayscale palette (#000, #fff, #e2e2e2, #f4f4f4).
   - No decorative headers, no banner art, and no slide source tags.
   - Content organized purely by physiological, scientific, or clinical topic.
3. Density Target:
   - 85% to 98% fullness on all pages, including the final page.
   - Zero large blank gaps.
4. Table Architecture (Crucial):
   - In Chromium multi-column layout, unconstrained tables cause row-height collapse and bleed horizontally into the adjacent column.
   - All tables must use fixed layout: table-layout: fixed; width: 100%;.
   - Never use more than 3 or 4 columns within a single 285pt column.
   - Always define explicit colgroup percentage widths on every table.
   - Set word-break: break-word; overflow-wrap: break-word; hyphens: auto; on all td and th elements.
   - Set tr { break-inside: avoid; } to prevent row shearing across page breaks.

## 2. End-to-End Pipeline

```
[Lecture Presentations (PPT/PPTX/PDF)]
               │
               ▼
   [extract_slides.py: Text + WinOCR]
               │
               ▼
[Clinical Topic Synthesis (15-20 Units)]
               │
               ▼
 [HTML5 Document (resources/template.html)]
               │
               ▼
   [render_pdf.py: Headless Edge/Chrome]
               │
               ▼
[verify_pdf.py: Zero-Collision QA Check]
```

## 3. Operational Steps

### Step 1: Slide and Image OCR Extraction
Run the slide extraction utility:
```bash
python scripts/extract_slides.py <path_to_slides_folder> <path_to_output_txt_dir>
```
Capabilities:
- Legacy .ppt files are automatically converted to .pptx via PowerPoint COM on Windows.
- Python-pptx extracts slide text, speaker notes, and shape tables.
- Embedded diagrams and chemical pathways are processed with WinOCR to capture flowchart labels, enzyme steps, and diagnostic matrices.

### Step 2: High-Yield Topic Synthesis
Group raw extracted slides into 15 to 20 logical topic units rather than transcribing slide-by-slide:
- Structure each unit:
  1. Core Concepts and Architecture (definitions, pathways, compartments).
  2. Physiological Regulation (feedback loops, stimuli, inhibitors).
  3. Second Messenger Transduction (G-protein, kinase cascades).
  4. Clinical Pathology and Disease Matrix (enzyme defects, inheritance, presentation).
  5. Laboratory Standards and Diagnostic Cutoffs (reference ranges, confirmatory tests).
  6. Pharmacology and Pathway Blockers (inhibitors, agonists, antagonists).

### Step 3: Anti-Collision HTML Formatting
Use `resources/template.html` and follow `resources/table_patterns.md`:
- Set `@page { size: legal; margin: 0.18in; }` (or letter, or A4).
- For complex multi-field disorders (Disease, Gene, Enzyme, Activator, Substrate, Presentation), consolidate into 3 spacious columns:
  - Column 1 (27%): Disorder and Genetics
  - Column 2 (33%): Enzyme Defect, Activator, and Substrate
  - Column 3 (40%): Clinical Hallmarks and Diagnostic Findings
- Enclose each unit in `<div class="card">` with `overflow: hidden;` to ensure complete column isolation.

### Step 4: Compiling PDF via Headless Browser
Execute PDF compilation using `scripts/render_pdf.py`:
```bash
python scripts/render_pdf.py <notes.html> <output.pdf> --page-size=legal
```
Supported page size flags: `--page-size=legal`, `--page-size=letter`, `--page-size=a4`.

### Step 5: Verification and Density Tuning
Run `scripts/verify_pdf.py` to confirm zero collisions and check page density:
```bash
python scripts/verify_pdf.py <output.pdf> [target_page_count] --page-size=legal
```
- Column Gap Check: Verifies that a clean gap (minimum 8pt) exists between Column 1 and Column 2 on every page.
- Collision Detector: Bins all words into 20pt spatial buckets and verifies that no two distinct words overlap by more than 2.5pt.
- Page Density Check: Confirms vertical coverage reaches 85% to 98%.
- If the final page is under-filled:
  - Add high-yield clinical case vignettes and a rapid-review diagnostic buzzword matrix.
  - Fine-tune line-height (1.11 to 1.14) and td padding (0.8px to 1.2px) to achieve continuous page fullness.
