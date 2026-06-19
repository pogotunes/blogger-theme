# Repository Map — Single-page-projects

## Directory Structure

```
/workspaces/Single-page-projects/
│
├── knowledge-base/                          # [NEW] Knowledge documentation
│   ├── REPOSITORY_MAP.md                    # This file
│   ├── BLOGGER_XML_ARCHITECTURE.md          # Blogger XML architecture reference
│   ├── THEME_ANALYSIS_REPORT.md             # Per-theme analysis
│   ├── COMPONENT_LIBRARY.md                 # Reusable component library
│   ├── SEO_AEO_GEO_BLUEPRINT.md             # Optimization blueprint
│   ├── BLOGGER_WIDGET_REFERENCE.md          # Widget reference
│   ├── SNIPPET_LIBRARY.xml                  # XML snippet library
│   ├── FAILURE_PATTERNS.md                  # Detected mistakes & fixes
│   └── RANKRSEO_THEME_SPEC.md               # Master theme specification
│
├── Root XML Themes (6 files)
│   ├── amitkr26.xml                         # Portfolio/Blog — RankrSEO custom
│   ├── handjee.xml                          # Education/Blog — Soratemplates X-Mag base
│   ├── helthifi.xml                         # Health Niche — RankrSEO branded
│   ├── neet.xml                             # NEET Education — Soratemplates X-Mag base
│   ├── neetjee.xml                          # NEET/JEE Education — Soratemplates X-Mag base
│   └── smartpadhailikhai.xml                # Education — Soratemplates base
│
├── Free Version Themes (7 directories from Pikitemplates.com)
│   ├── Citron_Free_Version/
│   │   ├── Citron_Free_Version.xml          # News/Magazine — 3,508 lines
│   │   ├── Assets/                          # 4 images (logo, favicon, preview)
│   │   └── Docs/Citron_Doc.url              # URL shortcut
│   │
│   ├── GridMag_Free_Version/
│   │   ├── GridMag_Free_Version.xml         # Grid Magazine — 3,221 lines
│   │   ├── Assets/                          # 16 images (icons, logo, favicon, preview)
│   │   └── Docs/                            # 3 URL shortcuts
│   │
│   ├── Monster_Free_Version/
│   │   ├── Monster_Free_Version.xml         # News/Magazine — 3,621 lines
│   │   ├── Assets/                          # 4 images
│   │   └── Docs/Monster_Doc.url             # URL shortcut
│   │
│   ├── Quick_Spot_Free_Version/
│   │   ├── Quick_Spot_Free_Version.xml      # Quick News — 3,409 lines
│   │   ├── Assets/                          # 4 images
│   │   └── Docs/Quick_Spot_Doc.url          # URL shortcut
│   │
│   ├── SEO_Spot_Free_Version/
│   │   ├── SEO_Spot_Free_Version.xml        # SEO/Marketing — 3,703 lines
│   │   ├── Assets/                          # 3 images
│   │   └── Docs/SEO_Spot_Doc.url            # URL shortcut
│   │
│   ├── Shopping_Free_Version/
│   │   ├── Shopping_Free_Version.xml        # eCommerce/Blog — 3,546 lines
│   │   ├── Assets/                          # 4 images
│   │   └── Docs/Shopping_Doc.url            # URL shortcut
│   │
│   └── Wind_Spot_Free_Version/
│       ├── Wind_Spot_Free_Version.xml       # News/Magazine — 3,638 lines
│       ├── Assets/                          # 4 images
│       └── Docs/WindSpot_Doc.url            # URL shortcut
│
└── .git/                                    # Git repository (13 commits)
```

## Theme Classification

### By Source

| Source | Count | Files |
|--------|-------|-------|
| **Pikitemplates.com** | 7 | Citron, GridMag, Monster, Quick_Spot, SEO_Spot, Shopping, Wind_Spot |
| **Soratemplates.com** | 4 | neet.xml, handjee.xml, neetjee.xml, smartpadhailikhai.xml |
| **RankrSEO Custom** | 2 | amitkr26.xml, helthifi.xml |

### By Niche

| Niche | Themes |
|-------|--------|
| News/Magazine | Citron, Monster, Wind_Spot |
| Grid/Magazine | GridMag |
| Marketing/SEO | SEO_Spot |
| eCommerce | Shopping |
| Quick News | Quick_Spot |
| Education | neet, neetjee, smartpadhailikhai, handjee |
| Health | helthifi |
| Portfolio/Blog | amitkr26 |

### By Complexity (Widget Count)

| Complexity | Themes | Widget Count |
|------------|--------|-------------|
| High (25-31 widgets) | Shopping, SEO_Spot, Citron, Monster, Wind_Spot | 25-31 |
| Medium (16-24 widgets) | GridMag, Quick_Spot | 16-17 |
| Custom/Unique | amitkr26, helthifi, neet, handjee, neetjee, smartpadhailikhai | Varies |

### By Generation

| Generation | Version | Themes |
|------------|---------|--------|
| Old (Soratemplates) | Blogger v1, b:version='2' | neet, handjee, neetjee, smartpadhailikhai |
| Modern (Pikitemplates) | b:templateVersion='1.3.x' - '2.0.0' | All 7 Free Version themes |
| Hybrid (RankrSEO) | Modern head + custom CSS | helthifi, amitkr26 |

## Shared Assets

| Asset Group | Location | Used By |
|-------------|----------|---------|
| Logo images | Each theme's Assets/ folder | Individual themes |
| Favicons | Each theme's Assets/ folder | Individual themes |
| Template previews | Each theme's Assets/ folder | Individual themes |
| Documentation URLs | Each theme's Docs/ folder | Individual themes |

## Dependencies

| Dependency | Type | Used By |
|------------|------|---------|
| jQuery 3.5.1 | CDN (cdnjs.cloudflare.com) | helthifi, all Pikitemplates |
| Font Awesome 5.15 | CDN (cdnjs.cloudflare.com) | helthifi, all Pikitemplates |
| Font Awesome 6 | CDN | Shopping |
| Material Icons Round | CDN | All Pikitemplates |
| Bootstrap Icons | CDN | GridMag |
| Google Fonts (Raleway) | fonts.googleapis.com | Citron, Monster |
| Google Fonts (Inter) | fonts.googleapis.com | GridMag, Shopping, amitkr26 |
| Google Fonts (Signika) | fonts.googleapis.com | Quick_Spot, SEO_Spot, Wind_Spot, helthifi |
| Google Fonts (Poppins) | fonts.googleapis.com | amitkr26 |
| Google AdSense | pagead2.googlesyndication.com | handjee, helthifi, neet, neetjee |
| Pikitemplates Scripts | CDN | All Pikitemplates themes |

## Version Variants

| Theme | Version | Lines | Last Updated |
|-------|---------|-------|-------------|
| Citron | Free Version | 3,508 | 16/May/2025 |
| GridMag | Free Version | 3,221 | 16/May/2025 |
| Monster | Free Version | 3,621 | 16/May/2025 |
| Quick_Spot | Free Version | 3,409 | 16/May/2025 |
| SEO_Spot | v2.1.0.V | 3,703 | 16/May/2025 |
| Shopping | Free Version | 3,546 | 16/May/2025 |
| Wind_Spot | Free Version | 3,638 | 16/May/2025 |
| amitkr26 | Custom | 1,057 | N/A |
| helthifi | RankrSEO v1.0 | 4,032 | N/A |
| neet | X-Mag Free | 4,569 | N/A |
| handjee | X-Mag Free | 4,679 | N/A |
| neetjee | X-Mag Free | 4,409 | N/A |
| smartpadhailikhai | Modified | 2,506 | N/A |
