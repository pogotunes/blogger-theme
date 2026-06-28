# Error Log — RankrSEO Project

> Generated: 2026-06-22
> Persistent memory for all fixed bugs

---

## Active Bugs

| Bug-ID | Severity | Status | Root Cause | Files | Fix |
|--------|----------|--------|------------|-------|-----|
| SEO-001 | 🔴 Critical | Fixed | Viewport was `maximum-scale=1` blocking pinch-zoom | rankrseo-theme.xml:6 | Changed to `maximum-scale=5` |

---

## Fixed Bugs

### BUG-001: Broken contact links
- **Severity:** 🔴 Critical
- **Root Cause:** 6 blog templates used `/p/contact` instead of `/p/contact-us.html`
- **Files:** how-to-choose-seo-agency.html, enterprise-seo.html, digital-marketing.html, seo-agency-vs-freelancer.html, seo-agency.html, questions-to-ask-seo-agency.html
- **Fix:** Replaced `/p/contact` → `/p/contact-us.html`
- **Prevention:** Add URL validation to all templates

### BUG-002: Missing Font Awesome icons on CTAs
- **Severity:** 🟡 Medium
- **Root Cause:** 8 CTA buttons missing `<i class='fas fa-search'>` icon
- **Files:** 6 blog templates + free-seo-audit.html + contact.html
- **Fix:** Added FA icon to all CTAs

### BUG-003: Missing hover animations on buttons
- **Severity:** 🟢 Low
- **Root Cause:** Blog templates had flat `background: var(--primary-dark)` hover only
- **Files:** 85 blog templates
- **Fix:** Added `transform: translateY(-2px)`, `box-shadow: var(--glow-primary)`, `transition: all 0.3s ease`

### BUG-004: Missing SVG featured image on contact page
- **Severity:** 🟢 Low
- **Root Cause:** contact.html had no SVG hero image
- **Files:** contact.html
- **Fix:** Added gradient SVG with "Get in Touch" text

### BUG-005: Duplicate "Our Projects" badges
- **Severity:** 🟡 Medium
- **Root Cause:** script left old badges in place when adding new ones
- **Files:** 93 blog + page templates
- **Fix:** Removed old duplicate divs, kept only new Portfolio CTA

### BUG-006: Generic meta descriptions (92 files)
- **Severity:** 🟡 Medium
- **Root Cause:** All templates shared the same generic description
- **Files:** 92 templates
- **Fix:** Generated unique descriptions based on title/keywords

---

## Prevention Rules

### Rule 1: Template Consistency
When updating a template, verify the same update is needed across ALL templates in the same category.

### Rule 2: URL Validation
All internal `/p/` URLs must end with `.html`. Run `grep -rn "href='/p/[^']*[^.]'"` to find broken links.

### Rule 3: CSS Inheritance
Blogger page content `<style>` blocks override theme CSS. When possible, prefer theme-level CSS over inline `<style>`.

### Rule 4: Meta Uniqueness
Every page must have a unique meta description. Never reuse generic descriptions across multiple pages.

### Rule 5: Schema Consistency
When adding schema to one page type, add it to ALL pages of the same type.

---

## Monitoring Checklist (Pre-Commit)

- [ ] No broken `/p/` links (check with regex)
- [ ] No duplicate meta descriptions
- [ ] All CTA buttons have FA icons
- [ ] All SVG images present on page templates
- [ ] All buttons have hover animations
- [ ] No orphan pages
- [ ] Internal links follow the strategy map
- [ ] Schema validates (Google Rich Results Test)
