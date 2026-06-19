# Repository Map — Single-page-projects

> Complete file inventory, architecture overview, and dependency map.
> Generated: 2026-06-19 | Total: 76 files (excluding .git) | ~4.9 MB

## Directory Tree

```
/workspaces/Single-page-projects/
│
├── knowledge-base/                          # Knowledge documentation system
│   ├── docs/                                # Core documentation
│   │   ├── REPOSITORY_MAP.md                # This file
│   │   ├── BLOGGER_XML_ARCHITECTURE.md      # Blogger XML architecture reference
│   │   ├── THEME_ANALYSIS_REPORT.md         # Per-theme analysis with scores
│   │   └── COMPONENT_LIBRARY.md             # Reusable component catalog
│   ├── blueprints/
│   │   └── SEO_AEO_GEO_BLUEPRINT.md         # SEO/AEO/GEO optimization standards
│   ├── snippets/
│   │   └── SNIPPET_LIBRARY.xml              # 27 reusable XML includable snippets
│   ├── error-memory/                        # Permanent error tracking system
│   │   ├── MASTER_ERROR_MEMORY.json         # Structured error database
│   │   ├── ERROR_HISTORY.md                 # Chronological error log
│   │   ├── ROOT_CAUSE_ANALYSIS.md           # Root cause for every error
│   │   ├── PREVENTION_RULES.md              # Engineering prevention rules
│   │   ├── HIGH_RISK_PATTERNS.md            # High-risk pattern registry
│   │   ├── KNOWN_FATAL_ERRORS.md            # Fatal error reference
│   │   └── VALIDATION_CHECKLIST.md          # Pre-generation validation
│   ├── RANKRSEO_THEME_SPEC.md               # Master theme specification
│   ├── FAILURE_PATTERNS.md                  # Detected failure patterns
│   ├── BLOGGER_WIDGET_REFERENCE.md          # Widget data binding reference
│   └── rankrseo-theme.xml                   # WIP RankrSEO master theme
│
├── Root XML Themes (6 files)
│   ├── amitkr26.xml                         # [EXPERIMENTAL] Portfolio/Blog — RankrSEO
│   ├── handjee.xml                          # Education — Soratemplates X-Mag base
│   ├── helthifi.xml                         # [PRODUCTION] Health — RankrSEO branded
│   ├── neet.xml                             # NEET Education — Soratemplates X-Mag
│   ├── neetjee.xml                          # NEET/JEE Education — Soratemplates
│   └── smartpadhailikhai.xml                # Education — Soratemplates
│
├── Pikitemplates Free Versions (7 directories)
│   ├── Citron_Free_Version/                 # News/Magazine — 3,508 lines
│   ├── GridMag_Free_Version/               # Grid Magazine — 3,221 lines
│   ├── Monster_Free_Version/                # News/Magazine — 3,621 lines
│   ├── Quick_Spot_Free_Version/            # Quick News — 3,409 lines
│   ├── SEO_Spot_Free_Version/              # SEO/Marketing — 3,703 lines
│   ├── Shopping_Free_Version/              # eCommerce — 3,546 lines
│   └── Wind_Spot_Free_Version/             # News/Magazine — 3,638 lines
│
└── .git/                                    # Git (13 commits, 1 branch)
```

## Theme Classification

### By Source

| Source | Count | Themes |
|--------|-------|--------|
| **Pikitemplates.com** | 7 | Citron, GridMag, Monster, Quick_Spot, SEO_Spot, Shopping, Wind_Spot |
| **Soratemplates.com** | 4 | neet, handjee, neetjee, smartpadhailikhai |
| **RankrSEO Custom** | 2 | amitkr26 (experimental), helthifi (production) |

### By Generation

| Generation | Version Markers | Themes | Lines Range | JS Dependency |
|------------|----------------|--------|-------------|---------------|
| **Old (Soratemplates)** | Blogger v1, b:version='2' | neet, handjee, neetjee, smartpadhailikhai | 2,505-4,679 | jQuery |
| **Modern (Pikitemplates)** | b:templateVersion='2.0.0' | All 7 Free Version themes | 3,221-3,703 | jQuery + Pikitemplates CDN |
| **Hybrid (RankrSEO)** | Modern head + custom CSS | helthifi, amitkr26 | 1,057-4,031 | jQuery or vanilla |

### By Complexity (Widget Count)

| Complexity | Widget Count | Themes |
|------------|-------------|--------|
| High | 25-31 | Shopping, SEO_Spot, Citron, Monster, Wind_Spot |
| Medium | 16-24 | GridMag, Quick_Spot |
| Variable | Custom | amitkr26, helthifi, neet, handjee, neetjee, smartpadhailikhai |

## File Size Summary

| Category | Count | Total Size |
|----------|-------|------------|
| Blogger XML Themes (production) | 12 | ~3.6 MB |
| Blogger XML Themes (experimental/WIP) | 2 | ~137 KB |
| Documentation (Markdown) | 15 | ~163 KB |
| XML Snippet Library | 1 | ~30 KB |
| PNG Images | 32 | ~269 KB |
| JPG Previews | 6 | ~417 KB |
| URL Shortcuts | 9 | ~1.2 KB |
| **Total (excl. .git)** | **76** | **~4.9 MB** |

## External Dependencies

| Dependency | Type | Used By |
|------------|------|---------|
| jQuery 3.5.1+ | CDN (cdnjs.cloudflare.com) | helthifi, all Pikitemplates |
| Font Awesome 5.15 / 6 | CDN | helthifi, all Pikitemplates |
| Material Icons Round | CDN | All Pikitemplates |
| Bootstrap Icons | CDN | GridMag |
| Google Fonts (Inter, Raleway, Signika, Poppins) | fonts.googleapis.com | Various |
| Google AdSense | pagead2.googlesyndication.com | handjee, helthifi, neet, neetjee |
| Pikitemplates Scripts | CDN | All Pikitemplates themes |

## Duplicate/Redundant Files Detected

| File | Issue |
|------|-------|
| GridMag/Assets/gridmag_v1_copy.png | _copy suffix — likely duplicate |
| Monster/Assets/monster_dark_copy.png | _copy suffix — likely duplicate |
| GridMag/Assets/vc_6_min_(1).png | _(1) auto-rename duplicate |
| Monster/Assets/monster_png_(1).png | _(1) auto-rename duplicate |
| Shopping/Assets/shopping_template_v1_min.png vs v2_min.png | Nearly identical (2,182 vs 2,183 bytes) |

## Deleted Files (Git History)

| File | Commit | Reason |
|------|--------|--------|
| MOSFET-Complete-Learning-Module.html | 3530977 | Old content, unrelated to themes |
| nosfet2.html | d52da24 | Old HTML content |
| portfolio1.html | 27736f8 | Old portfolio page |
| mosfet.html | 0697899 | Old HTML content |
