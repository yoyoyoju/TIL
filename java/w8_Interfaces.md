# Interfaces

### Interface
* Interface
    * an instrument we have to define the functionality our classes should have
    * behavioural agreement
    * `public interface InterfaceName {}`
    * access modifier is not specified, because it is always public
    * class implements interface
```java
public interface Readable {
    String read();
}

public class SMS implements Readable {
    private String content;

    public SMS(String content) {
        this.content = content;
    }

    public String read() {  // this should be implemented!!
        return this.content;
    }

    public String test() {
        return "test";
    }
}
```

### Type
* The type of an object can be different from its class.
* one can cast, if and only if the variable's type is really what we try to change it into.
    * but not usually a best practice
    * one of the only cases where that is legitimate is in connection with the `equals` method.
* one can create a list containing interface-type objects
```java
SMS message = new SMS("hi");
Readable readable = new SMS("readable");
((SMS) readable).test();
readable.read();
ArrayList<Readable> mylist = new ArrayList<Readable>();
```
```java
Readable readable = new SMS("teacher", "The SMS is Readable!"); // works
SMS message = readable; // not possible

SMS transformedMessage = (SMS) readable; // works
```

### Interface as Method Parameter
* interface can be used in method calls as parameter type
```java
public class Printer {
    public void print(Readerble readable) {
        System.out.println(readable.read());
    }
}
```
```java
public class NumberList implements Readable {
    private ArrayList<Readable> readables;

    public NumberList() {
        this.readables = new ArrayList<Readable>();
    }

    public void add(Readable readable) {
        this.readables.add(readable);
    }

    public int howManyReadables() {
        return this.readables.size();
    }

    public String read() {
        String read = "";
        for(Readable readable: this.readables) {
            read += readable.read() + "\n";
        }

        this.readables.clear();
        return read;
    }
}
```

### interface as method return value
* it is good to use interface to reduce dependencies
    * it is good to depend only on the interface (not the classes itself)
    * less dependences make it easy to extend a program
    * interface abstracts their internal functionality

### madeUp interfaces
* sensible number of made-up interfaces from Java API
    * List: followings implement List interface
        * ArrayList: saves the objects into a table
            * search is quick with a specific index
            `List<String> strings = new ArrayList<>();`
        * LinkedList: builds up a list where each item has a reference to the following item
            * to search, we have to go through all the list items till we reach the index
            * adding new items is always fast
    * Map: 
        * has methods like keySet() (returns Set interface), get(key), values() (Collection interface)
        * HashMap
    * Set:
        * contain 0 or 1 element of a certain type
        * can be parsed with a for-each loop
        * HashSet
    * Collection:
        * lists and sets are collections
        * methods: contains, size(),
        * can be parsed with a for-each loop
