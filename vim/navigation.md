# vim navigation


### move cursor 

- H: top line of the screen (High)
- M: middle line of the screen (Middle)
- L: last line of the screen (Low)
- zz: center the current line (= z.)
- zt: put the current line to the top of the screen
- zb: put the current line to the bottom of the screen
- n%: go to n% point of the file, where n is a number (like 10%)
- ctrl + o / ctrl + i: cycle through `:jumps`
- g; / g,: cycle through `:changes`
- gf: to go to the file under the cursor


### scroll

- ctrl + e: scroll down without moving cursor 
- ctrl + y: scroll up without moving cursor 
    - combine them with number (10 ctrl E) to move multiple lines
- ctrl + D: move half a screen down
- ctrl + U: move half a screen up
- ctrl + F: move full screen down
- ctrl + B: move full screen up


### move within a line

- 0: to the beginning of a line
- $: to the ending of a line
- ^: to the first non-blank character
- g_: to the last non-blank character
- f, F, t, T: forward, until a alphabet (for example fx)
- ; : to repeat f and t movement


### search

- *: searches the current word and goes to the next occurence of it
- #: backward


### wordwise

- w: 'small' word 
- W: 'big' word (this is a-word-together another-thing)
- e,E,b,B: the same for end, backward
- ge: move backwards to the end of the prev word


### mark

- mm: set a mark as 'm' (as the second alphabet)
- \`m: to the marked point
- 'm: first character of the marked line


### paragraphs

- (, ): jump between sentences
- {, }: jump between paragraphs
- [{, ]}: jump to opening/ closing bracket in {  } block
- [(, ]): jump to opening/ closing bracket in (  ) block 
- [#, ]#: jump to prev/ next #ifdef, #else, #endif
- [\*, [/, ]\*, ]/: jump to beginning/ end of a c style comment /\* \*/
- [m, ]m, [M, ]M: jump to beginning/ end of a next/ previous c++, java method


### parenthesis

- %: to the matching parenthesis


### buffers and args

- `:bn` go to next buffer
- `:b {filename}` go to buffer `{filename}`
- `:bd` delete current buffer
- `:buffers` or `:ls` print out all buffers
- `:bufdo {cmd}` execute `{cmd}` for all buffers
- `:n` go to the next file (based on arg list)
- `:prev` go to the prev file (based on arg list)
- `:arga {filename}` add `{filename}` to arg list
- `:argl {files}` make a local arg copy via `{files}`
- `:args` print out all arguments
- `:sall` split all args
- `:vert sall` vertically split all args


### windows

- `<Ctrl-w> s` split window
- `<Ctrl-w> v` split window vertically
- `<Ctrl-w> q` close window
- `<Ctrl-w> w` alternate window
- `<Ctrl-w> r` rotate window
- `<Ctrl-w> o` make the current split the only
- `:windo {cmd}` execute `{cmd}` for all windows
    - `:windo difft` diff for every file in the window
- `:sf {FILE}` split window and `:find {FILE}`
- `:vert {cmd}` make any split `{cmd}` be vertical


### tabs

- `gt` go to next tab
- `gT` go to prev tab
- `:tabc` close tab
- `:tabe` open tab
- `:tabo` close all other tabs
- `:tabf {filename}` to open a file in a new tab
