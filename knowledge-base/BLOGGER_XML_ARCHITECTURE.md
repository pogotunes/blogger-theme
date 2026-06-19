# Blogger XML Architecture — Complete Reference

## 1. XML Namespaces

Every Blogger theme must declare these namespaces on the `<html>` element:

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

Modern themes also add:

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
    <!-- SECTIONS + WIDGETS -->
    <b:section id='main'>
      <b:widget id='Blog1' type='Blog'>
        <b:includable id='main'>
          <!-- Post rendering -->
        </b:includable>
      </b:widget>
    </b:section>
  </body>
</html>
```

## 3. Complete Tag Reference

### `<b:section>` — Widget Container

Defines an area where widgets can be placed.

```xml
<b:section id='unique-id'
           maxwidgets='3'
           showaddelement='yes|no'
           class='custom-class'
           deleted='true|false'
           name='Display Name'>
```

| Attribute | Description |
|-----------|-------------|
| `id` | Unique identifier (required). Convention: lowercase-kebab-case |
| `maxwidgets` | Maximum widgets allowed in this section |
| `showaddelement` | Show "Add a Gadget" in Blogger Layout (yes=visible) |
| `class` | CSS class for the section container |
| `deleted` | If true, section and content hidden (used for hidden-widgets pattern) |
| `name` | Display name shown in Blogger Layout UI |

**Common section IDs:**
- `main` — Main blog content area
- `sidebar` — Sidebar widgets
- `header` — Header area
- `footer` — Footer widgets
- `hidden-widgets` — Invisible widget storage
- `admin` — Admin section (Blogger internal)
- `hot-posts` — Featured/hero posts area
- `ft-post` — Featured post grid
- `footer-copyright` — Copyright bar
- `footer-checks-menu` — Footer navigation

### `<b:widget>` — Widget Instance

Registers a widget in a section.

```xml
<b:widget id='WidgetId' locked='true|false' title='Widget Title' type='WidgetType' version='2' visible='true|false'>
  <b:widget-settings>
    <b:widget-setting name='settingName'>value</b:widget-setting>
  </b:widget-settings>
  <b:includable id='main'>...</b:includable>
</b:widget>
```

| Attribute | Description |
|-----------|-------------|
| `id` | Unique widget ID (e.g., Blog1, PopularPosts2, Label3) |
| `locked` | If true, cannot be moved/deleted in Layout UI |
| `title` | Widget title shown in Layout UI |
| `type` | Widget type (Blog, Header, PopularPosts, Label, LinkList, HTML, Image, ContactForm, etc.) |
| `version` | Widget version (1 or 2; 2 enables modern markup) |
| `visible` | If false, widget is hidden |

### `<b:includable>` — Template Override

Overrides the default rendering of a widget or creates reusable snippets.

```xml
<b:includable id='main' var='this'>
  <!-- Widget rendering code -->
</b:includable>

<!-- Reusable snippet -->
<b:includable id='widget-title'>
  <b:if cond='data:title'>
    <h3 class='title'><data:title/></h3>
  </b:if>
</b:includable>
```

| Attribute | Description |
|-----------|-------------|
| `id` | Must be `main` to override widget, or any custom name |
| `var` | Variable name passed when included (e.g., `var='post'`) |

**Required includables for Blog widget override:**
- `main` — Main rendering
- `postTitle` — Title rendering
- `postMeta` / `postsByline` — Metadata
- `postFooterByline` — Footer metadata
- `postCommentsLink` — Comments link
- `postShareButtons` — Share buttons
- `postAuthor` — Author display
- `postTimestamp` — Date display
- `postLabels` — Label display
- `postReactions` — Reactions
- `postJumpLink` — Read more link
- `postBody` — Post body snippet
- `feedLinks` — Feed links
- `previousPageLink` / `nextPageLink` — Pagination
- `blogPager` — Full pagination
- `headerByline` — Header byline
- `footerBylines` — Footer bylines

A widget with `b:includable id='main'` completely replaces the widget's default output. To selectively override parts, match the includable name exactly.

To disable a built-in feature without removing the widget:
```xml
<b:includable id='postShareButtons'><b:comment>Disabled</b:comment></b:includable>
```

### `<b:defaultmarkup>` — Type-Level Override

Overrides rendering for ALL widgets of a given type.

```xml
<b:defaultmarkup type='PopularPosts'>
  <b:includable id='main'>...</b:includable>
  <b:includable id='content'>...</b:includable>
</b:defaultmarkup>
```

This is more efficient than overriding each widget instance individually. Place inside `<head>` after `<b:skin>`.

### `<b:if>` — Conditional Rendering

```xml
<b:if cond='condition'>
  <!-- Show this -->
<b:elseif cond='other-condition'/>
  <!-- Show this instead -->
<b:else/>
  <!-- Fallback -->
</b:if>
```

**Common conditions:**

| Condition | When True |
|-----------|-----------|
| `data:view.isHomepage` | On homepage |
| `data:view.isPost` | On single post page |
| `data:view.isPage` | On static page |
| `data:view.isSingleItem` | On single item (post or page) |
| `data:view.isMultipleItems` | On index/archive/search/label pages |
| `data:view.isSearch` | On search results |
| `data:view.isLabelSearch` | On label filtered search |
| `data:view.isArchive` | On archive page |
| `data:view.isError` | On 404 error page |
| `data:view.isLayoutMode` | In Blogger Layout editor |
| `data:view.isPreview` | In preview mode |
| `data:view.isMobile` | On mobile view |
| `data:blog.url == data:blog.homepageUrl` | On homepage (older style) |
| `data:blog.pageType == "item"` | On item page (older style) |
| `data:blog.pageType == "index"` | On index page (older style) |
| `data:blog.pageType == "archive"` | On archive (older style) |
| `data:blog.pageType == "error_page"` | On 404 (older style) |
| `data:post.allowComments` | Comments are enabled |
| `data:post.allowNewComments` | New comments allowed |
| `data:post.featuredImage` | Post has featured image |
| `data:post.firstImageUrl` | Post has at least one image |
| `data:post.labels.any` | Post has labels |
| `data:posts.empty` | No posts found |
| `data:newerPageUrl` | There is a newer page |
| `data:olderPageUrl` | There is an older page |
| `data:post.author.authorPhoto.image` | Author has profile photo |

### `<b:loop>` — Iteration

```xml
<b:loop index='i' values='data:posts' var='post'>
  <!-- Access data:post.title, data:post.url, etc. -->
</b:loop>
```

| Attribute | Description |
|-----------|-------------|
| `values` | Collection to iterate (data:posts, data:labels, data:links, etc.) |
| `var` | Loop variable name (used as data:var.* inside loop) |
| `index` | Optional, access loop index: `data:i` |

**Common loop targets:**

| Expression | Iterates Over |
|------------|---------------|
| `data:posts` | Blog posts |
| `data:post.labels` | Post labels |
| `data:links` | LinkList widget links |
| `data:labels` | Label widget labels |
| `data:authors` | Team members |
| `data:archives` | Archive entries |
| `data:texts` | TextList widget items |

### `<b:include>` — Snippet Inclusion

```xml
<b:include name='widget-title'/>

<!-- With data passing -->
<b:include data='post' name='postTitle'/>

<!-- Conditional include -->
<b:include cond='data:view.isPost' name='share-box'/>
```

| Attribute | Description |
|-----------|-------------|
| `name` | Name of the includable (matches `id` on `<b:includable>`) |
| `data` | What variable to pass (e.g., `data='post'` becomes accessible as `var='post'`) |
| `cond` | Optional condition for conditional inclusion |

### `<data:*>` — Data Output

Outputs data values into the HTML. Auto-escaped in v2 widgets.

```xml
<data:post.title/>
<data:post.body/>
<data:post.date/>
<data:post.author.name/>
<data:blog.title/>
<data:blog.pageTitle/>
<data:blog.url/>
<data:messages.noTitle/>
<data:messages.home/>
<data:contactFormNameMsg/>
```

### `<expr:*>` — Dynamic Attribute Values

Sets HTML attributes dynamically:

```xml
<a expr:href='data:post.url' expr:title='data:post.title'>...</a>
<img expr:src='data:post.featuredImage' expr:alt='data:post.title'/>
<div expr:class='data:blog.languageDirection'>...</div>
```

### `<b:eval>` — Expression Evaluation (v2+)

Evaluates and outputs expressions with filtering:

```xml
<b:eval expr='data:post.title ? data:post.title : data:messages.noTitle'/>
<b:eval expr='data:post.snippets.short snippet { length: 120 }'/>
```

### `<b:class>` — Conditional CSS Class

```xml
<b:class expr:name='data:post.featuredImage.isYouTube ? "video-nos" : "image-nos"'/>
<b:class name='active'/>
```

### `<b:tag>` — Conditional HTML Tag

```xml
<b:tag name='script' type='text/javascript'>
  // JavaScript code
</b:tag>
<b:tag cond='data:view.isMultipleItems' name='link' rel='next'/>
```

### `<b:with>` — Variable Assignment

```xml
<b:with value='data:view.isSearch and (data:view.url == data:view.url params { amp: "1" })' var='isFeed'>
  <!-- data:isFeed is available inside this scope -->
</b:with>
```

### `<b:comment>` — Template Comments

```xml
<b:comment>This will NOT appear in HTML output</b:comment>
```

## 4. Data Variable Reference

### `data:view.*` — View Data (Modern API)

| Variable | Type | Description |
|----------|------|-------------|
| `data:view.isHomepage` | Boolean | True on homepage |
| `data:view.isPost` | Boolean | True on single post |
| `data:view.isPage` | Boolean | True on static page |
| `data:view.isSingleItem` | Boolean | True on post OR page |
| `data:view.isMultipleItems` | Boolean | True on index/archive/search/label |
| `data:view.isSearch` | Boolean | True on search results |
| `data:view.isLabelSearch` | Boolean | True on label search |
| `data:view.isArchive` | Boolean | True on archive |
| `data:view.isError` | Boolean | True on 404 |
| `data:view.isLayoutMode` | Boolean | True in Layout editor |
| `data:view.isPreview` | Boolean | True in preview |
| `data:view.isMobile` | Boolean | True on mobile |
| `data:view.title` | String | Page title (unescaped) |
| `data:view.title.escaped` | String | Page title (escaped) |
| `data:view.url` | URL | Current page URL |
| `data:view.url.canonical` | URL | Canonical URL |
| `data:view.description` | String | Page description |
| `data:view.description.escaped` | String | Escaped description |
| `data:view.featuredImage` | URL | Featured image URL |
| `data:view.search.query` | String | Search query |
| `data:view.search.label` | String | Label name |
| `data:view.archive.rangeMessage` | String | Archive range text |

### `data:blog.*` — Blog Configuration

| Variable | Description |
|----------|-------------|
| `data:blog.title` | Blog title |
| `data:blog.title.escaped` | Escaped blog title |
| `data:blog.pageTitle` | Current page title |
| `data:blog.pageName` | Post/page name |
| `data:blog.pageType` | Page type string: "item", "index", "archive", "error_page" |
| `data:blog.url` | Blog URL |
| `data:blog.homepageUrl` | Homepage URL |
| `data:blog.canonicalUrl` | Canonical URL |
| `data:blog.canonicalHomepageUrl` | Canonical homepage |
| `data:blog.metaDescription` | Meta description |
| `data:blog.languageDirection` | "ltr" or "rtl" |
| `data:blog.localeUnderscoreDelimited` | Locale (e.g., "en_US") |
| `data:blog.encoding` | Character encoding |
| `data:blog.blogId` | Blog ID number |
| `data:blog.postImageUrl` | Post image URL (item pages) |
| `data:blog.postImageThumbnailUrl` | Thumbnail URL |
| `data:blog.postThumbnailUrl` | Thumbnail URL (alternative) |
| `data:blog.feedLinks` | Atom/RSS feed link tags |
| `data:blog.meTag` | OpenID me tag |
| `data:blog.blogspotFaviconUrl` | Favicon URL |
| `data:blog.adultContent` | Boolean, adult content flag |
| `data:blog.isMobile` | Boolean, mobile view |

### `data:post.*` — Post Data (Inside Blog Loop)

| Variable | Description |
|----------|-------------|
| `data:post.title` | Post title |
| `data:post.body` | Full post body HTML |
| `data:post.snippets.short snippet { length: N }` | Truncated snippet (use with `<b:eval>`) |
| `data:post.url` | Post URL |
| `data:post.url.canonical` | Canonical post URL |
| `data:post.date` | Formatted date |
| `data:post.date.iso8601` | ISO 8601 date |
| `data:post.author.name` | Author display name |
| `data:post.author.authorPhoto.image` | Author photo URL |
| `data:post.authorUrl` | Author profile URL |
| `data:post.featuredImage` | Featured image URL |
| `data:post.featuredImage.isYouTube` | Boolean, is YouTube video |
| `data:post.featuredImage.youtubeMaxResDefaultUrl` | YouTube max res thumbnail |
| `data:post.firstImageUrl` | First image in post |
| `data:post.labels` | Label collection |
| `data:post.labels.any` | Boolean, has any label |
| `data:post.labels.first.name` | First label name |
| `data:post.numberOfComments` | Comment count |
| `data:post.allowComments` | Boolean, comments enabled |
| `data:post.allowNewComments` | Boolean, new comments allowed |
| `data:post.embedCommentForm` | Boolean, embedded form |
| `data:post.commentHtml` | Rendered comment HTML |
| `data:post.commentJso` | Comments JSON object |
| `data:post.commentMsgs` | Comments messages |
| `data:post.commentConfig` | Comments config |
| `data:post.commentSrc` | Comments script source |
| `data:post.appRpcRelayPath` | RPC relay path |
| `data:post.cmtfpIframe` | Comment form iframe |
| `data:post.noNewCommentsText` | No new comments text |
| `data:post.id` | Post ID |

### `data:widget.*` — Widget Data

| Variable | Description |
|----------|-------------|
| `data:widget.instanceId` | Unique widget instance ID |
| `data:widget.sectionId` | Section ID containing this widget |
| `data:widget.title` | Widget title |
| `data:widget.type` | Widget type string |
| `data:widgets.Blog.first.posts` | First blog widget's posts |

### `data:skin.vars.*` — Variable Access

Access theme variables defined in `<b:skin>` Variable definitions:

```xml
<data:skin.vars.keycolor/>
<data:skin.vars.main_button_color/>
```

### `data:messages.*` — Localized Strings

| Variable | English Default |
|----------|----------------|
| `data:messages.home` | "Home" |
| `data:messages.noTitle` | "No title" |
| `data:messages.newerPosts` | "Newer Posts" |
| `data:messages.olderPosts` | "Older Posts" |
| `data:messages.theresNothingHere` | "There's nothing here" |
| `data:messages.myPhoto` | "My photo" |
| `data:messages.reactions` | Reactions labels |

### `data:contactForm*` — Contact Form Messages

| Variable | Description |
|----------|-------------|
| `data:contactFormNameMsg` | "Name" placeholder |
| `data:contactFormEmailMsg` | "Email" placeholder |
| `data:contactFormMessageMsg` | "Message" placeholder |
| `data:contactFormSendMsg` | "Send" button text |

## 5. Skin System (CSS)

```xml
<b:skin><![CDATA[
  /*
  <Variable name="keycolor" description="Theme Color" type="color" default="#ff0000" value="#ff0000"/>
  <Group description="Colors" selector="body">
    <Variable name="body.background" description="Background" type="background" color="#fff" default="$(color) url() repeat fixed top left" value="$(color) url() repeat fixed top left"/>
  </Group>
  */
  
  :root {
    --accent: $(keycolor);
  }
  
  body {
    background: $(body.background);
  }
]]></b:skin>
```

### Variable Definition Types

| Type | Description | Example |
|------|-------------|---------|
| `color` | Color picker in Blogger Theme Designer | `default="#ff0000"` |
| `font` | Font selector | `family="Arial"` |
| `length` | Size selector | `default="1178px" min="900px" max="1600px"` |
| `background` | Background with image options | Complex type with color + image |

### Variable Groups

```
<Group description="Group Name" selector="css-selector">
```

Variables can be hidden from Theme Designer:
```
<Variable name="var.name" description="..." hideEditor="true" .../>
```

## 6. Render Lifecycle

1. **Blogger Server** evaluates XML template
2. `<b:if>`, `<b:loop>`, `<b:include>` processed server-side
3. `<data:*>` replaced with actual values
4. `<expr:*>` evaluated and applied to attributes
5. `<b:eval>` expressions computed
6. `<b:skin>` CSS extracted and served separately by Blogger
7. Final HTML sent to browser
8. Browser loads HTML + CSS + inline JS
9. Blogger's platform JS activates widgets (comments, reactions, etc.)

## 7. Template Inheritance

Blogger does not support modern template inheritance. Instead:

- **`<b:defaultmarkup>`** applies overrides widget-type-wide
- **`<b:includable>`** creates reusable snippets via `<b:include>`
- **`<b:with>`** scopes variables locally
- No extends/blocks pattern exists

## 8. Pagination Data

```xml
<b:if cond='data:newerPageUrl'>
  <a expr:href='data:newerPageUrl' rel='previous'>Newer</a>
</b:if>
<b:if cond='data:olderPageUrl'>
  <a expr:href='data:olderPageUrl' rel='next'>Older</a>
</b:if>
```

Available inside Blog widget's `main` includable:
- `data:newerPageUrl` — URL of newer posts page
- `data:newerPageTitle` — Title of newer page
- `data:olderPageUrl` — URL of older posts page
- `data:olderPageTitle` — Title of older page

## 9. Image Resize Function

```xml
resizeImage(data:post.featuredImage, 400, "16:9")
resizeImage(data:post.author.authorPhoto.image, 40)
```

Parameters: (imageUrl, size, aspectRatio?)

## 10. Best Practices from Repository Analysis

1. **Use `data:view.*` over `data:blog.*`** — Modern API is more reliable
2. **Use `data:view.url.canonical`** — Properly handles pagination params
3. **Use `data:view.title.escaped`** — XSS safe
4. **Use `b:eval` for expressions** — More powerful than nested `<b:if>`
5. **Wrap all JS in `//<![CDATA[ ... //]]>`** — Prevents XML parsing errors
6. **Use `b:include cond='...'`** — Conditional inclusion is cleaner than wrapping
7. **Use `b:defaultmarkup`** for widget-type-wide overrides instead of per-instance
8. **Use `b:class`** instead of `expr:class` for conditional CSS classes
9. **Always provide fallback for images** — ternary operator pattern
10. **Use `b:if cond='data:post.title'`** before outputting titles to avoid empty markup
