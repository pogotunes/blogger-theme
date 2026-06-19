# PREVENTION RULES

## RULE-001 — Verify includable id uniqueness

**Severity:** High

**Rule:** Before finalizing any Blogger theme, scan all `<b:includable id='...'>` elements within each `<b:widget>` to ensure no duplicate `id` values exist.

**Checklist:**
- [ ] Every `<b:includable>` within a widget has a unique `id`
- [ ] Includable lists merged from multiple sources are deduplicated
- [ ] Run `grep -n "includable id="` and verify uniqueness per widget

**Violation:** ERR-001 — duplicate `postCommentsLink` includable

---

## RULE-002 — Use version='2' setting names for version='2' widgets

**Severity:** High

**Rule:** When a widget declares `version='2'`, all `<b:widget-setting>` names must use the version='2' API, not version='1' legacy names.

**Version mapping table for BlogArchive:**
| Purpose | v1 (INVALID) | v2 (VALID) |
|---------|--------------|------------|
| Display style | `displayStyle` | `showStyle` |
| Grouping | `showType` | `frequency` |
| Show post count | `showPostsCount` | `showPosts` |

**Checklist:**
- [ ] Verify `version` attribute on widget tag
- [ ] Cross-reference setting names against version-specific documentation
- [ ] Never assume setting names are the same across versions

**Violation:** ERR-002, ERR-003 — used v1 setting names in v2 widget

---

## RULE-003 — Always validate Blogger widget settings against official reference

**Severity:** High

**Rule:** Never guess or assume setting names. Always consult the widget's official setting reference before writing `<b:widget-setting>` elements.

**Checklist:**
- [ ] Look up valid setting names for the specific widget type
- [ ] Look up valid setting names for the specific widget version
- [ ] Document all valid settings in the knowledge base

**Violation:** ERR-002, ERR-003

---

## RULE-004 — Run pre-validation before any theme export

**Severity:** Critical

**Rule:** Before delivering any Blogger theme, run mandatory pre-validation checks:

```bash
# Check tag balance
python3 -c "
import re
with open('theme.xml') as f:
    content = f.read()
# Verify tag pair counts
tags = ['b:section', 'b:widget', 'b:includable', 'b:if', 'b:loop']
for tag in tags:
    opens = len(re.findall(rf'<{tag}(?:\s|>)', content))
    closes = len(re.findall(rf'</{tag}>', content))
    self_close = len(re.findall(rf'<{tag}[^>]*/>', content))
    match = 'OK' if opens - self_close == closes else 'MISMATCH'
    print(f'{tag}: {opens} open, {closes} close, {self_close} self-close -> {match}')
"
```

**Violation:** ERR-001 would have been caught

---

## RULE-005 — One includable list source

**Severity:** Medium

**Rule:** Maintain a single authoritative list of default Blogger includables per widget type. Never compose includable lists from multiple partial references.

**Checklist:**
- [ ] Each widget has exactly one includable definition source
- [ ] The source is in the knowledge base (SNIPPET_LIBRARY.xml or COMPONENT_LIBRARY.md)
- [ ] When adding includables, always check against the existing list first

**Violation:** ERR-001

---

## RULE-006 — Use 5 standard responsive breakpoints

**Severity:** High

**Rule:** Every Blogger theme must implement exactly 5 responsive breakpoints:

| Breakpoint | Target |
|------------|--------|
| `>=1200px` | Desktop |
| `992px–1199px` | Laptop |
| `768px–991px` | Tablet |
| `481px–767px` | Mobile |
| `<=480px` | Small mobile |

Do not use arbitrary breakpoints like `640px`, `880px`, or `992px` alone.

**Checklist:**
- [ ] Desktop styles are the default (no media query)
- [ ] `@media (max-width: 1199px)` for laptop
- [ ] `@media (max-width: 991px)` for tablet
- [ ] `@media (max-width: 767px)` for mobile
- [ ] `@media (max-width: 480px)` for small mobile
- [ ] No gap between breakpoints (all values covered)
- [ ] Grid utilities collapse at correct breakpoints (grid-4 → 2col at 1199px, grid-3 → 2col at 1199px, all → 1col at 767px)

**Violation:** UI-001 — missing laptop and tablet breakpoints, used `640px` instead of `767px`

---

## RULE-007 — Use spacing scale exclusively

**Severity:** High

**Rule:** All margins, paddings, and gaps must use `--space-*` CSS custom properties. Never use raw `rem` or `px` values for layout spacing.

**Spacing scale:**
```css
--space-xs: 4px
--space-sm: 8px
--space-md: 12px
--space-lg: 16px
--space-xl: 24px
--space-2xl: 32px
--space-3xl: 48px
--space-4xl: 64px
--space-5xl: 96px
```

**Exception:** Font-size, line-height, and micro-level adjustments may use raw values.

**Checklist:**
- [ ] All `margin`, `padding`, `gap` values reference `--space-*`
- [ ] Section padding uses `--space-5xl` (desktop), `--space-4xl` (tablet), `--space-3xl` (mobile)
- [ ] Card padding uses `--space-2xl` (desktop), `--space-xl` (mobile)

**Violation:** UI-002 — no spacing scale existed; 10+ arbitrary values in use

---

## RULE-008 — Implement typography scale

**Severity:** High

**Rule:** Every theme must define a complete typography scale using CSS custom properties:

```css
--text-xs: 0.75rem;
--text-sm: 0.875rem;
--text-base: 1rem;
--text-lg: 1.125rem;
--text-xl: 1.25rem;
--text-2xl: 1.5rem;
--text-3xl: 1.875rem;
--text-4xl: 2.25rem;
--text-5xl: 3rem;
```

Plus line-height and letter-spacing scales.

**Checklist:**
- [ ] All `font-size` values use `--text-*` tokens
- [ ] Headings use `--leading-tight`
- [ ] Body uses `--leading-relaxed`
- [ ] H1/H2 use `--tracking-tight` for premium feel
- [ ] Small/utility text uses `--tracking-wide` or `--tracking-wider` for uppercase labels

**Violation:** UI-003 — no type scale, no tracking, inconsistent line-height

---

## RULE-009 — Hero must have content wrapper

**Severity:** Medium

**Rule:** The hero section must separate text content from visual content using a dedicated `.hero-content` wrapper div.

**Structure:**
```html
<section class='hero'>
  <div class='container hero-grid'>
    <div class='hero-content'>
      <span class='hero-tag'>...</span>
      <h1>...</h1>
      <p>...</p>
      <div class='hero-cta'>...</div>
      <div class='hero-trust'>...</div>
    </div>
    <div class='hero-visual'>
      <div class='hero-card'>...</div>
    </div>
  </div>
</section>
```

**Checklist:**
- [ ] Hero text content wrapped in `.hero-content`
- [ ] On tablet/mobile: `.hero-visual` has `order: -1` (appears above text)
- [ ] On small mobile: CTA buttons go full-width with `flex-direction: column`
- [ ] Hero trust labels use uppercase with letter-spacing

**Violation:** UI-004 — hero lacked content wrapper, making responsive layout difficult

---

## RULE-010 — Cards must use flex column for equal height

**Severity:** Medium

**Rule:** All card grids must use `display: flex; flex-direction: column` on cards with `flex: 1` on the content element to ensure equal height cards.

**Checklist:**
- [ ] Card uses `display: flex; flex-direction: column`
- [ ] Card description/body uses `flex: 1`
- [ ] Card has hover state with `transform: translateY(-3px)` minimum
- [ ] Service cards include hover "Learn More" indicator

**Violation:** UI-005 — service cards had unequal heights, no call-to-action indicator

---

## RULE-011 — Sidebar widgets need visual anchors

**Severity:** Low

**Rule:** Sidebar widget titles should have a colored bottom border (use `--primary-light` not `--border`) to create visual hierarchy.

**Checklist:**
- [ ] `.sidebar .widget h3` has `border-bottom: 2px solid var(--primary-light)`
- [ ] Widget padding uses `--space-xl`
- [ ] PopularPosts thumbnails are rounded with object-fit

**Violation:** UI-006 — sidebar widget titles had no visual anchor

---

## RULE-012 — Dark section cards need depth and hover states

**Severity:** Medium

**Rule:** Cards in dark sections (`section-dark`) must have glassmorphism effects and interactive hover states.

**Checklist:**
- [ ] Dark section cards use `rgba(255,255,255,0.05)` with backdrop-filter
- [ ] Hover state increases opacity and adds shadow
- [ ] Testimonial text has `::before` quote decoration
- [ ] Avatar uses gradient background

**Violation:** UI-007 — testimonial cards had no depth, no hover state, flat avatars

---

## RULE-013 — Contact form must use lead-gen styling

**Severity:** Medium

**Rule:** The contact form submit button must use squared corners (`--radius-sm`) not pill shape (`--radius-full`). Squared buttons convert better for lead generation forms.

**Checklist:**
- [ ] `.contact-form-button-submit` uses `border-radius: var(--radius-sm)`
- [ ] Input fields use `2px` border for prominence
- [ ] Textarea has `min-height: 140px` with `resize: vertical`
- [ ] Submit button has hover transform and shadow

**Violation:** UI-008 — contact form used pill button (inconsistent with lead-gen best practices)

---

## RULE-014 — Footer hierarchy needs uppercase headings

**Severity:** Low

**Rule:** Footer column headings must use uppercase with letter-spacing for visual hierarchy.

**Checklist:**
- [ ] `.footer h4` uses `text-transform: uppercase` with `letter-spacing: var(--tracking-wide)`
- [ ] Footer responsive has intermediate breakpoints (not just 992px → 640px)
- [ ] Social icons have hover animation

**Violation:** UI-009 — footer headings were plain, no hierarchy

---

## RULE-015 — Always start with a design token system

**Severity:** Critical

**Rule:** Before writing any theme CSS, define the complete design token system:

1. Color palette
2. Spacing scale (xs through 5xl)
3. Type scale (xs through 5xl)
4. Leading scale (none through loose)
5. Tracking scale (tight through wider)
6. Shadow scale (sm through 2xl)
7. Radius scale (sm through full)
8. Transition tokens (default, slow)

**Checklist:**
- [ ] All 8 token categories defined in `:root`
- [ ] Dark mode overrides every color token
- [ ] Components only reference tokens, never raw values
- [ ] No hardcoded colors outside `:root`

**Violation:** UI-010 — no design system existed; CSS grew ad-hoc without tokens
