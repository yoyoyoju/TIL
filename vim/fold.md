# fold
to do: add about the setting

### open and close folds
* `zc`: close the fold
* `zo`: open the fold
* `za`: toggle the fold
* `zC`, `zO`, `zA`: for all levels
* `zr`: open one more level (`zR` for all level)
* `zm`: close one more level (`zM` for all level)
* `zn`: to unfold everything
* `zi`: to toggle all folds
* `zd`: to delete a fold
* `ze`: to eliminate all folds


### automatic folding

create a fold according to some expression
below example creates a fold for each nested block structure

    :set foldexpr=strlen(matchstr(getline(v:lnum), '^-*'))
    :set foldmethod=expr
