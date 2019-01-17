# Iterator
* Iterable interface
    * object containers, which implements Collection interface, implements indirectly Iterable interface
    * objects, which implements Iterable, can be parsed (or iterated) with statements such as for each
    * ConcurrentModificationException: one cannot delete objects from a list while parsing it. [more on arraylist](arraylist.md#ConcurrentModificationException)
* iterator
    * object containers can also be iterated using `iterator`
    * iterator parses a particular object collection
    * iterator points out a specific object of the list, till the finger has gone through each object
    * methods: 
        * `hasNext()`: whether there are still objects to be iterated
        * `next()`: if(hasNext()){ retrieve the following object reference } else { throws NoSuchElementException }
        * `remove()`: delete the value which was returned by the iterator with its previous next method call

* example usage for iterator
```java
private ArrayList<Card> cards;
// ...
public void print() {
    Iterator<Card> iterator = cards.iterator();
    whiel(iterator.hasNext()) {
        Card nextCard = iterator.next();
        // ...
    }
}
```

* example for deleting while parsing
```java
public class Hand {
    // ...
    public void deleteWorst(int value) {
        Iterator<Card> iterator = cards.iterator();
        while(iterator.hasNext()) {
            if (iterator.next().getValue() < value) {
                // delete the object returned by the iterator with its previous method call
                iterator.remove();
            }
        }
    }
}
```


------
reference
[mooc.fi week12: 54.3 Iterator](https://materiaalit.github.io/2013-oo-programming/part2/week-12/)
