# Blogger XML Architecture — Complete Reference

> Deep reference covering every Blogger XML tag, data binding, rendering lifecycle, and engineering pattern.
> Total lines: 567 | Cross-references: BLOGGER_WIDGET_REFERENCE.md, SNIPPET_LIBRARY.xml

## 1. XML Namespaces

Every Blogger theme must declare these namespaces on `<html>`:

```xml
<html xmlns='http://www.w3.org/1999/xhtml'
      xmlns:b='http://www.google.com/2005/gml/b'
      xmlns:data='http://www.google.com/2005/gml/data'
      xmlns:expr='http://www.google.com/2005/gml/expr'>
```

| Namespace | Prefix | Purpose |
|-----------|--------|---------|
| `http://www.w3.org/1999/xhtml` | (default) | Standard XHTML |
| `http://www.google.com/2005/gml/b` | `b:` | Blogger tags (if, loop, widget, section, include) |
| `http://www.google.com/2005/gml/data` | `data:` | Access blog/post/widget data |
| `http://www.google.com/2005/gml/expr` | `expr:` | Dynamic attribute values |

### Modern Theme Attributes

```xml
<html b:css='false'
      b:defaultwidgetversion='2'
      b:layoutsVersion='3'
      b:responsive='true'
      b:templateVersion='2.0.0'
      expr:class='data:blog.languageDirection'
      expr:dir='data:blog.languageDirection'
      expr:lang='data:blog.localeUnderscoreDelimited'>
```

| Attribute | Purpose |
|-----------|---------|
| `b:css='false'` | Disable Blogger's built-in CSS injection |
| `b:defaultwidgetversion='2'` | Use modern widget templates |
| `b:layoutsVersion='3'` | Latest layout engine |
| `b:responsive='true'` | Enable responsive features |
| `b:templateVersion='2.0.0'` | Template version identifier |

## 2. Document Structure

```
<!DOCTYPE html>
<html ...>
  <head>
    <b:include data='blog' name='all-head-content'/>   <!-- Blogger essentials -->
    <title>...</title>
    <b:skin><![CDATA[ /* ALL CSS */ ]]></b:skin>        <!-- Embedded CSS -->
  </head>
  <body>
    <b:section id='...'>                                  <!-- Widget containers -->
      <b:widget id='...' type='...'>
        <b:includable id='main'>                           <!-- Widget template -->
          ...
        </b:includable>
      </b:widget>
    </b:section>
    <b:include name='...'/>                               <!-- Reusable includes -->
    <b:section-contents id='...'/>                        <!-- Section content -->
  </body>
</html>
```

## 3. Core Tags Reference

### `<b:section>`

```xml
<b:section id='unique-id'
           class='optional-css-class'
           maxwidgets='1'
           showaddelement='yes|no'>
```

| Attribute | Values | Purpose |
|-----------|--------|---------|
| `id` | Unique string | Section identifier (must be unique in document) |
| `class` | CSS class | Optional styling hook |
| `maxwidgets` | Number | Max widgets in this section |
| `showaddelement` | `yes`/`no` | Show "Add a Gadget" in Layout UI |

### `<b:widget>`

```xml
<b:widget id='Blog1'
          locked='false'
          title='Blog Posts'
          type='Blog'
          version='2'
          visible='true'>
  <b:widget-settings>
    <!-- Settings specific to widget type -->
  </b:widget-settings>
  <b:includable id='main' var='top'>
    <!-- Custom widget template -->
  </b:includable>
</b:widget>
```

### `<b:includable>`

```xml
<b:includable id='uniqueName' var='localVar'>
  <!-- Reusable template chunk -->
</b:includable>
```

All standard Blog widget includables must be defined or explicitly disabled:
```xml
<b:includable id='postCommentsLink'><b:comment>Disabled</b:comment></b:includable>
```

CRITICAL: All includable IDs within the same widget MUST be unique. Duplicate IDs cause Blogger to reject the template with validation error.

### `<b:if>` / `<b:else>`

```xml
<b:if cond='data:view.isPost'>
  <!-- Post content -->
<b:else/>
  <!-- Non-post content -->
</b:if>
```

Common conditional data:
- `data:view.isPost` / `data:view.isHomepage` / `data:view.isMultipleItems`
- `data:view.isArchive` / `data:view.isSearch` / `data:view.isLabelSearch`
- `data:view.isError` / `data:view.isPage` / `data:view.isSingleItem`
- `data:post.allowComments` / `data:post.allowNewComments`
- `data:post.labels.any` / `data:post.featuredImage`
- `data:posts.empty` / `data:view.search.query`

### `<b:loop>`

```xml
<b:loop index='i' values='data:posts' var='post' max='10'>
  <article>
    <h2><data:post.title/></h2>
  </article>
</b:loop>
```

| Attribute | Purpose |
|-----------|---------|
| `values` | Collection to iterate (e.g., `data:posts`, `data:post.labels`, `data:links`) |
| `var` | Loop variable name (e.g., `post`, `label`, `link`) |
| `index` | Optional loop index variable |
| `max` | Maximum iterations |

### `<b:include>`

```xml
<b:include name='componentName'/>
<b:include cond='data:view.isPost' name='shareBox'/>
<b:include data='post' name='commentFormIframeSrc'/>
```

### `<data:*>` — Dynamic Data Output

```xml
<data:post.title/>           <!-- Escaped title -->
<data:post.body/>            <!-- Post body HTML -->
<data:blog.title/>           <!-- Blog title -->
<data:view.title.escaped/>   <!-- View title, escaped -->
<data:view.url.canonical/>   <!-- Canonical URL -->
<data:post.url/>             <!-- Post URL -->
<data:post.date/>            <!-- Formatted date -->
<data:post.author.name/>     <!-- Author name -->
<data:post.numberOfComments/> <!-- Comment count -->
<data:post.labels.first.name/> <!-- First label -->
<data:messages.home/>        <!-- "Home" localized -->
<data:view.search.query/>    <!-- Search query -->
<data:skin.vars.keycolor/>   <!-- Skin variable -->
```

### `<expr:*>` — Dynamic Attributes

```xml
<a expr:href='data:post.url' expr:title='data:post.title'>
<img expr:src='resizeImage(data:post.featuredImage, 400, "16:9")'/>
```

### `<b:eval>`

```xml
<b:eval expr='data:post.snippets.short snippet { length: 150 }'/>
<b:eval expr='data:post.featuredImage.isYouTube
  ? data:post.featuredImage.youtubeMaxResDefaultUrl.jsonEscaped
  : resizeImage(data:post.featuredImage, 400, "16:9")'/>
```

### `<b:class>`

```xml
<b:class expr:name='data:blog.languageDirection'/>
<!-- Renders: class='ltr' or class='rtl' -->
```

### `<b:tag>` / `<b:with>`

```xml
<b:tag cond='data:post.featuredImage' name='figure' class='post-figure'>
  <b:with var='imgSrc' value='resizeImage(data:post.featuredImage, 800)'>
    <img expr:src='data:imgSrc'/>
  </b:with>
</b:tag>
```

### `<b:comment>`

```xml
<b:comment>This will NOT appear in HTML output</b:comment>
```

## 4. Data Variable Reference

### `data:view.*` — Current View

| Variable | Type | Description |
|----------|------|-------------|
| `data:view.isHomepage` | Boolean | True on homepage |
| `data:view.isPost` | Boolean | True on single post page |
| `data:view.isPage` | Boolean | True on static page |
| `data:view.isMultipleItems` | Boolean | True on multi-post views |
| `data:view.isArchive` | Boolean | True on archive page |
| `data:view.isSearch` | Boolean | True on search results |
| `data:view.isLabelSearch` | Boolean | True on label page |
| `data:view.isSingleItem` | Boolean | True for single item (post/page) |
| `data:view.isError` | Boolean | True on 404 error page |
| `data:view.isMobile` | Boolean | True on mobile view |
| `data:view.title.escaped` | String | Page title, escaped |
| `data:view.url.canonical` | URL | Canonical URL |
| `data:view.description.escaped` | String | Page description |
| `data:view.search.query` | String | Search query text |
| `data:view.search.label` | String | Label name if on label page |
| `data:view.archive.rangeMessage` | String | Archive date range |

### `data:blog.*` — Blog-Wide Data

| Variable | Type | Description |
|----------|------|-------------|
| `data:blog.title` | String | Blog title |
| `data:blog.title.escaped` | String | Escaped blog title |
| `data:blog.description` | String | Blog description |
| `data:blog.url` | URL | Blog root URL |
| `data:blog.homepageUrl` | URL | Homepage URL |
| `data:blog.pageType` | String | Page type string |
| `data:blog.languageDirection` | String | `ltr` or `rtl` |
| `data:blog.localeUnderscoreDelimited` | String | Locale (e.g., `en_US`) |
| `data:blog.encoding` | String | Character encoding |
| `data:blog.bloggerUrl` | URL | Blogger admin URL |
| `data:blog.feedLinks` | String | RSS/Atom link tags |
| `data:blog.blogspotFaviconUrl` | URL | Favicon URL |
| `data:blog.posts` | Collection | All blog posts |
| `data:blog.metaDescription` | String | Meta description |

### `data:post.*` — Post Data (inside `b:loop values='data:posts'`)

| Variable | Type | Description |
|----------|------|-------------|
| `data:post.id` | Number | Post ID |
| `data:post.title` | String | Post title |
| `data:post.body` | HTML | Post body content |
| `data:post.url` | URL | Post URL |
| `data:post.url.canonical` | URL | Canonical post URL |
| `data:post.date` | String | Formatted publish date |
| `data:post.date.iso8601` | String | ISO 8601 date |
| `data:post.author.name` | String | Author name |
| `data:post.author.authorPhoto.image` | URL | Author photo |
| `data:post.authorUrl` | URL | Author profile URL |
| `data:post.featuredImage` | URL | Featured image URL |
| `data:post.featuredImage.isYouTube` | Boolean | Is YouTube video |
| `data:post.featuredImage.youtubeMaxResDefaultUrl` | URL | YT max res thumbnail |
| `data:post.numberOfComments` | Number | Comment count |
| `data:post.allowComments` | Boolean | Comments enabled |
| `data:post.allowNewComments` | Boolean | New comments allowed |
| `data:post.embedCommentForm` | Boolean | Show embedded form |
| `data:post.commentHtml` | HTML | Rendered comments |
| `data:post.commentJso` | JSON | Comments JSON |
| `data:post.labels` | Collection | Post labels |
| `data:post.labels.any` | Boolean | Has labels |
| `data:post.labels.first.name` | String | First label name |
| `data:post.snippets.short` | String | Post snippet |

### `data:messages.*` — Localized Strings

| Variable | Description |
|----------|-------------|
| `data:messages.home` | "Home" |
| `data:messages.newerPosts` | "Newer Posts" |
| `data:messages.olderPosts` | "Older Posts" |
| `data:messages.noTitle` | "No title" |
| `data:messages.theresNothingHere` | 404 message |

### `data:skin.vars.*` — CSS Variables

Access to variables defined with `<Variable>` tag in `<b:skin>`:
```xml
<Variable name="keycolor" description="Main Color" type="color" default="#2563EB" value="#2563EB"/>
<!-- Access: data:skin.vars.keycolor -->
```

## 5. Render Lifecycle

1. **Template Parsing** — Blogger reads the XML template
2. **Widget Registration** — All `<b:widget>` elements registered
3. **Data Binding** — `data:*` expressions resolved against blog data
4. **Conditional Evaluation** — `<b:if>` branches resolved
5. **Loop Expansion** — `<b:loop>` iterates and expands
6. **Include Resolution** — `<b:include>` references expanded
7. **Skin Processing** — CSS variables in `<b:skin>` evaluated
8. **HTML Generation** — Final HTML output
9. **Blogger JS Activation** — Platform JS activates widgets (comments, reactions, etc.)
10. **Client Rendering** — Browser renders the page

## 6. Skin / CSS System

CSS is embedded within `<b:skin><![CDATA[...]]></b:skin>` in `<head>`.

```xml
<b:skin><![CDATA[
/* Variables defined here are accessible as CSS custom properties */
:root {
  --primary: $(keycolor);  /* $(name) references <Variable> tag */
}
]]></b:skin>
```

Variable definition:
```xml
<Variable name="keycolor" description="Main Color"
          type="color" default="#2563EB" value="#2563EB"
          min="0" max="16777215"/>
```

## 7. Image Resize Function

```xml
<!-- Syntax: resizeImage(url, width, aspectRatio) -->
<img expr:src='resizeImage(data:post.featuredImage, 400, "16:9")'/>
<img expr:src='resizeImage(data:post.author.authorPhoto.image, 40)'/>
```

## 8. Pagination Data

```xml
<b:if cond='data:newerPageUrl'>
  <a expr:href='data:newerPageUrl' rel='prev'>&larr; Newer</a>
</b:if>
<b:if cond='data:olderPageUrl'>
  <a expr:href='data:olderPageUrl' rel='next'>Older &rarr;</a>
</b:if>
```
