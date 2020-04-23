# Things you can do with just vim

from a lecture: [How to Do 90% of What Plugins Do](https://youtu.be/XA2WjJbmmoM)


### Finding Files

#### vimrc file

    " enable syntax and plugins
    syntax enable 
    filetype plugin on

    " FINDING FILES:

    " Search down into cubfolers
    " Provides tab completion for all file related tasks
    set path+=** " Search through nested sub-dirs

    " Display all matching files when we tab complete
    set wildmenu


#### Usage and comments

    " NOW WE CAN:
    " - Hit tab to :find by partial match
    " - Use * to make it fuzzy (like *.html and tab)

    " THINGS TO CONSIDER:
    " - :b lets you autocomplete any open buffer

- search with `:find FILENAME`
- tab and shift+tab to go through the file list
- `:ls` for list of 'buffers'
- `:b SUBSTRING_OF_FILE_IN_BUFFER` to go to the file 
    - like `:b tcp` to go to `tcp.rb`


### Tag Jumping

Need `ctags` installed in the system.
In macOS if ctags does not work, you might be using a wrong version.
Install ctags with homebrew or macports.


#### vimrc file

    " TAG JUMPING:

    " Create the `tags` file (may need to install ctags first)
    command! MakeTags !ctags -R . " the R flag means recursive


    " THINGS TO CONSIDER:
    " - This doesn't help if you want a visual list of tags


#### Usage and comments

The MakeTags will make `tags` file
Use the commands below 
when the files are opened in the same dir with `tags` file.
Or add the path into `tags`.
`:echo expand("%")` to print out the current file path.

`ctrl ]` to jump to tag and so on.
`g ctrl ]` when something is defined for more than twice.
`ctrl t` to jump back up a layer

    " NOW WE CAN:
    " - Use ^] to jump to tag under cursor
    " - Use g^] for ambiguous tags
    " - Use ^t to jump back up the tag stack


### Autocomplete

Documented in |ins-completion|
Type `:help ins-completion` for more information.

#### Usage

##### highlights

- `ctrl x ctrl n` for JUST this file
- `ctrl x ctrl f` for filenames (works with our path trick)
- `ctrl x ctrl ]` for tags only
- `ctrl n` for anything specified by the 'complete' option

- Use `ctrl n` and `ctrl p` to go back and forth in the suggestion list


##### complete option

To see the option `:set complete`.
The default is `complete=.,w,b,u,t,i`.
The `i` option scans all included files. When the path includes `**`,
it might take some time. To put the `i` out, use `:set complete-=i`

- `**`: any (recursive) directory
- you can use like `args **/*.yaml` to add all yaml file into the arg list


### File Browsing

    " FILE BROWSING:

    " Tweaks for browsing
    let g:netrw_banner=0        " disable annoyting banner
    let g:netrw_banner_split=4  " open in prior window
    let g:netrw_altv=1          " open splits to the right
    let g:netrw_liststyle=3     " tree view
    let g:netrw_list_hide=netrw_gitignore#Hide()
    let g:netrw_list_hide.=',\(^\|\s\s\)\zs\.\S\+'

    " NOW WE CAN:
    " - :edit a folder to open a file browser
    " - <CR>/v/t to open in an h-split/v-split/tab
    " - check |netrw-browse-maps| for more mappings


#### Usage

Use by `:edit .` or `:edit /path/to/open` to open file browser


### Snippets

Save a snippet in a path and make a key map
to read the snippet by a key stroke.

    " Read an empty HTML template and move cursor to title
    nnoremap ,html :read $HOME/.vim/snippets/html_skeleton.html<CR>3jwf>a
    " nnoremap ,html :-1read $HOME/.vim/snippets/html_skeleton.html<CR>3jwf>a
    " the -1 make it insert one line above

#### Usage

type `,html` in normal mode to insert the snippet


### Build Integration

see https://www.philipbradley.net/posts/rspec-into-vim-with-quickfix/

    " Configure the `make` command to run RSpec
    set makeprg=bundle\ exec\ rspec\ -f\ QuickfixFormatter

    " NOW WE CAN:
    " - Run :make to run RSpec
    " - :cl to list errors
    " - :cc# to jump to error by number
    " - :cn and :cp to navigate forward and back
    y"+a
    ":"
