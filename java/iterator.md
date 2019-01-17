# Iterator
* Iterable interface
    * object containers, which implements Collection interface, implements indirectly Iterable interface
    * objects, which implements Iterable, can be parsed (or iterated) with statements such as for each
    * ConcurrentModificationException: one cannot delete objects from a list while parsing it. [more](arraylist.md#ConcurrentModificationException)
* iterator
    * object containers can also be iterated using `iterator`
    * iterator parses a particular object collection
    * iterator points out a specific object of the list, till the finger has gone through each object
    * methods: 
        * `hasNext()`: whether there are still objects to be iterated
        * `next()`: if(hasNext()){ retrieve the following object reference } else { throws NoSuchElementException }
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


------
reference
[mooc.fi week12: 54.3 Iterator](https://materiaalit.github.io/2013-oo-programming/part2/week-12/)
