# Vim as a Python IDE

- from a [this video](https://youtu.be/YhqsjUUHj6g)
- [repo](https://github.com/mbrochh/vim-as-a-python-ide)


### install

    # Prerequisites:
    # (Ubuntu) sudo apt-get build-dep vim
    # (OSX) Command Line Tools for Xcode

    $ hg clone https://vim.googlecode.com/hg/ vim
    $ vim/src
    $ ./configure --enable-pythoninterp --with-features=huge --prefix=$HOME/opt/vim
    $ make && make install
    $ mkdir -p $HOME/bin
    $ cd $HOME/bin
    $ ln -s $HOME/opt/vim/bin/vim
    $ which vim
    $ vim --version

    # on Ubuntu
    $ sudo apt-get install gtk2-engines-pixbuf


### vimrc

    " map sort function to a key
    vnoremap <Leader>s :sort<CR>

    " easier moving of code blocks
    " the block selection remains after indentation
    vnoremap < <gv
    vnoremap > >gv

to format a paragraph
in visual mode: `gq`
in normal mode: `gqap`

`Q` for Ex mode

    " no tab but space
    set tabstop=4
    set softtabstop=4
    set shiftwidth=4
    set shiftround
    set expandtab

    " search case insensitive
    set hlsearch    " highlight search
    set incsearch
    set ignorecase
    set smartcase

    " Disable backup and swap files
    set nobackup
    set nowritebackup
    set noswapfile
