# Single Page Projects

A collection of Blogger XML themes, UI components, error memory system, and SEO/AEO/GEO knowledge base.

## Structure

```
├── knowledge-base/                     # Theme + documentation
│   ├── rankrseo-theme.xml              # Primary: RankrSEO Bloggers XML theme (4,700+ lines)
│   ├── RANKRSEO_THEME_SPEC.md          # Master design/SEO/performance specification
│   ├── SNIPPET_LIBRARY.xml             # 27 reusable Bloggers includable snippets
│   ├── SEO_AEO_GEO_BLUEPRINT.md        # Complete SEO/AEO/GEO blueprint
│   ├── FAILURE_PATTERNS.md             # Detected failure patterns catalog
│   ├── THEME_ANALYSIS_REPORT.md        # 13 themes scored across 8 categories
│   ├── BLOGGER_WIDGET_REFERENCE.md     # Complete Bloggers widget reference
│   ├── BLOGGER_XML_ARCHITECTURE.md     # Bloggers XML tag architecture
│   ├── COMPONENT_LIBRARY.md            # 18 reusable UI components
│   ├── REPOSITORY_MAP.md               # Full workspace inventory
│   ├── docs/
│   │   ├── REPOSITORY_MAP.md           # Full inventory
│   │   ├── BLOGGER_XML_ARCHITECTURE.md # Bloggers tag reference
│   │   ├── COMPONENT_LIBRARY.md        # 18 reusable UI components
│   │   ├── THEME_ANALYSIS_REPORT.md    # 13-theme analysis
│   │   └── XML_THEME_COMPARISON.md     # Cross-theme architecture audit
│   ├── blueprints/
│   │   └── SEO_AEO_GEO_BLUEPRINT.md    # Meta tags, JSON-LD, cards
│   ├── error-memory/                   # Permanent error tracking system
│   │   ├── MASTER_ERROR_MEMORY.json    # 31 errors logged & fixed
│   │   ├── PREVENTION_RULES.md         # 31 engineering rules
│   │   ├── VALIDATION_CHECKLIST.md     # 80-item pre-import checklist
│   │   ├── HIGH_RISK_PATTERNS.md       # 12 high-risk patterns
│   │   ├── KNOWN_FATAL_ERRORS.md       # 8 fatal error patterns
│   │   ├── ERROR_HISTORY.md            # Error history
│   │   ├── ROOT_CAUSE_ANALYSIS.md      # Root cause deep dives
│   │   ├── ERROR_LOG.md                # Error log
│   │   ├── ERROR_PATTERNS.md           # Error patterns catalog
│   │   ├── FIX_HISTORY.md              # Fix history
│   │   └── UI_UX_AUDIT.md             # UI/UX audit notes
│   └── snippets/
│       └── SNIPPET_LIBRARY.xml         # (duplicate of root)
├── Citron_Free_Version/                # News/Magazine theme (3,508 lines)
├── GridMag_Free_Version/               # Grid Magazine theme (3,221 lines)
├── Monster_Free_Version/               # News/Magazine theme (3,621 lines)
├── Quick_Spot_Free_Version/            # Quick News theme (3,409 lines)
├── SEO_Spot_Free_Version/              # SEO/Marketing theme (3,703 lines)
├── Shopping_Free_Version/              # eCommerce theme (3,546 lines)
├── Wind_Spot_Free_Version/             # News/Magazine theme (3,638 lines)
├── Other/                              # Legacy/Root XML themes
│   ├── amitkr26.xml                    # Portfolio/Blog (1,057 lines)
│   ├── handjee.xml                     # Education (4,679 lines)
│   ├── helthifi.xml                    # Health niche (4,031 lines)
│   ├── neet.xml                        # NEET Education (4,568 lines)
│   ├── neetjee.xml                     # NEET/JEE Education (4,409 lines)
│   └── smartpadhailikhai.xml           # Education (2,505 lines)
└── README.md
```

## RankrSEO Theme

`knowledge-base/rankrseo-theme.xml` is a production-ready, full Layout Editor compatible Bloggers XML theme for the RankrSEO SEO agency.

### Design System
- **Primary:** `#2563EB` | **Secondary:** `#0F172A` | **Accent:** `#14B8A6`
- 30+ CSS custom properties with dark mode support
- Responsive breakpoints: 1024px, 768px, 480px, 360px
- Font Awesome 6 subset (solid + brands, deferred load)
- Google Fonts: Inter + Poppins (preloaded)

### Features
- **19 Layout Editor sections** with b:layout tags and descriptive labels
- **Sticky header** with desktop dropdown nav + mobile hamburger menu
- **23 widgetized sections**: admin, hero, featured posts, services, why-rankrseo, process, blog + sidebar, case studies, client logos, FAQ, newsletter, lead magnets, CTA + contact form, 5 footer columns, copyright
- **12 defaultmarkup types**: Common, Blog, Profile, PopularPosts, Header, FeaturedPost, Label, BlogSearch, BlogArchive, TextList, LinkList, PageList
- **5 JSON-LD schema types**: WebSite, BlogPosting, BreadcrumbList, Organization+LocalBusiness, Service+OfferCatalog, FAQPage
- **Full Bloggers features**: posts (index + single), comments (embedded + threaded), labels (cloud), search (overlay + widget), archives (flat), pagination (load more + prev/next)
- **Agency sections**: hero with dashboard card, services grid, process timeline, testimonials, FAQ accordion, lead magnet downloads, CTA with contact form
- **SEO optimized**: OG tags, Twitter cards, hreflang, canonical, meta robots, JSON-LD
- **Performance**: lazy images, deferred FA, scroll animations, counter animations
- **Dark mode** with system preference detection + manual toggle
- **WhatsApp floating button**, back-to-top, sticky CTA bar

### Widget Inventory (29 total)
| Widget ID | Type | Section | Locked |
|-----------|------|---------|--------|
| TextList15 | TextList | admin | ✓ |
| LinkList1-3 | LinkList | admin | ✓ |
| HTML12 | HTML | hero-section | ✓ |
| HTML21 | HTML | featured-posts-wrapper | ✓ |
| PopularPosts2 | PopularPosts | featured | ✓ |
| HTML13 | HTML | services-section | ✓ |
| HTML14 | HTML | why-rankrseo-section | ✓ |
| HTML15 | HTML | process-section | ✓ |
| HTML23 | HTML | blog-posts-section | ✓ |
| Blog1 | Blog | main-blog | ✓ |
| PopularPosts1 | PopularPosts | sidebar | ✗ |
| Label1 | Label | sidebar | ✗ |
| HTML1 | HTML | sidebar | ✗ |
| BlogSearch1 | BlogSearch | sidebar | ✗ |
| HTML16 | HTML | case-studies-section | ✓ |
| HTML17 | HTML | client-logos-section | ✓ |
| HTML18 | HTML | faq-section | ✓ |
| HTML19 | HTML | newsletter-section | ✓ |
| HTML20 | HTML | lead-magnets-section | ✓ |
| HTML22 | HTML | cta-section | ✓ |
| ContactForm1 | ContactForm | contact-form | ✓ |
| HTML9 | HTML | footer-1 | ✗ |
| LinkList5 | LinkList | footer-2 | ✗ |
| LinkList6 | LinkList | footer-3 | ✗ |
| HTML10 | HTML | footer-4 | ✗ |
| LinkList7 | LinkList | footer-5 | ✗ |
| HTML11 | HTML | footer-copyright | ✓ |

### Error Prevention System
31 errors documented and fixed in `MASTER_ERROR_MEMORY.json`. 31 prevention rules in `PREVENTION_RULES.md` enforce:
- No LinkList for navigation/header (use hardcoded HTML widgets)
- Design token system required before CSS
- Unique `b:includable` IDs per widget
- `b:layout` tags on all sections for Layout Editor
- Valid XML well-formedness checks
- JSON-LD single source per type
- Small phone breakpoint (360px) required
- Filter blur performance budget
- Single media query per breakpoint
- Includable override completeness

### Setup
1. Download `knowledge-base/rankrseo-theme.xml`
2. In Blogger Dashboard → Theme → Backup → Restore
3. Replace `ca-pub-6446071541338143` (AdSense) with your publisher ID
4. Replace `G-E6D5N92MN9` (Analytics) with your measurement ID
5. Update social links, phone, email in footer HTML widgets
6. Customize via Theme → Edit HTML or Layout Editor

## Legacy Reference Themes

7 Pikitemplates themes in `Citron_Free_Version/`, `GridMag_Free_Version/`, `Monster_Free_Version/`, `Quick_Spot_Free_Version/`, `SEO_Spot_Free_Version/`, `Shopping_Free_Version/`, `Wind_Spot_Free_Version/` for cross-reference:
- Best CSS architecture: SEO_Spot (80+ variables, 8 breakpoints)
- Best design patterns: Citron (animated hero, SVG wave, category bubbles)
- Most relevant to RankrSEO: SEO_Spot (SEO/marketing niche)

6 legacy themes in `Other/`: Education, Health, Portfolio niches by Soratemplates/Pikitemplates.
