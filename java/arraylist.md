# ArrayList

### Removing Objects from an ArrayList
how NOT to remove a part of the list objects while parsing an ArrayList:
```java
/* this example does NOT work!!!
 * it throws ConcurrentModificationException
 * because it is not possible to modify a list
 * while parsing it with a foreach iteration
 */

// ArrayList<Object> list = new ...
for (Object object: list) {
    if (hasToBeRemoved(object)) {
        list.remove(object);
    }
}
```

how to do: 
```java
// ArrayList<Object> list = new ...

ArrayList<Object> toBeRemoved = new ArrayList<Object>();

for (Object object : list) {
    if (hasToBeRemoved(object)) {
        toBeRemoved.add(object);
    }
}
list.removeAll(toBeRemoved);
```

#### ConcurrentModificationException
* check also [iterator](iterator.md)
```java
// this method causes error!!!!
public class Hand {
    // ...
    public void deleteWorst(int value) {
        for (Card card : cards) {
            if (card.getValue() < value) {
                cards.remove(card);
            }
        }
    }
}
```


------
reference [Removing Objects from an ArrayList: mooc.fi week10 50.9](https://materiaalit.github.io/2013-oo-programming/part2/week-10/)
