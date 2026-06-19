# Component Library — Reusable Production-Ready Components

> 18 reusable UI components extracted from 13 analyzed Blogger themes.
> Each entry: best implementation source, dependencies, data bindings, and customization.

## 1. Header

### Logo + Navigation Header

**Best Implementation:** SEO_Spot_Free_Version.xml
**Alternative (lighter):** amitkr26.xml (lines 696-713)

```
Features:
- Sticky header with backdrop-filter blur
- Logo (text or image) via Header1 widget
- Horizontal nav links via LinkList widget
- Search toggle button
- Dark mode toggle
- Mobile hamburger menu with slide-in panel

Dependencies: None (CSS-based positioning + transitions)
Critical Data Bindings:
  <b:section id='header-room'> → Header1 widget
  <b:section id='nav-menu'> → LinkList1 widget
```

## 2. Navigation

### Desktop Menu + Dropdown

**Best Implementation:** Citron_Free_Version.xml (mega menu pattern)
**Dependencies:** jQuery + Menuiki plugin (Pikitemplates)

```
Features:
- Horizontal menu with dropdown
- Mega menu (5-column post grid on hover)
- Active page highlighting via CSS
- Mobile slide-in panel

Customization: Menu colors via Theme Designer variables
```

## 3. Hero Sections

### A. Color Hero with Search Bar
**Source:** Citron_Free_Version.xml
**Pattern:** Gradient background, centered text, prominent search bar, floating decorative elements

### B. Hero with Featured Grid
**Source:** GridMag_Free_Version.xml
**Pattern:** Large featured post + 2 smaller posts in grid layout

### C. Blob Hero with Animations
**Source:** SEO_Spot_Free_Version.xml
**Pattern:** Blob SVG shapes, animated gradient, floating elements, CTA buttons

## 4. Cards

### Post Card (Blog Grid)
**Best Implementation:** SEO_Spot_Free_Version.xml (.post-card pattern)
```
Features:
- Featured image with lazy loading
- Title with line-clamp
- Snippet
- Meta (date, author, comments)
- Hover elevation effect

Structure:
  article.post-card > a.post-thumb > img[loading=lazy]
                   > .post-body-card > .post-label + h3.post-title-card + p + .post-meta
```

### Service Card
**Best Implementation:** rankrseo-theme.xml (knowledge-base/rankrseo-theme.xml)
```
Features:
- Icon + title + description
- Gradient border on hover
- Card-arrow reveal on hover
- Equal-height via flex column
```

## 5. Blog Grid

**Best Implementation:** rankrseo-theme.xml
```css
.blog-posts { display: grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap: var(--space-2xl); }
```

## 6. Sidebar

**Best Implementation:** SEO_Spot_Free_Version.xml
```
Widgets:
- BlogSearch (search box)
- PopularPosts (thumbnail + title + snippet)
- Label (cloud or list)
- BlogArchive (dropdown)
- Profile (author card)

Critical: All sidebar widget titles need `border-bottom` visual anchor.
```

## 7. Breadcrumb

**Best Implementation:** rankrseo-theme.xml
```xml
<nav class='breadcrumb'>
  <a expr:href='data:blog.homepageUrl'><data:messages.home/></a>
  <span>&#8250;</span>
  <b:if cond='data:post.labels.any'>
    <b:loop index='i' values='data:post.labels' var='label' max='1'>
      <a expr:href='data:label.url'><data:label.name/></a>
      <span>&#8250;</span>
    </b:loop>
  </b:if>
  <span><data:post.title/></span>
</nav>
```

## 8. Post Layout

```
Article wrapper → Featured image → Post body → Labels → Share buttons → Navigation → Related posts → Comments
```

**Critical includables:**
- `postSchema` — JSON-LD BlogPosting schema
- `breadcrumb` — Breadcrumb nav
- `relatedPosts` — Label-based related posts loop
- `threadedComments` — Full comment system with form

## 9. Comments

**Best Implementation:** rankrseo-theme.xml

```
Features:
- Threaded comments (native Blogger)
- Embedded comment form iframe
- Allow/disallow new comments toggle
- No new comments message

Dependencies: Blogger platform JS (BLOG_CMT_createIframe)
```

## 10. Contact Form

**Critical Pattern — Hidden Widget Duplication:**
```xml
<!-- Visible on homepage -->
<b:section id='ContactSection'> → ContactForm2 widget

<!-- Hidden duplicate for item pages (prevents iframe breakage) -->
<b:section id='hidden-contact' deleted='true'>
  <b:widget id='ContactForm1' ...>
    <div style='display:none'>...</div>
```

## 11. CTA Section

**Best Implementation:** rankrseo-theme.xml
```
Features:
- Gradient background banner
- Two CTA buttons (primary + outline)
- Centered text layout
```

## 12. Footer

**Best Implementation:** SEO_Spot_Free_Version.xml
```
Columns:
1. About (HTML widget — logo + description + newsletter)
2. Services (LinkList)
3. Quick Links (LinkList)
4. Contact (LinkList — email, phone, address)

Bottom bar: Copyright + footer nav + social links
Social: Circular icon links with hover lift + glow
```

## 13. Pagination

**Post Navigation** (single post):
```xml
<a class='post-nav-link' expr:href='data:newerPageUrl' rel='prev'>&larr; Newer Post</a>
<a class='post-nav-link next' expr:href='data:olderPageUrl' rel='next'>Older Post &rarr;</a>
```

**Blog Pager** (multi-post views):
```xml
<b:if cond='data:newerPageUrl or data:olderPageUrl'>
  <div class='blog-pager'>
    <a expr:href='data:newerPageUrl' rel='prev'>&larr; Newer</a>
    <a expr:href='data:olderPageUrl' rel='next'>Older &rarr;</a>
  </div>
</b:if>
```

## 14. Search Overlay

**Best Implementation:** rankrseo-theme.xml, SEO_Spot_Free_Version.xml
```
Features:
- Full-screen overlay with blur backdrop
- Animated search input
- BlogSearch widget integration
- Close on Escape key
```

## 15. Dark Mode Toggle

**Best Implementation:** rankrseo-theme.xml
```
Features:
- Sun/moon icon toggle (animated)
- localStorage persistence
- CSS custom property swap
- Transition on all themed properties

Data binding:
  <button onclick='toggleDark()' id='darkToggle'>&#9790;</button>
  JS: document.body.classList.toggle('dark-mode')
```

## 16. Cookie Consent

**Best Implementation:** rankrseo-theme.xml
```
Features:
- Bottom banner with accept button
- localStorage to track consent
- Simple text + button layout
```

## 17. Share Modal

**Best Implementation:** rankrseo-theme.xml
```
Share channels:
- Facebook
- Twitter/X
- LinkedIn
- WhatsApp
```

## 18. FAQ Accordion

**Best Implementation:** rankrseo-theme.xml
```
Features:
- Semantic details/summary elements
- Animated rotation on expand (45deg)
- JSON-LD FAQPage schema alongside visible HTML
- Pure CSS + minimal JS toggle
```
