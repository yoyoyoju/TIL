# Bash shell expansion

The original post is [ here ](https://sanctum.geek.nz/arabesque/bash-shell-expansion/)

### Filename expansions

Filename expansions (globs)

* `*` wildcard
* `?`: for single character
* `[]`: for group of characters, or within a range

#### examples

    $ ls *.txt
    a.txt b.txt c.txt extra.txt

    $ ls ?.txt  # ? for single character
    a.txt b.txt c.txt

    $ ls [ac].txt  # a or c
    a.txt c.txt

    $ ls [a-c].txt # range from a to c
    a.txt b.txt c.txt


### Brace expansion

Brace expansion generates shell tokens.

#### examples

The basic examples:

    $ echo example{test,show,define,declare}
    exampletest exampleshow exampledefine exampledeclare

    # `..` separator syntax for ranges
    $ echo example{a..d}
    examplea exampleb examplec exampled
    $ echo example{1..5}
    example1 example2 example3 example4 example5


Use brace expansion to create, rename, copy, or move files:

    # create file1.txt file2.txt file3.txt file4.txt file5.txt file6.txt
    $ touch file{1..6}.txt

    # mv file.txt file.html
    $ mv file.{txt,html}

    # cp file.txt file.txt.bak
    $ cp file.txt{,.bak}

    # mv example.com/testing/index.html example.com/production/index.html
    $ mv example.com/{testing,production}/index.html


Use subversion branching and merging:

    # svn copy svn://server/project/trunk svn://server/project/branches/experimental
    $ svn copy svn://server/project/{trunk,branches/experimental}

    $ svn merge svn://server/project/{branches/experimental,trunk} .


Combine and nest these expansions:

    # To create directory tree
    $ mkdir -p {test,prod}/{,usr/,usr/local/}{etc,{,s}bin,lib,share}

    # the above line will create the following directories:
    test/etc
    test/bin
    test/sbin
    test/lib
    test/share
    test/usr/etc
    test/usr/bin
    test/usr/sbin
    test/usr/lib
    test/usr/share
    test/usr/local/etc
    test/usr/local/bin
    test/usr/local/sbin
    test/usr/local/lib
    test/usr/local/share
    prod/etc
    prod/bin
    prod/sbin
    prod/lib
    prod/share
    prod/usr/etc
    prod/usr/bin
    prod/usr/sbin
    prod/usr/lib
    prod/usr/share
    prod/usr/local/etc
    prod/usr/local/bin
    prod/usr/local/sbin
    prod/usr/local/lib
    prod/usr/local/share

