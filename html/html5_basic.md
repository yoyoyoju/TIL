# HTML5

### css

```html
<link rel="stylesheet" href="css.css">
```


### script

in the `<body>` after other contents
```html
<script src="src.js"></script>
```

### layout

```html
<body>
    <header>
        <nav>
            Navigation
        </nav>
    </header>
    <section>
        <main>
            <article>
                <figure>
                    <img src="image.jpg" alt="image"/>
                    <figcaption>
                        caption for the image
                    </figcaption>
                </figure>
                <video src="https://ww.something.com/video.mp4" controls autoplay muted loop preload width="600" height="350">
            </article>
            <article>
                <video controls autoplay muted loop preload width="600" height="350">
                    <source src="https://ww.something.com/video.mp4" 
                    type="video/mp4">
                    <source src="https://ww.something.com/video.ogg" 
                    type="video/ogg">
                </video>
                <div class="vid">
                    <iframe width="600" height="350" src="https://somesite.com"></iframe>
                </div>
            </article>

            <article>
            </article>
        </main>
        <aside>
        </aside>
    </section>
    <footer>
    </footer>
</body>
```


