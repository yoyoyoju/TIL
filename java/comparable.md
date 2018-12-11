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

### Comparator
* want to compare in different ways
* make use of different classes which execute the comparison
* implements Comparator<T>
* method, compare(T t1, T t2) (negative `t1 < t2`, positive, `t1 > t2`)
```java
import java.util.Comparator;
public class SortAgainstSuit implements Comparator<Card> {
    public int compare(Card card1, Card card2) {
        return card1.getSuit() - card2.getSuit();
    }
}
```
* one can sort based on this:
```java
SortAgainstSuit suitSorter = new SortAgainstSuit();
Collections.sort(cards, suitSorter); // cards is ArrayList of Card
```

