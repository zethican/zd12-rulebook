# ZD12 Layout Optimization Guide
**Quick Reference for Reducing Cascading Page Breaks**

## What Changed in style-optimized.css

### 7 High-Impact Fixes:

#### FIX #1: Explicit Page Dimensions
```css
@page {
  size: letter; /* Was: var(--page-width) */
}
```
**Why:** Makes page boundaries predictable. Content area is now exactly 7.8" × 10".

---

#### FIX #2: Keep Headings with Content
```css
h2, h3, h4 {
  keep-with-next: always;
}
```
**Why:** WeasyPrint-specific property that prevents headings from being orphaned at bottom of pages.

---

#### FIX #3: Smart Paragraph Breaking
Removed `break-inside: avoid` from ALL paragraphs by default.
**Why:** Long paragraphs can now split naturally. Use `.no-break` class only when needed.

---

#### FIX #4: Smart List Breaking
Lists can now break across pages, but individual items stay together.
**When to use:** Short lists (≤3 items) automatically stay together.

---

#### FIX #5: Large Table Support
New class: `.table-allow-break`
```html
<table class="table-allow-break">
```
**Use when:** Tables are too large to fit on one page.

---

#### FIX #6: New Utility Classes
```html
<!-- Allow breaking (override defaults) -->
<div class="allow-break">
  <!-- Long content that should split naturally -->
</div>

<!-- Soft page break (suggest break here) -->
<div class="page-break-soft"></div>

<!-- Spacing controls -->
<div class="spacer-large"></div>
```

---

#### FIX #7: Better Heading Control
Headings now more intelligently avoid being separated from their content.

---

## HTML Markup Strategy

### For Problem Areas:

#### 1. **Sections that keep breaking awkwardly:**
```html
<div class="no-break">
  <h4>Heading</h4>
  <p>Short content that should stay together</p>
  <ul>
    <li>Related list</li>
  </ul>
</div>
```

#### 2. **Long content that needs to flow naturally:**
```html
<div class="allow-break">
  <h3>Long Chapter Section</h3>
  <p>Paragraph 1...</p>
  <p>Paragraph 2...</p>
  <!-- Let it break where natural -->
</div>
```

#### 3. **Strategic page break suggestions:**
```html
<h2>Chapter End</h2>
<p>Final paragraph...</p>

<div class="page-break-soft"></div>
<!-- Suggests break here, but won't force it -->

<h2>New Chapter</h2>
```

#### 4. **Tables that are too long:**
```html
<table class="table-allow-break">
  <thead>
    <tr><th>Header</th></tr>
    <!-- This will repeat on each page -->
  </thead>
  <tbody>
    <!-- Rows can now split across pages -->
  </tbody>
</table>
```

---

## Workflow Improvements

### Before Regenerating PDF:

1. **Identify problem pages** (note page numbers)
2. **Check if it's a known pattern:**
   - Orphaned heading? → Already fixed with `keep-with-next`
   - Table too long? → Add `.table-allow-break`
   - Short section breaking? → Wrap in `.no-break`
   - Long section refusing to break? → Wrap in `.allow-break`

3. **Make ONE targeted change** at problem location
4. **Regenerate and check** if it fixed OTHER pages too
5. **Repeat** for remaining issues

### Common Patterns:

**Pattern:** Heading at bottom of page with content on next page
**Fix:** Already handled by `keep-with-next: always`

**Pattern:** Table splits awkwardly
**Fix:** Default is no-break. If table is legitimately too long, add `.table-allow-break`

**Pattern:** Long paragraph refuses to break, pushing everything down
**Fix:** Paragraphs now break naturally. If one is still stuck, it might be in a `.no-break` container—check parent elements.

**Pattern:** Short rule block or stat box causes cascading issues
**Fix:** These should already use `.no-break` via classes like `.stat-block`

---

## WeasyPrint-Specific Tips

### Faster Preview Workflow:
```bash
# Instead of regenerating full PDF each time:
weasyprint index.html output.pdf --verbose

# Add verbose flag to see warnings about page breaks
```

### Debug Mode:
Add this to see what's breaking where:
```css
* {
  outline: 1px solid red; /* Temporary - remove for final */
}
```

---

## Priority Areas to Fix First

Based on your HTML structure:

1. **Chapter 1: Character Creation** (lines 79-91)
   - Has `.no-break` divs already ✓
   - Should be stable

2. **Tables** (throughout)
   - If any are multi-page (likely in Appendices), add `.table-allow-break`

3. **Forward section** (lines 37-60)
   - Check if `.page-break` on line 44 is in the right place
   - May want `.page-break-soft` instead for flexibility

4. **Long list sections**
   - Table of Contents (lines 14-36)
   - Appendix libraries
   - Should now break more gracefully

---

## When to Give Up and Use Scribus

You'll know it's time when:
- You're making >5 fixes per PDF generation cycle
- Changes to one page affect 3+ other pages
- You need pixel-perfect visual control
- You're spending more time fixing than writing

At that point: **Import the HTML into Scribus as text**, apply paragraph styles, and finish there.

---

## Scribus Import Tips (for later)

When you do make the jump:

1. **Don't import HTML directly** - copy/paste text content
2. **Set up Paragraph Styles first** in Scribus to match your hierarchy
3. **Use Master Pages** for headers/footers
4. **Link text frames** for flow control
5. **Keep the HTML as source of truth** for content updates

Your current CSS work won't be wasted—it'll inform your Scribus paragraph styles!
