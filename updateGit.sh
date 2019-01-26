#!/bin/bash

# usage
# bash updateGit.sh "comment to commit"

# a script to update TIL directory
# 1. update README file by generateREADME.py
# 2. git add
# 3. git commit: the argument as the message or generate automated message from git status
# 4. git push to the origin master

python3 generateREADME.py

git add .

# check argument:
if [ "$#" -gt 0 ]; then
    git commit -m "$1"
else
    git status --porcelain \
    | git commit -F -
fi

git push
