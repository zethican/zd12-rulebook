## HTML Helper Classes for Booklet Formatting

Now available in `css/print-booklet-optimized.css`

---

## **Page Break Classes**

### Force New Page
```html
<div class="page-break"></div>
<!-- or -->
<div class="new-page"></div>
```
Starts the next element on a new page. Best used before chapters or major sections.

**Example:**
```html
</section>
<div class="page-break"></div>
<h1>Chapter 2: Combat</h1>
```

---

### Break After
```html
<h2>Important Section</h2>
<div class="page-break-after"></div>
```
Adds a page break after the element.

---

### Break Before
```html
<div class="page-break-before"></div>
<h2>Next Section</h2>
```
Adds a page break before the element.

---

## **Keep Content Together Classes**

### No Break (Keep on One Page)
```html
<div class="no-break">
  <h4>Special Rule</h4>
  <p>This entire box stays on one page.</p>
  <p>Prevents awkward splits.</p>
</div>
```

### Content Boxes (Styled + No Break)
```html
<div class="box">
  <h4>Important Note</h4>
  <p>This box is styled and won't break across pages.</p>
</div>
```

Other box classes (all work the same):
- `class="stat-block"` - For character stats
- `class="sidebar"` - For sidebar content
- `class="rules-box"` - For rule explanations

**Example:**
```html
<div class="stat-block">
  <h4>Specialist Backlash</h4>
  <table>...</table>
</div>
```

### Keep Tight (Very Aggressive)
```html
<div class="keep-tight">
  <p>This content will really stay together.</p>
  <p>Minimum 5 lines orphaned.</p>
</div>
```

---

## **Separator Classes**

### Simple Separator (No Page Break)
```html
<h2>Section One</h2>
<p>Content here...</p>

<hr class="separator">

<h2>Section Two</h2>
<p>More content...</p>
```

### Thick Separator
```html
<hr class="separator-thick">
```

### Section Break with Dashed Line
```html
<div class="section-break"></div>
```

---

## **Real-World Examples**

### Example 1: Chapter with Break
```html
<div class="page-break"></div>

<h1>Chapter 5: Magic & Resources</h1>

<h2>The Resource Die</h2>
<p>To track resources that are limited...</p>

<div class="box">
  <h4>Resource Die Rules</h4>
  <p>When you use the resource, you roll its die...</p>
</div>
```

### Example 2: Complex Table That Must Stay Together
```html
<h3>Armor Options</h3>

<div class="stat-block">
  <table>
    <thead>
      <tr>
        <th>Armor Name</th>
        <th>Bonus</th>
        <th>Notes</th>
      </tr>
    </thead>
    <tbody>
      <!-- Table rows -->
    </tbody>
  </table>
</div>
```

### Example 3: Related Items Grouped
```html
<div class="group">
  <h4>Signature Moves</h4>
  <ul>
    <li>Move One</li>
    <li>Move Two</li>
    <li>Move Three</li>
  </ul>
</div>

<hr class="separator">

<div class="group">
  <h4>Abilities</h4>
  <ul>
    <li>Ability One</li>
    <li>Ability Two</li>
  </ul>
</div>
```

### Example 4: Sidebar with Content
```html
<div class="sidebar">
  <h4>Designer's Note</h4>
  <p>This sidebar explains design philosophy...</p>
  <p>It stays together on one page.</p>
</div>
```

---

## **Quick Cheat Sheet**

| What You Want | HTML Code |
|---------------|-----------|
| New page before this | `<div class="page-break"></div>` before element |
| Keep box together | `<div class="box">...</div>` |
| Separator line | `<hr class="separator">` |
| Group of related items | `<div class="group">...</div>` |
| Very important: no breaks | `<div class="keep-tight">...</div>` |
| Styled stat block | `<div class="stat-block">...</div>` |
| Prevent orphans | Already applied to all paragraphs! |

---

## **CSS Classes Reference**

| Class | Purpose | Use When |
|-------|---------|----------|
| `.page-break` | Force new page | Starting major sections/chapters |
| `.new-page` | Force new page | Same as above (alternative name) |
| `.page-break-before` | New page before | Need more control |
| `.page-break-after` | New page after | Element should end page |
| `.no-break` | Keep together | Content must not split |
| `.box` | Styled + kept together | Special callout boxes |
| `.stat-block` | Styled box for stats | Character stats, tables |
| `.sidebar` | Styled sidebar | Designer notes, asides |
| `.rules-box` | Styled rule box | Important rules |
| `.group` | Keep related items | Lists, related paragraphs |
| `.keep-tight` | Very aggressive keep | Extremely critical content |
| `.separator` | Light divider line | Between sections |
| `.separator-thick` | Heavy divider line | Major section breaks |
| `.section-break` | Dashed divider | Subsection breaks |

---

## **Best Practices**

1. **Use `.page-break` before major chapters** to ensure consistent formatting
2. **Wrap complex tables in `.stat-block`** to prevent splits
3. **Use `.box` for important rules** to make them stand out AND keep them together
4. **Use `.separator` between logical sections** for visual flow
5. **Don't overuse page breaks** - let the CSS do the work when possible

---

## **Example: Professional Booklet Section**

```html
<div class="page-break"></div>

<h1>Chapter 3: Combat & Grit</h1>

<div class="box">
  <h2>⚠️ Combat is Dangerous</h2>
  <p>Combat in ZD12 is designed to be fast, lethal, and driven by meaningful choices.</p>
</div>

<h2>The Combat Round</h2>
<p>Combat is resolved in rounds...</p>

<div class="stat-block">
  <h3>The Action Economy</h3>
  <p>On your turn each round, you can take:</p>
  <ul>
    <li><strong>1 Major Action</strong>: Your primary action</li>
    <li><strong>1 Minor Action</strong>: A quick action</li>
    <li><strong>1 Reaction</strong>: An out-of-turn action</li>
  </ul>
</div>

<hr class="separator">

<h2>Distance & Movement</h2>
<p>ZD12 uses abstract Distance Bands...</p>
```

This creates a professional-looking booklet section with:
- ✅ Page break before chapter
- ✅ Highlighted intro box (keeps together)
- ✅ Content that flows naturally
- ✅ Stat block for reference (no breaks)
- ✅ Visual separator between concepts

---

Enjoy your formatting control! 📚
