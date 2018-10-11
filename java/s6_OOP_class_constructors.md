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
 57: 36min

### Inheritance
58, 59: 30min

### Reference Object Instance Class
60: 7min

### this super
7
### method overloading overriding
7
### static instance
8

### inheritance challenge
25min
