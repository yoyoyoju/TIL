# w3 methods ArrayList

#### methods
* watch the scope
* return value
    ```java
    public static int alwaysReturnTen() { return 10; }
    ```

#### String
* `"a".equals("b");` to compare
* `"a".length();` length
* `"abcde".charAt(2);` will return a character in the given index
    * char: store only one character
* `"012345678".substring(5);` prints `5678`
* `"012345678".substring(2,6);` prints `2345`
* `"Horse".indexOf("or");` returns 1 (-1 if not found)
* two way to create a string object
    * `String apple = new String("apple");`
    * `String apple = "apple";`

#### ArrayList
* object container
* methods of `ArrayList<T>` (int index, T element)
    * size()
    * get(index)
    * `remove(element)` or `remove(index)`
    * contains(element)
    * remove and contains uses `equals` method
* ordering etc
    * `import java.util.Collections;`
    * `Collections.sort(wordList);`
    * `shuffle` to shuffle
    * `reverse` to reverse the order of list items

Examples:
```java
import java.util.ArrayList;

// main method
ArrayList<String> wordList = new ArrayList<String>();
wordList.add("First");
```
```java
ArrayList<Integer> myint = new ArrayList<>();
myint.add(10);  // it autoboxed
myint.add(Integer.valueOf(10)); // is the same
myint.remove(1);    // remove by index
myint.remove(Integer.valueOf(10));  // remove as element
```

* looping through
```java
for (String word : wordList) {
    // do something with word
}
```


