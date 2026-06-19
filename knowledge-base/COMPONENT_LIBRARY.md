# Component Library — Reusable Production-Ready Components

This document catalogs all reusable components extracted from the analyzed themes. Each entry identifies the best implementation, its source file, dependencies, and customization options.

---

## 1. Header

### Logo + Navigation Header

**Best Implementation:** SEO_Spot_Free_Version.xml (lines ~400-600 area)
**Alternative:** amitkr26.xml (lines 696-713) — simpler, lighter

```
Features:
- Sticky header with backdrop-filter blur
- Logo (text or image)
- Horizontal nav links
- Search toggle
- Dark mode toggle (UI only)
- Mobile hamburger menu

Dependencies: None (CSS-based)
Customization: --accent, --primary, --bg colors; header height; font sizes
```

**Critical Data Bindings:**
```xml
<a expr:href='data:blog.homepageUrl'>Home</a>
<b:section id='header-room' maxwidgets='1' showaddelement='yes'>
  <b:widget id='Header1' type='Header'>
```

---

## 2. Navigation

### Desktop Horizontal Menu + Dropdown

**Best Implementation:** Citron_Free_Version.xml (mega menu pattern)
**Dependencies:** jQuery + Menuiki plugin (Pikitemplates)

```
Features:
- Horizontal menu with dropdown
- Mega menu (5-column post grid on hover)
- Active page highlighting
- Sub-menu support

Customization: Menu colors via Theme Designer variables
```

### Mobile Hamburger Menu

**Best Implementation:** Wind_Spot_Free_Version.xml (slide-in drawer)
**Simpler alternative:** amitkr26.xml (lines 696-713) — pure CSS/JS, no dependencies

```
Features:
- Fixed slide-in from left (80% width)
- Overlay backdrop
- Close button
- Social links in mobile menu
- CSS cubic-bezier transition

Dependencies: None (CSS + vanilla JS)
```

---

## 3. Hero / Featured Sections

### Color Hero with Search

**Best Implementation:** Citron_Free_Version.xml (color-section)

```
Features:
- Gradient background
- Search bar
- Floating geometric animations (rotating-box)
- SVG wave divider at bottom
- Category buttons

Dependencies: None
```

### Blob Hero (Portfolio)

**Best Implementation:** amitkr26.xml (lines 241-315)

```
Features:
- Radial gradient background
- Animated blob shape (border-radius morphing)
- Gradient text for name
- Two-column: content + image
- CTA buttons
- Responsive grid → single column

Dependencies: None (CSS animation only)
```

### Featured Posts Grid

**Best Implementation:** Monster_Free_Version.xml (7-col grid)
**Alternative:** GridMag_Free_Version.xml (4-col numbered grid)

```
Features:
- CSS Grid layout
- 4-7 column featured posts
- Numbered items (counter-increment)
- Overlay gradient on images
- Hot/trending label
- Responsive collapse → 2-col → 1-col

Dependencies: PopularPosts widget
```

### News Ticker

**Best Implementation:** Monster_Free_Version.xml, SEO_Spot_Free_Version.xml

```
Features:
- Horizontal scrolling breaking news
- Auto-rotate with interval
- Prev/Next buttons
- Active class management
- Responsive

Dependencies: jQuery + LazyTicker plugin
```

---

## 4. Cards

### Post Card (Index View)

**Best Implementation:** All Pikitemplates themes (post-filter class)

```
Structure:
+-- .post-filter
    +-- .post-filter-link (thumbnail)
    |   +-- img.snip-thumbnail (lazy-loaded)
    +-- .entery-category-box
        +-- .post-tag (label/pill)
        +-- h2.entry-title (clamped to 2 lines)
        +-- .post-snip (author, date, comments)
```

### Project Card (Portfolio)

**Best Implementation:** amitkr26.xml (lines 416-486)

```
Structure:
+-- .project-card.card
    +-- .project-image (200px, overflow hidden)
    |   +-- img (zoom on hover)
    +-- .project-info
        +-- h3 (title)
        +-- p (description)
        +-- .project-links
            +-- a.project-link

Features: Image zoom on hover, flex-grow for equal height, auto-fit grid
```

### Skill Tag Card

**Best Implementation:** amitkr26.xml (lines 378-414)

```
+-- .skill-card.card
    +-- h3 (category name)
    +-- .skill-tags (flex wrap)
        +-- span.skill-tag (pill badges)

Features: Wrap flex, pill shape, hover border accent, auto-fit grid
```

---

## 5. Blog Grid

**Best Implementation:** amitkr26.xml (lines 488-551)
**Pikitemplates Pattern:** post-filter layout with CSS Grid

```
Features:
- CSS Grid: auto-fit, minmax(350px, 1fr)
- Card layout with thumbnail + content
- 3-line snippet clamp
- Read more link
- Pagination below grid

Dependencies: Blog widget
```

---

## 6. Sidebar

**Best Implementation:** SEO_Spot_Free_Version.xml (standard Pikitemplates sidebar)

```
Features:
- Float right layout (width: 320px)
- Sticky sidebar (Theia Sticky Sidebar plugin)
- Popular posts with thumbnails
- Label cloud
- Blog archive
- Email subscription
- Profile widget
- HTML/Ad units

Dependencies: jQuery + Theia Sticky Sidebar
```

---

## 7. Breadcrumb

**Best Implementation:** helthifi.xml (JSON-LD + visual)

```
Structure:
<nav id='breadcrumb'>
  <a href='/'>Home</a> › 
  <a href='/label/topic'>Topic</a> › 
  <span>Post Title</span>
</nav>

Features:
- Visual breadcrumb (Home > Label > Title)
- JSON-LD BreadcrumbList schema
- Conditional: only on item pages
- First label used for category

Dependencies: None
```

---

## 8. Post Layout (Single Item)

**Best Implementation:** Combined from all Pikitemplates themes

```
Structure:
<article>
  <h1 class='entry-title'>Post Title</h1>
  <div class='all-flex'>
    <div class='post-inner-data'>
      <span class='author-image'><img/></span>
      <span class='post-author'>Author</span>
      <span class='post-date'>Date</span>
      <span id='readTime'>X min read</span>
    </div>
  </div>
  <div id='postBody' class='post-body entry-content'>
    <data:post.body/>
  </div>
  <!-- Related Posts -->
  <!-- Share Buttons -->
  <!-- Comments -->
</article>
```

**Features:**
- Author avatar + name + date
- Reading time estimation (JS)
- Featured image display
- Label display
- Share buttons (Facebook, Twitter, WhatsApp)
- Related posts
- Breadcrumb navigation
- Comments section

---

## 9. Comments

**Best Implementation:** All Pikitemplates themes (threaded comments)

```
Features:
- Native Blogger threaded comments
- Embedded comment form (iframe)
- Comment count display
- Reply system
- Nested comment support
- New comment toggle

Dependencies: Blogger platform JS (BLOG_CMT_createIframe)
```

---

## 10. Contact Form

**Best Implementation:** amitkr26.xml (lines 977-995)

```
Structure:
+-- .contact-form-widget
    +-- form
        +-- input.name (placeholder from data:contactFormNameMsg)
        +-- input.email (placeholder from data:contactFormEmailMsg)
        +-- textarea.message (placeholder from data:contactFormMessageMsg)
        +-- input.submit (value from data:contactFormSendMsg)
        +-- .contact-form-error-message
        +-- .contact-form-success-message

Dependencies: ContactForm widget (Blogger built-in)
Customization: CSS variables for colors, border-radius, focus states
```

---

## 11. CTA Section

**Best Implementation:** amitkr26.xml (lines 723-726)

```
Features:
- Primary button (filled, accent color)
- Secondary button (outlined, border)
- Hover effects (translateY, shadow)
- Centered or inline layout
```

---

## 12. Footer

**Best Implementation:** SEO_Spot_Free_Version.xml (3-column + copyright)

```
Structure:
+-- #llmflii (footer wrapper, dark background)
    +-- .container
        +-- Footer columns (3-4)
            +-- PopularPosts / Image / LinkList widgets
    +-- .footer-container (copyright bar, darker)
        +-- .footer-copyright (attribution text)
        +-- .footer-checks-menu (footer nav links)

Features:
- Dark background (--footer.background.color)
- Gadget titles in light color
- Social link icons
- Copyright text
- Footer navigation (privacy, about, contact)
- Responsive columns → stack on mobile
```

---

## 13. Pagination

### Newer/Older Links

**Implementation:** All themes

```
Features:
- Previous page link (rel='previous')
- Next page link (rel='next')
- Conditional rendering
- Title attributes

Condition: data:newerPageUrl or data:olderPageUrl
```

### Numbered Pagination

**Implementation:** helthifi.xml, neet.xml (custom JS pattern)

```
Features:
- Page number buttons
- Current page highlight
- Previous/Next buttons
- Ellipsis for page gaps
- Label-aware URL generation

Dependencies: Inline eval JS function
```

---

## 14. Search Overlay

**Best Implementation:** All Pikitemplates themes (#ijjiIf)

```
Features:
- Modal overlay with blur backdrop
- Centered search input (max-width 480px)
- Close button
- Animated with CSS transforms
- Auto-focus on open

Dependencies: None (CSS + JS)
```

---

## 15. Dark Mode Toggle

**Best Implementation:** All Pikitemplates themes (zeitdilo toggle)
**Status:** UI ONLY — no actual dark mode CSS variables implemented

```
Features:
- Sun/Moon icon toggle
- Sliding animation
- Persistent state (localStorage in some)
- Class toggle on body

Missing: Actual CSS custom property overrides for dark palette
```

**To make functional, add:**
```css
body.dark-mode {
  --bg: #0f172a;
  --surface: #1e293b;
  --text: #e2e8f0;
  --text-muted: #94a3b8;
  --border: #334155;
}
```

---

## 16. Cookie Consent

**Best Implementation:** All Pikitemplates themes (#xliiv)

```
Features:
- Fixed bottom-left toast (300px wide)
- Accept button
- Cookie icon
- cookies-show class toggle
- Fade animation
```

---

## 17. Share Modal

**Best Implementation:** All Pikitemplates themes (StickyBox)

```
Features:
- Full-screen overlay with centered modal
- Social share buttons (4-col grid)
- Facebook, Twitter, WhatsApp, Pinterest
- Copy link input
- Close button

Dependencies: None
```

---

## 18. Floating Buttons

### Back to Top

```
Features:
- Fixed bottom-right position
- Scroll-triggered visibility
- Smooth scroll to top
- Arrow icon

Implementation: CSS + JS scroll listener
```

### Sticky Mobile CTA

**Implementation:** Shopping_Free_Version.xml

```
Features:
- Fixed bottom bar on mobile
- WhatsApp, Call, Download buttons
- Only visible on mobile screens
```

---

## Component Reusability Rules

1. **Prefer CSS-only components** over JS-dependent ones
2. **Use CSS custom properties** for all color/sizing customization
3. **Keep JS dependencies minimal** — avoid jQuery when vanilla JS suffices
4. **Each component should be a `<b:includable>`** for easy inclusion
5. **Provide responsive fallbacks** for all grid/flex layouts
6. **Maintain 48px minimum touch targets** for mobile
7. **Use semantic HTML** (`<nav>`, `<article>`, `<section>`, `<header>`, `<footer>`)
