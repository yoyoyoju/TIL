# FILE BROWSING

### no plug-in

* `:!ls -lF`: list directory
* `:find path/to/file.txt` to open files
* `:vs path/to/file.txt` to open in a vertical split
* `:sp path/to/file.txt` to open in a horizontal split
* `:tabnew path/to/file.txt` to open in a new tab


### netrw

* `:Explore` to open `netrw` in the current window
* `:Sexplore` or `:Sex` to open `netrw` in a horizontal split
* `:Vexplore` or `:Sex` to open `netrw` in a vertical split


#### using netrw

* change view type by `i` in the directory browser
* remove directory banner `I`
* to exit from dir browser without selecting a file: 
    * `:bd` buffer delete
    * `:bw` buffer wipe


#### setting up netrw

In `.vimrc` file,
* `let g:netrw_liststyle = 3`
    * 0: thin, 1: long, 2: wide, 3: tree
* `let g:netrw_banner = 0` remove the banner
* change how the file opens
    * `let g:netrw_browse_split = 2`
    * 1: in horizontal split
    * 2: in a vertical split
    * 3: in a new tab
    * 4: in previous window
* set the width of the dir explorer
    * `let g:netrw_winsize = 25` set it 25%

Example setup

    let g:netrw_banner = 0
    let g:netrw_liststyle = 3
    let g:netrw_browse_split = 4
    let g:netrw_altv = 1            " open splits to the right
    let g:netrw_winsize = 25
    augroup ProjectDrawer
      autocmd!
      autocmd VimEnter * :Vexplore
    augroup END


