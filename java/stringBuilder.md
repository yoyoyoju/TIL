# String Builder
* strings are immutable objects
    * the result of a String operation is always a new String object
    * in a loop, if we keep doing string operation such as `str += ", ";`
        it keep creates new String objects, which could impact the programs execution time.

* String builder
    * in the situations, one has to keep modifying a str, it is better to use `StringBuilder`
    * StringBuilder objects are not immutable
    * it can be modified
    * methods:
        * `length()` returns the length (Character count)
        * `delete(int start, int end)` removes the characters in a substring of this sequence
        * `deleteCharAt(int index)` removes the char at the specified position
        * `charAt(int index)` returns the char value at the specified index


```java
StringBuilder sb = new StringBuilder();
sb.append("this").append("\n");
String mystring = sb.toString();
```

------
reference
[mood.fi, week12, 54.7 and Ex48](https://materiaalit.github.io/2013-oo-programming/part2/week-12/)
