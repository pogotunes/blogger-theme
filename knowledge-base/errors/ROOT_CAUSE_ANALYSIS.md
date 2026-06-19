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
