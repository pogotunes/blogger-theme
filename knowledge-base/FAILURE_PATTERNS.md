# Failure Patterns — Detected Issues & How to Avoid Them

> Documented from analysis of 13 Blogger XML themes.

---

## 1. XML / STRUCTURAL ISSUES

### 1.1 Invalid XML in Skin Comments

**Problem:** Malformed `/* */` comments inside `<b:skin><![CDATA[]]>` can break the skin parser. Both JavaScript-style `//` comments and CSS `/* */` blocks work, but nested comments or unclosed blocks crash.

**Detection:** Theme loads but no CSS is applied. Layout view shows unstyled page.

**Avoid:**
- Never nest `/*` inside `/*` — use `//` for single-line comments
- Ensure all `/*` have matching `*/` in skin
- Wrap all JS in `//<![CDATA[ ... //]]>` NOT inside skin

### 1.2 Mismatched XML Tags

**Problem:** Unclosed `<b:if>`, `<b:loop>`, `<b:section>`, or `<b:widget>` tags cause template to fail silently.

**Detection:** Layout editor shows "Template Error" or sections don't render.

**Avoid:**
- Always close `<b:if>` with `</b:if>`
- Always close `<b:loop>` with `</b:loop>`
- Use proper self-closing syntax: `<b:else/>` not `<b:else>`
- Indent consistently to spot mismatches

### 1.3 Missing Namespace Declaration

**Problem:** Missing `xmlns:b`, `xmlns:data`, or `xmlns:expr` on `<html>`.

**Detection:** Browser shows raw XML or Blogger says "Template is invalid".

**Avoid:** Always include all 4 namespace declarations on `<html>`:
```xml
<html xmlns='http://www.w3.org/1999/xhtml'
      xmlns:b='http://www.google.com/2005/gml/b'
      xmlns:data='http://www.google.com/2005/gml/data'
      xmlns:expr='http://www.google.com/2005/gml/expr'>
```

---

## 2. WIDGET ISSUES

### 2.1 Missing `main` Includable

**Problem:** Adding a `<b:widget>` without a `<b:includable id='main'>` override renders nothing — the widget is invisible.

**Detection:** Widget shows in Layout editor but nothing appears on page.

**Avoid:** Always include `main` includable:
```xml
<b:includable id='main' var='this'>
  <!-- widget content -->
</b:includable>
```

### 2.2 ContactForm Broken on Single Post Pages

**Problem:** ContactForm widget stops working on item pages because Blogger removes the form elements from DOM on single post pages.

**Detection:** Contact form works on homepage but not on post pages.

**Fix — The Hidden Widget Pattern:**
```xml
<b:if cond='data:view.isSingleItem'>
  <div id='hidden-widget-container' style='display:none'>
    <b:section class='hidden-widgets' deleted='true' id='hidden-widgets' maxwidgets='2' showaddelement='no'>
      <b:widget id='ContactForm1' locked='true' ...>
        <!-- ContactForm widget markup -->
      </b:widget>
    </b:section>
  </div>
</b:if>
```

### 2.3 Duplicate Widget IDs

**Problem:** Using the same widget ID twice causes JS conflicts (especially with ContactForm).

**Detection:** One of the widgets doesn't render or JS errors in console.

**Avoid:** Each widget must have a unique `id` (e.g., `ContactForm1`, `PopularPosts2`, `Label3`).

### 2.4 ContactForm Form Field ID Collisions

**Problem:** Multiple ContactForm widgets on same page get duplicate form field IDs.

**Detection:** Submit button doesn't work or wrong values submitted.

**Fix:** Always prefix form element IDs with `data:widget.instanceId`:
```xml
<input expr:id='data:widget.instanceId + &quot;_contact-form-name&quot;' .../>
```

---

## 3. COMMENT SYSTEM ISSUES

### 3.1 Missing Comment Iframe

**Problem:** Removing or modifying the comment iframe breaks the native comment system.

**Detection:** Clicking "Post a Comment" does nothing or opens blank page.

**Avoid:** Preserve this exact pattern:
```xml
<iframe allowtransparency='allowtransparency'
        class='blogger-iframe-colorize blogger-comment-from-post'
        frameborder='0' id='comment-editor' name='comment-editor'
        src='' style='min-height:110px;' width='100%'/>
<data:post.cmtfpIframe/>
<script type='text/javascript'>BLOG_CMT_createIframe('<data:post.appRpcRelayPath/>');</script>
```

### 3.2 Disabling Threaded Comments

**Problem:** Overriding `threadedCommentJs` or `threadedCommentForm` without proper fallback breaks replies.

**Detection:** Comments load but reply button doesn't work.

**Avoid:** If overriding, call Blogger's built-in thread init:
```xml
<b:template-script inline='true' name='threaded_comments'/>
<script>blogger.widgets.blog.initThreadedComments(...);</script>
```

### 3.3 Comments Not Showing

**Problem:** Comment count shows but comments don't render.

**Detection:** "No comments" appears but comments exist.

**Fix:** Ensure `data:post.commentHtml` is rendered inside `#comment-holder`:
```xml
<div id='comment-holder'><data:post.commentHtml/></div>
```

---

## 4. SEO MISTAKES

### 4.1 Using `data:blog.pageType` Instead of `data:view.*`

**Problem:** Old `data:blog.pageType` conditional checks are unreliabl across all views.

**Detection:** Wrong title or meta tags on certain pages.

**Fix:** Use modern `data:view.*` API:
```
BAD:  <b:if cond='data:blog.pageType == "item"'>
GOOD: <b:if cond='data:view.isSingleItem'>
```

### 4.2 No Canonical URL

**Problem:** Missing `<link rel='canonical'>` tag lets search engines pick wrong URL for paginated/parameterized pages.

**Detection:** Duplicate content issues in Google Search Console.

**Fix:**
```xml
<link expr:href='data:view.url.canonical' rel='canonical'/>
```

### 4.3 Using `data:blog.url` Instead of `data:view.url.canonical`

**Problem:** `data:blog.url` doesn't handle pagination, search params, or mobile URL variants properly.

**Fix:** Use `data:view.url.canonical` for canonical links and `data:blog.url.canonical` for OG URLs.

### 4.4 Hardcoded Placeholder Values

**Problem:** Themes like neet.xml use `"YOUR DESCRIPTION HERE"`, `"USER-TWITTER"`, `"CODE-VALIDATION-GOOGLE-WEBMASTER"` as meta content.

**Detection:** Tools like Lighthouse show missing or placeholder meta.

**Avoid:** Use dynamic Blogger data tags or leave blank (Blogger fills defaults):
```xml
<meta expr:content='data:view.description.escaped' name='description'/>
```

### 4.5 Overly Aggressive Noindex

**Problem:** The old X-Mag themes add `noindex,nofollow` on ALL mobile pages.

**Detection:** Mobile pages are not indexed — significant traffic loss.

**Fix:** Never add `noindex` to mobile pages. Mobile-first indexing uses mobile content.
```
BAD:  <b:if cond='data:blog.isMobile'><meta content='noindex,nofollow' name='robots'/></b:if>
GOOD: <meta content='index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1' name='robots'/>
```

### 4.6 Missing Open Graph Tags

**Problem:** No OG tags = bad social sharing previews.

**Detection:** Facebook/Twitter show no image, wrong title, or broken preview.

**Fix:** Include all required OG tags (title, description, image, url, type, site_name).

---

## 5. PERFORMANCE BOTTLENECKS

### 5.1 Render-Blocking Inline JavaScript

**Problem:** Inline `<script>` tags in `<head>` or early `<body>` block HTML parsing.

**Impact:** Slower LCP and FCP.

**Fix:** Move non-critical scripts to end of `<body>`:
```
BAD:  <head><script>...</script></head>
GOOD: </body><script>...</script>
```

### 5.2 No `font-display: swap` on @font-face

**Problem:** Custom fonts block text rendering until loaded.

**Impact:** Invisible text during font load (FOIT), poor LCP.

**Fix:** Always add `font-display: swap` to every `@font-face` block.

### 5.3 Heavy Universal Selector Reset

**Problem:**
```css
a,abbr,acronym,address,applet,b,big,blockquote,body,caption,center,cite,code,dd,del,dfn,div,dl,dt,em,fieldset,font,form,h1,h2,h3,h4,h5,h6,html,i,iframe,img,ins,kbd,label,legend,li,object,p,pre,q,s,samp,small,span,strike,strong,sub,sup,table,tbody,td,tfoot,th,thead,tr,tt,u,ul,var{padding:0;border:0;...}
```

**Impact:** Slow style recalculation, ~65-element selector.

**Fix:**
```css
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
```

### 5.4 No Native Lazy Loading

**Problem:** Using custom JS-based lazyload instead of browser-native `loading='lazy'`.

**Impact:** Custom JS adds complexity, can break, doesn't work in all browsers.

**Fix:** Add `loading='lazy'` to all below-the-fold images while keeping custom lazyload as enhancement.

### 5.5 Massive Inline CSS in `<b:skin>`

**Problem:** 15-25KB of CSS embedded in `<b:skin>` is always render-blocking.

**Impact:** Slower LCP on mobile.

**Fix:** Split critical CSS (above-fold) from deferred CSS. Use `<link rel='preload'>` for key styles.

### 5.6 Dead Code (Unused CSS Variables)

**Problem:** 35+ font variant CSS variables declared but never used in any theme.

**Impact:** Increased CSS file size, wasted bytes.

**Fix:** Remove unused variables. Only declare variables that are actually referenced in CSS rules.

---

## 6. MOBILE LAYOUT ISSUES

### 6.1 `maximum-scale=1` Prevents Zoom

**Problem:** Viewport `maximum-scale=1` prevents users from pinch-zooming.

**Impact:** Accessibility violation (WCAG 1.4.4). Users with visual impairments cannot read content.

**Fix:**
```
BAD:  <meta content='width=device-width, initial-scale=1, maximum-scale=1' name='viewport'/>
GOOD: <meta content='width=device-width, initial-scale=1, minimum-scale=1, maximum-scale=5' name='viewport'/>
```

### 6.2 No Touch Target Sizing

**Problem:** Small links/buttons (< 48px) on mobile are hard to tap.

**Impact:** Poor mobile UX, high accidental tap rate.

**Fix:** Ensure all interactive elements have minimum 48x48px tap targets.

### 6.3 Missing `prefers-reduced-motion`

**Problem:** Animations run even when user prefers reduced motion.

**Impact:** Accessibility issue, can cause discomfort for users with vestibular disorders.

**Fix:**
```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}
```

---

## 7. DESIGN & UX ISSUES

### 7.1 Copy-Paste Disabled

**Problem:** JavaScript disables right-click, text selection, and copy.

**Impact:** Terrible UX. Users cannot copy code, quotes, or content. Breaks browser extensions, password managers.

**Avoid:** NEVER disable copy-paste. It doesn't prevent theft (savvy users view source) but destroys UX.

### 7.2 Dark Mode Toggle Without Implementation

**Problem:** Dark mode toggle UI exists (sun/moon icon) but no actual CSS dark mode variables.

**Impact:** Users toggle "dark mode" and nothing happens — confusing and broken.

**Fix:** Either implement actual dark mode CSS or remove the toggle.

### 7.3 RTL Language Support Issues

**Problem:** Arabic/RTL font overrides declared but not properly tested.

**Impact:** RTL blogs may have broken layouts.

**Fix:** Test themes with `expr:dir='data:blog.languageDirection'` properly applied.

---

## 8. SCHEMA MISTAKES

### 8.1 Missing `@context` in JSON-LD

**Problem:** JSON-LD without `"@context": "http://schema.org"` is not valid.

**Impact:** Schema not recognized by Google.

### 8.2 Incorrect Date Format

**Problem:** Using non-ISO dates in `datePublished` / `dateModified`.

**Impact:** Google may not parse the date correctly.

**Fix:** Use ISO 8601 format: `data:post.date.iso8601`

### 8.3 Missing Publisher in BlogPosting

**Problem:** BlogPosting with author but no publisher/organization.

**Impact:** Google may not show publisher info in search results.

**Fix:** Always include `publisher` with Organization type and logo.

---

## 9. DUPLICATION PATTERNS TO AVOID

### 9.1 Copying Social Brand Colors in Every Theme

**Problem:** The same 30-line social brand color block is duplicated in all 7 Pikitemplates themes.

**Impact:** More maintenance, wasted space, inconsistency risk.

**Approach for new themes:** Use CSS custom properties or a shared stylesheet pattern.

### 9.2 Identical CSS Reset in Every Theme

**Problem:** The same 65-element universal reset is copied everywhere.

**Fix:** Use minimal modern reset once.

---

## 10. COMMON BLOGGER-SPECIFIC BUGS

| Bug | Symptom | Solution |
|-----|---------|----------|
| Missing `b:skin` | No styles applied | Wrap all CSS in `<b:skin><![CDATA[ ... ]]>` |
| Skin variable not parsed | `$(variable)` appears in output | Ensure Variable definition exists in skin comments |
| `expr:` not working | Attribute appears as literal string | Check namespace: `xmlns:expr='http://www.google.com/2005/gml/expr'` |
| `b:include` not found | Blank section | Check `name` matches an existing `b:includable id` |
| Blog widget not rendering | No posts show | Ensure `main` includable has proper post loop |
| Layout mode disabled | Can't edit in Layout | Ensure theme doesn't set `data:view.isLayoutMode` condition that hides edit UI |
| Widget settings not applying | Wrong widget behavior | Check widget-settings format is correct |
| Hidden widgets showing | Widgets visible in unexpected places | Use `deleted='true'` on hidden section |
| Script CDATA errors | XML parsing error | Wrap JS in `//<![CDATA[ ... //]]>` |
| AdSense not showing | Blank ad slots | Ensure AdSense code is async and properly placed |
