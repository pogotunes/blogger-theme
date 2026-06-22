# SEO Audit — RankrSEO Theme & Content

> Generated: 2026-06-22
> Auditor: AI SEO Specialist

---

## 1. TECHNICAL SEO

### 1.1 Crawlability
| Issue | Status | Details |
|-------|--------|---------|
| robots.txt | ✅ | Blogger default (allows all) |
| Sitemap.xml | ✅ | Blogger auto-generates |
| Noindex on label pages | ✅ | `/search/label/` pages are `noindex,follow` |
| Viewport zoom disabled | ❌ | `maximum-scale=1` — blocks pinch-zoom, WCAG failure |
| 404 page | ✅ | Custom 404 with navigation |
| Pagination | ✅ | `data:view.url.canonical` handles pagination |

### 1.2 Indexability
| Issue | Status | Details |
|-------|--------|---------|
| Canonical tags | ✅ | Single canonical using `data:view.url.canonical` |
| Meta robots | ✅ | `index,follow,max-snippet:-1,max-image-preview:large,max-video-preview:-1` |
| Duplicate content risk | ⚠️ | 22 geo pages have similar content — need differentiation |
| Orphan pages | ⚠️ | Blog posts not linked from any service page |

### 1.3 Core Web Vitals Readiness
| Issue | Status | Details |
|-------|--------|---------|
| Font Awesome deferred | ✅ | `media="print"` → `media="all"` swap |
| Google Fonts preloaded | ✅ | Inter & Poppins preloaded |
| Vanilla JS (no jQuery) | ✅ | Lightweight, no framework bloat |
| CSS inline in templates | ⚠️ | Blog templates have inline `<style>` — increases page size |

### 1.4 Mobile
| Issue | Status | Details |
|-------|--------|---------|
| Responsive design | ✅ | Full mobile-first responsive |
| Mobile nav | ✅ | Off-canvas slide-in menu |
| Touch targets | ✅ | Adequate sizing |
| Viewport zoom blocked | ❌ | `maximum-scale=1` — MUST FIX for accessibility |

---

## 2. SCHEMA AUDIT

### 2.1 Existing Schema

| Schema | Status | Issues |
|--------|--------|--------|
| WebSite + SearchAction | ✅ | On homepage only |
| Organization + LocalBusiness | ✅ | Combined — missing `image` property |
| Service + OfferCatalog | ✅ | Services listed, missing `provider` |
| FAQPage | ⚠️ | Homepage only — NOT on service pages |
| BreadcrumbList (head) | ⚠️ | Only 2 items (Home > Page) — missing label |
| BreadcrumbList (post) | ✅ | 3 items (Home > Label > Post) |
| BlogPosting | ✅ | Full schema on posts |
| Article (microdata) | ✅ | On `<article>` element |

### 2.2 Missing Schema (Critical)

| Schema | Priority | Where Needed |
|--------|----------|-------------|
| FAQPage | 🔴 P0 | Every service page (Technical SEO, Local SEO, etc.) |
| Review | 🔴 P0 | Homepage testimonials section |
| Speakable | 🔴 P0 | Blog posts — for AEO / voice search |
| BreadcrumbList | 🔴 P0 | Static pages (About, Services, Contact) |
| HowTo | 🟡 P1 | Blog posts with step-by-step instructions |
| VideoObject | 🟡 P1 | YouTube tutorial pages |
| ItemList | 🟡 P1 | Category/index pages |
| Product | 🟢 P2 | Service-specific pricing pages |
| Course | 🟢 P2 | SEO guide/resource pages |
| Person | 🟢 P2 | Author/about page |

---

## 3. ON-PAGE SEO

### 3.1 Heading Hierarchy
| Issue | Status | Details |
|-------|--------|--------|
| Single H1 per page | ✅ | All templates |
| H2 for main sections | ✅ | Consistent |
| Heading skip | ⚠️ | Some templates jump H1→H3 without H2 |
| Missing H2 in content | ⚠️ | Templates with only FAQ section lack structural H2s |

### 3.2 Meta Tags
| Issue | Status | Details |
|-------|--------|--------|
| Unique meta descriptions | ✅ | Just fixed (92 unique) |
| Meta keywords | ⚠️ | Present but Google ignores — safe to keep |
| Title tags | ⚠️ | Blogger auto-generates from post title — OK |
| OG tags | ✅ | Full implementation |
| Twitter cards | ✅ | `summary_large_image` |

### 3.3 Internal Linking
| Issue | Status | Details |
|-------|--------|--------|
| Nav links to services | ✅ | All 10 services linked from nav |
| Footer links to services | ✅ | Full service list in footer |
| Blog → Service links | ⚠️ | Inconsistent — some templates link back, others don't |
| Geo pages → Service links | ⚠️ | Not all geo pages link to related service pages |
| Service pages → Blog links | ❌ | Missing — service pages don't link to relevant blog posts |
| Case studies → Service links | ⚠️ | Case studies page doesn't link to relevant services |

---

## 4. AEO / GEO READINESS

### 4.1 Answer Engine Optimization
| Issue | Status | Details |
|-------|--------|--------|
| FAQ sections | ⚠️ | Only on homepage — needed on ALL service pages |
| Clear definitions | ⚠️ | Service descriptions lack concise "what is X" definitions |
| Structured lists | ✅ | Service features in `<ul>` lists |
| Tables | ❌ | No comparison tables — needed for pricing/feature comparisons |
| Speakable schema | ❌ | Missing — critical for voice/AI citations |

### 4.2 Entity Optimization
| Issue | Status | Details |
|-------|--------|--------|
| Brand entity | ✅ | Organization schema present |
| Service entities | ✅ | Service schema with 6 items |
| Location entities | ⚠️ | Weak — geo pages need better location entity signals |
| Semantic keyword coverage | ⚠️ | Needs improvement for topical authority |

---

## 5. CRITICAL BUGS (Must Fix Now)

| Bug-ID | Severity | Issue | File(s) | Fix |
|--------|----------|-------|---------|-----|
| SEO-001 | 🔴 Critical | Viewport `maximum-scale=1` blocks zoom | rankrseo-theme.xml:8 | Change to `maximum-scale=5` or remove |
| SEO-002 | 🔴 Critical | No FAQ schema on service pages | rankrseo-theme.xml | Add FAQPage JSON-LD for each service |
| SEO-003 | 🔴 Critical | No Review schema for testimonials | rankrseo-theme.xml | Add AggregateRating + Review schema |
| SEO-004 | 🔴 Critical | BreadcrumbList not on static pages | rankrseo-theme.xml | Add breadcrumb schema for all page types |
| SEO-005 | 🔴 Critical | No Speakable schema | rankrseo-theme.xml | Add Speakable for AEO optimization |
| SEO-006 | 🟡 High | Duplicate BreadcrumbList on posts | rankrseo-theme.xml | Consolidate to single schema per page |

---

## 6. RECOMMENDATION SUMMARY

### Priority 0: Immediate (This Session)
1. Fix `maximum-scale=1` → `maximum-scale=5` (SEO-001)
2. Add FAQPage schema to all service page templates (SEO-002)
3. Add Review/AggregateRating schema for testimonials (SEO-003)
4. Add BreadcrumbList schema for static pages (SEO-004)
5. Add Speakable schema for AEO (SEO-005)

### Priority 1: Next 48 Hours
6. Consolidate duplicate BreadcrumbList (SEO-006)
7. Add FAQ sections/content to all service page templates
8. Add comparison tables for pricing/service tiers
9. Improve service page → blog post internal linking
10. Add structured definition blocks to all service pages

### Priority 2: This Week
11. Add HowTo schema to guide/tutorial blog posts
12. Add VideoObject schema for video content
13. Improve geo page differentiation
14. Add Person schema for author page

### Priority 3: Ongoing
15. Build topical authority clusters
16. Expand entity coverage
17. Add multilingual hreflang if expanding languages
18. Monitor Core Web Vitals
