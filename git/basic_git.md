# git basics

## git first settings

### git config
* `/etc/gitconfig`: for the system. use `--system` option
* `~/.gitconfig` or `~/.config/git/config`: for the user. use `--global`
* `.git/config`: in the git repository.

each level overrides values in the previous level


### first config
To set up git for the first time:
* `git config --global user.name "John Doe"`: set the user name
* `git config --global user.email "example@email.com"`: set the e-mail
* `git config --global core.editor vim`: default is generally vim
* `git config --list`: to check my settings
* `git config <key>`: like `git config user.name`




## getting a git repository

### initialize in an existing directory
How to initialize a repository in an existing directory:
```shell
$ git init
$ git add *.c
$ git add LICENSE
$ git commit -m 'first commit'
```

### clone
How to clone an existing repository
* `git clone <url>`: clone the url into a dir created after the repository name
* `git clone <url> <dirname>`: create a dir of dirname and clone the repository there




## basics

### record changes
* `git status`: to check the current status
    * `git status --short` or `git status -s`: to show simplified output
        [for more info](status_options.md)
* `git add <filename>`: added files are staged, "add this content to the next commit"
    * track new files
    * to stage file
    * mark merge-confliecte files as resolved
* .gitignore file: add to ignore certain files
    * `*.[oa]`, `*~`
    * lines starting with `#` are ignored
    * standard glob patterns work
    * end pattern with `/` for directory
    * negate by `!`
* `git diff`: to see the change that are unstaged
    * `git diff --staged`
    * `git diff --cached`: what I have staged so far
* `git commit`: commit staged changes
    * `-v`: show `git diff` results into the commit message
    * `-m`: specify commit message after the flag
    * `-a`: stage every already tracked file
* `git rm`: remove file
    * `-f`: force, when it was modified and added
    * `--cached`: keep the file but remove from tracking
    * `git rm log/\*.log`: remove .log files in `log/` directory (`\*~`)
* `git mv file_from file_to`:


### commit history

* `git log`: show the log
    * `-p`: show the diff
    * `-2`: limits the output to the last two entries
    * `--since=2.weeks` 
    * `--stat`: show abbreviated stats
    * `--pretty=oneline` or short, full, fuller
    * `--pretty=format:"%h - %an, %ar : %s"`
    * `--graph`: add graph showing the branch and merge history
    * `-S<str>`: only shows introduced or removed `<str>`


### undo

* `git commit -amend`: this commit replaces the previous one.
added
---------------
reference: PRO GIT
