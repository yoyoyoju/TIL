# Interfaces

### why interface
* as an alternative of multiple inheritance:
    * having the polymorphic benefit
    * without the pain from the Deadly Diamond of Death [(see more)](inheritance.md#no%20multiple%20inheritance%20for%20java)
    * by making all the methods abstract:
        * the subclass must implemnt the method,
        * so at runtime, no confusion about which version of method to be called

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

### Collections
* Collections is a library for collection classes
    * methods to sort objects (through the interface Comparable or Comparator)
    * minimum and maximum values (`min`, `max`)
    * retrieve a specific value (`binarySearch`)
        * found: returns index of searched key, otherwise: negative value
        * uses comparable interface (if it returns `0`, considered found)
    * reverse the list (`reverse`)

### exceptions and interfaces
* interfaces can also define the exceptions throw
```java
public interface FileServer {
    // they can possibly throw and exception
    String download(String file) throws Exception;
    void save(String file, String string) throws Exception;
}

public class TextServer implements FileServer {
    // ...
    @Override
    public String download(String file) throws Exception {
        return this.data.get(file);
    }
    //...
```
```
