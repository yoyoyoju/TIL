# Comparator

* used in `Collections.sort(List<T> list, Comparator<? super T> c)`


### Comparator

* java.util.Comparator
    ```java
    public interface Comparator<T> {
        int compare(T o1, T o2);
    }
    ```
    * external to the element type you're comparing - it is a separate class
    * use when you want to compare in different ways
* make use of different classes which execute the comparison
* `implements Comparator<T>`
* method, compare(T t1, T t2) (negative `t1 < t2`, positive, `t1 > t2`)
* example: 
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

#### examples
* using a map to sort
    * [mooc.fi week12, Exercise 46:Film Reference](https://materiaalit.github.io/2013-oo-programming/part2/week-12/)
```java
public class PersonComparator implements Comparator<Person> {
    private Map<Person, Integer> peopleNum;
    public PersonComparator(Map<Person, Integer> peopleNum) {
        this.peopleNum = peopleNum;
    }
    @Override
    public int compare(Person p1, Person p2) {
        return this.peopleNum.get(p2) - this.peopleNum.get(p1);
    }
}
// use
Map<Person, Integer> peopleNum = new HashMap<>();
peopleNum.put(matti, 32);
// ...
List<Person> ppl = Arrays.asList(matti, //...);
Collections.sort(ppl, new PersonComparator(peopleNum));
```


----
see also:
[comparable](comparable.md)

----
reference
[mooc.fi week12, Exercise 46:Film Reference](https://materiaalit.github.io/2013-oo-programming/part2/week-12/)
