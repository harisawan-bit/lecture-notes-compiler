"""
render_pdf.py - Automated PDF compilation via headless Chromium / Microsoft Edge.
Supports US Legal, US Letter, and ISO A4 page sizes.

Usage:
    python render_pdf.py <input_html> <output_pdf> [--page-size=legal|letter|a4]
"""

import os
import sys
import shutil
import subprocess
import argparse

PAGE_SIZES = {
    "legal": "@page { size: legal; margin: 0.18in; }",
    "letter": "@page { size: letter; margin: 0.18in; }",
    "a4": "@page { size: A4; margin: 4.5mm; }"
}

def find_browser():
    """Locates Microsoft Edge or Google Chrome binary across Windows, macOS, and Linux."""
    candidates = []
    if sys.platform == "win32":
        candidates = [
            r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
            r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
            r"C:\Program Files\Google\Chrome\Application\chrome.exe",
            r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        ]
    elif sys.platform == "darwin":
        candidates = [
            "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
            "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        ]
    else:
        candidates = [
            "google-chrome",
            "google-chrome-stable",
            "chromium-browser",
            "chromium",
            "microsoft-edge-stable"
        ]

    for c in candidates:
        if os.path.isabs(c) and os.path.exists(c):
            return c
        path_in_env = shutil.which(c)
        if path_in_env:
            return path_in_env

    return None

def main():
    parser = argparse.ArgumentParser(description="Render high-density HTML notes to PDF via headless browser.")
    parser.add_argument("input_html", help="Path to input HTML file")
    parser.add_argument("output_pdf", help="Target output PDF file path")
    parser.add_argument("--page-size", choices=["legal", "letter", "a4"], default="legal", help="Page size preset")
    args = parser.parse_args()

    input_path = os.path.abspath(args.input_html)
    output_path = os.path.abspath(args.output_pdf)

    if not os.path.exists(input_path):
        print(f"Error: Input file does not exist: {input_path}")
        sys.exit(1)

    browser_bin = find_browser()
    if not browser_bin:
        print("Error: Could not locate Microsoft Edge or Google Chrome executable.")
        sys.exit(1)

    # Read HTML and update page size if specified
    with open(input_path, "r", encoding="utf-8") as f:
        content = f.read()

    target_rule = PAGE_SIZES[args.page_size]
    # Replace active @page rule
    import re
    updated_content = re.sub(r'@page\s*\{[^}]*\}', target_rule, content, count=1)

    temp_html = input_path
    if updated_content != content:
        temp_html = os.path.splitext(input_path)[0] + f"_{args.page_size}.tmp.html"
        with open(temp_html, "w", encoding="utf-8") as f:
            f.write(updated_content)

    print(f"Compiling PDF with {browser_bin} (Page Size: {args.page_size.upper()})...")
    cmd = [
        browser_bin,
        "--headless=new",
        "--disable-gpu",
        "--run-all-compositor-stages-before-draw",
        "--no-pdf-header-footer",
        f"--print-to-pdf={output_path}",
        temp_html
    ]

    result = subprocess.run(cmd, capture_output=True, text=True)
    if temp_html != input_path and os.path.exists(temp_html):
        try:
            os.remove(temp_html)
        except Exception:
            pass

    if result.returncode == 0 and os.path.exists(output_path):
        print(f"Success: PDF generated at: {output_path} ({os.path.getsize(output_path):,} bytes)")
    else:
        print(f"Compilation failed (exit code {result.returncode}):")
        print(result.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
