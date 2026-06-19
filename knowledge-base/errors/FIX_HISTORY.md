# FIX HISTORY

## ERR-001 — Duplicate includable id

| Field | Value |
|-------|-------|
| Error ID | ERR-001 |
| Status | Fixed |

### Old Code (lines 2144 and 2173)
```xml
<b:includable id='postCommentsLink'><b:comment>Disabled</b:comment></b:includable>
...
<b:includable id='postCommentsLink'><b:comment>Disabled</b:comment></b:includable>
<b:includable id='commentsLink'><b:comment>Disabled</b:comment></b:includable>
```

### New Code
```xml
<b:includable id='commentsLink'><b:comment>Disabled</b:comment></b:includable>
```

### Fix Explanation
Removed the duplicate `postCommentsLink` includable at line 2173 (the second occurrence). The first occurrence (line 2144) was kept as it was grouped with other standard post-related disabled includables. Since both were identical disabled stubs, either could be removed.

### Validation
- [x] Confirmed only one `postCommentsLink` includable remains
- [x] Widget tag balance verified (19 open, 18 close, 1 self-closing — correct)

---

## ERR-002 — Invalid setting name `displayStyle`

| Field | Value |
|-------|-------|
| Error ID | ERR-002 |
| Status | Fixed |

### Old Code
```xml
<b:widget-setting name='displayStyle'>DROPDOWN</b:widget-setting>
```

### New Code
```xml
<b:widget-setting name='showStyle'>MENU</b:widget-setting>
```

### Fix Explanation
Changed setting name from `displayStyle` (version='1') to `showStyle` (version='2'). Also changed value from `DROPDOWN` to `MENU` — version='2' uses `MENU` instead of `DROPDOWN` for the dropdown menu style.

### Validation
- [x] Confirmed setting name change in theme XML
- [x] Updated BLOGGER_WIDGET_REFERENCE.md documentation

---

## ERR-003 — Invalid setting name `showPostsCount`

| Field | Value |
|-------|-------|
| Error ID | ERR-003 |
| Status | Fixed |

### Old Code
```xml
<b:widget-setting name='showPostsCount'>true</b:widget-setting>
```

### New Code
```xml
<b:widget-setting name='showPosts'>true</b:widget-setting>
```

### Fix Explanation
Changed setting name from `showPostsCount` (version='1') to `showPosts` (version='2'). Also fixed `showType` → `frequency` in the same settings block for completeness.

### Validation
- [x] Confirmed all three BlogArchive1 settings use correct version='2' names
- [x] Updated BLOGGER_WIDGET_REFERENCE.md documentation with all 9 valid settings
