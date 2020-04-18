# Vim language

reference: https://youtu.be/wlR5gYd6um0

### repeat

dot(`.`) for repeat the previous command

### Verbs in Vim

- `d`: Delete
- `c`: Change 
- `>`: Indent
- `v`: Visually select
- `y`: Yank


### Nouns

#### Nouns in Vim -- Motions

- `w`: word
- `b`: back (back by a "word")
- `2j`: down 2 lines

#### Nouns in Vim -- Text Objects

- `iw`: inner word
- `it`: inner tag (content of xml or html tags)
- `i"`: inner quotes
- `ip`: inner paragraph
- `as`: a sentence

Usage example:
Type `di"` when the cursor is inside of a quotes 
will delte everything in the quotes.

#### Nouns in Vim -- Parameterized Text Objects

- `f, F`: "find" the next character (including the character)
- `t, T`: "find" the next character (excluding the character)
- the capital letters (`F`, `T`) goes backward
- `/`: Search (up to the next match)

Usage example:
Type `c/Search` will delete everything upto the Search word
and enter insert mode.

