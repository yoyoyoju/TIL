# git status options

### output
`XY PATH`

* *for paths with merge conflicts*: `X` and `Y` show the modification states of each side.

* *without merge conflicts*: `X` - status of the index, `Y` - status of the work tree
    * `' '` unmodified
    * `M` modified
    * `A` added
    * `D` deleted
    * `R` renamed
    * `C` copied
    * `U` updated but unmerged

example:
* `AU`: unmerged, added by us
* `UA`: unmerged, added by them
* `DU`: unmerged, deleted by us
* `AA`: unmerged, both added
* `UU`: unmerged, both modified
* `??`: untracked


### ignore option
Ignored files are not listed, unless `--ignored` option is in effect.
`!!`: ignored file


### porcelain format
is guaranteed not to change in a backwards incompatible way between Git versions.
ideal for parsing by scripts.
use option `--porcelain`


### branch headers
`--branch` for information about the current branch

---------
reference: [git-scm](https://git-scm.com/docs/git-status)
