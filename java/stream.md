# Stream

* Stream API from java8
* Classes to support functional-style operations on streams of elements, such as map-reduce transformations on collections
* [documentation](https://docs.oracle.com/javase/8/docs/api/java/util/stream/package-summary.html)


### map

* apply any function to every element of Collection
```java
import java.util.*;
import java.util.stream.Collectors;
import static java.util.stream.Collectors.toList;

public class Main {
    public static void main(String[] args) {
        List<Integer> numbers = Arrays.asList(1, 2, 3);
        List<Integer> squares = numbers.stream()
                                       .map(i -> i*i)
                                       .collect(Collectors.toList());
        List<String> strings = Arrays.asList("hello", "world");
        List<String> upperCaseStrings = strings.stream()
                                               .map(String::toUpperCase)
                                               .collect(toList());
    }
}
```


