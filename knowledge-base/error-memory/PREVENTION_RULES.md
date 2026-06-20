# Prevention Rules — Engineering Standards

> 15 permanent engineering rules derived from every error encountered.
> These rules are MANDATORY for all future RankrSEO theme generation.

---

## RULE-001: Includable Uniqueness
**Severity:** Critical
**Applies to:** All Blogger themes

All `<b:includable id='...'>` elements within a single `<b:widget>` MUST have unique IDs.

**Checklist:**
- [ ] Grep for `b:includable id=` within each widget
- [ ] Verify no duplicate IDs per widget
- [ ] Cross-reference includable lists from multiple sources for overlap

**Violation:** ERR-001 — duplicate `postCommentsLink` blocked theme import.

---

## RULE-002: Widget Version API Match
**Severity:** High
**Applies to:** All widget declarations

When using `version='2'` on a widget, all `<b:widget-setting>` names MUST match the v2 API.

**Known v2 Setting Name Changes:**

| Widget v1 (deprecated) | Widget v2 (current) |
|------------------------|---------------------|
| `displayStyle` | `showStyle` |
| `showType` | `frequency` |
| `showPostsCount` | `showPosts` |

**Checklist:**
- [ ] Verify each widget-setting name against Blogger v2 widget reference
- [ ] Cross-check version attribute value matches setting API version

**Violation:** ERR-002, ERR-003 — BlogArchive v1 settings on v2 widget.

---

## RULE-003: XML Well-Formedness
**Severity:** Critical
**Applies to:** All XML output

Validate XML syntax before importing to Blogger. Check for:
- Unclosed tags
- Duplicate close tags
- Invalid entities outside CDATA (`&rarr;`, `&larr;` etc.)

**Checklist:**
- [ ] Run XML parser validation
- [ ] Check all `&` entities for correctness
- [ ] Verify CDATA sections are properly opened/closed

---

## RULE-004: Pre-Validation Script
**Severity:** High
**Applies to:** All theme generation

Run validation script before writing final theme output. Script checks:
1. XML well-formedness
2. Unique includable IDs per widget
3. Valid widget setting names for version 2
4. No JavaScript comments (`//`) inside `<b:skin>` CSS
5. No invalid HTML entities outside CDATA

**Reference:** RANKRSEO_THEME_SPEC.md — Validation Checklist section.

---

## RULE-005: Includable Reference Sources
**Severity:** Medium
**Applies to:** Blog1 widget includables

When compiling Blog1 includable lists from multiple documentation sources, verify no overlap between groups (post metadata group vs comments group both include `postCommentsLink`).

**Checklist:**
- [ ] Merge all includable lists with deduplication
- [ ] Use a single authoritative source as primary

---

## RULE-006: Responsive Breakpoint Testing
**Severity:** High
**Applies to:** All layout CSS

Every section must be tested at all 5 breakpoints:

| Breakpoint | Range | Device |
|------------|-------|--------|
| Desktop | ≥1200px | Wide screens |
| Laptop | 992-1199px | Small laptop/tablet landscape |
| Tablet | 768-991px | Tablet portrait |
| Mobile | 481-767px | Phone landscape |
| Small Mobile | ≤480px | Phone portrait |

**Checklist:**
- [ ] No horizontal scroll at any breakpoint
- [ ] No text overflow/clipping
- [ ] CTAs stack vertically on mobile
- [ ] Images have `max-width: 100%`

---

## RULE-007: Design Token Spacing Scale
**Severity:** Medium
**Applies to:** All CSS spacing

Use only design token values for spacing. No raw `px`, `rem`, or `em` values for margins/padding/gaps.

**Token Scale:**
| Token | Value | Usage |
|-------|-------|-------|
| `--space-2xs` | 0.25rem | Tiny gaps |
| `--space-xs` | 0.5rem | Label-to-content |
| `--space-sm` | 0.75rem | Button padding |
| `--space-md` | 1rem | Base spacing |
| `--space-lg` | 1.5rem | Card padding |
| `--space-xl` | 2rem | Section inner padding |
| `--space-2xl` | 2.5rem | Large gaps |
| `--space-3xl` | 3rem | Mobile section padding |
| `--space-4xl` | 4rem | Tablet section padding |
| `--space-5xl` | 5rem | Laptop section padding |
| `--space-6xl` | 6rem | Desktop section padding |

---

## RULE-008: Fluid Typography Scale
**Severity:** Medium
**Applies to:** All headings

Use `clamp()` for fluid type scaling. Verify output at every breakpoint.

| Tag | clamp() | Mobile | Desktop |
|-----|---------|--------|---------|
| H1 | clamp(2.75rem, 5vw, 4.75rem) | 2.75rem | 4.75rem |
| H2 | clamp(1.875rem, 3.5vw, 3rem) | 1.875rem | 3rem |
| H3 | clamp(1.375rem, 2.5vw, 1.75rem) | 1.375rem | 1.75rem |

---

## RULE-009: Hero Content Wrapper
**Severity:** Medium
**Applies to:** Hero section

Hero must use a `.hero-content` wrapper div with `position: relative` for responsive control. Decorative elements with absolute positioning must be contained within this wrapper.

---

## RULE-010: Card Flex-Column Layout
**Severity:** Medium
**Applies to:** Grid card components

Card grid items must use `display: flex; flex-direction: column;` with content area using `flex: 1` for equal-height cards in the same row.

---

## RULE-011: Sidebar Widget Visual Anchor
**Severity:** Low
**Applies to:** Sidebar widget titles

Every sidebar widget title (`h3` or `.widget h2`) must have a visual separator (preferably `border-bottom: 2px solid var(--primary-light)`).

---

## RULE-012: Dark Section Card Depth
**Severity:** Low
**Applies to:** Components on dark backgrounds

Cards and elements placed on dark background sections must have:
- `border: 1px solid rgba(255,255,255,0.06)`
- Subtle shadow for depth separation

---

## RULE-013: Contact Form Lead-Gen Styling
**Severity:** Medium
**Applies to:** Contact form component

Contact form must use:
- Squared buttons (`--radius-sm`) for better conversion
- Gradient border wrapper via `.contact-form-card`
- Prominent CTA styling distinct from other forms

---

## RULE-014: Footer Grid Hierarchy
**Severity:** Low
**Applies to:** Footer component

Footer grid must use proportional column widths:
```css
grid-template-columns: 2fr 1fr 1fr 1fr;
```
Brand column (2fr) contains logo, description, newsletter, social links.
Remaining columns (1fr each) for link lists.

---

## RULE-015: Design Token System
**Severity:** Critical
**Applies to:** All CSS

EVERY CSS value MUST reference a custom property token. Raw values are forbidden outside `:root` and `body.dark-mode` declarations.

**Required Token Categories:**
- `--space-*` — Spacing (11 tokens)
- `--text-*` — Font sizes (6 tokens)
- `--leading-*` — Line heights (6 tokens)
- `--tracking-*` — Letter spacing (6 tokens)
- `--shadow-*` — Box shadows (9 tokens)
- `--radius-*` — Border radiuses (7 tokens)
- `--transition-*` — Transitions (3 tokens)
- Color tokens — `--primary`, `--primary-dark`, `--primary-light`, `--primary-bg`, `--accent`, `--accent-light`, `--bg`, `--bg-alt`, `--surface`, `--surface-alt`, `--text`, `--text-secondary`, `--text-muted`, `--border`, `--border-light`, `--error`, `--success`

---

## RULE-023: No LinkList for Navigation / Footer
**Severity:** Critical
**Applies to:** All Blogger themes

Never use `LinkList` widgets for header navigation, mobile navigation, or footer link columns. `LinkList` widgets bind to `data:links` which resolves from Blogger Dashboard link entries. Config variable names entered as link names in the Dashboard render unconditionally.

**Allowed Menu Sources (in priority order):**
1. **Hardcoded HTML widgets** with `locked='true'` — preferred for header nav, footer columns, social links
2. **Blogger Pages widget** (`type='PageList'`) — acceptable for page-based navigation only

**Forbidden:**
- `LinkList` widgets for any UI navigation
- `b:loop values='data:links'` in header, footer, or any visible UI section
- Any loop that could iterate over widget settings or theme configuration

**Exception:** LinkList widgets are acceptable only in `deleted='true'` hidden-widgets sections for data storage purposes (never rendered).

---

## RULE-024: Footer Architecture Standards
**Severity:** High
**Applies to:** All footer layouts

Footer must use a coherent, content-driven architecture with no fixed heights.

**Grid Layout (desktop):**
- `grid-template-columns: 2fr 1fr 1fr 1fr`
- `gap: 64px` (var(--space-4xl))
- Content-driven — no fixed heights or min-heights on any footer element

**Column Structure:**
1. **Brand column (2fr):** Logo (28px), short description, social icons (embedded, not separate section). Social icons use `.footer-social` class within brand content — never a separate `<b:section>`.
2. **Services column (1fr):** `<h4>Services</h4>`, link list
3. **Company column (1fr):** `<h4>Company</h4>`, link list
4. **Resources column (1fr):** `<h4>Resources</h4>`, link list

**Typography:**
- Brand logo: `1.75rem` (28px), bold
- Column heading: `1.125rem` (18px), semibold (600), clean (no uppercase, no letter-spacing)
- Column links: `0.875rem` (14px), subtle hover to white
- Bottom bar links: `0.8125rem` (13px)

**Bottom Bar:**
- Single widget containing both copyright (left) and legal links (right)
- Flex layout: `justify-content: space-between`
- Desktop: horizontal
- Mobile (767px): vertical stack, centered

**Responsive Breakpoints:**
- ≤1199px: reduce grid gap to 48px
- ≤991px: 2-column grid
- ≤767px: single column, centered text

**Forbidden:**
- Separate `footer-social` section (must be inside brand widget content)
- Separate legal links section (must be in same bottom bar widget as copyright)
- Fixed heights or min-heights
- Uppercase / letter-spacing on column headings
- Arrow pseudo-elements on link hover
- Newsletter form (unless explicitly required by design)

---

## RULE-025: Design Token System First
**Severity:** Critical
**Applies to:** All sections, all themes

Never design individual sections before defining global design tokens. All aesthetic values must reference CSS custom properties from `:root`.

**Required Token Categories:**
- `--space-*` — Spacing (padding, margin, gap)
- `--text-*` — Font sizes
- `--shadow-*` — Box shadows
- `--radius-*` — Border radii
- `--leading-*` — Line heights
- `--tracking-*` — Letter spacing
- `--transition-*` — Transition durations/easing
- Color tokens — All brand, surface, text, border, and state colors

**Forbidden:**
- Raw aesthetic values in section-specific CSS (padding, margins, font sizes, colors, shadows, radii)
- Ad-hoc spacing that doesn't use `--space-*` tokens
- Section-specific font sizes that don't use `--text-*` tokens
- Unique border radii or shadow values not in the token system

**Exception:** Layout-only properties (grid-template-columns, flex-direction, position, z-index, aspect-ratio) are exempt from the token requirement.
\n---\n## Superseded (from errors/ directory)\n
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
