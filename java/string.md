### forEach for string
* to loop through a string: `toCharArray()`
```java
public boolean containsAllVowels(String word) {
    String vowels = "aeiou";
    for (char vowel : vowels.toCharArray()) {
        if (!word.contains("" + vowel)) {
            return false;
        }
        return true;
    }
}
```

### methods
* `contains`
* `endsWith`
* `equals`
* `trim`
