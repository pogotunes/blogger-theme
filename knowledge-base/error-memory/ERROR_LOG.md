# ERROR LOG

## UI-001 — Mobile responsive layout broken

| Field | Value |
|-------|-------|
| Date | 2026-06-19 |
| Theme | RankrSEO-v1 |
| File | rankrseo-theme.xml (b:skin) |
| Affected Section | Entire theme — responsive breakpoints |
| Error Type | UI/UX — Responsive |
| Severity | High |

### Issues Found
- Only 2 breakpoints (992px and 640px) — missing laptop (1199px) and tablet (991px) and small mobile (480px)
- Grid utilities used non-standard `640px` instead of `767px` for mobile collapse
- No `min-width: 0` on flex children causing overflow
- Hero section lacked `.hero-content` wrapper for responsive control
- Cards had no flex column layout (unequal heights on mobile)

---

## UI-002 — Spacing system broken

| Field | Value |
|-------|-------|
| Date | 2026-06-19 |
| Theme | RankrSEO-v1 |
| File | rankrseo-theme.xml (b:skin) |
| Affected Section | Entire theme — all spacing values |
| Error Type | UI/UX — Spacing |
| Severity | High |

### Issues Found
- No spacing scale existed
- Mix of `3rem`, `5rem`, `2rem`, `1.5rem` with no system
- Section padding inconsistent
- Card padding varied arbitrarily

---

## UI-003 — Typography hierarchy weak

| Field | Value |
|-------|-------|
| Date | 2026-06-19 |
| Theme | RankrSEO-v1 |
| File | rankrseo-theme.xml (b:skin) |
| Affected Section | Entire theme — typography |
| Error Type | UI/UX — Typography |
| Severity | Medium |

### Issues Found
- No type scale (--text-xs through --text-5xl)
- No letter-spacing scale
- No line-height scale
- Headings lacked premium tracking
- Body line-height inconsistent

---

## UI-004 — Hero section unbalanced

| Field | Value |
|-------|-------|
| Date | 2026-06-19 |
| Theme | RankrSEO-v1 |
| File | rankrseo-theme.xml (b:skin + HTML) |
| Affected Section | Hero |
| Error Type | UI/UX — Layout |
| Severity | High |

---

## UI-005 — Service cards weak

| Field | Value |
|-------|-------|
| Date | 2026-06-19 |
| Theme | RankrSEO-v1 |
| File | rankrseo-theme.xml (b:skin) |
| Affected Section | Services grid |
| Error Type | UI/UX — Components |
| Severity | Medium |

---

## UI-006 — Blog section outdated

| Field | Value |
|-------|-------|
| Date | 2026-06-19 |
| Theme | RankrSEO-v1 |
| File | rankrseo-theme.xml (b:skin) |
| Affected Section | Blog grid + sidebar |
| Error Type | UI/UX — Components |
| Severity | Medium |

---

## UI-007 — Testimonials lack depth

| Field | Value |
|-------|-------|
| Date | 2026-06-19 |
| Theme | RankrSEO-v1 |
| File | rankrseo-theme.xml (b:skin) |
| Affected Section | Testimonials |
| Error Type | UI/UX — Components |
| Severity | Low |

---

## UI-008 — Contact form badly designed

| Field | Value |
|-------|-------|
| Date | 2026-06-19 |
| Theme | RankrSEO-v1 |
| File | rankrseo-theme.xml (b:skin) |
| Affected Section | Contact form |
| Error Type | UI/UX — Components |
| Severity | Low |

---

## UI-009 — Footer underdesigned

| Field | Value |
|-------|-------|
| Date | 2026-06-19 |
| Theme | RankrSEO-v1 |
| File | rankrseo-theme.xml (b:skin) |
| Affected Section | Footer |
| Error Type | UI/UX — Layout |
| Severity | Low |

---

## UI-010 — No design token system

| Field | Value |
|-------|-------|
| Date | 2026-06-19 |
| Theme | RankrSEO-v1 |
| File | rankrseo-theme.xml (b:skin) |
| Affected Section | Entire CSS architecture |
| Error Type | UI/UX — Architecture |
| Severity | Critical |

### Issues Found
- No spacing, type, leading, tracking, shadow, or radius tokens
- Hardcoded values throughout
- Dark mode only overrode colors, not shadows/transitions
- No font-mono token

## ERR-001 — Duplicate includable id

| Field | Value |
|-------|-------|
| Date | 2026-06-19 |
| Theme | RankrSEO-v1 |
| File | rankrseo-theme.xml |
| Affected Section | Blog1 widget — includables |
| Error Type | XML Validation |
| Severity | High |

### Error Message
```
The widget with id "Blog1" contains at least two b:includable elements with the same id: "postCommentsLink". All b:includable elements should have a unique id for a given widget.
```

---

## ERR-002 — Invalid setting name `displayStyle` in BlogArchive1

| Field | Value |
|-------|-------|
| Date | 2026-06-19 |
| Theme | RankrSEO-v1 |
| File | rankrseo-theme.xml |
| Affected Section | BlogArchive1 widget — widget-settings |
| Error Type | Widget Configuration |
| Severity | High |

### Error Message
```
The widget settings in widget with id "BlogArchive1" is not valid. 'displayStyle' is not a valid setting name.
```

---

## ERR-003 — Invalid setting name `showPostsCount` in BlogArchive1

| Field | Value |
|-------|-------|
| Date | 2026-06-19 |
| Theme | RankrSEO-v1 |
| File | rankrseo-theme.xml |
| Affected Section | BlogArchive1 widget — widget-settings |
| Error Type | Widget Configuration |
| Severity | High |

### Error Message
```
The widget settings in widget with id "BlogArchive1" is not valid. 'showPostsCount' is not a valid setting name.
```

---

## ERR-022 — Config variables rendering in nav; header spacing; blog title in brand

| Field | Value |
|-------|-------|
| Date | 2026-06-19 |
| Theme | RankrSEO-v1 |
| File | rankrseo-theme.xml |
| Affected Section | Header, navigation, footer |
| Error Type | Blogger Widget Binding |
| Severity | Critical |

### Issues Found
- LinkList widgets rendered config variable names (disqusShortname, etc.) as menu items
- Massive whitespace above header from admin section positioning
- Logo/nav/actions misaligned
- Full blog title rendered instead of short brand name

### Fix Applied
- Added `b:if cond='data:link.name'` guard on all LinkList renders
- Moved admin section to after header
- Restructured to LEFT(logo)/CENTER(nav)/RIGHT(actions)
- Replaced dynamic title with hardcoded 'RankrSEO' brand

---

## ERR-023 — Theme config variables rendered in UI

| Field | Value |
|-------|-------|
| Date | 2026-06-19 |
| Theme | RankrSEO-v1 |
| File | rankrseo-theme.xml |
| Affected Section | Header nav, mobile nav, footer columns |
| Error Type | Blogger Widget Binding |
| Severity | Critical |

### Issues Found
Config variable names (disqusShortname, commentsSystem, noThumb, etc.) displayed as visible menu items

### Fix Applied
- Replaced LinkList widgets in header/mobile nav with hardcoded `<a>` links
- Replaced footer LinkList widgets with locked HTML widgets containing hardcoded link lists
- Footer columns now use HTML widgets with hardcoded content

---

## ERR-024 — Footer architecture broken

| Field | Value |
|-------|-------|
| Date | 2026-06-19 |
| Theme | RankrSEO-v1 |
| File | rankrseo-theme.xml |
| Affected Section | Footer |
| Error Type | Layout |
| Severity | High |

### Issues Found
- Excessive vertical spacing (120px padding-top + 80px margin-bottom)
- Social icons as floating separate section
- Grid unbalanced, missing column headings
- Cluttered bottom bar with separate widgets

### Fix Applied
- Reduced footer padding to 80px, removed grid margin-bottom
- Merged social icons into brand widget content
- Merged copyright + legal links into single bottom bar widget

---

## ERR-025 — Inconsistent design across sections

| Field | Value |
|-------|-------|
| Date | 2026-06-19 |
| Theme | RankrSEO-v1 |
| File | rankrseo-theme.xml |
| Affected Section | Footer, blog, contact sections |
| Error Type | Design System |
| Severity | Critical |

### Fix Applied
- Defined 40+ design tokens in :root
- Applied tokens uniformly across all sections
- Established consistent component patterns

---

## ERR-026 — Empty postAuthor includable shadows defaultmarkup

| Field | Value |
|-------|-------|
| Date | 2026-06-19 |
| Theme | RankrSEO-v1 |
| File | rankrseo-theme.xml (Blog1 widget) |
| Affected Section | Post author display |
| Error Type | Widget Structure |
| Severity | Critical |

### Fix Applied
- Replaced empty includable with full author name implementation

---

## ERR-027 — Duplicate BlogPosting JSON-LD schema

| Field | Value |
|-------|-------|
| Date | 2026-06-19 |
| Theme | RankrSEO-v1 |
| File | rankrseo-theme.xml |
| Affected Section | Blog1 widget — post and postMeta includables |
| Error Type | JSON-LD |
| Severity | Critical |

### Fix Applied
- Removed duplicate schema from postMeta includable
- Added comment documenting canonical schema location

---

## ERR-028 — No small phone breakpoint (≤360px)

| Field | Value |
|-------|-------|
| Date | 2026-06-19 |
| Theme | RankrSEO-v1 |
| File | rankrseo-theme.xml (b:skin) |
| Affected Section | Responsive CSS |
| Error Type | Responsive |
| Severity | High |

### Fix Applied
- Added @media (max-width: 360px) breakpoint with reduced hero padding, smaller container, smaller headings

---

## ERR-029 — Hero vertical padding excessive on mobile

| Field | Value |
|-------|-------|
| Date | 2026-06-19 |
| Theme | RankrSEO-v1 |
| File | rankrseo-theme.xml |
| Affected Section | Hero section |
| Error Type | Mobile Design |
| Severity | High |

### Fix Applied
- Added responsive padding at 480px (64px/32px) and 360px (56px/24px)

---

## ERR-030 — Large CSS filter blur causes mobile jank

| Field | Value |
|-------|-------|
| Date | 2026-06-19 |
| Theme | RankrSEO-v1 |
| File | rankrseo-theme.xml (b:skin) |
| Affected Section | Hero and CTA decorative orbs |
| Error Type | Performance |
| Severity | Medium |

### Fix Applied
- Reduced blur from 80/100px to 60px
- Reduced orb dimensions from 600/400px to 400/300px
- Reduced opacity for lower compositing cost

---

## ERR-031 — Duplicate @media (max-width: 480px) blocks

| Field | Value |
|-------|-------|
| Date | 2026-06-19 |
| Theme | RankrSEO-v1 |
| File | rankrseo-theme.xml (b:skin) |
| Affected Section | CSS responsive blocks |
| Error Type | CSS Architecture |
| Severity | Medium |

### Fix Applied
- Merged 3 separate 480px blocks into one consolidated block
- Removed duplicate standalone media queries

---

## ERR-032 — Service card gradient border cross-browser compatibility

| Field | Value |
|-------|-------|
| Date | 2026-06-20 |
| Theme | RankrSEO-v2 |
| File | rankrseo-theme.xml (b:skin) |
| Affected Section | Service cards |
| Error Type | CSS — Cross-browser |
| Severity | Medium |

### Issues Found
- `mask-composite: exclude` for gradient border not supported in Firefox
- Service cards had no fallback styling

### Fix Applied
- Added `@supports not (mask-composite: exclude)` fallback with simple border
- Fallback shows primary color border on hover at 0.3 opacity

---

## ERR-033 — Featured post cards missing fallback background for missing images

| Field | Value |
|-------|-------|
| Date | 2026-06-20 |
| Theme | RankrSEO-v2 |
| File | rankrseo-theme.xml (b:skin) |
| Affected Section | Featured posts |
| Error Type | UI/UX |
| Severity | Low |

### Issues Found
- featured-card had no background when image was missing
- Empty space appeared instead of placeholder

### Fix Applied
- Added gradient background fallback to .featured-card class
- Background uses bg-alt and border-light for subtle placeholder effect
