# High-Risk Patterns Registry

> Patterns and practices that carry elevated risk of failure in Blogger XML theme development.
> Risk Level: 🔴 Critical | 🟠 High | 🟡 Medium

## 🔴 CRITICAL RISK

### HR-001: Duplicate Includable IDs
**Risk:** Theme import rejection
**Trigger:** Compiling includable lists from multiple sources without deduplication
**Detection:** `grep 'b:includable id='` and check for duplicate values
**Prevention:** RULE-001

### HR-002: Invalid XML Entities Outside CDATA
**Risk:** XML parse failure
**Examples:** `&rarr;`, `&larr;`, `&copy;` — Only `&amp;`, `&lt;`, `&gt;`, `&quot;`, `&apos;` are safe
**Exception:** Inside `<![CDATA[ ]]>` blocks
**Prevention:** RULE-003

### HR-003: No Design Token System
**Risk:** CSS inconsistency, maintenance nightmare
**Detection:** Existence of raw `px`, `rem`, `em` values outside `:root`
**Prevention:** RULE-015

## 🟠 HIGH RISK

### HR-004: Widget Settings API Mismatch
**Risk:** Widget silently ignores settings
**Trigger:** Using v1 setting names on v2 widget declarations
**Detection:** Check `version` attribute against `<b:widget-setting>` names
**Prevention:** RULE-002

### HR-005: JS Comments Inside `<b:skin>`
**Risk:** CSS parse failure
**Trigger:** Using `//` for comments inside CSS CDATA
**Safe:** `/* CSS comments */` or remove comments entirely
**Prevention:** RULE-003

### HR-006: Broken Comment iframe
**Risk:** Comment submission broken
**Trigger:** Removing or modifying the comment iframe source/sandbox attributes
**Prevention:** RULE-003

### HR-007: Unchecked Theme Import
**Risk:** Unknown failures on live Blogger
**Trigger:** Skipping XML validation before import
**Prevention:** RULE-004

## 🟡 MEDIUM RISK

### HR-008: Missing Responsive Breakpoints
**Risk:** Mobile layout breaks
**Detection:** No responsive CSS for ≤480px
**Prevention:** RULE-006

### HR-009: Absolute Heights on Cards
**Risk:** Content overflow on variable-length content
**Detection:** `height:` on card components (not `min-height:`)
**Prevention:** RULE-010

### HR-010: Contact Form Without Hidden Duplicate
**Risk:** Contact form iframe breaks on item pages
**Detection:** Only one ContactForm widget, not hidden
**Prevention:** Hidden widget pattern

### HR-011: Undeclared Includables
**Risk:** Blogger uses default includables, overriding custom templates
**Detection:** Missing disabled includables for unused features
**Prevention:** Include all standard Blog1 includables

### HR-012: Missing Schema Markup
**Risk:** Poor SEO/AEO/GEO performance
**Detection:** No JSON-LD `@graph` or BlogPosting schema
**Prevention:** Include all schemas per SEO_AEO_GEO_BLUEPRINT.md

## Monitoring Checklist

| Risk ID | Last Checked | Status |
|---------|-------------|--------|
| HR-001 | — | Not checked |
| HR-002 | — | Not checked |
| HR-003 | — | Not checked |
| HR-004 | — | Not checked |
| HR-005 | — | Not checked |
| HR-006 | — | Not checked |
| HR-007 | — | Not checked |
| HR-008 | — | Not checked |
| HR-009 | — | Not checked |
| HR-010 | — | Not checked |
| HR-011 | — | Not checked |
| HR-012 | — | Not checked |
