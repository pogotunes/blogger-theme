# ERROR PATTERNS

## Pattern Categories

### XML Errors
| Error | Count | Risk |
|-------|-------|------|
| Duplicate includable ids | ERR-001 | HIGH |
| Unclosed tags | — | HIGH |
| Invalid nesting | — | HIGH |

### Widget Errors
| Error | Count | Risk |
|-------|-------|------|
| Wrong version setting names | ERR-002, ERR-003 | **HIGH** |
| Missing widget-settings | — | MEDIUM |
| Invalid widget type | — | HIGH |

### Comment Errors
| Error | Count | Risk |
|-------|-------|------|
| Comment iframe attributes modified | — | HIGH |
| Threaded comment JS not included | — | HIGH |
| No comment-holder container for commentHtml | — | HIGH |

### Contact Form Errors
| Error | Count | Risk |
|-------|-------|------|
| Missing hidden duplicate for item pages | — | HIGH |
| Wrong button radius (pill vs squared) | UI-008 | LOW |
| Missing expr:id on error/success containers | — | MEDIUM |

### Schema Errors
| Error | Count | Risk |
|-------|-------|------|
| Missing @context on JSON-LD | — | HIGH |
| Hardcoded values not dynamic data | — | MEDIUM |
| Invalid JSON caused by unescaped post titles | — | MEDIUM |

### Responsive Errors
| Error | Count | Risk |
|-------|-------|------|
| Missing breakpoints (1200px, 768px) | UI-001 | HIGH |
| No tablet layout | UI-001 | HIGH |
| Grid collapse at wrong breakpoints | UI-001 | MEDIUM |

### Spacing Errors
| Error | Count | Risk |
|-------|-------|------|
| No spacing scale | UI-002 | HIGH |
| Inconsistent padding/margins | UI-002 | MEDIUM |

### Typography Errors
| Error | Count | Risk |
|-------|-------|------|
| No type scale | UI-003 | HIGH |
| Missing letter-spacing hierarchy | UI-003 | MEDIUM |
| Inconsistent line-height | UI-003 | LOW |

### Card/Component Errors
| Error | Count | Risk |
|-------|-------|------|
| Unequal card heights | UI-005 | MEDIUM |
| No hover indicators | UI-005 | LOW |
| Weak sidebar anchors | UI-006 | LOW |

### Dark Section Errors
| Error | Count | Risk |
|-------|-------|------|
| No hover states | UI-007 | MEDIUM |
| Flat avatar styling | UI-007 | LOW |

### Contact Form Errors
| Error | Count | Risk |
|-------|-------|------|
| Wrong button radius (pill vs squared) | UI-008 | LOW |

### Footer Errors
| Error | Count | Risk |
|-------|-------|------|
| No heading hierarchy | UI-009 | LOW |
| Missing intermediate breakpoints | UI-009 | LOW |

### Design System Errors
| Error | Count | Risk |
|-------|-------|------|
| No design tokens | UI-010 | **CRITICAL** |
| Hardcoded values everywhere | UI-010 | HIGH |

### SEO Errors
| Error | Count | Risk |
|-------|-------|------|
| No Open Graph tags | — | HIGH |
| No JSON-LD schema | — | HIGH |
| Missing canonical URL | — | HIGH |
| No robots meta rules | — | MEDIUM |

### Performance Errors
| Error | Count | Risk |
|-------|-------|------|
| No lazy loading on images | — | HIGH |
| Render-blocking external JS | — | MEDIUM |
| No image width/height attributes | — | MEDIUM |
| Heavy jQuery dependency | — | LOW |

### JavaScript Errors
| Error | Count | Risk |
|-------|-------|------|
| JS comments inside b:skin CSS | — | HIGH |
| Unclosed JS function brackets | — | CRITICAL |
| Missing variable declarations (implicit globals) | — | MEDIUM |
| DOM accessed before element exists | — | MEDIUM |

---

## Risk Assessment

### HIGH RISK: Widget Settings Version Mismatch
- Pattern: Using version='1' setting names in version='2' widgets
- Occurrences: 2 (ERR-002, ERR-003)
- Root cause: Developer assumed setting names were consistent across versions
- Impact: Template rejection on import
- Mitigation: Always verify setting names against version-specific documentation

### HIGH RISK: Duplicate Includable IDs
- Pattern: Same includable id used twice within one widget
- Occurrences: 1 (ERR-001)
- Root cause: Merging includable lists from multiple sources without deduplication
- Impact: Template rejection on import
- Mitigation: Always deduplicate includable lists; run pre-validation checks

---

## Recurring Categories

| Category | Occurrences | Risk Level |
|----------|-------------|------------|
| Widget Configuration | 2 | HIGH |
| XML Validation | 1 | HIGH |
| Responsive Layout | 1 | HIGH |
| Spacing System | 1 | HIGH |
| Typography | 1 | HIGH |
| Design System | 1 | **CRITICAL** |

---

## Watchlist

The following areas have not yet caused errors but are high-risk based on complexity:

1. **Comment system** — custom threaded comments with Blogger native data bindings
2. **Contact form hidden widget** — dual widget pattern for homepage + item page
3. **Related posts loop** — nested loop with conditional filtering
4. **FAQ JSON-LD** — hybrid visible microdata + separate JSON-LD schema
5. **Dark mode** — localStorage + CSS custom properties interaction
6. **Service card "Learn More" pseudo-element** — `::after` may be stripped by Blogger's CSS parser in some versions
7. **Glassmorphism in dark sections** — `backdrop-filter` may not work in all mobile browsers
