### HashMap
```java
import java.util.HashMap;
import java.util.Map;
HashMap<String, String> numbers = new HashMap<String, String>();
numbers.put("One", "eins");
numbers.put("Two", "zwei");
String translation = numbers.get("One");
```

### loop
* loop through the keys: `keySet()`
```java
for (String key : wordPairs.keySet()) {
    System.out.print(key +" ");
}
```


### OriginalType Variables in a HashMap
* HashMap keys and stored objects are reference-type variabels
* reference-type quivalent to the original-type
    * int: Integer
    * double: Double
    * char: Character
* Auto-boxing: automatic translation of original-type variables into reference-type ones
    * allocateion into a slot
    ```java
    HashMap<Integer, String> table = new HashMap<Integer, String>();
    table.put(1, "Be!");
    ```
* Unboxing
    * be careful with the cases with null -> java.lang.reflect.InvocationTargetException error
    ```java
    private HashMap<String, Integer> twitched;
    public int lastTwitch(String name) {
        if (this.twitched.containsKey(name)) {
            return this.twitched.get(name);
        }
        return 0;
    }
    ```

