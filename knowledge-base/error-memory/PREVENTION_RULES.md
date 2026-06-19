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
