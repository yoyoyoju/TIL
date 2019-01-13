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
* `split`

#### split
example:
```java
String line = "word:translation";
String[] parts = line.split(":");
System.out.println(parts[0]);
System.out.println(parts[1]);
```



### format
```java
String.format("%s %.1f", "some String", 1.0002);
String.format(Locale.ROOT, "%s %.2f", "when the format uses local decimal point (,) to make sure use (.)", 1.2312);
```

