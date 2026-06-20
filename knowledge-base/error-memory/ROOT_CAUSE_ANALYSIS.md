# Root Cause Analysis — Deep Error Investigation

> For every error, identify the true root cause to prevent recurrence.

## ERR-001: Duplicate b:includable id='postCommentsLink'

**Problem:** Blogger rejects theme import — `b:includable id="postCommentsLink" declared more than once`

**Root Cause:** The includable list was compiled from two separate documentation sources:
1. Post-section includables list (which included `postCommentsLink`)
2. Comment-section includables list (which also included `postCommentsLink`)

Both were merged without deduplication. Both copies had identical content (`<b:comment>Disabled</b:comment>`).

**Why it happened:** The developer referenced two separate sections of the Blogger widget documentation without cross-referencing for overlap. The `postCommentsLink` includable appears in both the post metadata group and the comments group in Blogger's documentation.

**Technical Detail:** Blogger's XML parser enforces unique `id` attributes on `<b:includable>` elements within the same `<b:widget>`. Duplicate IDs cause an XML validation error that prevents template import/save. This is enforced at the Blogger platform level, not at the template level.

**Fix:** Removed one of the two identical includables. Either copy is safe to remove since both just disable the feature.

---

## ERR-002: Wrong BlogArchive v2 Setting Names

**Problem:** BlogArchive widget settings silently ignored

**Root Cause:** Version 2 of the BlogArchive widget uses different setting names than version 1:

| v1 (deprecated) | v2 (current) |
|-----------------|--------------|
| `displayStyle` | `showStyle` |
| `showType` | `frequency` |
| `showPostsCount` | `showPosts` |

The theme was using v1 names on a v2 widget declaration.

**Why it happened:** There are very few public references documenting the v2 setting names. Most Blogger documentation and tutorials reference the v1 API. No validation was run against a live Blogger instance.

**Fix:** Replaced all three setting names with their v2 equivalents.

---

## ERR-003: Incorrect Widget Version Attribute

**Problem:** Widget version string in wrong format

**Root Cause:** The version attribute on BlogArchive widget declared as `version='2'` but the setting names matched v1 API, creating inconsistency. The version value itself (`'2'`) was correct for v2, but the settings contradicted it.

**Why it happened:** No cross-validation between the version attribute and the setting names used.

**Fix:** Corrected setting names to match v2 API. Version remains `'2'`.

---

## UI-001 through UI-010: Design System Issues

**Common Root Cause:** The original theme was built without a centralized design token system, responsive testing methodology, or standardized component patterns. Each UI issue stemmed from missing abstraction layers:

| Issue | Root Cause Category |
|-------|---------------------|
| UI-001 (Hero mobile) | No responsive testing at ≤480px |
| UI-002 (Spacing) | No spacing scale abstraction |
| UI-003 (Typography) | No fluid type scale |
| UI-004 (Hero wrapper) | Missing containment pattern |
| UI-005 (Card heights) | Missing flex-column pattern |
| UI-006 (Sidebar) | Missing widget title pattern |
| UI-007 (Dark depth) | Missing dark-section pattern |
| UI-008 (Contact form) | Missing form pattern |
| UI-009 (Footer) | Missing grid hierarchy pattern |
| UI-010 (Design system) | No token system at all |

**Systemic Root Cause:** No design system specification existed before theme development began. Components were built ad-hoc without reusable patterns. The solution was to create `RANKRSEO_THEME_SPEC.md` with a complete token system and component library.
# ROOT CAUSE ANALYSIS

## ERR-001 — Duplicate includable id

### Problem
Blog1 widget had two `<b:includable id='postCommentsLink'>` elements, which violates Blogger's requirement that includable IDs be unique within a widget.

### Root Cause
When disabling unused default Blogger includables, the `postCommentsLink` includable was included twice:
1. In a group of standard post-related disabled includables (feedLinks, postShareButtons, postAuthor, etc.)
2. In a group of comment-related disabled includables (commentsLink, commentsLinkIframe, etc.)

The developer manually enumerated all known Blogger default includables from two different reference lists without cross-checking for duplicates.

### Why It Happened
- No automated deduplication check was run during assembly.
- The includable lists were composed from separate widget documentation sections (post section vs comments section) that both listed `postCommentsLink`.
- Hand-written XML with no validation step.

### Technical Explanation
Blogger's XML parser enforces unique `id` attributes on `<b:includable>` elements within the same `<b:widget>`. When two includables share the same id, Blogger rejects the template with a validation error. Both includables had identical disabled content (`<b:comment>Disabled</b:comment>`), making either one safe to remove.

---

## ERR-002 — Invalid setting name `displayStyle`

### Problem
BlogArchive1 widget used `<b:widget-setting name='displayStyle'>`, which is not a valid setting name for version='2' BlogArchive widgets.

### Root Cause
The setting name `displayStyle` is valid for **version='1'** BlogArchive widgets, but **version='2'** uses `showStyle` instead. The developer used the version='1' name without verifying the version='2' API.

### Why It Happened
- The initial knowledge base research documented `displayStyle` based on older Blogger references.
- No version check was performed when writing the widget settings.
- The version='2' widget API has renamed several settings from their version='1' names.

### Technical Explanation
BlogArchive widget settings differ between versions:

| Purpose | v1 Name | v2 Name |
|---------|---------|---------|
| Display style | `displayStyle` | `showStyle` |
| Grouping | `showType` | `frequency` |
| Show post count | `showPostsCount` | `showPosts` |
| Chronological order | — | `chronological` |
| Show week end | — | `showWeekEnd` |
| Year pattern | — | `yearPattern` |
| Month pattern | — | `monthPattern` |
| Week pattern | — | `weekPattern` |
| Day pattern | — | `dayPattern` |

The data property `data:this.style` is available in both versions, but the `<b:widget-setting>` name changed.

---

## ERR-003 — Invalid setting name `showPostsCount`

### Problem
BlogArchive1 widget used `<b:widget-setting name='showPostsCount'>`, which is not valid for version='2'.

### Root Cause
Same root cause as ERR-002. `showPostsCount` is a version='1' setting name; version='2' uses `showPosts`.

### Why It Happened
Identical to ERR-002 — the version='1' names were used throughout without checking version='2' compatibility.

### Technical Explanation
Version='2' BlogArchive uses `showPosts` (no "Count" suffix) as the setting name. The data property is still accessed as `data:i.post-count` in template markup, but the widget configuration setting name dropped the "Count" suffix.
