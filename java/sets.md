# Set

* Set has only unique entries.
* the same object can not be contained twice in a set
* (the sameness is based on `equals` and `hashCode`)
```java
private Set<Integer> myset = new HashSet<>();
myset.add(1);
myset.add(1);
myset.add(1);
// the set has only one 1
```

### HashSet

* HashSet implements Set interface


### TreeSet

* TreeSet implements SortedSet
* methods:
    * boolean add 
        * // adds if it is not already present
        * // returns false if it already present
    * boolean contains
