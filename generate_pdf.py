#!/usr/bin/env python3
"""
Simple WeasyPrint PDF generator for ZD12 Rulebook
Run this locally to generate PDFs from your HTML
"""

import weasyprint
import sys
from pathlib import Path

def generate_pdf(html_file, output_file):
    """Convert HTML file to PDF"""
    print(f"Converting {html_file} to {output_file}...")

    # Convert HTML to PDF
    weasyprint.HTML(html_file).write_pdf(output_file)

    print(f"✓ PDF created: {output_file}")

if __name__ == "__main__":
    # Default files
    html_input = "index.html"
    pdf_output = "build/zd12-rulebook.pdf"

    # Allow command line arguments
    if len(sys.argv) > 1:
        html_input = sys.argv[1]
    if len(sys.argv) > 2:
        pdf_output = sys.argv[2]

    # Generate PDF
    try:
        generate_pdf(html_input, pdf_output)
    except Exception as e:
        print(f"✗ Error: {e}")
        sys.exit(1)
