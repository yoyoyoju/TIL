# object Polymorphism
* all objects are Object-type.
```java
String string = "string";
Object stringObject = "another string";
Object fromString = string;
// String fromObject = string; // does NOT work!!
```
* Variables have got their own type and their parent classes and interfaces.

### example of String
* the package: `java.lang`
* inheritance hierarchy: `java.lang.Object-java.lang.String`
* implemented interfaces: Serializable, CharSequence, Comparable<String>
    * `CharSequence` has `int length()`, `char charAt(int index)` for example




----
[ref: MOOC2 week10](https://materiaalit.github.io/2013-oo-programming/part2/week-10/)
