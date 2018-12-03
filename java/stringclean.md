# to clean string

```java
String stringCleaner(String string) {
    if (string == null) {
        return "";
    }
    string = string.toLowerCase();
    return string.trim();
}
```
