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

SHA-1 hash into a link to that commit on GitHub
```markdown
6e02119fa3b2c4cfc36be1a52c218af09661299a
yoyoyoju@6e02119fa3b2c4cfc36be1a52c218af09661299a
yoyoyoju/TIL/Markdown@6e02119fa3b2c4cfc36be1a52c218af09661299a
yoyoyoju/TIL/Markdown/github_flavored.md@6e02119fa3b2c4cfc36be1a52c218af09661299a
```
6e02119fa3b2c4cfc36be1a52c218af09661299a
yoyoyoju@6e02119fa3b2c4cfc36be1a52c218af09661299a
yoyoyoju/TIL/Markdown@6e02119fa3b2c4cfc36be1a52c218af09661299a
yoyoyoju/TIL/Markdown/github_flavored.md@6e02119fa3b2c4cfc36be1a52c218af09661299a

16c999e8c71134401a78d4d46435517b2271d6ac
mojombo@16c999e8c71134401a78d4d46435517b2271d6ac
mojombo/github-flavored-markdown@16c999e8c71134401a78d4d46435517b2271d6ac


### Issue references within a repository

#1
mojombo#1
mojombo/github-flavored-markdown#1

### Username @mentions
```markdown
@yoyoyoju
```
@yoyoyoju