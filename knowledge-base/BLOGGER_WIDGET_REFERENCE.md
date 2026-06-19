# Blogger Widget Reference

Complete documentation of all Blogger widget types used across the repository.

---

## 1. Blog Widget (`type='Blog'`)

The core widget that renders blog posts.

### XML Registration

```xml
<b:widget id='Blog1' locked='false' title='Blog Posts' type='Blog' version='2'>
  <b:includable id='main' var='top'>
    <!-- Override default post rendering -->
  </b:includable>
</b:widget>
```

### Available Data (Inside `main` includable)

| Data Variable | Type | Description |
|--------------|------|-------------|
| `data:posts` | Collection | All posts in current view |
| `data:newerPageUrl` | URL | Newer posts page URL |
| `data:newerPageTitle` | String | Newer page title |
| `data:olderPageUrl` | URL | Older posts page URL |
| `data:olderPageTitle` | String | Older page title |
| `data:top` | Object | Top-level widget data |
| `data:view.isMultipleItems` | Boolean | Index/archive/search/label |
| `data:view.isSingleItem` | Boolean | Single post/page |
| `data:posts.empty` | Boolean | No posts found |

### Overridable Includables

Override these to customize specific parts without rewriting the entire widget:

```xml
<b:includable id='main' var='top'>        <!-- Main rendering -->
<b:includable id='postTitle' var='post'>   <!-- Post title -->
<b:includable id='postBody' var='post'>    <!-- Post body -->
<b:includable id='postMeta' var='post'>    <!-- Post metadata -->
<b:includable id='postAuthor' var='post'>  <!-- Author display -->
<b:includable id='postTimestamp' var='post'><!-- Date display -->
<b:includable id='postLabels' var='post'>  <!-- Labels display -->
<b:includable id='postCommentsLink'/>      <!-- Comments link -->
<b:includable id='postShareButtons' var='post'/><!-- Share buttons -->
<b:includable id='postReactions'/>         <!-- Reactions -->
<b:includable id='postJumpLink' var='post'/><!-- Read more -->
<b:includable id='postFooterByline' var='post'/><!-- Footer byline -->
<b:includable id='feedLinks'/>             <!-- RSS/Atom links -->
<b:includable id='blogPager'/>             <!-- Full pagination -->
<b:includable id='previousPageLink'/>      <!-- Newer link -->
<b:includable id='nextPageLink'/>          <!-- Older link -->
<b:includable id='headerByline'/>          <!-- Header byline -->
<b:includable id='footerBylines'/>         <!-- Footer bylines -->
<b:includable id='postShareButtons'/>      <!-- Share buttons -->
<b:includable id='snippetedPosts'/>        <!-- Snippeted post view -->
<b:includable id='snippetedPostContent'/>  <!-- Snippet content -->
<b:includable id='snippetedPostThumbnail'/><!-- Snippet thumbnail -->
<b:includable id='snippetedPostTitle'/>    <!-- Snippet title -->
<b:includable id='snippetedPostByline'/>   <!-- Snippet byline -->
<b:includable id='postCommentsLink'/>      <!-- Comments link -->
<b:includable id='commentsLink'/>          <!-- Comments link alt -->
<b:includable id='commentsLinkIframe'/>    <!-- Comments iframe -->
<b:includable id='emailPostIcon'/>         <!-- Email icon -->
<b:includable id='facebookShare'/>         <!-- Facebook share -->
<b:includable id='googlePlusShare'/>       <!-- Google+ share -->
<b:includable id='linkShare'/>             <!-- Link share -->
<b:includable id='otherSharingButton'/>    <!-- Other share -->
<b:includable id='platformShare'/>         <!-- Platform share -->
<b:includable id='bylineByName'/>          <!-- Byline region -->
<b:includable id='bylineRegion'/>          <!-- Byline region alt -->
<b:includable id='blogThisShare'/>         <!-- BlogThis share -->
<b:includable id='postLocation'/>          <!-- Location data -->
<b:includable id='sharingButton'/>         <!-- Share button -->
<b:includable id='sharingButtonContent'/>  <!-- Share button content -->
<b:includable id='sharingButtons'/>        <!-- Share buttons container -->
<b:includable id='sharingButtonsMenu'/>    <!-- Share menu -->
<b:includable id='sharingPlatformIcon'/>   <!-- Platform icon -->
<b:includable id='scriptTime' var='post'/> <!-- Reading time script -->
```

### Disabling Built-in Features

To disable a feature without breaking the widget:
```xml
<b:includable id='postShareButtons'><b:comment>Disabled</b:comment></b:includable>
```

### Post Data Reference

```xml
data:post.title              — Post title
data:post.body               — Full body HTML
data:post.url                — Post URL
data:post.url.canonical      — Canonical URL
data:post.date               — Formatted date
data:post.date.iso8601       — ISO 8601 date
data:post.author.name        — Author name
data:post.authorUrl          — Author URL
data:post.author.authorPhoto.image — Author photo URL
data:post.featuredImage      — Featured image URL
data:post.featuredImage.isYouTube — Boolean
data:post.featuredImage.youtubeMaxResDefaultUrl — YouTube thumbnail
data:post.firstImageUrl      — First image in post
data:post.labels             — Label collection
data:post.labels.any         — Has labels?
data:post.labels.first.name  — First label name
data:post.numberOfComments   — Comment count
data:post.allowComments      — Comments enabled?
data:post.allowNewComments   — New comments allowed?
data:post.embedCommentForm   — Embedded comment form?
data:post.snippets.short snippet { length: N } — Truncated snippet
data:post.id                 — Post ID
data:post.commentHtml        — Rendered comments HTML
data:post.commentJso         — Comments JSON
data:post.commentMsgs        — Comments messages
data:post.commentConfig      — Comments config
data:post.commentSrc         — Comments script source
data:post.appRpcRelayPath    — RPC relay path
data:post.cmtfpIframe        — Comment form iframe
data:post.noNewCommentsText  — No new comments text
```

### Failure Cases

| Issue | Symptom | Fix |
|-------|---------|-----|
| Missing `main` includable | Widget shows nothing | Add `<b:includable id='main'>` |
| Broken pagination | No newer/older links | Check `data:newerPageUrl` and `data:olderPageUrl` conditions |
| Post body not rendering | Empty post | Ensure `<data:post.body/>` is inside the loop |
| Featured image not showing | Broken image | Use `data:post.featuredImage` with ternary fallback |

---

## 2. PopularPosts Widget (`type='PopularPosts'`)

### XML Registration

```xml
<b:widget id='PopularPosts1' locked='false' title='Popular Posts' type='PopularPosts' version='2' visible='true'>
  <b:widget-settings>
    <b:widget-setting name='numItemsToShow'>5</b:widget-setting>
    <b:widget-setting name='showThumbnails'>true</b:widget-setting>
    <b:widget-setting name='showSnippets'>true</b:widget-setting>
    <b:widget-setting name='timeRange'>LAST_YEAR</b:widget-setting>
  </b:widget-settings>
  <b:includable id='main' var='this'>
    <b:include name='widget-title'/>
    <div class='widget-content'>
      <b:loop values='data:posts' var='post'>
        <b:include data='post' name='content'/>
      </b:loop>
    </div>
  </b:includable>
  <b:includable id='content' var='post'>
    <!-- Post rendering -->
  </b:includable>
</b:widget>
```

### Widget Settings

| Setting | Values | Description |
|---------|--------|-------------|
| `numItemsToShow` | 1-10 | Number of posts shown |
| `showThumbnails` | true/false | Show post thumbnails |
| `showSnippets` | true/false | Show text snippets |
| `timeRange` | `LAST_WEEK`, `LAST_MONTH`, `LAST_YEAR`, `ALL_TIME` | Time filter |

### Available Data (Inside loop)

| Variable | Description |
|----------|-------------|
| `data:post.title` | Post title |
| `data:post.url` | Post URL |
| `data:post.date` | Post date |
| `data:post.featuredImage` | Featured image |
| `data:post.firstImageUrl` | First image |
| `data:post.snippets.short` | Short snippet |
| `data:post.author.name` | Author name |
| `data:post.numberOfComments` | Comment count |

### Section-Based Conditional Rendering (Pikitemplates Pattern)

```xml
<b:if cond='data:widget.sectionId == &quot;hot-posts&quot;'>
  <!-- Breaking ticker layout -->
<b:elseif cond='data:widget.sectionId == &quot;ft-post&quot;'/>
  <!-- Featured grid layout -->
<b:else/>
  <!-- Sidebar list layout -->
</b:if>
```

### Failure Cases

| Issue | Symptom | Fix |
|-------|---------|-----|
| No posts showing | Empty widget | Ensure at least one post exists and is published |
| Thumbnails not showing | Missing images | Set `showThumbnails` to true in settings |
| Wrong time range | Unexpected posts | Check `timeRange` setting |

---

## 3. Label Widget (`type='Label'`)

### XML Registration

```xml
<b:widget id='Label1' locked='false' title='Labels' type='Label' version='2' visible='true'>
  <b:widget-settings>
    <b:widget-setting name='sorting'>ALPHA</b:widget-setting>
    <b:widget-setting name='display'>LIST</b:widget-setting>
    <b:widget-setting name='selectedLabelsList'>All</b:widget-setting>
    <b:widget-setting name='showType'>ALL</b:widget-setting>
    <b:widget-setting name='showFreqNumbers'>true</b:widget-setting>
  </b:widget-settings>
  <b:includable id='main' var='this'>
    <b:include name='widget-title'/>
    <b:include name='content'/>
  </b:includable>
  <b:includable id='content'>
    <div class='widget-content'>
      <b:loop values='data:labels' var='label'>
        <a expr:href='data:label.url'>
          <data:label.name/>
          <b:if cond='data:label.count'>
            <span>(<data:label.count/>)</span>
          </b:if>
        </a>
      </b:loop>
    </div>
  </b:includable>
  <b:includable id='cloud'>
    <!-- Cloud/3D view style -->
  </b:includable>
</b:widget>
```

### Widget Settings

| Setting | Values | Description |
|---------|--------|-------------|
| `sorting` | `ALPHA`, `FREQUENCY` | Sort order |
| `display` | `LIST`, `CLOUD` | Display style |
| `selectedLabelsList` | String | Selected labels |
| `showType` | `ALL`, `SELECTED` | Filter type |
| `showFreqNumbers` | true/false | Show post count |

### Available Data (Inside loop)

| Variable | Description |
|----------|-------------|
| `data:label.name` | Label name |
| `data:label.url` | Label page URL |
| `data:label.count` | Post count (can be undefined) |

### Failure Cases

| Issue | Symptom | Fix |
|-------|---------|-----|
| `data:label.count` undefined | Count not showing | Wrap in `<b:if cond='data:label.count'>` |
| Labels not linking | Broken URLs | Use `expr:href='data:label.url'` |

---

## 4. Header Widget (`type='Header'`)

### XML Registration

```xml
<b:widget id='Header1' locked='false' title='Blog Header' type='Header' version='2' visible='true'>
  <b:includable id='main' var='this'>
    <div class='header-widget'>
      <b:include cond='data:imagePlacement in {&quot;REPLACE&quot;, &quot;BEFORE_DESCRIPTION&quot;}' name='image'/>
      <b:include cond='data:imagePlacement == &quot;BEHIND&quot;' name='title'/>
    </div>
  </b:includable>
  <b:includable id='image'>
    <a class='header-image-wrapper' expr:href='data:blog.homepageUrl'>
      <img expr:alt='data:blog.title.escaped' expr:data-height='data:height' expr:data-width='data:width' expr:src='data:image'/>
    </a>
  </b:includable>
</b:widget>
```

### Available Data

| Variable | Description |
|----------|-------------|
| `data:image` | Header image URL |
| `data:imagePlacement` | `REPLACE`, `BEFORE_DESCRIPTION`, `BEHIND` |
| `data:height` | Image height |
| `data:width` | Image width |

---

## 5. LinkList Widget (`type='LinkList'`)

Used for menus and social links.

### XML Registration

```xml
<b:widget id='LinkList1' locked='false' title='Menu' type='LinkList' version='2' visible='true'>
  <b:widget-settings>
    <b:widget-setting name='link-0'>https://example.com</b:widget-setting>
    <b:widget-setting name='text-0'>Home</b:widget-setting>
    <b:widget-setting name='sorting'>NONE</b:widget-setting>
  </b:widget-settings>
  <b:includable id='main'>
    <b:include name='content'/>
  </b:includable>
  <b:includable id='content'>
    <div class='widget-content'>
      <ul>
        <b:loop values='data:links' var='link'>
          <li><a expr:href='data:link.target'><data:link.name/></a></li>
        </b:loop>
      </ul>
    </div>
  </b:includable>
</b:widget>
```

### Available Data (Inside loop)

| Variable | Description |
|----------|-------------|
| `data:link.name` | Link display text |
| `data:link.target` | Link URL |
| `data:link.length` | Number of links |

### Failure Cases

| Issue | Symptom | Fix |
|-------|---------|-----|
| Links not showing | Empty widget | Add links via Layout editor |
| Wrong sort order | Unexpected order | Set `sorting` to `NONE` |

---

## 6. ContactForm Widget (`type='ContactForm'`)

### XML Registration

```xml
<b:widget id='ContactForm1' locked='true' title='Contact Form' type='ContactForm' version='2' visible='true'>
  <b:includable id='main'>
    <div class='contact-form-widget'>
      <form name='contact-form'>
        <input class='contact-form-name' 
               expr:id='data:widget.instanceId + &quot;_contact-form-name&quot;'
               expr:placeholder='data:contactFormNameMsg' 
               name='name' type='text'/>
        <input class='contact-form-email' 
               expr:id='data:widget.instanceId + &quot;_contact-form-email&quot;'
               expr:placeholder='data:contactFormEmailMsg + &quot;*&quot;' 
               name='email' type='text'/>
        <textarea class='contact-form-email-message' 
                  expr:id='data:widget.instanceId + &quot;_contact-form-email-message&quot;'
                  expr:placeholder='data:contactFormMessageMsg + &quot;*&quot;' 
                  name='email-message' rows='5'/>
        <input class='contact-form-button contact-form-button-submit' 
               expr:id='data:widget.instanceId + &quot;_contact-form-submit&quot;'
               expr:value='data:contactFormSendMsg' type='button'/>
        <div style='text-align: center; width: 100%; margin-top: 1rem;'>
          <p class='contact-form-error-message' 
             expr:id='data:widget.instanceId + &quot;_contact-form-error-message&quot;'/>
          <p class='contact-form-success-message' 
             expr:id='data:widget.instanceId + &quot;_contact-form-success-message&quot;'/>
        </div>
      </form>
    </div>
  </b:includable>
</b:widget>
```

### Available Data

| Variable | Description |
|----------|-------------|
| `data:contactFormNameMsg` | "Name" placeholder text |
| `data:contactFormEmailMsg` | "Email" placeholder text |
| `data:contactFormMessageMsg` | "Message" placeholder text |
| `data:contactFormSendMsg` | "Send" button text |
| `data:widget.instanceId` | Unique widget ID (used to prefix form element IDs) |

### Critical Requirements

1. **Widget must be in a section with `showaddelement='yes'`** (or placed directly)
2. **Form field IDs must be unique** — use `data:widget.instanceId` prefix
3. **Error and success message elements require `expr:id`** matching Blogger's expected pattern
4. **Hidden-widget-container pattern**: Place a second ContactForm in hidden section for item page access

### Hidden Widget Pattern (Required for Single Post Pages)

```xml
<b:if cond='data:view.isSingleItem'>
  <div id='hidden-widget-container' style='display:none'>
    <b:section class='hidden-widgets' deleted='true' id='hidden-widgets' maxwidgets='2' showaddelement='no'>
      <b:widget id='ContactForm1' locked='true' title='Contact form' type='ContactForm' version='2' visible='true'>
        <!-- Same as above -->
      </b:widget>
    </b:section>
  </div>
</b:if>
```

Without this pattern, ContactForm breaks on single post pages.

### Failure Cases

| Issue | Symptom | Fix |
|-------|---------|-----|
| Form not showing | Missing form HTML | Ensure widget has `main` includable |
| Submit not working | No email sent | Check hidden-widget pattern is correct |
| Error message not rendering | No feedback | Ensure `contact-form-error-message` has correct expr:id |
| Duplicate IDs | JS conflicts | Use `data:widget.instanceId` for all form IDs |

---

## 7. HTML Widget (`type='HTML'`)

Used for custom HTML/JavaScript content in sidebar or footer.

### XML Registration

```xml
<b:widget id='HTML1' locked='false' title='Custom HTML' type='HTML' version='2' visible='true'>
  <b:widget-settings>
    <b:widget-setting name='content'><![CDATA[
      <!-- Custom HTML here -->
      <p>Your custom content</p>
    ]]></b:widget-setting>
  </b:widget-settings>
  <b:includable id='main'>
    <b:include name='widget-title'/>
    <div class='widget-content'>
      <data:content/>
    </div>
  </b:includable>
</b:widget>
```

### Available Data

| Variable | Description |
|----------|-------------|
| `data:content` | CDATA content from widget settings |
| `data:title` | Widget title |

---

## 8. FeaturedPost Widget (`type='FeaturedPost'`)

### XML Registration

```xml
<b:widget id='FeaturedPost1' locked='false' title='Featured Post' type='FeaturedPost' version='2' visible='true'>
  <b:includable id='main' var='this'>
    <b:include name='widget-title'/>
    <div class='widget-content'>
      <b:loop values='data:posts' var='post'>
        <b:include data='post' name='postContent'/>
      </b:loop>
    </div>
  </b:includable>
  <b:includable id='postContent' var='post'>
    <!-- Single featured post display -->
  </b:includable>
</b:widget>
```

### Available Data

Same as PopularPosts content variables.

### Section-Specific Rendering

Like PopularPosts, FeaturedPost can use `data:widget.sectionId` for different layouts based on placement.

---

## 9. Profile Widget (`type='Profile'`)

### XML Registration

```xml
<b:widget id='Profile1' locked='false' title='About Me' type='Profile' version='2' visible='true'>
  <b:includable id='main' var='this'>
    <b:include name='widget-title'/>
    <b:include name='content'/>
  </b:includable>
  <b:includable id='content'>
    <b:if cond='data:team'>
      <div class='widget-content team'><b:include name='teamProfile'/></div>
    <b:else/>
      <div class='widget-content individual'><b:include name='userProfile'/></div>
    </b:if>
  </b:includable>
</b:widget>
```

### Available Data

| Variable | Description |
|----------|-------------|
| `data:team` | Boolean, multi-author blog? |
| `data:authors` | Collection (team mode) |
| `data:displayname` | Display name |
| `data:aboutme` | About text |
| `data:location` | Location |
| `data:userUrl` | Profile URL |
| `data:authorPhoto.image` | Photo URL |
| `data:authorPhoto.height` | Photo height |
| `data:authorPhoto.width` | Photo width |

---

## 10. BlogArchive Widget (`type='BlogArchive'`)

### XML Registration

```xml
<b:widget id='BlogArchive1' locked='false' title='Archives' type='BlogArchive' version='2' visible='true'>
  <b:widget-settings>
    <b:widget-setting name='showStyle'>HIERARCHY</b:widget-setting>
    <b:widget-setting name='frequency'>MONTHLY</b:widget-setting>
    <b:widget-setting name='showPosts'>true</b:widget-setting>
  </b:widget-settings>
  <b:includable id='main'>
    <b:include name='widget-title'/>
    <b:include name='content'/>
  </b:includable>
</b:widget>
```

### Settings

| Setting | Values | Description |
|---------|--------|-------------|
| `showStyle` | `FLAT`, `HIERARCHY`, `MENU` | Display style |
| `frequency` | `MONTHLY`, `YEARLY` | Grouping |
| `showPosts` | true/false | Show post count |
| `chronological` | true/false | Chronological order |
| `showWeekEnd` | true/false | Show week end |
| `yearPattern` | string | Year format pattern |
| `monthPattern` | string | Month format pattern |
| `weekPattern` | string | Week format pattern |
| `dayPattern` | string | Day format pattern |

---

## 11. BlogSearch Widget (`type='BlogSearch'`)

### XML Registration

```xml
<b:widget id='BlogSearch1' locked='false' title='Search' type='BlogSearch' version='2' visible='true'>
  <b:includable id='main'>
    <b:include name='widget-title'/>
    <div class='widget-content'>
      <form expr:action='data:blog.homepageUrl + &quot;search&quot;' method='get'>
        <input name='q' type='text' placeholder='Search...'/>
        <button type='submit'>Search</button>
      </form>
    </div>
  </b:includable>
</b:widget>
```

---

## 12. PageList Widget (`type='PageList'`)

Used for page navigation.

```xml
<b:widget id='PageList1' locked='false' title='Pages' type='PageList' version='2' visible='true'>
  <b:widget-settings>
    <b:widget-setting name='pagesToShow'>10</b:widget-setting>
    <b:widget-setting name='sorting'>NONE</b:widget-setting>
  </b:widget-settings>
  <b:includable id='main'>
    <b:include name='content'/>
  </b:includable>
</b:widget>
```

---

## 13. Image Widget (`type='Image'`)

```xml
<b:widget id='Image1' locked='false' title='' type='Image' version='2' visible='true'>
  <b:includable id='main'>
    <b:if cond='data:sourceUrl != &quot;&quot;'>
      <img expr:alt='data:title' expr:src='data:sourceUrl'/>
    <b:else/>
      <img alt='Fallback' src='placeholder.png'/>
    </b:if>
  </b:includable>
</b:widget>
```

---

## 14. Text Widget (`type='Text'`)

```xml
<b:widget id='Text1' locked='false' title='Text' type='Text' version='2' visible='true'>
  <b:includable id='main'>
    <b:include name='widget-title'/>
    <div class='widget-content'>
      <data:content/>
    </div>
  </b:includable>
</b:widget>
```

---

## 15. TextList Widget (`type='TextList'`)

```xml
<b:widget id='TextList1' locked='false' title='List' type='TextList' version='2' visible='true'>
  <b:includable id='main'>
    <b:include name='widget-title'/>
    <div class='widget-content'>
      <ul>
        <b:loop values='data:texts' var='text'>
          <li><data:text/></li>
        </b:loop>
      </ul>
    </div>
  </b:includable>
</b:widget>
```

---

## Widget Coverage Checklist (for New Theme)

| Widget | Required? | Purpose |
|--------|-----------|---------|
| Blog | REQUIRED | Main content |
| Header | REQUIRED | Blog logo/title |
| PopularPosts | RECOMMENDED | Related/sidebar content |
| Label | RECOMMENDED | Category navigation |
| LinkList | RECOMMENDED | Menus, social links |
| ContactForm | RECOMMENDED | Contact functionality |
| FeaturedPost | OPTIONAL | Hero content |
| Profile | OPTIONAL | Author widget |
| BlogArchive | OPTIONAL | Archive navigation |
| BlogSearch | OPTIONAL | Search functionality |
| PageList | OPTIONAL | Page navigation |
| HTML | OPTIONAL | Custom ads/content |
| Image | OPTIONAL | Static images |
| Text | OPTIONAL | Static text |
| TextList | OPTIONAL | Simple lists |
