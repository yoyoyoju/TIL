# Unix as IDE

[link to the original post](https://sanctum.geek.nz/arabesque/unix-as-ide-introduction/)

### Files

#### Listing Files

Use `ls` with:

* `-t` - in order of last modification date, newest first
* `-S` - sort by file size
* `-R` - list files recursively


##### Examples

    $ ls -tl | sed 10q  # list recent 10 files
    $ ls -tl | head     # can also use head
    $ ls -tlr           # add r for reverse order in time
    $ ls -Rl | less    # list files recursively in a pager
    $ ls -R | vi -     # pipe the output into vi


#### Finding Files

Use `find` to get a complete list of files including relative paths

    $ find .        # walk through all dir, files in current dir
    $ find . -ls    # and print it out in `ls -l` style

    # sort by the 11th column of output (the filenames)
    $ find . -ls | sort -k 11
    $ find . -ls | sort -k 9    # sort by the date

    # Filtering files
    $ find . -name '*.c'    # filter with file names matching a shell-style pattern
    $ find . -iname 'name.c'    # case-insensitive search
    $ find . -path '*test*' # find files with paths matching pattern
    $ find . -ipath '*test*'    # case-insensitive path matching
    $ find . -mtime -5      # find files edited within the last five days
    $ find . -mtime +5      # find files edited before five days ago
    $ find . -name '*.c' -mtime -2  # find c files edited in last two days
    $ find . -mtime -2 -ls | sort -k 11
    $ find . -newer server.c # find files newer than server.c
    $ find . -type d        # find directories
    $ find . -type f        # find files
    $ find . -type l        # find symbolic links


##### Actions on files

One can perform some actions on the files you found:

* `-delete` - delete matching files
* `-exec` - run an arbitrary command line on each file

For more information and example check out `man find`

##### Examples

    $ find . -name '*.pl' -exec perl -c {} \;

    # exec example:
    $ find . -exec echo {} \;           # echo all the results
    $ find . -type f -exec cat {} \;    # concatenate all the files 
        # it means cat file1; cat file2; ...
    $ find . -path '*test*' -exec grep somevar {} \; 

    # `+` for all of the results on one invocation
    $ find . -type f -exec diff {} +    # it only works there is two files
        # it means diff file1 file2

    # Open c files in vim
    $ find . -name '*.c' -exec vi {} +
        # then one can use `:vert sall` to open all the args vertically
        # put number like `:vert sall2` to set maximum number of window
    

#### Searching Files

Use `grep`.

Useful flags:
* `-R, -r`: recursively search
* `-F, --fixed-strings`: `fgrep` interpret pattern as a set of fixed strings
* `-i, --ignore-case`: case insensitive matching
* `-l, --files-with-matches`: only the name of matching files
* `-v`: invert match (select only those without given pattern
* `--exclude`: exclude with files with given filename pattern
* `--exclude-dir`: exclude given directory from searching (when -R)
    

##### examples

    # print head of the files in current dir, which contain someVar
    grep -lR someVar . | while IFS= read -r file; do
        head "$file"
    done

    # select all files with someVar except .svn files
    grep -R someVar. | grep -vF .svn
    grep -R --exclude '*\.svn' someVar .     # same with exclude

Find more examples in `man grep`


#### File metadata

The `file` tool gives you a one-line summary.

    # gives file info for everything in current directory
    $ find . -exec file {} \; 
