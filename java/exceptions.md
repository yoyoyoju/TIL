# Exceptions
* when things are not as we expected: throw an exception
* `NullPointerException`, `IndexOutOfBoundsException`, etc.
* handling exception using `try{ } catch (Exception e) { }`
```java
// example of parseInt and NumberFormatException
try {
    int num = Integer.parseInt(reader.nextLine());
} catch (Exception e) {
    System.out.println("is not proper number");
}
```

### methods
* the class Exception has methods
    * `printStackTrace()`
