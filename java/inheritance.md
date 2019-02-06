# inheritance
* the advantages of inheritance:
    * avoid duplicate code
    * define a common protocol for a group of classes
        * all the subclasses have the moethods that the supertype has
        * it establish a *contract*
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
    * the arguments must be the same
    * return types must be compatible
        * the overriding method must declare either the same type, or a subclass type (of the superclass return type)
        * so that it is safe to return a subclass where the superclass is expected
    * overriden method cannot be less accessible
        * access level must be the same, or friendlier
        * for example, cannot override a public method and make it private
* overload:
    * having multiple versions of method with the same name but different argument lists
    * the return types can be different
    * cannot change only the return type; must change the argument list
    * can vary the access levels in any direction

### polymorphism
* polymorphism: the ability of an object to take on many forms. [ref](https://www.tutorialspoint.com/java/java_polymorphism.htm)
    * refer to a subclass object using a reference declared as the supertype
    * Normal declaration
        1. Declare a reference variable
            * allocate space for a reference varible, which is of type Dog.
        2. Create an object
            * allocate spce for a new Dog object on the garbage collectible heap
        3. Link the object and the reference
            * assigns the new Dog to the reference vareable myDog
        * the reference type and the object type are the same
        ```java
        Dog myDog   // 1. Declare a reference varible
        =           // 3. Link the object and the reference
        new Dog();  // 2. Create an objec
        ```
    * with polymorphism
        * the reference and the object can be different
        ```java
        Animal myDog = new Dog(); // the reference type is superclass of the objecttype
        ```
* advantage:
    * can write flexible, cleaner and efficient code
    * easier to extend
    * does not need to change the code as new subclass types are introduced
    * example cases:
        * polymorphic arrays
            ```java
            Animal[] animals = new Animal[5];  // can hold any type of animal
            ```
        * polymorphic arguments and return type
            ```java
            public void giveShot(Animal a) {...} // any animal can be passed as parameter
            ```
* which method is invoked
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
                * by looking at the actual objct on the heap (rather than the reference type)
        * `lucas` is actually `Student`: use `Student`'s `toString` method.
        * *the lowest one wins*: the lowest (on the inheritance tree) version of method is called

### access modifier
* access levels control who sees what
* four access levels for members (methods and instance variables)
    * private
        * cannot be seen by its subclasses
        * its subclasses do not have any straight way to access it
        * private members are not inherited
    * default
    * protected
        * access is restricted to only its subclasses
    * public
        * subclass can see `public` variables and methods
        * public members are inherited

* for class
    * public
    * non-public
        * do not declare as public
        * can be subclassed and used only by classes in the same package as the class
        * classes in a different package cannot subclass nor use it.


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


### cannot be subclassed
* when a class is non-public: cannot be subclassed from outside of the package
* final keyword: it's the end of the inheritance line
* private constructors: if a class has only private constructors, it cannot be subclassed

----
reference:
* MOOC.fi java
* *headfirst java* chapter 7
