# GEO / AEO / AI Search Strategy — RankrSEO

> Generated: 2026-06-22
> Focus: ChatGPT, Gemini, Claude, Perplexity, Google SGE, Voice Search

---

## 1. Core Principles

### For AI Answer Engines
1. **Be the authority** — AI models cite high-authority, entity-rich sources
2. **Answer directly** — First 60 words should answer the core question
3. **Use structured data** — Speakable schema signals which content to voice-read
4. **Cite data** — Statistics and research increase citation probability
5. **Use clear headers** — AI-parses H2/H3 for answer extraction

### The "Featured Answer" Framework
```
Question: [User Query]
Answer: [Direct answer in 30-60 words]
Details: [Supporting points, 2-4 sentences]
Source: [Citation / Authority link]
```

---

## 2. Speakable Schema Implementation

Every blog post and service page should include:

```json
{
  "@context": "https://schema.org",
  "@type": "WebPage",
  "speakable": {
    "@type": "SpeakableSpecification",
    "cssSelector": [
      ".speakable-summary",
      ".speakable-headline"
    ]
  }
}
```

CSS classes to add:
- `.speakable-summary` — Opening summary paragraph (30-60 words answering the core question)
- `.speakable-headline` — H1 title of the page

---

## 3. AEO Content Template

### What AI Reads First
```
[Speakable Headline: H1 - keyword rich, question format if possible]

[Speakable Summary: 40-60 word paragraph answering the core query directly]
Example: "Technical SEO is the practice of optimizing your website's infrastructure 
to help search engines crawl, index, and render your content effectively. 
At RankrSEO, we specialize in technical SEO services including Core Web Vitals 
optimization, schema markup, and site architecture improvements."
```

### Question-Answer Pairs
Every page should include clear Q&A formatting:
```
## What Is [Topic]?
[Direct 30-50 word definition]

## How Does [Topic] Work?
[3-4 sentence explanation]

## Why Is [Topic] Important?
[2-3 sentence value proposition]
```

---

## 4. Entity Optimization

### Entities RankrSEO Should Own

| Entity Type | Value | Where to Signal |
|-------------|-------|-----------------|
| Organization | RankrSEO | Homepage, Organization schema |
| Service | SEO Agency Services | All service pages |
| Person | Founders/Key team | About page |
| Location | New Delhi, India | Contact, LocalBusiness schema |
| ServiceArea | USA, UK, India, Canada, Australia | LocalBusiness schema |
| Offer | SEO Audit, SEO Services | Service schema, Pricing page |
| Review | Client testimonials | Homepage, Testimonials |

### Semantic Keyword Triples
```
RankrSEO → provides → SEO services
RankrSEO → specializes in → technical SEO
RankrSEO → serves → US, UK, India, Canada, Australia
RankrSEO → offers → free SEO audit
Technical SEO → includes → Core Web Vitals
Local SEO → includes → Google Business Profile optimization
```

---

## 5. Voice Search Optimization

### Voice Query Patterns
| Query Type | Example | Page |
|------------|---------|------|
| "Best" queries | "best SEO agency for startups" | startup-seo-services |
| "Near me" queries | "SEO consultant near me" | seo-consultant-services |
| "How to" queries | "how to do an SEO audit" | how-to-perform-seo-audit |
| "What is" queries | "what is technical SEO" | technical-seo-services |
| "Why" queries | "why is SEO important" | what-does-seo-agency-do |

### Voice-Friendly Content Rules
- Use natural language questions as H2s
- Keep answers under 50 words
- Use bullet points for list answers
- Include price/range information
- Include location context

---

## 6. SGE (Search Generative Experience) Optimization

### Google SGE Preferences
- **First-hand experience** — Original data, case studies, client results
- **Cited sources** — Clear references to data points
- **Structured content** — Tables, lists, clear headers
- **Freshness** — 2026 content signals

### SGE Content Patterns
```
SGE-Optimized Section Structure:
1. Direct answer block (30-50 words)
2. Context/background (2-3 sentences)
3. Key data points (2-4 stats with sources)
4. "How to" or step-by-step
5. FAQ (3-5 Q&As)
```

---

## 7. ChatGPT / Claude / Perplexity Optimization

### What LLMs Cite
- Wikipedia-style opening definitions
- Authoritative statistics with sources
- Well-structured FAQ content
- Schema.org structured data
- .gov / .edu / high-DR domains

### LLM Citation Checklist
- [ ] Clear, concise opening definition
- [ ] 2-3 data points with sources
- [ ] FAQ with clear Q&A pairs
- [ ] Well-labeled sections (H2/H3)
- [ ] Schema markup (WebPage, Speakable)
- [ ] External citations linking to authoritative sources

---

## 8. Implementation Plan

| Task | Priority | Pages Affected |
|------|----------|---------------|
| Add Speakable schema to theme | P0 | All blog posts |
| Add .speakable-summary class to all templates | P0 | All blog + service pages |
| Rewrite opening paragraphs as AEO-style answers | P0 | All service page templates |
| Add "What Is X" definition sections | P0 | All service page templates |
| Add FAQPage schema to service pages | P0 | 10+ service page templates |
| Convert key H2s to question format | P1 | All blog templates |
| Add data citations to top blog posts | P1 | Top 20 blog templates |
| Update entity references in schema | P1 | Theme XML |
| Optimize for voice search patterns | P2 | All service + geo pages |
