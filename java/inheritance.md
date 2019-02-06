# inheritance
* use `extends` keyword
    * subclass *extends* the superclass
    * the subclass inherits the members (instance variables, methods) of the superclass
    * IS-A test: subclass IS-A superclass
        * Triangle IS-A Shape, Cat IS-A Feline
        * if it is X HAS-A Y, X does not extend Y, rather X has a reference to Y
* how to design the inheritance tree
    * look for objects that have common attributes and behaviors
    * design a class that represents the common state and behavior
    * decide if a subclass needs behaviors (method implementations) that are specific to that particular subclass type
    * look for more opportunities to use abstraction, by finding two or more subclasses that might need common behavior

```java
public class Person {
    private String name;
    public Person(String name) {
        this.name = name;
    }
    @Override
    public String toString() {
        return this.name;
    }
}
public class Student extends Person {
    private int credit;
    public Student(String name, int credit) {
        super(name);
        this.credit = credit;
    }
    @Override
    public String toString() {
        return super.toString() + " : " + this.credit;
    }
    public int credit() {
        return this.credit;
    }
}
```

### override 
* override:
    * the subclass redefines one of its inherited methods when it needs to change or extend the behavior of that method

### polymorphism
```java
Person lucas = new Student("lucas", 1);
lucas.credit(); //NOT WORK
lucas.toString();   // work with toString definded in Student
```
* which methods can be called, is defined through the variable type:
    * `lucas` is a `Person` type: can only use the methods defined in Person class.
* the execution method is chosen based on its real type, regardless of the variable type which is used.
    * Objects are diverse, which means they can be used through different variable types.
    * The execution method does always depend of the object's actual type.
    * if the actual class does not have the method, move to its parent class.
        * the compiler guarantees that a particular method is callable for a specific reference type
        * JVM picks the right one (most specific one) at runtime
    * `lucas` is actually `Student`: use `Student`'s `toString` method.
    * *the lowest one wins*: the lowest (on the inheritance tree) version of method is called

### access modifier
* private
    * cannot be seen by its subclasses
    * its subclasses do not have any straight way to access it
* protected
    * access is restricted to only its subclasses
* public
    * subclass can see `public` variables and methods

### superclass
* call `super` in constructor to call the constructor of superclass
    * super call must always be in the first line
* `super` prefix to call the methods defined in the superclass
    ```java
    @Override
    public String toString() {
        return super.toString() + "\n and additional message";
    }
    ```


----
reference:
* MOOC.fi java
* *headfirst java* chapter 7
