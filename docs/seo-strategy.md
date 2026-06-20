# SEO / AEO / GEO Strategy — RankrSEO Blogger Theme

## 1. Executive Summary

RankrSEO is a Blogger XML theme designed for an SEO agency targeting English-speaking markets (USA, UK, India, Canada, Australia). The theme must be optimized for traditional search engines (Google, Bing) and AI-powered search (ChatGPT, Gemini, Claude, Perplexity).

## 2. Keyword Strategy

### Primary Service Keywords
- SEO Agency, SEO Company, SEO Consultant
- Technical SEO Services, Local SEO Services, Ecommerce SEO Services
- Enterprise SEO Services, Blogger SEO Services, WordPress SEO Services
- SEO Audit Services, Digital Marketing Agency
- Content Marketing Services, YouTube SEO Services, AI SEO Services

### GEO Target Keywords
- India: SEO Agency India, SEO Consultant Delhi/Mumbai/Bangalore/Hyderabad
- UK: SEO Agency UK, SEO Consultant London, SEO Services Manchester
- USA: SEO Agency USA, SEO Consultant New York/Los Angeles/Chicago
- Canada: SEO Agency Canada, SEO Consultant Toronto
- Australia: SEO Agency Australia, SEO Consultant Sydney

### Long Tail Keywords
- affordable SEO services, SEO consultant near me
- best SEO agency in [city], digital marketing agency for startups
- SEO for local businesses, technical SEO consultant, AI SEO consultant

## 3. On-Page SEO Implementation

### Title Tags
- Homepage: "RankrSEO - SEO Agency & Digital Marketing Services for USA, UK & India"
- Posts: "{Post Title} | RankrSEO SEO Agency"
- Pages: "{Page Title} | RankrSEO"
- Label pages: "{Label} | RankrSEO"
- Search: "Search: {query} | RankrSEO"

### Meta Descriptions
- Homepage: "RankrSEO is a results-driven SEO agency and digital marketing company offering technical SEO, local SEO, ecommerce SEO, and AI search optimization services for businesses in USA, UK, and India. Get a free SEO audit."
- Posts: Auto-generated from post snippets

### Canonical URLs
- `data:view.url.canonical` used throughout
- Proper pagination handling

### Hreflang Tags
- x-default, en, en-US, en-GB, en-CA, en-AU

### Robots Meta
- index, follow on all pages except search (noindex, follow)

## 4. Structured Data (JSON-LD)

### Schema Types Implemented
1. **WebSite** - Homepage only, includes SearchAction
2. **Organization + LocalBusiness** - Combined schema with address, contact, social profiles
3. **Service + OfferCatalog** - Service listing with 5 service offerings
4. **FAQPage** - 5 questions/answers on homepage
5. **BreadcrumbList** - On single post pages
6. **BlogPosting** - On each post with full metadata (headline, image, date, author, publisher)

### Schema Improvements Needed
- Add Person schema for author pages
- Add VideoObject schema for YouTube content
- Add Speakable schema for AEO optimization
- Add ItemList schema for index pages

## 5. Open Graph & Social

### OG Tags
- og:title, og:description, og:url, og:image, og:type, og:site_name, og:locale
- Type: website (homepage), article (posts), object (index)

### Twitter Cards
- summary_large_image card
- twitter:title, twitter:description, twitter:image, twitter:domain

### Social Profiles
- Facebook: https://www.facebook.com/RankrSEOs/
- LinkedIn: https://in.linkedin.com/in/rankrseo
- Instagram: https://www.instagram.com/rankrseo/
- YouTube: https://www.youtube.com/@rankrseo

## 6. AEO (Answer Engine Optimization)

### Optimizing for AI Search
- FAQ schema provides direct answers for featured snippets and AI responses
- Clear, concise answers structured as Q&A pairs
- Semantic entity markup (knowsAbout, areaServed)

### Content Recommendations
- Create "People Also Ask" optimized sections
- Use conversational language in introductions
- Include data, statistics, and citations
- Structure content with clear H2/H3 hierarchies

## 7. Content Clusters

### Cluster 1: Technical SEO
- Parent page: /p/technical-seo-services.html
- Child articles: Core Web Vitals, Site Architecture, Schema Markup, Crawl Budget, Page Speed

### Cluster 2: Local SEO
- Parent page: /p/local-seo-services.html
- Child articles: Google Business Profile, Local Citations, Review Management, Near Me SEO

### Cluster 3: AI SEO
- Parent page: /p/ai-seo-services.html  
- Child articles: Generative Engine Optimization, ChatGPT SEO, Entity SEO, Semantic Search

### Cluster 4: Ecommerce SEO
- Parent page: /p/ecommerce-seo-services.html
- Child articles: Product Page Optimization, Category Structure, Ecommerce Schema

### Cluster 5: Blogger SEO
- Parent page: /p/blogger-seo-services.html
- Child articles: Blogger Custom Domain, Blogger SEO Settings, Blogger Theme Optimization

### Cluster 6: Content Marketing
- Parent page: /p/content-marketing-services.html
- Child articles: SEO Writing, Content Strategy, Linkable Assets, Guest Posting

## 8. Internal Linking Structure

- Navigation: Home > Services (dropdown) > Blog > Case Studies > About > Contact
- Footer: Quick Links (Home, Blog, Case Studies, About, Services, Portfolio) + Services list + Resources
- Content: Posts link to service pages and related articles

## 9. Performance Budget

### Core Web Vitals Targets
- LCP: < 2.5s
- FID: < 100ms
- CLS: < 0.1

### Optimization Techniques
- Deferred font loading (preload + noscript fallback)
- Deferred Font Awesome (media='print' onload trick)
- Native lazy loading (loading='lazy' on images)
- DNS prefetch for 3rd party domains
- Vanilla JS (no jQuery)
- CSS custom properties for efficient style computation
- Reduced filter blur (60px max) for mobile GPU performance

## 10. GEO (Generative Engine Optimization)

### What is GEO
Generative Engine Optimization optimizes content for AI search engines like ChatGPT, Gemini, Claude, and Perplexity. It goes beyond traditional SEO by structuring content for LLM consumption.

### GEO Techniques Applied
- FAQPage schema for direct answers
- Clear heading hierarchy (H1 > H2 > H3)
- Entity-rich content (schema.org markup for people, places, organizations)
- Citation-friendly claims and statistics
- Structured data that LLMs can parse

### GEO Improvements
- Add "key definitions" sections to posts
- Include executive summaries in blog posts
- Use bullet points and tables for structured information
- Add "quick answers" before detailed explanations

## 11. Monitoring & Measurement

### KPIs
- Organic traffic growth (monthly)
- Keyword rankings (top 3, top 10, top 100)
- Featured snippets acquired
- AI search mentions (ChatGPT citations, Perplexity references)
- Core Web Vitals scores
- Conversion rate from organic traffic

### Tools
- Google Search Console
- Google Analytics 4
- Google PageSpeed Insights
- Ahrefs / SEMrush (for competitive analysis)
- Manual ChatGPT/Perplexity queries for brand mention tracking

## 12. Service Pages Roadmap

The following static pages should be created in Blogger:
1. /p/seo-services.html - SEO Services overview
2. /p/technical-seo-services.html - Technical SEO
3. /p/local-seo-services.html - Local SEO  
4. /p/ecommerce-seo-services.html - Ecommerce SEO
5. /p/ai-seo-services.html - AI SEO / GEO
6. /p/content-marketing-services.html - Content Marketing
7. /p/seo-audit-services.html - SEO Audit
8. /p/about.html - About Us
9. /p/contact.html - Contact
10. /p/privacy-policy.html - Privacy Policy
11. /p/terms.html - Terms of Service

## 13. Current Implementation Status

| Feature | Status | Location |
|---------|--------|----------|
| Title tags | Done | `<title>` in `<head>` |
| Meta descriptions | Done | `<meta name='description'>` |
| Canonical URLs | Done | `<link rel='canonical'>` |
| Hreflang | Done | `<link rel='alternate' hreflang='...'>` |
| Robots | Done | `<meta name='robots'>` |
| OG tags | Done | `<meta property='og:*'>` |
| Twitter cards | Done | `<meta name='twitter:*'>` |
| WebSite schema | Done | JSON-LD in `<head>` |
| Org+LocalBusiness schema | Done | JSON-LD in `<head>` |
| Service schema | Done | JSON-LD in `<head>` |
| FAQPage schema | Done | JSON-LD in `<head>` (homepage) |
| BreadcrumbList schema | Done | JSON-LD in `<head>` + per-post |
| BlogPosting schema | Done | JSON-LD in Blog1 widget |
| Breadcrumb nav | Done | Visual + JSON-LD |
| DNS prefetch | Done | `<link rel='dns-prefetch'>` |
| Dark mode | Done | CSS custom properties + JS |
| AdSense | Done | Conditional in `<head>` |
| Analytics | Done | Gtag.js in `<head>` |
| Speakable schema | Missing | Future addition |
| Person schema | Missing | Future addition |
| VideoObject schema | Missing | Future addition |
| Content clusters | Missing | Blogger pages needed |
