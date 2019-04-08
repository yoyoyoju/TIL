# Collection

* note from HeadFirst java chapter 16


### Array and Collection

* Array types are checked again at runtime,
* but collection type checks happen only when you compile


### Collection interfaces

* Three main interfaces:
    * List
        * when sequence matters
        * has index position: knows where something is in the list
        * duplicates Ok
    * Set
        * when uniqueness matters
        * do not allow duplicates
    * Map
        * when finding something by key matters
        * uses key-value pairs
        * duplicate values OK, but NO duplicate keys

### Collection Classes

* Collection interface 
    * List interface
        * ArrayList
        * Vector
        * LinkedList
            * Makes it easy to create structures like stacks or queues
    * Set interface
        * SortedSet interface
            * TreeSet
                * Keeps the elements sorted and prevents duplicates
                * uses object's compareTo() method as default
                * can pass Comparator to the TreeSet constructor instead
        * HashSet
            * Prevents duplicates in the collection, and given an element, can find that element in the collection quickly
        * LinkedHashSet
* Map interface
    * HashMap
        * Lets you store and access elements as name/value pairs
    * LinkedHashMap
        * Like a regular HashMap, except it can remember the order in which elements were inserted, or it can be configured to remember the order in which elements were last accessed
    * Hashtable
    * SortedMap interface
        * TreeMap


#### Collections methods

* `static <T extends Comparable<? super T>> void sort(List<T> list)`
    * Sorts the specified list into ascending order, according to the natural ordering of its elements.
* `static <T> void sort(List<T> list, Comparator<? super T> c)`
    * Sorts the specified list according to the order induced by the specified comparator.
