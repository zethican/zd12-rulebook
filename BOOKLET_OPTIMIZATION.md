# ZD12 PDF Generation - Using the Print Booklet Stylesheet

## Quick Start

To generate your booklet with the optimized print styles, use:

```bash
python generate_pdf.py --preset booklet
```

This will:
1. Generate a 5.5x8.5" booklet PDF
2. Automatically inject the booklet CSS from `generate_booklet_css()`
3. Apply page breaks at chapter headers (h1)
4. Keep tables, lists, and content blocks together
5. Optimize spacing for tight pages

## The Optimized CSS File

A new stylesheet has been created: `css/print-booklet-optimized.css`

This file contains:
- **Page Break Control**: `h1` forces new pages, `h2-h4` avoid breaks
- **Widow/Orphan Prevention**: 3+ lines required to orphan
- **Table Protection**: `page-break-inside: avoid` prevents splits
- **Typography Tightening**: Reduced font sizes and line-height
- **Margin Compression**: Reduced spacing throughout
- **Smart List Handling**: Lists stay together as atomic units

## Customization Tips

### Adjust Spacing
Edit the hardcoded margins if you need more/less compression:

```css
/* In print-booklet-optimized.css, line ~20-30 */
h1 { margin-bottom: 0.15in; }    /* Reduce/increase for more/less space */
h2 { margin-bottom: 0.1in; }
p { margin-bottom: 0.1in; }
```

### Protect Specific Sections
If a particular section keeps breaking awkwardly, you can add:

```html
<div class="stats">
  <!-- Content here won't break -->
</div>
```

The CSS already has:
```css
.stats, .abilities, .rules-block {
  page-break-inside: avoid;
}
```

### Adjust for Binding Gutter
If you're binding the booklets, adjust margin-left/margin-right:

```bash
python generate_pdf.py --preset booklet --margin-left 0.4 --margin-right 0.2
```

## Injection Strategy

The `generate_pdf.py` script has a `generate_booklet_css()` function that creates the @page rules and running headers. To also include the print-booklet-optimized.css styles, you can either:

### Option 1: Link in HTML (Simple)
Add this to your `<head>` in index.html:
```html
<link rel="stylesheet" href="css/print-booklet-optimized.css" media="print">
```

Then WeasyPrint will automatically apply it when generating PDFs.

### Option 2: Inject Programmatically (Advanced)
Modify generate_pdf.py to read print-booklet-optimized.css and inject both stylesheets:

```python
# In generate_pdf function, before injecting booklet_css:
try:
    with open('css/print-booklet-optimized.css', 'r') as f:
        optimization_css = f.read()
except:
    optimization_css = ""
```

Then inject both the booklet CSS and optimization CSS in the <style> tag.

## What These Optimizations Do

### Before Optimization:
- ❌ Tables split across pages
- ❌ Single orphan lines at page breaks
- ❌ Large spacing wastes page real estate
- ❌ Sections awkwardly split
- ❌ Chapter heads sometimes avoid breaks, sometimes don't

### After Optimization:
- ✅ Tables stay together
- ✅ Minimum 3 lines before/after breaks
- ✅ Compact spacing fits more per page
- ✅ Logical sections stay intact
- ✅ Consistent, predictable page breaks

## Testing

To see the results:

1. Generate a booklet:
   ```bash
   python generate_pdf.py --preset booklet
   ```

2. Open `build/zd12-rulebook.pdf` in your PDF viewer

3. Look for:
   - Do chapter titles start on new pages?
   - Are tables complete on one page?
   - Are there awkward orphan lines at page breaks?
   - Does content feel "tight" without being cramped?

If you need more aggressive compression, you can reduce font sizes further in `print-booklet-optimized.css`:

```css
body { font-size: 10pt; }      /* Even smaller */
h1 { font-size: 22pt; }
table { font-size: 8.5pt; }    /* For complex tables */
```

## Pro Tips

1. **For maximum density**: Use `--margin 0.25` or even `--margin 0.2`
2. **For readability**: Keep at least `--margin 0.3` 
3. **For binding**: Use `--margin-left 0.4 --margin-right 0.15` (gutter on left)
4. **High quality**: Use `--dpi 300` for professional printing

Example:
```bash
python generate_pdf.py --preset booklet --margin 0.25 --dpi 300
```

This creates a high-quality, tight 5.5x8.5" booklet perfect for printing and binding.
