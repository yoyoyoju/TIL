# HTML
(based on HTML5, [webpage](https://www.w3.org/TR/html52/introduction.html), Jan2019)

### quick intro
a basic HTML document example
```HTML
<!DOCTYPE html>
<html>
    <head>
        <title>Sample page</title>
    </head>
    <body>
        <h1>Sample page</h1>
        <p>This is a <a href="demo.html">simple</a> sample.</p>
        <!-- this is a comment-->
    </body>
</html>
```

* HTML documents consist of a tree of elements and test
    * each element is denoted by start tag (for example `<body>`) and an end tag (`</body>`)
    * elements can have attributes (for example `href` in `<a>` element)
        * `id`
        * `class`
        * `ismap` for the `img` element
        * `style`
        * `title` to attach subtextual explanation
        * `lang` identify the natural language
            `<span lang="fr">c'est la vie</span>`
        * `dir` language-related attribute, specify text direction
    * empty element (like `<br>`) cannot take content, it may not have an end tag
    * elements example: [(see more)](https://en.wikipedia.org/wiki/HTML#HTML_versions_timeline)
        * `<html>...</html>` define boundaries of the HTML document
        * `<head>...</head>` Header of the HTML document
        * `<title>...</title>` title (included in the head)
        * `<body>...</body>` document's body
        * `<h1>...</h2>` headings (h1 to h6)
        * `<p>...</p>` paragraphs (sections the page into paragraphs)
        * `<br>` line breaks (without altering the semantic structure of the page - empty element
        * `<a>` anchor
            * can create a link by using `href` attribute to hold the URL
        * `<form>` define a form (usually provides input field)
        * `<input>` inputs
            * `<input type>` define an input widget to a form
            * `<input type="text" />` for text input
            * `<input type="file" />` for uploading files
            * `<input type="checkbox" />` for checkboxes
        * `<!-- comment  -->` comment
        * `<b>...</b>` bold
        * `<i>...</i>` italic
        * `<strong>...</strong>` strong text
        * `<em>...</em>` emphasized text
        * `<img src="image.gif" alt="description" width="50" height="50" border="0">` image
        * `<abbr id="ID" class="jargon" style="color:purple;" title="HTML">HTML</abbr>` abbreviation element


### block inline
* block elements:
    * `<h1>`, `<h6>`, `<p>`, `<blockquote>`
    * display its own
* inline elements:
    * `<q>`, `<a>`, `<em>`


### void elements
* void elements
    * does not have any content
    * `<br>`, `<img>`


### more elements
* `<code>` to display code from a computer program
* `<time>` the content is a date or time
* `<strong>` toe emphasize with extra strength
* `<pre>` show the text exactly as I type it
