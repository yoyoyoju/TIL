# section9: Inner and Abstract Classes and Interfaces

### interfaces
* define common behaviors for certain classes
* can be seen as a commitment to have the methods 
specified by the method signiture.
    * name of method
    * return type
    * parameters and thier types
* As convention, the first letter is `I`
* `public` keyword is redundant - can be omitted
* to show certain class uses an iterface,
use `implements`.
* a class can use more than one interfaces
```java
public interface ITelephone {
    // have to implement all the functionality
    // to implement this interface
    void powerOn();
}
```
```java
public class DeskPhone implements ITelephone {
    private int myNumber;
    private boolean isRinging;

    @Override
    public void powerOn() {
        System.out.println("power's on");
    }
}
```
```java
// in the main class,  main method
ITelephone = phone;
phone = new DeskPhone(1111);
phone = new MobilePhone(1121);   //works if MobilePhone implements ITelephone
// On the other hand;
DeskPhone = phone;
phone = new MobilePhone(2111);  // do not work cause the class is specified
ITelephone myPhone = new ITelephone();   // do not work cause it is not a concrete type
        // should implement ITelephone to do like this
```

```java
List<String> values = new ArrayList<~>();
ISaveable warewolf = new Monster("w" , 10, 10);
// cannot access methods in Monster but not in ISaveable
((Monster) warewolf).getString()  // should cast to do it
```

### Inner classes
* nest class inside of class
* inner class : non-static inner class
    * need instance to create one
    * maybe want to keep it private
* inner class variables shadow outer class variable
```java
Gearbox macLaren = new Gearbox(6);  // outer class
Gearbox.Gear first = maLaren.new Gear(1, 12.3);    // create inner class
// need instance (of outer) to create the inner class
// not:
// Gearbox.Gear second = new Gearbox.Gear(2, 22);
// Gearbox.Gear third = new maLaren.Gear(3, 24);
```
* local class
    * defined in a block or scope

* anonymous class
    * local without name
    * cannot be used again
```java
public class Button {
    private String title;
    private OnClickListener onClickLister;
    //Constructor, getter setter

    public void onClick() {
        this.onClickLister.onClick(this.title);
    }

    public interface OnClickListener { 
        public void onClick(String title);
    }
}
```

```java
btnPrint.setOnClickListener(new Button.OnClickListener() {
    @Override
    public void onClick(String title) {
        System.out.println(title + " clicked");
    }
});
```

### Abstract Class
* interface
    * what has to be done (rather than how it's done)
    * implemented in class
    * interface `List`

* Abstract class
    * cannot be instantiated
```java
public abstract class Animal {
    private String name;
    public Animal(String name) {
        this.name = name;
    }

    // force child class to implement those
    public abstract void eat();
    public abstract void breathe();

    // does not need to be abstract
    public String getName() {
        return this.name;
    }
}
```
```java
public class Dog extends Animal {
    public Dog(String name) {
        super(name);
    }

    // common to all animals
    @Override
    public void eat() {
        System.out.println(getName() + "eating");
    }

    @Override
    public void breathe() {
        System.out.println("breathe");
    }
}
```
* is-a: inherit
* has-a:
* can: interface
```java
public interface CanFly {
    void fly();
}
```
```java
public abstract class Bird extends Animal implements CanFly {
    //constructor, 

    @Override
    public void fly() {
        System.out.println("flying");
    }
}
```

#### Protected keyword

### Interface vs Abstract Class
* Interface
   * unrelated classes 
   * behavior
   * separate different behavior

