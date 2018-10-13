# section6 - Classes, Constructors and inheritance
estimated 2h 30m

### Classes
* what is object? 
    * has state (field as variables) and behavior
* class is a templete (blue print) for objects
    * (kind of) user-defined type
    * usually use Capital letter for the first letter of the name
    * has a file named after the class name followed by `.java`
    * encapsulate 
    * inherit the base java class
* access modifier
    * for fields or methods
    * public: unrestricted access to outside of this class
    * private: accessable only to inside
        * encapsulate - hide the fields and mothods from outside
* getters and setters:
    * ensure the data is valid


```java
// under the file name Car.java:
package mypack;
public class Car {              // statement to create a new class

    // state components: fields
    private int doors;          // private: from outside of Car, they are not accessable
    private int wheels;
    private String model;    
    private String engine;
    private String colour;
    // if a field is defined public, they can be accessed from outside or by other classes
    // public String model;     // but not a good practic 

    //setter : validate the data before set it
    public void setModel(String model){     // public: can be accessed from outside
        String validModel = model.toLowerCase();
        if(validModel.equals("carrera") || validModel.equals("commodore")) {
            this.model = model;      // this: to refer the field in the class 
        } else {
            this.model = "Unknown";
        }
    }

    //getter
    public String getModel() {
        return this.model;
    }
}
```
```java
package mypack;
public class Main {
    public static void main(String[] args) {
        // Car porsche;                 // should be initialized
        // define an object of type Car and initialize it
        // use keyword new to initialize
        Car porshe = new Car();         
        Car holden = new Car();
        // porsche.model = "Carrera";   // possible for public field but not a good way 
        System.out.println("Model is " + porsche.getModel());   // null (default state for class and a String)
        porsche.setModel("Carrera");
        System.out.println("Model is " + porsche.getModel());
    }
}
```
```shell
javac -d . Car.java  // create a folder with package name and put compiled file in it
javac -d . Main.java
java mypack.Main     // execute the Main
```

### Constructors
* is called when a new object is made
* initialize the object
* can be overloaded (has different definition depending on parameters)
* can call constructor from another constructor
    * but the constructor (`this`) should be called on the first line
    * hava a general constructor and others call it
* don't call other methods such as setters
    * set value directly
* IntelliJ: under menu code->generate - the constructors, getters, setters etc.
```java
public class Account{
    private String number;
    private double balance;
    private String custormerName;


    public Account() {  // constructor: done when a new class is created
        // call a constructor with default value
        this("123", 2.0, "default name");   // this should be the first line
    }

    public Account(String number, double balance, String customerName) {    // overload
        this.number = number;
        this.balance = balance;
        this.customerName = customerName;
    }
}
```

```java
// use the constructor
Account bobsAccount = new Account('123', 100.0, "bob");
Account janesAccount = new Account();   // called the constructor with default values:
// this("123", 2.0, "default name");
```

#### create
Can also make a method to return new object:
(it's a `static` method because we want to use without creating an instance of the class)
```java
public static Contact createContact(String name, String phoneNumber) {
    return new Contact(name, phoneNumber);
}

// ...
Contact myContact = createContact("me", "11111");
```


### Inheritance
* sharing common characteristics between objects, while having different characteristics, too.
* child class should call super classes constructor (`super(//...);`)
* methods from super can be override
* all the classes extends Object (automatically)

```java
package animals;
public class Animal {
    private String name;
    private int body;
    private int weight;

    // constructor and getters and setters ...
    public Animal(String name, int body, int weight) {
        this.name = name;
        this.body = body;
        this.weight = weight;
    }

    public void eat() {
        System.out.println("Animal eats");
    }

    public void move(int speed) {
        System.out.println("Animal moves speed at " + speed);
    }

    public void breath() [
        System.out.println("Animal breaths");
    }
}
```
```java
package animals;
public class Dog extends Animal {
    // can add more fields related to Dog addition to the Animal class
    private int legs;
    private int tail;

    // it should call a constructor of Animal
    public Dog(String name, int weight, int legs, int tail) {
        // call the constructor  of superclass
        // this initializes Animal class 
        super(name, 1, weight);     // can give a fixed value as well
        this.legs = legs;
        this.tail = tail;
    }

    // Dog can also use method eat, move and breath (from superclass)

    // can also define unique method only for Dog
    private void chew() {
        System.out.println("Dogs chew");
    }

    // override existing methods
    @Override       
    public void eat() {
        chew();
        System.out.println("Dogs eat");
        super.eat();    // call eat in Animal class
    }

    
    // illustrate difference between super.move() and move()
    public void walk() {
        System.out.println("Dog walks");
        // super.move()
        // super calls method from superclass even if it is overriden
        super.move(5)          
    }

    public void run() {
        System.out.println("Dogs walk");
        // move()
        // calls move from super if move method is not overriden
        // calls its own move method when there is one
        move(10)          
    }

    @Override
    public void move(int speed) {
        System.out.println("Dog uses " + this.legs + " legs to move."); 
        super.move(speed);
    }

}
```
```java
Animal animal = new Animal("animal", 1, 4);
Dog dog = new Dog("Yorkie", 10, 4, 1);
dog.eat();          
dog.breath();   // method from Animal
dog.walk();     // uses move from Animal
dog.run();      // uses move from Dog (override)
```

```java
public class Fish extends Animal {
    private int fins;

    public Fish(String name, int weight, int fins){
        super(name, 1, weight);
        this.fins = fins;
    }

    private void rest() {
    }

    private void swim() {
        System.out.println("Fish swims.");
        super.move(3);
    }
}
```


### Reference Object Instance Class
* **class**: a blueprint for a house
* each house we build from the blueprint is an **object** (a.k.a. **instance**)
* each house has an address. a paper the address is writen is **reference**
    * the address paper can be copied of passed to other people
    * everything is done with reference
```java
House blueHouse = new House("blue");// created a house and wrote the address in blueHouse
House anotherHouse = blueHouse;     // two papers poinint the same house
anotherHouse.setColor("yellow");    // painted the house in the address into yellow
// so far there is only one house, the color was blue and not yellow

House greenHouse = new House("green");  // built a new house with a color green
anotherHouse = greenHouse;              // it is now pointing the greenHouse newly created
```

### this super
* super and this
    * super: access/ call the parent class members
        * commonly used in method overriding
    * this: call the current class members
        * commonly used constructors and setters (optional for getters)
    * can be used anywhere in a class except static areas (static blocks or static methods)
* constructors `this()` and `super()`
    * cannot have this() and super() both in one constructor
    * this(): this call a constructor from another overloaded constructor in the same class
        * only in a constructor, must be the first statement
        * used for constructor chaining: avoid duplicated code
    * super() : calls parent constructor
        * must be first statement
* Abstract classes have constructors (but can never instantiate using the new keyword)
    * an abstract class is still a super class
    * its constructors run when someone makes an instance of a concrete subclass


### method overloading overriding
* Method **overloading** - (a.k.a Compile Time Polymorphism)
    * provide more separate methods in a class with same name but different parameters
    * method return type, access modifier  may or may not be different: can reuse the same method name
    * compiler decides which method is going to be called based on name, return type, arg list
    * we can overload static and instance methods
    * we can use the same name and avoid duplicated code
    * can be in a single class or in a child class

* Method **overriding** - (a.k.a. Runtime Polymorphism, Dynamic Method Dispatch)
    * define a method in a child class that already exists in the parent class with same signature
        * same name, same arguments
    * derived methods: child class has all the methods definded in the parent class 
    * which method to be called is decided at runtime by the JVM
    * recommended to put `@Override` annotation immediately above the method definition
    * only instance methods can be overriden (cannot override static method)
    * rules;
        * same name and same arguments
        * return type can be a subclass of the return type in the parent class
        * cannot have a lower access modifier
            (for example: parent - protected, child - public)
        * Only inherited methods can be overridden
        * constructors and private methods cannot be overriden
        * final methods cannot be overriden
        * A subclass can use super.methodNAme() to call the superclass version
        *


### static instance
* static methods 
    * declared using static modifier
    * cannot access instance methods and instance varibles directly
    * `this` keyword: the current instance of a class
    * when do not need any data from an instance of the classe (from `this`)
    * cannot use `this` keyword
    * called as `ClassName.methodName();` or `methodName();` in the same class
    * instance do not be created to use the statice methods
* static variables
    * keyword `static`
    * a.k.a. static member variables
    * every instance of that class shares the same static variable
    * if it is changed all the instances are affected

* instance methods
    * belong to an instance of a class
    * to use, we have to instantiate the class first (by using the `new` keyword)
    * can access instancemethods and instance variables directly
    * can also access static methods and static variables directly
* instance variables
    * don't use `static` keyword
    * a.k.a. fields or member variables
    * belog to an instance of a class
    * each instance has it's own copy of an instance variable
    * every instance can hava a different value (state)
    * instance variables represent the state of an instance

* does it use instance variables or instance methods? 
    * yes -> probably instance method
    * no -> probably static method


```java
class Dog {
    private static String name;     // all instances share the name
    private String realname;        // everybody has its own

    public Dog(String name) {
        Dog.name = name;
        Dog.realname = name;
    }

    public void printName() {
        System.out.println("static name = " + name);
        System.out.println("instance name = " + realname);
    }
}

public class Main {
    public static void main(String[] args) {
        Dog rex = new Dog("rex");              // set the static name to rex
        Dog fluffy = new Dog("fluffy");        // modify the static name to fluffy
        rex.printName();            // fluffy rex
        fluffy.printName();         // fluffy fluffy
```




