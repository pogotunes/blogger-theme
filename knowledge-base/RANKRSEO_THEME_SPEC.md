# RankrSEO Theme Specification — Master Document

> This document defines the design language, standards, and requirements for all future RankrSEO Blogger themes.

---

## 1. BRAND IDENTITY

### 1.1 Brand Name
**RankrSEO** — Clean, modern, high-performance Blogger themes

### 1.2 Design Philosophy
- **Clean** — Minimal, uncluttered, whitespace-rich
- **Fast** — Performance-first, Core Web Vitals optimized
- **Accessible** — WCAG 2.1 AA compliant
- **SEO-native** — Structured data built-in from ground up
- **AEO/GEO-ready** — Optimized for AI crawlers and answer engines

### 1.3 Voice
- Professional but approachable
- Technical but clear
- Modern but timeless

---

## 2. COLOR PALETTE

### 2.1 Default Theme Colors

```css
:root {
  /* Primary Brand Colors */
  --primary: #0f172a;          /* Dark navy — headers, footer, accents */
  --accent: #6366f1;           /* Indigo — CTAs, links, highlights */
  --accent-hover: #4f46e5;     /* Darker indigo — hover states */
  
  /* Background Colors */
  --bg: #f8fafc;               /* Light slate — page background */
  --surface: #ffffff;           /* White — cards, modals, dropdowns */
  
  /* Text Colors */
  --text: #1e293b;             /* Near-black — body text */
  --text-muted: #64748b;       /* Slate — secondary text, meta */
  
  /* Borders & Dividers */
  --border: #e2e8f0;           /* Light slate — borders, dividers */
  
  /* Semantic Colors */
  --success: #10b981;          /* Green — success states */
  --warning: #f59e0b;          /* Amber — warnings */
  --error: #ef4444;            /* Red — errors */
  --info: #3b82f6;            /* Blue — info */
  
  /* Shadows */
  --shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.1), 0 8px 10px -6px rgba(0, 0, 0, 0.1);
  --shadow-hover: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
}
```

### 2.2 Theme Variant Color Overrides

Each theme variant defines only the accent/primary/bg colors:

| Variant | Accent | Primary | Background |
|---------|--------|---------|------------|
| Default | `#6366f1` (Indigo) | `#0f172a` (Navy) | `#f8fafc` (Light) |
| Health | `#10b981` (Emerald) | `#064e3b` (Dark Green) | `#f0fdf4` (Light Green) |
| Tech | `#3b82f6` (Blue) | `#1e3a5f` (Dark Blue) | `#f8fafc` (Light) |
| Education | `#f59e0b` (Amber) | `#451a03` (Dark Brown) | `#fffbeb` (Warm) |
| eCommerce | `#ea971d` (Gold) | `#1a1a2e` (Dark) | `#fcfeff` (White) |
| SEO | `#e30347` (Red) | `#101121` (Dark) | `#ffffff` (White) |

### 2.3 Dark Mode Palette

```css
body.dark-mode {
  --bg: #0f172a;
  --surface: #1e293b;
  --text: #e2e8f0;
  --text-muted: #94a3b8;
  --border: #334155;
  --shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.3);
  --shadow-hover: 0 20px 25px -5px rgba(0, 0, 0, 0.4);
}
```

---

## 3. TYPOGRAPHY

### 3.1 Font Families

```css
--heading-font: 'Poppins', sans-serif;      /* Headings — bold, geometric */
--body-font: 'Inter', sans-serif;           /* Body — clean, readable */
--meta-font: 'Inter', sans-serif;           /* Meta — compact */
--mono-font: 'JetBrains Mono', monospace;   /* Code — (future use) */
```

### 3.2 Font Loading Strategy

```css
/* Self-hosted @font-face with font-display: swap */
@font-face {
  font-family: 'Inter';
  font-style: normal;
  font-weight: 400;
  font-display: swap;
  src: url(...) format('woff2');
}
/* Repeat for all weights used (400, 500, 600, 700) */
```

### 3.3 Typographic Scale

```css
/* Desktop */
h1 { font-size: 3rem; }      /* 48px — Page title */
h2 { font-size: 2.5rem; }    /* 40px — Section title */
h3 { font-size: 1.5rem; }    /* 24px — Card title */
h4 { font-size: 1.25rem; }   /* 20px — Widget title */
h5 { font-size: 1.125rem; }  /* 18px — Subtitle */
h6 { font-size: 1rem; }      /* 16px — Small heading */
p  { font-size: 1rem; }      /* 16px — Body */
.small { font-size: 0.875rem; } /* 14px — Meta, captions */

/* Mobile */
@media (max-width: 768px) {
  h1 { font-size: 2rem; }
  h2 { font-size: 1.75rem; }
  h3 { font-size: 1.25rem; }
}
```

### 3.4 Line Heights

```css
body { line-height: 1.6; }       /* Body readability */
h1, h2, h3 { line-height: 1.2; } /* Headings tight */
.post-body { line-height: 1.8; } /* Post content spacious */
```

---

## 4. LAYOUT SYSTEM

### 4.1 Grid

```css
--max-width: 1200px;           /* Container max width */
--sidebar-width: 320px;        /* Sidebar width */
--gap: 2rem;                   /* Default gap */
```

### 4.2 Layout Patterns

```
Desktop:
┌─────────────────────────────────────┐
│            HEADER                    │
├─────────────────────────────────────┤
│   MAIN CONTENT    │    SIDEBAR      │
│   (calc(100% -    │   (320px)       │
│    sidebar - gap)) │                 │
├─────────────────────────────────────┤
│            FOOTER                    │
└─────────────────────────────────────┘

Mobile (< 880px):
┌─────────────────────┐
│      HEADER         │
├─────────────────────┤
│   MAIN CONTENT      │
├─────────────────────┤
│   SIDEBAR           │
├─────────────────────┤
│   FOOTER            │
└─────────────────────┘
```

### 4.3 Breakpoints

```css
/* Desktop */   min-width: 1179px;
/* Tablet */    768px - 1178px;
/* Mobile */    max-width: 767px;
/* Small */     max-width: 480px;
```

---

## 5. COMPONENT REQUIREMENTS

### 5.1 Required Sections (in order)

| Section | ID | Required? | Notes |
|---------|-----|-----------|-------|
| Hidden widgets | `hidden-widgets` | REQUIRED | For ContactForm on item pages |
| Top bar | `top-bar` | OPTIONAL | Social icons, date |
| News ticker | `hot-posts` | OPTIONAL | Breaking news |
| Header | `header-room` | REQUIRED | Logo + nav |
| Mega menu | `mega-wrap` | OPTIONAL | Dropdown grid |
| Featured | `ft-post` | RECOMMENDED | Hero posts |
| Main content | `main` | REQUIRED | Blog posts |
| Sidebar | `sidebar` | RECOMMENDED | Widget area |
| Footer columns | `footer` | REQUIRED | Footer widgets |
| Footer copyright | `footer-copyright` | REQUIRED | Attribution |
| Footer menu | `footer-checks-menu` | REQUIRED | Footer links |

### 5.2 Required Widgets

| Widget | Type | Required? | Purpose |
|--------|------|-----------|---------|
| Blog | `Blog` | REQUIRED | Main content |
| Header | `Header` | REQUIRED | Blog identity |
| PopularPosts | `PopularPosts` | RECOMMENDED | Sidebar/content |
| Labels | `Label` | RECOMMENDED | Category nav |
| LinkList | `LinkList` | RECOMMENDED | Menu + social |
| ContactForm | `ContactForm` | REQUIRED | Contact (hidden) |
| Search | `BlogSearch` | REQUIRED | Search |
| Archive | `BlogArchive` | RECOMMENDED | Archive nav |
| Profile | `Profile` | OPTIONAL | About me |

### 5.3 Required Includes

| Include Name | Purpose |
|-------------|---------|
| `theme-head` | All meta tags, schema, dns-prefetch |
| `theme-js` | All JavaScript |
| `widget-title` | Reusable widget title rendering |
| `searchMessage` | Search/archive/error messages |
| `breadcrumb` | Breadcrumb with JSON-LD |
| `postTitle` | Post title (h2 on index, h1 on item) |
| `postMeta` | Author, date, comments |
| `postThumbnail` | Lazy-loaded image |
| `postShareButtons` | Social share |
| `popular-content` | PopularPosts rendering |
| `threadedComments` | Full comment system |
| `threadedCommentForm` | Comment form iframe |
| `authorProfile` | Author widget profile |

### 5.4 Component Checklist

- [ ] Header with sticky behavior
- [ ] Responsive navigation (desktop horizontal + mobile hamburger)
- [ ] Search overlay modal
- [ ] Blog post grid (index view)
- [ ] Single post layout with featured image
- [ ] Sidebar with widgets
- [ ] Footer with columns + copyright
- [ ] Breadcrumb navigation
- [ ] Pagination (newer/older with rel attributes)
- [ ] Related posts section
- [ ] Social share buttons
- [ ] Contact form
- [ ] Comments (threaded)
- [ ] Cookie consent banner
- [ ] Back to top button
- [ ] Dark mode toggle (WITH actual implementation)

---

## 6. SEO STANDARDS

All themes MUST achieve the following SEO baseline (minimum):

### 6.1 Technical SEO Score: 9/10 minimum

- [ ] Single `<title>` with `data:view.title.escaped`
- [ ] Canonical with `data:view.url.canonical`
- [ ] Meta description with `data:view.description.escaped`
- [ ] Extended robots directives
- [ ] Open Graph — all required tags
- [ ] Twitter Card — summary_large_image
- [ ] Viewport with `maximum-scale=5`
- [ ] Favicon (all sizes)
- [ ] DNS prefetch for all external domains
- [ ] Theme-color meta

### 6.2 Schema Score: 9/10 minimum

- [ ] WebSite + SearchAction JSON-LD
- [ ] BlogPosting JSON-LD
- [ ] BreadcrumbList JSON-LD
- [ ] Organization + Person
- [ ] All dates in ISO 8601
- [ ] Proper publisher with logo

### 6.3 Semantic Score: 8/10 minimum

- [ ] Single h1 per page
- [ ] Logical heading hierarchy
- [ ] Semantic HTML5 landmarks
- [ ] Alt text on all images
- [ ] `rel='next'` and `rel='previous'` on pagination

---

## 7. PERFORMANCE STANDARDS

### 7.1 Core Web Vitals Targets

| Metric | Target |
|--------|--------|
| LCP | < 2.0s |
| CLS | < 0.05 |
| INP | < 150ms |
| TTFB | < 500ms |
| FCP | < 1.5s |

### 7.2 CSS Standards

- [ ] CSS size < 15KB uncompressed
- [ ] No universal selector reset (use `*, *::before, *::after`)
- [ ] CSS custom properties for all colors
- [ ] No dead code/unused variables
- [ ] `font-display: swap` on all `@font-face`
- [ ] Minimal `!important` usage

### 7.3 JavaScript Standards

- [ ] No render-blocking scripts in `<head>`
- [ ] All inline scripts at end of `<body>`
- [ ] `async` or `defer` on all external scripts
- [ ] No jQuery dependency (vanilla JS preferred)
- [ ] No anti-copy/right-click scripts
- [ ] Lazy loading with `loading='lazy'` on images

### 7.4 Asset Optimization

- [ ] Preload hero/LCP image
- [ ] Preconnect to critical origins
- [ ] No render-blocking external resources
- [ ] SVG icons preferred over icon fonts

---

## 8. AEO STANDARDS

### 8.1 Minimum AEO Requirements

- [ ] FAQPage schema for any FAQ content
- [ ] Clean, concise paragraph formatting
- [ ] List-friendly content structure
- [ ] Question-format headings where applicable
- [ ] Summary sections for key content

### 8.2 AEO Score Target: 7/10

---

## 9. GEO STANDARDS

### 9.1 Minimum GEO Requirements

- [ ] Entity clarity (Person, Organization, WebSite)
- [ ] Author credibility (name, URL, photo)
- [ ] Publication/modified dates in ISO 8601
- [ ] Semantic section landmarks
- [ ] Machine-readable JSON-LD
- [ ] No content hidden behind JS

### 9.2 GEO Score Target: 8/10

---

## 10. ACCESSIBILITY STANDARDS

- [ ] `minimum-scale=1, maximum-scale=5` in viewport
- [ ] 48px minimum touch targets
- [ ] Proper heading hierarchy
- [ ] Alt text on all images
- [ ] Semantic HTML landmarks
- [ ] `prefers-reduced-motion` support
- [ ] Focus indicators on interactive elements
- [ ] Color contrast ratio ≥ 4.5:1 for text
- [ ] `aria-label` on navigation elements
- [ ] Skip-to-content link (optional but recommended)

---

## 11. BROWSER SUPPORT

- [ ] Chrome (latest 2 versions)
- [ ] Firefox (latest 2 versions)
- [ ] Safari (latest 2 versions)
- [ ] Edge (latest 2 versions)
- [ ] Samsung Internet (latest)
- [ ] Opera (latest)
- [ ] iOS Safari (latest 2 versions)
- [ ] Chrome for Android (latest)

---

## 12. CODE QUALITY STANDARDS

### 12.1 XML

- [ ] Proper indentation (2 spaces)
- [ ] All tags properly closed
- [ ] No hardcoded placeholder values
- [ ] Comments in English only
- [ ] Consistent attribute ordering

### 12.2 CSS

- [ ] CSS custom properties for theming
- [ ] No `!important` (except utilities)
- [ ] Organized by component
- [ ] Responsive-first approach
- [ ] No duplicate rules

### 12.3 JavaScript

- [ ] No global scope pollution
- [ ] No eval/obfuscation
- [ ] Proper error handling
- [ ] Performance-conscious DOM queries
- [ ] Event delegation where appropriate

---

## 13. THEME FILE STRUCTURE

```
theme-name.xml
│
├── <?xml> + <!DOCTYPE> + <html> (namespaces)
├── <head>
│   ├── <b:include name='theme-head'/>   (meta, schema, preconnect)
│   ├── <b:skin>                         (ALL CSS)
│   ├── <b:defaultmarkup> blocks         (widget overrides)
│   └── <b:include name='theme-js'/>     (inline JS)
├── <body>
│   ├── <header>                         (top bar, logo, nav, search)
│   ├── <b:section id='hot-posts'/>      (featured/ticker)
│   ├── <main>
│   │   ├── <b:section id='main'/>       (Blog1 widget)
│   │   └── <aside id='sidebar'>         (sidebar widgets)
│   ├── <footer>                         (footer columns + copyright)
│   ├── Hidden widgets                   (ContactForm for item pages)
│   ├── Modals                           (search, share, cookie)
│   └── <script>                         (all JS at end)
└── </html>
```

---

## 14. THEME GENERATION CHECKLIST

Before finalizing any new theme, verify:

### Essential
- [ ] All required sections present
- [ ] Blog widget renders posts correctly
- [ ] Single post page shows full content
- [ ] Static pages render correctly
- [ ] Labels work (clickable, filtering)
- [ ] Search works (form + results)
- [ ] Archive works (dropdown/list + results)
- [ ] Comments load and work (reply, form)
- [ ] Contact form works on all pages
- [ ] Pagination works (newer/older)
- [ ] Mobile responsive (all breakpoints)
- [ ] No broken images (all have fallbacks)

### SEO
- [ ] All meta tags present and correct
- [ ] All OG tags present
- [ ] Twitter Card tags present
- [ ] Canonical URL correct
- [ ] Robots directives correct per page type
- [ ] WebSite schema present (homepage)
- [ ] BlogPosting schema present (item pages)
- [ ] Breadcrumb schema present (item pages)
- [ ] Semantic heading hierarchy verified
- [ ] All images have alt text

### Performance
- [ ] CSS under 15KB
- [ ] No render-blocking scripts in head
- [ ] font-display: swap on all fonts
- [ ] Native lazy loading on images
- [ ] DNS prefetch for external domains
- [ ] No dead code

### Accessibility
- [ ] Viewport allows zoom (max-scale=5)
- [ ] Touch targets at least 48px
- [ ] prefers-reduced-motion supported
- [ ] Color contrast sufficient

---

## 15. SCORING MATRIX

| Category | Minimum | Target | Stretch |
|----------|---------|--------|---------|
| SEO | 8/10 | 9/10 | 10/10 |
| AEO | 5/10 | 7/10 | 9/10 |
| GEO | 6/10 | 8/10 | 9/10 |
| Performance | 7/10 | 8/10 | 9/10 |
| Accessibility | 7/10 | 8/10 | 10/10 |
| Design Quality | 7/10 | 8/10 | 9/10 |
| Code Quality | 7/10 | 8/10 | 9/10 |
| Widget Coverage | 8/10 | 9/10 | 10/10 |
| **Overall** | **7/10** | **8.5/10** | **9.5/10** |

---

## 16. RESOURCES

- **Blogger XML Reference:** `knowledge-base/BLOGGER_XML_ARCHITECTURE.md`
- **Component Library:** `knowledge-base/COMPONENT_LIBRARY.md`
- **SEO Blueprint:** `knowledge-base/SEO_AEO_GEO_BLUEPRINT.md`
- **Snippet Library:** `knowledge-base/SNIPPET_LIBRARY.xml`
- **Widget Reference:** `knowledge-base/BLOGGER_WIDGET_REFERENCE.md`
- **Failure Patterns:** `knowledge-base/FAILURE_PATTERNS.md`
