#!/usr/bin/env python3
"""
ZD12 Quick PDF Preview Tool
Generates PDF with page number overlay to quickly identify problem pages
"""

import subprocess
import sys
from pathlib import Path

def generate_pdf(html_file, output_pdf, verbose=True):
    """Generate PDF using WeasyPrint with optional verbose output."""
    cmd = ['weasyprint', html_file, output_pdf]
    if verbose:
        cmd.append('--verbose')
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✓ PDF generated: {output_pdf}")
            if verbose and result.stderr:
                print("\nWarnings/Info:")
                print(result.stderr)
        else:
            print(f"✗ Error generating PDF:")
            print(result.stderr)
            sys.exit(1)
    except FileNotFoundError:
        print("✗ Error: WeasyPrint not found. Install with: pip install weasyprint")
        sys.exit(1)

def main():
    # Default paths
    html_file = "index.html"
    css_file = "css/style.css"
    output_pdf = "ZD12-preview.pdf"
    
    # Check if files exist
    if not Path(html_file).exists():
        print(f"✗ Error: {html_file} not found")
        sys.exit(1)
    
    if not Path(css_file).exists():
        print(f"⚠ Warning: {css_file} not found (might cause issues)")
    
    print("=" * 60)
    print("ZD12 Quick PDF Generator")
    print("=" * 60)
    print(f"Input:  {html_file}")
    print(f"Output: {output_pdf}")
    print()
    
    # Allow command line args
    if len(sys.argv) > 1:
        if sys.argv[1] in ['-h', '--help']:
            print("Usage: python quick-preview.py [output-name.pdf]")
            print("\nOptional: Specify output filename")
            print("Example: python quick-preview.py test.pdf")
            sys.exit(0)
        output_pdf = sys.argv[1]
    
    # Generate PDF
    generate_pdf(html_file, output_pdf, verbose=True)
    
    # Quick stats
    pdf_path = Path(output_pdf)
    if pdf_path.exists():
        size_mb = pdf_path.stat().st_size / (1024 * 1024)
        print(f"\nFile size: {size_mb:.2f} MB")
        print("\n" + "=" * 60)
        print("Next steps:")
        print("  1. Open PDF and note problem page numbers")
        print("  2. Refer to LAYOUT-OPTIMIZATION-GUIDE.md for fixes")
        print("  3. Make targeted HTML/CSS changes")
        print("  4. Run this script again")
        print("=" * 60)

if __name__ == "__main__":
    main()
