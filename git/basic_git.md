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
How to clone an existing repository: 
* `git clone <url>`: clone the url into a dir created after the repository name
* `git clone <url> <dirname>`: create a dir of dirname and clone the repository there
* This remote is named as `origin`
    * automatically sets my local master branch to track the (origin) remote master branch




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

* `git commit --amend`: this commit replaces the previous one. 
    * when I want to add something to the previous commit
* `git reset HEAD <file>`: unstage staged file
* `git checkout -- <file>`: discard changes, copy the unchanged file over current file.
    * the current change is lost. be careful to use it.




## remotes
remote repositories are versions of my project hosted on the internet or network somewhere.

### add, see, remove remotes
* To see it use `git remote` or `git remote -v` to see the URL.
* `git remote show <remote-name>`: to inspect
* `git remote add <shortname> <url>`: to add a remote
* `git remote rename <name-old> <name-new>`: rename remote name (its branch names too)
* `git remote rm <remote-name>`: remove the remote


### fetch and pull from remote
* `git fetch <shortname>`: to fetch from the remote. 
    * accessable locally.
    * does not automatically merge.
* `git fetch origin`: fetch from the origin remote
* `git pull`: fetch and merge from the corresponding remote branch to my current branch.


### push to remote
* `git push <remote-name> <branch-name>`: push commited data into remote
* `git push origin master`: push my master branch to my `origin` server




## tagging
* lightweight tag: pointer to a specific commit
* annotated tags: stored as full objects in the Git database. has all the information.
* `git tag`: to list the available tags
* `git show v1.4`: to show the tag data

### create tags
* `git tag -a v1.4 -m 'my version 1.4'`: create annotated tag (by `-a` flag)
* `git tag v1.4-lw`: create lightweight tag (no `-a`, `-s`, `-m` option)
* `git tag -a <tag> <commit-hash>`: tag onto previous commit ex)`git tag -a v1.2 9f232cb`


### share tags
* `git push <remote> <tag>`: push the tag (`git push` does not push tag by default)
* `git push <remote> --tags`: transfer all my tags




## Aliases

### set up aliases
set up aliases by using `git config`.

examples:
* `git config --global alias.ci commit`: to commit use `git ci` 
* `git config --global alias.unstage 'reset HEAD --'`: `git unstage fileA`
* `git config --global alias.last 'log -1 HEAD'`: `git last`
* to run external command use `!` character in front of it.
    * `git config --global alias.visual "!gitk"`


---------------
reference: PRO GIT
