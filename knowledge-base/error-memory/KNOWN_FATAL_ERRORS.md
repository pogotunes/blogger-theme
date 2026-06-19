# Known Fatal Errors — Unrecoverable Patterns

> Errors that cause Blogger to reject theme import (fatal).
> These MUST NEVER appear in a theme submitted to Blogger.

## ERROR TYPE: XML Parse Failure

### FE-001: Duplicate `<b:includable id='...'>` in Same Widget
```
Blogger message: "includable with id postCommentsLink declared more than once"
Result: Theme import rejected. None of the theme is applied.
```

### FE-002: Invalid HTML Entity Outside CDATA
```
Example: &rarr; (should be → or &#8594;)
Result: XML parser refuses to parse the template file.
```

### FE-003: Unclosed `<b:skin><![CDATA[`
```
Result: Theme import rejected. The skin section must be a valid XML structure.
```

## ERROR TYPE: Structure Violation

### FE-004: Multiple `<head>` or `<body>` Elements
```
Result: Blogger template engine fails during rendering.
```

### FE-005: Missing Required Widget
```
Required widgets: Navbar1 (or no Navbar), Header1, Blog1
Result: Core blogging features unavailable.
```

### FE-006: Duplicate Section IDs
```
Each <b:section id='...'> must be unique.
Result: Section hidden or overlapping in Layout UI.
```

## ERROR TYPE: JavaScript Breakage

### FE-007: Modified Comment Editor Iframe
```html
<!-- WRONG: Removing or altering these attributes breaks comment submission -->
<iframe class='blogger-iframe-colorize blogger-comment-from-post'
        frameborder='0' id='comment-editor' name='comment-editor' src='' .../>
```
```
Symptom: Clicking "Post Comment" does nothing. Form doesn't load.
```

### FE-008: Removed ContactForm Iframe Bindings
```html
<!-- WRONG: Missing or broken expr:id on error/success message containers -->
```
```
Symptom: Contact form submits but no success/error feedback shown.
```

## FATAL PATTERN TABLE

| Code | Pattern | Error Message | Prevented By |
|------|---------|---------------|--------------|
| FE-001 | Duplicate includable id | "declared more than once" | RULE-001 |
| FE-002 | Invalid entity outside CDATA | XML parse error | RULE-003 |
| FE-003 | Broken skin/CDATA | XML parse error | RULE-003 |
| FE-004 | Multiple head/body | Template engine error | Structure check |
| FE-005 | Missing required widget | Layout/feature broken | Widget checklist |
| FE-006 | Duplicate section ID | Layout UI broken | Section check |
| FE-007 | Broken comment iframe | Comments broken | RULE-003 |
| FE-008 | Broken contact form | Form feedback broken | Widget reference |

## Recovery Procedure

If any fatal error is detected:
1. **STOP** theme generation
2. Document the error in MASTER_ERROR_MEMORY.json
3. Create new prevention rule if needed
4. Fix the specific pattern
5. Re-run validation
6. Only proceed after all fatal errors are cleared
