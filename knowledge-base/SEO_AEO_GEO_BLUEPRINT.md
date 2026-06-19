# SEO / AEO / GEO Optimization Blueprint

> Master optimization standards for all future Blogger themes.

---

## 1. TECHNICAL SEO

### 1.1 Meta Tags — Required

```xml
<!-- Charset -->
<meta charset='UTF-8'/>

<!-- Viewport (accessibility: allow zoom) -->
<meta content='width=device-width, initial-scale=1, minimum-scale=1, maximum-scale=5' name='viewport'/>

<!-- Title — single universal tag, properly escaped -->
<title><data:view.title.escaped/></title>

<!-- Canonical — must use data:view.url.canonical -->
<link expr:href='data:view.url.canonical' rel='canonical'/>

<!-- Description -->
<meta expr:content='data:view.description.escaped' name='description'/>

<!-- Robots — extended directives -->
<b:if cond='!data:view.isSearch and !data:view.isLabelSearch'>
  <meta content='index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1' name='robots'/>
</b:if>
<b:if cond='data:view.isArchive'>
  <meta content='noindex' name='robots'/>
</b:if>
<b:if cond='data:view.isSearch or data:view.isLabelSearch'>
  <meta content='noindex,nofollow' name='robots'/>
</b:if>

<!-- Theme color (mobile browser chrome) -->
<meta expr:content='data:skin.vars.keycolor' name='theme-color'/>
```

### 1.2 Open Graph — Required

```xml
<!-- Conditional type -->
<b:if cond='data:view.isHomepage'><meta content='website' property='og:type'/></b:if>
<b:if cond='data:view.isSingleItem'><meta content='article' property='og:type'/></b:if>
<b:if cond='data:view.isMultipleItems and not data:view.isHomepage'>
  <meta content='object' property='og:type'/>
</b:if>

<!-- Core OG tags -->
<meta expr:content='data:view.title.escaped' property='og:title'/>
<meta expr:content='data:blog.url.canonical' property='og:url'/>
<meta expr:content='data:view.description.escaped' property='og:description'/>
<meta expr:content='data:blog.title.escaped' property='og:site_name'/>
<meta expr:content='data:blog.localeUnderscoreDelimited' property='og:locale'/>

<!-- OG Image — use featured image with fallback -->
<b:if cond='data:view.featuredImage'>
  <meta expr:content='data:view.featuredImage' property='og:image'/>
</b:if>
<b:if cond='data:view.isMultipleItems and data:widgets.Blog.first.posts[0].featuredImage'>
  <meta expr:content='data:widgets.Blog.first.posts[0].featuredImage' property='og:image'/>
</b:if>
```

### 1.3 Twitter Card — Required

```xml
<meta content='summary_large_image' name='twitter:card'/>
<meta expr:content='data:view.title.escaped' name='twitter:title'/>
<meta expr:content='data:blog.url.canonical' name='twitter:domain'/>
<meta expr:content='data:view.description.escaped' name='twitter:description'/>
<b:if cond='data:view.featuredImage'>
  <meta expr:content='data:view.featuredImage' name='twitter:image'/>
</b:if>
<!-- IMPORTANT: Set twitter:creator to actual handle from settings -->
<!-- Use data:view.description.escaped as fallback; ideally from blog setting -->
```

### 1.4 Favicon

```xml
<link expr:href='data:blog.blogspotFaviconUrl' rel='icon' type='image/x-icon'/>
<link expr:href='data:blog.blogspotFaviconUrl' rel='icon' sizes='32x32'/>
<link expr:href='data:blog.blogspotFaviconUrl' rel='icon' sizes='100x100'/>
<link expr:href='data:blog.blogspotFaviconUrl' rel='apple-touch-icon'/>
<meta expr:content='data:blog.blogspotFaviconUrl' name='msapplication-TileImage'/>
```

### 1.5 DNS Prefetch & Preconnect — Required

```xml
<link href='//1.bp.blogspot.com' rel='dns-prefetch'/>
<link href='//www.blogger.com' rel='dns-prefetch'/>
<link href='//fonts.googleapis.com' rel='dns-prefetch'/>
<link href='//cdnjs.cloudflare.com' rel='dns-prefetch'/>
<link href='//pagead2.googlesyndication.com' rel='dns-prefetch'/>
<link href='//www.gstatic.com' rel='preconnect'/>
```

---

## 2. STRUCTURED DATA (Schema.org)

### 2.1 WebSite + SearchAction — REQUIRED (Homepage only)

```json
{
  "@context": "http://schema.org",
  "@type": "WebSite",
  "name": "BLOG_TITLE",
  "url": "BLOG_URL",
  "potentialAction": {
    "@type": "SearchAction",
    "target": "BLOG_URL/search?q={search_term_string}",
    "query-input": "required name=search_term_string"
  }
}
```

### 2.2 BlogPosting — REQUIRED (Item pages)

```json
{
  "@context": "http://schema.org",
  "@type": "BlogPosting",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "POST_URL"
  },
  "headline": "POST_TITLE",
  "description": "POST_SNIPPET",
  "image": {
    "@type": "ImageObject",
    "url": "FEATURED_IMAGE_URL"
  },
  "author": {
    "@type": "Person",
    "name": "AUTHOR_NAME",
    "url": "AUTHOR_URL"
  },
  "publisher": {
    "@type": "Organization",
    "name": "BLOG_NAME",
    "logo": {
      "@type": "ImageObject",
      "url": "LOGO_URL"
    }
  },
  "datePublished": "ISO_DATE",
  "dateModified": "ISO_DATE"
}
```

### 2.3 BreadcrumbList — REQUIRED (Item pages)

```json
{
  "@context": "http://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {"@type": "ListItem", "position": 1, "name": "Home", "item": "HOME_URL"},
    {"@type": "ListItem", "position": 2, "name": "CATEGORY", "item": "CATEGORY_URL"},
    {"@type": "ListItem", "position": 3, "name": "POST_TITLE"}
  ]
}
```

### 2.4 Organization — REQUIRED (Part of BlogPosting publisher)

```json
{
  "@type": "Organization",
  "name": "BLOG_NAME",
  "logo": {
    "@type": "ImageObject",
    "url": "LOGO_URL"
  }
}
```

### 2.5 Person — REQUIRED (Author in BlogPosting)

```json
{
  "@type": "Person",
  "name": "AUTHOR_NAME",
  "url": "AUTHOR_PROFILE_URL"
}
```

### 2.6 FAQPage — RECOMMENDED (Conditional)

```json
{
  "@context": "http://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "QUESTION_TEXT",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "ANSWER_TEXT"
      }
    }
  ]
}
```

### 2.7 @graph — Bundle Method (Pikitemplates Gold Standard)

Bundle multiple schemas into one script:

```json
{
  "@context": "http://schema.org",
  "@graph": [
    {WebSite schema},
    {BlogPosting schema},
    {BreadcrumbList schema}
  ]
}
```

### 2.8 Additional Schema Types (Future Enhancement)

| Schema | When to Use | Priority |
|--------|-------------|----------|
| `Article` | Static pages | Medium |
| `NewsArticle` | News/blog content | Low (BlogPosting sufficient) |
| `HowTo` | Tutorial content | Medium (AEO benefit) |
| `FAQPage` | FAQ content | High (AEO benefit) |
| `Product` | eCommerce (Shopping theme) | Medium |
| `VideoObject` | Video content | Low |
| `Speakable` | Voice search | Low (future) |
| `WPHeader` | Header landmark | Low (nice to have) |
| `WPSideBar` | Sidebar landmark | Low (nice to have) |
| `WPFooter` | Footer landmark | Low (nice to have) |
| `SiteNavigationElement` | Navigation | Low (nice to have) |

---

## 3. SEMANTIC HTML

### 3.1 Heading Hierarchy

| Page Type | h1 | h2 | h3 | h4 |
|-----------|-----|-----|-----|-----|
| Homepage | Blog title (visible or hidden) | Post titles | Widget titles | - |
| Single Post | Post title | - | Widget titles | Comment sections |
| Static Page | Page title | - | Section subheadings | - |
| Archive/Label | Archive/Label name | Post titles | Widget titles | - |
| Error Page | "404" or error title | - | - | - |

Rule: ONE h1 per page. Logical descending hierarchy.

### 3.2 Semantic Landmarks

```xml
<body>
  <header>  <!-- or role="banner" -->
    <nav>    <!-- or role="navigation" -->
  </header>
  <main>    <!-- or role="main" -->
    <article>  <!-- Individual post -->
      <h1>Title</h1>
      <div class='post-body entry-content'>
        <data:post.body/>
      </div>
    </article>
    <aside>  <!-- Sidebar -->
    </aside>
  </main>
  <footer>  <!-- or role="contentinfo" -->
  </footer>
</body>
```

### 3.3 Image Alt Text (Best Practice)

```xml
<!-- Post thumbnail with ternary fallback -->
<img expr:alt='data:post.title ? data:post.title : data:messages.noTitle'
     expr:src='...'/>

<!-- Author photo -->
<img expr:alt='data:post.author.name' expr:src='...'/>

<!-- Decorative icons (use empty alt) -->
<img alt='' src='decorative-icon.png'/>
```

---

## 4. AEO (ANSWER ENGINE OPTIMIZATION)

### 4.1 Principles

AEO optimizes content for AI-powered answer engines (Google Featured Snippets, Bing Answers, etc.)

### 4.2 Implementation Requirements

| Pattern | Implementation | Priority |
|---------|---------------|----------|
| **FAQPage Schema** | JSON-LD FAQPage with Question + Answer | HIGH |
| **Clean Q&A Structure** | Visible FAQ on page matching schema | HIGH |
| **Short Snippets** | Paragraphs under 2-3 sentences | MEDIUM |
| **List Content** | Use `<ul>`/`<ol>` for structured lists | MEDIUM |
| **Table Content** | Use `<table>` for data comparison | MEDIUM |
| **Question Headings** | h2/h3 in question format ("How to...?") | MEDIUM |
| **Definition Boxes** | `<dfn>` or schema DefinedTerm | LOW |
| **HowTo Schema** | Step-by-step structured data | MEDIUM |
| **Speakable** | XML for Google Assistant | LOW |

### 4.3 FAQ Block Template

```xml
<div class='faq-section' itemscope='' itemtype='https://schema.org/FAQPage'>
  <div class='faq-item' itemscope='' itemprop='mainEntity' itemtype='https://schema.org/Question'>
    <h3 itemprop='name'>Question text here?</h3>
    <div itemscope='' itemprop='acceptedAnswer' itemtype='https://schema.org/Answer'>
      <div itemprop='text'>
        <p>Answer text here.</p>
      </div>
    </div>
  </div>
</div>
```

---

## 5. GEO (GENERATIVE ENGINE OPTIMIZATION)

### 5.1 Principles

GEO optimizes for AI/LLM crawlers (ChatGPT, Gemini, Perplexity, AI search engines).

### 5.2 Entity Optimization

| Entity Type | Schema | Implementation |
|-------------|--------|----------------|
| Blog | `WebSite` | JSON-LD with name, url, description |
| Author | `Person` | JSON-LD with name, url, image |
| Organization | `Organization` | JSON-LD with name, logo |
| Post | `BlogPosting` | JSON-LD with headline, date, author, publisher |
| Breadcrumb | `BreadcrumbList` | JSON-LD with itemListElement |
| FAQ | `FAQPage` | JSON-LD with mainEntity |

### 5.3 Content Chunking

```
Clear section boundaries using:
- <section id='unique-id'> — Unique landmark per section
- <h2> — Section headings that describe content
- <article> — Self-contained content units
- <aside> — Complementary content
- <nav> — Navigation landmarks
```

### 5.4 Trust Signals

| Signal | Implementation | Priority |
|--------|---------------|----------|
| Author credibility | Author name + URL + photo in JSON-LD | HIGH |
| Publication date | `datePublished` ISO 8601 | HIGH |
| Last modified | `dateModified` ISO 8601 | HIGH |
| Organization | Publisher with logo in JSON-LD | HIGH |
| Citations | Citation-specific markup | LOW |
| Fact-checking | ClaimReview schema | LOW |

### 5.5 Machine Readability

- Use `itemprop` attributes for microdata (backup to JSON-LD)
- Use semantic HTML5 elements
- Avoid obfuscated CSS class names (prefer descriptive ones)
- Use meaningful `id` attributes
- Keep critical content in HTML (not loaded by JS)

---

## 6. PERFORMANCE SEO

### 6.1 Core Web Vitals Optimization

| Metric | Target | Strategy |
|--------|--------|----------|
| LCP | < 2.5s | Preload hero image, optimize font loading, reduce CSS size |
| CLS | < 0.1 | Explicit image dimensions, no late-loading content shifts |
| INP | < 200ms | Defer non-critical JS, minimize main thread work |

### 6.2 Font Optimization

```css
/* Always use font-display: swap */
@font-face {
  font-family: 'Font Name';
  font-style: normal;
  font-weight: 400;
  font-display: swap;
  src: url(...) format('woff2');
}
```

### 6.3 Image Optimization

```xml
<!-- Native lazy loading -->
<img loading='lazy' expr:src='...' expr:alt='...'/>

<!-- Preload featured image -->
<link rel='preload' as='image' expr:href='data:view.featuredImage'/>

<!-- Responsive images via resizeImage() -->
<img expr:src='resizeImage(data:post.featuredImage, 800, "16:9")'/>
```

### 6.4 JavaScript Optimization

```
✓ Use async for external scripts
✓ Defer non-critical inline JS
✗ Avoid document.write
✗ Avoid blocking inline scripts in <head>
✓ Move scripts to end of <body>
```

---

## 7. CRAWLABILITY

### 7.1 Internal Linking

```
✓ Breadcrumb navigation on all item pages
✓ Related posts at bottom of posts
✓ Label/category links
✓ Recent posts in sidebar
✓ Pagination with rel='next' / rel='previous'
✗ No orphan pages
```

### 7.2 Robots Directives

| Page Type | Directive | Rationale |
|-----------|-----------|-----------|
| Homepage | `index, follow` | Main entry |
| Posts | `index, follow` | Primary content |
| Static Pages | `index, follow` | Important content |
| Label Pages | `noindex,follow` | Avoid duplicate content |
| Search Results | `noindex,nofollow` | No value for index |
| Archive Pages | `noindex,follow` | Avoid duplicate content |
| 404 | (none needed) | No content |
| Mobile | NO restriction | Essential for mobile indexing |

### 7.3 Sitemap

Blogger auto-generates sitemap at `/sitemap.xml`. Ensure:
- Posts are published as public
- Labels are used consistently
- Archive is accessible

---

## 8. OPTIMIZATION CHECKLIST

### Pre-Release Checklist

- [ ] Title tag: single `<data:view.title.escaped/>`
- [ ] Canonical: `<link expr:href='data:view.url.canonical' rel='canonical'/>`
- [ ] Meta description: `data:view.description.escaped`
- [ ] Robots: extended directives with conditional noindex
- [ ] Open Graph: all required tags present
- [ ] Twitter Card: summary_large_image
- [ ] WebSite schema: with SearchAction
- [ ] BlogPosting schema: on item pages
- [ ] Breadcrumb schema: on item pages
- [ ] Organization schema: with logo
- [ ] Semantic headings: single h1, logical hierarchy
- [ ] Image alt text: all images have descriptive alt
- [ ] DNS prefetch: for all external domains
- [ ] Viewport: includes minimum-scale=1, maximum-scale=5
- [ ] Pagination: rel='next' and rel='previous'
- [ ] No render-blocking JS in head
- [ ] font-display: swap on all @font-face
- [ ] Native lazy loading on images
- [ ] No duplicate meta tags
- [ ] No hardcoded placeholder values
