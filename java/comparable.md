# Comparable interface
* has a method compareTo (only one way to compare)
```java
class Hand implements Comparable<Hand> {
//...
    @Override
    public int compareTo(Hand other) {
        return this.value - other.getValue();
    }
```

----
see also:
[comparable](comparable.md)
