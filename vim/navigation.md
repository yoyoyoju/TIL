# vim navigation


### move cursor 

- H: top line of the screen (High)
- M: middle line of the screen (Middle)
- L: last line of the screen (Low)
- zz: center the current line (= z.)
- zt: put the current line to the top of the screen
- zb: put the current line to the bottom of the screen
- n%: go to n% point of the file, where n is a number (like 10%)
- ctrl + o: move back to where you were


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
