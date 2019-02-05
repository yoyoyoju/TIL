# ArrayList

### ArrayList
* methods:
    * add(Object elem)
        * adds elem to the list
    * remove(int index)
        * removes the object at the index parameter
    * remove(Object elem)
        * removes this object (if it is in the ArrayList)
    * contains(Object elem)
        * returns true if there's a match for the object parameter
    * isEmpty()
        * returns true if the list has no elements
    * indexOf(Object elem)
        * returns either the index of the object parameter, or -1
    * size()
        * returns the number of elements currently in the list
    * get(int index)
        * returns the object currently at the index parameter
    * // and more

---
reference:
*headfirst java* chapter 6


### ArrayList and array
* both lives on the heap (both are object)
    * (objects live on the heap)
* ArrayList:
    * cannot hold primitives
        * use primitive wrapper class for that
    * has methods
    * can remove elements
    ```java
    // have to import
    import java.util.ArrayList
    // no size required (may give though)
    // declare type as parameterized type (<String>)
    ArrayList<String> myList = new ArrayList<>();
    // does not need index
    // (may specify as: add(anInt, anObject))
    myList.add("foo");
    myList.size();
    myList.get(0);
    myList.remove(0);
    boolean isIn = myList.contains("bar");
    ```
* array:
    * use special array syntax (`myArray[0] = foo`)
    * cannot invoke any methods
    * has one instance varible length (`myArray.length`)
    ```java
    String[] myList = new String[1];    // needs a size
    myList[0] = "foo";
    myList.length;
    myList[0];
    myList[0] = null; // the length of array does not change though
    // below is corresponding to myList.contains("bar"); from ArrayList
    boolean isIn = false;
    for (String item : myList) {
        if (item.equals("bar")) {
            isIn = true;
            break;
        }
    }
    ```
---
reference:
*headfirst java* chapter 6




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
* the for each statement "gets all worked up"
* to delete a part of the objects while parsing the list, use [iterator](iterator.md)
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

### List and Set
* List to Set
`Set set = new HashSet(list);`
* Set to List
`List list = new ArrayList(set);`
* JDK 8:
`List list = set.stream().collect(Collectors.toList());`
------
reference [Removing Objects from an ArrayList: mooc.fi week10 50.9](https://materiaalit.github.io/2013-oo-programming/part2/week-10/)
