# Validation Checklist — Pre-Generation & Pre-Import

> MUST be run before generating any new theme and before importing to Blogger.
> Check the file used to generate this theme, and check the final output.

## A. PRE-GENERATION VALIDATION

### A1 Read All Knowledge Base
- [ ] Read REPOSITORY_MAP.md
- [ ] Read BLOGGER_XML_ARCHITECTURE.md
- [ ] Read COMPONENT_LIBRARY.md
- [ ] Read SEO_AEO_GEO_BLUEPRINT.md
- [ ] Read SNIPPET_LIBRARY.xml
- [ ] Read MASTER_ERROR_MEMORY.json
- [ ] Read PREVENTION_RULES.md
- [ ] Read VALIDATION_CHECKLIST.md
- [ ] Read HIGH_RISK_PATTERNS.md
- [ ] Read KNOWN_FATAL_ERRORS.md
- [ ] Read RANKRSEO_THEME_SPEC.md
- [ ] Read FAILURE_PATTERNS.md

### A2 Historical Comparison
- [ ] Search MASTER_ERROR_MEMORY.json for similar error patterns
- [ ] Check if any planned code pattern matches documented failure patterns
- [ ] If match found: STOP generation and show warning

## B. POST-GENERATION VALIDATION

### B1 XML Structure
- [ ] XML is well-formed (passes XML parser check)
- [ ] All namespaces declared: xhtml, b, data, expr
- [ ] `<b:skin><![CDATA[` is properly opened and closed
- [ ] `</head>` and `</body>` present exactly once each
- [ ] No duplicate `<b:section id='...'>` values
- [ ] `b:widget id` values follow safe patterns (alphanumeric + digits)

### B2 Includable Uniqueness
- [ ] No duplicate `<b:includable id='...'>` within any single widget
- [ ] All standard Blog1 includables present (active or disabled)
- [ ] Disabled includables use pattern: `<b:includable id='x'><b:comment>Disabled</b:comment></b:includable>`

### B3 Widget Settings
- [ ] All `<b:widget-setting>` names match current Blogger v2 API
- [ ] BlogArchive settings: showStyle, frequency, showPosts (not displayStyle, showType, showPostsCount)
- [ ] Widget version attribute correct (`version='2'` for all)

### B4 SEO & Structured Data
- [ ] Meta charset, viewport, title tags present
- [ ] Canonical link tag present
- [ ] Open Graph tags present (og:title, og:description, og:url, og:type, og:image)
- [ ] Twitter Card tags present
- [ ] Robots meta with conditional rules (homepage=index, archive/search=noindex)
- [ ] Theme-color meta tag present
- [ ] JSON-LD schema present (WebSite, BlogPosting, Organization, BreadcrumbList)
- [ ] FAQPage schema if FAQ section exists

### B5 Core Widgets (Present & Functional)
- [ ] **Header1** — Blog header with logo/text
- [ ] **Blog1** — Post list and single post view
- [ ] **Navbar1** — Blogger admin navbar (or hidden)
- [ ] **ContactForm1/2** — Contact form (visible + hidden duplicate for item pages)
- [ ] **PopularPosts1** — Sidebar popular posts
- [ ] **Label1** — Category/label widget
- [ ] **BlogArchive1** — Archive dropdown/list
- [ ] **BlogSearch1/2** — Search functionality
- [ ] **LinkList1-6** — Navigation, footer links, social links

### B6 Critical Blogger Features
- [ ] Post list renders (homepage and label/archive/search results)
- [ ] Single post renders with titles, body, images
- [ ] Page navigation (newer/older posts)
- [ ] Blog pager on multi-post views
- [ ] Breadcrumb on single posts
- [ ] Related posts (by label)
- [ ] Comments section with threaded replies
- [ ] Comment form embedded iframe
- [ ] Share buttons (Facebook, Twitter, LinkedIn, WhatsApp)
- [ ] Labels displayed on posts
- [ ] Post metadata (author, date, comments count)

### B7 Responsive Behavior (5 Breakpoints)
- [ ] ≥1200px: Full desktop layout
- [ ] 992-1199px: Laptop adjustments
- [ ] 768-991px: Tablet adjustments
- [ ] 481-767px: Mobile adjustments
- [ ] ≤480px: Small mobile adjustments
- [ ] No horizontal scroll at any width
- [ ] Font sizes readable at all widths
- [ ] CTAs and buttons usable on touch devices

### B8 Design Token Compliance
- [ ] No raw CSS values outside `:root`/`body.dark-mode`
- [ ] All spacing uses `--space-*` tokens
- [ ] All font sizes use `--text-*` tokens
- [ ] All shadows use `--shadow-*` tokens
- [ ] All radiuses use `--radius-*` tokens
- [ ] All transitions use `--transition-*` tokens
- [ ] Color tokens cover: primary, accent, bg, surface, text, border, error, success

### B9 Performance
- [ ] Images use `loading='lazy'`
- [ ] No render-blocking external JS
- [ ] Minimal inline JS only
- [ ] No jQuery dependency (vanilla JS preferred)
- [ ] CSS obeys `--content-width: 740px` for readability

### B10 Error Prevention
- [ ] No JavaScript `//` comments inside `<b:skin>` (use `/* */`)
- [ ] No invalid HTML entities outside CDATA (`&rarr;`, `&larr;` invalid)
- [ ] `&copy;` inside CDATA only
- [ ] Contact form hidden duplicate in `deleted='true'` section
- [ ] All `<b:include>` names match actual includable IDs

## C. SCORING

| Section | Items | Pass | Fail | Score |
|---------|-------|------|------|-------|
| A. Pre-generation | 12 | — | — | — |
| B1. XML Structure | 6 | — | — | — |
| B2. Includables | 3 | — | — | — |
| B3. Widget Settings | 3 | — | — | — |
| B4. SEO & Data | 10 | — | — | — |
| B5. Core Widgets | 8 | — | — | — |
| B6. Blogger Features | 13 | — | — | — |
| B7. Responsive | 6 | — | — | — |
| B8. Design Tokens | 7 | — | — | — |
| B9. Performance | 5 | — | — | — |
| B10. Error Prevention | 7 | — | — | — |
| **TOTAL** | **80** | — | — | — |

**Pass Threshold:** 75/80 (93.75%)

## D. FINAL VERDICT

- [ ] PASS — All checks pass. Theme ready for import.
- [ ] FAIL — One or more critical checks fail. See notes above.

**Inspector:**
**Date:**
