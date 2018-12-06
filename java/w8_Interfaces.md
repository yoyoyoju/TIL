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
    * but not usually a best practice;
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

from 40.2 
