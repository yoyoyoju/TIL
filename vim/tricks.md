# Vim Tricks

from the talk [From Vim Muggle to Wizard](https://youtu.be/MquaityA1SM)


### Regex
To count how many matchs:
`:%s/jabberwock//gn`
`n` means do not really to the substitution

`:help regex`

### Mark

- Mark with m
    - mark with lower letter: within file
    - mark with upper: you can come back from another file

- vim automatically marks 
    - the boundaries of the chunk of text you previously changed or yanked as `[`, `]`
    - the boundaries of your last visual selection as `<`, `>`

`:help marks`


### Command line

- how to target text
    - `{number}` an absolute line number
    - `.` the current line
    - `$` the last line in the file
    - `%` equal to 1,$ (the entire file)
    - `'t` position of mark t
    - `/{pattern}[/]` the next line where {pattern} matches
    - `?{pattern}[?]` the previous line where {pattern} matches
    - give a direction `+` or `-` followed by a number
        - `:'am/\sFortunately/-1` 
            move the line with mark a to the one line above Fortunately
        - `:/\sFor example/m/\sFortunately/+3`
            move the line with "For example" three lines after "Fortunately"
`:help range`
Ctrl-F on command line history, edit and enter to excute it.


### Registers

- default register is `""` register or `0` register
    - `"jdd` delete a line and keep it "j register -> `"jp` paste it back
    - use as normal mode command by `@j` when `j` is the name of register
- Registers "1-9 keep track of last nine delete operations.

- example
    - `03wcWmy good^[j`
        - `^[` is like esc

`:help registers`


### Commands

- Can use external commands in the command line as `:!{cmd}`
- `:.!{cmd}` uses the current line(`.` range) as arguments to {cmd}
    and replaces the current line with {cmd}'s output

- in normal-mode us `!!{cmd}`
    - example run shell `!!sh` on a command I want to use
    - generate hexadecimal number from 0 to 255 (do `!!sh` on next line)

        seq 0 255 | xargs printf '%02x\n' | fmt -w 49

- For further reading, [blog](http://blog.sanctum.geek.nz/series/unix-as-ide/)
- `:help :read!`, `:help filter`


### Split

- `Ctrl-w + h,j,k,l` to move arround
- `Ctrl-w + s` to split current file
- `Ctrl-w + v` for vertical split
- `Ctrl-w + o` makes the current split the only one
- `Ctrl-w + c` to close the current one


### Visual

- `1<Ctrl-v>` to redraw visual block
    - the [count] multiplies the width and height
- When visual block is selected
    - `<Ctrl-v>I` to insert in the beginning of the block
    - `<Ctrl-v>A` to append at the end of the block
- `:help visual` `:help visual-block`


### Auto-complete

- insert mode completion `<Ctrl-n>`
- `<Ctrl-x><Ctrl-f>` filenames
- `<Ctrl-x>s` for spelling alternatives
- `<Ctrl-x><Ctrl-v>` vim keywords (best in the command-line window)
- `<Ctrl-x><Ctrl-l>` completely finishes an entire line
- `:help ins-completion`


### Text Objects

can use `i` for inner, `a` for all

    "quoted" 'string' `literals`,

    [brackets],

    (parens),

    <Tags>
        <markup type="XML">
            <nested/>
        </markup>
    </Tags>

    {
        blocks.of($source, 'code');
    }

- `help text-objects`
