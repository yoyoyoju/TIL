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


### Tables
Create table by hyphens `-` and pipe `|`.

```markdown
First Header | Second Header
-------------| -------------
cell1 | cell2
next  | next
```

First Header | Second Header
-------------| -------------
cell1 | cell2
next  | next


### SHA references
Used in descriptions and comments of Issues and Pull Requests.
SHA-1 hash into a link to that commit on GitHub.
```markdown
6e02119fa3b2c4cfc36be1a52c218af09661299a
yoyoyoju@6e02119fa3b2c4cfc36be1a52c218af09661299a
yoyoyoju/TIL/Markdown@6e02119fa3b2c4cfc36be1a52c218af09661299a
yoyoyoju/TIL/Markdown/github_flavored.md@6e02119fa3b2c4cfc36be1a52c218af09661299a
```

### Issue references within a repository
Used in descriptions and comments of Issues and Pull Requests.
refers the issue

```markdown
#1
yoyoyoju#1
```

### Username @mentions
notify that person to come and view the comment.
```markdown
@yoyoyoju
```
@yoyoyoju


### Strikethrough

```markdown
~~crossed out~~
```
~~crossed out~~



-------
reference: [GitHubGuides](https://guides.github.com/features/mastering-markdown/)

