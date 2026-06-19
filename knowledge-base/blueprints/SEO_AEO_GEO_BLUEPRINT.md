# SEO / AEO / GEO Optimization Blueprint

> Master optimization standards for all future RankrSEO Blogger themes.
> Cross-ref: SNIPPET_LIBRARY.xml (snippets 01-05 for meta/schema), RANKRSEO_THEME_SPEC.md

## 1. TECHNICAL SEO

### 1.1 Meta Tags — Required Header Block

```xml
<meta charset='UTF-8'/>
<meta content='width=device-width, initial-scale=1, minimum-scale=1, maximum-scale=5' name='viewport'/>
<title><data:view.title.escaped/></title>
<link expr:href='data:view.url.canonical' rel='canonical'/>
<meta expr:content='data:view.description.escaped' name='description'/>
<b:if cond='!data:view.isSearch and !data:view.isLabelSearch'>
  <meta content='index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1' name='robots'/>
</b:if>
<b:if cond='data:view.isArchive'>
  <meta content='noindex' name='robots'/>
</b:if>
<b:if cond='data:view.isSearch or data:view.isLabelSearch'>
  <meta content='noindex,nofollow' name='robots'/>
</b:if>
<meta expr:content='data:skin.vars.keycolor' name='theme-color'/>
<meta expr:content='data:skin.vars.keycolor' name='msapplication-navbutton-color'/>
```

### 1.2 Open Graph — Required

```xml
<b:if cond='data:view.isHomepage'><meta content='website' property='og:type'/></b:if>
<b:if cond='data:view.isSingleItem'><meta content='article' property='og:type'/></b:if>
<b:if cond='data:view.isMultipleItems and not data:view.isHomepage'>
  <meta content='object' property='og:type'/>
</b:if>
<meta expr:content='data:blog.title.escaped' property='og:site_name'/>
<meta expr:content='data:view.title.escaped' property='og:title'/>
<meta expr:content='data:view.url.canonical' property='og:url'/>
<meta expr:content='data:view.description.escaped' property='og:description'/>
<b:if cond='data:view.isSingleItem'>
  <b:if cond='data:post.featuredImage'>
    <meta expr:content='data:post.featuredImage' property='og:image'/>
  </b:if>
  <meta expr:content='data:post.author.name' property='article:author'/>
  <meta expr:content='data:post.date.iso8601' property='article:published_time'/>
</b:if>
```

### 1.3 Twitter Cards

```xml
<meta content='summary_large_image' name='twitter:card'/>
<meta expr:content='data:blog.title.escaped' name='twitter:site'/>
<meta expr:content='data:view.title.escaped' name='twitter:title'/>
<meta expr:content='data:view.description.escaped' name='twitter:description'/>
<b:if cond='data:view.isSingleItem and data:post.featuredImage'>
  <meta expr:content='data:post.featuredImage' name='twitter:image'/>
</b:if>
```

### 1.4 Favicon & Icons

```xml
<link expr:href='data:blog.blogspotFaviconUrl' rel='icon' type='image/x-icon'/>
<link expr:href='data:blog.blogspotFaviconUrl' rel='icon' sizes='32x32'/>
<link expr:href='data:blog.blogspotFaviconUrl' rel='icon' sizes='100x100'/>
<link expr:href='data:blog.blogspotFaviconUrl' rel='apple-touch-icon'/>
<meta expr:content='data:blog.blogspotFaviconUrl' name='msapplication-TileImage'/>
```

### 1.5 DNS Prefetch & Preconnect

```xml
<link href='//1.bp.blogspot.com' rel='dns-prefetch'/>
<link href='//www.blogger.com' rel='dns-prefetch'/>
<link href='//fonts.googleapis.com' rel='dns-prefetch'/>
```

## 2. STRUCTURED DATA (JSON-LD)

### 2.1 WebSite Schema (on Homepage)
```json
{
  "@context": "http://schema.org",
  "@type": "WebSite",
  "@id": "#website",
  "url": "<data:blog.homepageUrl/>",
  "name": "<data:blog.title.escaped/>",
  "description": "<data:blog.description/>",
  "potentialAction": {
    "@type": "SearchAction",
    "target": "<data:blog.homepageUrl/>search?q={search_term_string}",
    "query-input": "required name=search_term_string"
  }
}
```

### 2.2 BlogPosting Schema (on Post Pages)
```json
{
  "@context": "http://schema.org",
  "@type": "BlogPosting",
  "mainEntityOfPage": {"@type":"WebPage","@id":"<data:post.url.canonical/>"},
  "headline": "<data:post.title/>",
  "description": "...",
  "image": {"@type":"ImageObject","url":"<data:post.featuredImage/>"},
  "author": {"@type":"Person","name":"<data:post.author.name/>"},
  "publisher": {"@type":"Organization","name":"<data:blog.title.escaped/>"},
  "datePublished": "<data:post.date.iso8601/>",
  "dateModified": "<data:post.date.iso8601/>"
}
```

### 2.3 BreadcrumbList Schema
```json
{
  "@context": "http://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {"@type":"ListItem","position":1,"name":"Home","item":"<data:blog.homepageUrl/>"},
    {"@type":"ListItem","position":2,"name":"<data:post.labels.first.name/>","item":"<data:post.labels.first.url/>"},
    {"@type":"ListItem","position":3,"name":"<data:post.title/>","item":"<data:post.url.canonical/>"}
  ]
}
```

### 2.4 Organization Schema
```json
{
  "@context": "http://schema.org",
  "@type": "Organization",
  "@id": "#organization",
  "name": "<data:blog.title.escaped/>",
  "url": "<data:blog.homepageUrl/>"
}
```

### 2.5 FAQPage Schema
```json
{
  "@context": "http://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {"@type":"Question","name":"Question 1","acceptedAnswer":{"@type":"Answer","text":"Answer 1"}},
    {"@type":"Question","name":"Question 2","acceptedAnswer":{"@type":"Answer","text":"Answer 2"}}
  ]
}
```

### 2.6 @graph Bundle (Recommended)
Use `@graph` array to bundle multiple schemas into a single script:
```json
{
  "@context": "http://schema.org",
  "@graph": [
    {"@type":"WebSite","@id":"#website","url":"...","name":"..."},
    {"@type":"BlogPosting","@id":"#post","mainEntityOfPage":{"@id":"..."},...},
    {"@type":"BreadcrumbList","itemListElement":[...]},
    {"@type":"Organization","@id":"#organization","name":"...","url":"..."}
  ]
}
```

## 3. AEO — Answer Engine Optimization

### Principles
1. **Direct Answers** — Open content with a clear, concise answer to the target query
2. **FAQ Structure** — Q&A pairs marked up with FAQPage schema
3. **Snippet Optimization** — First 160 chars of content should answer the question
4. **Semantic HTML** — Proper heading hierarchy (h1→h2→h3), descriptive alt text

### FAQ Section Template
```xml
<section class='faq-section'>
  <div class='faq-item'>
    <button onclick='toggleFaq(this)'><span>Question?</span><i class='faq-icon'></i></button>
    <div class='faq-answer'><p>Answer text here.</p></div>
  </div>
</section>
```

## 4. GEO — Generative Engine Optimization

### Principles
1. **Entity Optimization** — Define entities explicitly: people, places, organizations, concepts
2. **Semantic Chunking** — Content organized into clear sections with descriptive headings
3. **Trust Signals** — Author bylines, publication dates, citations, references
4. **Structured Data** — Comprehensive JSON-LD for AI crawler context

### AI Crawler Optimization Checklist
- [ ] JSON-LD schema bundled via @graph
- [ ] Semantic HTML5 elements (article, section, nav, aside, header, footer)
- [ ] Descriptive heading hierarchy
- [ ] Image alt text with entity keywords
- [ ] Author information on all posts
- [ ] Publication dates in ISO 8601 format
- [ ] Internal linking with descriptive anchor text
- [ ] FAQPage schema for Q&A content
- [ ] Organization + WebSite + BreadcrumbList schemas
- [ ] Open Graph + Twitter Cards
- [ ] Canonical URLs on all pages
- [ ] `noindex` on archive/label/search

## 5. Performance SEO

### Targets
- **PageSpeed Score:** 90+ (mobile + desktop)
- **LCP:** < 2.5s
- **FID:** < 100ms
- **CLS:** < 0.1
- **TBT:** < 200ms

### Tactics
1. **Lazy Loading** — `loading='lazy'` on all images
2. **Minimal JS** — Vanilla JS only; defer all scripts
3. **CSS Variables** — Single token system, no redundant declarations
4. **Font Optimization** — `font-display: swap`, subset where possible
5. **No Render-Blocking** — Inline critical CSS in `<b:skin>`, defer non-critical
6. **Image Sizing** — Explicit `width` + `height` attributes
7. **Responsive Images** — `resizeImage()` function for appropriate sizes
