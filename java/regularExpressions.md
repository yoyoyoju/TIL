# Regular Expressions
* a compact form to define a string
* used to check the validity of strings
* `matches` method of the String class: checks whether the string matches with the regular expression
```java
String num = "01";
if (num.matches("01[0-9]{7}")) {
    System.out.println("valid form");
}
```

* Vertical Bar: Logical or
    * `00|111|0000` defines the strings `00`, `111`, `0000`
    * `matches` method returns true if the string in question matches to one of them
    * it should match exactly the same(not like `contains`)
    * `"00".matches("00|111|0000");` returns true
* Round Brackets: a Delimited Part of the String
    * define what part of the regEx is affected by the symbols
    * `"00000|00001"` can be written as `"0000(0|1)"`
    * `word.matches("look(|s|ed|ing|er)");` (look, looks, looked, looking, looker)
* Repetitions
    * whether a substring repeats within another string
    * `*` stands for a repetition from 0 to n times
        * `string.matches("trolo(lo)*");` (trolo, trololo, trolololo, ...)
    * `+` stands for a repetition from 1 to n times
        * `string.matches("tro(lo)+");` (trolo, trololo, trolololo, ...)
    * `?` stands for a repetition of 0 or 1 time
        * `string.matches("tro(lo)?");` (tro, trolo)
    * `{a}` stands for a repetition of `a` times
        * `string.matches("(10){2}");` (1010)
    * `{a,b}` stands for a repetition from `a` to `b` times
        * `string.matches("1{2,4}");` (11, 111, 1111)
    * `{a,}` stands for a repetition from `a` to n times
        * `string.matches("1{2,}");` (11, 111, 1111, 11111, ...)
    * example: `5{3}(1|0)*5{3}` (555555, 5551555, 5550555, 55511555, ...)
* Square Brackets: Character Groups
    * define groups of characters
    * can define an interval by a hyphen (`-`)
    * `[145]` means `(1|4|5)`
    * `[2-36-9]` means `(2|3|6|7|8|9)`
    * `[a-c]*` a string made only of characters ("", "a", "b", "c", "ab", ...)
* example
    * valid time expression?: `string.matches("([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]");`

----
reference
[Mooc.fi week12](https://materiaalit.github.io/2013-oo-programming/part2/week-12/)
