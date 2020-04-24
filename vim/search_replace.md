### search and replace
g is for global: in all lines
```vim
:%s/foo/bar/g
```

### grep

- `:vim /something to search/ %`: search from current file
    - navigate with `:cn`, `:cp` and `:cl`
    - repeat comman with `@:`
    - `cd` do something with every occurance
    - `cdo s/TODO/DONE/g` replace for every occurance on every line

- `:args **/*.py` to add all `py` file into my arg list
- `:vim /somthing/ ##`: search from all my arg list


- prefix regexes with `\v` 
    - `\v\d+`
    - `\vfoo|bar`
