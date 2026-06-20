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
