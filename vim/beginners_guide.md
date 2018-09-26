# A Biginner's Gui8de to Vim
about basic thing.

### basic movement

* `0`: to the beginning of the line.
* `$`: to the end of the line.
* `w`: forward one word.
* `b`: backward one word.
* `G`: end of the file.
* `gg`: beginning of the file.
* `` `. ``: move to the last edit.

can type numbers in front of these to make it multiple times:
`5w` or `10b`.


### edit

* `d`: starts delete operation. combine with movement.
* `dd`: delete the line.
* `dw`: delete word.
* `d0`: delete to the beginneing of the line.
* `d$`: delete to the end of the line.
* `dgg`: delete to the beginning of the fline.
* `dG`: delete to the end of the file.
* `u`: undo the last operation.
* `Ctrl-r`: redo the last undo.


### search and replace

#### search
* `/text`: search forward
* `?text`: search backward
* `n`: to the next instance
* `N`: to the previous instance

#### replace
* `%s/text/replacement/g`: search trough the entire document
* `c`: at the end to confirm


### highlight
* `v`: one character at a time
* `V`: one line at a time
* `Ctrl-v`: highlight by columns


### Copy and paste
* `y`: yank, use with movement commend.
* `d`: cut (delete but saved in the buffer)
* `p`: paste on current line
* `P`: paset after current line


### save and quit
* `:w`: save
* `:w filename`: save as filename
* `:q`: quit
* `ZZ`: save and quit

