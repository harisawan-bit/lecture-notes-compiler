# Lecture Notes Compiler

A high-density lecture notes compiler and agentic skill that extracts, consolidates, and formats academic and medical lecture presentations (PPT, PPTX, PDFs, diagrams) into publication-grade, zero-waste study compendiums.

Designed for AI IDEs and autonomous coding agents across Antigravity, Claude Code, Cursor, Windsurf, Cline, and Roo Code.

## Overview

Traditional slide summaries generate fragmented, slide-by-slide bullet points with excessive blank margins and poor data density. Lecture Notes Compiler transforms raw lecture decks into dense, two-column study compendiums organized strictly by conceptual topic.

Key Capabilities:
- Multi-Page Size Support: Pre-configured presets for US Legal (8.5in x 14in), US Letter (8.5in x 11in), and ISO A4 (210mm x 297mm).
- Automated Extraction: Extracts text, speaker notes, and shape tables from PPT and PPTX decks.
- Diagram OCR: Automatically runs optical character recognition on embedded diagrams, metabolic pathways, and cycle flowcharts.
- Anti-Collision Table Layout: Uses fixed-layout column groups and structured 3-column architectures to eliminate Chromium multi-column row-height collapse and column bleed.
- Zero-Waste Typography: Standardized 8.0px Arial typography with 1.13 line-height and monochrome styling.
- Automated Spatial QA: Python verification engine that detects text collisions, verifies column separation gaps, and measures vertical page density.

## Page Size Presets

The compiler supports three primary page dimensions:

1. US Legal (8.5in x 14in / 612pt x 1008pt):
   - Default master compendium format.
   - Column width: approximately 285 pt.
   - Ideal for extensive medical blocks and multi-topic reviews.
2. US Letter (8.5in x 11in / 612pt x 792pt):
   - Standard North American print size.
   - Column width: approximately 285 pt.
   - Configured via letter.css or --page-size=letter.
3. ISO A4 (210mm x 297mm / 595pt x 842pt):
   - Standard international print size.
   - Column width: approximately 278 pt.
   - Configured via a4.css or --page-size=a4.

## Cross-IDE Installation

### Automated Installation
Run the installer script to deploy to all detected IDEs:
```bash
python install.py --global
```

Or target a specific environment:
```bash
python install.py --ide=antigravity
python install.py --ide=claude
python install.py --ide=cursor
python install.py --ide=windsurf
```

### Manual Installation per IDE

#### 1. Antigravity / Gemini CLI
Copy the skill directory into your active agents folder or global config:
- Workspace: `.agents/skills/lecture-notes-compiler/`
- Global: `~/.gemini/config/skills/lecture-notes-compiler/`

#### 2. Claude Code
Copy the skill into the Claude skills directory:
- Workspace: `.agents/skills/lecture-notes-compiler/`
- Global: `~/.claude/skills/lecture-notes-compiler/`

#### 3. Cursor
Add the rules file to your workspace:
- Copy `.cursor/rules/lecture-notes-compiler.mdc` to your project root.

#### 4. Windsurf
Add the rules file to your workspace:
- Copy `.windsurf/rules/lecture-notes-compiler.md` to your project root.

#### 5. Cline and Roo Code
Copy `SKILL.md` into your project instructions or system prompts:
- `.cline/skills/lecture-notes-compiler/SKILL.md`

## The Anti-Collision Table Problem and Solution

When Chromium renders HTML tables inside CSS multi-column layouts (column-count: 2):
1. Column Bleed: Unconstrained tables (table-layout: auto) expand beyond column boundaries when long technical terms (e.g. Dipalmitoylphosphatidylcholine, 17-hydroxyprogesterone) appear. Because column gaps are small, text spills across into adjacent columns.
2. Vertical Row Collapse: Blink engine miscalculates multi-line row heights in narrow columns, allocating single-line height to multi-line cells and causing row overlap.

Solution Architecture:
- Enforce `table-layout: fixed; width: 100%;` on every table.
- Define explicit `<colgroup>` percentage widths.
- Consolidate multi-attribute entities (Disease, Gene, Enzyme, Activator, Substrate, Presentation) into 3 spacious columns:
  - Column 1 (27%): Disorder and Genetics
  - Column 2 (33%): Enzyme Defect and Substrates
  - Column 3 (40%): Clinical Hallmarks and Diagnostics
- Add `overflow: hidden;` to card containers.

## Tooling and Scripts

### 1. Slide and Diagram Extraction
```bash
python scripts/extract_slides.py <path_to_slides_folder> <output_text_dir>
```
Extracts text from all PPT and PPTX files in the input folder. Converts binary PPT to PPTX via COM automation on Windows and processes embedded pictures through Windows OCR.

### 2. PDF Rendering
```bash
python scripts/render_pdf.py <input.html> <output.pdf> --page-size=legal
```
Supported options: `--page-size=legal`, `--page-size=letter`, `--page-size=a4`.
Finds Microsoft Edge or Google Chrome binary automatically and prints without headers or footers.

### 3. Spatial Verification
```bash
python scripts/verify_pdf.py <output.pdf> [expected_page_count] --page-size=legal
```
Analyzes the compiled PDF using PyMuPDF (fitz):
- Spatial Bounding-Box Analysis: Bins text words into 20pt spatial buckets and verifies that zero words collide or overlap.
- Column Boundary Check: Verifies that text in Column 1 and Column 2 does not encroach upon the central gap.
- Page Density Measurement: Reports vertical extent percentage per page.

## File Structure

```text
lecture-notes-compiler/
├── .agents/
│   └── skills/
│       └── lecture-notes-compiler/
│           ├── SKILL.md
│           ├── resources/
│           │   ├── template.html
│           │   ├── table_patterns.md
│           │   ├── legal.css
│           │   ├── letter.css
│           │   └── a4.css
│           └── scripts/
│               ├── extract_slides.py
│               ├── render_pdf.py
│               └── verify_pdf.py
├── .cursor/
│   └── rules/
│       └── lecture-notes-compiler.mdc
├── .windsurf/
│   └── rules/
│       └── lecture-notes-compiler.md
├── resources/
│   ├── template.html
│   ├── table_patterns.md
│   ├── legal.css
│   ├── letter.css
│   └── a4.css
├── scripts/
│   ├── extract_slides.py
│   ├── render_pdf.py
│   └── verify_pdf.py
├── install.py
├── SKILL.md
├── LICENSE
└── README.md
```

## Requirements

- Python 3.9+
- python-pptx (for slide parsing)
- PyMuPDF (fitz, for spatial verification)
- Pillow (for image processing)
- winocr (optional, for Windows native OCR)
- Microsoft Edge or Google Chrome (for headless PDF rendering)

Install Python dependencies:
```bash
pip install python-pptx pymupdf pillow winocr
```

## License

MIT License. Copyright (c) 2026 Muhammad Haris Awan.
