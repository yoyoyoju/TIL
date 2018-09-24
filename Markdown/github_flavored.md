# GitHub Flavored Markdown

### code blocks

#### without highlight

1. indent your code by four spaces:
```markdown
    def foo():
        if not bar:
            return True
```

2. use fenced code
`````
```
def foo():
    if not bar:
        return True
```
`````

#### with highlight

`````markdown
```python
def foo():
    if not bar:
        return True
```
`````

### double code blocks

Either combine indent and fenced or
`````markdown
    code
    ```
    fenced code
    ```
    more code
`````
increase the amount of backticks:
```````markdown
`````markdown
You can write and code like this:
```python
def foo():
    return True
```
`````
```````


### Task Lists
```markdown
- [x] @mentions, #refs, [links](), **formatting**, and <del>tags</del> supported
- [x] list syntax
- [x] complete item
- [ ] incomplete item
```
- [x] @mentions, #refs, [links](), **formatting**, and <del>tags</del> supported
- [x] list syntax
- [x] complete item
- [ ] incomplete item



