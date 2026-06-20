# Single Page Projects

A collection of Blogger XML themes, UI components, and SEO knowledge base.

## Structure

```
├── knowledge-base/
│   ├── rankrseo-theme.xml          # Primary: RankrSEO Blogger XML theme (4,400+ lines)
│   ├── RANKRSEO_THEME_SPEC.md      # Master design/SEO/performance spec
│   ├── SNIPPET_LIBRARY.xml         # 27 reusable Blogger includable snippets
│   ├── blueprints/
│   │   └── SEO_AEO_GEO_BLUEPRINT.md  # Meta tags, JSON-LD, OG/Twitter cards
│   ├── docs/
│   │   ├── REPOSITORY_MAP.md       # Full workspace inventory
│   │   ├── BLOGGER_XML_ARCHITECTURE.md  # Blogger tag reference
│   │   ├── COMPONENT_LIBRARY.md    # 18 reusable UI components
│   │   └── THEME_ANALYSIS_REPORT.md # 13 themes scored across 8 categories
│   ├── error-memory/               # Error tracking & prevention rules
│   │   ├── MASTER_ERROR_MEMORY.json   # 25 errors logged (all fixed)
│   │   ├── PREVENTION_RULES.md        # 25 engineering rules
│   │   ├── VALIDATION_CHECKLIST.md    # 80-item pre-import checklist
│   │   ├── HIGH_RISK_PATTERNS.md      # 12 high-risk patterns
│   │   ├── KNOWN_FATAL_ERRORS.md      # 8 fatal error patterns
│   │   ├── ERROR_HISTORY.md           # Error history log
│   │   ├── ROOT_CAUSE_ANALYSIS.md     # Root cause deep dives
│   │   ├── ERROR_LOG.md               # Error log
│   │   ├── ERROR_PATTERNS.md          # Error patterns catalog
│   │   ├── FIX_HISTORY.md             # Fix history
│   │   └── UI_UX_AUDIT.md            # UI/UX audit notes
│   └── snippets/
│       └── SNIPPET_LIBRARY.xml
├── Other/                          # Legacy pikitemplates themes
│   ├── Citron_Free_Version/
│   ├── GridMag_Free_Version/
│   └── Magazine_Free_Version/
├── README.md
```

## RankrSEO Theme

`knowledge-base/rankrseo-theme.xml` is a production-ready Blogger XML theme for the RankrSEO agency.

### Design System
- **Primary:** `#2563EB` | **Secondary:** `#0F172A` | **Accent:** `#14B8A6`
- 40+ CSS custom properties (`--space-*`, `--text-*`, `--shadow-*`, `--radius-*`, etc.)
- Dark mode support via `body.dark-mode` class
- Responsive breakpoints at 1199px, 991px, 767px, 479px

### Features
- Sticky header with desktop/mobile navigation
- Hero, featured posts, services, testimonials, FAQ, CTA, process, about, stats, contact sections
- Blog with sidebar (PopularPosts, Label, HTML, BlogSearch)
- Single post layout (centered 800px, breadcrumbs, author, related posts)
- Contact form with glassmorphism card
- Footer grid (brand+social, services, company, resources, copyright)
- WhatsApp floating button
- SEO meta tags, JSON-LD schemas, OG/Twitter cards
- PageSpeed 90+ target with lazy loading
- `b:layout` tags for full Layout Editor compatibility

### Widgets (17 total)
| Widget | Type | Section |
|--------|------|---------|
| TextList15 | TextList | Admin (hidden) |
| LinkList1-3 | LinkList | Admin (hidden) |
| LinkList7 | LinkList | Footer Column 5 |
| PopularPosts2 | PopularPosts | Featured Posts |
| Blog1 | Blog | Blog Posts |
| PopularPosts1 | PopularPosts | Sidebar |
| Label1 | Label | Sidebar |
| HTML1 | HTML | Sidebar |
| BlogSearch1 | BlogSearch | Sidebar |
| ContactForm1 | ContactForm | Contact Form |
| HTML9 | HTML | Footer Column 1 |
| LinkList5 | LinkList | Footer Column 2 |
| LinkList6 | LinkList | Footer Column 3 |
| HTML10 | HTML | Footer Column 4 |
| HTML11 | HTML | Footer Copyright |

## Legacy Themes

The `Other/` directory contains three pikitemplates themes for reference:
- **Citron** (3,508 lines) — News/Magazine
- **GridMag** (6,239 lines) — Grid Magazine
- **Magazine** (6,008 lines) — Magazine

## Error Prevention

25 errors documented and fixed in `MASTER_ERROR_MEMORY.json`. Prevention rules in `PREVENTION_RULES.md` enforce:
- No LinkList for navigation/header (use hardcoded HTML)
- Design token system required before CSS
- Unique `b:includable` IDs
- `b:layout` tags on all widgets
- Valid XML well-formedness checks
